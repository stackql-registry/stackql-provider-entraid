--- 
title: entitlement_management_resource_requests_catalog_custom_workflow_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_resource_requests_catalog_custom_workflow_extensions
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_resource_requests_catalog_custom_workflow_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_resource_requests_catalog_custom_workflow_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_resource_requests_catalog_custom_workflow_extensions" /></td></tr>
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
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a>, <a href="#parameter-custom_callout_extension_id"><code>custom_callout_extension_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a>, <a href="#parameter-custom_callout_extension_id"><code>custom_callout_extension_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a>, <a href="#parameter-custom_callout_extension_id"><code>custom_callout_extension_id</code></a></td>
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
<tr id="parameter-access_package_resource_request_id">
    <td><CopyableCode code="access_package_resource_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceRequest</td>
</tr>
<tr id="parameter-custom_callout_extension_id">
    <td><CopyableCode code="custom_callout_extension_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customCalloutExtension</td>
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

Retrieved navigation property

```sql
SELECT
id,
authenticationConfiguration,
clientConfiguration,
description,
displayName,
endpointConfiguration
FROM entra_id.identity_governance.entitlement_management_resource_requests_catalog_custom_workflow_extensions
WHERE access_package_resource_request_id = '{{ access_package_resource_request_id }}' -- required
AND custom_callout_extension_id = '{{ custom_callout_extension_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
authenticationConfiguration,
clientConfiguration,
description,
displayName,
endpointConfiguration
FROM entra_id.identity_governance.entitlement_management_resource_requests_catalog_custom_workflow_extensions
WHERE access_package_resource_request_id = '{{ access_package_resource_request_id }}' -- required
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
INSERT INTO entra_id.identity_governance.entitlement_management_resource_requests_catalog_custom_workflow_extensions (
id,
authenticationConfiguration,
clientConfiguration,
description,
displayName,
endpointConfiguration,
access_package_resource_request_id
)
SELECT 
'{{ id }}',
'{{ authenticationConfiguration }}',
'{{ clientConfiguration }}',
'{{ description }}',
'{{ displayName }}',
'{{ endpointConfiguration }}',
'{{ access_package_resource_request_id }}'
RETURNING
id,
authenticationConfiguration,
clientConfiguration,
description,
displayName,
endpointConfiguration
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_resource_requests_catalog_custom_workflow_extensions
  props:
    - name: access_package_resource_request_id
      value: "{{ access_package_resource_request_id }}"
      description: Required parameter for the entitlement_management_resource_requests_catalog_custom_workflow_extensions resource.
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
UPDATE entra_id.identity_governance.entitlement_management_resource_requests_catalog_custom_workflow_extensions
SET 
id = '{{ id }}',
authenticationConfiguration = '{{ authenticationConfiguration }}',
clientConfiguration = '{{ clientConfiguration }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
endpointConfiguration = '{{ endpointConfiguration }}'
WHERE 
access_package_resource_request_id = '{{ access_package_resource_request_id }}' --required
AND custom_callout_extension_id = '{{ custom_callout_extension_id }}' --required
RETURNING
id,
authenticationConfiguration,
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

No description available.

```sql
DELETE FROM entra_id.identity_governance.entitlement_management_resource_requests_catalog_custom_workflow_extensions
WHERE access_package_resource_request_id = '{{ access_package_resource_request_id }}' --required
AND custom_callout_extension_id = '{{ custom_callout_extension_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
