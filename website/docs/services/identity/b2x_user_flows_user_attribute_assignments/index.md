--- 
title: b2x_user_flows_user_attribute_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_user_attribute_assignments
  - identity
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_user_attribute_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_user_attribute_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity.b2x_user_flows_user_attribute_assignments" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-identityUserFlowAttributeAssignment-id"><code>identityUserFlowAttributeAssignment-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of an identityUserFlowAttributeAssignment object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the identityUserFlowAttributeAssignment resources from the userAttributeAssignments navigation property in a b2xIdentityUserFlow.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new identityUserFlowAttributeAssignment object in a b2xIdentityUserFlow.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-identityUserFlowAttributeAssignment-id"><code>identityUserFlowAttributeAssignment-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a identityUserFlowAttributeAssignment object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-identityUserFlowAttributeAssignment-id"><code>identityUserFlowAttributeAssignment-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an identityUserFlowAttributeAssignment object.</td>
</tr>
<tr>
    <td><a href="#set_order"><CopyableCode code="set_order" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
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
<tr id="parameter-b2xIdentityUserFlow-id">
    <td><CopyableCode code="b2xIdentityUserFlow-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of b2xIdentityUserFlow</td>
</tr>
<tr id="parameter-identityUserFlowAttributeAssignment-id">
    <td><CopyableCode code="identityUserFlowAttributeAssignment-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of identityUserFlowAttributeAssignment</td>
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

Read the properties and relationships of an identityUserFlowAttributeAssignment object.

```sql
SELECT
id,
@odata.type,
displayName,
isOptional,
requiresVerification,
userAttribute,
userAttributeValues,
userInputType
FROM entraid.identity.b2x_user_flows_user_attribute_assignments
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' -- required
AND identityUserFlowAttributeAssignment-id = '{{ identityUserFlowAttributeAssignment-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get the identityUserFlowAttributeAssignment resources from the userAttributeAssignments navigation property in a b2xIdentityUserFlow.

```sql
SELECT
id,
@odata.type,
displayName,
isOptional,
requiresVerification,
userAttribute,
userAttributeValues,
userInputType
FROM entraid.identity.b2x_user_flows_user_attribute_assignments
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' -- required
AND $top = '{{ $top }}'
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

Create a new identityUserFlowAttributeAssignment object in a b2xIdentityUserFlow.

```sql
INSERT INTO entraid.identity.b2x_user_flows_user_attribute_assignments (
id,
@odata.type,
displayName,
isOptional,
requiresVerification,
userAttributeValues,
userInputType,
userAttribute,
b2xIdentityUserFlow-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ displayName }}',
{{ isOptional }},
{{ requiresVerification }},
'{{ userAttributeValues }}',
'{{ userInputType }}',
'{{ userAttribute }}',
'{{ b2xIdentityUserFlow-id }}'
RETURNING
id,
@odata.type,
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
    - name: b2xIdentityUserFlow-id
      value: "{{ b2xIdentityUserFlow-id }}"
      description: Required parameter for the b2x_user_flows_user_attribute_assignments resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
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
          @odata.type: "{{ @odata.type }}"
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
UPDATE entraid.identity.b2x_user_flows_user_attribute_assignments
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
displayName = '{{ displayName }}',
isOptional = {{ isOptional }},
requiresVerification = {{ requiresVerification }},
userAttributeValues = '{{ userAttributeValues }}',
userInputType = '{{ userInputType }}',
userAttribute = '{{ userAttribute }}'
WHERE 
b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' --required
AND identityUserFlowAttributeAssignment-id = '{{ identityUserFlowAttributeAssignment-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
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
DELETE FROM entraid.identity.b2x_user_flows_user_attribute_assignments
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' --required
AND identityUserFlowAttributeAssignment-id = '{{ identityUserFlowAttributeAssignment-id }}' --required
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
EXEC entraid.identity.b2x_user_flows_user_attribute_assignments.set_order 
@b2xIdentityUserFlow-id='{{ b2xIdentityUserFlow-id }}' --required 
@@json=
'{
"newAssignmentOrder": "{{ newAssignmentOrder }}"
}'
;
```
</TabItem>
</Tabs>
