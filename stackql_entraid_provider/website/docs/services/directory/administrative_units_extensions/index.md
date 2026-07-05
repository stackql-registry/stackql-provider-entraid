--- 
title: administrative_units_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - administrative_units_extensions
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

Creates, updates, deletes, gets or lists an <code>administrative_units_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="administrative_units_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.administrative_units_extensions" /></td></tr>
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
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a>, <a href="#parameter-extension_id"><code>extension_id</code></a></td>
    <td></td>
    <td>The collection of open extensions defined for this administrative unit. Nullable.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a></td>
    <td></td>
    <td>The collection of open extensions defined for this administrative unit. Nullable.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a>, <a href="#parameter-extension_id"><code>extension_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-administrative_unit_id"><code>administrative_unit_id</code></a>, <a href="#parameter-extension_id"><code>extension_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
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
<tr id="parameter-administrative_unit_id">
    <td><CopyableCode code="administrative_unit_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of administrativeUnit</td>
</tr>
<tr id="parameter-extension_id">
    <td><CopyableCode code="extension_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of extension</td>
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

The collection of open extensions defined for this administrative unit. Nullable.

```sql
SELECT
id
FROM entra_id.directory.administrative_units_extensions
WHERE administrative_unit_id = '{{ administrative_unit_id }}' -- required
AND extension_id = '{{ extension_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The collection of open extensions defined for this administrative unit. Nullable.

```sql
SELECT
id
FROM entra_id.directory.administrative_units_extensions
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

No description available.

```sql
INSERT INTO entra_id.directory.administrative_units_extensions (
id,
administrative_unit_id
)
SELECT 
'{{ id }}',
'{{ administrative_unit_id }}'
RETURNING
id
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: administrative_units_extensions
  props:
    - name: administrative_unit_id
      value: "{{ administrative_unit_id }}"
      description: Required parameter for the administrative_units_extensions resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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
UPDATE entra_id.directory.administrative_units_extensions
SET 
id = '{{ id }}',
WHERE 
administrative_unit_id = '{{ administrative_unit_id }}' --required
AND extension_id = '{{ extension_id }}' --required
RETURNING
id,
@odata.type;
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
DELETE FROM entra_id.directory.administrative_units_extensions
WHERE administrative_unit_id = '{{ administrative_unit_id }}' --required
AND extension_id = '{{ extension_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
