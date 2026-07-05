--- 
title: user_flow_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - user_flow_attributes
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

Creates, updates, deletes, gets or lists a <code>user_flow_attributes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="user_flow_attributes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.user_flow_attributes" /></td></tr>
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
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td> (string, boolean, int64, stringCollection, dateTime, unknownFutureValue) (title: identityUserFlowAttributeDataType)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the user flow attribute that's shown to the user at the time of sign up.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user flow attribute.  Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="userFlowAttributeType" /></td>
    <td><code>string</code></td>
    <td> (builtIn, custom, required, unknownFutureValue) (title: identityUserFlowAttributeType)</td>
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
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td> (string, boolean, int64, stringCollection, dateTime, unknownFutureValue) (title: identityUserFlowAttributeDataType)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the user flow attribute that's shown to the user at the time of sign up.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user flow attribute.  Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="userFlowAttributeType" /></td>
    <td><code>string</code></td>
    <td> (builtIn, custom, required, unknownFutureValue) (title: identityUserFlowAttributeType)</td>
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
    <td><a href="#parameter-identity_user_flow_attribute_id"><code>identity_user_flow_attribute_id</code></a></td>
    <td></td>
    <td>Retrieve the properties and relationships of a identityUserFlowAttribute object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of identityUserFlowAttribute objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new custom identityUserFlowAttribute object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-identity_user_flow_attribute_id"><code>identity_user_flow_attribute_id</code></a></td>
    <td></td>
    <td>Update the properties of a custom identityUserFlowAttribute object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-identity_user_flow_attribute_id"><code>identity_user_flow_attribute_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a custom identityUserFlowAttribute.</td>
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
<tr id="parameter-identity_user_flow_attribute_id">
    <td><CopyableCode code="identity_user_flow_attribute_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of identityUserFlowAttribute</td>
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

Retrieve the properties and relationships of a identityUserFlowAttribute object.

```sql
SELECT
id,
dataType,
description,
displayName,
userFlowAttributeType
FROM entra_id.identity.user_flow_attributes
WHERE identity_user_flow_attribute_id = '{{ identity_user_flow_attribute_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of identityUserFlowAttribute objects.

```sql
SELECT
id,
dataType,
description,
displayName,
userFlowAttributeType
FROM entra_id.identity.user_flow_attributes
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

Create a new custom identityUserFlowAttribute object.

```sql
INSERT INTO entra_id.identity.user_flow_attributes (
id,
dataType,
description,
displayName,
userFlowAttributeType
)
SELECT 
'{{ id }}',
'{{ dataType }}',
'{{ description }}',
'{{ displayName }}',
'{{ userFlowAttributeType }}'
RETURNING
id,
dataType,
description,
displayName,
userFlowAttributeType
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: user_flow_attributes
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: dataType
      value: "{{ dataType }}"
      valid_values: ['string', 'boolean', 'int64', 'stringCollection', 'dateTime', 'unknownFutureValue']
    - name: description
      value: "{{ description }}"
      description: |
        The description of the user flow attribute that's shown to the user at the time of sign up.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the user flow attribute.  Supports $filter (eq, ne).
    - name: userFlowAttributeType
      value: "{{ userFlowAttributeType }}"
      valid_values: ['builtIn', 'custom', 'required', 'unknownFutureValue']
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

Update the properties of a custom identityUserFlowAttribute object.

```sql
UPDATE entra_id.identity.user_flow_attributes
SET 
id = '{{ id }}',
dataType = '{{ dataType }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
userFlowAttributeType = '{{ userFlowAttributeType }}'
WHERE 
identity_user_flow_attribute_id = '{{ identity_user_flow_attribute_id }}' --required
RETURNING
id,
dataType,
description,
displayName,
userFlowAttributeType;
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

Delete a custom identityUserFlowAttribute.

```sql
DELETE FROM entra_id.identity.user_flow_attributes
WHERE identity_user_flow_attribute_id = '{{ identity_user_flow_attribute_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
