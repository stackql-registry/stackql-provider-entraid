# `entraid` provider for [`stackql`](https://github.com/stackql/stackql)

This repository builds and documents the **`entraid`** provider for StackQL — query and manage **Microsoft Entra ID** (formerly Azure Active Directory) using SQL.

The provider is **derived from the Microsoft Graph `v1.0` OpenAPI description** (this repo originated as a fork of [`microsoftgraph/msgraph-metadata`](https://github.com/microsoftgraph/msgraph-metadata)). The identity & directory surface of Microsoft Graph is extracted, normalized, and transformed into a StackQL provider using [`@stackql/provider-utils`](https://www.npmjs.com/package/@stackql/provider-utils), following the conventions of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry).

The generated provider lives under [`provider-dev/openapi/src/entraid/`](provider-dev/openapi/src/entraid/) — a `provider.yaml` plus one OpenAPI-extension service file per service.

## Scope

Microsoft Graph spans many workloads (Exchange, SharePoint/OneDrive, Teams, Intune, Planner, Search, Security, …). The `entraid` provider deliberately exposes only the **identity & directory** workloads. From the Graph spec's `<workload>.<entity>` operation tags we keep the Entra ID workloads (users, groups, applications, service principals, directory roles, devices, domains, policies, identity governance/protection, role management, etc.) and drop the productivity ones. For the large `users` and `groups` workloads we additionally keep only their directory-relevant resources (app role assignments, authentication methods, licences, memberships, owners, …) and drop mailbox/calendar/drive/Teams resources.

The scope is encoded in [`provider-dev/scripts/entraid-discriminator.mjs`](provider-dev/scripts/entraid-discriminator.mjs).

The result is **39 services / 858 resources / 2,634 methods**, all of which `DESCRIBE` cleanly in StackQL.

## Authentication

`entraid` uses the Microsoft Graph **OAuth2 client-credentials (app-only)** grant. Register an app in Entra ID, grant it the Microsoft Graph **application** permissions you need (admin-consented), and create a client secret. Then set:

| Env var | Description |
|---|---|
| `AZURE_TENANT_ID` | Tenant ID (GUID or verified domain) — interpolated into the token endpoint |
| `AZURE_CLIENT_ID` | Application (client) ID |
| `AZURE_CLIENT_SECRET` | Client secret |

The provider's `config.auth` block (in `provider.yaml`) requests the `https://graph.microsoft.com/.default` scope against `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`.

## Building the provider

Prerequisites: Node.js ≥ 18, Python 3, and the [`stackql`](https://github.com/stackql/stackql) CLI. Install tooling with `npm install` (the `.npmrc` points the `@jsr` scope at the JSR registry).

The source Graph OpenAPI specs are already vendored under [`openapi/v1.0/`](openapi/v1.0/). The pipeline:

```bash
# 1. Split the monolithic Graph v1.0 spec into per-service specs (entraid scope only)
npm run split -- \
  --provider-name entraid \
  --api-doc openapi/v1.0/openapi.yaml \
  --svc-discriminator function \
  --svc-discriminator-fn provider-dev/scripts/entraid-discriminator.mjs \
  --output-dir provider-dev/source \
  --overwrite

# 2. Normalize schemas (flatten allOf, lift path params, etc.)
npm run normalize -- --api-dir provider-dev/source

# 3. Generate the mapping CSV, then curate it (resource/method/verb/objectKey)
npm run generate-mappings -- --input-dir provider-dev/source --output-dir provider-dev/config
python3 provider-dev/scripts/curate_mappings.py

# 4. Generate the StackQL provider
npm run generate-provider -- \
  --provider-name entraid \
  --input-dir provider-dev/source \
  --output-dir provider-dev/openapi/src/entraid \
  --config-path provider-dev/config/all_services.csv \
  --servers provider-dev/config/servers.json \
  --provider-config provider-dev/config/provider-config.json \
  --naive-req-body-translate \
  --overwrite

# 5. Validate structure (every $ref resolves) and engine load
python3 provider-dev/scripts/validate_provider.py
```

### Mapping curation

`generate-mappings` (the `analyze` step) cannot infer resource names from Graph's OData operation IDs, so [`provider-dev/scripts/curate_mappings.py`](provider-dev/scripts/curate_mappings.py) does it deterministically from the path structure:

- **Resource name** = the navigation-collection chain (root collection dropped), e.g. `/users/{id}/appRoleAssignments` → `app_role_assignments`.
- **Method / SQL verb** = derived from the HTTP verb and path shape: `GET` collection → `list`/`select`, `GET` item → `get`/`select`, `POST` → `insert`, `PATCH` → `update`, `PUT` → `replace`, `DELETE` → `delete`; bound actions → `exec`; relationship `$ref` writes → `insert`/`delete`.
- **Object key** is **schema-driven**: `$.value` is emitted only when the operation's success-response schema actually exposes a `value` array. Single-valued navigation properties (`manager`, `createdOnBehalfOf`, OData key-accessors like `federatedIdentityCredentials(name='{name}')`) and scalar/binary responses (logos, branding images, CSS) are handled accordingly — this is required, since StackQL fails a `SELECT` if the object key points at a property the response lacks.
- OData noise that does not model relationally — type-cast projections (`/graph.<type>`), `$count`, `$value` binary streams — is dropped via the `skip_this_resource` sentinel.

## Testing

```bash
ROOT="$(pwd)/provider-dev/openapi"
REG='{"url": "file://'${ROOT}'", "localDocRoot": "'${ROOT}'", "verifyConfig": {"nopVerify": true}}'

stackql exec "SHOW SERVICES IN entraid" --registry="${REG}"
stackql exec "SHOW RESOURCES IN entraid.users" --registry="${REG}"
stackql exec "DESCRIBE entraid.applications.applications" --registry="${REG}"
```

Example queries (require the auth env vars above and a live tenant):

```sql
-- list users
SELECT id, displayName, userPrincipalName, accountEnabled
FROM entraid.users.users;

-- list app registrations
SELECT id, appId, displayName, signInAudience
FROM entraid.applications.applications;

-- list groups
SELECT id, displayName, mailEnabled, securityEnabled
FROM entraid.groups.groups;

-- list service principals
SELECT id, appId, displayName, servicePrincipalType
FROM entraid.service_principals.service_principals;
```

## Generating the docs

```bash
npm run generate-docs -- \
  --provider-name entraid \
  --provider-dir ./provider-dev/openapi/src/entraid/v00.00.00000 \
  --output-dir ./website \
  --provider-data-dir ./provider-dev/docgen/provider-data
```

## Publishing

To publish, push the `entraid` directory (`provider-dev/openapi/src/entraid`) to `providers/src` on a feature branch of the [`stackql-provider-registry`](https://github.com/stackql/stackql-provider-registry) and follow the registry release flow.

## License

MIT (see [LICENSE](LICENSE)). Microsoft Graph metadata is © Microsoft.
