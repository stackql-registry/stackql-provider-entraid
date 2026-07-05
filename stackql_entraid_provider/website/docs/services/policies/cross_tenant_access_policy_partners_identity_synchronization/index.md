--- 
title: cross_tenant_access_policy_partners_identity_synchronization
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_tenant_access_policy_partners_identity_synchronization
  - policies
  - entra_id
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage entra_id resources using SQL
custom_edit_url: null
image: /img/stackql-entra_id-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>cross_tenant_access_policy_partners_identity_synchronization</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cross_tenant_access_policy_partners_identity_synchronization" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.cross_tenant_access_policy_partners_identity_synchronization" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieved navigation property

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the cross-tenant user synchronization policy. Use the name of the partner Microsoft Entra tenant to easily identify the policy. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant identifier for the partner Microsoft Entra organization. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="userSyncInbound" /></td>
    <td><code>object</code></td>
    <td>Defines whether users can be synchronized from the partner tenant. Key. (title: crossTenantUserSyncInbound)</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-cross_tenant_access_policy_configuration_partner_tenant_id"><code>cross_tenant_access_policy_configuration_partner_tenant_id</code></a></td>
    <td></td>
    <td>Get the user synchronization policy of a partner-specific configuration.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-cross_tenant_access_policy_configuration_partner_tenant_id"><code>cross_tenant_access_policy_configuration_partner_tenant_id</code></a></td>
    <td></td>
    <td>Create a cross-tenant user synchronization policy for a partner-specific configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-cross_tenant_access_policy_configuration_partner_tenant_id"><code>cross_tenant_access_policy_configuration_partner_tenant_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete the user synchronization policy for a partner-specific configuration.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-cross_tenant_access_policy_configuration_partner_tenant_id">
    <td><CopyableCode code="cross_tenant_access_policy_configuration_partner_tenant_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of crossTenantAccessPolicyConfigurationPartner</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get the user synchronization policy of a partner-specific configuration.

```sql
SELECT
displayName,
tenantId,
userSyncInbound
FROM entra_id.policies.cross_tenant_access_policy_partners_identity_synchronization
WHERE cross_tenant_access_policy_configuration_partner_tenant_id = '{{ cross_tenant_access_policy_configuration_partner_tenant_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Create a cross-tenant user synchronization policy for a partner-specific configuration.

```sql
REPLACE entra_id.policies.cross_tenant_access_policy_partners_identity_synchronization
SET 
displayName = '{{ displayName }}',
tenantId = '{{ tenantId }}',
userSyncInbound = '{{ userSyncInbound }}',
WHERE 
cross_tenant_access_policy_configuration_partner_tenant_id = '{{ cross_tenant_access_policy_configuration_partner_tenant_id }}' --required
RETURNING
displayName,
tenantId,
userSyncInbound;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete the user synchronization policy for a partner-specific configuration.

```sql
DELETE FROM entra_id.policies.cross_tenant_access_policy_partners_identity_synchronization
WHERE cross_tenant_access_policy_configuration_partner_tenant_id = '{{ cross_tenant_access_policy_configuration_partner_tenant_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
