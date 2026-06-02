--- 
title: cross_tenant_access_policy_default
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_tenant_access_policy_default
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

Creates, updates, deletes, gets or lists a <code>cross_tenant_access_policy_default</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cross_tenant_access_policy_default" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.cross_tenant_access_policy_default" /></td></tr>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for an entity. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="appServiceConnectInbound" /></td>
    <td><code></code></td>
    <td>Defines your default configuration for inbound app service connect settings that control which applications can connect across tenant boundaries.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticUserConsentSettings" /></td>
    <td><code></code></td>
    <td>Determines the default configuration for automatic user consent settings. The inboundAllowed and outboundAllowed properties are always false and can't be updated in the default configuration. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationInbound" /></td>
    <td><code></code></td>
    <td>Defines your default configuration for users from other organizations accessing your resources via Microsoft Entra B2B collaboration.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationOutbound" /></td>
    <td><code></code></td>
    <td>Defines your default configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B collaboration.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectInbound" /></td>
    <td><code></code></td>
    <td>Defines your default configuration for users from other organizations accessing your resources via Microsoft Entra B2B direct connect.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectOutbound" /></td>
    <td><code></code></td>
    <td>Defines your default configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B direct connect.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundTrust" /></td>
    <td><code></code></td>
    <td>Determines the default configuration for trusting other Conditional Access claims from external Microsoft Entra organizations.</td>
</tr>
<tr>
    <td><CopyableCode code="invitationRedemptionIdentityProviderConfiguration" /></td>
    <td><code></code></td>
    <td>Defines the priority order based on which an identity provider is selected during invitation redemption for a guest user.</td>
</tr>
<tr>
    <td><CopyableCode code="isServiceDefault" /></td>
    <td><code>boolean</code></td>
    <td>If true, the default configuration is set to the system default configuration. If false, the default settings are customized.</td>
</tr>
<tr>
    <td><CopyableCode code="m365CollaborationInbound" /></td>
    <td><code></code></td>
    <td>Defines your default configuration for inbound Microsoft 365 collaboration settings that determine which users from other organizations can collaborate with your organization using Microsoft 365 apps.</td>
</tr>
<tr>
    <td><CopyableCode code="m365CollaborationOutbound" /></td>
    <td><code></code></td>
    <td>Defines your default configuration for outbound Microsoft 365 collaboration settings that determine which users in your organization can collaborate with other organizations using Microsoft 365 apps.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantRestrictions" /></td>
    <td><code></code></td>
    <td>Defines the default tenant restrictions configuration for users in your organization who access an external organization on your network or devices.</td>
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
    <td></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the default configuration of a cross-tenant access policy. This default configuration may be the service default assigned by Microsoft Entra ID (isServiceDefault is true) or may be customized in your tenant (isServiceDefault is false).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the default configuration of a cross-tenant access policy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#reset_to_system_default"><CopyableCode code="reset_to_system_default" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Reset any changes made to the default configuration in a cross-tenant access policy back to the system default.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
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

Read the default configuration of a cross-tenant access policy. This default configuration may be the service default assigned by Microsoft Entra ID (isServiceDefault is true) or may be customized in your tenant (isServiceDefault is false).

```sql
SELECT
id,
@odata.type,
appServiceConnectInbound,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
inboundTrust,
invitationRedemptionIdentityProviderConfiguration,
isServiceDefault,
m365CollaborationInbound,
m365CollaborationOutbound,
tenantRestrictions
FROM entra_id.policies.cross_tenant_access_policy_default
WHERE $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update the default configuration of a cross-tenant access policy.

```sql
UPDATE entra_id.policies.cross_tenant_access_policy_default
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
appServiceConnectInbound = '{{ appServiceConnectInbound }}',
automaticUserConsentSettings = '{{ automaticUserConsentSettings }}',
b2bCollaborationInbound = '{{ b2bCollaborationInbound }}',
b2bCollaborationOutbound = '{{ b2bCollaborationOutbound }}',
b2bDirectConnectInbound = '{{ b2bDirectConnectInbound }}',
b2bDirectConnectOutbound = '{{ b2bDirectConnectOutbound }}',
inboundTrust = '{{ inboundTrust }}',
invitationRedemptionIdentityProviderConfiguration = '{{ invitationRedemptionIdentityProviderConfiguration }}',
isServiceDefault = {{ isServiceDefault }},
m365CollaborationInbound = '{{ m365CollaborationInbound }}',
m365CollaborationOutbound = '{{ m365CollaborationOutbound }}',
tenantRestrictions = '{{ tenantRestrictions }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
appServiceConnectInbound,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
inboundTrust,
invitationRedemptionIdentityProviderConfiguration,
isServiceDefault,
m365CollaborationInbound,
m365CollaborationOutbound,
tenantRestrictions;
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

No description available.

```sql
DELETE FROM entra_id.policies.cross_tenant_access_policy_default
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reset_to_system_default"
    values={[
        { label: 'reset_to_system_default', value: 'reset_to_system_default' }
    ]}
>
<TabItem value="reset_to_system_default">

Reset any changes made to the default configuration in a cross-tenant access policy back to the system default.

```sql
EXEC entra_id.policies.cross_tenant_access_policy_default.reset_to_system_default 

;
```
</TabItem>
</Tabs>
