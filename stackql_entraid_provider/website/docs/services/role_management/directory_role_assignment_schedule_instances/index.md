--- 
title: directory_role_assignment_schedule_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_role_assignment_schedule_instances
  - role_management
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

Creates, updates, deletes, gets or lists a <code>directory_role_assignment_schedule_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="directory_role_assignment_schedule_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.directory_role_assignment_schedule_instances" /></td></tr>
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
    <td><CopyableCode code="activatedUsing" /></td>
    <td><code></code></td>
    <td>If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app-specific scope when the assignment or role eligibility is scoped to an app. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app-specific scope when the assignment or role eligibility is scoped to an app. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the assignment or role eligibility. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment or role eligibility. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the schedule instance. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code>string</code></td>
    <td>How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>The principal that's getting a role assignment or role eligibility through the request.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal that has been granted the role assignment or that's eligible for a role.</td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignmentOriginId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the role assignment in Microsoft Entra. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignmentScheduleId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the unifiedRoleAssignmentSchedule object from which this instance was created. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that the principal is eligible for.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When this instance starts. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><CopyableCode code="activatedUsing" /></td>
    <td><code></code></td>
    <td>If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app-specific scope when the assignment or role eligibility is scoped to an app. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app-specific scope when the assignment or role eligibility is scoped to an app. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the assignment or role eligibility. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment or role eligibility. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end date of the schedule instance. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code>string</code></td>
    <td>How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>The principal that's getting a role assignment or role eligibility through the request.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal that has been granted the role assignment or that's eligible for a role.</td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignmentOriginId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the role assignment in Microsoft Entra. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignmentScheduleId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the unifiedRoleAssignmentSchedule object from which this instance was created. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that the principal is eligible for.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When this instance starts. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-unified_role_assignment_schedule_instance_id"><code>unified_role_assignment_schedule_instance_id</code></a></td>
    <td></td>
    <td>Get the instance of an active role assignment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get the instances of active role assignments in your tenant. The active assignments include those made through assignments and activation requests, and directly through the role assignments API.</td>
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
    <td><a href="#parameter-unified_role_assignment_schedule_instance_id"><code>unified_role_assignment_schedule_instance_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_role_assignment_schedule_instance_id"><code>unified_role_assignment_schedule_instance_id</code></a></td>
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
<tr id="parameter-unified_role_assignment_schedule_instance_id">
    <td><CopyableCode code="unified_role_assignment_schedule_instance_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleAssignmentScheduleInstance</td>
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

Get the instance of an active role assignment.

```sql
SELECT
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
directoryScope,
directoryScopeId,
endDateTime,
memberType,
principal,
principalId,
roleAssignmentOriginId,
roleAssignmentScheduleId,
roleDefinition,
roleDefinitionId,
startDateTime
FROM entra_id.role_management.directory_role_assignment_schedule_instances
WHERE unified_role_assignment_schedule_instance_id = '{{ unified_role_assignment_schedule_instance_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the instances of active role assignments in your tenant. The active assignments include those made through assignments and activation requests, and directly through the role assignments API.

```sql
SELECT
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
directoryScope,
directoryScopeId,
endDateTime,
memberType,
principal,
principalId,
roleAssignmentOriginId,
roleAssignmentScheduleId,
roleDefinition,
roleDefinitionId,
startDateTime
FROM entra_id.role_management.directory_role_assignment_schedule_instances
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
INSERT INTO entra_id.role_management.directory_role_assignment_schedule_instances (
id,
appScopeId,
directoryScopeId,
principalId,
roleDefinitionId,
appScope,
directoryScope,
principal,
roleDefinition,
assignmentType,
endDateTime,
memberType,
roleAssignmentOriginId,
roleAssignmentScheduleId,
startDateTime,
activatedUsing
)
SELECT 
'{{ id }}',
'{{ appScopeId }}',
'{{ directoryScopeId }}',
'{{ principalId }}',
'{{ roleDefinitionId }}',
'{{ appScope }}',
'{{ directoryScope }}',
'{{ principal }}',
'{{ roleDefinition }}',
'{{ assignmentType }}',
'{{ endDateTime }}',
'{{ memberType }}',
'{{ roleAssignmentOriginId }}',
'{{ roleAssignmentScheduleId }}',
'{{ startDateTime }}',
'{{ activatedUsing }}'
RETURNING
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
directoryScope,
directoryScopeId,
endDateTime,
memberType,
principal,
principalId,
roleAssignmentOriginId,
roleAssignmentScheduleId,
roleDefinition,
roleDefinitionId,
startDateTime
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: directory_role_assignment_schedule_instances
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: appScopeId
      value: "{{ appScopeId }}"
      description: |
        Identifier of the app-specific scope when the assignment or role eligibility is scoped to an app. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
    - name: directoryScopeId
      value: "{{ directoryScopeId }}"
      description: |
        Identifier of the directory object representing the scope of the assignment or role eligibility. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
    - name: principalId
      value: "{{ principalId }}"
      description: |
        Identifier of the principal that has been granted the role assignment or that's eligible for a role.
    - name: roleDefinitionId
      value: "{{ roleDefinitionId }}"
      description: |
        Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that the principal is eligible for.
    - name: appScope
      value: "{{ appScope }}"
      description: |
        Read-only property with details of the app-specific scope when the assignment or role eligibility is scoped to an app. Nullable.
    - name: directoryScope
      value: "{{ directoryScope }}"
      description: |
        The directory object that is the scope of the assignment or role eligibility. Read-only.
    - name: principal
      value: "{{ principal }}"
      description: |
        The principal that's getting a role assignment or role eligibility through the request.
    - name: roleDefinition
      value: "{{ roleDefinition }}"
      description: |
        Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
    - name: assignmentType
      value: "{{ assignmentType }}"
      description: |
        The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).
    - name: endDateTime
      value: "{{ endDateTime }}"
      description: |
        The end date of the schedule instance.
    - name: memberType
      value: "{{ memberType }}"
      description: |
        How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
    - name: roleAssignmentOriginId
      value: "{{ roleAssignmentOriginId }}"
      description: |
        The identifier of the role assignment in Microsoft Entra. Supports $filter (eq, ne).
    - name: roleAssignmentScheduleId
      value: "{{ roleAssignmentScheduleId }}"
      description: |
        The identifier of the unifiedRoleAssignmentSchedule object from which this instance was created. Supports $filter (eq, ne).
    - name: startDateTime
      value: "{{ startDateTime }}"
      description: |
        When this instance starts.
    - name: activatedUsing
      value: "{{ activatedUsing }}"
      description: |
        If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.
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
UPDATE entra_id.role_management.directory_role_assignment_schedule_instances
SET 
id = '{{ id }}',
appScopeId = '{{ appScopeId }}',
directoryScopeId = '{{ directoryScopeId }}',
principalId = '{{ principalId }}',
roleDefinitionId = '{{ roleDefinitionId }}',
appScope = '{{ appScope }}',
directoryScope = '{{ directoryScope }}',
principal = '{{ principal }}',
roleDefinition = '{{ roleDefinition }}',
assignmentType = '{{ assignmentType }}',
endDateTime = '{{ endDateTime }}',
memberType = '{{ memberType }}',
roleAssignmentOriginId = '{{ roleAssignmentOriginId }}',
roleAssignmentScheduleId = '{{ roleAssignmentScheduleId }}',
startDateTime = '{{ startDateTime }}',
activatedUsing = '{{ activatedUsing }}'
WHERE 
unified_role_assignment_schedule_instance_id = '{{ unified_role_assignment_schedule_instance_id }}' --required
RETURNING
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
directoryScope,
directoryScopeId,
endDateTime,
memberType,
principal,
principalId,
roleAssignmentOriginId,
roleAssignmentScheduleId,
roleDefinition,
roleDefinitionId,
startDateTime;
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
DELETE FROM entra_id.role_management.directory_role_assignment_schedule_instances
WHERE unified_role_assignment_schedule_instance_id = '{{ unified_role_assignment_schedule_instance_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
