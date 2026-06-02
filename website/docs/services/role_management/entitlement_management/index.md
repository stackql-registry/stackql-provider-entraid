--- 
title: entitlement_management
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management
  - role_management
  - entraid
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage entraid resources using SQL
custom_edit_url: null
image: /img/stackql-entraid-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>entitlement_management</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.role_management.entitlement_management" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resourceNamespaces" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignmentScheduleInstances" /></td>
    <td><code>array</code></td>
    <td>Instances for active role assignments.</td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignmentScheduleRequests" /></td>
    <td><code>array</code></td>
    <td>Requests for active role assignments to principals through PIM.</td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignmentSchedules" /></td>
    <td><code>array</code></td>
    <td>Schedules for active role assignment operations.</td>
</tr>
<tr>
    <td><CopyableCode code="roleAssignments" /></td>
    <td><code>array</code></td>
    <td>Resource to grant access to users or groups.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitions" /></td>
    <td><code>array</code></td>
    <td>Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.</td>
</tr>
<tr>
    <td><CopyableCode code="roleEligibilityScheduleInstances" /></td>
    <td><code>array</code></td>
    <td>Instances for role eligibility requests.</td>
</tr>
<tr>
    <td><CopyableCode code="roleEligibilityScheduleRequests" /></td>
    <td><code>array</code></td>
    <td>Requests for role eligibilities for principals through PIM.</td>
</tr>
<tr>
    <td><CopyableCode code="roleEligibilitySchedules" /></td>
    <td><code>array</code></td>
    <td>Schedules for role eligibility operations.</td>
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
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Container for roles and assignments for entitlement management resources.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Container for roles and assignments for entitlement management resources.

```sql
SELECT
id,
@odata.type,
resourceNamespaces,
roleAssignmentScheduleInstances,
roleAssignmentScheduleRequests,
roleAssignmentSchedules,
roleAssignments,
roleDefinitions,
roleEligibilityScheduleInstances,
roleEligibilityScheduleRequests,
roleEligibilitySchedules
FROM entraid.role_management.entitlement_management
WHERE $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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
UPDATE entraid.role_management.entitlement_management
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
resourceNamespaces = '{{ resourceNamespaces }}',
roleAssignments = '{{ roleAssignments }}',
roleAssignmentScheduleInstances = '{{ roleAssignmentScheduleInstances }}',
roleAssignmentScheduleRequests = '{{ roleAssignmentScheduleRequests }}',
roleAssignmentSchedules = '{{ roleAssignmentSchedules }}',
roleDefinitions = '{{ roleDefinitions }}',
roleEligibilityScheduleInstances = '{{ roleEligibilityScheduleInstances }}',
roleEligibilityScheduleRequests = '{{ roleEligibilityScheduleRequests }}',
roleEligibilitySchedules = '{{ roleEligibilitySchedules }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
resourceNamespaces,
roleAssignmentScheduleInstances,
roleAssignmentScheduleRequests,
roleAssignmentSchedules,
roleAssignments,
roleDefinitions,
roleEligibilityScheduleInstances,
roleEligibilityScheduleRequests,
roleEligibilitySchedules;
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
DELETE FROM entraid.role_management.entitlement_management
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
