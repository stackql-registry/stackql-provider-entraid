--- 
title: app_management_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - app_management_policies
  - policies
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

Creates, updates, deletes, gets or lists an <code>app_management_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_management_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.app_management_policies" /></td></tr>
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
    <td><CopyableCode code="appliesTo" /></td>
    <td><code>array</code></td>
    <td>Collection of applications and service principals to which the policy is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Denotes whether the policy is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="restrictions" /></td>
    <td><code></code></td>
    <td>Restrictions that apply to an application or service principal object.</td>
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
    <td><CopyableCode code="appliesTo" /></td>
    <td><code>array</code></td>
    <td>Collection of applications and service principals to which the policy is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Denotes whether the policy is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="restrictions" /></td>
    <td><code></code></td>
    <td>Restrictions that apply to an application or service principal object.</td>
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
    <td><a href="#parameter-app_management_policy_id"><code>app_management_policy_id</code></a></td>
    <td></td>
    <td>Read the properties of an appManagementPolicy object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of appManagementPolicy objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create an appManagementPolicy object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-app_management_policy_id"><code>app_management_policy_id</code></a></td>
    <td></td>
    <td>Update an appManagementPolicy object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_management_policy_id"><code>app_management_policy_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an appManagementPolicy object.</td>
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
<tr id="parameter-app_management_policy_id">
    <td><CopyableCode code="app_management_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of appManagementPolicy</td>
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

Read the properties of an appManagementPolicy object.

```sql
SELECT
id,
appliesTo,
deletedDateTime,
description,
displayName,
isEnabled,
restrictions
FROM entra_id.policies.app_management_policies
WHERE app_management_policy_id = '{{ app_management_policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of appManagementPolicy objects.

```sql
SELECT
id,
appliesTo,
deletedDateTime,
description,
displayName,
isEnabled,
restrictions
FROM entra_id.policies.app_management_policies
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

Create an appManagementPolicy object.

```sql
INSERT INTO entra_id.policies.app_management_policies (
id,
deletedDateTime,
description,
displayName,
isEnabled,
restrictions,
appliesTo
)
SELECT 
'{{ id }}',
'{{ deletedDateTime }}',
'{{ description }}',
'{{ displayName }}',
{{ isEnabled }},
'{{ restrictions }}',
'{{ appliesTo }}'
RETURNING
id,
appliesTo,
deletedDateTime,
description,
displayName,
isEnabled,
restrictions
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_management_policies
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: description
      value: "{{ description }}"
      description: |
        Description for this policy. Required.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name for this policy. Required.
    - name: isEnabled
      value: {{ isEnabled }}
      description: |
        Denotes whether the policy is enabled.
    - name: restrictions
      value: "{{ restrictions }}"
      description: |
        Restrictions that apply to an application or service principal object.
    - name: appliesTo
      description: |
        Collection of applications and service principals to which the policy is applied.
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
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

Update an appManagementPolicy object.

```sql
UPDATE entra_id.policies.app_management_policies
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isEnabled = {{ isEnabled }},
restrictions = '{{ restrictions }}',
appliesTo = '{{ appliesTo }}'
WHERE 
app_management_policy_id = '{{ app_management_policy_id }}' --required
RETURNING
id,
appliesTo,
deletedDateTime,
description,
displayName,
isEnabled,
restrictions;
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

Delete an appManagementPolicy object.

```sql
DELETE FROM entra_id.policies.app_management_policies
WHERE app_management_policy_id = '{{ app_management_policy_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
