--- 
title: entitlement_management_role_assignment_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_role_assignment_schedules
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_role_assignment_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_role_assignment_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.entitlement_management_role_assignment_schedules" /></td></tr>
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
    <td>If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdUsing" /></td>
    <td><code>string</code></td>
    <td>Identifier of the object through which this schedule was created.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the role eligibility or assignment. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code>string</code></td>
    <td>How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was last modified. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>The principal that's getting a role assignment or that's eligible for a role through the request.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal that has been granted the role assignment or eligibility.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>The period of the role assignment. It can represent a single occurrence or multiple recurrences.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the role assignment or eligibility request.</td>
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
    <td>If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentType" /></td>
    <td><code>string</code></td>
    <td>The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdUsing" /></td>
    <td><code>string</code></td>
    <td>Identifier of the object through which this schedule was created.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the role eligibility or assignment. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code>string</code></td>
    <td>How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was last modified. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>The principal that's getting a role assignment or that's eligible for a role through the request.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal that has been granted the role assignment or eligibility.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>The period of the role assignment. It can represent a single occurrence or multiple recurrences.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the role assignment or eligibility request.</td>
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
    <td><a href="#parameter-unified_role_assignment_schedule_id"><code>unified_role_assignment_schedule_id</code></a></td>
    <td></td>
    <td>Schedules for active role assignment operations.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Schedules for active role assignment operations.</td>
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
    <td><a href="#parameter-unified_role_assignment_schedule_id"><code>unified_role_assignment_schedule_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_role_assignment_schedule_id"><code>unified_role_assignment_schedule_id</code></a></td>
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
<tr id="parameter-unified_role_assignment_schedule_id">
    <td><CopyableCode code="unified_role_assignment_schedule_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleAssignmentSchedule</td>
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

Schedules for active role assignment operations.

```sql
SELECT
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
createdDateTime,
createdUsing,
directoryScope,
directoryScopeId,
memberType,
modifiedDateTime,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status
FROM entra_id.role_management.entitlement_management_role_assignment_schedules
WHERE unified_role_assignment_schedule_id = '{{ unified_role_assignment_schedule_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Schedules for active role assignment operations.

```sql
SELECT
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
createdDateTime,
createdUsing,
directoryScope,
directoryScopeId,
memberType,
modifiedDateTime,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status
FROM entra_id.role_management.entitlement_management_role_assignment_schedules
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
INSERT INTO entra_id.role_management.entitlement_management_role_assignment_schedules (
id,
appScopeId,
createdDateTime,
createdUsing,
directoryScopeId,
modifiedDateTime,
principalId,
roleDefinitionId,
status,
appScope,
directoryScope,
principal,
roleDefinition,
assignmentType,
memberType,
scheduleInfo,
activatedUsing
)
SELECT 
'{{ id }}',
'{{ appScopeId }}',
'{{ createdDateTime }}',
'{{ createdUsing }}',
'{{ directoryScopeId }}',
'{{ modifiedDateTime }}',
'{{ principalId }}',
'{{ roleDefinitionId }}',
'{{ status }}',
'{{ appScope }}',
'{{ directoryScope }}',
'{{ principal }}',
'{{ roleDefinition }}',
'{{ assignmentType }}',
'{{ memberType }}',
'{{ scheduleInfo }}',
'{{ activatedUsing }}'
RETURNING
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
createdDateTime,
createdUsing,
directoryScope,
directoryScopeId,
memberType,
modifiedDateTime,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_role_assignment_schedules
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: appScopeId
      value: "{{ appScopeId }}"
      description: |
        Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        When the schedule was created.
    - name: createdUsing
      value: "{{ createdUsing }}"
      description: |
        Identifier of the object through which this schedule was created.
    - name: directoryScopeId
      value: "{{ directoryScopeId }}"
      description: |
        Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        When the schedule was last modified.
    - name: principalId
      value: "{{ principalId }}"
      description: |
        Identifier of the principal that has been granted the role assignment or eligibility.
    - name: roleDefinitionId
      value: "{{ roleDefinitionId }}"
      description: |
        Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.
    - name: status
      value: "{{ status }}"
      description: |
        The status of the role assignment or eligibility request.
    - name: appScope
      value: "{{ appScope }}"
      description: |
        Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.
    - name: directoryScope
      value: "{{ directoryScope }}"
      description: |
        The directory object that is the scope of the role eligibility or assignment. Read-only.
    - name: principal
      value: "{{ principal }}"
      description: |
        The principal that's getting a role assignment or that's eligible for a role through the request.
    - name: roleDefinition
      value: "{{ roleDefinition }}"
      description: |
        Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
    - name: assignmentType
      value: "{{ assignmentType }}"
      description: |
        The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).
    - name: memberType
      value: "{{ memberType }}"
      description: |
        How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
    - name: scheduleInfo
      value: "{{ scheduleInfo }}"
      description: |
        The period of the role assignment. It can represent a single occurrence or multiple recurrences.
    - name: activatedUsing
      value: "{{ activatedUsing }}"
      description: |
        If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand.
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
UPDATE entra_id.role_management.entitlement_management_role_assignment_schedules
SET 
id = '{{ id }}',
appScopeId = '{{ appScopeId }}',
createdDateTime = '{{ createdDateTime }}',
createdUsing = '{{ createdUsing }}',
directoryScopeId = '{{ directoryScopeId }}',
modifiedDateTime = '{{ modifiedDateTime }}',
principalId = '{{ principalId }}',
roleDefinitionId = '{{ roleDefinitionId }}',
status = '{{ status }}',
appScope = '{{ appScope }}',
directoryScope = '{{ directoryScope }}',
principal = '{{ principal }}',
roleDefinition = '{{ roleDefinition }}',
assignmentType = '{{ assignmentType }}',
memberType = '{{ memberType }}',
scheduleInfo = '{{ scheduleInfo }}',
activatedUsing = '{{ activatedUsing }}'
WHERE 
unified_role_assignment_schedule_id = '{{ unified_role_assignment_schedule_id }}' --required
RETURNING
id,
activatedUsing,
appScope,
appScopeId,
assignmentType,
createdDateTime,
createdUsing,
directoryScope,
directoryScopeId,
memberType,
modifiedDateTime,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status;
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
DELETE FROM entra_id.role_management.entitlement_management_role_assignment_schedules
WHERE unified_role_assignment_schedule_id = '{{ unified_role_assignment_schedule_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
