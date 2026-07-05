--- 
title: extension_properties
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_properties
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

Creates, updates, deletes, gets or lists an <code>extension_properties</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="extension_properties" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.applications.extension_properties" /></td></tr>
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
    <td>Name of the extension property. Not nullable. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="appDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the application object on which this extension property is defined. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>Specifies the data type of the value the extension property can hold. Following values are supported. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximumNot nullable. For multivalued directory extensions, these limits apply per value in the collection.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isMultiValued" /></td>
    <td><code>boolean</code></td>
    <td>Defines the directory extension as a multi-valued property. When true, the directory extension property can store a collection of objects of the dataType; for example, a collection of string types such as 'extensionb7b1c57b532f40b8b5ed4b7a7ba67401jobGroupTracker': ['String 1', 'String 2']. The default value is false. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="isSyncedFromOnPremises" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if this extension property was synced from on-premises active directory using Microsoft Entra Connect. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="targetObjects" /></td>
    <td><code>array</code></td>
    <td>Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization</td>
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
    <td>Name of the extension property. Not nullable. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="appDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the application object on which this extension property is defined. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td>Specifies the data type of the value the extension property can hold. Following values are supported. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximumNot nullable. For multivalued directory extensions, these limits apply per value in the collection.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isMultiValued" /></td>
    <td><code>boolean</code></td>
    <td>Defines the directory extension as a multi-valued property. When true, the directory extension property can store a collection of objects of the dataType; for example, a collection of string types such as 'extensionb7b1c57b532f40b8b5ed4b7a7ba67401jobGroupTracker': ['String 1', 'String 2']. The default value is false. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="isSyncedFromOnPremises" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if this extension property was synced from on-premises active directory using Microsoft Entra Connect. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="targetObjects" /></td>
    <td><code>array</code></td>
    <td>Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization</td>
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
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-extension_property_id"><code>extension_property_id</code></a></td>
    <td></td>
    <td>Read a directory extension definition represented by an extensionProperty object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Retrieve the list of directory extension definitions, represented by extensionProperty objects on an application.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Create a new directory extension definition, represented by an extensionProperty object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-extension_property_id"><code>extension_property_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-extension_property_id"><code>extension_property_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a directory extension definition represented by an extensionProperty object. You can delete only directory extensions that aren't synced from on-premises active directory (AD).</td>
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
<tr id="parameter-extension_property_id">
    <td><CopyableCode code="extension_property_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of extensionProperty</td>
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

Read a directory extension definition represented by an extensionProperty object.

```sql
SELECT
id,
name,
appDisplayName,
dataType,
deletedDateTime,
isMultiValued,
isSyncedFromOnPremises,
targetObjects
FROM entra_id.applications.extension_properties
WHERE application_id = '{{ application_id }}' -- required
AND extension_property_id = '{{ extension_property_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve the list of directory extension definitions, represented by extensionProperty objects on an application.

```sql
SELECT
id,
name,
appDisplayName,
dataType,
deletedDateTime,
isMultiValued,
isSyncedFromOnPremises,
targetObjects
FROM entra_id.applications.extension_properties
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

Create a new directory extension definition, represented by an extensionProperty object.

```sql
INSERT INTO entra_id.applications.extension_properties (
id,
deletedDateTime,
appDisplayName,
dataType,
isMultiValued,
isSyncedFromOnPremises,
name,
targetObjects,
application_id
)
SELECT 
'{{ id }}',
'{{ deletedDateTime }}',
'{{ appDisplayName }}',
'{{ dataType }}',
{{ isMultiValued }},
{{ isSyncedFromOnPremises }},
'{{ name }}',
'{{ targetObjects }}',
'{{ application_id }}'
RETURNING
id,
name,
appDisplayName,
dataType,
deletedDateTime,
isMultiValued,
isSyncedFromOnPremises,
targetObjects
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: extension_properties
  props:
    - name: application_id
      value: "{{ application_id }}"
      description: Required parameter for the extension_properties resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: appDisplayName
      value: "{{ appDisplayName }}"
      description: |
        Display name of the application object on which this extension property is defined. Read-only.
    - name: dataType
      value: "{{ dataType }}"
      description: |
        Specifies the data type of the value the extension property can hold. Following values are supported. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximumNot nullable. For multivalued directory extensions, these limits apply per value in the collection.
    - name: isMultiValued
      value: {{ isMultiValued }}
      description: |
        Defines the directory extension as a multi-valued property. When true, the directory extension property can store a collection of objects of the dataType; for example, a collection of string types such as 'extensionb7b1c57b532f40b8b5ed4b7a7ba67401jobGroupTracker': ['String 1', 'String 2']. The default value is false. Supports $filter (eq).
    - name: isSyncedFromOnPremises
      value: {{ isSyncedFromOnPremises }}
      description: |
        Indicates if this extension property was synced from on-premises active directory using Microsoft Entra Connect. Read-only.
    - name: name
      value: "{{ name }}"
      description: |
        Name of the extension property. Not nullable. Supports $filter (eq).
    - name: targetObjects
      value:
        - "{{ targetObjects }}"
      description: |
        Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization
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
UPDATE entra_id.applications.extension_properties
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
appDisplayName = '{{ appDisplayName }}',
dataType = '{{ dataType }}',
isMultiValued = {{ isMultiValued }},
isSyncedFromOnPremises = {{ isSyncedFromOnPremises }},
name = '{{ name }}',
targetObjects = '{{ targetObjects }}'
WHERE 
application_id = '{{ application_id }}' --required
AND extension_property_id = '{{ extension_property_id }}' --required
RETURNING
id,
name,
appDisplayName,
dataType,
deletedDateTime,
isMultiValued,
isSyncedFromOnPremises,
targetObjects;
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

Delete a directory extension definition represented by an extensionProperty object. You can delete only directory extensions that aren't synced from on-premises active directory (AD).

```sql
DELETE FROM entra_id.applications.extension_properties
WHERE application_id = '{{ application_id }}' --required
AND extension_property_id = '{{ extension_property_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
