#!/usr/bin/env python3
"""
Inject the OData query-param push-down config into every generated service doc.

Push-down config (`queryParamPushdown`) is honoured by stackql/any-sdk at the
Method / Resource / Service / ProviderService / Provider inheritance levels.
Provider-level config in `provider.yaml` is NOT propagated to operation stores
built from the separately `$ref`'d service docs during registry load, so a
provider-level block is a no-op in practice. **Service level works** and is one
block per service file (39) rather than per resource (858), so we inject a
top-level `x-stackQL-config` extension into each service YAML.

`generate-provider` overwrites the service docs, so run this AFTER it (and after
`curate_mappings.py`), as the last step before `validate_provider.py`.

Idempotent: files that already carry a top-level `x-stackQL-config` are skipped.
Insertion is line-based (these files reach tens of MB; a full YAML round-trip
would be slow and could reorder keys) - the block is inserted immediately before
the first top-level `paths:` line, which every generated service doc has.

Every Microsoft Graph resource is OData, so the same all-options block applies
uniformly. `dialect: odata` gives the standard param names/rendering
($select / $filter / $orderby / $top / $skip / $count); empty supported-column /
operator lists mean "all supported" (push-down is best-effort, so Graph rejecting
a specific shape is a per-query concern, not a config one).
"""

from __future__ import annotations

import sys
from pathlib import Path

SERVICES_DIR = (
    Path(__file__).resolve().parent.parent
    / "openapi" / "src" / "entra_id" / "v00.00.00000" / "services"
)

MARKER = "x-stackQL-config:"

# Top-level extension block. Two-space indented under the (column-0) key.
CONFIG_BLOCK = """\
x-stackQL-config:
  queryParamPushdown:
    select:
      dialect: odata
    filter:
      dialect: odata
    orderBy:
      dialect: odata
    top:
      dialect: odata
    skip:
      dialect: odata
    count:
      dialect: odata
"""


def inject(path: Path) -> bool:
    """Insert the config block before the first top-level `paths:` line.
    Returns True if the file was modified."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)

    if any(line.startswith(MARKER) for line in lines):
        return False  # already present

    for i, line in enumerate(lines):
        if line.startswith("paths:"):  # first column-0 `paths:`
            block = CONFIG_BLOCK if lines[i - 1].endswith("\n") else "\n" + CONFIG_BLOCK
            lines.insert(i, block)
            path.write_text("".join(lines), encoding="utf-8")
            return True

    raise SystemExit(f"no top-level 'paths:' found in {path.name}; cannot inject config")


def main() -> None:
    if not SERVICES_DIR.is_dir():
        raise SystemExit(f"services dir not found: {SERVICES_DIR}")
    service_files = sorted(SERVICES_DIR.glob("*.yaml"))
    if not service_files:
        raise SystemExit(f"no service YAMLs under {SERVICES_DIR}")

    changed = skipped = 0
    for path in service_files:
        if inject(path):
            changed += 1
            print(f"injected: {path.name}")
        else:
            skipped += 1
    print(f"\n{changed} injected, {skipped} already had config "
          f"({len(service_files)} services)")


if __name__ == "__main__":
    sys.exit(main())
