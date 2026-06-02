#!/usr/bin/env python3
"""Structural validation of the generated entra_id provider.

For every service file: parse YAML, then verify that each
x-stackQL-resources method's operation.$ref resolves to a real path+verb,
that the referenced response openAPIDocKey exists, and that every sqlVerbs
$ref points to a defined method.
"""
import glob
import os
import sys
import urllib.parse

import yaml

ROOT = "provider-dev/openapi/src/entra_id/v00.00.00000"


def deref_pointer(doc, ref):
    assert ref.startswith("#/")
    node = doc
    for raw in ref[2:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        if isinstance(node, list):
            node = node[int(token)]
        else:
            if token not in node:
                return None
            node = node[token]
    return node


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "services", "*.yaml")))
    total_res = total_meth = errors = 0
    for fp in files:
        with open(fp) as f:
            doc = yaml.safe_load(f)
        svc = os.path.basename(fp)
        res = doc.get("components", {}).get("x-stackQL-resources", {})
        for rname, r in res.items():
            total_res += 1
            methods = r.get("methods", {})
            for mname, m in methods.items():
                total_meth += 1
                ref = m.get("operation", {}).get("$ref")
                if not ref:
                    print(f"  [ERR] {svc}:{rname}.{mname} missing operation.$ref")
                    errors += 1
                    continue
                op = deref_pointer(doc, ref)
                if op is None:
                    print(f"  [ERR] {svc}:{rname}.{mname} unresolved $ref {ref}")
                    errors += 1
                    continue
                dk = str(m.get("response", {}).get("openAPIDocKey", ""))
                if dk and dk not in (op.get("responses", {}) or {}):
                    print(f"  [ERR] {svc}:{rname}.{mname} response key {dk} "
                          f"absent in {ref}")
                    errors += 1
            # sqlVerbs refs
            for verb, lst in (r.get("sqlVerbs", {}) or {}).items():
                for entry in lst:
                    vref = entry.get("$ref", "")
                    target = deref_pointer(doc, vref)
                    if target is None:
                        print(f"  [ERR] {svc}:{rname} sqlVerb {verb} unresolved "
                              f"{vref}")
                        errors += 1
    print(f"\nservices={len(files)} resources={total_res} methods={total_meth} "
          f"errors={errors}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
