--- 
title: privileged_access_group_assignment_schedule_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - privileged_access_group_assignment_schedule_instances
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

Creates, updates, deletes, gets or lists a <code>privileged_access_group_assignment_schedule_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="privileged_access_group_assignment_schedule_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.privileged_access_group_assignment_schedule_instances" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="accessId" /></td>
    <td><code></code></td>
    <td>The identifier of the membership or ownership assignment relationship to the group. Required. The possible values are: owner, member,  unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="activatedUsing" /></td>
    <td><code></code></td>
    <td>When the request activates a membership or ownership in PIM for Groups, this object represents the eligibility request for the group. Otherwise, it is null.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentScheduleId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the privilegedAccessGroupAssignmentSchedule from which this instance was created. Required. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentType" /></td>
    <td><code></code></td>
    <td>Indicates whether the membership or ownership assignment is granted through activation of an eligibility or through direct assignment. Required. The possible values are: assigned, activated, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule instance ends. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code></code></td>
    <td>References the group that is the scope of the membership or ownership assignment through PIM for Groups. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the group representing the scope of the membership or ownership assignment through PIM for Groups. Optional. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code></code></td>
    <td>Indicates whether the assignment is derived from a group assignment. It can further imply whether the caller can manage the assignment schedule. Required. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>References the principal that's in the scope of the membership or ownership assignment request through the group that's governed by PIM. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the principal whose membership or ownership assignment to the group is managed through PIM for Groups. Required. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When this instance starts. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="accessId" /></td>
    <td><code></code></td>
    <td>The identifier of the membership or ownership assignment relationship to the group. Required. The possible values are: owner, member,  unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="activatedUsing" /></td>
    <td><code></code></td>
    <td>When the request activates a membership or ownership in PIM for Groups, this object represents the eligibility request for the group. Otherwise, it is null.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentScheduleId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the privilegedAccessGroupAssignmentSchedule from which this instance was created. Required. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentType" /></td>
    <td><code></code></td>
    <td>Indicates whether the membership or ownership assignment is granted through activation of an eligibility or through direct assignment. Required. The possible values are: assigned, activated, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule instance ends. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code></code></td>
    <td>References the group that is the scope of the membership or ownership assignment through PIM for Groups. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="groupId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the group representing the scope of the membership or ownership assignment through PIM for Groups. Optional. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="memberType" /></td>
    <td><code></code></td>
    <td>Indicates whether the assignment is derived from a group assignment. It can further imply whether the caller can manage the assignment schedule. Required. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>References the principal that's in the scope of the membership or ownership assignment request through the group that's governed by PIM. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the principal whose membership or ownership assignment to the group is managed through PIM for Groups. Required. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When this instance starts. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td><a href="#parameter-privilegedAccessGroupAssignmentScheduleInstance-id"><code>privilegedAccessGroupAssignmentScheduleInstance-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of a privilegedAccessGroupAssignmentScheduleInstance object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of the privilegedAccessGroupAssignmentScheduleInstance objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-privilegedAccessGroupAssignmentScheduleInstance-id"><code>privilegedAccessGroupAssignmentScheduleInstance-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-privilegedAccessGroupAssignmentScheduleInstance-id"><code>privilegedAccessGroupAssignmentScheduleInstance-id</code></a></td>
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
<tr id="parameter-privilegedAccessGroupAssignmentScheduleInstance-id">
    <td><CopyableCode code="privilegedAccessGroupAssignmentScheduleInstance-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of privilegedAccessGroupAssignmentScheduleInstance</td>
</tr>
<tr id="parameter-$count">
    <td><CopyableCode code="$count" /></td>
    <td><code>boolean</code></td>
    <td>Include count of items</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter items by property values</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>array</code></td>
    <td>Order items by property values</td>
</tr>
<tr id="parameter-$search">
    <td><CopyableCode code="$search" /></td>
    <td><code>string</code></td>
    <td>Search items by search phrases</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Skip the first n items</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Show only the first n items (example: 50)</td>
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

Read the properties and relationships of a privilegedAccessGroupAssignmentScheduleInstance object.

```sql
SELECT
id,
@odata.type,
accessId,
activatedUsing,
assignmentScheduleId,
assignmentType,
endDateTime,
group,
groupId,
memberType,
principal,
principalId,
startDateTime
FROM entra_id.identity_governance.privileged_access_group_assignment_schedule_instances
WHERE privilegedAccessGroupAssignmentScheduleInstance-id = '{{ privilegedAccessGroupAssignmentScheduleInstance-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of the privilegedAccessGroupAssignmentScheduleInstance objects and their properties.

```sql
SELECT
id,
@odata.type,
accessId,
activatedUsing,
assignmentScheduleId,
assignmentType,
endDateTime,
group,
groupId,
memberType,
principal,
principalId,
startDateTime
FROM entra_id.identity_governance.privileged_access_group_assignment_schedule_instances
WHERE $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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
INSERT INTO entra_id.identity_governance.privileged_access_group_assignment_schedule_instances (
id,
@odata.type,
endDateTime,
startDateTime,
accessId,
assignmentScheduleId,
assignmentType,
groupId,
memberType,
principalId,
activatedUsing,
group,
principal
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ endDateTime }}',
'{{ startDateTime }}',
'{{ accessId }}',
'{{ assignmentScheduleId }}',
'{{ assignmentType }}',
'{{ groupId }}',
'{{ memberType }}',
'{{ principalId }}',
'{{ activatedUsing }}',
'{{ group }}',
'{{ principal }}'
RETURNING
id,
@odata.type,
accessId,
activatedUsing,
assignmentScheduleId,
assignmentType,
endDateTime,
group,
groupId,
memberType,
principal,
principalId,
startDateTime
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: privileged_access_group_assignment_schedule_instances
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: endDateTime
      value: "{{ endDateTime }}"
      description: |
        When the schedule instance ends. Required.
    - name: startDateTime
      value: "{{ startDateTime }}"
      description: |
        When this instance starts. Required.
    - name: accessId
      value: "{{ accessId }}"
      description: |
        The identifier of the membership or ownership assignment relationship to the group. Required. The possible values are: owner, member,  unknownFutureValue. Supports $filter (eq).
    - name: assignmentScheduleId
      value: "{{ assignmentScheduleId }}"
      description: |
        The identifier of the privilegedAccessGroupAssignmentSchedule from which this instance was created. Required. Supports $filter (eq, ne).
    - name: assignmentType
      value: "{{ assignmentType }}"
      description: |
        Indicates whether the membership or ownership assignment is granted through activation of an eligibility or through direct assignment. Required. The possible values are: assigned, activated, unknownFutureValue. Supports $filter (eq).
    - name: groupId
      value: "{{ groupId }}"
      description: |
        The identifier of the group representing the scope of the membership or ownership assignment through PIM for Groups. Optional. Supports $filter (eq).
    - name: memberType
      value: "{{ memberType }}"
      description: |
        Indicates whether the assignment is derived from a group assignment. It can further imply whether the caller can manage the assignment schedule. Required. The possible values are: direct, group, unknownFutureValue. Supports $filter (eq).
    - name: principalId
      value: "{{ principalId }}"
      description: |
        The identifier of the principal whose membership or ownership assignment to the group is managed through PIM for Groups. Required. Supports $filter (eq).
    - name: activatedUsing
      value: "{{ activatedUsing }}"
      description: |
        When the request activates a membership or ownership in PIM for Groups, this object represents the eligibility request for the group. Otherwise, it is null.
    - name: group
      value: "{{ group }}"
      description: |
        References the group that is the scope of the membership or ownership assignment through PIM for Groups. Supports $expand.
    - name: principal
      value: "{{ principal }}"
      description: |
        References the principal that's in the scope of the membership or ownership assignment request through the group that's governed by PIM. Supports $expand.
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
UPDATE entra_id.identity_governance.privileged_access_group_assignment_schedule_instances
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
endDateTime = '{{ endDateTime }}',
startDateTime = '{{ startDateTime }}',
accessId = '{{ accessId }}',
assignmentScheduleId = '{{ assignmentScheduleId }}',
assignmentType = '{{ assignmentType }}',
groupId = '{{ groupId }}',
memberType = '{{ memberType }}',
principalId = '{{ principalId }}',
activatedUsing = '{{ activatedUsing }}',
group = '{{ group }}',
principal = '{{ principal }}'
WHERE 
privilegedAccessGroupAssignmentScheduleInstance-id = '{{ privilegedAccessGroupAssignmentScheduleInstance-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
accessId,
activatedUsing,
assignmentScheduleId,
assignmentType,
endDateTime,
group,
groupId,
memberType,
principal,
principalId,
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
DELETE FROM entra_id.identity_governance.privileged_access_group_assignment_schedule_instances
WHERE privilegedAccessGroupAssignmentScheduleInstance-id = '{{ privilegedAccessGroupAssignmentScheduleInstance-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
