#!/usr/bin/env python3
"""
Inject per-service StackQL config into every generated service doc:

1. **OData query-param push-down** (`queryParamPushdown` under a top-level
   `x-stackQL-config`). Honoured by stackql/any-sdk at the Method / Resource /
   Service / ProviderService / Provider inheritance levels, but provider-level
   config in `provider.yaml` is NOT propagated to operation stores built from
   the separately `$ref`'d service docs during registry load, so service level
   it is (one block per service file rather than per resource).

   The provider keeps the GRAPH WIRE CASING for columns and body properties
   (camelCase, e.g. `displayName`), so the raw SQL identifiers that stackql's
   push-down emits (v0.10.542 does no identifier re-casing) are exactly the
   wire property names Graph accepts in `$select` / `$filter` / `$orderby`.
   This is a deliberate trade-off: snake_case response aliases
   (`snake_case_aliases`) would break column-bearing push-down
   (`$select=display_name` 400s the whole call) and - worse - projection
   queries would silently lose data (without `$select`, Graph returns only
   its DEFAULT property subset, so non-default columns come back null). Wire
   casing preserves full push-down fidelity. Path params ARE snake_cased
   (curate_source_specs.py) - they never travel on the wire by name, and
   Graph's kebab forms (`application-id`) are unusable unquoted in SQL.

   The column-bearing options (`select` / `filter` / `orderBy`) carry a
   `supportedColumns` allowlist = the service's ACTUAL schema property names
   (harvested from every `properties:` map in the doc, `@odata.*` excluded).
   Purpose: push-down extracts predicates from the raw WHERE clause, INCLUDING
   keys that were consumed as OPERATION PARAMS during routing - without the
   allowlist, `WHERE user_id = 'x'` (a by-id get) also emits
   `$filter=user_id eq 'x'` onto the single-entity URL (Graph rejects $filter
   there), and `WHERE ConsistencyLevel = 'eventual'` would leak into $filter
   too. Property names are pushable; param names are not.

   `skip` is NOT configured: Microsoft Graph does not support `$skip` on
   directory objects ("'$skip' is not supported by the service", HTTP 400 -
   it offers cursor paging via @odata.nextLink instead). SQL OFFSET therefore
   stays a client-side primitive, which is always correct: stackql follows
   nextLink pagination, so the full row set is available locally regardless
   of what was pushed. `top` IS configured ($top bounds the page size; the
   nextLink loop keeps overall results correct and the global http.pageLimit
   applies as usual).

2. **`request.nativeCasing: camel` on every x-stackQL-resources method.**
   Input tolerance only, invisible in SHOW / DESCRIBE / docs (those show wire
   names): any-sdk's reverse-casing resolution (stackql >= v0.10.542) lets a
   snake_case input key (`data__display_name`) also resolve to its camelCase
   wire parameter / request-body property during method routing and request
   construction. The loader auto-fills mediaType/schema for body-bearing ops;
   on body-less GETs the block is metadata-only.

3. **`request.transform` on every `add_ref` method.** OData relationship
   ($ref) writes take the body `{"@odata.id": "https://graph.microsoft.com/
   v1.0/directoryObjects/<id>"}` - unfriendly in SQL both as a column name
   and as a value. curate_source_specs.py adds a plain `directoryObjectId`
   property to the shared `ReferenceCreate` schema; the transform injected
   here (golang_template_json_v0.1.0, applied by any-sdk in place of plain
   JSON marshalling) renders the wire body from it, falling back to a
   verbatim `@odata.id` when that is what was supplied:
       INSERT INTO entra_id.groups.members (group_id, directoryObjectId)
       SELECT '<group-id>', '<user-object-id>';
   -> POST .../members/$ref  {"@odata.id": ".../directoryObjects/<id>"}

`generate-provider` overwrites the service docs, so run this AFTER it (and
after `curate_mappings.py`), as the last step before `validate_provider.py`.

Idempotent: files that already carry a top-level `x-stackQL-config` are
skipped entirely. Insertion is line-based (these files reach tens of MB; a
full YAML round-trip would be slow and could reorder keys).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

try:
    YamlLoader = yaml.CSafeLoader
except AttributeError:  # no libyaml bindings
    YamlLoader = yaml.SafeLoader

SERVICES_DIR = (
    Path(__file__).resolve().parent.parent
    / "openapi" / "src" / "entra_id" / "v00.00.00000" / "services"
)

MARKER = "x-stackQL-config:"

METHOD_KEY_RE = re.compile(r"^        ([A-Za-z0-9_]+):$")


def harvest_property_names(text: str) -> list[str]:
    """Every schema property name in the doc (each key of every `properties:`
    map under components.schemas), excluding the `@odata.*` primitives. These
    are the identifiers safe to emit in $select/$filter/$orderby."""
    doc = yaml.load(text, Loader=YamlLoader)
    props: set[str] = set()

    def walk(node) -> None:
        if isinstance(node, dict):
            p = node.get("properties")
            if isinstance(p, dict):
                props.update(k for k in p if isinstance(k, str))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk((doc.get("components") or {}).get("schemas") or {})
    return sorted(p for p in props if not p.startswith("@"))


def build_config_block(supported_columns: list[str]) -> str:
    # single-quote every entry: bare `on` / `no` / `true` etc. would otherwise
    # parse as YAML booleans and break []string unmarshalling
    cols = "[" + ", ".join(f"'{c}'" for c in supported_columns) + "]"
    return (
        "x-stackQL-config:\n"
        "  queryParamPushdown:\n"
        "    select:\n"
        "      dialect: odata\n"
        f"      supportedColumns: {cols}\n"
        "    filter:\n"
        "      dialect: odata\n"
        f"      supportedColumns: {cols}\n"
        "    orderBy:\n"
        "      dialect: odata\n"
        f"      supportedColumns: {cols}\n"
        "    top:\n"
        "      dialect: odata\n"
        "    count:\n"
        "      dialect: odata\n"
    )

REQUEST_BLOCK = "          request:\n            nativeCasing: camel\n"

# add_ref methods additionally carry the $ref body transform: render
# {"@odata.id": ".../directoryObjects/<id>"} from the friendly
# directoryObjectId property (fall back to a verbatim @odata.id; stackql
# splits the dotted SQL identifier "@odata.id" into a NESTED body map
# {"@odata": {"id": ...}}, so the fallback reads that shape).
REF_TEMPLATE = (
    '{{ if safeIndex . "directoryObjectId" }}'
    '{"@odata.id": "https://graph.microsoft.com/v1.0/directoryObjects/'
    '{{ safeIndex . "directoryObjectId" }}"}'
    '{{ else }}{{ with safeIndex . "@odata" }}'
    '{"@odata.id": "{{ index . "id" }}"}'
    '{{ else }}{}{{ end }}{{ end }}'
)
ADD_REF_REQUEST_BLOCK = (
    "          request:\n"
    "            nativeCasing: camel\n"
    "            transform:\n"
    "              type: golang_template_json_v0.1.0\n"
    f"              body: '{REF_TEMPLATE}'\n"
)


def inject_native_casing(lines: list[str]) -> tuple[list[str], int]:
    """Insert a request block after every method key inside the
    x-stackQL-resources methods sections. Returns (new_lines, count)."""
    out: list[str] = []
    injected = 0
    in_resources = False
    in_methods = False
    for idx, line in enumerate(lines):
        out.append(line)
        stripped = line.rstrip("\n")
        if stripped == "  x-stackQL-resources:":
            in_resources = True
            in_methods = False
            continue
        if in_resources:
            # leaving the resources block (a column-0 or 2-space sibling key)
            if stripped and not line.startswith("   ") and not stripped.startswith("  x-stackQL"):
                in_resources = False
                in_methods = False
                continue
            if stripped == "      methods:":
                in_methods = True
                continue
            # any other 6-space (or shallower) key ends the methods section
            if in_methods and stripped and not line.startswith("        "):
                in_methods = False
                continue
            if in_methods:
                m = METHOD_KEY_RE.match(stripped)
                if m:
                    nxt = lines[idx + 1] if idx + 1 < len(lines) else ""
                    if nxt.rstrip("\n") != "          request:":
                        block = (ADD_REF_REQUEST_BLOCK
                                 if m.group(1).startswith("add_ref")
                                 else REQUEST_BLOCK)
                        out.append(block)
                        injected += 1
    return out, injected


def inject(path: Path) -> tuple[bool, int]:
    """Inject the config block and per-method request blocks.
    Returns (modified, methods_injected)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    if any(line.startswith(MARKER) for line in lines):
        return False, 0  # already present

    config_block = build_config_block(harvest_property_names(text))

    lines, n_methods = inject_native_casing(lines)

    for i, line in enumerate(lines):
        if line.startswith("paths:"):  # first column-0 `paths:`
            block = config_block if lines[i - 1].endswith("\n") else "\n" + config_block
            lines.insert(i, block)
            path.write_text("".join(lines), encoding="utf-8")
            return True, n_methods

    raise SystemExit(f"no top-level 'paths:' found in {path.name}; cannot inject config")


def main() -> None:
    if not SERVICES_DIR.is_dir():
        raise SystemExit(f"services dir not found: {SERVICES_DIR}")
    service_files = sorted(SERVICES_DIR.glob("*.yaml"))
    if not service_files:
        raise SystemExit(f"no service YAMLs under {SERVICES_DIR}")

    changed = skipped = methods = 0
    for path in service_files:
        modified, n_methods = inject(path)
        if modified:
            changed += 1
            methods += n_methods
            print(f"injected: {path.name} ({n_methods} methods)")
        else:
            skipped += 1
    print(f"\n{changed} injected ({methods} method request blocks), "
          f"{skipped} already had config ({len(service_files)} services)")


if __name__ == "__main__":
    sys.exit(main())
