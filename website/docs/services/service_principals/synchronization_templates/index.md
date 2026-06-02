--- 
title: synchronization_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_templates
  - service_principals
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

Creates, updates, deletes, gets or lists a <code>synchronization_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.service_principals.synchronization_templates" /></td></tr>
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
    <td><CopyableCode code="applicationId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Identifier of the application this template belongs to. (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="default" /></td>
    <td><code>boolean</code></td>
    <td>true if this template is recommended to be the default for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="discoverable" /></td>
    <td><code>boolean</code></td>
    <td>true if this template should appear in the collection of templates available for the application instance (service principal).</td>
</tr>
<tr>
    <td><CopyableCode code="factoryTag" /></td>
    <td><code>string</code></td>
    <td>One of the well-known factory tags supported by the synchronization engine. The factoryTag tells the synchronization engine which implementation to use when processing jobs based on this template.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code></code></td>
    <td>Default synchronization schema for the jobs based on this template.</td>
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
    <td><CopyableCode code="applicationId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Identifier of the application this template belongs to. (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="default" /></td>
    <td><code>boolean</code></td>
    <td>true if this template is recommended to be the default for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the template.</td>
</tr>
<tr>
    <td><CopyableCode code="discoverable" /></td>
    <td><code>boolean</code></td>
    <td>true if this template should appear in the collection of templates available for the application instance (service principal).</td>
</tr>
<tr>
    <td><CopyableCode code="factoryTag" /></td>
    <td><code>string</code></td>
    <td>One of the well-known factory tags supported by the synchronization engine. The factoryTag tells the synchronization engine which implementation to use when processing jobs based on this template.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code></code></td>
    <td>Default synchronization schema for the jobs based on this template.</td>
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
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationTemplate-id"><code>synchronizationTemplate-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Preconfigured synchronization settings for a particular application.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>List the synchronization templates associated with a given application or service principal.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationTemplate-id"><code>synchronizationTemplate-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationTemplate-id"><code>synchronizationTemplate-id</code></a></td>
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
<tr id="parameter-servicePrincipal-id">
    <td><CopyableCode code="servicePrincipal-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
</tr>
<tr id="parameter-synchronizationTemplate-id">
    <td><CopyableCode code="synchronizationTemplate-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of synchronizationTemplate</td>
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

Preconfigured synchronization settings for a particular application.

```sql
SELECT
id,
@odata.type,
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema
FROM entraid.service_principals.synchronization_templates
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
AND synchronizationTemplate-id = '{{ synchronizationTemplate-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List the synchronization templates associated with a given application or service principal.

```sql
SELECT
id,
@odata.type,
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema
FROM entraid.service_principals.synchronization_templates
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
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
INSERT INTO entraid.service_principals.synchronization_templates (
id,
@odata.type,
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema,
servicePrincipal-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ applicationId }}',
{{ default }},
'{{ description }}',
{{ discoverable }},
'{{ factoryTag }}',
'{{ metadata }}',
'{{ schema }}',
'{{ servicePrincipal-id }}'
RETURNING
id,
@odata.type,
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: synchronization_templates
  props:
    - name: servicePrincipal-id
      value: "{{ servicePrincipal-id }}"
      description: Required parameter for the synchronization_templates resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: applicationId
      value: "{{ applicationId }}"
      description: |
        Identifier of the application this template belongs to.
    - name: default
      value: {{ default }}
      description: |
        true if this template is recommended to be the default for the application.
    - name: description
      value: "{{ description }}"
      description: |
        Description of the template.
    - name: discoverable
      value: {{ discoverable }}
      description: |
        true if this template should appear in the collection of templates available for the application instance (service principal).
    - name: factoryTag
      value: "{{ factoryTag }}"
      description: |
        One of the well-known factory tags supported by the synchronization engine. The factoryTag tells the synchronization engine which implementation to use when processing jobs based on this template.
    - name: metadata
      description: |
        Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
      value:
        - key: "{{ key }}"
          value: "{{ value }}"
          @odata.type: "{{ @odata.type }}"
    - name: schema
      value: "{{ schema }}"
      description: |
        Default synchronization schema for the jobs based on this template.
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
UPDATE entraid.service_principals.synchronization_templates
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
applicationId = '{{ applicationId }}',
default = {{ default }},
description = '{{ description }}',
discoverable = {{ discoverable }},
factoryTag = '{{ factoryTag }}',
metadata = '{{ metadata }}',
schema = '{{ schema }}'
WHERE 
servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND synchronizationTemplate-id = '{{ synchronizationTemplate-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema;
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
DELETE FROM entraid.service_principals.synchronization_templates
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND synchronizationTemplate-id = '{{ synchronizationTemplate-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
