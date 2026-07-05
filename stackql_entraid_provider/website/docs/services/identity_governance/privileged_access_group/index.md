--- 
title: privileged_access_group
hide_title: false
hide_table_of_contents: false
keywords:
  - privileged_access_group
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

Creates, updates, deletes, gets or lists a <code>privileged_access_group</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="privileged_access_group" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.privileged_access_group" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="assignmentApprovals" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="assignmentScheduleInstances" /></td>
    <td><code>array</code></td>
    <td>The instances of assignment schedules to activate a just-in-time access.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentScheduleRequests" /></td>
    <td><code>array</code></td>
    <td>The schedule requests for operations to create, update, delete, extend, and renew an assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentSchedules" /></td>
    <td><code>array</code></td>
    <td>The assignment schedules to activate a just-in-time access.</td>
</tr>
<tr>
    <td><CopyableCode code="eligibilityScheduleInstances" /></td>
    <td><code>array</code></td>
    <td>The instances of eligibility schedules to activate a just-in-time access.</td>
</tr>
<tr>
    <td><CopyableCode code="eligibilityScheduleRequests" /></td>
    <td><code>array</code></td>
    <td>The schedule requests for operations to create, update, delete, extend, and renew an eligibility.</td>
</tr>
<tr>
    <td><CopyableCode code="eligibilitySchedules" /></td>
    <td><code>array</code></td>
    <td>The eligibility schedules to activate a just-in-time access.</td>
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
    <td></td>
    <td></td>
    <td>A group that's governed through Privileged Identity Management (PIM).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

A group that's governed through Privileged Identity Management (PIM).

```sql
SELECT
id,
assignmentApprovals,
assignmentScheduleInstances,
assignmentScheduleRequests,
assignmentSchedules,
eligibilityScheduleInstances,
eligibilityScheduleRequests,
eligibilitySchedules
FROM entra_id.identity_governance.privileged_access_group
;
```
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
UPDATE entra_id.identity_governance.privileged_access_group
SET 
id = '{{ id }}',
assignmentApprovals = '{{ assignmentApprovals }}',
assignmentScheduleInstances = '{{ assignmentScheduleInstances }}',
assignmentScheduleRequests = '{{ assignmentScheduleRequests }}',
assignmentSchedules = '{{ assignmentSchedules }}',
eligibilityScheduleInstances = '{{ eligibilityScheduleInstances }}',
eligibilityScheduleRequests = '{{ eligibilityScheduleRequests }}',
eligibilitySchedules = '{{ eligibilitySchedules }}'
RETURNING
id,
assignmentApprovals,
assignmentScheduleInstances,
assignmentScheduleRequests,
assignmentSchedules,
eligibilityScheduleInstances,
eligibilityScheduleRequests,
eligibilitySchedules;
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
DELETE FROM entra_id.identity_governance.privileged_access_group
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
