#!/usr/bin/env python3
"""
Curate the analyze-generated all_services.csv into a fully-mapped StackQL
manifest for the entra_id provider.

all_services.csv is the MASTER record of every operation's mapping. On each run
an operation that already has a stackql_resource_name recorded is PRESERVED
verbatim - the rules below never re-map it - so the provider's resource / method
/ verb surface is stable across versions (no accidental breaking changes when the
classification code evolves). Only operations with no recorded mapping (new to
the spec) are classified by the rules and written back into the master for next
time. To (re)master an operation deliberately, blank its stackql_* columns (or
hand-edit them) and re-run.

For a new (unmastered) operation the rules derive, from its OData-shaped path:
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
    # lifecycle/action verbs that head bound actions on directory resources
    "unset", "dismiss", "force", "promote", "subscribe", "unsubscribe",
    "acquire", "restart", "translate",
}

# Read/lookup verbs: a bound *function* headed by one of these returns data for a
# supplied key (findTenantInformationByDomainName(domainName='x')) and reads
# naturally as a SELECT, so it stays its own queryable resource rather than being
# folded to an exec lifecycle op like a mutating action.
READ_FUNCTION_VERBS = {"find", "query", "track"}

# Explicit, hand-curated exec folds: re-home a whole curated resource onto a
# parent resource as exec method(s). These are settable singletons (logo, branding
# images/css), bound actions whose path shape does not reduce to the desired
# parent mechanically (synchronization <schema>/directories/discover,
# parseExpression), $ref-only residue resources, and container nav-properties -
# all of which read better as lifecycle ops on a higher-level parent than as their
# own (mostly non-selectable) resource. Keyed by (service_file, resource_name);
# value is the parent resource in that same service.
EXEC_FOLD = {
    ("applications.yaml", "logo"): "applications",
    ("applications.yaml", "synchronization_jobs_schema_directories_discover"): "synchronization_jobs",
    ("applications.yaml", "synchronization_jobs_schema_parse_expression"): "synchronization_jobs",
    ("applications.yaml", "synchronization_secrets"): "synchronization",
    ("applications.yaml", "synchronization_templates_schema_directories_discover"): "synchronization_templates",
    ("applications.yaml", "synchronization_templates_schema_parse_expression"): "synchronization_templates",
    ("identity.yaml", "b2x_user_flows_api_connector_configuration_post_attribute_collection"): "b2x_user_flows",
    ("identity.yaml", "b2x_user_flows_api_connector_configuration_post_federation_signup"): "b2x_user_flows",
    ("identity.yaml", "conditional_access"): "identity",
    ("organization.yaml", "branding_background_image"): "branding",
    ("organization.yaml", "branding_banner_logo"): "branding",
    ("organization.yaml", "branding_custom_css"): "branding",
    ("organization.yaml", "branding_favicon"): "branding",
    ("organization.yaml", "branding_header_logo"): "branding",
    ("organization.yaml", "branding_localizations_background_image"): "branding_localizations",
    ("organization.yaml", "branding_localizations_banner_logo"): "branding_localizations",
    ("organization.yaml", "branding_localizations_custom_css"): "branding_localizations",
    ("organization.yaml", "branding_localizations_favicon"): "branding_localizations",
    ("organization.yaml", "branding_localizations_header_logo"): "branding_localizations",
    ("organization.yaml", "branding_localizations_square_logo"): "branding_localizations",
    ("organization.yaml", "branding_localizations_square_logo_dark"): "branding_localizations",
    ("organization.yaml", "branding_square_logo"): "branding",
    ("organization.yaml", "branding_square_logo_dark"): "branding",
    ("service_principals.yaml", "synchronization_jobs_schema_directories_discover"): "synchronization_jobs",
    ("service_principals.yaml", "synchronization_jobs_schema_parse_expression"): "synchronization_jobs",
    ("service_principals.yaml", "synchronization_secrets"): "synchronization",
    ("service_principals.yaml", "synchronization_templates_schema_directories_discover"): "synchronization_templates",
    ("service_principals.yaml", "synchronization_templates_schema_parse_expression"): "synchronization_templates",
    ("users.yaml", "change_password"): "users",
}

_GENERIC_METHODS = {"insert", "update", "replace", "delete", "get", "list", "create"}

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
        # every plain collection segment name appearing in any path. Skip
        # parenthesized segments (bound functions like getManagedAppPolicies() and
        # OData key-accessors): a function name must NOT register as a collection,
        # or a later `X()` is misread as a key-accessor of a collection `X` and
        # becomes its own resource. Real keyed collections (e.g.
        # federatedIdentityCredentials) still register from their plain `/X` path.
        self.collections = set()
        for p in self.paths:
            for seg in p.strip("/").split("/"):
                if (not seg or is_key(seg) or is_cast(seg)
                        or seg.startswith("$") or "(" in seg):
                    continue
                self.collections.add(seg)

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


def item_key_param(spec, collection_prefix):
    """The key param name of a collection's canonical item path
    (`/devices/{device_id}` -> `device_id`), or None if there is none."""
    want_depth = collection_prefix.count("/") + 1
    for p in spec.paths:
        if (p.startswith(collection_prefix + "/{") and p.endswith("}")
                and p.count("/") == want_depth):
            return p[len(collection_prefix) + 2:-1]
    return None


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
    # SharePoint `sites` subtree is a productivity workload outside the entra_id
    # identity/directory scope. Leave it in the source spec but do not surface it
    # (or its nested getByPath()/getActivitiesByInterval() function chains) as a
    # resource.
    if any(s.split("(")[0] == "sites" for s in raw):
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

    # A single-valued navigation property whose trailing segment is an action/verb
    # phrase (bulkUpload, batchRecordDecisions, postAttributeCollection, ...) is a
    # lifecycle operation on the parent, not a queryable sub-resource. Route every
    # verb to `exec` on the parent so a GET does not become a `select` that collides
    # with the parent's item `get` (same required path keys), and writes do not
    # spawn a write-only sub-resource. The single-valued guard (GET exposes no
    # `value` array) keeps real collections whose name happens to start with an
    # action word - e.g. signIns - as normal list/select resources. `$value` media
    # content is already dropped by the `$count`/`$value` guard above.
    if (len(raw) >= 2 and not is_key(last) and "(" not in last
            and (is_action_seg(last) or leading_word(last) == "batch")
            and not spec.response_has_value_array(path, "get")):
        parent = resource_from_chain(collections_of(raw[:-1])) or snake(last)
        prefix = {"get": "get_", "post": "", "patch": "update_",
                  "put": "replace_", "delete": "delete_"}.get(verb, snake(verb) + "_")
        return parent, f"{prefix}{snake(last)}", "exec", ""

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
            # An alternate-key accessor whose (snake_cased) parameter collides
            # with the canonical item path's key param is unroutable: two
            # SELECT methods on the resource with identical required-param
            # signatures (e.g. /devices/{device_id} vs
            # /devices(deviceId='{device_id}')). Keep the canonical get; skip
            # the accessor. Non-colliding accessors (appId, uniqueName,
            # userPrincipalName, roleTemplateId, name, ...) are kept.
            acc_param = re.search(r"\{([^{}]+)\}", seg)
            collection_prefix = "/" + "/".join(raw[:paren_idx] + [base])
            if acc_param and acc_param.group(1) == item_key_param(
                    spec, collection_prefix):
                return None, None, None, None
            m, sv = item_verb(verb)
            return resource, m, sv, (okey if has_value else "")
        # bound function
        chain = collections_of(raw[:paren_idx])
        base_snake = snake(base)
        # get* data-retrieval functions (getManagedAppPolicies(),
        # getTeamsLicensingDetails(), ...) are their own queryable resource, named
        # after the function with the leading `get_` dropped - so
        # entra_id.users.get_managed_app_policies becomes
        # entra_id.users.managed_app_policies. The parent chain is not prefixed
        # (these read like top-level reports of the service).
        if base_snake == "get" or base_snake.startswith("get_"):
            # Deeply-nested report functions (>2 collections deep, e.g.
            # b2xUserFlows/{id}/userAttributeAssignments/getOrder()) are too niche
            # to surface as a top-level resource; leave them in the source spec
            # only. The wanted reports sit 1-2 deep (users/{id}/getManagedAppPolicies,
            # users/{id}/licenseDetails/getTeamsLicensingDetails).
            if len(chain) > 2:
                return None, None, None, None
            resource = base_snake[4:] if base_snake.startswith("get_") else base_snake
            resource = resource or base_snake
            if verb == "get":
                return resource, "get", "select", okey
            return resource, base_snake, "exec", ""
        # scalar-returning action functions (exportDeviceAndAppManagementData())
        # are lifecycle operations -> exec on the parent. The `not has_value` guard
        # keeps collection-returning functions (delta(), filterByCurrentUser(), ...)
        # queryable; read/lookup verbs (find/query/track, e.g.
        # findTenantInformationByDomainName()) stay their own SELECT resources
        # rather than being demoted to exec.
        if (is_action_seg(base) and not has_value
                and leading_word(base) not in READ_FUNCTION_VERBS):
            parent = resource_from_chain(chain) or base_snake
            return parent, base_snake, "exec", ""
        # any other bound function -> its OWN queryable resource, named with the
        # full nav chain so it never collides with the parent's get/list (this is
        # the long-standing behaviour for delta(), filterByCurrentUser(),
        # <schema>/filterOperators(), <policy>/usage(), etc.).
        resource = resource_from_chain(chain + [base]) or base_snake
        if verb == "get":
            return resource, "get", "select", okey
        return resource, base_snake, "exec", ""

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
        # A direct create POST paired with a sibling `<collection>/$ref` POST (the
        # reference-link write, classified as `add_ref`) both map to `insert` with
        # the same signature and collide. Emulate the Terraform azuread provider -
        # directory membership / assignment = link an EXISTING object by reference -
        # by keeping the $ref write as the canonical INSERT and demoting the
        # inline-create to an exec method (non-lossy).
        ref_ops = spec.paths.get(path.rstrip("/") + "/$ref") or {}
        if isinstance(ref_ops, dict) and "post" in ref_ops:
            return resource, f"create_{snake(last)}", "exec", ""
        return resource, "insert", "insert", ""
    if verb == "patch":
        return resource, "update", "update", ""
    if verb == "put":
        return resource, "replace", "replace", ""
    if verb == "delete":
        return resource, "delete", "delete", ""
    return resource, snake(verb), "exec", ""


STACKQL_COLS = (
    "stackql_resource_name", "stackql_method_name", "stackql_verb",
    "stackql_object_key",
)


def classify_row(r, specs):
    """Fill a single row's stackql_* mapping from the classification rules
    (used only for operations not already mastered in all_services.csv)."""
    spec = specs.get(r["filename"])
    verb = r["verb"].strip().lower()
    resource = None
    if spec is not None:
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


def main():
    specs = {}
    for fp in glob.glob(os.path.join(SOURCE_DIR, "*.yaml")):
        specs[os.path.basename(fp)] = Spec(fp)

    rows = list(csv.DictReader(open(SRC_CSV)))
    fieldnames = list(rows[0].keys()) if rows else []
    for c in STACKQL_COLS:
        if c not in fieldnames:
            fieldnames.append(c)
    for r in rows:
        for c in STACKQL_COLS:
            if r.get(c) is None:
                r[c] = ""

    # all_services.csv is the MASTER record of every operation's mapping
    # (resource / method / verb / object_key), keyed by operationId via its row.
    # A row that already carries a stackql_resource_name was mastered on a prior
    # run: PRESERVE it verbatim so a change to the rules below can never re-route
    # an existing operation - guaranteeing no breaking changes to the provider
    # surface between versions. Only operations with no recorded mapping (new to
    # the spec) are classified here and written back into the master for next run.
    new_rows = [r for r in rows if not (r.get("stackql_resource_name") or "").strip()]
    new_ids = {id(r) for r in new_rows}

    for r in new_rows:
        classify_row(r, specs)

    # hand-curated exec folds apply to newly-classified rows only; existing folds
    # are already frozen in the master and are left untouched.
    for r in new_rows:
        parent = EXEC_FOLD.get((r["filename"], r["stackql_resource_name"]))
        if parent is None:
            continue
        old = r["stackql_resource_name"]
        remainder = old[len(parent) + 1:] if old.startswith(parent + "_") else old
        orig = r["stackql_method_name"]
        r["stackql_resource_name"] = parent
        r["stackql_method_name"] = remainder if orig in _GENERIC_METHODS else f"{remainder}_{orig}"
        r["stackql_verb"] = "exec"
        r["stackql_object_key"] = ""

    # enforce unique (service, resource, method) for NEW methods only: seed the
    # counts from the mastered rows so a new operation is renamed around an
    # existing method rather than the existing one ever changing.
    seen = defaultdict(int)
    for r in rows:
        if r["stackql_resource_name"] == "skip_this_resource" or id(r) in new_ids:
            continue
        seen[(r["filename"], r["stackql_resource_name"], r["stackql_method_name"])] += 1
    for r in new_rows:
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
    print(f"rows={len(rows)} preserved={len(rows) - len(new_rows)} "
          f"newly_classified={len(new_rows)}")
    print(f"kept={len(kept)} skipped={len(rows) - len(kept)}")
    print(f"services={len(svc_res)} resources={sum(len(v) for v in svc_res.values())}")


if __name__ == "__main__":
    main()
