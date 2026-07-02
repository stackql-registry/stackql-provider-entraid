# CLAUDE.md

Guidance for working in this repository. Read this first, then the root
[`stackql_entraid_provider/README.md`](stackql_entraid_provider/README.md) for
the full build/test/publish flow.

## What this repo is

Builds the **`entra_id`** StackQL provider - query and manage Microsoft Entra ID
(formerly Azure AD) with SQL. The provider is derived from the Microsoft Graph
`v1.0` OpenAPI description; this repo began as a fork of
[`microsoftgraph/msgraph-metadata`](https://github.com/microsoftgraph/msgraph-metadata).

Two zones live side by side:

- **Repo root** - upstream `msgraph-metadata` files (including `openapi/v1.0/`),
  synced periodically from upstream. Do not put StackQL-specific work here.
- **[`stackql_entraid_provider/`](stackql_entraid_provider/)** - everything
  StackQL-specific, so it never collides with an upstream sync. Almost all work
  happens here. The `npm run` / Python commands assume you have `cd`'d into it.

Scope is deliberately narrowed to the **identity & directory** workloads of
Graph (users, groups, applications, service principals, directory roles, devices,
domains, policies, identity governance/protection, role management, ...) and
drops productivity workloads (Exchange/SharePoint/Teams/Intune/...). The scope
rule lives in
[`provider-dev/scripts/entra_id-discriminator.mjs`](stackql_entraid_provider/provider-dev/scripts/entra_id-discriminator.mjs).
Result: **39 services / 858 resources / 2,634 methods**.

## Layout (under `stackql_entraid_provider/`)

- `provider-dev/openapi/src/entra_id/` - **the generated provider** (a
  `provider.yaml` + one service YAML per service under
  `v00.00.00000/services/`). This is what gets published. Service files are
  large (several are 30-50 MB); prefer `grep`/`Glob` with line offsets over
  reading them whole.
- `provider-dev/config/` - generator inputs: `provider-config.json` (becomes the
  provider-level `config` block), `servers.json`, and the curated
  `all_services.csv` mapping.
- `provider-dev/scripts/` - `entra_id-discriminator.mjs` (scope),
  `curate_mappings.py` (resource/verb/objectKey curation), `validate_provider.py`.
- `provider-dev/source/` - intermediate split/normalized specs (regenerated).
- `provider-dev/test/` - pytest tier-1 / UAT smoke tests (see Testing).
- `website/` - Docusaurus microsite (has its own `node_modules`; ignore for
  provider work).

## Build pipeline

Prereqs: Node >= 18, Python 3, the `stackql` CLI. From `stackql_entraid_provider/`:

```bash
npm install            # .npmrc points @jsr at the JSR registry
npm run split -- --provider-name entra_id --api-doc ../openapi/v1.0/openapi.yaml \
  --svc-discriminator function \
  --svc-discriminator-fn provider-dev/scripts/entra_id-discriminator.mjs \
  --output-dir provider-dev/source --overwrite
npm run normalize -- --api-dir provider-dev/source
npm run generate-mappings -- --input-dir provider-dev/source --output-dir provider-dev/config
python3 provider-dev/scripts/curate_mappings.py
npm run generate-provider -- --provider-name entra_id \
  --input-dir provider-dev/source --output-dir provider-dev/openapi/src/entra_id \
  --config-path provider-dev/config/all_services.csv \
  --servers provider-dev/config/servers.json \
  --provider-config provider-dev/config/provider-config.json \
  --naive-req-body-translate --overwrite
python3 provider-dev/scripts/inject_pushdown_config.py   # service-level OData push-down config
python3 provider-dev/scripts/validate_provider.py
```

`generate-provider` overwrites everything under
`provider-dev/openapi/src/entra_id/`. **Anything you want to survive a rebuild
must live in a generator input** (e.g. `provider-config.json` for the auth
`config` block, `all_services.csv` for mappings) **or in a post-generation
script** that you re-run afterwards (`curate_mappings.py`,
`inject_pushdown_config.py`). Hand-edits to the generated `provider.yaml` /
service docs are fine for a quick local iteration but get wiped on the next
`generate-provider`.

## Authentication

Microsoft Graph OAuth2 **client-credentials (app-only)**. Set `AZURE_TENANT_ID`,
`AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`; the app needs admin-consented Graph
**application** permissions for whatever you query (e.g. `User.Read.All`,
`Group.Read.All`, `Application.Read.All`, `Organization.Read.All`). The auth
block requests `https://graph.microsoft.com/.default` against
`https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`. Provisioning:
[`provider-dev/entra_id_access_permissions.md`](stackql_entraid_provider/provider-dev/entra_id_access_permissions.md).

## Testing (WSL / Linux)

The Go toolchain and the preferred test path are in **WSL**. Run the pytest
suite from `stackql_entraid_provider/`:

```bash
bash provider-dev/test/bootstrap.sh          # downloads stackql into provider-dev/test/.bin/
python -m venv provider-dev/test/.venv && source provider-dev/test/.venv/bin/activate
pip install -r provider-dev/test/requirements.txt
source provider-dev/.env                     # AZURE_* creds for the live tenant
pytest provider-dev/test/ -v                 # exec mode; add --mode=pgwire or --mode=both
```

`tier1.yaml` is data-driven (name / sql / assertions); add a query there, no
Python changes needed. `conftest.py` and `test_tier1.py` are reusable across
providers. Tier-1 tests hit the **live** tenant, so they need the `AZURE_*`
creds and the corresponding Graph permissions.

Quick structural checks without creds (registry pointed at the local build):

```bash
ROOT="$(pwd)/provider-dev/openapi"
REG='{"url": "file://'${ROOT}'", "localDocRoot": "'${ROOT}'", "verifyConfig": {"nopVerify": true}}'
stackql exec "SHOW SERVICES IN entra_id" --registry="${REG}"
stackql exec "DESCRIBE entra_id.applications.applications" --registry="${REG}"
```

## OData query-option push-down

Graph is an OData API. StackQL (as of PR
[stackql/stackql#678](https://github.com/stackql/stackql/pull/678)) can push a
`SELECT`'s projection / `WHERE` / `ORDER BY` / `LIMIT` / `OFFSET` / `COUNT(*)`
down to the upstream as OData query options. It is **best-effort and additive**:
the client-side WHERE / projection / LIMIT stay authoritative, so a partial or
absent translation never changes results.

- Enabled by a `queryParamPushdown` block. Config inheritance is
  **Method -> Resource -> Service -> ProviderService -> Provider**, but in
  practice a **provider-level** block (in `provider.yaml` / `provider-config.json`)
  is a no-op: it is not propagated to the operation stores built from the
  separately `$ref`'d service docs during registry load (verified empirically -
  provider-level pushes nothing; resource- and service-level both work). So the
  config is injected at **service level** as a top-level `x-stackQL-config`
  extension in each of the 39 service docs, by
  [`provider-dev/scripts/inject_pushdown_config.py`](stackql_entraid_provider/provider-dev/scripts/inject_pushdown_config.py)
  (one block per service, not per resource; idempotent). `generate-provider`
  overwrites the service docs, so **re-run the injector after every rebuild**
  (see the pipeline step below).
- SQL -> intent extraction lives in stackql
  (`internal/stackql/pushdown/pushdown.go`); intent -> OData wire translation
  lives in any-sdk (`internal/anysdk/query_param_pushdown_apply.go`). Local
  checkouts: `C:\LocalGitRepos\stackql\core\stackql` and
  `...\core\any-sdk` (schema defs under `any-sdk/cicd/schema-definitions`).
- Only string- and integer-literal comparisons and prefix `LIKE` reach `$filter`.
  A boolean-keyword literal (`col = true`) is **not** pushed by current stackql
  (parsed as a keyword, not a pushable `SQLVal`) and stays a client-side filter.

SQL -> OData wire mapping:

| SQL | OData wire param |
|---|---|
| `SELECT a, b` (simple scan) | `$select=a,b` |
| `WHERE col = 'x'` (also `!= > >= < <=`) | `$filter=col eq 'x'` (`ne gt ge lt le`) |
| `WHERE col LIKE 'A%'` (prefix only) | `$filter=startswith(col,'A')` |
| multiple `AND` predicates | joined with ` and ` |
| `ORDER BY col [asc|desc]` | `$orderby=col asc` |
| `LIMIT n` | `$top=n` |
| `OFFSET n` | `$skip=n` |
| `COUNT(*)` | `$count=true` (suppresses top/skip/select/orderby) |

Push-down only fires for a **simple resource-scoped scan** - a single table, no
`JOIN` / `GROUP BY` / `DISTINCT` / `HAVING` (those change grain, so LIMIT etc.
revert to client-side primitives). `OR`, non-column LHS, and non-prefix `LIKE`
stay client-side.

**Observing the wire request**: run stackql with `--http.log.enabled`. any-sdk
prints the outgoing request to stderr as
`http request url: '<url incl. ?$filter=...&$select=...>', method: 'GET'`
(URL-encoded: `$`->`%24`, space->`+`, `'`->`%27`). This is what the push-down
tests assert against - see `provider-dev/test/` pushdown cases.

Graph caveat: some advanced `$filter`/`$orderby`/`$count` combinations require
the header `ConsistencyLevel: eventual` and `$count=true` (Graph "advanced
queries"). Push-down emits the params regardless; if Graph rejects a specific
query the whole call fails (push-down is not a silent fallback at the HTTP
layer). Choose test/query shapes Graph accepts.

## Docs & publishing

- Docs: `npm run generate-docs -- --provider-name entra_id --provider-dir
  ./provider-dev/openapi/src/entra_id/v00.00.00000 --output-dir ./website
  --provider-data-dir ./provider-dev/docgen/provider-data`.
- Publish: push
  `provider-dev/openapi/src/entra_id` to `providers/src` on a feature branch of
  [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry)
  and follow the registry release flow.

## Conventions

- Object keys are schema-driven: `$.value` is emitted only when the response
  actually exposes a `value` array. A `SELECT` fails if the object key points at
  a property the response lacks - keep this in mind when curating mappings.
- Resource names come from the navigation-collection chain with the root
  collection dropped (`/users/{id}/appRoleAssignments` -> `app_role_assignments`).
- SQL column names are the Graph property names (camelCase, e.g. `displayName`,
  `userPrincipalName`), so `$select` / `$filter` push-down uses them verbatim.
</content>
