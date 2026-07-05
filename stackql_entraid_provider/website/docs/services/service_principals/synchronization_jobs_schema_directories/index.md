--- 
title: synchronization_jobs_schema_directories
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_jobs_schema_directories
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

Creates, updates, deletes, gets or lists a <code>synchronization_jobs_schema_directories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_jobs_schema_directories" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.synchronization_jobs_schema_directories" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the directory. Must be unique within the synchronization schema. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="discoverabilities" /></td>
    <td><code>string</code></td>
    <td> (None, AttributeNames, AttributeDataTypes, AttributeReadOnly, ReferenceAttributes, UnknownFutureValue) (title: directoryDefinitionDiscoverabilities)</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the discovery date and time using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="objects" /></td>
    <td><code>array</code></td>
    <td>Collection of objects supported by the directory.</td>
</tr>
<tr>
    <td><CopyableCode code="readOnly" /></td>
    <td><code>boolean</code></td>
    <td>Whether this object is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Read only value that indicates version discovered. null if discovery hasn't yet occurred.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the directory. Must be unique within the synchronization schema. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="discoverabilities" /></td>
    <td><code>string</code></td>
    <td> (None, AttributeNames, AttributeDataTypes, AttributeReadOnly, ReferenceAttributes, UnknownFutureValue) (title: directoryDefinitionDiscoverabilities)</td>
</tr>
<tr>
    <td><CopyableCode code="discoveryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the discovery date and time using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="objects" /></td>
    <td><code>array</code></td>
    <td>Collection of objects supported by the directory.</td>
</tr>
<tr>
    <td><CopyableCode code="readOnly" /></td>
    <td><code>boolean</code></td>
    <td>Whether this object is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Read only value that indicates version discovered. null if discovery hasn't yet occurred.</td>
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
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a>, <a href="#parameter-directory_definition_id"><code>directory_definition_id</code></a></td>
    <td></td>
    <td>Contains the collection of directories and all of their objects.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Contains the collection of directories and all of their objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a>, <a href="#parameter-directory_definition_id"><code>directory_definition_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a>, <a href="#parameter-directory_definition_id"><code>directory_definition_id</code></a></td>
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
<tr id="parameter-directory_definition_id">
    <td><CopyableCode code="directory_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryDefinition</td>
</tr>
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

Contains the collection of directories and all of their objects.

```sql
SELECT
id,
name,
discoverabilities,
discoveryDateTime,
objects,
readOnly,
version
FROM entra_id.service_principals.synchronization_jobs_schema_directories
WHERE service_principal_id = '{{ service_principal_id }}' -- required
AND synchronization_job_id = '{{ synchronization_job_id }}' -- required
AND directory_definition_id = '{{ directory_definition_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Contains the collection of directories and all of their objects.

```sql
SELECT
id,
name,
discoverabilities,
discoveryDateTime,
objects,
readOnly,
version
FROM entra_id.service_principals.synchronization_jobs_schema_directories
WHERE service_principal_id = '{{ service_principal_id }}' -- required
AND synchronization_job_id = '{{ synchronization_job_id }}' -- required
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
INSERT INTO entra_id.service_principals.synchronization_jobs_schema_directories (
id,
discoverabilities,
discoveryDateTime,
name,
objects,
readOnly,
version,
service_principal_id,
synchronization_job_id
)
SELECT 
'{{ id }}',
'{{ discoverabilities }}',
'{{ discoveryDateTime }}',
'{{ name }}',
'{{ objects }}',
{{ readOnly }},
'{{ version }}',
'{{ service_principal_id }}',
'{{ synchronization_job_id }}'
RETURNING
id,
name,
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
- name: synchronization_jobs_schema_directories
  props:
    - name: service_principal_id
      value: "{{ service_principal_id }}"
      description: Required parameter for the synchronization_jobs_schema_directories resource.
    - name: synchronization_job_id
      value: "{{ synchronization_job_id }}"
      description: Required parameter for the synchronization_jobs_schema_directories resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: discoverabilities
      value: "{{ discoverabilities }}"
      valid_values: ['None', 'AttributeNames', 'AttributeDataTypes', 'AttributeReadOnly', 'ReferenceAttributes', 'UnknownFutureValue']
    - name: discoveryDateTime
      value: "{{ discoveryDateTime }}"
      description: |
        Represents the discovery date and time using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the directory. Must be unique within the synchronization schema. Not nullable.
    - name: objects
      description: |
        Collection of objects supported by the directory.
      value:
        - attributes: "{{ attributes }}"
          metadata: "{{ metadata }}"
          name: "{{ name }}"
          supportedApis: "{{ supportedApis }}"
    - name: readOnly
      value: {{ readOnly }}
      description: |
        Whether this object is read-only.
    - name: version
      value: "{{ version }}"
      description: |
        Read only value that indicates version discovered. null if discovery hasn't yet occurred.
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
UPDATE entra_id.service_principals.synchronization_jobs_schema_directories
SET 
id = '{{ id }}',
discoverabilities = '{{ discoverabilities }}',
discoveryDateTime = '{{ discoveryDateTime }}',
name = '{{ name }}',
objects = '{{ objects }}',
readOnly = {{ readOnly }},
version = '{{ version }}'
WHERE 
service_principal_id = '{{ service_principal_id }}' --required
AND synchronization_job_id = '{{ synchronization_job_id }}' --required
AND directory_definition_id = '{{ directory_definition_id }}' --required
RETURNING
id,
name,
discoverabilities,
discoveryDateTime,
objects,
readOnly,
version;
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
DELETE FROM entra_id.service_principals.synchronization_jobs_schema_directories
WHERE service_principal_id = '{{ service_principal_id }}' --required
AND synchronization_job_id = '{{ synchronization_job_id }}' --required
AND directory_definition_id = '{{ directory_definition_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
