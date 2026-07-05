--- 
title: cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration
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

Creates, updates, deletes, gets or lists a <code>cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration" /></td></tr>
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
    <td><CopyableCode code="automaticUserConsentSettings" /></td>
    <td><code></code></td>
    <td>Determines the partner-specific configuration for automatic user consent settings. Unless configured, the inboundAllowed and outboundAllowed properties are null and inherit from the default settings, which is always false.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationInbound" /></td>
    <td><code></code></td>
    <td>Defines your partner-specific configuration for users from other organizations accessing your resources via Microsoft Entra B2B collaboration.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationOutbound" /></td>
    <td><code></code></td>
    <td>Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B collaboration.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectInbound" /></td>
    <td><code></code></td>
    <td>Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect.</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectOutbound" /></td>
    <td><code></code></td>
    <td>Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B direct connect.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundTrust" /></td>
    <td><code></code></td>
    <td>Determines the partner-specific configuration for trusting other Conditional Access claims from external Microsoft Entra organizations.</td>
</tr>
<tr>
    <td><CopyableCode code="templateApplicationLevel" /></td>
    <td><code>string</code></td>
    <td> (none, newPartners, existingPartners, unknownFutureValue) (title: templateApplicationLevel)</td>
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
    <td></td>
    <td>Get the cross-tenant access policy template with inbound and outbound partner configuration settings for a multitenant organization.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Update the cross-tenant access policy template with inbound and outbound partner configuration settings for a multitenant organization.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
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

Get the cross-tenant access policy template with inbound and outbound partner configuration settings for a multitenant organization.

```sql
SELECT
id,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
inboundTrust,
templateApplicationLevel
FROM entra_id.policies.cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration
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

Update the cross-tenant access policy template with inbound and outbound partner configuration settings for a multitenant organization.

```sql
UPDATE entra_id.policies.cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration
SET 
id = '{{ id }}',
automaticUserConsentSettings = '{{ automaticUserConsentSettings }}',
b2bCollaborationInbound = '{{ b2bCollaborationInbound }}',
b2bCollaborationOutbound = '{{ b2bCollaborationOutbound }}',
b2bDirectConnectInbound = '{{ b2bDirectConnectInbound }}',
b2bDirectConnectOutbound = '{{ b2bDirectConnectOutbound }}',
inboundTrust = '{{ inboundTrust }}',
templateApplicationLevel = '{{ templateApplicationLevel }}'
RETURNING
id,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
inboundTrust,
templateApplicationLevel;
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
DELETE FROM entra_id.policies.cross_tenant_access_policy_templates_multi_tenant_organization_partner_configuration
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
