--- 
title: custom_security_attribute_definitions_allowed_values
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_security_attribute_definitions_allowed_values
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

Creates, updates, deletes, gets or lists a <code>custom_security_attribute_definitions_allowed_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_security_attribute_definitions_allowed_values" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.custom_security_attribute_definitions_allowed_values" /></td></tr>
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
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the predefined value is active or deactivated. If set to false, this predefined value can't be assigned to any other supported directory objects.</td>
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
    <td><CopyableCode code="isActive" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the predefined value is active or deactivated. If set to false, this predefined value can't be assigned to any other supported directory objects.</td>
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
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a>, <a href="#parameter-allowed_value_id"><code>allowed_value_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of an allowedValue object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a></td>
    <td></td>
    <td>Get a list of the allowedValue objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a></td>
    <td></td>
    <td>Create a new allowedValue object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a>, <a href="#parameter-allowed_value_id"><code>allowed_value_id</code></a></td>
    <td></td>
    <td>Update the properties of an allowedValue object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a>, <a href="#parameter-allowed_value_id"><code>allowed_value_id</code></a></td>
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
<tr id="parameter-allowed_value_id">
    <td><CopyableCode code="allowed_value_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of allowedValue</td>
</tr>
<tr id="parameter-custom_security_attribute_definition_id">
    <td><CopyableCode code="custom_security_attribute_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customSecurityAttributeDefinition</td>
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

Read the properties and relationships of an allowedValue object.

```sql
SELECT
id,
isActive
FROM entra_id.directory.custom_security_attribute_definitions_allowed_values
WHERE custom_security_attribute_definition_id = '{{ custom_security_attribute_definition_id }}' -- required
AND allowed_value_id = '{{ allowed_value_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the allowedValue objects and their properties.

```sql
SELECT
id,
isActive
FROM entra_id.directory.custom_security_attribute_definitions_allowed_values
WHERE custom_security_attribute_definition_id = '{{ custom_security_attribute_definition_id }}' -- required
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

Create a new allowedValue object.

```sql
INSERT INTO entra_id.directory.custom_security_attribute_definitions_allowed_values (
id,
isActive,
custom_security_attribute_definition_id
)
SELECT 
'{{ id }}',
{{ isActive }},
'{{ custom_security_attribute_definition_id }}'
RETURNING
id,
isActive
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: custom_security_attribute_definitions_allowed_values
  props:
    - name: custom_security_attribute_definition_id
      value: "{{ custom_security_attribute_definition_id }}"
      description: Required parameter for the custom_security_attribute_definitions_allowed_values resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: isActive
      value: {{ isActive }}
      description: |
        Indicates whether the predefined value is active or deactivated. If set to false, this predefined value can't be assigned to any other supported directory objects.
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

Update the properties of an allowedValue object.

```sql
UPDATE entra_id.directory.custom_security_attribute_definitions_allowed_values
SET 
id = '{{ id }}',
isActive = {{ isActive }}
WHERE 
custom_security_attribute_definition_id = '{{ custom_security_attribute_definition_id }}' --required
AND allowed_value_id = '{{ allowed_value_id }}' --required
RETURNING
id,
isActive;
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
DELETE FROM entra_id.directory.custom_security_attribute_definitions_allowed_values
WHERE custom_security_attribute_definition_id = '{{ custom_security_attribute_definition_id }}' --required
AND allowed_value_id = '{{ allowed_value_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
