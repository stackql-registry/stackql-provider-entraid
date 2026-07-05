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
Result: **39 services / 839 resources / 2,630 methods**.

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
python3 provider-dev/scripts/curate_source_specs.py      # snake path params + de-require @odata.type
# DO NOT rm all_services.csv - it is the MASTER mapping record (see below).
npm run generate-mappings -- --input-dir provider-dev/source --output-dir provider-dev/config  # preserves mapped ops, appends new ones blank
python3 provider-dev/scripts/curate_mappings.py          # classifies only the NEW (blank) ops; preserves the rest
npm run generate-provider -- --provider-name entra_id \
  --input-dir provider-dev/source --output-dir provider-dev/openapi/src/entra_id \
  --config-path provider-dev/config/all_services.csv \
  --servers provider-dev/config/servers.json \
  --provider-config provider-dev/config/provider-config.json \
  --naive-req-body-translate --overwrite
python3 provider-dev/scripts/inject_pushdown_config.py   # OData push-down + per-method request blocks
python3 provider-dev/scripts/validate_provider.py
```

`generate-provider` overwrites everything under
`provider-dev/openapi/src/entra_id/`. **Anything you want to survive a rebuild
must live in a generator input** (e.g. `provider-config.json` for the auth
`config` block, `all_services.csv` for mappings), **in a source curation**
(`curate_source_specs.py`, which snake-cases path params, de-requires
`@odata.type`, and adds `directoryObjectId` to `ReferenceCreate` in
`provider-dev/source`), **or in a post-generation script** that you re-run
afterwards (`curate_mappings.py`, `inject_pushdown_config.py`). Hand-edits to
the generated `provider.yaml` / service docs are fine for a quick local
iteration but get wiped on the next `generate-provider`.

## Mapping stability - `all_services.csv` is the master

`all_services.csv` is the **durable master record** of how every operation maps
to a `(stackql_resource_name, stackql_method_name, stackql_verb, object_key)`,
keyed by **`file` + `operationId`**. It is committed and must NOT be `rm`'d.
The point: an operation's SQL routing (e.g. `INSERT INTO entra_id.users.users`)
stays pinned to the same upstream operation **across code changes** - the
classification heuristics can evolve without silently re-routing (breaking)
existing resources/methods between provider versions. Only genuinely new
operations get a fresh mapping.

Two steps cooperate, both preserve-by-`operationId`:

- **`generate-mappings`** (provider-utils `analyze`) parses each source spec.
  An `operationId` already present in the CSV is left untouched (logs
  `Skipping already mapped operation`); a new one is appended with **blank**
  `stackql_*` columns - analyze does not classify it.
- **`curate_mappings.py`** fills the blanks: a row that already carries a
  `stackql_resource_name` is **preserved verbatim**; only blank (new) rows are
  classified by the heuristics in `classify()` (nav-collection chain -> resource,
  HTTP verb + path shape -> method/verb, schema-driven `$.value` object key, plus
  the lifecycle/`exec` folds and the hand-curated `EXEC_FOLD` overrides). The
  uniqueness pass seeds from the mastered rows, so a new method is renamed around
  existing ones - an existing method name never shifts.

Net effect: `generate-mappings` + `curate_mappings.py` are idempotent on an
unchanged spec (re-running rewrites the CSV byte-identical) and additive on a
changed one (new services / resources / operations get sensible defaults;
everything already mapped is backward-compatible by default). This is the same
pattern used for every stackql provider, whether built from vendor OpenAPI specs
or from a spec reconstituted via the provider's SDK.

To **re-master** an operation deliberately, edit its `stackql_*` cells directly,
or blank them and re-run **`curate_mappings.py`** (curate reclassifies just that
row). Do not blank-then-re-run `generate-mappings`: analyze appends a duplicate
row when it finds an existing row whose `stackql_*` is blank. A `rm` + full
rebuild reclassifies everything from the heuristics (bootstrap) - use it only to
intentionally rebaseline, never in the normal version-to-version flow.

Bear in mind the CSV masters **mappings only**; the OData push-down extensions
(`x-stackQL-config`) and per-method request primitives (`nativeCasing`,
`transform`) are a separate concern applied post-generation by
`inject_pushdown_config.py`.

## SQL surface casing (stackql >= v0.10.542)

The SQL surface: **properties keep the Graph wire casing (camelCase); path
params are snake_case**.

- **Columns and body properties are wire-cased** (`displayName`,
  `userPrincipalName`). DELIBERATE: stackql push-down (v0.10.542) emits the
  RAW SQL identifier with no re-casing, so wire-cased identifiers give full
  `$select`/`$filter`/`$orderby` push-down. snake aliases
  (`snake_case_aliases: true`) were tried and REVERTED: `$select=display_name`
  400s the whole call, so column-bearing push-down had to be disabled - and
  without `$select`, Graph returns only its DEFAULT property subset, so
  non-default columns (e.g. `accountEnabled`) silently came back null. Do not
  re-enable snake aliases unless engine push-down learns identifier re-casing
  (via `request.nativeCasing`); camelCase is fine unquoted in SQL.
- **Push-down `supportedColumns` = real schema property names** (harvested per
  service by `inject_pushdown_config.py` via a YAML parse of each doc's
  `properties:` maps). Required because push-down extracts predicates from the
  raw WHERE clause INCLUDING keys consumed as operation params during routing:
  without the allowlist, `WHERE user_id = 'x'` (by-id get) also emits
  `$filter=user_id eq 'x'` on the single-entity URL (Graph rejects $filter
  there) and `WHERE ConsistencyLevel = 'eventual'` leaks into $filter.
- **Path params** are physically snake_case in the specs
  (`{domain_dns_record_id}`, `WHERE application_id = ...`), renamed at source
  level by `curate_source_specs.py` in both path templates and parameter
  declarations. Kebab wire forms (`application-id`) are unusable unquoted in
  SQL, and path param names never travel on the wire. (Before this, templates
  said `{domainDnsRecord_id}` while declarations said `domainDnsRecord-id` -
  by-id routing never actually worked.)
- **Input tolerance (invisible)**: `request.nativeCasing: camel` is injected
  on every method; snake input keys (`data__display_name`) ALSO resolve to
  their camel wire form in routing/request construction. Display everywhere
  (SHOW/DESCRIBE/docs) is wire-cased.
- **Header params** (`ConsistencyLevel`, `If-Match`) keep wire names and must
  be typed verbatim (quoted where needed). `WHERE ConsistencyLevel =
  'eventual'` enables Graph advanced queries ($count on directory objects).
- **No `data__` prefix**: `--naive-req-body-translate` makes `generate-provider`
  emit `config: {requestBodyTranslate: {algorithm: naive}}` on every
  POST/PUT/PATCH method that has a requestBody, so body params are addressed
  bare (`INSERT INTO ... (displayName, ...)`), not `data__`-prefixed.
  CAVEAT: although the stackql-config schema allows `requestBodyTranslate` at
  every level, the v0.10.542 runtime only CONSUMES it from METHOD-level config
  (`getRequestBodyTranslateAlgorithmString` reads `op.StackQLConfig` with no
  inheritance walk, unlike `queryParamPushdown`/`retry`). A service-level block
  is a silent no-op - keep the generator flag; do not hoist.
- **COUNT(*) is client-side even when pushed**: `$count=true` goes to the wire
  but v0.10.542 never harvests the `@odata.count` annotation
  (`CountResponseKey` is plumbed but unconsumed) - correct results, full
  pagination cost.
- `@odata.type` is de-required everywhere (source curation); it stays an
  optional property for polymorphic creates. There is NO engine mechanism to
  default it into a populated body (`request.base` is an empty-body fallback
  only; `request.required` / `request.default` are not consumed by any-sdk).
- **Relationship ($ref) writes take `directoryObjectId`**, not `@odata.id`:
  `curate_source_specs.py` adds the property to the shared `ReferenceCreate`
  schema and `inject_pushdown_config.py` puts a `request.transform`
  (golang_template_json_v0.1.0) on every `add_ref` method that renders
  `{"@odata.id": "https://graph.microsoft.com/v1.0/directoryObjects/<id>"}`
  from it (a verbatim `@odata.id` still works as a fallback). Example:
  `INSERT INTO entra_id.groups.members (group_id, directoryObjectId)
  SELECT '<group-id>', '<user-object-id>';`

## Authentication

Microsoft Graph OAuth2 **client-credentials (app-only)**. Set `AZURE_TENANT_ID`,
`AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`; the app needs admin-consented Graph
**application** permissions for whatever you query (e.g. `User.Read.All`,
`Group.Read.All`, `Application.Read.All`, `Organization.Read.All`). The auth
block requests `https://graph.microsoft.com/.default` against
`https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`. Provisioning:
[`provider-dev/entra_id_access_permissions.md`](stackql_entraid_provider/provider-dev/entra_id_access_permissions.md).

## Test the provider (meta routes)

Run this **after every build (post `inject_pushdown_config.py` / `validate_provider.py`)
and before the live UAT tests and web docs**. It starts a local StackQL server
against the fresh build and walks every `SHOW SERVICES` / `SHOW RESOURCES` /
`SHOW EXTENDED METHODS` / `DESCRIBE EXTENDED` route - a no-creds structural gate
that catches resources with no methods, duplicate method signatures within a SQL
verb, and selectable resources whose columns do not resolve. The npm scripts
wrap `bin/*.sh` + `bin/test-meta-routes.cjs` (copied from the `github` provider
archetype; provider-agnostic - name comes from `package.json` / the CLI arg).

```bash
npm run start-server -- --provider entra_id --registry "$(pwd)/provider-dev/openapi"
npm run test-meta-routes -- entra_id --verbose   # exits non-zero on first defect
npm run stop-server
```

It exits on the first structural defect; fix it (usually in `curate_mappings.py`,
then rebuild) before the UAT tests. Runtime artifacts (`./stackql`,
`stackql-server.log`) are gitignored.

## Testing (WSL / Linux)

The Go toolchain and the preferred test path are in **WSL**. Run the pytest
suite from `stackql_entraid_provider/`:

```bash
bash provider-dev/test/bootstrap.sh          # downloads stackql into provider-dev/test/.bin/
python -m venv provider-dev/test/.venv && source provider-dev/test/.venv/bin/activate
pip install -r provider-dev/test/requirements.txt
source .env    # AZURE_* creds for the live tenant (CRLF + single-quoted values:
               # when parsing in WSL, strip \r and the wrapping quotes)
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
| `OFFSET n` | NOT pushed - Graph rejects `$skip` on directory objects ("'$skip' is not supported by the service", 400); `skip` is omitted from the injected config and OFFSET stays client-side (correct via nextLink pagination) |
| `COUNT(*)` | `$count=true` (suppresses top/select/orderby) |

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
  --provider-data-dir ./provider-dev/docgen/provider-data`, then
  `python3 provider-dev/scripts/curate_docs.py` (post-docgen: suppresses the
  OData `$`-params from parameter tables and examples and drops `@odata.type`
  rows; identifiers stay wire-cased, matching the SQL surface).
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
