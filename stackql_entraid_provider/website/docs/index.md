---
title: entra_id
hide_title: false
hide_table_of_contents: false
keywords:
  - entra_id
  - entra
  - azuread
  - microsoft graph
  - identity
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Entra ID resources using SQL
custom_edit_url: null
image: /img/stackql-entra_id-provider-featured-image.png
id: 'provider-intro'
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Identity and directory management for Microsoft Entra ID (formerly Azure Active Directory), derived from the Microsoft Graph `v1.0` API.


:::info[Provider Summary] 

total services: __39__  
total resources: __849__  

:::

See also:
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * *

## Installation

To pull the latest version of the `entra_id` provider, run the following command:

```bash
REGISTRY PULL entra_id;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).

## Authentication

The `entra_id` provider authenticates to Microsoft Graph using the OAuth2 **client credentials** (app-only) grant. Register an application in Microsoft Entra ID, grant it the required Microsoft Graph **application** permissions (and admin-consent them), then create a client secret.

The following system environment variables are used for authentication by default:

- <CopyableCode code="AZURE_TENANT_ID" /> - your Entra ID tenant ID (GUID or verified domain), used in the token endpoint
- <CopyableCode code="AZURE_CLIENT_ID" /> - the application (client) ID of your app registration
- <CopyableCode code="AZURE_CLIENT_SECRET" /> - a client secret for the app registration

These variables are sourced at runtime (from the local machine or as CI variables/secrets).

<details>

<summary>Using different environment variables</summary>

To use different environment variables (instead of the defaults), use the `--auth` flag of the `stackql` program.  For example:

```bash

AUTH='{ "entra_id": { "type": "oauth2", "grant_type": "client_credentials", "client_id_env_var": "MY_CLIENT_ID", "client_secret_env_var": "MY_CLIENT_SECRET", "token_url": "https://login.microsoftonline.com/{{ .__env__MY_TENANT_ID }}/oauth2/v2.0/token", "scopes": ["https://graph.microsoft.com/.default"] }}'
stackql shell --auth="${AUTH}"

```
</details>

## Example Queries

Try the following queries using `stackql shell`, or run them from a script or CI pipeline with `stackql exec`.

### Users with account status and UPN

Every user in the tenant with its sign-in status, user type and organisational attributes, sorted by name:

```sql
SELECT id, displayName, userPrincipalName, accountEnabled, userType,
       mail, jobTitle, department, createdDateTime
FROM entra_id.users.users
ORDER BY displayName;
```

### Groups and their members

All groups with their type, visibility and dynamic membership rule, then the direct user members of one group (the `members` resource returns directory object IDs, so the join to `users` supplies the names):

```sql
SELECT id, displayName, mailEnabled, securityEnabled, groupTypes,
       membershipRule, visibility, createdDateTime
FROM entra_id.groups.groups;

SELECT u.displayName, u.userPrincipalName, u.mail
FROM entra_id.groups.members m
JOIN entra_id.users.users u ON u.id = m.id
WHERE m.group_id = '{{ group_id }}';
```

### App registrations with credentials

App registrations that hold at least one client secret or certificate, with the number of each and the expiry of the first listed secret:

```sql
SELECT displayName, appId, signInAudience,
       json_array_length(passwordCredentials) AS secret_count,
       json_extract(passwordCredentials, '$[0].endDateTime') AS first_secret_expiry,
       json_array_length(keyCredentials) AS certificate_count
FROM entra_id.applications.applications
WHERE json_array_length(passwordCredentials) > 0
   OR json_array_length(keyCredentials) > 0;
```

### Service principals

Enterprise applications, managed identities and other service principals in the tenant, with the principal type and whether sign-in is enabled:

```sql
SELECT id, appId, displayName, servicePrincipalType, accountEnabled,
       appOwnerOrganizationId, appRoleAssignmentRequired
FROM entra_id.service_principals.service_principals;
```

### Directory roles and their members

The directory roles activated in the tenant, then the users that hold one of them:

```sql
SELECT id, displayName, description, roleTemplateId
FROM entra_id.directory_roles.directory_roles;

SELECT u.displayName, u.userPrincipalName, u.mail
FROM entra_id.directory_roles.members m
JOIN entra_id.users.users u ON u.id = m.id
WHERE m.directory_role_id = '{{ directory_role_id }}';
```

### Conditional access policies

Enabled policies that require multifactor authentication for all users, with the applications each one covers:

```sql
SELECT displayName, state,
       json_extract(conditions, '$.applications.includeApplications') AS include_applications,
       json_extract(grantControls, '$.builtInControls') AS built_in_controls
FROM entra_id.identity.conditional_access_policies
WHERE state = 'enabled'
  AND json_extract(conditions, '$.users.includeUsers') LIKE '%All%'
  AND json_extract(grantControls, '$.builtInControls') LIKE '%mfa%';
```

### Failed sign-ins for one user

Sign-ins by one user that did not succeed, newest first, with the application, client, conditional access outcome and failure reason (the user predicate is pushed to Graph as `$filter` and the sort as `$orderby`):

```sql
SELECT createdDateTime, appDisplayName, clientAppUsed, ipAddress,
       conditionalAccessStatus,
       json_extract(status, '$.errorCode') AS error_code,
       json_extract(status, '$.failureReason') AS failure_reason
FROM entra_id.audit_logs.sign_ins
WHERE userPrincipalName = 'alice@example.com'
  AND json_extract(status, '$.errorCode') <> 0
ORDER BY createdDateTime DESC;
```

### Guest users

External (B2B) accounts in the tenant with their invitation state (the predicate is pushed to Graph as `$filter=userType eq 'Guest'`):

```sql
SELECT id, displayName, userPrincipalName, mail, externalUserState, createdDateTime
FROM entra_id.users.users
WHERE userType = 'Guest';
```

### Device posture by operating system

Registered devices counted by operating system, compliance state and management state:

```sql
SELECT operatingSystem, isCompliant, isManaged, COUNT(*) AS device_count
FROM entra_id.devices.devices
GROUP BY operatingSystem, isCompliant, isManaged
ORDER BY device_count DESC;
```

### Group provisioning

Create a security group, add a member to it (relationship writes take the target object ID as `directoryObjectId`), update its description and finally delete it:

```sql
INSERT INTO entra_id.groups.groups (displayName, mailNickname, mailEnabled, securityEnabled, description)
SELECT 'Platform Engineering', 'platform-engineering', false, true, 'Platform engineering team';

INSERT INTO entra_id.groups.members (group_id, directoryObjectId)
SELECT '{{ group_id }}', '{{ directoryObjectId }}';

UPDATE entra_id.groups.groups
SET description = 'Platform engineering team, owned by the CTO office'
WHERE group_id = '{{ group_id }}';

DELETE FROM entra_id.groups.groups
WHERE group_id = '{{ group_id }}';
```


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/services/agreement_acceptances">agreement_acceptances</a><br />
<a href="/services/agreements">agreements</a><br />
<a href="/services/application_templates">application_templates</a><br />
<a href="/services/applications">applications</a><br />
<a href="/services/audit_logs">audit_logs</a><br />
<a href="/services/authentication_method_configurations">authentication_method_configurations</a><br />
<a href="/services/authentication_methods_policy">authentication_methods_policy</a><br />
<a href="/services/certificate_based_auth_configuration">certificate_based_auth_configuration</a><br />
<a href="/services/contracts">contracts</a><br />
<a href="/services/data_policy_operations">data_policy_operations</a><br />
<a href="/services/devices">devices</a><br />
<a href="/services/directory">directory</a><br />
<a href="/services/directory_objects">directory_objects</a><br />
<a href="/services/directory_role_templates">directory_role_templates</a><br />
<a href="/services/directory_roles">directory_roles</a><br />
<a href="/services/domain_dns_records">domain_dns_records</a><br />
<a href="/services/domains">domains</a><br />
<a href="/services/group_lifecycle_policies">group_lifecycle_policies</a><br />
<a href="/services/group_setting_templates">group_setting_templates</a><br />
<a href="/services/group_settings">group_settings</a><br />
</div>
<div class="providerDocColumn">
<a href="/services/groups">groups</a><br />
<a href="/services/identity">identity</a><br />
<a href="/services/identity_governance">identity_governance</a><br />
<a href="/services/identity_protection">identity_protection</a><br />
<a href="/services/identity_providers">identity_providers</a><br />
<a href="/services/invitations">invitations</a><br />
<a href="/services/oauth2_permission_grants">oauth2_permission_grants</a><br />
<a href="/services/org_contacts">org_contacts</a><br />
<a href="/services/organization">organization</a><br />
<a href="/services/permission_grants">permission_grants</a><br />
<a href="/services/policies">policies</a><br />
<a href="/services/role_management">role_management</a><br />
<a href="/services/schema_extensions">schema_extensions</a><br />
<a href="/services/scoped_role_memberships">scoped_role_memberships</a><br />
<a href="/services/service_principals">service_principals</a><br />
<a href="/services/subscribed_skus">subscribed_skus</a><br />
<a href="/services/synchronization">synchronization</a><br />
<a href="/services/tenant_relationships">tenant_relationships</a><br />
<a href="/services/users">users</a><br />
</div>
</div>
