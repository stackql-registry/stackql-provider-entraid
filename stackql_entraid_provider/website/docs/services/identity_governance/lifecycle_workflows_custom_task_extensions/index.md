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
    <td>When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>When the custom task extension was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>When the custom extension was last modified.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-custom_task_extension_id"><code>custom_task_extension_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a customTaskExtension object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the customTaskExtension objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new customTaskExtension object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-custom_task_extension_id"><code>custom_task_extension_id</code></a></td>
    <td></td>
    <td>Update the properties of a customTaskExtension object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_task_extension_id"><code>custom_task_extension_id</code></a></td>
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
<tr id="parameter-custom_task_extension_id">
    <td><CopyableCode code="custom_task_extension_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customTaskExtension</td>
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
WHERE custom_task_extension_id = '{{ custom_task_extension_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the customTaskExtension objects and their properties.

```sql
SELECT
id,
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
custom_task_extension_id = '{{ custom_task_extension_id }}' --required
RETURNING
id,
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
WHERE custom_task_extension_id = '{{ custom_task_extension_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
