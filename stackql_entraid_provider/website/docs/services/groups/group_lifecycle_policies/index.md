--- 
title: group_lifecycle_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - group_lifecycle_policies
  - groups
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

Creates, updates, deletes, gets or lists a <code>group_lifecycle_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="group_lifecycle_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.groups.group_lifecycle_policies" /></td></tr>
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
    <td><CopyableCode code="alternateNotificationEmails" /></td>
    <td><code>string</code></td>
    <td>List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.</td>
</tr>
<tr>
    <td><CopyableCode code="groupLifetimeInDays" /></td>
    <td><code>number (int32)</code></td>
    <td>Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.</td>
</tr>
<tr>
    <td><CopyableCode code="managedGroupTypes" /></td>
    <td><code>string</code></td>
    <td>The group type for which the expiration policy applies. Possible values are All, Selected or None.</td>
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
    <td><CopyableCode code="alternateNotificationEmails" /></td>
    <td><code>string</code></td>
    <td>List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.</td>
</tr>
<tr>
    <td><CopyableCode code="groupLifetimeInDays" /></td>
    <td><code>number (int32)</code></td>
    <td>Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.</td>
</tr>
<tr>
    <td><CopyableCode code="managedGroupTypes" /></td>
    <td><code>string</code></td>
    <td>The group type for which the expiration policy applies. Possible values are All, Selected or None.</td>
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
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-groupLifecyclePolicy-id"><code>groupLifecyclePolicy-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The collection of lifecycle policies for this group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieves a list of groupLifecyclePolicy objects to which a group belongs.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-groupLifecyclePolicy-id"><code>groupLifecyclePolicy-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-groupLifecyclePolicy-id"><code>groupLifecyclePolicy-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#add_group"><CopyableCode code="add_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-groupLifecyclePolicy-id"><code>groupLifecyclePolicy-id</code></a></td>
    <td></td>
    <td>Add a group to a groupLifecyclePolicy. This action is supported only if the managedGroupTypes property of the policy is set to Selected.</td>
</tr>
<tr>
    <td><a href="#remove_group"><CopyableCode code="remove_group" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-groupLifecyclePolicy-id"><code>groupLifecyclePolicy-id</code></a></td>
    <td></td>
    <td>Removes a group from a lifecycle policy.</td>
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
<tr id="parameter-group-id">
    <td><CopyableCode code="group-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of group</td>
</tr>
<tr id="parameter-groupLifecyclePolicy-id">
    <td><CopyableCode code="groupLifecyclePolicy-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of groupLifecyclePolicy</td>
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

The collection of lifecycle policies for this group. Read-only. Nullable.

```sql
SELECT
id,
@odata.type,
alternateNotificationEmails,
groupLifetimeInDays,
managedGroupTypes
FROM entra_id.groups.group_lifecycle_policies
WHERE group-id = '{{ group-id }}' -- required
AND groupLifecyclePolicy-id = '{{ groupLifecyclePolicy-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of groupLifecyclePolicy objects to which a group belongs.

```sql
SELECT
id,
@odata.type,
alternateNotificationEmails,
groupLifetimeInDays,
managedGroupTypes
FROM entra_id.groups.group_lifecycle_policies
WHERE group-id = '{{ group-id }}' -- required
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

No description available.

```sql
INSERT INTO entra_id.groups.group_lifecycle_policies (
id,
@odata.type,
alternateNotificationEmails,
groupLifetimeInDays,
managedGroupTypes,
group-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ alternateNotificationEmails }}',
{{ groupLifetimeInDays }},
'{{ managedGroupTypes }}',
'{{ group-id }}'
RETURNING
id,
@odata.type,
alternateNotificationEmails,
groupLifetimeInDays,
managedGroupTypes
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: group_lifecycle_policies
  props:
    - name: group-id
      value: "{{ group-id }}"
      description: Required parameter for the group_lifecycle_policies resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: alternateNotificationEmails
      value: "{{ alternateNotificationEmails }}"
      description: |
        List of email address to send notifications for groups without owners. Multiple email address can be defined by separating email address with a semicolon.
    - name: groupLifetimeInDays
      value: {{ groupLifetimeInDays }}
      description: |
        Number of days before a group expires and needs to be renewed. Once renewed, the group expiration is extended by the number of days defined.
    - name: managedGroupTypes
      value: "{{ managedGroupTypes }}"
      description: |
        The group type for which the expiration policy applies. Possible values are All, Selected or None.
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
UPDATE entra_id.groups.group_lifecycle_policies
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
alternateNotificationEmails = '{{ alternateNotificationEmails }}',
groupLifetimeInDays = {{ groupLifetimeInDays }},
managedGroupTypes = '{{ managedGroupTypes }}'
WHERE 
group-id = '{{ group-id }}' --required
AND groupLifecyclePolicy-id = '{{ groupLifecyclePolicy-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
alternateNotificationEmails,
groupLifetimeInDays,
managedGroupTypes;
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
DELETE FROM entra_id.groups.group_lifecycle_policies
WHERE group-id = '{{ group-id }}' --required
AND groupLifecyclePolicy-id = '{{ groupLifecyclePolicy-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="add_group"
    values={[
        { label: 'add_group', value: 'add_group' },
        { label: 'remove_group', value: 'remove_group' }
    ]}
>
<TabItem value="add_group">

Add a group to a groupLifecyclePolicy. This action is supported only if the managedGroupTypes property of the policy is set to Selected.

```sql
EXEC entra_id.groups.group_lifecycle_policies.add_group 
@group-id='{{ group-id }}' --required, 
@groupLifecyclePolicy-id='{{ groupLifecyclePolicy-id }}' --required 
@@json=
'{
"groupId": "{{ groupId }}"
}'
;
```
</TabItem>
<TabItem value="remove_group">

Removes a group from a lifecycle policy.

```sql
EXEC entra_id.groups.group_lifecycle_policies.remove_group 
@group-id='{{ group-id }}' --required, 
@groupLifecyclePolicy-id='{{ groupLifecyclePolicy-id }}' --required 
@@json=
'{
"groupId": "{{ groupId }}"
}'
;
```
</TabItem>
</Tabs>
