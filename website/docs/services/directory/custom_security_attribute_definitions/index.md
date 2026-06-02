--- 
title: custom_security_attribute_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_security_attribute_definitions
  - directory
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

Creates, updates, deletes, gets or lists a <code>custom_security_attribute_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_security_attribute_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.directory.custom_security_attribute_definitions" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#parameter-customSecurityAttributeDefinition-id"><code>customSecurityAttributeDefinition-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of a customSecurityAttributeDefinition object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of the customSecurityAttributeDefinition objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new customSecurityAttributeDefinition object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-customSecurityAttributeDefinition-id"><code>customSecurityAttributeDefinition-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a customSecurityAttributeDefinition object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-customSecurityAttributeDefinition-id"><code>customSecurityAttributeDefinition-id</code></a></td>
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
<tr id="parameter-customSecurityAttributeDefinition-id">
    <td><CopyableCode code="customSecurityAttributeDefinition-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customSecurityAttributeDefinition</td>
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

Read the properties and relationships of a customSecurityAttributeDefinition object.

```sql
SELECT
id,
name,
@odata.type,
allowedValues,
attributeSet,
description,
isCollection,
isSearchable,
status,
type,
usePreDefinedValuesOnly
FROM entraid.directory.custom_security_attribute_definitions
WHERE customSecurityAttributeDefinition-id = '{{ customSecurityAttributeDefinition-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of the customSecurityAttributeDefinition objects and their properties.

```sql
SELECT
id,
name,
@odata.type,
allowedValues,
attributeSet,
description,
isCollection,
isSearchable,
status,
type,
usePreDefinedValuesOnly
FROM entraid.directory.custom_security_attribute_definitions
WHERE $top = '{{ $top }}'
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

Create a new customSecurityAttributeDefinition object.

```sql
INSERT INTO entraid.directory.custom_security_attribute_definitions (
id,
@odata.type,
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
'{{ @odata.type }}' /* required */,
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
@odata.type,
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
    - name: @odata.type
      value: "{{ @odata.type }}"
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
          @odata.type: "{{ @odata.type }}"
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
UPDATE entraid.directory.custom_security_attribute_definitions
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
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
customSecurityAttributeDefinition-id = '{{ customSecurityAttributeDefinition-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
name,
@odata.type,
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
DELETE FROM entraid.directory.custom_security_attribute_definitions
WHERE customSecurityAttributeDefinition-id = '{{ customSecurityAttributeDefinition-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
