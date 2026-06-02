--- 
title: lifecycle_workflows_custom_task_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_custom_task_extensions
  - identity_governance
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_custom_task_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_custom_task_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_custom_task_extensions" /></td></tr>
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
    <td><CopyableCode code="authenticationConfiguration" /></td>
    <td><code></code></td>
    <td>Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.</td>
</tr>
<tr>
    <td><CopyableCode code="callbackConfiguration" /></td>
    <td><code></code></td>
    <td>The callback configuration for a custom task extension.</td>
</tr>
<tr>
    <td><CopyableCode code="clientConfiguration" /></td>
    <td><code></code></td>
    <td>HTTP connection settings that define how long Microsoft Entra ID can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>The unique identifier of the Microsoft Entra user that created the custom task extension.Supports $filter(eq, ne) and $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the customCalloutExtension object.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the customCalloutExtension object.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointConfiguration" /></td>
    <td><code></code></td>
    <td>The type and details for configuring the endpoint to call the logic app's workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code></code></td>
    <td>The unique identifier of the Microsoft Entra user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td><CopyableCode code="authenticationConfiguration" /></td>
    <td><code></code></td>
    <td>Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.</td>
</tr>
<tr>
    <td><CopyableCode code="callbackConfiguration" /></td>
    <td><code></code></td>
    <td>The callback configuration for a custom task extension.</td>
</tr>
<tr>
    <td><CopyableCode code="clientConfiguration" /></td>
    <td><code></code></td>
    <td>HTTP connection settings that define how long Microsoft Entra ID can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>The unique identifier of the Microsoft Entra user that created the custom task extension.Supports $filter(eq, ne) and $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the customCalloutExtension object.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the customCalloutExtension object.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointConfiguration" /></td>
    <td><code></code></td>
    <td>The type and details for configuring the endpoint to call the logic app's workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code></code></td>
    <td>The unique identifier of the Microsoft Entra user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td><a href="#parameter-customTaskExtension-id"><code>customTaskExtension-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of a customTaskExtension object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of the customTaskExtension objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new customTaskExtension object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-customTaskExtension-id"><code>customTaskExtension-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a customTaskExtension object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-customTaskExtension-id"><code>customTaskExtension-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a customTaskExtension object. A custom task extension  can only be deleted if it is not referenced in any task objects in a lifecycle workflow.</td>
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
<tr id="parameter-customTaskExtension-id">
    <td><CopyableCode code="customTaskExtension-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customTaskExtension</td>
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

Read the properties and relationships of a customTaskExtension object.

```sql
SELECT
id,
@odata.type,
authenticationConfiguration,
callbackConfiguration,
clientConfiguration,
createdBy,
createdDateTime,
description,
displayName,
endpointConfiguration,
lastModifiedBy,
lastModifiedDateTime
FROM entra_id.identity_governance.lifecycle_workflows_custom_task_extensions
WHERE customTaskExtension-id = '{{ customTaskExtension-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of the customTaskExtension objects and their properties.

```sql
SELECT
id,
@odata.type,
authenticationConfiguration,
callbackConfiguration,
clientConfiguration,
createdBy,
createdDateTime,
description,
displayName,
endpointConfiguration,
lastModifiedBy,
lastModifiedDateTime
FROM entra_id.identity_governance.lifecycle_workflows_custom_task_extensions
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

Create a new customTaskExtension object.

```sql
INSERT INTO entra_id.identity_governance.lifecycle_workflows_custom_task_extensions (
id,
@odata.type,
authenticationConfiguration,
clientConfiguration,
description,
displayName,
endpointConfiguration,
callbackConfiguration,
createdDateTime,
lastModifiedDateTime,
createdBy,
lastModifiedBy
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ authenticationConfiguration }}',
'{{ clientConfiguration }}',
'{{ description }}',
'{{ displayName }}',
'{{ endpointConfiguration }}',
'{{ callbackConfiguration }}',
'{{ createdDateTime }}',
'{{ lastModifiedDateTime }}',
'{{ createdBy }}',
'{{ lastModifiedBy }}'
RETURNING
id,
@odata.type,
authenticationConfiguration,
callbackConfiguration,
clientConfiguration,
createdBy,
createdDateTime,
description,
displayName,
endpointConfiguration,
lastModifiedBy,
lastModifiedDateTime
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: lifecycle_workflows_custom_task_extensions
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: authenticationConfiguration
      value: "{{ authenticationConfiguration }}"
      description: |
        Configuration for securing the API call to the logic app. For example, using OAuth client credentials flow.
    - name: clientConfiguration
      value: "{{ clientConfiguration }}"
      description: |
        HTTP connection settings that define how long Microsoft Entra ID can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.
    - name: description
      value: "{{ description }}"
      description: |
        Description for the customCalloutExtension object.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name for the customCalloutExtension object.
    - name: endpointConfiguration
      value: "{{ endpointConfiguration }}"
      description: |
        The type and details for configuring the endpoint to call the logic app's workflow.
    - name: callbackConfiguration
      value: "{{ callbackConfiguration }}"
      description: |
        The callback configuration for a custom task extension.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    - name: createdBy
      value: "{{ createdBy }}"
      description: |
        The unique identifier of the Microsoft Entra user that created the custom task extension.Supports $filter(eq, ne) and $expand.
    - name: lastModifiedBy
      value: "{{ lastModifiedBy }}"
      description: |
        The unique identifier of the Microsoft Entra user that modified the custom task extension last.Supports $filter(eq, ne) and $expand.
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

Update the properties of a customTaskExtension object.

```sql
UPDATE entra_id.identity_governance.lifecycle_workflows_custom_task_extensions
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
authenticationConfiguration = '{{ authenticationConfiguration }}',
clientConfiguration = '{{ clientConfiguration }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
endpointConfiguration = '{{ endpointConfiguration }}',
callbackConfiguration = '{{ callbackConfiguration }}',
createdDateTime = '{{ createdDateTime }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
createdBy = '{{ createdBy }}',
lastModifiedBy = '{{ lastModifiedBy }}'
WHERE 
customTaskExtension-id = '{{ customTaskExtension-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
authenticationConfiguration,
callbackConfiguration,
clientConfiguration,
createdBy,
createdDateTime,
description,
displayName,
endpointConfiguration,
lastModifiedBy,
lastModifiedDateTime;
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

Delete a customTaskExtension object. A custom task extension  can only be deleted if it is not referenced in any task objects in a lifecycle workflow.

```sql
DELETE FROM entra_id.identity_governance.lifecycle_workflows_custom_task_extensions
WHERE customTaskExtension-id = '{{ customTaskExtension-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
