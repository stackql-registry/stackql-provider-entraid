# `entra_id` provider for [`stackql`](https://github.com/stackql/stackql)

This repository builds and documents the **`entra_id`** provider for StackQL - query and manage **Microsoft Entra ID** (formerly Azure Active Directory) using SQL.

The provider is **derived from the Microsoft Graph `v1.0` OpenAPI description** (this repo originated as a fork of [`microsoftgraph/msgraph-metadata`](https://github.com/microsoftgraph/msgraph-metadata)). The identity & directory surface of Microsoft Graph is extracted, normalized, and transformed into a StackQL provider using [`@stackql/provider-utils`](https://www.npmjs.com/package/@stackql/provider-utils), following the conventions of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry).

The generated provider lives under [`stackql_entraid_provider/provider-dev/openapi/src/entra_id/`](provider-dev/openapi/src/entra_id/) - a `provider.yaml` plus one OpenAPI-extension service file per service.

> Everything specific to the StackQL provider lives under `stackql_entraid_provider/` at the repo root so it does not collide with files synced periodically from upstream [`microsoftgraph/msgraph-metadata`](https://github.com/microsoftgraph/msgraph-metadata). Paths in this document are written **relative to the repository root**. The `npm run` commands and Python scripts below assume you have `cd`'d into `stackql_entraid_provider/` first, since they resolve their own inputs relative to the current working directory.

## Scope

Microsoft Graph spans many workloads (Exchange, SharePoint/OneDrive, Teams, Intune, Planner, Search, Security, ...). The `entra_id` provider deliberately exposes only the **identity & directory** workloads. From the Graph spec's `<workload>.<entity>` operation tags we keep the Entra ID workloads (users, groups, applications, service principals, directory roles, devices, domains, policies, identity governance/protection, role management, etc.) and drop the productivity ones. For the large `users` and `groups` workloads we additionally keep only their directory-relevant resources (app role assignments, authentication methods, licences, memberships, owners, ...) and drop mailbox/calendar/drive/Teams resources.

The scope is encoded in [`stackql_entraid_provider/provider-dev/scripts/entra_id-discriminator.mjs`](provider-dev/scripts/entra_id-discriminator.mjs).

The result is **39 services / 839 resources / 2,630 methods**, all of which `DESCRIBE` cleanly in StackQL.

## Authentication

`entra_id` uses the Microsoft Graph **OAuth2 client-credentials (app-only)** grant. Register an app in Entra ID, grant it the Microsoft Graph **application** permissions you need (admin-consented), and create a client secret. Then set:

| Env var | Description |
|---|---|
| `AZURE_TENANT_ID` | Tenant ID (GUID or verified domain) - interpolated into the token endpoint |
| `AZURE_CLIENT_ID` | Application (client) ID |
| `AZURE_CLIENT_SECRET` | Client secret |

The provider's `config.auth` block (in `provider.yaml`) requests the `https://graph.microsoft.com/.default` scope against `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`.

See [`stackql_entraid_provider/provider-dev/entra_id_access_permissions.md`](provider-dev/entra_id_access_permissions.md) for how to provision the application permissions in your tenant.

## Building the provider

Prerequisites: Node.js >= 18, Python 3, and the [`stackql`](https://github.com/stackql/stackql) CLI. From the repository root:

```bash
cd stackql_entraid_provider
npm install   # the .npmrc points the @jsr scope at the JSR registry
```

The source Graph OpenAPI specs are vendored at the repo root under [`openapi/v1.0/`](../openapi/v1.0/) (upstream layout, not moved). The pipeline (run from `stackql_entraid_provider/`):

```bash
# 1. Split the monolithic Graph v1.0 spec into per-service specs (entra_id scope only)
npm run split -- \
  --provider-name entra_id \
  --api-doc ../openapi/v1.0/openapi.yaml \
  --svc-discriminator function \
  --svc-discriminator-fn provider-dev/scripts/entra_id-discriminator.mjs \
  --output-dir provider-dev/source \
  --overwrite

# 2. Normalize schemas (flatten allOf, lift path params, etc.)
npm run normalize -- --api-dir provider-dev/source

# 2a. Curate the source specs for a SQL-friendly surface:
#     - path params -> full snake_case ({domainDnsRecord_id} -> {domain_dns_record_id}),
#       in both the path templates and the parameter declarations
#       (properties/columns keep the Graph wire casing - see the push-down note)
#     - '@odata.type' stripped from every schema `required:` array (the OData
#       discriminator is only needed for polymorphic creates; it stays available
#       as an optional property)
#     - a friendly `directoryObjectId` property added to the shared
#       ReferenceCreate schema (relationship $ref write bodies)
python3 provider-dev/scripts/curate_source_specs.py

# 3. Generate the mapping CSV, then curate it (resource/method/verb/objectKey)
#    NOTE: analyze MERGES into an existing all_services.csv (stale paths survive
#    renames) - delete it first for a truly fresh build after source changes.
npm run generate-mappings -- --input-dir provider-dev/source --output-dir provider-dev/config
python3 provider-dev/scripts/curate_mappings.py

# 4. Generate the StackQL provider
npm run generate-provider -- \
  --provider-name entra_id \
  --input-dir provider-dev/source \
  --output-dir provider-dev/openapi/src/entra_id \
  --config-path provider-dev/config/all_services.csv \
  --servers provider-dev/config/servers.json \
  --provider-config provider-dev/config/provider-config.json \
  --naive-req-body-translate \
  --overwrite

# 5. Inject per-service StackQL config into each service doc
#    (generate-provider overwrites the service docs, so re-run this every build):
#    - OData query-param push-down (queryParamPushdown); $select/$filter/
#      $orderby carry a supportedColumns allowlist = the service's real schema
#      property names, so WHERE keys consumed as operation params (user_id,
#      ConsistencyLevel) never leak into $filter
#    - request.nativeCasing: camel on every method (input tolerance: snake keys
#      also resolve to the camelCase wire params / body properties)
#    - a request transform on every add_ref method rendering the OData $ref
#      body from the friendly directoryObjectId property
python3 provider-dev/scripts/inject_pushdown_config.py

# 6. Validate structure (every $ref resolves) and engine load
python3 provider-dev/scripts/validate_provider.py
```

### Mapping curation

`generate-mappings` (the `analyze` step) cannot infer resource names from Graph's OData operation IDs, so [`stackql_entraid_provider/provider-dev/scripts/curate_mappings.py`](provider-dev/scripts/curate_mappings.py) does it deterministically from the path structure:

- **Resource name** = the navigation-collection chain (root collection dropped), e.g. `/users/{id}/appRoleAssignments` -> `app_role_assignments`.
- **Method / SQL verb** = derived from the HTTP verb and path shape: `GET` collection -> `list`/`select`, `GET` item -> `get`/`select`, `POST` -> `insert`, `PATCH` -> `update`, `PUT` -> `replace`, `DELETE` -> `delete`; bound actions -> `exec`; relationship `$ref` writes -> `insert`/`delete`.
- **Object key** is **schema-driven**: `$.value` is emitted only when the operation's success-response schema actually exposes a `value` array. Single-valued navigation properties (`manager`, `createdOnBehalfOf`, OData key-accessors like `federatedIdentityCredentials(name='{name}')`) and scalar/binary responses (logos, branding images, CSS) are handled accordingly - this is required, since StackQL fails a `SELECT` if the object key points at a property the response lacks.
- OData noise that does not model relationally - type-cast projections (`/graph.<type>`), `$count`, `$value` binary streams - is dropped via the `skip_this_resource` sentinel.

## Test the provider (meta routes)

Before the live UAT tests and the web docs, run the metadata smoke test. It
starts a local StackQL server against the freshly-built provider and walks every
`SHOW SERVICES` / `SHOW RESOURCES` / `SHOW EXTENDED METHODS` / `DESCRIBE EXTENDED`
route, so it catches structural defects (a resource with no methods, duplicate
method signatures within a SQL verb, a selectable resource whose columns do not
resolve) without needing tenant credentials.

From `stackql_entraid_provider/`:

```bash
# start a server against the local build (downloads stackql to ./stackql if absent)
npm run start-server -- --provider entra_id --registry "$(pwd)/provider-dev/openapi"
npm run server-status                       # optional: confirm it is up

# walk every meta route for the provider
npm run test-meta-routes -- entra_id --verbose

npm run stop-server                         # stop the server when done
```

The meta-routes test exits non-zero on the first structural defect it finds -
fix it (usually in [`provider-dev/scripts/curate_mappings.py`](provider-dev/scripts/curate_mappings.py),
then rebuild) before moving on to the live UAT tests below.

## Testing

From `stackql_entraid_provider/`:

```bash
ROOT="$(pwd)/provider-dev/openapi"
REG='{"url": "file://'${ROOT}'", "localDocRoot": "'${ROOT}'", "verifyConfig": {"nopVerify": true}}'

./stackql exec "SHOW SERVICES IN entra_id" --registry="${REG}"
./stackql exec "SHOW RESOURCES IN entra_id.users" --registry="${REG}"
./stackql exec "DESCRIBE entra_id.applications.applications" --registry="${REG}"
./stackql exec "DESCRIBE EXTENDED entra_id.applications.applications" --registry="${REG}"

./stackql shell --registry="${REG}"
```

Example queries (require the auth env vars above and a live tenant). Columns
and body properties use the Graph wire casing (`displayName`,
`userPrincipalName`) - this keeps OData query push-down at full fidelity
(projection -> `$select`, WHERE -> `$filter`, ORDER BY -> `$orderby`,
LIMIT/OFFSET -> `$top`/`$skip`, COUNT(*) -> `$count`). Path params are
snake_case (`WHERE user_id = ...`) - Graph's kebab wire forms (`user-id`) are
not usable unquoted in SQL:

```sql
-- list users (projection pushes down as $select)
SELECT id, displayName, userPrincipalName, accountEnabled
FROM entra_id.users.users;

-- get a user by id (snake_case path param)
SELECT id, displayName
FROM entra_id.users.users
WHERE user_id = '00000000-0000-0000-0000-000000000000';

-- server-side filter ($filter=startswith(displayName,'A'))
SELECT id, displayName
FROM entra_id.users.users
WHERE displayName LIKE 'A%';

-- list app registrations
SELECT id, appId, displayName, signInAudience
FROM entra_id.applications.applications;

-- list groups
SELECT id, displayName, mailEnabled, securityEnabled
FROM entra_id.groups.groups;

-- add a group member (rendered on the wire as the OData $ref body)
INSERT INTO entra_id.groups.members (group_id, directoryObjectId)
SELECT '<group-id>', '<user-object-id>';
```

See [`stackql_entraid_provider/provider-dev/test/README.md`](provider-dev/test/README.md) for the pytest-based tier 1 / UAT smoke tests.

## Generating the docs

From `stackql_entraid_provider/`:

```bash
npm run generate-docs -- \
  --provider-name entra_id \
  --provider-dir ./provider-dev/openapi/src/entra_id/v00.00.00000 \
  --output-dir ./website \
  --provider-data-dir ./provider-dev/docgen/provider-data

# post-docgen curation: suppress the OData query-option params ($top/$skip/
# $search/$filter/$count/$orderby/$select/$expand - SQL primitives map to these
# via push-down) and drop @odata.type rows from field tables and examples
python3 provider-dev/scripts/curate_docs.py
```

## Publishing

To publish, push the `entra_id` directory ([`stackql_entraid_provider/provider-dev/openapi/src/entra_id`](provider-dev/openapi/src/entra_id)) to `providers/src` on a feature branch of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry) and follow the registry release flow.

## License

MIT (see [LICENSE](../LICENSE)). Microsoft Graph metadata is (c) Microsoft.
