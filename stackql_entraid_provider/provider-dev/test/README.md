# Tier 1 / UAT tests

Smoke tests that exercise the locally-built provider against the live upstream
API. Designed for WSL / Linux. Same suite runs in two modes:

- `exec`   - one-shot `stackql exec --output json` per query
- `pgwire` - long-lived `stackql srv`, queried over Postgres wire (psycopg)

## One-time setup

Run from `stackql_entraid_provider/` (i.e. `cd stackql_entraid_provider` from the repo root first):

```bash
bash provider-dev/test/bootstrap.sh          # downloads latest stackql into provider-dev/test/.bin/
python -m venv provider-dev/test/.venv
source provider-dev/test/.venv/bin/activate
pip install -r provider-dev/test/requirements.txt
```

## Run

Also from `stackql_entraid_provider/`:

```bash
source provider-dev/.env                     # exports STACKQL_GITHUB_USERNAME / PASSWORD

# exec mode (default)
pytest provider-dev/test/ -v

# pgwire mode
pytest provider-dev/test/ -v --mode=pgwire

# both modes - same suite runs twice
pytest provider-dev/test/ -v --mode=both
```

## What to edit when

- **Add / change a query**: edit `tier1.yaml`. No Python changes needed.
- **Add a new assertion primitive**: edit `test_tier1.py`.
- **Reuse for another provider**: copy this directory, edit `provider.yaml`
  (provider name, registry path, required auth env vars) and `tier1.yaml`.
  Nothing else should need to change.

## tier1.yaml shape

```yaml
- name: short_test_id
  sql: |
    SELECT ... WHERE org = '${TEST_ORG}'
  assertions:
    min_rows: 1                              # default 1; set 0 to allow empty
    required_columns: [col_a, col_b]         # must be present on every row
    row_predicates:                          # python exprs, `rows` and `r` in scope
      - "r['col_a'] == 'expected'"
```

`${VAR}` substitution looks up `test_env_defaults` in `provider.yaml` first,
then the process environment. Use it for anything per-environment (target org,
expected username, etc.) - do not hard-code values in `tier1.yaml`.

## OData push-down tests

`test_odata_pushdown.py` (data-driven from `pushdown.yaml`) verifies that stackql
translates SQL query options into OData query params on the outgoing Microsoft
Graph request: projection -> `$select`, `WHERE` -> `$filter`, `ORDER BY` ->
`$orderby`, `LIMIT` -> `$top`, `OFFSET` -> `$skip`, `COUNT(*)` -> `$count`.

Each case runs `stackql exec --http.log.enabled`, which makes any-sdk print the
outgoing request URL to stderr (`http request url: '<url>', method: 'GET'`) just
before dispatch. The test URL-decodes the graph.microsoft.com request query and
asserts the pushed options (`expect_wire`) / absent options (`forbid_wire`). The
URL is logged before the request is sent, so the assertions do not depend on
Graph returning 200 - only on the `AZURE_*` app-only creds being valid enough to
mint a token. These run in exec mode only (the translation is transport-agnostic).

Two prerequisites beyond the tier-1 setup:

- **Push-down is not in a released stackql yet.** The bootstrapped
  `.bin/stackql` will not have it. Point `STACKQL_BINARY` at a build of the
  feature branch:

  ```bash
  STACKQL_BINARY=/mnt/c/LocalGitRepos/stackql/core/stackql/build/stackql \
    pytest provider-dev/test/test_odata_pushdown.py -v
  ```

- **The push-down config must be present in the built provider.** It is injected
  at service level by `provider-dev/scripts/inject_pushdown_config.py`; re-run
  that after any `generate-provider` (see the root `CLAUDE.md`).

To add a case: edit `pushdown.yaml` (`name` / `sql` / `expect_wire` /
`forbid_wire`). `expect_wire` / `forbid_wire` fragments are matched against the
URL-**decoded** query string (so write `$filter=userType eq 'Member'`, not the
`%24filter=...%27Member%27` wire encoding). Only string/integer-literal and
prefix-`LIKE` predicates reach `$filter`; a boolean literal (`col = true`) is not
pushed by current stackql - `bool_literal_not_pushed` pins that.
