#!/usr/bin/env python3
"""
Post-docgen curation of the generated web docs (website/docs/services/**).
Run AFTER `npm run generate-docs`. Idempotent.

The docgen in @stackql/provider-utils renders the provider spec verbatim, which
surfaces OData wire plumbing the runtime abstracts away from SQL users:

1. **OData query-option params are suppressed** ($top / $skip / $search /
   $filter / $count / $orderby / $select / $expand and the `@id` $ref
   primitive) from the Methods table's optional-params cells, the Parameters
   table, and the WHERE clauses of the SQL examples. SQL primitives translate
   to these on the wire via the injected `queryParamPushdown` config
   (projection -> $select, WHERE -> $filter, ORDER BY -> $orderby,
   LIMIT -> $top, OFFSET -> $skip, COUNT(*) -> $count), so documenting them as
   WHERE-clause params is noise. (They remain usable in a WHERE clause for
   power users - e.g. `$search` / `$expand`, which have no SQL equivalent -
   they are just no longer documented.) Header params (`ConsistencyLevel`,
   `If-Match`) are kept: they are real, occasionally-required upstream knobs
   (e.g. `WHERE ConsistencyLevel = 'eventual'` for Graph advanced queries).

2. **`@odata.type` rows/lines are dropped** from field tables and examples -
   a low-level OData discriminator, no longer a required body attribute
   (de-required at build time by curate_source_specs.py).

3. **Trailing slashes are stripped from internal `/services/...` links** (the
   service-index and resource-index anchor grids). The site is built with
   `trailingSlash: false`, so pages are emitted as flat `.html` files and
   GitHub Pages serves the slashed URL as a 404 (the SPA recovers on
   hydration, but each click flashes "Page Not Found" and returns HTTP 404
   to crawlers). These are raw `<a>` tags, so Docusaurus's broken-link
   checker never sees them.

Column and body-property names are left in their Graph wire casing
(camelCase) - that is the SQL surface (see inject_pushdown_config.py for the
rationale: raw-identifier push-down fidelity). Path params are snake_case in
the spec itself, so they render correctly without any doc-side rewriting.

This is a post-docgen script (not wired into the docgen tool) because the
OData-isms are a Graph/OData edge case, not a provider-utils concern.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# The whole docs tree, not just services/: the provider intro page
# (docs/index.md) carries the same slashed /services/ links.
DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "website" / "docs"

# OData query-option params to suppress from docs.
ODATA_PARAMS = {"$top", "$skip", "$search", "$filter", "$count", "$orderby",
                "$select", "$expand", "@id"}

BARE_COL_RE = re.compile(r"^([A-Za-z@][A-Za-z0-9_.@]*)(,?)$")
ASSIGN_RE = re.compile(r"^(\s*(?:AND |WHERE )?)([A-Za-z@$][A-Za-z0-9_.@$-]*)( = )")
MANIFEST_NAME_RE = re.compile(r"^(\s*- name: )([A-Za-z@][A-Za-z0-9_.@]*)\s*$")


def strip_odata_param_links(cell: str) -> str:
    """Remove suppressed-param <a> items from a comma-joined params cell."""
    items = [it.strip() for it in cell.split(", ")]
    kept = []
    for it in items:
        m = re.search(r"<code>([^<]+)</code>", it)
        if m and m.group(1) in ODATA_PARAMS:
            continue
        kept.append(it)
    return ", ".join(kept)


def transform_tables_and_links(text: str) -> str:
    # drop @odata.type field rows (<tr> ... code="@odata.type" ... </tr>)
    text = re.sub(
        r"<tr>\s*<td><CopyableCode code=\"@odata\.type\" /></td>.*?</tr>\n?",
        "", text, flags=re.DOTALL)
    # drop suppressed-param rows from the Parameters table
    for p in ODATA_PARAMS:
        text = re.sub(
            r"<tr id=\"parameter-" + re.escape(p).replace(r"\$", r"\$") +
            r"\">.*?</tr>\n?",
            "", text, flags=re.DOTALL)
    # strip suppressed params from method-table cells (any <td> containing
    # parameter links)
    def cell_fix(m: re.Match) -> str:
        return "<td>" + strip_odata_param_links(m.group(1)) + "</td>"
    text = re.sub(r"<td>((?:<a href=\"#parameter-[^\"]+\"><code>[^<]+</code></a>(?:, )?)+)</td>",
                  cell_fix, text)
    # strip trailing slashes from internal /services/ links (trailingSlash:
    # false site - the slashed form 404s on GitHub Pages)
    text = re.sub(r"(href=\"/services/[^\"]+)/\"", r'\1"', text)
    return text


def transform_example_lines(text: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    in_code = False
    skip_manifest_prop = False
    manifest_indent = ""

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```") or "<CodeBlock" in line or "`}</CodeBlock>" in line:
            in_code = stripped.startswith("```sql") or "<CodeBlock" in line
            skip_manifest_prop = False
            out.append(line)
            continue
        if not in_code:
            out.append(line)
            continue

        # manifest prop skipping (name + value + description block)
        mn = MANIFEST_NAME_RE.match(line)
        if skip_manifest_prop:
            if mn or stripped.startswith("- name:"):
                skip_manifest_prop = False  # fall through to normal handling
            elif line.startswith(manifest_indent + " ") or stripped in ("",):
                continue  # still inside the skipped prop block
            else:
                skip_manifest_prop = False
        if mn and mn.group(2).startswith("@odata."):
            skip_manifest_prop = True
            manifest_indent = re.match(r"^\s*", line).group(0)
            continue

        # drop @odata.* lines in SQL examples (column lists, value lists,
        # assignments, WHERE terms)
        if ("@odata." in line
                and ("{{" in line or BARE_COL_RE.match(stripped))):
            continue

        # suppressed OData params in WHERE clauses
        am = ASSIGN_RE.match(line)
        if am and am.group(2) in ODATA_PARAMS:
            continue

        out.append(line)

    text = "\n".join(out)
    # fix dangling commas produced by dropped lines: `x,` directly before a
    # closer line
    text = re.sub(r",(\n(?:\)|RETURNING|FROM |;))", r"\1", text)
    return text


def fix_where_leading_and(text: str) -> str:
    """If a WHERE's first term was removed, promote the next AND to WHERE."""
    return re.sub(r"(WHERE\s*\n)AND ", r"\1", text)


def curate(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = transform_tables_and_links(original)
    text = transform_example_lines(text)
    text = fix_where_leading_and(text)
    if text != original:
        # pin LF so a run under Windows Python doesn't CRLF-flip the tree
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> None:
    if not DOCS_DIR.is_dir():
        raise SystemExit(f"docs dir not found: {DOCS_DIR} (run generate-docs first)")
    pages = sorted(DOCS_DIR.rglob("index.md"))
    changed = sum(1 for p in pages if curate(p))
    print(f"curated {changed} of {len(pages)} doc pages")


if __name__ == "__main__":
    sys.exit(main())
