--- 
title: privileged_access_group_eligibility_schedule_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - privileged_access_group_eligibility_schedule_requests
  - identity_governance
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

Creates, updates, deletes, gets or lists a <code>privileged_access_group_eligibility_schedule_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="privileged_access_group_eligibility_schedule_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.privileged_access_group_eligibility_schedule_requests" /></td></tr>
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
    <td><CopyableCode code="accessId" /></td>
    <td><code></code></td>
    <td>The identifier of membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code></code></td>
    <td>Represents the type of operation on the group membership or ownership assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew. adminAssign: For administrators to assign group membership or ownership to principals.adminRemove: For administrators to remove principals from group membership or ownership. adminUpdate: For administrators to change existing group membership or ownership assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.</td>
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
    <td><CopyableCode code="group" /></td>
    <td><code></code></td>
    <td>References the group that is the scope of the membership or ownership eligibility request through PIM for Groups. Supports $expand and $select nested in $expand for select properties like id, displayName, and mail.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the group representing the scope of the membership and ownership eligibility through PIM for Groups. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isValidationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>A message provided by users and administrators when create they create the privilegedAccessGroupAssignmentScheduleRequest object.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand and $select nested in $expand for id only.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for Groups. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>The period of the group membership or ownership assignment. Recurring schedules are currently unsupported.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSchedule" /></td>
    <td><code></code></td>
    <td>Schedule created by this request.</td>
</tr>
<tr>
    <td><CopyableCode code="targetScheduleId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the schedule that's created from the eligibility request. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="ticketInfo" /></td>
    <td><code></code></td>
    <td>Ticket details linked to the group membership or ownership assignment request including details of the ticket number and ticket system.</td>
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
    <td><CopyableCode code="accessId" /></td>
    <td><code></code></td>
    <td>The identifier of membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="action" /></td>
    <td><code></code></td>
    <td>Represents the type of operation on the group membership or ownership assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew. adminAssign: For administrators to assign group membership or ownership to principals.adminRemove: For administrators to remove principals from group membership or ownership. adminUpdate: For administrators to change existing group membership or ownership assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.</td>
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
    <td><CopyableCode code="group" /></td>
    <td><code></code></td>
    <td>References the group that is the scope of the membership or ownership eligibility request through PIM for Groups. Supports $expand and $select nested in $expand for select properties like id, displayName, and mail.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the group representing the scope of the membership and ownership eligibility through PIM for Groups. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isValidationOnly" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>A message provided by users and administrators when create they create the privilegedAccessGroupAssignmentScheduleRequest object.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand and $select nested in $expand for id only.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for Groups. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>The period of the group membership or ownership assignment. Recurring schedules are currently unsupported.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSchedule" /></td>
    <td><code></code></td>
    <td>Schedule created by this request.</td>
</tr>
<tr>
    <td><CopyableCode code="targetScheduleId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the schedule that's created from the eligibility request. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="ticketInfo" /></td>
    <td><code></code></td>
    <td>Ticket details linked to the group membership or ownership assignment request including details of the ticket number and ticket system.</td>
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
    <td><a href="#parameter-privileged_access_group_eligibility_schedule_request_id"><code>privileged_access_group_eligibility_schedule_request_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a privilegedAccessGroupEligibilityScheduleRequest object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the privilegedAccessGroupEligibilityScheduleRequest objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new privilegedAccessGroupEligibilityScheduleRequest object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-privileged_access_group_eligibility_schedule_request_id"><code>privileged_access_group_eligibility_schedule_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-privileged_access_group_eligibility_schedule_request_id"><code>privileged_access_group_eligibility_schedule_request_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-privileged_access_group_eligibility_schedule_request_id"><code>privileged_access_group_eligibility_schedule_request_id</code></a></td>
    <td></td>
    <td>Cancel an eligibility assignment request to a group whose membership and ownership are governed by PIM.</td>
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
<tr id="parameter-privileged_access_group_eligibility_schedule_request_id">
    <td><CopyableCode code="privileged_access_group_eligibility_schedule_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of privilegedAccessGroupEligibilityScheduleRequest</td>
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

Read the properties and relationships of a privilegedAccessGroupEligibilityScheduleRequest object.

```sql
SELECT
id,
accessId,
action,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
group,
groupId,
isValidationOnly,
justification,
principal,
principalId,
scheduleInfo,
status,
targetSchedule,
targetScheduleId,
ticketInfo
FROM entra_id.identity_governance.privileged_access_group_eligibility_schedule_requests
WHERE privileged_access_group_eligibility_schedule_request_id = '{{ privileged_access_group_eligibility_schedule_request_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the privilegedAccessGroupEligibilityScheduleRequest objects and their properties.

```sql
SELECT
id,
accessId,
action,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
group,
groupId,
isValidationOnly,
justification,
principal,
principalId,
scheduleInfo,
status,
targetSchedule,
targetScheduleId,
ticketInfo
FROM entra_id.identity_governance.privileged_access_group_eligibility_schedule_requests
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

Create a new privilegedAccessGroupEligibilityScheduleRequest object.

```sql
INSERT INTO entra_id.identity_governance.privileged_access_group_eligibility_schedule_requests (
id,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
status,
action,
isValidationOnly,
justification,
scheduleInfo,
ticketInfo,
accessId,
groupId,
principalId,
targetScheduleId,
group,
principal,
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
{{ isValidationOnly }},
'{{ justification }}',
'{{ scheduleInfo }}',
'{{ ticketInfo }}',
'{{ accessId }}',
'{{ groupId }}',
'{{ principalId }}',
'{{ targetScheduleId }}',
'{{ group }}',
'{{ principal }}',
'{{ targetSchedule }}'
RETURNING
id,
accessId,
action,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
group,
groupId,
isValidationOnly,
justification,
principal,
principalId,
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
- name: privileged_access_group_eligibility_schedule_requests
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
        Represents the type of operation on the group membership or ownership assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew. adminAssign: For administrators to assign group membership or ownership to principals.adminRemove: For administrators to remove principals from group membership or ownership. adminUpdate: For administrators to change existing group membership or ownership assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.
    - name: isValidationOnly
      value: {{ isValidationOnly }}
      description: |
        Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.
    - name: justification
      value: "{{ justification }}"
      description: |
        A message provided by users and administrators when create they create the privilegedAccessGroupAssignmentScheduleRequest object.
    - name: scheduleInfo
      value: "{{ scheduleInfo }}"
      description: |
        The period of the group membership or ownership assignment. Recurring schedules are currently unsupported.
    - name: ticketInfo
      value: "{{ ticketInfo }}"
      description: |
        Ticket details linked to the group membership or ownership assignment request including details of the ticket number and ticket system.
    - name: accessId
      value: "{{ accessId }}"
      description: |
        The identifier of membership or ownership eligibility relationship to the group. Required. The possible values are: owner, member, unknownFutureValue.
    - name: groupId
      value: "{{ groupId }}"
      description: |
        The identifier of the group representing the scope of the membership and ownership eligibility through PIM for Groups. Required.
    - name: principalId
      value: "{{ principalId }}"
      description: |
        The identifier of the principal whose membership or ownership eligibility to the group is managed through PIM for Groups. Required.
    - name: targetScheduleId
      value: "{{ targetScheduleId }}"
      description: |
        The identifier of the schedule that's created from the eligibility request. Optional.
    - name: group
      value: "{{ group }}"
      description: |
        References the group that is the scope of the membership or ownership eligibility request through PIM for Groups. Supports $expand and $select nested in $expand for select properties like id, displayName, and mail.
    - name: principal
      value: "{{ principal }}"
      description: |
        References the principal that's in the scope of the membership or ownership eligibility request through the group that's governed by PIM. Supports $expand and $select nested in $expand for id only.
    - name: targetSchedule
      value: "{{ targetSchedule }}"
      description: |
        Schedule created by this request.
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
UPDATE entra_id.identity_governance.privileged_access_group_eligibility_schedule_requests
SET 
id = '{{ id }}',
approvalId = '{{ approvalId }}',
completedDateTime = '{{ completedDateTime }}',
createdBy = '{{ createdBy }}',
createdDateTime = '{{ createdDateTime }}',
customData = '{{ customData }}',
status = '{{ status }}',
action = '{{ action }}',
isValidationOnly = {{ isValidationOnly }},
justification = '{{ justification }}',
scheduleInfo = '{{ scheduleInfo }}',
ticketInfo = '{{ ticketInfo }}',
accessId = '{{ accessId }}',
groupId = '{{ groupId }}',
principalId = '{{ principalId }}',
targetScheduleId = '{{ targetScheduleId }}',
group = '{{ group }}',
principal = '{{ principal }}',
targetSchedule = '{{ targetSchedule }}'
WHERE 
privileged_access_group_eligibility_schedule_request_id = '{{ privileged_access_group_eligibility_schedule_request_id }}' --required
RETURNING
id,
accessId,
action,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
group,
groupId,
isValidationOnly,
justification,
principal,
principalId,
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
DELETE FROM entra_id.identity_governance.privileged_access_group_eligibility_schedule_requests
WHERE privileged_access_group_eligibility_schedule_request_id = '{{ privileged_access_group_eligibility_schedule_request_id }}' --required
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

Cancel an eligibility assignment request to a group whose membership and ownership are governed by PIM.

```sql
EXEC entra_id.identity_governance.privileged_access_group_eligibility_schedule_requests.cancel 
@privileged_access_group_eligibility_schedule_request_id='{{ privileged_access_group_eligibility_schedule_request_id }}' --required
;
```
</TabItem>
</Tabs>
