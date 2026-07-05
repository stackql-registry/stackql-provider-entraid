--- 
title: permission_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_grants
  - groups
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

Creates, updates, deletes, gets or lists a <code>permission_grants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="permission_grants" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.groups.permission_grants" /></td></tr>
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
    <td><CopyableCode code="clientAppId" /></td>
    <td><code>string</code></td>
    <td>ID of the service principal of the Microsoft Entra app that has been granted access. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>ID of the Microsoft Entra app that has been granted access. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="permission" /></td>
    <td><code>string</code></td>
    <td>The name of the resource-specific permission. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionType" /></td>
    <td><code>string</code></td>
    <td>The type of permission. The possible values are: Application, Delegated. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAppId" /></td>
    <td><code>string</code></td>
    <td>ID of the Microsoft Entra app that is hosting the resource. Read-only.</td>
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
    <td><CopyableCode code="clientAppId" /></td>
    <td><code>string</code></td>
    <td>ID of the service principal of the Microsoft Entra app that has been granted access. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>ID of the Microsoft Entra app that has been granted access. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="permission" /></td>
    <td><code>string</code></td>
    <td>The name of the resource-specific permission. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionType" /></td>
    <td><code>string</code></td>
    <td>The type of permission. The possible values are: Application, Delegated. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAppId" /></td>
    <td><code>string</code></td>
    <td>ID of the Microsoft Entra app that is hosting the resource. Read-only.</td>
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
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-resource_specific_permission_grant_id"><code>resource_specific_permission_grant_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td>List all resource-specific permission grants on the group. This list specifies the Microsoft Entra apps that have access to the group, along with the corresponding resource-specific access that each app has.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-resource_specific_permission_grant_id"><code>resource_specific_permission_grant_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-resource_specific_permission_grant_id"><code>resource_specific_permission_grant_id</code></a></td>
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
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of group</td>
</tr>
<tr id="parameter-resource_specific_permission_grant_id">
    <td><CopyableCode code="resource_specific_permission_grant_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of resourceSpecificPermissionGrant</td>
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
clientAppId,
clientId,
deletedDateTime,
permission,
permissionType,
resourceAppId
FROM entra_id.groups.permission_grants
WHERE group_id = '{{ group_id }}' -- required
AND resource_specific_permission_grant_id = '{{ resource_specific_permission_grant_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all resource-specific permission grants on the group. This list specifies the Microsoft Entra apps that have access to the group, along with the corresponding resource-specific access that each app has.

```sql
SELECT
id,
clientAppId,
clientId,
deletedDateTime,
permission,
permissionType,
resourceAppId
FROM entra_id.groups.permission_grants
WHERE group_id = '{{ group_id }}' -- required
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
INSERT INTO entra_id.groups.permission_grants (
id,
deletedDateTime,
clientAppId,
clientId,
permission,
permissionType,
resourceAppId,
group_id
)
SELECT 
'{{ id }}',
'{{ deletedDateTime }}',
'{{ clientAppId }}',
'{{ clientId }}',
'{{ permission }}',
'{{ permissionType }}',
'{{ resourceAppId }}',
'{{ group_id }}'
RETURNING
id,
clientAppId,
clientId,
deletedDateTime,
permission,
permissionType,
resourceAppId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: permission_grants
  props:
    - name: group_id
      value: "{{ group_id }}"
      description: Required parameter for the permission_grants resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: clientAppId
      value: "{{ clientAppId }}"
      description: |
        ID of the service principal of the Microsoft Entra app that has been granted access. Read-only.
    - name: clientId
      value: "{{ clientId }}"
      description: |
        ID of the Microsoft Entra app that has been granted access. Read-only.
    - name: permission
      value: "{{ permission }}"
      description: |
        The name of the resource-specific permission. Read-only.
    - name: permissionType
      value: "{{ permissionType }}"
      description: |
        The type of permission. The possible values are: Application, Delegated. Read-only.
    - name: resourceAppId
      value: "{{ resourceAppId }}"
      description: |
        ID of the Microsoft Entra app that is hosting the resource. Read-only.
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
UPDATE entra_id.groups.permission_grants
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
clientAppId = '{{ clientAppId }}',
clientId = '{{ clientId }}',
permission = '{{ permission }}',
permissionType = '{{ permissionType }}',
resourceAppId = '{{ resourceAppId }}'
WHERE 
group_id = '{{ group_id }}' --required
AND resource_specific_permission_grant_id = '{{ resource_specific_permission_grant_id }}' --required
RETURNING
id,
clientAppId,
clientId,
deletedDateTime,
permission,
permissionType,
resourceAppId;
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
DELETE FROM entra_id.groups.permission_grants
WHERE group_id = '{{ group_id }}' --required
AND resource_specific_permission_grant_id = '{{ resource_specific_permission_grant_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
