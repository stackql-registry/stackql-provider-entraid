"""
OData push-down tests, parametrised from pushdown.yaml.

Verifies that stackql translates SQL query options (projection / WHERE /
ORDER BY / LIMIT / OFFSET / COUNT(*)) into OData query params ($select /
$filter / $orderby / $top / $skip / $count) on the outgoing Microsoft Graph
request.

Observability: `--http.log.enabled` makes any-sdk print each outgoing request to
stderr as `http request url: '<url>', method: '<verb>'` just before dispatch.
We capture that, keep the graph.microsoft.com request (not the token endpoint),
URL-decode its query string, and assert the pushed options.

The URL is logged before the request is sent, so these assertions do not depend
on Graph returning 200 - only on the app-only credentials being valid enough to
mint a token (same AZURE_* creds tier1 needs). Push-down is exec-mode only here;
the translation is transport-independent, so there is no pgwire variant.

Binary: push-down is not in a released stackql yet, so the bootstrapped
provider-dev/test/.bin/stackql will not have it. Point STACKQL_BINARY at a build
of the feature branch (e.g. C:/LocalGitRepos/stackql/core/stackql/build/stackql,
as /mnt/c/... under WSL) to run these; without it the shared fixture binary is
used and the wire assertions will fail if that binary predates push-down.
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Any
from urllib.parse import unquote_plus, urlsplit

import pytest
import yaml

PUSHDOWN = Path(__file__).resolve().parent / "pushdown.yaml"

_VAR_RE = re.compile(r"\$\{([A-Z_][A-Z0-9_]*)\}")
# any-sdk log line: http request url: '<url>', method: '<verb>'
_URL_RE = re.compile(r"http request url: '([^']*)'")


def _substitute(template: str, env: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        if name in env:
            return env[name]
        if name in os.environ:
            return os.environ[name]
        raise KeyError(f"pushdown.yaml references ${{{name}}} but it is not set")
    return _VAR_RE.sub(repl, template)


def _load_cases() -> list[dict[str, Any]]:
    with PUSHDOWN.open() as f:
        return list(yaml.safe_load(f))


@pytest.fixture(scope="session")
def pushdown_binary(stackql_binary: Path) -> Path:
    """The stackql to test push-down with. Honours STACKQL_BINARY (point it at a
    feature-branch build that has push-down); falls back to the shared fixture."""
    override = os.environ.get("STACKQL_BINARY")
    if override:
        p = Path(override)
        if not p.exists():
            pytest.exit(f"STACKQL_BINARY={override} does not exist", returncode=2)
        return p
    return stackql_binary


def _graph_request_query(stderr: str) -> str:
    """Return the URL-decoded query string of the first graph.microsoft.com
    request logged by --http.log.enabled. Raises with the captured log on miss."""
    urls = _URL_RE.findall(stderr)
    graph_urls = [u for u in urls if "graph.microsoft.com" in u]
    if not graph_urls:
        raise AssertionError(
            "no 'http request url:' line for graph.microsoft.com found in stderr.\n"
            "Is --http.log.enabled honoured and did auth succeed?\n"
            f"--- stderr ---\n{stderr}"
        )
    return unquote_plus(urlsplit(graph_urls[0]).query)


@pytest.mark.parametrize("case", _load_cases(), ids=lambda c: c["name"])
def test_odata_pushdown(
    case: dict[str, Any],
    pushdown_binary: Path,
    registry_arg: str,
    test_env: dict[str, str],
) -> None:
    sql = _substitute(case["sql"], test_env)
    proc = subprocess.run(
        [
            str(pushdown_binary),
            "exec",
            "--registry", registry_arg,
            "--http.log.enabled",
            "--output", "json",
            sql,
        ],
        capture_output=True,
        text=True,
        timeout=60,
    )
    # rc is intentionally not asserted: the request URL is logged before dispatch,
    # so a Graph-side rejection (e.g. an advanced query needing ConsistencyLevel)
    # still yields a verifiable wire shape. Both streams are searched because the
    # log target has moved between stackql versions.
    log = proc.stderr + proc.stdout
    query = _graph_request_query(log)

    for fragment in case.get("expect_wire", []):
        assert fragment in query, (
            f"expected wire fragment not pushed: {fragment!r}\n"
            f"decoded request query: {query!r}\nSQL:\n{sql}"
        )

    for fragment in case.get("forbid_wire", []):
        assert fragment not in query, (
            f"forbidden wire fragment was pushed: {fragment!r}\n"
            f"decoded request query: {query!r}\nSQL:\n{sql}"
        )
