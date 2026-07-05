--- 
title: multi_tenant_organization_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - multi_tenant_organization_tenants
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

Creates, updates, deletes, gets or lists a <code>multi_tenant_organization_tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="multi_tenant_organization_tenants" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.tenant_relationships.multi_tenant_organization_tenants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
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
    <td><code>string (uuid)</code></td>
    <td>Tenant ID of the tenant that added the tenant to the multitenant organization. Read-only. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="addedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the tenant was added to the multitenant organization. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the tenant added to the multitenant organization.</td>
</tr>
<tr>
    <td><CopyableCode code="joinedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the tenant joined the multitenant organization. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code></code></td>
    <td>Role of the tenant in the multitenant organization. The possible values are: owner, member (default), unknownFutureValue. Tenants with the owner role can manage the multitenant organization but tenants with the member role can only participate in a multitenant organization. There can be multiple tenants with the owner role in a multitenant organization.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>State of the tenant in the multitenant organization. The possible values are: pending, active, removed, unknownFutureValue. Tenants in the pending state must join the multitenant organization to participate in the multitenant organization. Tenants in the active state can participate in the multitenant organization. Tenants in the removed state are in the process of being removed from the multitenant organization. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID of the Microsoft Entra tenant added to the multitenant organization. Set at the time tenant is added.Supports $filter. Key.</td>
</tr>
<tr>
    <td><CopyableCode code="transitionDetails" /></td>
    <td><code></code></td>
    <td>Details of the processing status for a tenant in a multitenant organization. Read-only. Nullable.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

Retrieved collection

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
    <td><code>string (uuid)</code></td>
    <td>Tenant ID of the tenant that added the tenant to the multitenant organization. Read-only. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="addedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the tenant was added to the multitenant organization. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the tenant added to the multitenant organization.</td>
</tr>
<tr>
    <td><CopyableCode code="joinedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the tenant joined the multitenant organization. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code></code></td>
    <td>Role of the tenant in the multitenant organization. The possible values are: owner, member (default), unknownFutureValue. Tenants with the owner role can manage the multitenant organization but tenants with the member role can only participate in a multitenant organization. There can be multiple tenants with the owner role in a multitenant organization.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>State of the tenant in the multitenant organization. The possible values are: pending, active, removed, unknownFutureValue. Tenants in the pending state must join the multitenant organization to participate in the multitenant organization. Tenants in the active state can participate in the multitenant organization. Tenants in the removed state are in the process of being removed from the multitenant organization. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant ID of the Microsoft Entra tenant added to the multitenant organization. Set at the time tenant is added.Supports $filter. Key.</td>
</tr>
<tr>
    <td><CopyableCode code="transitionDetails" /></td>
    <td><code></code></td>
    <td>Details of the processing status for a tenant in a multitenant organization. Read-only. Nullable.</td>
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
    <td><a href="#parameter-multi_tenant_organization_member_id"><code>multi_tenant_organization_member_id</code></a></td>
    <td></td>
    <td>Get a tenant and its properties in the multitenant organization.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>List the tenants and their properties in the multitenant organization.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Add a tenant to a multitenant organization. The administrator of an owner tenant has the permissions to add tenants to the multitenant organization. The added tenant is in the pending state until the administrator of the added tenant joins the multitenant organization by submitting a join request. A tenant can be part of only one multitenant organization.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-multi_tenant_organization_member_id"><code>multi_tenant_organization_member_id</code></a></td>
    <td></td>
    <td>Update the properties of a tenant in a multitenant organization. Only owner tenants can call this API.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-multi_tenant_organization_member_id"><code>multi_tenant_organization_member_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a tenant from a multitenant organization. A tenant can be removed in the following scenarios:</td>
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
<tr id="parameter-multi_tenant_organization_member_id">
    <td><CopyableCode code="multi_tenant_organization_member_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of multiTenantOrganizationMember</td>
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
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a tenant and its properties in the multitenant organization.

```sql
SELECT
id,
addedByTenantId,
addedDateTime,
deletedDateTime,
displayName,
joinedDateTime,
role,
state,
tenantId,
transitionDetails
FROM entra_id.tenant_relationships.multi_tenant_organization_tenants
WHERE multi_tenant_organization_member_id = '{{ multi_tenant_organization_member_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the tenants and their properties in the multitenant organization.

```sql
SELECT
id,
addedByTenantId,
addedDateTime,
deletedDateTime,
displayName,
joinedDateTime,
role,
state,
tenantId,
transitionDetails
FROM entra_id.tenant_relationships.multi_tenant_organization_tenants
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="insert"
    values={[
        { label: 'insert', value: 'insert' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="insert">

Add a tenant to a multitenant organization. The administrator of an owner tenant has the permissions to add tenants to the multitenant organization. The added tenant is in the pending state until the administrator of the added tenant joins the multitenant organization by submitting a join request. A tenant can be part of only one multitenant organization.

```sql
INSERT INTO entra_id.tenant_relationships.multi_tenant_organization_tenants (
id,
deletedDateTime,
addedByTenantId,
addedDateTime,
displayName,
joinedDateTime,
role,
state,
tenantId,
transitionDetails
)
SELECT 
'{{ id }}',
'{{ deletedDateTime }}',
'{{ addedByTenantId }}',
'{{ addedDateTime }}',
'{{ displayName }}',
'{{ joinedDateTime }}',
'{{ role }}',
'{{ state }}',
'{{ tenantId }}',
'{{ transitionDetails }}'
RETURNING
id,
addedByTenantId,
addedDateTime,
deletedDateTime,
displayName,
joinedDateTime,
role,
state,
tenantId,
transitionDetails
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: multi_tenant_organization_tenants
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: addedByTenantId
      value: "{{ addedByTenantId }}"
      description: |
        Tenant ID of the tenant that added the tenant to the multitenant organization. Read-only.
    - name: addedDateTime
      value: "{{ addedDateTime }}"
      description: |
        Date and time when the tenant was added to the multitenant organization. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name of the tenant added to the multitenant organization.
    - name: joinedDateTime
      value: "{{ joinedDateTime }}"
      description: |
        Date and time when the tenant joined the multitenant organization. Read-only.
    - name: role
      value: "{{ role }}"
      description: |
        Role of the tenant in the multitenant organization. The possible values are: owner, member (default), unknownFutureValue. Tenants with the owner role can manage the multitenant organization but tenants with the member role can only participate in a multitenant organization. There can be multiple tenants with the owner role in a multitenant organization.
    - name: state
      value: "{{ state }}"
      description: |
        State of the tenant in the multitenant organization. The possible values are: pending, active, removed, unknownFutureValue. Tenants in the pending state must join the multitenant organization to participate in the multitenant organization. Tenants in the active state can participate in the multitenant organization. Tenants in the removed state are in the process of being removed from the multitenant organization. Read-only.
    - name: tenantId
      value: "{{ tenantId }}"
      description: |
        Tenant ID of the Microsoft Entra tenant added to the multitenant organization. Set at the time tenant is added.Supports $filter. Key.
    - name: transitionDetails
      value: "{{ transitionDetails }}"
      description: |
        Details of the processing status for a tenant in a multitenant organization. Read-only. Nullable.
`}</CodeBlock>

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

Update the properties of a tenant in a multitenant organization. Only owner tenants can call this API.

```sql
UPDATE entra_id.tenant_relationships.multi_tenant_organization_tenants
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
addedByTenantId = '{{ addedByTenantId }}',
addedDateTime = '{{ addedDateTime }}',
displayName = '{{ displayName }}',
joinedDateTime = '{{ joinedDateTime }}',
role = '{{ role }}',
state = '{{ state }}',
tenantId = '{{ tenantId }}',
transitionDetails = '{{ transitionDetails }}'
WHERE 
multi_tenant_organization_member_id = '{{ multi_tenant_organization_member_id }}' --required
RETURNING
id,
addedByTenantId,
addedDateTime,
deletedDateTime,
displayName,
joinedDateTime,
role,
state,
tenantId,
transitionDetails;
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

Remove a tenant from a multitenant organization. A tenant can be removed in the following scenarios:

```sql
DELETE FROM entra_id.tenant_relationships.multi_tenant_organization_tenants
WHERE multi_tenant_organization_member_id = '{{ multi_tenant_organization_member_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
