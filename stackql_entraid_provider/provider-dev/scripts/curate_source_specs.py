#!/usr/bin/env python3
"""
Curate the split/normalized source specs (provider-dev/source/*.yaml) for a
SQL-friendly surface, BEFORE mapping generation. Run order:

    npm run split ... && npm run normalize ...
    python3 provider-dev/scripts/curate_source_specs.py      # this script
    npm run generate-mappings ...
    python3 provider-dev/scripts/curate_mappings.py
    npm run generate-provider ...
    python3 provider-dev/scripts/inject_pushdown_config.py
    python3 provider-dev/scripts/validate_provider.py

Two curations, both idempotent:

1. **snake_case path parameters.** Upstream Graph path params are wire-cased
   hybrids (`domainDnsRecord-id`, `appId`, `EndDateTime`); the split step only
   swapped `-` for `_` in the path *templates*, leaving the `- name:` parameter
   declarations dashed - so `{domainDnsRecord_id}` never matched its declared
   `domainDnsRecord-id` parameter, and none of the names were snake_case. Here
   both the `{...}` template placeholders in path keys and the `in: path`
   parameter declarations are renamed to full snake_case
   (`domain_dns_record_id`, `app_id`, `end_date_time`), so the SQL surface
   (SHOW METHODS required params, WHERE keys) is snake and template/declaration
   agree. Wire-literal text outside `{...}` (e.g. the `userPrincipalName=` in
   `/users(userPrincipalName='{user_principal_name}')`) is untouched - path
   param names never travel on the wire, only their values do. Query params
   (the OData `$`-options) and header params (`ConsistencyLevel`, `If-Match`)
   keep their wire names.

2. **De-require `@odata.type`.** The Graph `entity` base schema (and its allOf
   descendants) mark the low-level OData discriminator `@odata.type` as a
   REQUIRED property, which surfaces `data__@odata.type` as a required param on
   nearly every INSERT/UPDATE in SHOW METHODS / DESCRIBE / web docs. Graph only
   actually needs it for polymorphic creates (e.g. identity providers). It is
   stripped from every `required:` array (the property itself stays, so it can
   still be supplied explicitly when a polymorphic create needs it).

3. **Friendly `directoryObjectId` on `ReferenceCreate`.** The OData
   relationship ($ref) write body is `{"@odata.id": "https://graph.microsoft
   .com/v1.0/directoryObjects/<id>"}` - both the property name and the URL
   value are wire noise for a SQL user. A `directoryObjectId` (plain object
   id) property is added alongside `@odata.id` (camelCase, matching the wire
   casing kept for all properties); inject_pushdown_config.py adds a request
   transform to every add_ref method that renders the wire body from it
   (`@odata.id` remains usable as an explicit fallback).

Line-based processing (files reach 50 MB; a YAML round-trip is slow and
reorders keys). Both transforms rely on the uniform normalized style:
path keys as plain scalars at 2-space indent, `required:` arrays block-style
with items at key indent + 2.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent.parent / "source"

PLACEHOLDER_RE = re.compile(r"\{([^{}]+)\}")
PATH_KEY_RE = re.compile(r"^  (/[^ ].*):$")
PARAM_NAME_RE = re.compile(r"^(\s*)- name: (.+?)\s*$")
IN_RE = re.compile(r"^\s*in: (\w+)\s*$")
REQUIRED_KEY_RE = re.compile(r"^(\s*)required:\s*$")
ODATA_TYPE_ITEM = "@odata.type"

# ReferenceCreate augmentation: the exact upstream block ...
REFERENCE_CREATE_MATCH = (
    "    ReferenceCreate:\n"
    "      type: object\n"
    "      properties:\n"
    "        '@odata.id':\n"
    "          type: string\n"
)
# ... gains a SQL-friendly plain-object-id property. camelCase like every
# other body property (the provider keeps Graph wire casing for properties).
REFERENCE_CREATE_REPLACE = (
    "    ReferenceCreate:\n"
    "      type: object\n"
    "      properties:\n"
    "        '@odata.id':\n"
    "          type: string\n"
    "        directoryObjectId:\n"
    "          type: string\n"
    "          description: >-\n"
    "            The id of the directory object to reference (a user, group,\n"
    "            service principal, device, ...). Sent on the wire as\n"
    "            '@odata.id':\n"
    "            'https://graph.microsoft.com/v1.0/directoryObjects/{id}'.\n"
)
# migration: an earlier curation named the property snake_case
REFERENCE_CREATE_OLD_PROP = "        directory_object_id:\n"
REFERENCE_CREATE_NEW_PROP = "        directoryObjectId:\n"

# 4. Schema patches for upstream spec omissions: properties the live Graph
# service accepts/returns but Microsoft's published OpenAPI description omits.
# Without the declaration the local SQL table has no such column, so a SELECT
# of the property fails at projection even though the wire response carries it
# (all the more confusing since $select push-down happily requests it - the
# allowlist is a service-wide union). Each patch = (schema key line, property
# block inserted at the TOP of that schema's `properties:` map).
SCHEMA_PATCHES = [
    (
        "    microsoft.graph.servicePrincipal:\n",
        "        createdDateTime:\n"
        "          type: string\n"
        "          format: date-time\n"
        "          description: >-\n"
        "            The date and time the service principal was created.\n"
        "            Read-only. (Returned by the service but omitted from\n"
        "            Microsoft's published OpenAPI description; declared here\n"
        "            by curate_source_specs.py.)\n",
    ),
]


def apply_schema_patches(text: str) -> tuple[str, int]:
    n = 0
    for key, patch in SCHEMA_PATCHES:
        k = text.find(key)
        if k == -1:
            continue
        marker = "\n      properties:\n"
        p = text.find(marker, k)
        if p == -1:
            continue
        # the properties: line must belong to THIS schema - bail if another
        # 4-space schema key intervenes
        if any(ln.startswith("    ") and not ln.startswith("     ")
               for ln in text[k + len(key):p].splitlines()):
            continue
        insert_at = p + len(marker)
        if text[insert_at:insert_at + len(patch)] == patch:
            continue  # already patched
        text = text[:insert_at] + patch + text[insert_at:]
        n += 1
    return text, n


def snake(name: str) -> str:
    """wire-cased hybrid (kebab / camel / Pascal / mixed) -> snake_case."""
    s = name.replace("-", "_")
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"__+", "_", s)
    return s.lower()


def rename_path_key(line: str) -> str:
    m = PATH_KEY_RE.match(line.rstrip("\n"))
    if not m:
        return line
    key = m.group(1)
    new_key = PLACEHOLDER_RE.sub(lambda mm: "{" + snake(mm.group(1)) + "}", key)
    if new_key == key:
        return line
    return f"  {new_key}:\n"


def unquote(scalar: str) -> str:
    s = scalar.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1].replace("''", "'") if s[0] == "'" else s[1:-1]
    return s


def curate_file(path: Path) -> tuple[int, int, int]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out: list[str] = []
    n_paths = n_params = n_required = 0

    i = 0
    total = len(lines)
    while i < total:
        line = lines[i]

        # 1a. path key templates -> snake
        if line.startswith("  /"):
            new_line = rename_path_key(line)
            if new_line != line:
                n_paths += 1
            out.append(new_line)
            i += 1
            continue

        # 1b. `- name:` declarations for in: path -> snake
        pm = PARAM_NAME_RE.match(line)
        if pm:
            indent, raw_name = pm.group(1), pm.group(2)
            # find the `in:` of this parameter item (before the next list item
            # at the same indent or a dedent)
            loc = None
            j = i + 1
            while j < total:
                nxt = lines[j]
                if nxt.startswith(f"{indent}- ") or (
                    nxt.strip() and not nxt.startswith(f"{indent} ")
                ):
                    break
                im = IN_RE.match(nxt)
                if im:
                    loc = im.group(1)
                    break
                j += 1
            if loc == "path":
                name = unquote(raw_name)
                new_name = snake(name)
                if new_name != name:
                    n_params += 1
                    out.append(f"{indent}- name: {new_name}\n")
                    i += 1
                    continue
            out.append(line)
            i += 1
            continue

        # 2. strip '@odata.type' from required: arrays
        rm = REQUIRED_KEY_RE.match(line)
        if rm:
            indent = rm.group(1)
            item_prefix = f"{indent}  - "
            j = i + 1
            items: list[str] = []
            while j < total and lines[j].startswith(item_prefix):
                items.append(lines[j])
                j += 1
            kept = [
                it for it in items
                if unquote(it[len(item_prefix):].rstrip("\n")) != ODATA_TYPE_ITEM
            ]
            if len(kept) != len(items):
                n_required += 1
                if kept:  # keep the (pruned) block
                    out.append(line)
                    out.extend(kept)
                # else: drop the whole empty `required:` block
                i = j
                continue
            out.append(line)
            out.extend(items)
            i = j
            continue

        out.append(line)
        i += 1

    new_text = "".join(out)

    # 3. ReferenceCreate: add the friendly directoryObjectId property.
    # (Idempotency must test for the augmented block itself: similar names
    # also occur as renamed path params.) Also migrates the earlier
    # snake_cased augmentation in place.
    n_refcreate = 0
    if REFERENCE_CREATE_OLD_PROP in new_text:
        new_text = new_text.replace(
            REFERENCE_CREATE_OLD_PROP, REFERENCE_CREATE_NEW_PROP, 1)
        n_refcreate = 1
    elif (REFERENCE_CREATE_REPLACE not in new_text
            and REFERENCE_CREATE_MATCH in new_text):
        new_text = new_text.replace(
            REFERENCE_CREATE_MATCH, REFERENCE_CREATE_REPLACE, 1)
        n_refcreate = 1

    # 4. upstream spec-omission schema patches
    new_text, n_patches = apply_schema_patches(new_text)

    if n_paths or n_params or n_required or n_refcreate or n_patches:
        path.write_text(new_text, encoding="utf-8")
    return n_paths, n_params, n_required, n_refcreate + n_patches


def main() -> None:
    if not SOURCE_DIR.is_dir():
        raise SystemExit(f"source dir not found: {SOURCE_DIR}")
    files = sorted(SOURCE_DIR.glob("*.yaml"))
    if not files:
        raise SystemExit(f"no source YAMLs under {SOURCE_DIR}")

    tot_paths = tot_params = tot_required = tot_refcreate = 0
    for fp in files:
        n_paths, n_params, n_required, n_refcreate = curate_file(fp)
        tot_paths += n_paths
        tot_params += n_params
        tot_required += n_required
        tot_refcreate += n_refcreate
        if n_paths or n_params or n_required or n_refcreate:
            print(f"{fp.name}: {n_paths} path keys, {n_params} path params, "
                  f"{n_required} required-array strips, "
                  f"{n_refcreate} ReferenceCreate augmentations")

    print(f"\ntotal: {tot_paths} path keys renamed, {tot_params} path param "
          f"declarations renamed, {tot_required} required arrays stripped of "
          f"'@odata.type', {tot_refcreate} ReferenceCreate augmentations "
          f"({len(files)} files)")


if __name__ == "__main__":
    sys.exit(main())
