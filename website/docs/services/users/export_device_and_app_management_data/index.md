--- 
title: export_device_and_app_management_data
hide_title: false
hide_table_of_contents: false
keywords:
  - export_device_and_app_management_data
  - users
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

Creates, updates, deletes, gets or lists an <code>export_device_and_app_management_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="export_device_and_app_management_data" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.export_device_and_app_management_data" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_2"
    values={[
        { label: 'get_2', value: 'get_2' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_2">

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
</TabItem>
<TabItem value="get">

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
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a>, <a href="#parameter-skip"><code>skip</code></a>, <a href="#parameter-top"><code>top</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
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
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>number (int32)</code></td>
    <td>Usage: skip=&#123;skip&#125;</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>number (int32)</code></td>
    <td>Usage: top=&#123;top&#125;</td>
</tr>
<tr id="parameter-user-id">
    <td><CopyableCode code="user-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of user</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_2"
    values={[
        { label: 'get_2', value: 'get_2' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_2">

Success

```sql
SELECT
*
FROM entra_id.users.export_device_and_app_management_data
WHERE user-id = '{{ user-id }}' -- required
AND skip = '{{ skip }}' -- required
AND top = '{{ top }}' -- required
;
```
</TabItem>
<TabItem value="get">

Success

```sql
SELECT
*
FROM entra_id.users.export_device_and_app_management_data
WHERE user-id = '{{ user-id }}' -- required
;
```
</TabItem>
</Tabs>
