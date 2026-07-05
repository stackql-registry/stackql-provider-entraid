--- 
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
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

Creates, updates, deletes, gets or lists a <code>members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="members" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.groups.members" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a></td>
    <td>Get a list of the group's direct members. A group can have users, organizational contacts, devices, service principals and other groups as members. This operation is not transitive.</td>
</tr>
<tr>
    <td><a href="#add_ref"><CopyableCode code="add_ref" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>Add a member to a security or Microsoft 365 group. When using the API to add multiple members in one request, you can add up to only 20 members.  The following table shows the types of members that can be added to either security groups or Microsoft 365 groups.</td>
</tr>
<tr>
    <td><a href="#remove_ref"><CopyableCode code="remove_ref" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-directory_object_id"><code>directory_object_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a member from a group via the members navigation property. You can't remove a member from groups with dynamic memberships.</td>
</tr>
<tr>
    <td><a href="#remove_ref_2"><CopyableCode code="remove_ref_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a member from a group via the members navigation property. You can't remove a member from groups with dynamic memberships.</td>
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
<tr id="parameter-directory_object_id">
    <td><CopyableCode code="directory_object_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryObject</td>
</tr>
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of group</td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Get a list of the group's direct members. A group can have users, organizational contacts, devices, service principals and other groups as members. This operation is not transitive.

```sql
SELECT
id,
deletedDateTime
FROM entra_id.groups.members
WHERE group_id = '{{ group_id }}' -- required
AND ConsistencyLevel = '{{ ConsistencyLevel }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="add_ref"
    values={[
        { label: 'add_ref', value: 'add_ref' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="add_ref">

Add a member to a security or Microsoft 365 group. When using the API to add multiple members in one request, you can add up to only 20 members.  The following table shows the types of members that can be added to either security groups or Microsoft 365 groups.

```sql
INSERT INTO entra_id.groups.members (
directoryObjectId,
group_id
)
SELECT 
'{{ directoryObjectId }}',
'{{ group_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: members
  props:
    - name: group_id
      value: "{{ group_id }}"
      description: Required parameter for the members resource.
    - name: directoryObjectId
      value: "{{ directoryObjectId }}"
      description: |
        The id of the directory object to reference (a user, group, service principal, device, ...). Sent on the wire as '@odata.id': 'https://graph.microsoft.com/v1.0/directoryObjects/{id}'.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="remove_ref"
    values={[
        { label: 'remove_ref', value: 'remove_ref' },
        { label: 'remove_ref_2', value: 'remove_ref_2' }
    ]}
>
<TabItem value="remove_ref">

Remove a member from a group via the members navigation property. You can't remove a member from groups with dynamic memberships.

```sql
DELETE FROM entra_id.groups.members
WHERE group_id = '{{ group_id }}' --required
AND directory_object_id = '{{ directory_object_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="remove_ref_2">

Remove a member from a group via the members navigation property. You can't remove a member from groups with dynamic memberships.

```sql
DELETE FROM entra_id.groups.members
AND group_id = '{{ group_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
