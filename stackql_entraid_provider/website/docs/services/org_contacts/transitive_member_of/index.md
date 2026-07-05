--- 
title: transitive_member_of
hide_title: false
hide_table_of_contents: false
keywords:
  - transitive_member_of
  - org_contacts
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

Creates, updates, deletes, gets or lists a <code>transitive_member_of</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="transitive_member_of" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.org_contacts.transitive_member_of" /></td></tr>
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
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-org_contact_id"><code>org_contact_id</code></a>, <a href="#parameter-directory_object_id"><code>directory_object_id</code></a></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a></td>
    <td>Groups that this contact is a member of, including groups that the contact is nested under. Read-only. Nullable.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-org_contact_id"><code>org_contact_id</code></a></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a></td>
    <td>Get groups that this organizational contact is a member of. The API request is transitive, and returns all groups the organizational contact is a nested member of.</td>
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
<tr id="parameter-org_contact_id">
    <td><CopyableCode code="org_contact_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of orgContact</td>
</tr>
<tr id="parameter-ConsistencyLevel">
    <td><CopyableCode code="ConsistencyLevel" /></td>
    <td><code>string</code></td>
    <td>Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries</td>
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

Groups that this contact is a member of, including groups that the contact is nested under. Read-only. Nullable.

```sql
SELECT
id,
deletedDateTime
FROM entra_id.org_contacts.transitive_member_of
WHERE org_contact_id = '{{ org_contact_id }}' -- required
AND directory_object_id = '{{ directory_object_id }}' -- required
AND ConsistencyLevel = '{{ ConsistencyLevel }}'
;
```
</TabItem>
<TabItem value="list">

Get groups that this organizational contact is a member of. The API request is transitive, and returns all groups the organizational contact is a nested member of.

```sql
SELECT
id,
deletedDateTime
FROM entra_id.org_contacts.transitive_member_of
WHERE org_contact_id = '{{ org_contact_id }}' -- required
AND ConsistencyLevel = '{{ ConsistencyLevel }}'
;
```
</TabItem>
</Tabs>
