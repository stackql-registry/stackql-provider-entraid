--- 
title: administrative_units_scoped_role_members
hide_title: false
hide_table_of_contents: false
keywords:
  - administrative_units_scoped_role_members
  - directory
  - entraid
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage entraid resources using SQL
custom_edit_url: null
image: /img/stackql-entraid-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>administrative_units_scoped_role_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="administrative_units_scoped_role_members" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.directory.administrative_units_scoped_role_members" /></td></tr>
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
    <td><CopyableCode code="administrativeUnitId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the administrative unit that the directory role is scoped to</td>
</tr>
<tr>
    <td><CopyableCode code="roleId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the directory role that the member is in.</td>
</tr>
<tr>
    <td><CopyableCode code="roleMemberInfo" /></td>
    <td><code>object</code></td>
    <td> (title: identity)</td>
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
    <td><CopyableCode code="administrativeUnitId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the administrative unit that the directory role is scoped to</td>
</tr>
<tr>
    <td><CopyableCode code="roleId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the directory role that the member is in.</td>
</tr>
<tr>
    <td><CopyableCode code="roleMemberInfo" /></td>
    <td><code>object</code></td>
    <td> (title: identity)</td>
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
    <td><a href="#parameter-administrativeUnit-id"><code>administrativeUnit-id</code></a>, <a href="#parameter-scopedRoleMembership-id"><code>scopedRoleMembership-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a Microsoft Entra role assignment with administrative unit scope.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-administrativeUnit-id"><code>administrativeUnit-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>List Microsoft Entra role assignments with administrative unit scope.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-administrativeUnit-id"><code>administrativeUnit-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Assign a Microsoft Entra role with administrative unit scope. For a list of roles that can be assigned with administrative unit scope, see Assign Microsoft Entra roles with administrative unit scope.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-administrativeUnit-id"><code>administrativeUnit-id</code></a>, <a href="#parameter-scopedRoleMembership-id"><code>scopedRoleMembership-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-administrativeUnit-id"><code>administrativeUnit-id</code></a>, <a href="#parameter-scopedRoleMembership-id"><code>scopedRoleMembership-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a Microsoft Entra role assignment with administrative unit scope.</td>
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
<tr id="parameter-administrativeUnit-id">
    <td><CopyableCode code="administrativeUnit-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of administrativeUnit</td>
</tr>
<tr id="parameter-scopedRoleMembership-id">
    <td><CopyableCode code="scopedRoleMembership-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of scopedRoleMembership</td>
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

Get a Microsoft Entra role assignment with administrative unit scope.

```sql
SELECT
id,
@odata.type,
administrativeUnitId,
roleId,
roleMemberInfo
FROM entraid.directory.administrative_units_scoped_role_members
WHERE administrativeUnit-id = '{{ administrativeUnit-id }}' -- required
AND scopedRoleMembership-id = '{{ scopedRoleMembership-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List Microsoft Entra role assignments with administrative unit scope.

```sql
SELECT
id,
@odata.type,
administrativeUnitId,
roleId,
roleMemberInfo
FROM entraid.directory.administrative_units_scoped_role_members
WHERE administrativeUnit-id = '{{ administrativeUnit-id }}' -- required
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

Assign a Microsoft Entra role with administrative unit scope. For a list of roles that can be assigned with administrative unit scope, see Assign Microsoft Entra roles with administrative unit scope.

```sql
INSERT INTO entraid.directory.administrative_units_scoped_role_members (
id,
@odata.type,
administrativeUnitId,
roleId,
roleMemberInfo,
administrativeUnit-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ administrativeUnitId }}',
'{{ roleId }}',
'{{ roleMemberInfo }}',
'{{ administrativeUnit-id }}'
RETURNING
id,
@odata.type,
administrativeUnitId,
roleId,
roleMemberInfo
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: administrative_units_scoped_role_members
  props:
    - name: administrativeUnit-id
      value: "{{ administrativeUnit-id }}"
      description: Required parameter for the administrative_units_scoped_role_members resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: administrativeUnitId
      value: "{{ administrativeUnitId }}"
      description: |
        Unique identifier for the administrative unit that the directory role is scoped to
    - name: roleId
      value: "{{ roleId }}"
      description: |
        Unique identifier for the directory role that the member is in.
    - name: roleMemberInfo
      value:
        displayName: "{{ displayName }}"
        id: "{{ id }}"
        @odata.type: "{{ @odata.type }}"
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
UPDATE entraid.directory.administrative_units_scoped_role_members
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
administrativeUnitId = '{{ administrativeUnitId }}',
roleId = '{{ roleId }}',
roleMemberInfo = '{{ roleMemberInfo }}'
WHERE 
administrativeUnit-id = '{{ administrativeUnit-id }}' --required
AND scopedRoleMembership-id = '{{ scopedRoleMembership-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
administrativeUnitId,
roleId,
roleMemberInfo;
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

Remove a Microsoft Entra role assignment with administrative unit scope.

```sql
DELETE FROM entraid.directory.administrative_units_scoped_role_members
WHERE administrativeUnit-id = '{{ administrativeUnit-id }}' --required
AND scopedRoleMembership-id = '{{ scopedRoleMembership-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
