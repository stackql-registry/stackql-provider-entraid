--- 
title: custom_security_attribute_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_security_attribute_definitions
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

Creates, updates, deletes, gets or lists a <code>custom_security_attribute_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_security_attribute_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.custom_security_attribute_definitions" /></td></tr>
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
    <td>Name of the custom security attribute. Must be unique within an attribute set. Can be up to 32 characters long and include Unicode characters. Cannot contain spaces or special characters. Cannot be changed later. Case insensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedValues" /></td>
    <td><code>array</code></td>
    <td>Values that are predefined for this custom security attribute. This navigation property is not returned by default and must be specified in an $expand query. For example, /directory/customSecurityAttributeDefinitions?$expand=allowedValues.</td>
</tr>
<tr>
    <td><CopyableCode code="attributeSet" /></td>
    <td><code>string</code></td>
    <td>Name of the attribute set. Case insensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the custom security attribute. Can be up to 128 characters long and include Unicode characters. Can be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="isCollection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether multiple values can be assigned to the custom security attribute. Cannot be changed later. If type is set to Boolean, isCollection cannot be set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSearchable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether custom security attribute values are indexed for searching on objects that are assigned attribute values. Cannot be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the custom security attribute is active or deactivated. Acceptable values are: Available and Deprecated. Can be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Data type for the custom security attribute values. Supported types are: Boolean, Integer, and String. Cannot be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="usePreDefinedValuesOnly" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether only predefined values can be assigned to the custom security attribute. If set to false, free-form values are allowed. Can later be changed from true to false, but cannot be changed from false to true. If type is set to Boolean, usePreDefinedValuesOnly cannot be set to true.</td>
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
    <td>Name of the custom security attribute. Must be unique within an attribute set. Can be up to 32 characters long and include Unicode characters. Cannot contain spaces or special characters. Cannot be changed later. Case insensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedValues" /></td>
    <td><code>array</code></td>
    <td>Values that are predefined for this custom security attribute. This navigation property is not returned by default and must be specified in an $expand query. For example, /directory/customSecurityAttributeDefinitions?$expand=allowedValues.</td>
</tr>
<tr>
    <td><CopyableCode code="attributeSet" /></td>
    <td><code>string</code></td>
    <td>Name of the attribute set. Case insensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the custom security attribute. Can be up to 128 characters long and include Unicode characters. Can be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="isCollection" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether multiple values can be assigned to the custom security attribute. Cannot be changed later. If type is set to Boolean, isCollection cannot be set to true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSearchable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether custom security attribute values are indexed for searching on objects that are assigned attribute values. Cannot be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies whether the custom security attribute is active or deactivated. Acceptable values are: Available and Deprecated. Can be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Data type for the custom security attribute values. Supported types are: Boolean, Integer, and String. Cannot be changed later.</td>
</tr>
<tr>
    <td><CopyableCode code="usePreDefinedValuesOnly" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether only predefined values can be assigned to the custom security attribute. If set to false, free-form values are allowed. Can later be changed from true to false, but cannot be changed from false to true. If type is set to Boolean, usePreDefinedValuesOnly cannot be set to true.</td>
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
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a customSecurityAttributeDefinition object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the customSecurityAttributeDefinition objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new customSecurityAttributeDefinition object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a></td>
    <td></td>
    <td>Update the properties of a customSecurityAttributeDefinition object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_security_attribute_definition_id"><code>custom_security_attribute_definition_id</code></a></td>
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

Read the properties and relationships of a customSecurityAttributeDefinition object.

```sql
SELECT
id,
name,
allowedValues,
attributeSet,
description,
isCollection,
isSearchable,
status,
type,
usePreDefinedValuesOnly
FROM entra_id.directory.custom_security_attribute_definitions
WHERE custom_security_attribute_definition_id = '{{ custom_security_attribute_definition_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the customSecurityAttributeDefinition objects and their properties.

```sql
SELECT
id,
name,
allowedValues,
attributeSet,
description,
isCollection,
isSearchable,
status,
type,
usePreDefinedValuesOnly
FROM entra_id.directory.custom_security_attribute_definitions
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

Create a new customSecurityAttributeDefinition object.

```sql
INSERT INTO entra_id.directory.custom_security_attribute_definitions (
id,
attributeSet,
description,
isCollection,
isSearchable,
name,
status,
type,
usePreDefinedValuesOnly,
allowedValues
)
SELECT 
'{{ id }}',
'{{ attributeSet }}',
'{{ description }}',
{{ isCollection }},
{{ isSearchable }},
'{{ name }}',
'{{ status }}',
'{{ type }}',
{{ usePreDefinedValuesOnly }},
'{{ allowedValues }}'
RETURNING
id,
name,
allowedValues,
attributeSet,
description,
isCollection,
isSearchable,
status,
type,
usePreDefinedValuesOnly
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: custom_security_attribute_definitions
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: attributeSet
      value: "{{ attributeSet }}"
      description: |
        Name of the attribute set. Case insensitive.
    - name: description
      value: "{{ description }}"
      description: |
        Description of the custom security attribute. Can be up to 128 characters long and include Unicode characters. Can be changed later.
    - name: isCollection
      value: {{ isCollection }}
      description: |
        Indicates whether multiple values can be assigned to the custom security attribute. Cannot be changed later. If type is set to Boolean, isCollection cannot be set to true.
    - name: isSearchable
      value: {{ isSearchable }}
      description: |
        Indicates whether custom security attribute values are indexed for searching on objects that are assigned attribute values. Cannot be changed later.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the custom security attribute. Must be unique within an attribute set. Can be up to 32 characters long and include Unicode characters. Cannot contain spaces or special characters. Cannot be changed later. Case insensitive.
    - name: status
      value: "{{ status }}"
      description: |
        Specifies whether the custom security attribute is active or deactivated. Acceptable values are: Available and Deprecated. Can be changed later.
    - name: type
      value: "{{ type }}"
      description: |
        Data type for the custom security attribute values. Supported types are: Boolean, Integer, and String. Cannot be changed later.
    - name: usePreDefinedValuesOnly
      value: {{ usePreDefinedValuesOnly }}
      description: |
        Indicates whether only predefined values can be assigned to the custom security attribute. If set to false, free-form values are allowed. Can later be changed from true to false, but cannot be changed from false to true. If type is set to Boolean, usePreDefinedValuesOnly cannot be set to true.
    - name: allowedValues
      description: |
        Values that are predefined for this custom security attribute. This navigation property is not returned by default and must be specified in an $expand query. For example, /directory/customSecurityAttributeDefinitions?$expand=allowedValues.
      value:
        - id: "{{ id }}"
          isActive: {{ isActive }}
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

Update the properties of a customSecurityAttributeDefinition object.

```sql
UPDATE entra_id.directory.custom_security_attribute_definitions
SET 
id = '{{ id }}',
attributeSet = '{{ attributeSet }}',
description = '{{ description }}',
isCollection = {{ isCollection }},
isSearchable = {{ isSearchable }},
name = '{{ name }}',
status = '{{ status }}',
type = '{{ type }}',
usePreDefinedValuesOnly = {{ usePreDefinedValuesOnly }},
allowedValues = '{{ allowedValues }}'
WHERE 
custom_security_attribute_definition_id = '{{ custom_security_attribute_definition_id }}' --required
RETURNING
id,
name,
allowedValues,
attributeSet,
description,
isCollection,
isSearchable,
status,
type,
usePreDefinedValuesOnly;
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
DELETE FROM entra_id.directory.custom_security_attribute_definitions
WHERE custom_security_attribute_definition_id = '{{ custom_security_attribute_definition_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
