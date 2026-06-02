--- 
title: app_role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - app_role_assignments
  - service_principals
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

Creates, updates, deletes, gets or lists an <code>app_role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_role_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.app_role_assignments" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="appRoleId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The identifier (id) for the app role that's assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application hasn't declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user, group, or service principal that was granted the app role assignment. Maximum length is 256 characters. Read-only. Supports $filter (eq and startswith).</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create. (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource app's service principal to which the assignment is made. Maximum length is 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only). (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="appRoleId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The identifier (id) for the app role that's assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application hasn't declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user, group, or service principal that was granted the app role assignment. Maximum length is 256 characters. Read-only. Supports $filter (eq and startswith).</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create. (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource app's service principal to which the assignment is made. Maximum length is 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only). (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
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
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-appRoleAssignment-id"><code>appRoleAssignment-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of an appRoleAssignment object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of an appRoleAssignment object.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Assign an app role to a client service principal. App roles that are assigned to service principals are also known as application permissions. Application permissions can be granted directly with app role assignments, or through a consent experience. To grant an app role assignment to a client service principal, you need three identifiers:</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-appRoleAssignment-id"><code>appRoleAssignment-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-appRoleAssignment-id"><code>appRoleAssignment-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes an appRoleAssignment that a service principal has been granted. App roles which are assigned to service principals are also known as application permissions. Deleting an app role assignment for a service principal is equivalent to revoking the app-only permission grant.</td>
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
<tr id="parameter-appRoleAssignment-id">
    <td><CopyableCode code="appRoleAssignment-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of appRoleAssignment</td>
</tr>
<tr id="parameter-servicePrincipal-id">
    <td><CopyableCode code="servicePrincipal-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
</tr>
<tr id="parameter-$count">
    <td><CopyableCode code="$count" /></td>
    <td><code>boolean</code></td>
    <td>Include count of items</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter items by property values</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>array</code></td>
    <td>Order items by property values</td>
</tr>
<tr id="parameter-$search">
    <td><CopyableCode code="$search" /></td>
    <td><code>string</code></td>
    <td>Search items by search phrases</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Skip the first n items</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Show only the first n items (example: 50)</td>
</tr>
<tr id="parameter-ConsistencyLevel">
    <td><CopyableCode code="ConsistencyLevel" /></td>
    <td><code>string</code></td>
    <td>Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries</td>
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

Read the properties and relationships of an appRoleAssignment object.

```sql
SELECT
id,
@odata.type,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId
FROM entra_id.service_principals.app_role_assignments
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
AND appRoleAssignment-id = '{{ appRoleAssignment-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Read the properties and relationships of an appRoleAssignment object.

```sql
SELECT
id,
@odata.type,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId
FROM entra_id.service_principals.app_role_assignments
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
AND ConsistencyLevel = '{{ ConsistencyLevel }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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

Assign an app role to a client service principal. App roles that are assigned to service principals are also known as application permissions. Application permissions can be granted directly with app role assignments, or through a consent experience. To grant an app role assignment to a client service principal, you need three identifiers:

```sql
INSERT INTO entra_id.service_principals.app_role_assignments (
id,
@odata.type,
deletedDateTime,
appRoleId,
createdDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId,
servicePrincipal-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
'{{ appRoleId }}',
'{{ createdDateTime }}',
'{{ principalDisplayName }}',
'{{ principalId }}',
'{{ principalType }}',
'{{ resourceDisplayName }}',
'{{ resourceId }}',
'{{ servicePrincipal-id }}'
RETURNING
id,
@odata.type,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_role_assignments
  props:
    - name: servicePrincipal-id
      value: "{{ servicePrincipal-id }}"
      description: Required parameter for the app_role_assignments resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: appRoleId
      value: "{{ appRoleId }}"
      description: |
        The identifier (id) for the app role that's assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application hasn't declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: principalDisplayName
      value: "{{ principalDisplayName }}"
      description: |
        The display name of the user, group, or service principal that was granted the app role assignment. Maximum length is 256 characters. Read-only. Supports $filter (eq and startswith).
    - name: principalId
      value: "{{ principalId }}"
      description: |
        The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create.
    - name: principalType
      value: "{{ principalType }}"
      description: |
        The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.
    - name: resourceDisplayName
      value: "{{ resourceDisplayName }}"
      description: |
        The display name of the resource app's service principal to which the assignment is made. Maximum length is 256 characters.
    - name: resourceId
      value: "{{ resourceId }}"
      description: |
        The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).
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

No description available.

```sql
UPDATE entra_id.service_principals.app_role_assignments
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
appRoleId = '{{ appRoleId }}',
createdDateTime = '{{ createdDateTime }}',
principalDisplayName = '{{ principalDisplayName }}',
principalId = '{{ principalId }}',
principalType = '{{ principalType }}',
resourceDisplayName = '{{ resourceDisplayName }}',
resourceId = '{{ resourceId }}'
WHERE 
servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND appRoleAssignment-id = '{{ appRoleAssignment-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId;
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

Deletes an appRoleAssignment that a service principal has been granted. App roles which are assigned to service principals are also known as application permissions. Deleting an app role assignment for a service principal is equivalent to revoking the app-only permission grant.

```sql
DELETE FROM entra_id.service_principals.app_role_assignments
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND appRoleAssignment-id = '{{ appRoleAssignment-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
