--- 
title: synchronization_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_templates
  - applications
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

Creates, updates, deletes, gets or lists a <code>synchronization_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.applications.synchronization_templates" /></td></tr>
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
    <td><CopyableCode code="applicationId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Identifier of the application this template belongs to. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
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
    <td><CopyableCode code="applicationId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Identifier of the application this template belongs to. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
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
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_template_id"><code>synchronization_template_id</code></a></td>
    <td></td>
    <td>Preconfigured synchronization settings for a particular application.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Preconfigured synchronization settings for a particular application.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_template_id"><code>synchronization_template_id</code></a></td>
    <td></td>
    <td>Update (override) the synchronization template associated with a given application.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_template_id"><code>synchronization_template_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#schema_directories_discover"><CopyableCode code="schema_directories_discover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_template_id"><code>synchronization_template_id</code></a>, <a href="#parameter-directory_definition_id"><code>directory_definition_id</code></a></td>
    <td></td>
    <td>Discover the latest schema definition for provisioning to an application. </td>
</tr>
<tr>
    <td><a href="#schema_parse_expression"><CopyableCode code="schema_parse_expression" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_template_id"><code>synchronization_template_id</code></a></td>
    <td></td>
    <td>Parse a given string expression into an attributeMappingSource object. For more information about expressions, see Writing Expressions for Attribute Mappings in Microsoft Entra ID.</td>
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
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of application</td>
</tr>
<tr id="parameter-directory_definition_id">
    <td><CopyableCode code="directory_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryDefinition</td>
</tr>
<tr id="parameter-synchronization_template_id">
    <td><CopyableCode code="synchronization_template_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of synchronizationTemplate</td>
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
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema
FROM entra_id.applications.synchronization_templates
WHERE application_id = '{{ application_id }}' -- required
AND synchronization_template_id = '{{ synchronization_template_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Preconfigured synchronization settings for a particular application.

```sql
SELECT
id,
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema
FROM entra_id.applications.synchronization_templates
WHERE application_id = '{{ application_id }}' -- required
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
INSERT INTO entra_id.applications.synchronization_templates (
id,
applicationId,
default,
description,
discoverable,
factoryTag,
metadata,
schema,
application_id
)
SELECT 
'{{ id }}',
'{{ applicationId }}',
{{ default }},
'{{ description }}',
{{ discoverable }},
'{{ factoryTag }}',
'{{ metadata }}',
'{{ schema }}',
'{{ application_id }}'
RETURNING
id,
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
    - name: application_id
      value: "{{ application_id }}"
      description: Required parameter for the synchronization_templates resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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

Update (override) the synchronization template associated with a given application.

```sql
UPDATE entra_id.applications.synchronization_templates
SET 
id = '{{ id }}',
applicationId = '{{ applicationId }}',
default = {{ default }},
description = '{{ description }}',
discoverable = {{ discoverable }},
factoryTag = '{{ factoryTag }}',
metadata = '{{ metadata }}',
schema = '{{ schema }}'
WHERE 
application_id = '{{ application_id }}' --required
AND synchronization_template_id = '{{ synchronization_template_id }}' --required
RETURNING
id,
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
DELETE FROM entra_id.applications.synchronization_templates
WHERE application_id = '{{ application_id }}' --required
AND synchronization_template_id = '{{ synchronization_template_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="schema_directories_discover"
    values={[
        { label: 'schema_directories_discover', value: 'schema_directories_discover' },
        { label: 'schema_parse_expression', value: 'schema_parse_expression' }
    ]}
>
<TabItem value="schema_directories_discover">

Discover the latest schema definition for provisioning to an application. 

```sql
EXEC entra_id.applications.synchronization_templates.schema_directories_discover 
@application_id='{{ application_id }}' --required, 
@synchronization_template_id='{{ synchronization_template_id }}' --required, 
@directory_definition_id='{{ directory_definition_id }}' --required
;
```
</TabItem>
<TabItem value="schema_parse_expression">

Parse a given string expression into an attributeMappingSource object. For more information about expressions, see Writing Expressions for Attribute Mappings in Microsoft Entra ID.

```sql
EXEC entra_id.applications.synchronization_templates.schema_parse_expression 
@application_id='{{ application_id }}' --required, 
@synchronization_template_id='{{ synchronization_template_id }}' --required 
@@json=
'{
"expression": "{{ expression }}", 
"testInputObject": "{{ testInputObject }}", 
"targetAttributeDefinition": "{{ targetAttributeDefinition }}"
}'
;
```
</TabItem>
</Tabs>
