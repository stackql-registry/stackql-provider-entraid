--- 
title: entitlement_management_access_packages_assignment_policies_custom_extension_stage_settings_custom_extension
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_access_packages_assignment_policies_custom_extension_stage_settings_custom_extension
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_access_packages_assignment_policies_custom_extension_stage_settings_custom_extension</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_access_packages_assignment_policies_custom_extension_stage_settings_custom_extension" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.entitlement_management_access_packages_assignment_policies_custom_extension_stage_settings_custom_extension" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><a href="#parameter-accessPackage-id"><code>accessPackage-id</code></a>, <a href="#parameter-accessPackageAssignmentPolicy-id"><code>accessPackageAssignmentPolicy-id</code></a>, <a href="#parameter-customExtensionStageSetting-id"><code>customExtensionStageSetting-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.</td>
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
<tr id="parameter-accessPackage-id">
    <td><CopyableCode code="accessPackage-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackage</td>
</tr>
<tr id="parameter-accessPackageAssignmentPolicy-id">
    <td><CopyableCode code="accessPackageAssignmentPolicy-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageAssignmentPolicy</td>
</tr>
<tr id="parameter-customExtensionStageSetting-id">
    <td><CopyableCode code="customExtensionStageSetting-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customExtensionStageSetting</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.

```sql
SELECT
id,
@odata.type,
authenticationConfiguration,
clientConfiguration,
description,
displayName,
endpointConfiguration
FROM entraid.identity_governance.entitlement_management_access_packages_assignment_policies_custom_extension_stage_settings_custom_extension
WHERE accessPackage-id = '{{ accessPackage-id }}' -- required
AND accessPackageAssignmentPolicy-id = '{{ accessPackageAssignmentPolicy-id }}' -- required
AND customExtensionStageSetting-id = '{{ customExtensionStageSetting-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
