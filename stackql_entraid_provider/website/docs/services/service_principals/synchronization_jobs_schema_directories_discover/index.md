--- 
title: synchronization_jobs_schema_directories_discover
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_jobs_schema_directories_discover
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

Creates, updates, deletes, gets or lists a <code>synchronization_jobs_schema_directories_discover</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_jobs_schema_directories_discover" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.synchronization_jobs_schema_directories_discover" /></td></tr>
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
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a>, <a href="#parameter-directoryDefinition-id"><code>directoryDefinition-id</code></a></td>
    <td></td>
    <td>Discover the latest schema definition for provisioning to an application. </td>
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
<tr id="parameter-directoryDefinition-id">
    <td><CopyableCode code="directoryDefinition-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryDefinition</td>
</tr>
<tr id="parameter-servicePrincipal-id">
    <td><CopyableCode code="servicePrincipal-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
</tr>
<tr id="parameter-synchronizationJob-id">
    <td><CopyableCode code="synchronizationJob-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of synchronizationJob</td>
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

Discover the latest schema definition for provisioning to an application. 

```sql
INSERT INTO entra_id.service_principals.synchronization_jobs_schema_directories_discover (
servicePrincipal-id,
synchronizationJob-id,
directoryDefinition-id
)
SELECT 
'{{ servicePrincipal-id }}',
'{{ synchronizationJob-id }}',
'{{ directoryDefinition-id }}'
RETURNING
id,
name,
@odata.type,
discoverabilities,
discoveryDateTime,
objects,
readOnly,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: synchronization_jobs_schema_directories_discover
  props:
    - name: servicePrincipal-id
      value: "{{ servicePrincipal-id }}"
      description: Required parameter for the synchronization_jobs_schema_directories_discover resource.
    - name: synchronizationJob-id
      value: "{{ synchronizationJob-id }}"
      description: Required parameter for the synchronization_jobs_schema_directories_discover resource.
    - name: directoryDefinition-id
      value: "{{ directoryDefinition-id }}"
      description: Required parameter for the synchronization_jobs_schema_directories_discover resource.
`}</CodeBlock>

</TabItem>
</Tabs>
