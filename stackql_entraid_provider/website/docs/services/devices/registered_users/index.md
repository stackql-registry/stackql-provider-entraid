--- 
title: registered_users
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_users
  - devices
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

Creates, updates, deletes, gets or lists a <code>registered_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="registered_users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.devices.registered_users" /></td></tr>
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
    <td><a href="#parameter-device_id"><code>device_id</code></a></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a></td>
    <td>Retrieve a list of users that are registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration.</td>
</tr>
<tr>
    <td><a href="#add_ref"><CopyableCode code="add_ref" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-device_id"><code>device_id</code></a></td>
    <td></td>
    <td>Add a registered user for the device.</td>
</tr>
<tr>
    <td><a href="#remove_ref"><CopyableCode code="remove_ref" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_id"><code>device_id</code></a>, <a href="#parameter-directory_object_id"><code>directory_object_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a user as a registered user of the device.</td>
</tr>
<tr>
    <td><a href="#remove_ref_2"><CopyableCode code="remove_ref_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_id"><code>device_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a user as a registered user of the device.</td>
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
<tr id="parameter-device_id">
    <td><CopyableCode code="device_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of device</td>
</tr>
<tr id="parameter-directory_object_id">
    <td><CopyableCode code="directory_object_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryObject</td>
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

Retrieve a list of users that are registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration.

```sql
SELECT
id,
deletedDateTime
FROM entra_id.devices.registered_users
WHERE device_id = '{{ device_id }}' -- required
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

Add a registered user for the device.

```sql
INSERT INTO entra_id.devices.registered_users (
directoryObjectId,
device_id
)
SELECT 
'{{ directoryObjectId }}',
'{{ device_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: registered_users
  props:
    - name: device_id
      value: "{{ device_id }}"
      description: Required parameter for the registered_users resource.
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

Remove a user as a registered user of the device.

```sql
DELETE FROM entra_id.devices.registered_users
WHERE device_id = '{{ device_id }}' --required
AND directory_object_id = '{{ directory_object_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="remove_ref_2">

Remove a user as a registered user of the device.

```sql
DELETE FROM entra_id.devices.registered_users
AND device_id = '{{ device_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
