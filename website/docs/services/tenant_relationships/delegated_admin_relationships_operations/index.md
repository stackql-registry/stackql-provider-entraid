--- 
title: delegated_admin_relationships_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_admin_relationships_operations
  - tenant_relationships
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

Creates, updates, deletes, gets or lists a <code>delegated_admin_relationships_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delegated_admin_relationships_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.tenant_relationships.delegated_admin_relationships_operations" /></td></tr>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time in ISO 8601 format and in UTC time when the long-running operation was created. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>string</code></td>
    <td>The data (payload) for the operation. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time in ISO 8601 format and in UTC time when the long-running operation was last modified. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="operationType" /></td>
    <td><code>string</code></td>
    <td> (delegatedAdminAccessAssignmentUpdate, unknownFutureValue, delegatedAdminRelationshipUpdate) (title: delegatedAdminRelationshipOperationType)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (notStarted, running, succeeded, failed, unknownFutureValue) (title: longRunningOperationStatus)</td>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time in ISO 8601 format and in UTC time when the long-running operation was created. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>string</code></td>
    <td>The data (payload) for the operation. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time in ISO 8601 format and in UTC time when the long-running operation was last modified. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="operationType" /></td>
    <td><code>string</code></td>
    <td> (delegatedAdminAccessAssignmentUpdate, unknownFutureValue, delegatedAdminRelationshipUpdate) (title: delegatedAdminRelationshipOperationType)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td> (notStarted, running, succeeded, failed, unknownFutureValue) (title: longRunningOperationStatus)</td>
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
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a>, <a href="#parameter-delegatedAdminRelationshipOperation-id"><code>delegatedAdminRelationshipOperation-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties of a delegatedAdminRelationshipOperation object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of the delegatedAdminRelationshipOperation objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a>, <a href="#parameter-delegatedAdminRelationshipOperation-id"><code>delegatedAdminRelationshipOperation-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a>, <a href="#parameter-delegatedAdminRelationshipOperation-id"><code>delegatedAdminRelationshipOperation-id</code></a></td>
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
<tr id="parameter-delegatedAdminRelationship-id">
    <td><CopyableCode code="delegatedAdminRelationship-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of delegatedAdminRelationship</td>
</tr>
<tr id="parameter-delegatedAdminRelationshipOperation-id">
    <td><CopyableCode code="delegatedAdminRelationshipOperation-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of delegatedAdminRelationshipOperation</td>
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

Read the properties of a delegatedAdminRelationshipOperation object.

```sql
SELECT
id,
@odata.type,
createdDateTime,
data,
lastModifiedDateTime,
operationType,
status
FROM entra_id.tenant_relationships.delegated_admin_relationships_operations
WHERE delegatedAdminRelationship-id = '{{ delegatedAdminRelationship-id }}' -- required
AND delegatedAdminRelationshipOperation-id = '{{ delegatedAdminRelationshipOperation-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of the delegatedAdminRelationshipOperation objects and their properties.

```sql
SELECT
id,
@odata.type,
createdDateTime,
data,
lastModifiedDateTime,
operationType,
status
FROM entra_id.tenant_relationships.delegated_admin_relationships_operations
WHERE delegatedAdminRelationship-id = '{{ delegatedAdminRelationship-id }}' -- required
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
INSERT INTO entra_id.tenant_relationships.delegated_admin_relationships_operations (
id,
@odata.type,
createdDateTime,
data,
lastModifiedDateTime,
operationType,
status,
delegatedAdminRelationship-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ createdDateTime }}',
'{{ data }}',
'{{ lastModifiedDateTime }}',
'{{ operationType }}',
'{{ status }}',
'{{ delegatedAdminRelationship-id }}'
RETURNING
id,
@odata.type,
createdDateTime,
data,
lastModifiedDateTime,
operationType,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: delegated_admin_relationships_operations
  props:
    - name: delegatedAdminRelationship-id
      value: "{{ delegatedAdminRelationship-id }}"
      description: Required parameter for the delegated_admin_relationships_operations resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The time in ISO 8601 format and in UTC time when the long-running operation was created. Read-only.
    - name: data
      value: "{{ data }}"
      description: |
        The data (payload) for the operation. Read-only.
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        The time in ISO 8601 format and in UTC time when the long-running operation was last modified. Read-only.
    - name: operationType
      value: "{{ operationType }}"
      valid_values: ['delegatedAdminAccessAssignmentUpdate', 'unknownFutureValue', 'delegatedAdminRelationshipUpdate']
    - name: status
      value: "{{ status }}"
      valid_values: ['notStarted', 'running', 'succeeded', 'failed', 'unknownFutureValue']
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
UPDATE entra_id.tenant_relationships.delegated_admin_relationships_operations
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
createdDateTime = '{{ createdDateTime }}',
data = '{{ data }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
operationType = '{{ operationType }}',
status = '{{ status }}'
WHERE 
delegatedAdminRelationship-id = '{{ delegatedAdminRelationship-id }}' --required
AND delegatedAdminRelationshipOperation-id = '{{ delegatedAdminRelationshipOperation-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
createdDateTime,
data,
lastModifiedDateTime,
operationType,
status;
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
DELETE FROM entra_id.tenant_relationships.delegated_admin_relationships_operations
WHERE delegatedAdminRelationship-id = '{{ delegatedAdminRelationship-id }}' --required
AND delegatedAdminRelationshipOperation-id = '{{ delegatedAdminRelationshipOperation-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
