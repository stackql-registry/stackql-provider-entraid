--- 
title: app_role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - app_role_assignments
  - users
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

Creates, updates, deletes, gets or lists an <code>app_role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_role_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.app_role_assignments" /></td></tr>
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
    <td><CopyableCode code="appRoleId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The identifier (id) for the app role that's assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application hasn't declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user, group, or service principal that was granted the app role assignment. Maximum length is 256 characters. Read-only. Supports $filter (eq and startswith).</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource app's service principal to which the assignment is made. Maximum length is 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only). (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
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
    <td><CopyableCode code="appRoleId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The identifier (id) for the app role that's assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application hasn't declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user, group, or service principal that was granted the app role assignment. Maximum length is 256 characters. Read-only. Supports $filter (eq and startswith).</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource app's service principal to which the assignment is made. Maximum length is 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only). (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
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
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-app_role_assignment_id"><code>app_role_assignment_id</code></a></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a></td>
    <td>Represents the app roles a user is granted for an application. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a></td>
    <td>Retrieve the list of appRoleAssignments granted to an agentUser.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>Grant an app role assignment to an agentUser.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-app_role_assignment_id"><code>app_role_assignment_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-app_role_assignment_id"><code>app_role_assignment_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an appRoleAssignment that has been granted to a user.</td>
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
<tr id="parameter-app_role_assignment_id">
    <td><CopyableCode code="app_role_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of appRoleAssignment</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of user</td>
</tr>
<tr id="parameter-ConsistencyLevel">
    <td><CopyableCode code="ConsistencyLevel" /></td>
    <td><code>string</code></td>
    <td>Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries</td>
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

Represents the app roles a user is granted for an application. Supports $expand.

```sql
SELECT
id,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId
FROM entra_id.users.app_role_assignments
WHERE user_id = '{{ user_id }}' -- required
AND app_role_assignment_id = '{{ app_role_assignment_id }}' -- required
AND ConsistencyLevel = '{{ ConsistencyLevel }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve the list of appRoleAssignments granted to an agentUser.

```sql
SELECT
id,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId
FROM entra_id.users.app_role_assignments
WHERE user_id = '{{ user_id }}' -- required
AND ConsistencyLevel = '{{ ConsistencyLevel }}'
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

Grant an app role assignment to an agentUser.

```sql
INSERT INTO entra_id.users.app_role_assignments (
id,
deletedDateTime,
appRoleId,
createdDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId,
user_id
)
SELECT 
'{{ id }}',
'{{ deletedDateTime }}',
'{{ appRoleId }}',
'{{ createdDateTime }}',
'{{ principalDisplayName }}',
'{{ principalId }}',
'{{ principalType }}',
'{{ resourceDisplayName }}',
'{{ resourceId }}',
'{{ user_id }}'
RETURNING
id,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_role_assignments
  props:
    - name: user_id
      value: "{{ user_id }}"
      description: Required parameter for the app_role_assignments resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: appRoleId
      value: "{{ appRoleId }}"
      description: |
        The identifier (id) for the app role that's assigned to the principal. This app role must be exposed in the appRoles property on the resource application's service principal (resourceId). If the resource application hasn't declared any app roles, a default app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the principal is assigned to the resource app without any specific app roles. Required on create.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The time when the app role assignment was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: principalDisplayName
      value: "{{ principalDisplayName }}"
      description: |
        The display name of the user, group, or service principal that was granted the app role assignment. Maximum length is 256 characters. Read-only. Supports $filter (eq and startswith).
    - name: principalId
      value: "{{ principalId }}"
      description: |
        The unique identifier (id) for the user, security group, or service principal being granted the app role. Security groups with dynamic memberships are supported. Required on create.
    - name: principalType
      value: "{{ principalType }}"
      description: |
        The type of the assigned principal. This can either be User, Group, or ServicePrincipal. Read-only.
    - name: resourceDisplayName
      value: "{{ resourceDisplayName }}"
      description: |
        The display name of the resource app's service principal to which the assignment is made. Maximum length is 256 characters.
    - name: resourceId
      value: "{{ resourceId }}"
      description: |
        The unique identifier (id) for the resource service principal for which the assignment is made. Required on create. Supports $filter (eq only).
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
UPDATE entra_id.users.app_role_assignments
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
appRoleId = '{{ appRoleId }}',
createdDateTime = '{{ createdDateTime }}',
principalDisplayName = '{{ principalDisplayName }}',
principalId = '{{ principalId }}',
principalType = '{{ principalType }}',
resourceDisplayName = '{{ resourceDisplayName }}',
resourceId = '{{ resourceId }}'
WHERE 
user_id = '{{ user_id }}' --required
AND app_role_assignment_id = '{{ app_role_assignment_id }}' --required
RETURNING
id,
appRoleId,
createdDateTime,
deletedDateTime,
principalDisplayName,
principalId,
principalType,
resourceDisplayName,
resourceId;
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

Delete an appRoleAssignment that has been granted to a user.

```sql
DELETE FROM entra_id.users.app_role_assignments
WHERE user_id = '{{ user_id }}' --required
AND app_role_assignment_id = '{{ app_role_assignment_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
