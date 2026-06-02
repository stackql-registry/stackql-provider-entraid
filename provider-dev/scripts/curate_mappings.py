#!/usr/bin/env python3
"""
Curate the analyze-generated all_services.csv into a fully-mapped StackQL
manifest for the entra_id provider.

Microsoft Graph paths are OData-shaped. For every operation we derive:
  - stackql_resource_name : the navigation-collection chain (root dropped)
  - stackql_method_name   : a clean, unique-per-resource method name
  - stackql_verb          : select | insert | update | delete | replace | exec
  - stackql_object_key    : $.value ONLY when the response is a real collection

The object key is SCHEMA-DRIVEN: we resolve each GET's success response schema
and emit `$.value` only when that schema actually exposes a `value` array
(Graph collection responses do; single-valued navigation properties such as
`manager`/`createdOnBehalfOf`, and OData key-accessors like
`federatedIdentityCredentials(name='{name}')`, do not). This is essential:
stackql fails a SELECT if the object key points at a property the response
schema doesn't have.

OData noise that does not model relationally is dropped via the
`skip_this_resource` sentinel: type-cast projections (`graph.<type>`),
`$count`, and `$value` (binary) endpoints. Relationship `$ref` writes and
bound actions/functions are kept.
"""
import csv
import glob
import os
import re
from collections import defaultdict

import yaml

SRC_CSV = "provider-dev/config/all_services.csv"
SOURCE_DIR = "provider-dev/source"

ACTION_VERBS = {
    "assign", "unassign", "reset", "disable", "enable", "restore", "remove",
    "add", "revoke", "check", "validate", "get", "find", "activate",
    "deactivate", "retry", "cancel", "complete", "start", "stop", "lock",
    "unlock", "move", "copy", "send", "forward", "accept", "decline", "renew",
    "extend", "reprocess", "provision", "deprovision", "sync", "refresh",
    "set", "confirm", "record", "instantiate", "delta", "track", "query",
    "export", "import", "recalculate", "evaluate", "test", "ping", "verify",
    "wipe", "retire", "locate", "rotate", "generate", "issue", "redeem",
    "submit", "approve", "reject", "schedule", "calculate", "reauthorize",
    "store", "apply", "associate", "bulk", "clone", "create", "delete",
    "deny", "grant", "increment", "invite", "notify", "pause", "post",
    "preview", "publish", "purge", "reload", "render", "replace",
    "request", "rerun", "resume", "run", "save", "scrub", "share", "sign",
    "summarize", "suspend", "swap", "terminate", "unblock", "unfollow",
    "update", "upgrade", "upload", "use", "win",
}

CAMEL_RE = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def snake(s):
    s = s.replace("-", "_").replace(".", "_")
    s = CAMEL_RE.sub("_", s)
    s = re.sub(r"[^0-9a-zA-Z_]+", "_", s)
    return re.sub(r"_+", "_", s).strip("_").lower()


def is_key(seg):
    return seg.startswith("{") and seg.endswith("}")


def is_cast(seg):
    return seg.startswith("graph.") or seg.startswith("microsoft.graph.")


def leading_word(seg):
    m = re.match(r"[a-z]+", seg)
    return m.group(0) if m else ""


def is_action_seg(seg):
    return leading_word(seg) in ACTION_VERBS


# --- per-spec schema introspection (drives the object key) -------------------

class Spec:
    """Lazily-loaded source spec with response-schema resolution."""

    def __init__(self, path):
        self.doc = yaml.safe_load(open(path))
        self.paths = self.doc.get("paths", {}) or {}
        comps = self.doc.get("components", {}) or {}
        self.schemas = comps.get("schemas", {}) or {}
        self.responses = comps.get("responses", {}) or {}
        # every plain collection segment name appearing in any path
        self.collections = set()
        for p in self.paths:
            for seg in p.strip("/").split("/"):
                if not seg or is_key(seg) or is_cast(seg) or seg.startswith("$"):
                    continue
                base = seg.split("(")[0]
                if base:
                    self.collections.add(base)

    def _deref_schema(self, sch, depth=0):
        if not isinstance(sch, dict) or depth > 5:
            return sch
        if "$ref" in sch:
            key = sch["$ref"].split("/")[-1]
            return self._deref_schema(self.schemas.get(key, {}), depth + 1)
        return sch

    def _success_schema(self, path, verb):
        op = (self.paths.get(path) or {}).get(verb)
        if not isinstance(op, dict):
            return None
        responses = op.get("responses") or {}
        codes = sorted(c for c in responses if str(c).startswith("2"))
        if not codes:
            return None
        r = responses[codes[0]]
        if isinstance(r, dict) and "$ref" in r:
            r = self.responses.get(r["$ref"].split("/")[-1], {})
        content = (r or {}).get("content") or {}
        media = content.get("application/json") or (
            next(iter(content.values())) if content else None)
        if not media or "schema" not in media:
            return None
        return self._deref_schema(media["schema"])

    def response_has_value_array(self, path, verb):
        sch = self._success_schema(path, verb)
        if not isinstance(sch, dict):
            return False
        val = (sch.get("properties") or {}).get("value")
        return isinstance(val, dict) and val.get("type") == "array"

    def response_is_scalar(self, path, verb):
        """A primitive (non-row) success body — e.g. raw image/CSS bytes."""
        sch = self._success_schema(path, verb)
        if not isinstance(sch, dict):
            return False
        return sch.get("type") in ("string", "integer", "boolean", "number")


# --- path classification -----------------------------------------------------

def collections_of(segs):
    out = []
    for s in segs:
        if is_key(s) or is_cast(s) or s.startswith("$") or "(" in s:
            continue
        out.append(s)
    return out


def resource_from_chain(chain):
    if not chain:
        return None
    if len(chain) == 1:
        return snake(chain[0])
    return "_".join(snake(s) for s in chain[1:])


def item_verb(verb):
    return {"get": ("get", "select"), "patch": ("update", "update"),
            "put": ("replace", "replace"), "delete": ("delete", "delete"),
            "post": ("insert", "insert")}.get(verb, (snake(verb), "exec"))


def classify(path, verb, spec):
    """Return (resource, method, sqlverb, object_key) or (None,...) to skip."""
    raw = [s for s in path.strip("/").split("/") if s != ""]
    if not raw:
        return None, None, None, None
    if any(is_cast(s) for s in raw):
        return None, None, None, None
    last = raw[-1]
    if last in ("$count", "$value"):
        return None, None, None, None

    # GET returning a primitive (raw image/CSS bytes, etc.) is not a row set.
    if verb == "get" and spec.response_is_scalar(path, verb):
        return None, None, None, None

    has_value = spec.response_has_value_array(path, verb) if verb == "get" else False
    okey = "$.value" if has_value else ""

    # Relationship reference writes: /.../<collection>[/{id}]/$ref
    if last == "$ref":
        core = raw[:-1]
        if core and is_key(core[-1]):
            core = core[:-1]
        resource = resource_from_chain(collections_of(core))
        if not resource:
            return None, None, None, None
        if verb in ("post", "put"):
            return resource, "add_ref", "insert", ""
        if verb == "delete":
            return resource, "remove_ref", "delete", ""
        return None, None, None, None

    # Parenthesized segment: OData key-accessor vs bound function.
    paren_idx = next((i for i, s in enumerate(raw) if "(" in s), -1)
    if paren_idx != -1:
        seg = raw[paren_idx]
        base = seg.split("(")[0]
        tail = raw[paren_idx + 1:]
        if base in spec.collections and not tail:
            # key-accessor: behaves like <...>/<base>/{key}
            chain = collections_of(raw[:paren_idx]) + [base]
            resource = resource_from_chain(chain)
            if not resource:
                return None, None, None, None
            m, sv = item_verb(verb)
            return resource, m, sv, (okey if has_value else "")
        # bound function
        chain = collections_of(raw[:paren_idx])
        resource = resource_from_chain(chain) or snake(base)
        if verb == "get":
            return resource, snake(base), "select", okey
        return resource, snake(base), "exec", ""

    # Item-level operation: trailing key.
    if is_key(last):
        resource = resource_from_chain(collections_of(raw))
        if not resource:
            return None, None, None, None
        m, sv = item_verb(verb)
        return resource, m, sv, ""

    # Trailing bound action / function segment (no parens form).
    if verb == "post" and is_action_seg(last) and len(raw) >= 2:
        resource = resource_from_chain(collections_of(raw[:-1])) or snake(last)
        return resource, snake(last), "exec", ""
    if verb == "get" and is_action_seg(last) and len(raw) >= 2 and not has_value:
        # GET bound function returning a scalar/single (no value array)
        resource = resource_from_chain(collections_of(raw[:-1])) or snake(last)
        return resource, snake(last), "select", ""

    # Plain collection / navigation property.
    resource = resource_from_chain(collections_of(raw))
    if not resource:
        return None, None, None, None
    if verb == "get":
        # collection (value array) -> list ; single-valued nav prop -> get
        return resource, ("list" if has_value else "get"), "select", okey
    if verb == "post":
        return resource, "insert", "insert", ""
    if verb == "patch":
        return resource, "update", "update", ""
    if verb == "put":
        return resource, "replace", "replace", ""
    if verb == "delete":
        return resource, "delete", "delete", ""
    return resource, snake(verb), "exec", ""


def main():
    specs = {}
    for fp in glob.glob(os.path.join(SOURCE_DIR, "*.yaml")):
        specs[os.path.basename(fp)] = Spec(fp)

    rows = list(csv.DictReader(open(SRC_CSV)))
    fieldnames = list(rows[0].keys()) if rows else []

    for r in rows:
        spec = specs.get(r["filename"])
        verb = r["verb"].strip().lower()
        if spec is None:
            resource = None
        else:
            resource, method, sv, okey = classify(r["path"], verb, spec)
        if spec is None or resource is None:
            r["stackql_resource_name"] = "skip_this_resource"
            r["stackql_method_name"] = snake(r["operationId"]) or "op"
            r["stackql_verb"] = "exec"
            r["stackql_object_key"] = ""
        else:
            r["stackql_resource_name"] = resource
            r["stackql_method_name"] = method
            r["stackql_verb"] = sv
            r["stackql_object_key"] = okey

    # enforce unique (service, resource, method)
    seen = defaultdict(int)
    for r in rows:
        if r["stackql_resource_name"] == "skip_this_resource":
            continue
        key = (r["filename"], r["stackql_resource_name"], r["stackql_method_name"])
        seen[key] += 1
        if seen[key] > 1:
            r["stackql_method_name"] = f'{r["stackql_method_name"]}_{seen[key]}'

    with open(SRC_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    kept = [r for r in rows if r["stackql_resource_name"] != "skip_this_resource"]
    svc_res = defaultdict(set)
    for r in kept:
        svc_res[r["filename"]].add(r["stackql_resource_name"])
    verbs = defaultdict(int)
    okeys = 0
    for r in kept:
        verbs[r["stackql_verb"]] += 1
        if r["stackql_object_key"]:
            okeys += 1
    print(f"rows={len(rows)} kept={len(kept)} skipped={len(rows)-len(kept)}")
    print(f"services={len(svc_res)} resources={sum(len(v) for v in svc_res.values())}")
    print(f"object_keys($.value)={okeys}")
    print("verbs:", dict(verbs))


if __name__ == "__main__":
    main()
