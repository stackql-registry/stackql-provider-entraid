--- 
title: conditional_access_authentication_context_class_references
hide_title: false
hide_table_of_contents: false
keywords:
  - conditional_access_authentication_context_class_references
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

Creates, updates, deletes, gets or lists a <code>conditional_access_authentication_context_class_references</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="conditional_access_authentication_context_class_references" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.conditional_access_authentication_context_class_references" /></td></tr>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short explanation of the policies that are enforced by authenticationContextClassReference. This value should be used to provide secondary text to describe the authentication context class reference when building user-facing admin experiences. For example, a selection UX.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name is the friendly name of the authenticationContextClassReference object. This value should be used to identify the authentication context class reference when building user-facing admin experiences. For example, a selection UX.</td>
</tr>
<tr>
    <td><CopyableCode code="isAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the authenticationContextClassReference has been published by the security admin and is ready for use by apps. When it's set to false, it shouldn't be shown in authentication context selection UX, or used to protect app resources. It's shown and available for Conditional Access policy authoring. The default value is false.  Supports $filter (eq).</td>
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A short explanation of the policies that are enforced by authenticationContextClassReference. This value should be used to provide secondary text to describe the authentication context class reference when building user-facing admin experiences. For example, a selection UX.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name is the friendly name of the authenticationContextClassReference object. This value should be used to identify the authentication context class reference when building user-facing admin experiences. For example, a selection UX.</td>
</tr>
<tr>
    <td><CopyableCode code="isAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the authenticationContextClassReference has been published by the security admin and is ready for use by apps. When it's set to false, it shouldn't be shown in authentication context selection UX, or used to protect app resources. It's shown and available for Conditional Access policy authoring. The default value is false.  Supports $filter (eq).</td>
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
    <td><a href="#parameter-authentication_context_class_reference_id"><code>authentication_context_class_reference_id</code></a></td>
    <td></td>
    <td>Retrieve the properties and relationships of a authenticationContextClassReference object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of authenticationContextClassReference objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-authentication_context_class_reference_id"><code>authentication_context_class_reference_id</code></a></td>
    <td></td>
    <td>Create an authenticationContextClassReference object, if the ID has not been used. If ID has been used, this call updates the authenticationContextClassReference object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-authentication_context_class_reference_id"><code>authentication_context_class_reference_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an authenticationContextClassReference object that's not published or used by a conditional access policy.</td>
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
<tr id="parameter-authentication_context_class_reference_id">
    <td><CopyableCode code="authentication_context_class_reference_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of authenticationContextClassReference</td>
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

Retrieve the properties and relationships of a authenticationContextClassReference object.

```sql
SELECT
id,
description,
displayName,
isAvailable
FROM entra_id.identity.conditional_access_authentication_context_class_references
WHERE authentication_context_class_reference_id = '{{ authentication_context_class_reference_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of authenticationContextClassReference objects.

```sql
SELECT
id,
description,
displayName,
isAvailable
FROM entra_id.identity.conditional_access_authentication_context_class_references
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
INSERT INTO entra_id.identity.conditional_access_authentication_context_class_references (
id,
description,
displayName,
isAvailable
)
SELECT 
'{{ id }}',
'{{ description }}',
'{{ displayName }}',
{{ isAvailable }}
RETURNING
id,
description,
displayName,
isAvailable
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: conditional_access_authentication_context_class_references
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        A short explanation of the policies that are enforced by authenticationContextClassReference. This value should be used to provide secondary text to describe the authentication context class reference when building user-facing admin experiences. For example, a selection UX.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name is the friendly name of the authenticationContextClassReference object. This value should be used to identify the authentication context class reference when building user-facing admin experiences. For example, a selection UX.
    - name: isAvailable
      value: {{ isAvailable }}
      description: |
        Indicates whether the authenticationContextClassReference has been published by the security admin and is ready for use by apps. When it's set to false, it shouldn't be shown in authentication context selection UX, or used to protect app resources. It's shown and available for Conditional Access policy authoring. The default value is false.  Supports $filter (eq).
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

Create an authenticationContextClassReference object, if the ID has not been used. If ID has been used, this call updates the authenticationContextClassReference object.

```sql
UPDATE entra_id.identity.conditional_access_authentication_context_class_references
SET 
id = '{{ id }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isAvailable = {{ isAvailable }}
WHERE 
authentication_context_class_reference_id = '{{ authentication_context_class_reference_id }}' --required
RETURNING
id,
description,
displayName,
isAvailable;
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

Delete an authenticationContextClassReference object that's not published or used by a conditional access policy.

```sql
DELETE FROM entra_id.identity.conditional_access_authentication_context_class_references
WHERE authentication_context_class_reference_id = '{{ authentication_context_class_reference_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
