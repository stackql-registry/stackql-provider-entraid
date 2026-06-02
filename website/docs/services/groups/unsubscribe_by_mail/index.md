--- 
title: unsubscribe_by_mail
hide_title: false
hide_table_of_contents: false
keywords:
  - unsubscribe_by_mail
  - groups
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

Creates, updates, deletes, gets or lists an <code>unsubscribe_by_mail</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="unsubscribe_by_mail" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.groups.unsubscribe_by_mail" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Calling this method prevents the current user from receiving email notifications for this group about new posts, events, and files in that group. Supported for Microsoft 365 groups only.</td>
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
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="insert"
    values={[
        { label: 'insert', value: 'insert' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="insert">

Calling this method prevents the current user from receiving email notifications for this group about new posts, events, and files in that group. Supported for Microsoft 365 groups only.

```sql
INSERT INTO entraid.groups.unsubscribe_by_mail (
group-id
)
SELECT 
'{{ group-id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: unsubscribe_by_mail
  props:
    - name: group-id
      value: "{{ group-id }}"
      description: Required parameter for the unsubscribe_by_mail resource.
`}</CodeBlock>

</TabItem>
</Tabs>
