--- 
title: entitlement_management_role_assignment_schedule_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_role_assignment_schedule_requests
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_role_assignment_schedule_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_role_assignment_schedule_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.entitlement_management_role_assignment_schedule_requests" /></td></tr>
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
    <td><CopyableCode code="action" /></td>
    <td><code></code></td>
    <td>Represents the type of the operation on the role assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew, selfExtend, selfRenew, unknownFutureValue. adminAssign: For administrators to assign roles to principals.adminRemove: For administrators to remove principals from roles. adminUpdate: For administrators to change existing role assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.selfExtend: For principals to request to extend their expiring assignments.selfRenew: For principals to request to renew their expired assignments.</td>
</tr>
<tr>
    <td><CopyableCode code="activatedUsing" /></td>
    <td><code></code></td>
    <td>If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app-specific scope when the assignment is scoped to an app. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app-specific scope when the assignment is scoped to an app. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units. Supports $filter (eq, ne, and on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="approvalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the approval of the request.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request completion date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>The principal that created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request creation date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customData" /></td>
    <td><code>string</code></td>
    <td>Free text field to define any custom data for the request. Not used.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the assignment. Read-only. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only. Supports $filter (eq, ne, and on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="isValidationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>A message provided by users and administrators when create they create the unifiedRoleAssignmentScheduleRequest object.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>The principal that's getting a role assignment through the request. Supports $expand and $select nested in $expand for id only.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal that has been granted the assignment. Can be a user, role-assignable group, or a service principal. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>Detailed information for the unifiedRoleDefinition object that is referenced through the roleDefinitionId property. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition object that is being assigned to the principal. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>The period of the role assignment. Recurring schedules are currently unsupported.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSchedule" /></td>
    <td><code></code></td>
    <td>The schedule for an eligible role assignment that is referenced through the targetScheduleId property. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="targetScheduleId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the schedule object that's linked to the assignment request. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="ticketInfo" /></td>
    <td><code></code></td>
    <td>Ticket details linked to the role assignment request including details of the ticket number and ticket system.</td>
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
    <td><CopyableCode code="action" /></td>
    <td><code></code></td>
    <td>Represents the type of the operation on the role assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew, selfExtend, selfRenew, unknownFutureValue. adminAssign: For administrators to assign roles to principals.adminRemove: For administrators to remove principals from roles. adminUpdate: For administrators to change existing role assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.selfExtend: For principals to request to extend their expiring assignments.selfRenew: For principals to request to renew their expired assignments.</td>
</tr>
<tr>
    <td><CopyableCode code="activatedUsing" /></td>
    <td><code></code></td>
    <td>If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app-specific scope when the assignment is scoped to an app. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app-specific scope when the assignment is scoped to an app. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units. Supports $filter (eq, ne, and on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="approvalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the approval of the request.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request completion date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>The principal that created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request creation date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customData" /></td>
    <td><code>string</code></td>
    <td>Free text field to define any custom data for the request. Not used.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the assignment. Read-only. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only. Supports $filter (eq, ne, and on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="isValidationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>A message provided by users and administrators when create they create the unifiedRoleAssignmentScheduleRequest object.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>The principal that's getting a role assignment through the request. Supports $expand and $select nested in $expand for id only.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal that has been granted the assignment. Can be a user, role-assignable group, or a service principal. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>Detailed information for the unifiedRoleDefinition object that is referenced through the roleDefinitionId property. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition object that is being assigned to the principal. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>The period of the role assignment. Recurring schedules are currently unsupported.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSchedule" /></td>
    <td><code></code></td>
    <td>The schedule for an eligible role assignment that is referenced through the targetScheduleId property. Supports $expand and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="targetScheduleId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the schedule object that's linked to the assignment request. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="ticketInfo" /></td>
    <td><code></code></td>
    <td>Ticket details linked to the role assignment request including details of the ticket number and ticket system.</td>
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
    <td><a href="#parameter-unified_role_assignment_schedule_request_id"><code>unified_role_assignment_schedule_request_id</code></a></td>
    <td></td>
    <td>Requests for active role assignments to principals through PIM.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Requests for active role assignments to principals through PIM.</td>
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
    <td><a href="#parameter-unified_role_assignment_schedule_request_id"><code>unified_role_assignment_schedule_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_role_assignment_schedule_request_id"><code>unified_role_assignment_schedule_request_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-unified_role_assignment_schedule_request_id"><code>unified_role_assignment_schedule_request_id</code></a></td>
    <td></td>
    <td>Immediately cancel a unifiedRoleAssignmentScheduleRequest object that is in a Granted status, and have the system automatically delete the canceled request after 30 days. After calling this action, the status of the canceled unifiedRoleAssignmentScheduleRequest changes to Canceled.</td>
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
<tr id="parameter-unified_role_assignment_schedule_request_id">
    <td><CopyableCode code="unified_role_assignment_schedule_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleAssignmentScheduleRequest</td>
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

Requests for active role assignments to principals through PIM.

```sql
SELECT
id,
action,
activatedUsing,
appScope,
appScopeId,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
directoryScope,
directoryScopeId,
isValidationOnly,
justification,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status,
targetSchedule,
targetScheduleId,
ticketInfo
FROM entra_id.role_management.entitlement_management_role_assignment_schedule_requests
WHERE unified_role_assignment_schedule_request_id = '{{ unified_role_assignment_schedule_request_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Requests for active role assignments to principals through PIM.

```sql
SELECT
id,
action,
activatedUsing,
appScope,
appScopeId,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
directoryScope,
directoryScopeId,
isValidationOnly,
justification,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status,
targetSchedule,
targetScheduleId,
ticketInfo
FROM entra_id.role_management.entitlement_management_role_assignment_schedule_requests
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
INSERT INTO entra_id.role_management.entitlement_management_role_assignment_schedule_requests (
id,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
status,
action,
appScopeId,
directoryScopeId,
isValidationOnly,
justification,
principalId,
roleDefinitionId,
scheduleInfo,
targetScheduleId,
ticketInfo,
activatedUsing,
appScope,
directoryScope,
principal,
roleDefinition,
targetSchedule
)
SELECT 
'{{ id }}',
'{{ approvalId }}',
'{{ completedDateTime }}',
'{{ createdBy }}',
'{{ createdDateTime }}',
'{{ customData }}',
'{{ status }}',
'{{ action }}',
'{{ appScopeId }}',
'{{ directoryScopeId }}',
{{ isValidationOnly }},
'{{ justification }}',
'{{ principalId }}',
'{{ roleDefinitionId }}',
'{{ scheduleInfo }}',
'{{ targetScheduleId }}',
'{{ ticketInfo }}',
'{{ activatedUsing }}',
'{{ appScope }}',
'{{ directoryScope }}',
'{{ principal }}',
'{{ roleDefinition }}',
'{{ targetSchedule }}'
RETURNING
id,
action,
activatedUsing,
appScope,
appScopeId,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
directoryScope,
directoryScopeId,
isValidationOnly,
justification,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status,
targetSchedule,
targetScheduleId,
ticketInfo
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_role_assignment_schedule_requests
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: approvalId
      value: "{{ approvalId }}"
      description: |
        The identifier of the approval of the request.
    - name: completedDateTime
      value: "{{ completedDateTime }}"
      description: |
        The request completion date time.
    - name: createdBy
      value: "{{ createdBy }}"
      description: |
        The principal that created the request.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The request creation date time.
    - name: customData
      value: "{{ customData }}"
      description: |
        Free text field to define any custom data for the request. Not used.
    - name: status
      value: "{{ status }}"
      description: |
        The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.
    - name: action
      value: "{{ action }}"
      description: |
        Represents the type of the operation on the role assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew, selfExtend, selfRenew, unknownFutureValue. adminAssign: For administrators to assign roles to principals.adminRemove: For administrators to remove principals from roles. adminUpdate: For administrators to change existing role assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.selfExtend: For principals to request to extend their expiring assignments.selfRenew: For principals to request to renew their expired assignments.
    - name: appScopeId
      value: "{{ appScopeId }}"
      description: |
        Identifier of the app-specific scope when the assignment is scoped to an app. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units. Supports $filter (eq, ne, and on null values).
    - name: directoryScopeId
      value: "{{ directoryScopeId }}"
      description: |
        Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only. Supports $filter (eq, ne, and on null values).
    - name: isValidationOnly
      value: {{ isValidationOnly }}
      description: |
        Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.
    - name: justification
      value: "{{ justification }}"
      description: |
        A message provided by users and administrators when create they create the unifiedRoleAssignmentScheduleRequest object.
    - name: principalId
      value: "{{ principalId }}"
      description: |
        Identifier of the principal that has been granted the assignment. Can be a user, role-assignable group, or a service principal. Supports $filter (eq, ne).
    - name: roleDefinitionId
      value: "{{ roleDefinitionId }}"
      description: |
        Identifier of the unifiedRoleDefinition object that is being assigned to the principal. Supports $filter (eq, ne).
    - name: scheduleInfo
      value: "{{ scheduleInfo }}"
      description: |
        The period of the role assignment. Recurring schedules are currently unsupported.
    - name: targetScheduleId
      value: "{{ targetScheduleId }}"
      description: |
        Identifier of the schedule object that's linked to the assignment request. Supports $filter (eq, ne).
    - name: ticketInfo
      value: "{{ ticketInfo }}"
      description: |
        Ticket details linked to the role assignment request including details of the ticket number and ticket system.
    - name: activatedUsing
      value: "{{ activatedUsing }}"
      description: |
        If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.
    - name: appScope
      value: "{{ appScope }}"
      description: |
        Read-only property with details of the app-specific scope when the assignment is scoped to an app. Nullable. Supports $expand.
    - name: directoryScope
      value: "{{ directoryScope }}"
      description: |
        The directory object that is the scope of the assignment. Read-only. Supports $expand.
    - name: principal
      value: "{{ principal }}"
      description: |
        The principal that's getting a role assignment through the request. Supports $expand and $select nested in $expand for id only.
    - name: roleDefinition
      value: "{{ roleDefinition }}"
      description: |
        Detailed information for the unifiedRoleDefinition object that is referenced through the roleDefinitionId property. Supports $expand and $select nested in $expand.
    - name: targetSchedule
      value: "{{ targetSchedule }}"
      description: |
        The schedule for an eligible role assignment that is referenced through the targetScheduleId property. Supports $expand and $select nested in $expand.
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
UPDATE entra_id.role_management.entitlement_management_role_assignment_schedule_requests
SET 
id = '{{ id }}',
approvalId = '{{ approvalId }}',
completedDateTime = '{{ completedDateTime }}',
createdBy = '{{ createdBy }}',
createdDateTime = '{{ createdDateTime }}',
customData = '{{ customData }}',
status = '{{ status }}',
action = '{{ action }}',
appScopeId = '{{ appScopeId }}',
directoryScopeId = '{{ directoryScopeId }}',
isValidationOnly = {{ isValidationOnly }},
justification = '{{ justification }}',
principalId = '{{ principalId }}',
roleDefinitionId = '{{ roleDefinitionId }}',
scheduleInfo = '{{ scheduleInfo }}',
targetScheduleId = '{{ targetScheduleId }}',
ticketInfo = '{{ ticketInfo }}',
activatedUsing = '{{ activatedUsing }}',
appScope = '{{ appScope }}',
directoryScope = '{{ directoryScope }}',
principal = '{{ principal }}',
roleDefinition = '{{ roleDefinition }}',
targetSchedule = '{{ targetSchedule }}'
WHERE 
unified_role_assignment_schedule_request_id = '{{ unified_role_assignment_schedule_request_id }}' --required
RETURNING
id,
action,
activatedUsing,
appScope,
appScopeId,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
directoryScope,
directoryScopeId,
isValidationOnly,
justification,
principal,
principalId,
roleDefinition,
roleDefinitionId,
scheduleInfo,
status,
targetSchedule,
targetScheduleId,
ticketInfo;
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
DELETE FROM entra_id.role_management.entitlement_management_role_assignment_schedule_requests
WHERE unified_role_assignment_schedule_request_id = '{{ unified_role_assignment_schedule_request_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Immediately cancel a unifiedRoleAssignmentScheduleRequest object that is in a Granted status, and have the system automatically delete the canceled request after 30 days. After calling this action, the status of the canceled unifiedRoleAssignmentScheduleRequest changes to Canceled.

```sql
EXEC entra_id.role_management.entitlement_management_role_assignment_schedule_requests.cancel 
@unified_role_assignment_schedule_request_id='{{ unified_role_assignment_schedule_request_id }}' --required
;
```
</TabItem>
</Tabs>
