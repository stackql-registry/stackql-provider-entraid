--- 
title: entitlement_management_role_assignment_schedule_instances_filter_by_current_user
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_role_assignment_schedule_instances_filter_by_current_user
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_role_assignment_schedule_instances_filter_by_current_user</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_role_assignment_schedule_instances_filter_by_current_user" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.entitlement_management_role_assignment_schedule_instances_filter_by_current_user" /></td></tr>
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
    <td><a href="#parameter-on"><code>on</code></a></td>
    <td></td>
    <td>Get the instances of active role assignments for the calling principal.</td>
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
<tr id="parameter-on">
    <td><CopyableCode code="on" /></td>
    <td><code>string</code></td>
    <td>Usage: on='&#123;on&#125;'</td>
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

Get the instances of active role assignments for the calling principal.

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
FROM entra_id.role_management.entitlement_management_role_assignment_schedule_instances_filter_by_current_user
WHERE on = '{{ on }}' -- required
;
```
</TabItem>
</Tabs>
