--- 
title: multi_tenant_organization_join_request
hide_title: false
hide_table_of_contents: false
keywords:
  - multi_tenant_organization_join_request
  - tenant_relationships
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

Creates, updates, deletes, gets or lists a <code>multi_tenant_organization_join_request</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="multi_tenant_organization_join_request" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.tenant_relationships.multi_tenant_organization_join_request" /></td></tr>
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
    <td><CopyableCode code="addedByTenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID of the Microsoft Entra tenant that added a tenant to the multitenant organization. To reset a failed join request, set addedByTenantId to 00000000-0000-0000-0000-000000000000. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="memberState" /></td>
    <td><code></code></td>
    <td>State of the tenant in the multitenant organization. The possible values are: pending, active, removed, unknownFutureValue. Tenants in the pending state must join the multitenant organization to participate in the multitenant organization. Tenants in the active state can participate in the multitenant organization. Tenants in the removed state are in the process of being removed from the multitenant organization. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code></code></td>
    <td>Role of the tenant in the multitenant organization. The possible values are: owner, member (default), unknownFutureValue. Tenants with the owner role can manage the multitenant organization. There can be multiple tenants with the owner role in a multitenant organization. Tenants with the member role can participate in a multitenant organization.</td>
</tr>
<tr>
    <td><CopyableCode code="transitionDetails" /></td>
    <td><code></code></td>
    <td>Details of the processing status for a tenant joining a multitenant organization. Read-only.</td>
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
    <td>Get the status of a tenant joining a multitenant organization.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Join a multitenant organization, after the owner of the multitenant organization has added your tenant to the multitenant organization as pending. Before a tenant added to a multitenant organization can participate in the multitenant organization, the administrator of the joining tenant must submit a join request. To allow for asynchronous processing, you must wait up to 2 hours before joining a multitenant organization is completed.</td>
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

Get the status of a tenant joining a multitenant organization.

```sql
SELECT
id,
addedByTenantId,
memberState,
role,
transitionDetails
FROM entra_id.tenant_relationships.multi_tenant_organization_join_request
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

Join a multitenant organization, after the owner of the multitenant organization has added your tenant to the multitenant organization as pending. Before a tenant added to a multitenant organization can participate in the multitenant organization, the administrator of the joining tenant must submit a join request. To allow for asynchronous processing, you must wait up to 2 hours before joining a multitenant organization is completed.

```sql
UPDATE entra_id.tenant_relationships.multi_tenant_organization_join_request
SET 
id = '{{ id }}',
addedByTenantId = '{{ addedByTenantId }}',
memberState = '{{ memberState }}',
role = '{{ role }}',
transitionDetails = '{{ transitionDetails }}'
RETURNING
id,
addedByTenantId,
memberState,
role,
transitionDetails;
```
</TabItem>
</Tabs>
