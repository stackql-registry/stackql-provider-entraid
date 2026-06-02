--- 
title: directory_role_eligibility_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_role_eligibility_schedules
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

Creates, updates, deletes, gets or lists a <code>directory_role_eligibility_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="directory_role_eligibility_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.directory_role_eligibility_schedules" /></td></tr>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was created. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td>How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td>The period of the role eligibility.</td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was created. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td>How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the schedule was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
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
    <td>The period of the role eligibility.</td>
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
    <td><a href="#parameter-unifiedRoleEligibilitySchedule-id"><code>unifiedRoleEligibilitySchedule-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the schedule for a role eligibility operation.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the unifiedRoleEligibilitySchedule resources from the roleEligibilitySchedules navigation property.</td>
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
    <td><a href="#parameter-unifiedRoleEligibilitySchedule-id"><code>unifiedRoleEligibilitySchedule-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unifiedRoleEligibilitySchedule-id"><code>unifiedRoleEligibilitySchedule-id</code></a></td>
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
<tr id="parameter-unifiedRoleEligibilitySchedule-id">
    <td><CopyableCode code="unifiedRoleEligibilitySchedule-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleEligibilitySchedule</td>
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

Retrieve the schedule for a role eligibility operation.

```sql
SELECT
id,
@odata.type,
appScope,
appScopeId,
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
FROM entra_id.role_management.directory_role_eligibility_schedules
WHERE unifiedRoleEligibilitySchedule-id = '{{ unifiedRoleEligibilitySchedule-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get the unifiedRoleEligibilitySchedule resources from the roleEligibilitySchedules navigation property.

```sql
SELECT
id,
@odata.type,
appScope,
appScopeId,
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
FROM entra_id.role_management.directory_role_eligibility_schedules
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
INSERT INTO entra_id.role_management.directory_role_eligibility_schedules (
id,
@odata.type,
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
memberType,
scheduleInfo
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
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
'{{ memberType }}',
'{{ scheduleInfo }}'
RETURNING
id,
@odata.type,
appScope,
appScopeId,
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
- name: directory_role_eligibility_schedules
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
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
    - name: memberType
      value: "{{ memberType }}"
      description: |
        How the role eligibility is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleEligibilitySchedule can be managed by the caller. Supports $filter (eq, ne).
    - name: scheduleInfo
      value: "{{ scheduleInfo }}"
      description: |
        The period of the role eligibility.
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
UPDATE entra_id.role_management.directory_role_eligibility_schedules
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
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
memberType = '{{ memberType }}',
scheduleInfo = '{{ scheduleInfo }}'
WHERE 
unifiedRoleEligibilitySchedule-id = '{{ unifiedRoleEligibilitySchedule-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
appScope,
appScopeId,
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
DELETE FROM entra_id.role_management.directory_role_eligibility_schedules
WHERE unifiedRoleEligibilitySchedule-id = '{{ unifiedRoleEligibilitySchedule-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
