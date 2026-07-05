--- 
title: administrative_units_scoped_role_members
hide_title: false
hide_table_of_contents: false
keywords:
  - administrative_units_scoped_role_members
  - directory
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

Creates, updates, deletes, gets or lists an <code>administrative_units_scoped_role_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="administrative_units_scoped_role_members" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.administrative_units_scoped_role_members" /></td></tr>
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
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a>, <a href="#parameter-scoped_role_membership_id"><code>scoped_role_membership_id</code></a></td>
    <td></td>
    <td>Get a Microsoft Entra role assignment with administrative unit scope.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a></td>
    <td></td>
    <td>List Microsoft Entra role assignments with administrative unit scope.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a></td>
    <td></td>
    <td>Assign a Microsoft Entra role with administrative unit scope. For a list of roles that can be assigned with administrative unit scope, see Assign Microsoft Entra roles with administrative unit scope.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a>, <a href="#parameter-scoped_role_membership_id"><code>scoped_role_membership_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a>, <a href="#parameter-scoped_role_membership_id"><code>scoped_role_membership_id</code></a></td>
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
<tr id="parameter-administrative_unit_id">
    <td><CopyableCode code="administrative_unit_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of administrativeUnit</td>
</tr>
<tr id="parameter-scoped_role_membership_id">
    <td><CopyableCode code="scoped_role_membership_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of scopedRoleMembership</td>
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
administrativeUnitId,
roleId,
roleMemberInfo
FROM entra_id.directory.administrative_units_scoped_role_members
WHERE administrative_unit_id = '{{ administrative_unit_id }}' -- required
AND scoped_role_membership_id = '{{ scoped_role_membership_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Microsoft Entra role assignments with administrative unit scope.

```sql
SELECT
id,
administrativeUnitId,
roleId,
roleMemberInfo
FROM entra_id.directory.administrative_units_scoped_role_members
WHERE administrative_unit_id = '{{ administrative_unit_id }}' -- required
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
INSERT INTO entra_id.directory.administrative_units_scoped_role_members (
id,
administrativeUnitId,
roleId,
roleMemberInfo,
administrative_unit_id
)
SELECT 
'{{ id }}',
'{{ administrativeUnitId }}',
'{{ roleId }}',
'{{ roleMemberInfo }}',
'{{ administrative_unit_id }}'
RETURNING
id,
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
    - name: administrative_unit_id
      value: "{{ administrative_unit_id }}"
      description: Required parameter for the administrative_units_scoped_role_members resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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
UPDATE entra_id.directory.administrative_units_scoped_role_members
SET 
id = '{{ id }}',
administrativeUnitId = '{{ administrativeUnitId }}',
roleId = '{{ roleId }}',
roleMemberInfo = '{{ roleMemberInfo }}'
WHERE 
administrative_unit_id = '{{ administrative_unit_id }}' --required
AND scoped_role_membership_id = '{{ scoped_role_membership_id }}' --required
RETURNING
id,
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
DELETE FROM entra_id.directory.administrative_units_scoped_role_members
WHERE administrative_unit_id = '{{ administrative_unit_id }}' --required
AND scoped_role_membership_id = '{{ scoped_role_membership_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
