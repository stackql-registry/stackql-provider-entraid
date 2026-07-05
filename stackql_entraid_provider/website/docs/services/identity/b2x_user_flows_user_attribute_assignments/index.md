--- 
title: b2x_user_flows_user_attribute_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_user_attribute_assignments
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_user_attribute_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_user_attribute_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_user_attribute_assignments" /></td></tr>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the identityUserFlowAttribute within a user flow.</td>
</tr>
<tr>
    <td><CopyableCode code="isOptional" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the identityUserFlowAttribute is optional. true means the user doesn't have to provide a value. false means the user can't complete sign-up without providing a value.</td>
</tr>
<tr>
    <td><CopyableCode code="requiresVerification" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the identityUserFlowAttribute requires verification, and is only used for verifying the user's phone number or email address.</td>
</tr>
<tr>
    <td><CopyableCode code="userAttribute" /></td>
    <td><code></code></td>
    <td>The user attribute that you want to add to your user flow.</td>
</tr>
<tr>
    <td><CopyableCode code="userAttributeValues" /></td>
    <td><code>array</code></td>
    <td>The input options for the user flow attribute. Only applicable when the userInputType is radioSingleSelect, dropdownSingleSelect, or checkboxMultiSelect.</td>
</tr>
<tr>
    <td><CopyableCode code="userInputType" /></td>
    <td><code>string</code></td>
    <td> (textBox, dateTimeDropdown, radioSingleSelect, dropdownSingleSelect, emailBox, checkboxMultiSelect) (title: identityUserFlowAttributeInputType)</td>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the identityUserFlowAttribute within a user flow.</td>
</tr>
<tr>
    <td><CopyableCode code="isOptional" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the identityUserFlowAttribute is optional. true means the user doesn't have to provide a value. false means the user can't complete sign-up without providing a value.</td>
</tr>
<tr>
    <td><CopyableCode code="requiresVerification" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the identityUserFlowAttribute requires verification, and is only used for verifying the user's phone number or email address.</td>
</tr>
<tr>
    <td><CopyableCode code="userAttribute" /></td>
    <td><code></code></td>
    <td>The user attribute that you want to add to your user flow.</td>
</tr>
<tr>
    <td><CopyableCode code="userAttributeValues" /></td>
    <td><code>array</code></td>
    <td>The input options for the user flow attribute. Only applicable when the userInputType is radioSingleSelect, dropdownSingleSelect, or checkboxMultiSelect.</td>
</tr>
<tr>
    <td><CopyableCode code="userInputType" /></td>
    <td><code>string</code></td>
    <td> (textBox, dateTimeDropdown, radioSingleSelect, dropdownSingleSelect, emailBox, checkboxMultiSelect) (title: identityUserFlowAttributeInputType)</td>
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
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-identity_user_flow_attribute_assignment_id"><code>identity_user_flow_attribute_assignment_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of an identityUserFlowAttributeAssignment object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td>Get the identityUserFlowAttributeAssignment resources from the userAttributeAssignments navigation property in a b2xIdentityUserFlow.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td>Create a new identityUserFlowAttributeAssignment object in a b2xIdentityUserFlow.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-identity_user_flow_attribute_assignment_id"><code>identity_user_flow_attribute_assignment_id</code></a></td>
    <td></td>
    <td>Update the properties of a identityUserFlowAttributeAssignment object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-identity_user_flow_attribute_assignment_id"><code>identity_user_flow_attribute_assignment_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an identityUserFlowAttributeAssignment object.</td>
</tr>
<tr>
    <td><a href="#set_order"><CopyableCode code="set_order" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td>Set the order of identityUserFlowAttributeAssignments being collected within a user flow.</td>
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
<tr id="parameter-b2x_identity_user_flow_id">
    <td><CopyableCode code="b2x_identity_user_flow_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of b2xIdentityUserFlow</td>
</tr>
<tr id="parameter-identity_user_flow_attribute_assignment_id">
    <td><CopyableCode code="identity_user_flow_attribute_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of identityUserFlowAttributeAssignment</td>
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

Read the properties and relationships of an identityUserFlowAttributeAssignment object.

```sql
SELECT
id,
displayName,
isOptional,
requiresVerification,
userAttribute,
userAttributeValues,
userInputType
FROM entra_id.identity.b2x_user_flows_user_attribute_assignments
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
AND identity_user_flow_attribute_assignment_id = '{{ identity_user_flow_attribute_assignment_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the identityUserFlowAttributeAssignment resources from the userAttributeAssignments navigation property in a b2xIdentityUserFlow.

```sql
SELECT
id,
displayName,
isOptional,
requiresVerification,
userAttribute,
userAttributeValues,
userInputType
FROM entra_id.identity.b2x_user_flows_user_attribute_assignments
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
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

Create a new identityUserFlowAttributeAssignment object in a b2xIdentityUserFlow.

```sql
INSERT INTO entra_id.identity.b2x_user_flows_user_attribute_assignments (
id,
displayName,
isOptional,
requiresVerification,
userAttributeValues,
userInputType,
userAttribute,
b2x_identity_user_flow_id
)
SELECT 
'{{ id }}',
'{{ displayName }}',
{{ isOptional }},
{{ requiresVerification }},
'{{ userAttributeValues }}',
'{{ userInputType }}',
'{{ userAttribute }}',
'{{ b2x_identity_user_flow_id }}'
RETURNING
id,
displayName,
isOptional,
requiresVerification,
userAttribute,
userAttributeValues,
userInputType
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: b2x_user_flows_user_attribute_assignments
  props:
    - name: b2x_identity_user_flow_id
      value: "{{ b2x_identity_user_flow_id }}"
      description: Required parameter for the b2x_user_flows_user_attribute_assignments resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the identityUserFlowAttribute within a user flow.
    - name: isOptional
      value: {{ isOptional }}
      description: |
        Determines whether the identityUserFlowAttribute is optional. true means the user doesn't have to provide a value. false means the user can't complete sign-up without providing a value.
    - name: requiresVerification
      value: {{ requiresVerification }}
      description: |
        Determines whether the identityUserFlowAttribute requires verification, and is only used for verifying the user's phone number or email address.
    - name: userAttributeValues
      description: |
        The input options for the user flow attribute. Only applicable when the userInputType is radioSingleSelect, dropdownSingleSelect, or checkboxMultiSelect.
      value:
        - isDefault: {{ isDefault }}
          name: "{{ name }}"
          value: "{{ value }}"
    - name: userInputType
      value: "{{ userInputType }}"
      valid_values: ['textBox', 'dateTimeDropdown', 'radioSingleSelect', 'dropdownSingleSelect', 'emailBox', 'checkboxMultiSelect']
    - name: userAttribute
      value: "{{ userAttribute }}"
      description: |
        The user attribute that you want to add to your user flow.
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

Update the properties of a identityUserFlowAttributeAssignment object.

```sql
UPDATE entra_id.identity.b2x_user_flows_user_attribute_assignments
SET 
id = '{{ id }}',
displayName = '{{ displayName }}',
isOptional = {{ isOptional }},
requiresVerification = {{ requiresVerification }},
userAttributeValues = '{{ userAttributeValues }}',
userInputType = '{{ userInputType }}',
userAttribute = '{{ userAttribute }}'
WHERE 
b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' --required
AND identity_user_flow_attribute_assignment_id = '{{ identity_user_flow_attribute_assignment_id }}' --required
RETURNING
id,
displayName,
isOptional,
requiresVerification,
userAttribute,
userAttributeValues,
userInputType;
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

Delete an identityUserFlowAttributeAssignment object.

```sql
DELETE FROM entra_id.identity.b2x_user_flows_user_attribute_assignments
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' --required
AND identity_user_flow_attribute_assignment_id = '{{ identity_user_flow_attribute_assignment_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="set_order"
    values={[
        { label: 'set_order', value: 'set_order' }
    ]}
>
<TabItem value="set_order">

Set the order of identityUserFlowAttributeAssignments being collected within a user flow.

```sql
EXEC entra_id.identity.b2x_user_flows_user_attribute_assignments.set_order 
@b2x_identity_user_flow_id='{{ b2x_identity_user_flow_id }}' --required 
@@json=
'{
"newAssignmentOrder": "{{ newAssignmentOrder }}"
}'
;
```
</TabItem>
</Tabs>
