# Giving the `entra_id` provider access to your tenant

## What you need

One app principal with:

1. These Microsoft Graph **Application** permissions, admin-consented:
   `Directory.Read.All`, `Application.Read.All`, `AuditLog.Read.All`,
   `Policy.Read.All`, `RoleManagement.Read.Directory`
2. A **client secret** (auth is app-only — no signed-in user, so permissions
   must be *Application* type, not *Delegated*).

Prereq: `az login` as a Global / Privileged Role / Cloud Application Admin.

## Which app?

- **Local** (under *App registrations* — you own it) → **A**
- **Foreign** (only under *Enterprise applications*, owned by another tenant) → **B**

## A. Local app

```bash
bin/setup-app-registration.sh <CLIENT_ID>
```
Adds the permissions + admin consent. Then add a secret under *Certificates &
secrets*.

## B. Foreign app

Can't edit its registration; copy the roles onto its service principal from a
local app that's already set up:

```bash
bin/mirror-app-permissions.sh <SOURCE_CLIENT_ID> <FOREIGN_CLIENT_ID>
```
(API-only — no portal UI. A public/native foreign app has no secret, so it
can't do app-only auth until it gets one.)

## Verify

```bash
SP=$(az ad sp show --id <CLIENT_ID> --query id -o tsv)
az rest --method GET --url "https://graph.microsoft.com/v1.0/servicePrincipals/$SP/appRoleAssignments" --query "value[].appRoleId" -o tsv
```
Five GUIDs back = done.

## Query

```bash
export AZURE_TENANT_ID=<TENANT_ID> AZURE_CLIENT_ID=<CLIENT_ID> AZURE_CLIENT_SECRET=<secret>
ROOT="$(pwd)/provider-dev/openapi"
REG='{"url":"file://'${ROOT}'","localDocRoot":"'${ROOT}'","verifyConfig":{"nopVerify":true}}'
stackql exec "SELECT id, displayName FROM entra_id.users.users" --registry="${REG}"
```
