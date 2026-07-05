--- 
title: entitlement_management_assignment_policies_custom_extension_stage_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_assignment_policies_custom_extension_stage_settings
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_assignment_policies_custom_extension_stage_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_assignment_policies_custom_extension_stage_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_assignment_policies_custom_extension_stage_settings" /></td></tr>
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
    <td><CopyableCode code="customExtension" /></td>
    <td><code></code></td>
    <td>Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="stage" /></td>
    <td><code>string</code></td>
    <td> (assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue) (title: accessPackageCustomExtensionStage)</td>
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
    <td><CopyableCode code="customExtension" /></td>
    <td><code></code></td>
    <td>Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="stage" /></td>
    <td><code>string</code></td>
    <td> (assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue) (title: accessPackageCustomExtensionStage)</td>
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
    <td><a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a>, <a href="#parameter-custom_extension_stage_setting_id"><code>custom_extension_stage_setting_id</code></a></td>
    <td></td>
    <td>The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a></td>
    <td></td>
    <td>The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a>, <a href="#parameter-custom_extension_stage_setting_id"><code>custom_extension_stage_setting_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a>, <a href="#parameter-custom_extension_stage_setting_id"><code>custom_extension_stage_setting_id</code></a></td>
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
<tr id="parameter-access_package_assignment_policy_id">
    <td><CopyableCode code="access_package_assignment_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageAssignmentPolicy</td>
</tr>
<tr id="parameter-custom_extension_stage_setting_id">
    <td><CopyableCode code="custom_extension_stage_setting_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of customExtensionStageSetting</td>
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

The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.

```sql
SELECT
id,
customExtension,
stage
FROM entra_id.identity_governance.entitlement_management_assignment_policies_custom_extension_stage_settings
WHERE access_package_assignment_policy_id = '{{ access_package_assignment_policy_id }}' -- required
AND custom_extension_stage_setting_id = '{{ custom_extension_stage_setting_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.

```sql
SELECT
id,
customExtension,
stage
FROM entra_id.identity_governance.entitlement_management_assignment_policies_custom_extension_stage_settings
WHERE access_package_assignment_policy_id = '{{ access_package_assignment_policy_id }}' -- required
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
INSERT INTO entra_id.identity_governance.entitlement_management_assignment_policies_custom_extension_stage_settings (
id,
stage,
customExtension,
access_package_assignment_policy_id
)
SELECT 
'{{ id }}',
'{{ stage }}',
'{{ customExtension }}',
'{{ access_package_assignment_policy_id }}'
RETURNING
id,
customExtension,
stage
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_assignment_policies_custom_extension_stage_settings
  props:
    - name: access_package_assignment_policy_id
      value: "{{ access_package_assignment_policy_id }}"
      description: Required parameter for the entitlement_management_assignment_policies_custom_extension_stage_settings resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: stage
      value: "{{ stage }}"
      valid_values: ['assignmentRequestCreated', 'assignmentRequestApproved', 'assignmentRequestGranted', 'assignmentRequestRemoved', 'assignmentFourteenDaysBeforeExpiration', 'assignmentOneDayBeforeExpiration', 'unknownFutureValue']
    - name: customExtension
      value: "{{ customExtension }}"
      description: |
        Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.
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
UPDATE entra_id.identity_governance.entitlement_management_assignment_policies_custom_extension_stage_settings
SET 
id = '{{ id }}',
stage = '{{ stage }}',
customExtension = '{{ customExtension }}'
WHERE 
access_package_assignment_policy_id = '{{ access_package_assignment_policy_id }}' --required
AND custom_extension_stage_setting_id = '{{ custom_extension_stage_setting_id }}' --required
RETURNING
id,
customExtension,
stage;
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
DELETE FROM entra_id.identity_governance.entitlement_management_assignment_policies_custom_extension_stage_settings
WHERE access_package_assignment_policy_id = '{{ access_package_assignment_policy_id }}' --required
AND custom_extension_stage_setting_id = '{{ custom_extension_stage_setting_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
