--- 
title: custom_authentication_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_authentication_extensions
  - identity
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

Creates, updates, deletes, gets or lists a <code>custom_authentication_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_authentication_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.custom_authentication_extensions" /></td></tr>
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
    <td><CopyableCode code="behaviorOnError" /></td>
    <td><code></code></td>
    <td>The behaviour on error for the custom authentication extension.</td>
</tr>
<tr>
    <td><CopyableCode code="clientConfiguration" /></td>
    <td><code></code></td>
    <td>HTTP connection settings that define how long Microsoft Entra ID can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.</td>
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
    <td><CopyableCode code="behaviorOnError" /></td>
    <td><code></code></td>
    <td>The behaviour on error for the custom authentication extension.</td>
</tr>
<tr>
    <td><CopyableCode code="clientConfiguration" /></td>
    <td><code></code></td>
    <td>HTTP connection settings that define how long Microsoft Entra ID can wait for a connection to a logic app, how many times you can retry a timed-out connection and the exception scenarios when retries are allowed.</td>
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
    <td><a href="#parameter-custom_authentication_extension_id"><code>custom_authentication_extension_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a customAuthenticationExtension object. The following derived types are currently supported.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the customAuthenticationExtension objects and their properties. The following derived types are supported.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new customAuthenticationExtension object. The following derived types are currently supported.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-custom_authentication_extension_id"><code>custom_authentication_extension_id</code></a></td>
    <td></td>
    <td>Update the properties of a customAuthenticationExtension object. The following derived types are currently supported.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-custom_authentication_extension_id"><code>custom_authentication_extension_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a customAuthenticationExtension object. The following derived types are currently supported.</td>
</tr>
<tr>
    <td><a href="#validate_authentication_configuration"><CopyableCode code="validate_authentication_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#validate_authentication_configuration_2"><CopyableCode code="validate_authentication_configuration_2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-custom_authentication_extension_id"><code>custom_authentication_extension_id</code></a></td>
    <td></td>
    <td>An API to check validity of the endpoint and and authentication configuration for a customAuthenticationExtension object, which can represent one of the following derived types:</td>
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
<tr id="parameter-custom_authentication_extension_id">
    <td><CopyableCode code="custom_authentication_extension_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customAuthenticationExtension</td>
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

Read the properties and relationships of a customAuthenticationExtension object. The following derived types are currently supported.

```sql
SELECT
id,
authenticationConfiguration,
behaviorOnError,
clientConfiguration,
description,
displayName,
endpointConfiguration
FROM entra_id.identity.custom_authentication_extensions
WHERE custom_authentication_extension_id = '{{ custom_authentication_extension_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the customAuthenticationExtension objects and their properties. The following derived types are supported.

```sql
SELECT
id,
authenticationConfiguration,
behaviorOnError,
clientConfiguration,
description,
displayName,
endpointConfiguration
FROM entra_id.identity.custom_authentication_extensions
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

Create a new customAuthenticationExtension object. The following derived types are currently supported.

```sql
INSERT INTO entra_id.identity.custom_authentication_extensions (
id,
authenticationConfiguration,
clientConfiguration,
description,
displayName,
endpointConfiguration,
behaviorOnError
)
SELECT 
'{{ id }}',
'{{ authenticationConfiguration }}',
'{{ clientConfiguration }}',
'{{ description }}',
'{{ displayName }}',
'{{ endpointConfiguration }}',
'{{ behaviorOnError }}'
RETURNING
id,
authenticationConfiguration,
behaviorOnError,
clientConfiguration,
description,
displayName,
endpointConfiguration
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: custom_authentication_extensions
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
    - name: behaviorOnError
      value: "{{ behaviorOnError }}"
      description: |
        The behaviour on error for the custom authentication extension.
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

Update the properties of a customAuthenticationExtension object. The following derived types are currently supported.

```sql
UPDATE entra_id.identity.custom_authentication_extensions
SET 
id = '{{ id }}',
authenticationConfiguration = '{{ authenticationConfiguration }}',
clientConfiguration = '{{ clientConfiguration }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
endpointConfiguration = '{{ endpointConfiguration }}',
behaviorOnError = '{{ behaviorOnError }}'
WHERE 
custom_authentication_extension_id = '{{ custom_authentication_extension_id }}' --required
RETURNING
id,
authenticationConfiguration,
behaviorOnError,
clientConfiguration,
description,
displayName,
endpointConfiguration;
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

Delete a customAuthenticationExtension object. The following derived types are currently supported.

```sql
DELETE FROM entra_id.identity.custom_authentication_extensions
WHERE custom_authentication_extension_id = '{{ custom_authentication_extension_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate_authentication_configuration"
    values={[
        { label: 'validate_authentication_configuration', value: 'validate_authentication_configuration' },
        { label: 'validate_authentication_configuration_2', value: 'validate_authentication_configuration_2' }
    ]}
>
<TabItem value="validate_authentication_configuration">

Success

```sql
EXEC entra_id.identity.custom_authentication_extensions.validate_authentication_configuration 
@@json=
'{
"endpointConfiguration": "{{ endpointConfiguration }}", 
"authenticationConfiguration": "{{ authenticationConfiguration }}"
}'
;
```
</TabItem>
<TabItem value="validate_authentication_configuration_2">

An API to check validity of the endpoint and and authentication configuration for a customAuthenticationExtension object, which can represent one of the following derived types:

```sql
EXEC entra_id.identity.custom_authentication_extensions.validate_authentication_configuration_2 
@custom_authentication_extension_id='{{ custom_authentication_extension_id }}' --required
;
```
</TabItem>
</Tabs>
