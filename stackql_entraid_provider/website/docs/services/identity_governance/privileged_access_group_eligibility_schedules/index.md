--- 
title: privileged_access_group_eligibility_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - privileged_access_group_eligibility_schedules
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

Creates, updates, deletes, gets or lists a <code>privileged_access_group_eligibility_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="privileged_access_group_eligibility_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.privileged_access_group_eligibility_schedules" /></td></tr>
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
    <td>The identifier of the membership or ownership eligibility to the group that is governed by PIM. Required. The possible values are: owner, member. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was created. Optional. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdUsing" /></td>
    <td><code>string</code></td>
    <td>The identifier of the access assignment or eligibility request that created this schedule. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code></code></td>
    <td>References the group that is the scope of the membership or ownership eligibility through PIM for Groups. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the group representing the scope of the membership or ownership eligibility through PIM for Groups. Required. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code></code></td>
    <td>Indicates whether the assignment is derived from a group assignment. It can further imply whether the caller can manage the schedule. Required. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was last modified. Optional. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>References the principal that's in the scope of this membership or ownership eligibility request to the group that's governed by PIM. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the principal whose membership or ownership eligibility is granted through PIM for Groups. Required. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>Represents the period of the access assignment or eligibility. The scheduleInfo can represent a single occurrence or multiple recurring instances. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the access assignment or eligibility request. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable. Optional.</td>
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
    <td>The identifier of the membership or ownership eligibility to the group that is governed by PIM. Required. The possible values are: owner, member. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was created. Optional. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdUsing" /></td>
    <td><code>string</code></td>
    <td>The identifier of the access assignment or eligibility request that created this schedule. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code></code></td>
    <td>References the group that is the scope of the membership or ownership eligibility through PIM for Groups. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the group representing the scope of the membership or ownership eligibility through PIM for Groups. Required. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code></code></td>
    <td>Indicates whether the assignment is derived from a group assignment. It can further imply whether the caller can manage the schedule. Required. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was last modified. Optional. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>References the principal that's in the scope of this membership or ownership eligibility request to the group that's governed by PIM. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the principal whose membership or ownership eligibility is granted through PIM for Groups. Required. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code></code></td>
    <td>Represents the period of the access assignment or eligibility. The scheduleInfo can represent a single occurrence or multiple recurring instances. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the access assignment or eligibility request. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable. Optional.</td>
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
    <td><a href="#parameter-privileged_access_group_eligibility_schedule_id"><code>privileged_access_group_eligibility_schedule_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a privilegedAccessGroupEligibilitySchedule object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the privilegedAccessGroupEligibilitySchedule objects and their properties.</td>
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
    <td><a href="#parameter-privileged_access_group_eligibility_schedule_id"><code>privileged_access_group_eligibility_schedule_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-privileged_access_group_eligibility_schedule_id"><code>privileged_access_group_eligibility_schedule_id</code></a></td>
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
<tr id="parameter-privileged_access_group_eligibility_schedule_id">
    <td><CopyableCode code="privileged_access_group_eligibility_schedule_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of privilegedAccessGroupEligibilitySchedule</td>
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

Read the properties and relationships of a privilegedAccessGroupEligibilitySchedule object.

```sql
SELECT
id,
accessId,
createdDateTime,
createdUsing,
group,
groupId,
memberType,
modifiedDateTime,
principal,
principalId,
scheduleInfo,
status
FROM entra_id.identity_governance.privileged_access_group_eligibility_schedules
WHERE privileged_access_group_eligibility_schedule_id = '{{ privileged_access_group_eligibility_schedule_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the privilegedAccessGroupEligibilitySchedule objects and their properties.

```sql
SELECT
id,
accessId,
createdDateTime,
createdUsing,
group,
groupId,
memberType,
modifiedDateTime,
principal,
principalId,
scheduleInfo,
status
FROM entra_id.identity_governance.privileged_access_group_eligibility_schedules
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
INSERT INTO entra_id.identity_governance.privileged_access_group_eligibility_schedules (
id,
createdDateTime,
createdUsing,
modifiedDateTime,
scheduleInfo,
status,
accessId,
groupId,
memberType,
principalId,
group,
principal
)
SELECT 
'{{ id }}',
'{{ createdDateTime }}',
'{{ createdUsing }}',
'{{ modifiedDateTime }}',
'{{ scheduleInfo }}',
'{{ status }}',
'{{ accessId }}',
'{{ groupId }}',
'{{ memberType }}',
'{{ principalId }}',
'{{ group }}',
'{{ principal }}'
RETURNING
id,
accessId,
createdDateTime,
createdUsing,
group,
groupId,
memberType,
modifiedDateTime,
principal,
principalId,
scheduleInfo,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: privileged_access_group_eligibility_schedules
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        When the schedule was created. Optional.
    - name: createdUsing
      value: "{{ createdUsing }}"
      description: |
        The identifier of the access assignment or eligibility request that created this schedule. Optional.
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        When the schedule was last modified. Optional.
    - name: scheduleInfo
      value: "{{ scheduleInfo }}"
      description: |
        Represents the period of the access assignment or eligibility. The scheduleInfo can represent a single occurrence or multiple recurring instances. Required.
    - name: status
      value: "{{ status }}"
      description: |
        The status of the access assignment or eligibility request. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable. Optional.
    - name: accessId
      value: "{{ accessId }}"
      description: |
        The identifier of the membership or ownership eligibility to the group that is governed by PIM. Required. The possible values are: owner, member. Supports $filter (eq).
    - name: groupId
      value: "{{ groupId }}"
      description: |
        The identifier of the group representing the scope of the membership or ownership eligibility through PIM for Groups. Required. Supports $filter (eq).
    - name: memberType
      value: "{{ memberType }}"
      description: |
        Indicates whether the assignment is derived from a group assignment. It can further imply whether the caller can manage the schedule. Required. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq).
    - name: principalId
      value: "{{ principalId }}"
      description: |
        The identifier of the principal whose membership or ownership eligibility is granted through PIM for Groups. Required. Supports $filter (eq).
    - name: group
      value: "{{ group }}"
      description: |
        References the group that is the scope of the membership or ownership eligibility through PIM for Groups. Supports $expand.
    - name: principal
      value: "{{ principal }}"
      description: |
        References the principal that's in the scope of this membership or ownership eligibility request to the group that's governed by PIM. Supports $expand.
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
UPDATE entra_id.identity_governance.privileged_access_group_eligibility_schedules
SET 
id = '{{ id }}',
createdDateTime = '{{ createdDateTime }}',
createdUsing = '{{ createdUsing }}',
modifiedDateTime = '{{ modifiedDateTime }}',
scheduleInfo = '{{ scheduleInfo }}',
status = '{{ status }}',
accessId = '{{ accessId }}',
groupId = '{{ groupId }}',
memberType = '{{ memberType }}',
principalId = '{{ principalId }}',
group = '{{ group }}',
principal = '{{ principal }}'
WHERE 
privileged_access_group_eligibility_schedule_id = '{{ privileged_access_group_eligibility_schedule_id }}' --required
RETURNING
id,
accessId,
createdDateTime,
createdUsing,
group,
groupId,
memberType,
modifiedDateTime,
principal,
principalId,
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
DELETE FROM entra_id.identity_governance.privileged_access_group_eligibility_schedules
WHERE privileged_access_group_eligibility_schedule_id = '{{ privileged_access_group_eligibility_schedule_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
