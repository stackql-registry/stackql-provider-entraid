--- 
title: synchronization_jobs_schema_filter_operators
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_jobs_schema_filter_operators
  - service_principals
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

Creates, updates, deletes, gets or lists a <code>synchronization_jobs_schema_filter_operators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_jobs_schema_filter_operators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.synchronization_jobs_schema_filter_operators" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
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
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>List all operators supported in the scoping filters.</td>
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
<tr id="parameter-service_principal_id">
    <td><CopyableCode code="service_principal_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
</tr>
<tr id="parameter-synchronization_job_id">
    <td><CopyableCode code="synchronization_job_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of synchronizationJob</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

List all operators supported in the scoping filters.

```sql
SELECT
id,
arity,
multivaluedComparisonType,
supportedAttributeTypes
FROM entra_id.service_principals.synchronization_jobs_schema_filter_operators
WHERE service_principal_id = '{{ service_principal_id }}' -- required
AND synchronization_job_id = '{{ synchronization_job_id }}' -- required
;
```
</TabItem>
</Tabs>
