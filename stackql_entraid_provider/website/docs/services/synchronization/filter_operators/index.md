--- 
title: filter_operators
hide_title: false
hide_table_of_contents: false
keywords:
  - filter_operators
  - synchronization
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

Creates, updates, deletes, gets or lists a <code>filter_operators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="filter_operators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.synchronization.filter_operators" /></td></tr>
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

Retrieved entity

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
    <td><CopyableCode code="arity" /></td>
    <td><code>string</code></td>
    <td> (Binary, Unary) (title: scopeOperatorType)</td>
</tr>
<tr>
    <td><CopyableCode code="multivaluedComparisonType" /></td>
    <td><code>string</code></td>
    <td> (All, Any) (title: scopeOperatorMultiValuedComparisonType)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedAttributeTypes" /></td>
    <td><code>array</code></td>
    <td>Attribute types supported by the operator. The possible values are: Boolean, Binary, Reference, Integer, String.</td>
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
    <td><CopyableCode code="arity" /></td>
    <td><code>string</code></td>
    <td> (Binary, Unary) (title: scopeOperatorType)</td>
</tr>
<tr>
    <td><CopyableCode code="multivaluedComparisonType" /></td>
    <td><code>string</code></td>
    <td> (All, Any) (title: scopeOperatorMultiValuedComparisonType)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedAttributeTypes" /></td>
    <td><code>array</code></td>
    <td>Attribute types supported by the operator. The possible values are: Boolean, Binary, Reference, Integer, String.</td>
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
    <td><a href="#parameter-filter_operator_schema_id"><code>filter_operator_schema_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-filter_operator_schema_id"><code>filter_operator_schema_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-filter_operator_schema_id"><code>filter_operator_schema_id</code></a></td>
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
<tr id="parameter-filter_operator_schema_id">
    <td><CopyableCode code="filter_operator_schema_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of filterOperatorSchema</td>
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

Retrieved entity

```sql
SELECT
id,
arity,
multivaluedComparisonType,
supportedAttributeTypes
FROM entra_id.synchronization.filter_operators
WHERE filter_operator_schema_id = '{{ filter_operator_schema_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
arity,
multivaluedComparisonType,
supportedAttributeTypes
FROM entra_id.synchronization.filter_operators
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
INSERT INTO entra_id.synchronization.filter_operators (
id,
arity,
multivaluedComparisonType,
supportedAttributeTypes
)
SELECT 
'{{ id }}',
'{{ arity }}',
'{{ multivaluedComparisonType }}',
'{{ supportedAttributeTypes }}'
RETURNING
id,
arity,
multivaluedComparisonType,
supportedAttributeTypes
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: filter_operators
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: arity
      value: "{{ arity }}"
      valid_values: ['Binary', 'Unary']
    - name: multivaluedComparisonType
      value: "{{ multivaluedComparisonType }}"
      valid_values: ['All', 'Any']
    - name: supportedAttributeTypes
      value:
        - "{{ supportedAttributeTypes }}"
      description: |
        Attribute types supported by the operator. The possible values are: Boolean, Binary, Reference, Integer, String.
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
UPDATE entra_id.synchronization.filter_operators
SET 
id = '{{ id }}',
arity = '{{ arity }}',
multivaluedComparisonType = '{{ multivaluedComparisonType }}',
supportedAttributeTypes = '{{ supportedAttributeTypes }}'
WHERE 
filter_operator_schema_id = '{{ filter_operator_schema_id }}' --required
RETURNING
id,
arity,
multivaluedComparisonType,
supportedAttributeTypes;
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
DELETE FROM entra_id.synchronization.filter_operators
WHERE filter_operator_schema_id = '{{ filter_operator_schema_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
