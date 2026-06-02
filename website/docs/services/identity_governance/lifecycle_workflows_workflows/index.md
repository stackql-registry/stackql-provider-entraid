--- 
title: lifecycle_workflows_workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_workflows
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_workflows" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_workflows" /></td></tr>
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
    <td>Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="administrationScopeTargets" /></td>
    <td><code>array</code></td>
    <td>The administrative units in the scope of the workflow. Optional. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td> (joiner, leaver, unknownFutureValue, mover) (title: lifecycleWorkflowCategory)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The user who created the workflow. (title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When a workflow was created. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A string that describes the purpose of the workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A string to identify the workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="executionConditions" /></td>
    <td><code>object</code></td>
    <td>Defines when and for who the workflow will run. (title: workflowExecutionConditions)</td>
</tr>
<tr>
    <td><CopyableCode code="executionScope" /></td>
    <td><code>array</code></td>
    <td>The list of users that meet the workflowExecutionConditions of a workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the workflow is enabled or disabled. If this setting is true, the workflow can be run on demand or on schedule when isSchedulingEnabled is true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSchedulingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, the Lifecycle Workflow engine executes the workflow based on the schedule defined by tenant settings. Can't be true for a disabled workflow (where isEnabled is false).</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>object</code></td>
    <td>The unique identifier of the Microsoft Entra identity that last modified the workflow. (title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the workflow was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="nextScheduleRunDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="runs" /></td>
    <td><code>array</code></td>
    <td>Workflow runs.</td>
</tr>
<tr>
    <td><CopyableCode code="taskReports" /></td>
    <td><code>array</code></td>
    <td>Represents the aggregation of task execution data for tasks within a workflow object.</td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>array</code></td>
    <td>The tasks in the workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="userProcessingResults" /></td>
    <td><code>array</code></td>
    <td>Per-user workflow execution results.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>number (int32)</code></td>
    <td>The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>The workflow versions that are available.</td>
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
    <td>Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="administrationScopeTargets" /></td>
    <td><code>array</code></td>
    <td>The administrative units in the scope of the workflow. Optional. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td> (joiner, leaver, unknownFutureValue, mover) (title: lifecycleWorkflowCategory)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The user who created the workflow. (title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When a workflow was created. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A string that describes the purpose of the workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A string to identify the workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="executionConditions" /></td>
    <td><code>object</code></td>
    <td>Defines when and for who the workflow will run. (title: workflowExecutionConditions)</td>
</tr>
<tr>
    <td><CopyableCode code="executionScope" /></td>
    <td><code>array</code></td>
    <td>The list of users that meet the workflowExecutionConditions of a workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether the workflow is enabled or disabled. If this setting is true, the workflow can be run on demand or on schedule when isSchedulingEnabled is true.</td>
</tr>
<tr>
    <td><CopyableCode code="isSchedulingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>If true, the Lifecycle Workflow engine executes the workflow based on the schedule defined by tenant settings. Can't be true for a disabled workflow (where isEnabled is false).</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>object</code></td>
    <td>The unique identifier of the Microsoft Entra identity that last modified the workflow. (title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the workflow was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="nextScheduleRunDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="runs" /></td>
    <td><code>array</code></td>
    <td>Workflow runs.</td>
</tr>
<tr>
    <td><CopyableCode code="taskReports" /></td>
    <td><code>array</code></td>
    <td>Represents the aggregation of task execution data for tasks within a workflow object.</td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>array</code></td>
    <td>The tasks in the workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="userProcessingResults" /></td>
    <td><code>array</code></td>
    <td>Per-user workflow execution results.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>number (int32)</code></td>
    <td>The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="versions" /></td>
    <td><code>array</code></td>
    <td>The workflow versions that are available.</td>
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
    <td><a href="#parameter-workflow-id"><code>workflow-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of a workflow object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of workflow resources that are associated with lifecycle workflows.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new workflow object. You can create up to 100 workflows in a tenant.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workflow-id"><code>workflow-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a workflow object. Only the properties listed in the request body table can be updated. To update any other workflow properties, see workflow: createNewVersion.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workflow-id"><code>workflow-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a workflow object and its associated tasks, taskProcessingResults and versions. You can restore a deleted workflow and its associated objects within 30 days of deletion.</td>
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
<tr id="parameter-workflow-id">
    <td><CopyableCode code="workflow-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of workflow</td>
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

Read the properties and relationships of a workflow object.

```sql
SELECT
id,
@odata.type,
administrationScopeTargets,
category,
createdBy,
createdDateTime,
deletedDateTime,
description,
displayName,
executionConditions,
executionScope,
isEnabled,
isSchedulingEnabled,
lastModifiedBy,
lastModifiedDateTime,
nextScheduleRunDateTime,
runs,
taskReports,
tasks,
userProcessingResults,
version,
versions
FROM entra_id.identity_governance.lifecycle_workflows_workflows
WHERE workflow-id = '{{ workflow-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of workflow resources that are associated with lifecycle workflows.

```sql
SELECT
id,
@odata.type,
administrationScopeTargets,
category,
createdBy,
createdDateTime,
deletedDateTime,
description,
displayName,
executionConditions,
executionScope,
isEnabled,
isSchedulingEnabled,
lastModifiedBy,
lastModifiedDateTime,
nextScheduleRunDateTime,
runs,
taskReports,
tasks,
userProcessingResults,
version,
versions
FROM entra_id.identity_governance.lifecycle_workflows_workflows
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

Create a new workflow object. You can create up to 100 workflows in a tenant.

```sql
INSERT INTO entra_id.identity_governance.lifecycle_workflows_workflows (
category,
createdDateTime,
description,
displayName,
executionConditions,
isEnabled,
isSchedulingEnabled,
lastModifiedDateTime,
administrationScopeTargets,
createdBy,
lastModifiedBy,
tasks,
@odata.type,
deletedDateTime,
id,
nextScheduleRunDateTime,
version,
executionScope,
runs,
taskReports,
userProcessingResults,
versions
)
SELECT 
'{{ category }}',
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ executionConditions }}',
{{ isEnabled }},
{{ isSchedulingEnabled }},
'{{ lastModifiedDateTime }}',
'{{ administrationScopeTargets }}',
'{{ createdBy }}',
'{{ lastModifiedBy }}',
'{{ tasks }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
'{{ id }}',
'{{ nextScheduleRunDateTime }}',
{{ version }},
'{{ executionScope }}',
'{{ runs }}',
'{{ taskReports }}',
'{{ userProcessingResults }}',
'{{ versions }}'
RETURNING
id,
@odata.type,
administrationScopeTargets,
category,
createdBy,
createdDateTime,
deletedDateTime,
description,
displayName,
executionConditions,
executionScope,
isEnabled,
isSchedulingEnabled,
lastModifiedBy,
lastModifiedDateTime,
nextScheduleRunDateTime,
runs,
taskReports,
tasks,
userProcessingResults,
version,
versions
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: lifecycle_workflows_workflows
  props:
    - name: category
      value: "{{ category }}"
      valid_values: ['joiner', 'leaver', 'unknownFutureValue', 'mover']
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        When a workflow was created.
    - name: description
      value: "{{ description }}"
      description: |
        A string that describes the purpose of the workflow.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        A string to identify the workflow.
    - name: executionConditions
      description: |
        Defines when and for who the workflow will run.
      value:
        @odata.type: "{{ @odata.type }}"
    - name: isEnabled
      value: {{ isEnabled }}
      description: |
        Whether the workflow is enabled or disabled. If this setting is true, the workflow can be run on demand or on schedule when isSchedulingEnabled is true.
    - name: isSchedulingEnabled
      value: {{ isSchedulingEnabled }}
      description: |
        If true, the Lifecycle Workflow engine executes the workflow based on the schedule defined by tenant settings. Can't be true for a disabled workflow (where isEnabled is false).
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        When the workflow was last modified.
    - name: administrationScopeTargets
      description: |
        The administrative units in the scope of the workflow. Optional. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: createdBy
      description: |
        The user who created the workflow.
      value:
        id: "{{ id }}"
        @odata.type: "{{ @odata.type }}"
        deletedDateTime: "{{ deletedDateTime }}"
        aboutMe: "{{ aboutMe }}"
        accountEnabled: {{ accountEnabled }}
        ageGroup: "{{ ageGroup }}"
        assignedLicenses:
          - disabledPlans: "{{ disabledPlans }}"
            skuId: "{{ skuId }}"
            @odata.type: "{{ @odata.type }}"
        assignedPlans:
          - assignedDateTime: "{{ assignedDateTime }}"
            capabilityStatus: "{{ capabilityStatus }}"
            service: "{{ service }}"
            servicePlanId: "{{ servicePlanId }}"
            @odata.type: "{{ @odata.type }}"
        authorizationInfo: "{{ authorizationInfo }}"
        birthday: "{{ birthday }}"
        businessPhones:
          - "{{ businessPhones }}"
        city: "{{ city }}"
        companyName: "{{ companyName }}"
        consentProvidedForMinor: "{{ consentProvidedForMinor }}"
        country: "{{ country }}"
        createdDateTime: "{{ createdDateTime }}"
        creationType: "{{ creationType }}"
        customSecurityAttributes: "{{ customSecurityAttributes }}"
        department: "{{ department }}"
        deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
        displayName: "{{ displayName }}"
        employeeHireDate: "{{ employeeHireDate }}"
        employeeId: "{{ employeeId }}"
        employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
        employeeOrgData: "{{ employeeOrgData }}"
        employeeType: "{{ employeeType }}"
        externalUserState: "{{ externalUserState }}"
        externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
        faxNumber: "{{ faxNumber }}"
        givenName: "{{ givenName }}"
        hireDate: "{{ hireDate }}"
        identities:
          - issuer: "{{ issuer }}"
            issuerAssignedId: "{{ issuerAssignedId }}"
            signInType: "{{ signInType }}"
            @odata.type: "{{ @odata.type }}"
        identityParentId: "{{ identityParentId }}"
        imAddresses:
          - "{{ imAddresses }}"
        interests:
          - "{{ interests }}"
        isManagementRestricted: {{ isManagementRestricted }}
        isResourceAccount: {{ isResourceAccount }}
        jobTitle: "{{ jobTitle }}"
        lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
        legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
        licenseAssignmentStates:
          - assignedByGroup: "{{ assignedByGroup }}"
            disabledPlans: "{{ disabledPlans }}"
            error: "{{ error }}"
            lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
            skuId: "{{ skuId }}"
            state: "{{ state }}"
            @odata.type: "{{ @odata.type }}"
        mail: "{{ mail }}"
        mailboxSettings: "{{ mailboxSettings }}"
        mailNickname: "{{ mailNickname }}"
        mobilePhone: "{{ mobilePhone }}"
        mySite: "{{ mySite }}"
        officeLocation: "{{ officeLocation }}"
        onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
        onPremisesDomainName: "{{ onPremisesDomainName }}"
        onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
        onPremisesImmutableId: "{{ onPremisesImmutableId }}"
        onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
        onPremisesProvisioningErrors:
          - category: "{{ category }}"
            occurredDateTime: "{{ occurredDateTime }}"
            propertyCausingError: "{{ propertyCausingError }}"
            value: "{{ value }}"
            @odata.type: "{{ @odata.type }}"
        onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
        onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
        onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
        onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
        otherMails:
          - "{{ otherMails }}"
        passwordPolicies: "{{ passwordPolicies }}"
        passwordProfile: "{{ passwordProfile }}"
        pastProjects:
          - "{{ pastProjects }}"
        postalCode: "{{ postalCode }}"
        preferredDataLocation: "{{ preferredDataLocation }}"
        preferredLanguage: "{{ preferredLanguage }}"
        preferredName: "{{ preferredName }}"
        print: "{{ print }}"
        provisionedPlans:
          - capabilityStatus: "{{ capabilityStatus }}"
            provisioningStatus: "{{ provisioningStatus }}"
            service: "{{ service }}"
            @odata.type: "{{ @odata.type }}"
        proxyAddresses:
          - "{{ proxyAddresses }}"
        responsibilities:
          - "{{ responsibilities }}"
        schools:
          - "{{ schools }}"
        securityIdentifier: "{{ securityIdentifier }}"
        serviceProvisioningErrors:
          - createdDateTime: "{{ createdDateTime }}"
            isResolved: {{ isResolved }}
            serviceInstance: "{{ serviceInstance }}"
            @odata.type: "{{ @odata.type }}"
        showInAddressList: {{ showInAddressList }}
        signInActivity: "{{ signInActivity }}"
        signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
        skills:
          - "{{ skills }}"
        state: "{{ state }}"
        streetAddress: "{{ streetAddress }}"
        surname: "{{ surname }}"
        usageLocation: "{{ usageLocation }}"
        userPrincipalName: "{{ userPrincipalName }}"
        userType: "{{ userType }}"
        activities:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            activationUrl: "{{ activationUrl }}"
            activitySourceHost: "{{ activitySourceHost }}"
            appActivityId: "{{ appActivityId }}"
            appDisplayName: "{{ appDisplayName }}"
            contentInfo: "{{ contentInfo }}"
            contentUrl: "{{ contentUrl }}"
            createdDateTime: "{{ createdDateTime }}"
            expirationDateTime: "{{ expirationDateTime }}"
            fallbackUrl: "{{ fallbackUrl }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            status: "{{ status }}"
            userTimezone: "{{ userTimezone }}"
            visualElements:
              attribution:
                addImageQuery: {{ addImageQuery }}
                alternateText: "{{ alternateText }}"
                alternativeText: "{{ alternativeText }}"
                iconUrl: "{{ iconUrl }}"
                @odata.type: "{{ @odata.type }}"
              backgroundColor: "{{ backgroundColor }}"
              content: "{{ content }}"
              description: "{{ description }}"
              displayText: "{{ displayText }}"
              @odata.type: "{{ @odata.type }}"
            historyItems: "{{ historyItems }}"
        adhocCalls:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            recordings: "{{ recordings }}"
            transcripts: "{{ transcripts }}"
        agreementAcceptances:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            agreementFileId: "{{ agreementFileId }}"
            agreementId: "{{ agreementId }}"
            deviceDisplayName: "{{ deviceDisplayName }}"
            deviceId: "{{ deviceId }}"
            deviceOSType: "{{ deviceOSType }}"
            deviceOSVersion: "{{ deviceOSVersion }}"
            expirationDateTime: "{{ expirationDateTime }}"
            recordedDateTime: "{{ recordedDateTime }}"
            state: "{{ state }}"
            userDisplayName: "{{ userDisplayName }}"
            userEmail: "{{ userEmail }}"
            userId: "{{ userId }}"
            userPrincipalName: "{{ userPrincipalName }}"
        appRoleAssignments:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            appRoleId: "{{ appRoleId }}"
            createdDateTime: "{{ createdDateTime }}"
            principalDisplayName: "{{ principalDisplayName }}"
            principalId: "{{ principalId }}"
            principalType: "{{ principalType }}"
            resourceDisplayName: "{{ resourceDisplayName }}"
            resourceId: "{{ resourceId }}"
        authentication: "{{ authentication }}"
        calendar: "{{ calendar }}"
        calendarGroups:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            changeKey: "{{ changeKey }}"
            classId: "{{ classId }}"
            name: "{{ name }}"
            calendars: "{{ calendars }}"
        calendars:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
            canEdit: {{ canEdit }}
            canShare: {{ canShare }}
            canViewPrivateItems: {{ canViewPrivateItems }}
            changeKey: "{{ changeKey }}"
            color: "{{ color }}"
            defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
            hexColor: "{{ hexColor }}"
            isDefaultCalendar: {{ isDefaultCalendar }}
            isRemovable: {{ isRemovable }}
            isTallyingResponses: {{ isTallyingResponses }}
            name: "{{ name }}"
            owner: "{{ owner }}"
            calendarPermissions: "{{ calendarPermissions }}"
            calendarView: "{{ calendarView }}"
            events: "{{ events }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        calendarView:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            allowNewTimeProposals: {{ allowNewTimeProposals }}
            attendees: "{{ attendees }}"
            body: "{{ body }}"
            bodyPreview: "{{ bodyPreview }}"
            cancelledOccurrences: "{{ cancelledOccurrences }}"
            end: "{{ end }}"
            hasAttachments: {{ hasAttachments }}
            hideAttendees: {{ hideAttendees }}
            iCalUId: "{{ iCalUId }}"
            importance: "{{ importance }}"
            isAllDay: {{ isAllDay }}
            isCancelled: {{ isCancelled }}
            isDraft: {{ isDraft }}
            isOnlineMeeting: {{ isOnlineMeeting }}
            isOrganizer: {{ isOrganizer }}
            isReminderOn: {{ isReminderOn }}
            location: "{{ location }}"
            locations: "{{ locations }}"
            onlineMeeting: "{{ onlineMeeting }}"
            onlineMeetingProvider: "{{ onlineMeetingProvider }}"
            onlineMeetingUrl: "{{ onlineMeetingUrl }}"
            organizer: "{{ organizer }}"
            originalEndTimeZone: "{{ originalEndTimeZone }}"
            originalStart: "{{ originalStart }}"
            originalStartTimeZone: "{{ originalStartTimeZone }}"
            recurrence: "{{ recurrence }}"
            reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
            responseRequested: {{ responseRequested }}
            responseStatus: "{{ responseStatus }}"
            sensitivity: "{{ sensitivity }}"
            seriesMasterId: "{{ seriesMasterId }}"
            showAs: "{{ showAs }}"
            start: "{{ start }}"
            subject: "{{ subject }}"
            transactionId: "{{ transactionId }}"
            type: "{{ type }}"
            webLink: "{{ webLink }}"
            attachments: "{{ attachments }}"
            calendar: "{{ calendar }}"
            exceptionOccurrences: "{{ exceptionOccurrences }}"
            extensions: "{{ extensions }}"
            instances: "{{ instances }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        chats:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            chatType: "{{ chatType }}"
            createdDateTime: "{{ createdDateTime }}"
            isHiddenForAllMembers: {{ isHiddenForAllMembers }}
            lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
            migrationMode: "{{ migrationMode }}"
            onlineMeetingInfo: "{{ onlineMeetingInfo }}"
            originalCreatedDateTime: "{{ originalCreatedDateTime }}"
            tenantId: "{{ tenantId }}"
            topic: "{{ topic }}"
            viewpoint: "{{ viewpoint }}"
            webUrl: "{{ webUrl }}"
            installedApps: "{{ installedApps }}"
            lastMessagePreview: "{{ lastMessagePreview }}"
            members: "{{ members }}"
            messages: "{{ messages }}"
            permissionGrants: "{{ permissionGrants }}"
            pinnedMessages: "{{ pinnedMessages }}"
            tabs: "{{ tabs }}"
        cloudClipboard: "{{ cloudClipboard }}"
        cloudPCs:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            aadDeviceId: "{{ aadDeviceId }}"
            displayName: "{{ displayName }}"
            gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
            imageDisplayName: "{{ imageDisplayName }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            managedDeviceId: "{{ managedDeviceId }}"
            managedDeviceName: "{{ managedDeviceName }}"
            onPremisesConnectionName: "{{ onPremisesConnectionName }}"
            provisioningPolicyId: "{{ provisioningPolicyId }}"
            provisioningPolicyName: "{{ provisioningPolicyName }}"
            provisioningType: "{{ provisioningType }}"
            servicePlanId: "{{ servicePlanId }}"
            servicePlanName: "{{ servicePlanName }}"
            userPrincipalName: "{{ userPrincipalName }}"
        contactFolders:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            displayName: "{{ displayName }}"
            parentFolderId: "{{ parentFolderId }}"
            childFolders: "{{ childFolders }}"
            contacts: "{{ contacts }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        contacts:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            assistantName: "{{ assistantName }}"
            birthday: "{{ birthday }}"
            businessAddress: "{{ businessAddress }}"
            businessHomePage: "{{ businessHomePage }}"
            businessPhones: "{{ businessPhones }}"
            children: "{{ children }}"
            companyName: "{{ companyName }}"
            department: "{{ department }}"
            displayName: "{{ displayName }}"
            emailAddresses: "{{ emailAddresses }}"
            fileAs: "{{ fileAs }}"
            generation: "{{ generation }}"
            givenName: "{{ givenName }}"
            homeAddress: "{{ homeAddress }}"
            homePhones: "{{ homePhones }}"
            imAddresses: "{{ imAddresses }}"
            initials: "{{ initials }}"
            jobTitle: "{{ jobTitle }}"
            manager: "{{ manager }}"
            middleName: "{{ middleName }}"
            mobilePhone: "{{ mobilePhone }}"
            nickName: "{{ nickName }}"
            officeLocation: "{{ officeLocation }}"
            otherAddress: "{{ otherAddress }}"
            parentFolderId: "{{ parentFolderId }}"
            personalNotes: "{{ personalNotes }}"
            primaryEmailAddress: "{{ primaryEmailAddress }}"
            profession: "{{ profession }}"
            secondaryEmailAddress: "{{ secondaryEmailAddress }}"
            spouseName: "{{ spouseName }}"
            surname: "{{ surname }}"
            tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
            title: "{{ title }}"
            yomiCompanyName: "{{ yomiCompanyName }}"
            yomiGivenName: "{{ yomiGivenName }}"
            yomiSurname: "{{ yomiSurname }}"
            extensions: "{{ extensions }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            photo: "{{ photo }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        createdObjects:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
        deviceManagementTroubleshootingEvents:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            correlationId: "{{ correlationId }}"
            eventDateTime: "{{ eventDateTime }}"
        directReports:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        drive: "{{ drive }}"
        drives:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            createdBy: "{{ createdBy }}"
            createdDateTime: "{{ createdDateTime }}"
            description: "{{ description }}"
            eTag: "{{ eTag }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            name: "{{ name }}"
            parentReference: "{{ parentReference }}"
            webUrl: "{{ webUrl }}"
            createdByUser: "{{ createdByUser }}"
            lastModifiedByUser: "{{ lastModifiedByUser }}"
            driveType: "{{ driveType }}"
            owner: "{{ owner }}"
            quota: "{{ quota }}"
            sharePointIds: "{{ sharePointIds }}"
            system: "{{ system }}"
            bundles: "{{ bundles }}"
            following: "{{ following }}"
            items: "{{ items }}"
            list: "{{ list }}"
            root: "{{ root }}"
            special: "{{ special }}"
        employeeExperience: "{{ employeeExperience }}"
        events:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            allowNewTimeProposals: {{ allowNewTimeProposals }}
            attendees: "{{ attendees }}"
            body: "{{ body }}"
            bodyPreview: "{{ bodyPreview }}"
            cancelledOccurrences: "{{ cancelledOccurrences }}"
            end: "{{ end }}"
            hasAttachments: {{ hasAttachments }}
            hideAttendees: {{ hideAttendees }}
            iCalUId: "{{ iCalUId }}"
            importance: "{{ importance }}"
            isAllDay: {{ isAllDay }}
            isCancelled: {{ isCancelled }}
            isDraft: {{ isDraft }}
            isOnlineMeeting: {{ isOnlineMeeting }}
            isOrganizer: {{ isOrganizer }}
            isReminderOn: {{ isReminderOn }}
            location: "{{ location }}"
            locations: "{{ locations }}"
            onlineMeeting: "{{ onlineMeeting }}"
            onlineMeetingProvider: "{{ onlineMeetingProvider }}"
            onlineMeetingUrl: "{{ onlineMeetingUrl }}"
            organizer: "{{ organizer }}"
            originalEndTimeZone: "{{ originalEndTimeZone }}"
            originalStart: "{{ originalStart }}"
            originalStartTimeZone: "{{ originalStartTimeZone }}"
            recurrence: "{{ recurrence }}"
            reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
            responseRequested: {{ responseRequested }}
            responseStatus: "{{ responseStatus }}"
            sensitivity: "{{ sensitivity }}"
            seriesMasterId: "{{ seriesMasterId }}"
            showAs: "{{ showAs }}"
            start: "{{ start }}"
            subject: "{{ subject }}"
            transactionId: "{{ transactionId }}"
            type: "{{ type }}"
            webLink: "{{ webLink }}"
            attachments: "{{ attachments }}"
            calendar: "{{ calendar }}"
            exceptionOccurrences: "{{ exceptionOccurrences }}"
            extensions: "{{ extensions }}"
            instances: "{{ instances }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        extensions:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
        followedSites:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            createdBy: "{{ createdBy }}"
            createdDateTime: "{{ createdDateTime }}"
            description: "{{ description }}"
            eTag: "{{ eTag }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            name: "{{ name }}"
            parentReference: "{{ parentReference }}"
            webUrl: "{{ webUrl }}"
            createdByUser: "{{ createdByUser }}"
            lastModifiedByUser: "{{ lastModifiedByUser }}"
            displayName: "{{ displayName }}"
            error: "{{ error }}"
            isPersonalSite: {{ isPersonalSite }}
            root: "{{ root }}"
            sharepointIds: "{{ sharepointIds }}"
            siteCollection: "{{ siteCollection }}"
            analytics: "{{ analytics }}"
            columns: "{{ columns }}"
            contentTypes: "{{ contentTypes }}"
            drive: "{{ drive }}"
            drives: "{{ drives }}"
            externalColumns: "{{ externalColumns }}"
            items: "{{ items }}"
            lists: "{{ lists }}"
            onenote: "{{ onenote }}"
            operations: "{{ operations }}"
            pages: "{{ pages }}"
            permissions: "{{ permissions }}"
            sites: "{{ sites }}"
            termStore: "{{ termStore }}"
            termStores: "{{ termStores }}"
        inferenceClassification: "{{ inferenceClassification }}"
        insights: "{{ insights }}"
        joinedTeams:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            classification: "{{ classification }}"
            createdDateTime: "{{ createdDateTime }}"
            description: "{{ description }}"
            displayName: "{{ displayName }}"
            firstChannelName: "{{ firstChannelName }}"
            funSettings: "{{ funSettings }}"
            guestSettings: "{{ guestSettings }}"
            internalId: "{{ internalId }}"
            isArchived: {{ isArchived }}
            memberSettings: "{{ memberSettings }}"
            messagingSettings: "{{ messagingSettings }}"
            specialization: "{{ specialization }}"
            summary: "{{ summary }}"
            tenantId: "{{ tenantId }}"
            visibility: "{{ visibility }}"
            webUrl: "{{ webUrl }}"
            allChannels: "{{ allChannels }}"
            channels: "{{ channels }}"
            group: "{{ group }}"
            incomingChannels: "{{ incomingChannels }}"
            installedApps: "{{ installedApps }}"
            members: "{{ members }}"
            operations: "{{ operations }}"
            permissionGrants: "{{ permissionGrants }}"
            photo: "{{ photo }}"
            primaryChannel: "{{ primaryChannel }}"
            schedule: "{{ schedule }}"
            tags: "{{ tags }}"
            template: "{{ template }}"
        licenseDetails:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            servicePlans: "{{ servicePlans }}"
            skuId: "{{ skuId }}"
            skuPartNumber: "{{ skuPartNumber }}"
        mailFolders:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            childFolderCount: {{ childFolderCount }}
            displayName: "{{ displayName }}"
            isHidden: {{ isHidden }}
            parentFolderId: "{{ parentFolderId }}"
            totalItemCount: {{ totalItemCount }}
            unreadItemCount: {{ unreadItemCount }}
            childFolders: "{{ childFolders }}"
            messageRules: "{{ messageRules }}"
            messages: "{{ messages }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        managedAppRegistrations:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            appIdentifier: "{{ appIdentifier }}"
            applicationVersion: "{{ applicationVersion }}"
            createdDateTime: "{{ createdDateTime }}"
            deviceName: "{{ deviceName }}"
            deviceTag: "{{ deviceTag }}"
            deviceType: "{{ deviceType }}"
            flaggedReasons: "{{ flaggedReasons }}"
            lastSyncDateTime: "{{ lastSyncDateTime }}"
            managementSdkVersion: "{{ managementSdkVersion }}"
            platformVersion: "{{ platformVersion }}"
            userId: "{{ userId }}"
            version: "{{ version }}"
            appliedPolicies: "{{ appliedPolicies }}"
            intendedPolicies: "{{ intendedPolicies }}"
            operations: "{{ operations }}"
        managedDevices:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            activationLockBypassCode: "{{ activationLockBypassCode }}"
            androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
            azureADDeviceId: "{{ azureADDeviceId }}"
            azureADRegistered: {{ azureADRegistered }}
            complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
            complianceState: "{{ complianceState }}"
            configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
            deviceActionResults: "{{ deviceActionResults }}"
            deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
            deviceEnrollmentType: "{{ deviceEnrollmentType }}"
            deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
            deviceName: "{{ deviceName }}"
            deviceRegistrationState: "{{ deviceRegistrationState }}"
            easActivated: {{ easActivated }}
            easActivationDateTime: "{{ easActivationDateTime }}"
            easDeviceId: "{{ easDeviceId }}"
            emailAddress: "{{ emailAddress }}"
            enrolledDateTime: "{{ enrolledDateTime }}"
            enrollmentProfileName: "{{ enrollmentProfileName }}"
            ethernetMacAddress: "{{ ethernetMacAddress }}"
            exchangeAccessState: "{{ exchangeAccessState }}"
            exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
            exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
            freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
            iccid: "{{ iccid }}"
            imei: "{{ imei }}"
            isEncrypted: {{ isEncrypted }}
            isSupervised: {{ isSupervised }}
            jailBroken: "{{ jailBroken }}"
            lastSyncDateTime: "{{ lastSyncDateTime }}"
            managedDeviceName: "{{ managedDeviceName }}"
            managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
            managementAgent: "{{ managementAgent }}"
            managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
            managementState: "{{ managementState }}"
            manufacturer: "{{ manufacturer }}"
            meid: "{{ meid }}"
            model: "{{ model }}"
            notes: "{{ notes }}"
            operatingSystem: "{{ operatingSystem }}"
            osVersion: "{{ osVersion }}"
            partnerReportedThreatState: "{{ partnerReportedThreatState }}"
            phoneNumber: "{{ phoneNumber }}"
            physicalMemoryInBytes: {{ physicalMemoryInBytes }}
            remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
            remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
            requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
            serialNumber: "{{ serialNumber }}"
            subscriberCarrier: "{{ subscriberCarrier }}"
            totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
            udid: "{{ udid }}"
            userDisplayName: "{{ userDisplayName }}"
            userId: "{{ userId }}"
            userPrincipalName: "{{ userPrincipalName }}"
            wiFiMacAddress: "{{ wiFiMacAddress }}"
            deviceCategory: "{{ deviceCategory }}"
            deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
            deviceConfigurationStates: "{{ deviceConfigurationStates }}"
            logCollectionRequests: "{{ logCollectionRequests }}"
            users: "{{ users }}"
            windowsProtectionState: "{{ windowsProtectionState }}"
        manager: "{{ manager }}"
        memberOf:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        messages:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            bccRecipients: "{{ bccRecipients }}"
            body: "{{ body }}"
            bodyPreview: "{{ bodyPreview }}"
            ccRecipients: "{{ ccRecipients }}"
            conversationId: "{{ conversationId }}"
            conversationIndex: "{{ conversationIndex }}"
            flag: "{{ flag }}"
            from: "{{ from }}"
            hasAttachments: {{ hasAttachments }}
            importance: "{{ importance }}"
            inferenceClassification: "{{ inferenceClassification }}"
            internetMessageHeaders: "{{ internetMessageHeaders }}"
            internetMessageId: "{{ internetMessageId }}"
            isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
            isDraft: {{ isDraft }}
            isRead: {{ isRead }}
            isReadReceiptRequested: {{ isReadReceiptRequested }}
            parentFolderId: "{{ parentFolderId }}"
            receivedDateTime: "{{ receivedDateTime }}"
            replyTo: "{{ replyTo }}"
            sender: "{{ sender }}"
            sentDateTime: "{{ sentDateTime }}"
            subject: "{{ subject }}"
            toRecipients: "{{ toRecipients }}"
            uniqueBody: "{{ uniqueBody }}"
            webLink: "{{ webLink }}"
            attachments: "{{ attachments }}"
            extensions: "{{ extensions }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        oauth2PermissionGrants:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            clientId: "{{ clientId }}"
            consentType: "{{ consentType }}"
            principalId: "{{ principalId }}"
            resourceId: "{{ resourceId }}"
            scope: "{{ scope }}"
        onenote: "{{ onenote }}"
        onlineMeetings:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
            allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
            allowBreakoutRooms: {{ allowBreakoutRooms }}
            allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
            allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
            allowedPresenters: "{{ allowedPresenters }}"
            allowLiveShare: "{{ allowLiveShare }}"
            allowMeetingChat: "{{ allowMeetingChat }}"
            allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
            allowPowerPointSharing: {{ allowPowerPointSharing }}
            allowRecording: {{ allowRecording }}
            allowTeamworkReactions: {{ allowTeamworkReactions }}
            allowTranscription: {{ allowTranscription }}
            allowWhiteboard: {{ allowWhiteboard }}
            audioConferencing: "{{ audioConferencing }}"
            chatInfo: "{{ chatInfo }}"
            chatRestrictions: "{{ chatRestrictions }}"
            expiryDateTime: "{{ expiryDateTime }}"
            isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
            isEntryExitAnnounced: {{ isEntryExitAnnounced }}
            joinInformation: "{{ joinInformation }}"
            joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
            joinWebUrl: "{{ joinWebUrl }}"
            lobbyBypassSettings: "{{ lobbyBypassSettings }}"
            meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
            meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
            recordAutomatically: {{ recordAutomatically }}
            sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
            shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
            subject: "{{ subject }}"
            videoTeleconferenceId: "{{ videoTeleconferenceId }}"
            watermarkProtection: "{{ watermarkProtection }}"
            attendanceReports: "{{ attendanceReports }}"
            attendeeReport: "{{ attendeeReport }}"
            broadcastSettings: "{{ broadcastSettings }}"
            creationDateTime: "{{ creationDateTime }}"
            endDateTime: "{{ endDateTime }}"
            externalId: "{{ externalId }}"
            isBroadcast: {{ isBroadcast }}
            meetingTemplateId: "{{ meetingTemplateId }}"
            participants: "{{ participants }}"
            startDateTime: "{{ startDateTime }}"
            recordings: "{{ recordings }}"
            transcripts: "{{ transcripts }}"
        onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
        outlook: "{{ outlook }}"
        ownedDevices:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        ownedObjects:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        people:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            birthday: "{{ birthday }}"
            companyName: "{{ companyName }}"
            department: "{{ department }}"
            displayName: "{{ displayName }}"
            givenName: "{{ givenName }}"
            imAddress: "{{ imAddress }}"
            isFavorite: {{ isFavorite }}
            jobTitle: "{{ jobTitle }}"
            officeLocation: "{{ officeLocation }}"
            personNotes: "{{ personNotes }}"
            personType: "{{ personType }}"
            phones: "{{ phones }}"
            postalAddresses: "{{ postalAddresses }}"
            profession: "{{ profession }}"
            scoredEmailAddresses: "{{ scoredEmailAddresses }}"
            surname: "{{ surname }}"
            userPrincipalName: "{{ userPrincipalName }}"
            websites: "{{ websites }}"
            yomiCompany: "{{ yomiCompany }}"
        permissionGrants:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            clientAppId: "{{ clientAppId }}"
            clientId: "{{ clientId }}"
            permission: "{{ permission }}"
            permissionType: "{{ permissionType }}"
            resourceAppId: "{{ resourceAppId }}"
        photo: "{{ photo }}"
        photos:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            height: {{ height }}
            width: {{ width }}
        planner: "{{ planner }}"
        presence: "{{ presence }}"
        registeredDevices:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        scopedRoleMemberOf:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            administrativeUnitId: "{{ administrativeUnitId }}"
            roleId: "{{ roleId }}"
            roleMemberInfo:
              displayName: "{{ displayName }}"
              id: "{{ id }}"
              @odata.type: "{{ @odata.type }}"
        settings: "{{ settings }}"
        solutions: "{{ solutions }}"
        sponsors:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        teamwork: "{{ teamwork }}"
        todo: "{{ todo }}"
        transitiveMemberOf:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
    - name: lastModifiedBy
      description: |
        The unique identifier of the Microsoft Entra identity that last modified the workflow.
      value:
        id: "{{ id }}"
        @odata.type: "{{ @odata.type }}"
        deletedDateTime: "{{ deletedDateTime }}"
        aboutMe: "{{ aboutMe }}"
        accountEnabled: {{ accountEnabled }}
        ageGroup: "{{ ageGroup }}"
        assignedLicenses:
          - disabledPlans: "{{ disabledPlans }}"
            skuId: "{{ skuId }}"
            @odata.type: "{{ @odata.type }}"
        assignedPlans:
          - assignedDateTime: "{{ assignedDateTime }}"
            capabilityStatus: "{{ capabilityStatus }}"
            service: "{{ service }}"
            servicePlanId: "{{ servicePlanId }}"
            @odata.type: "{{ @odata.type }}"
        authorizationInfo: "{{ authorizationInfo }}"
        birthday: "{{ birthday }}"
        businessPhones:
          - "{{ businessPhones }}"
        city: "{{ city }}"
        companyName: "{{ companyName }}"
        consentProvidedForMinor: "{{ consentProvidedForMinor }}"
        country: "{{ country }}"
        createdDateTime: "{{ createdDateTime }}"
        creationType: "{{ creationType }}"
        customSecurityAttributes: "{{ customSecurityAttributes }}"
        department: "{{ department }}"
        deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
        displayName: "{{ displayName }}"
        employeeHireDate: "{{ employeeHireDate }}"
        employeeId: "{{ employeeId }}"
        employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
        employeeOrgData: "{{ employeeOrgData }}"
        employeeType: "{{ employeeType }}"
        externalUserState: "{{ externalUserState }}"
        externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
        faxNumber: "{{ faxNumber }}"
        givenName: "{{ givenName }}"
        hireDate: "{{ hireDate }}"
        identities:
          - issuer: "{{ issuer }}"
            issuerAssignedId: "{{ issuerAssignedId }}"
            signInType: "{{ signInType }}"
            @odata.type: "{{ @odata.type }}"
        identityParentId: "{{ identityParentId }}"
        imAddresses:
          - "{{ imAddresses }}"
        interests:
          - "{{ interests }}"
        isManagementRestricted: {{ isManagementRestricted }}
        isResourceAccount: {{ isResourceAccount }}
        jobTitle: "{{ jobTitle }}"
        lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
        legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
        licenseAssignmentStates:
          - assignedByGroup: "{{ assignedByGroup }}"
            disabledPlans: "{{ disabledPlans }}"
            error: "{{ error }}"
            lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
            skuId: "{{ skuId }}"
            state: "{{ state }}"
            @odata.type: "{{ @odata.type }}"
        mail: "{{ mail }}"
        mailboxSettings: "{{ mailboxSettings }}"
        mailNickname: "{{ mailNickname }}"
        mobilePhone: "{{ mobilePhone }}"
        mySite: "{{ mySite }}"
        officeLocation: "{{ officeLocation }}"
        onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
        onPremisesDomainName: "{{ onPremisesDomainName }}"
        onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
        onPremisesImmutableId: "{{ onPremisesImmutableId }}"
        onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
        onPremisesProvisioningErrors:
          - category: "{{ category }}"
            occurredDateTime: "{{ occurredDateTime }}"
            propertyCausingError: "{{ propertyCausingError }}"
            value: "{{ value }}"
            @odata.type: "{{ @odata.type }}"
        onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
        onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
        onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
        onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
        otherMails:
          - "{{ otherMails }}"
        passwordPolicies: "{{ passwordPolicies }}"
        passwordProfile: "{{ passwordProfile }}"
        pastProjects:
          - "{{ pastProjects }}"
        postalCode: "{{ postalCode }}"
        preferredDataLocation: "{{ preferredDataLocation }}"
        preferredLanguage: "{{ preferredLanguage }}"
        preferredName: "{{ preferredName }}"
        print: "{{ print }}"
        provisionedPlans:
          - capabilityStatus: "{{ capabilityStatus }}"
            provisioningStatus: "{{ provisioningStatus }}"
            service: "{{ service }}"
            @odata.type: "{{ @odata.type }}"
        proxyAddresses:
          - "{{ proxyAddresses }}"
        responsibilities:
          - "{{ responsibilities }}"
        schools:
          - "{{ schools }}"
        securityIdentifier: "{{ securityIdentifier }}"
        serviceProvisioningErrors:
          - createdDateTime: "{{ createdDateTime }}"
            isResolved: {{ isResolved }}
            serviceInstance: "{{ serviceInstance }}"
            @odata.type: "{{ @odata.type }}"
        showInAddressList: {{ showInAddressList }}
        signInActivity: "{{ signInActivity }}"
        signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
        skills:
          - "{{ skills }}"
        state: "{{ state }}"
        streetAddress: "{{ streetAddress }}"
        surname: "{{ surname }}"
        usageLocation: "{{ usageLocation }}"
        userPrincipalName: "{{ userPrincipalName }}"
        userType: "{{ userType }}"
        activities:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            activationUrl: "{{ activationUrl }}"
            activitySourceHost: "{{ activitySourceHost }}"
            appActivityId: "{{ appActivityId }}"
            appDisplayName: "{{ appDisplayName }}"
            contentInfo: "{{ contentInfo }}"
            contentUrl: "{{ contentUrl }}"
            createdDateTime: "{{ createdDateTime }}"
            expirationDateTime: "{{ expirationDateTime }}"
            fallbackUrl: "{{ fallbackUrl }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            status: "{{ status }}"
            userTimezone: "{{ userTimezone }}"
            visualElements:
              attribution:
                addImageQuery: {{ addImageQuery }}
                alternateText: "{{ alternateText }}"
                alternativeText: "{{ alternativeText }}"
                iconUrl: "{{ iconUrl }}"
                @odata.type: "{{ @odata.type }}"
              backgroundColor: "{{ backgroundColor }}"
              content: "{{ content }}"
              description: "{{ description }}"
              displayText: "{{ displayText }}"
              @odata.type: "{{ @odata.type }}"
            historyItems: "{{ historyItems }}"
        adhocCalls:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            recordings: "{{ recordings }}"
            transcripts: "{{ transcripts }}"
        agreementAcceptances:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            agreementFileId: "{{ agreementFileId }}"
            agreementId: "{{ agreementId }}"
            deviceDisplayName: "{{ deviceDisplayName }}"
            deviceId: "{{ deviceId }}"
            deviceOSType: "{{ deviceOSType }}"
            deviceOSVersion: "{{ deviceOSVersion }}"
            expirationDateTime: "{{ expirationDateTime }}"
            recordedDateTime: "{{ recordedDateTime }}"
            state: "{{ state }}"
            userDisplayName: "{{ userDisplayName }}"
            userEmail: "{{ userEmail }}"
            userId: "{{ userId }}"
            userPrincipalName: "{{ userPrincipalName }}"
        appRoleAssignments:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            appRoleId: "{{ appRoleId }}"
            createdDateTime: "{{ createdDateTime }}"
            principalDisplayName: "{{ principalDisplayName }}"
            principalId: "{{ principalId }}"
            principalType: "{{ principalType }}"
            resourceDisplayName: "{{ resourceDisplayName }}"
            resourceId: "{{ resourceId }}"
        authentication: "{{ authentication }}"
        calendar: "{{ calendar }}"
        calendarGroups:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            changeKey: "{{ changeKey }}"
            classId: "{{ classId }}"
            name: "{{ name }}"
            calendars: "{{ calendars }}"
        calendars:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
            canEdit: {{ canEdit }}
            canShare: {{ canShare }}
            canViewPrivateItems: {{ canViewPrivateItems }}
            changeKey: "{{ changeKey }}"
            color: "{{ color }}"
            defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
            hexColor: "{{ hexColor }}"
            isDefaultCalendar: {{ isDefaultCalendar }}
            isRemovable: {{ isRemovable }}
            isTallyingResponses: {{ isTallyingResponses }}
            name: "{{ name }}"
            owner: "{{ owner }}"
            calendarPermissions: "{{ calendarPermissions }}"
            calendarView: "{{ calendarView }}"
            events: "{{ events }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        calendarView:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            allowNewTimeProposals: {{ allowNewTimeProposals }}
            attendees: "{{ attendees }}"
            body: "{{ body }}"
            bodyPreview: "{{ bodyPreview }}"
            cancelledOccurrences: "{{ cancelledOccurrences }}"
            end: "{{ end }}"
            hasAttachments: {{ hasAttachments }}
            hideAttendees: {{ hideAttendees }}
            iCalUId: "{{ iCalUId }}"
            importance: "{{ importance }}"
            isAllDay: {{ isAllDay }}
            isCancelled: {{ isCancelled }}
            isDraft: {{ isDraft }}
            isOnlineMeeting: {{ isOnlineMeeting }}
            isOrganizer: {{ isOrganizer }}
            isReminderOn: {{ isReminderOn }}
            location: "{{ location }}"
            locations: "{{ locations }}"
            onlineMeeting: "{{ onlineMeeting }}"
            onlineMeetingProvider: "{{ onlineMeetingProvider }}"
            onlineMeetingUrl: "{{ onlineMeetingUrl }}"
            organizer: "{{ organizer }}"
            originalEndTimeZone: "{{ originalEndTimeZone }}"
            originalStart: "{{ originalStart }}"
            originalStartTimeZone: "{{ originalStartTimeZone }}"
            recurrence: "{{ recurrence }}"
            reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
            responseRequested: {{ responseRequested }}
            responseStatus: "{{ responseStatus }}"
            sensitivity: "{{ sensitivity }}"
            seriesMasterId: "{{ seriesMasterId }}"
            showAs: "{{ showAs }}"
            start: "{{ start }}"
            subject: "{{ subject }}"
            transactionId: "{{ transactionId }}"
            type: "{{ type }}"
            webLink: "{{ webLink }}"
            attachments: "{{ attachments }}"
            calendar: "{{ calendar }}"
            exceptionOccurrences: "{{ exceptionOccurrences }}"
            extensions: "{{ extensions }}"
            instances: "{{ instances }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        chats:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            chatType: "{{ chatType }}"
            createdDateTime: "{{ createdDateTime }}"
            isHiddenForAllMembers: {{ isHiddenForAllMembers }}
            lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
            migrationMode: "{{ migrationMode }}"
            onlineMeetingInfo: "{{ onlineMeetingInfo }}"
            originalCreatedDateTime: "{{ originalCreatedDateTime }}"
            tenantId: "{{ tenantId }}"
            topic: "{{ topic }}"
            viewpoint: "{{ viewpoint }}"
            webUrl: "{{ webUrl }}"
            installedApps: "{{ installedApps }}"
            lastMessagePreview: "{{ lastMessagePreview }}"
            members: "{{ members }}"
            messages: "{{ messages }}"
            permissionGrants: "{{ permissionGrants }}"
            pinnedMessages: "{{ pinnedMessages }}"
            tabs: "{{ tabs }}"
        cloudClipboard: "{{ cloudClipboard }}"
        cloudPCs:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            aadDeviceId: "{{ aadDeviceId }}"
            displayName: "{{ displayName }}"
            gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
            imageDisplayName: "{{ imageDisplayName }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            managedDeviceId: "{{ managedDeviceId }}"
            managedDeviceName: "{{ managedDeviceName }}"
            onPremisesConnectionName: "{{ onPremisesConnectionName }}"
            provisioningPolicyId: "{{ provisioningPolicyId }}"
            provisioningPolicyName: "{{ provisioningPolicyName }}"
            provisioningType: "{{ provisioningType }}"
            servicePlanId: "{{ servicePlanId }}"
            servicePlanName: "{{ servicePlanName }}"
            userPrincipalName: "{{ userPrincipalName }}"
        contactFolders:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            displayName: "{{ displayName }}"
            parentFolderId: "{{ parentFolderId }}"
            childFolders: "{{ childFolders }}"
            contacts: "{{ contacts }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        contacts:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            assistantName: "{{ assistantName }}"
            birthday: "{{ birthday }}"
            businessAddress: "{{ businessAddress }}"
            businessHomePage: "{{ businessHomePage }}"
            businessPhones: "{{ businessPhones }}"
            children: "{{ children }}"
            companyName: "{{ companyName }}"
            department: "{{ department }}"
            displayName: "{{ displayName }}"
            emailAddresses: "{{ emailAddresses }}"
            fileAs: "{{ fileAs }}"
            generation: "{{ generation }}"
            givenName: "{{ givenName }}"
            homeAddress: "{{ homeAddress }}"
            homePhones: "{{ homePhones }}"
            imAddresses: "{{ imAddresses }}"
            initials: "{{ initials }}"
            jobTitle: "{{ jobTitle }}"
            manager: "{{ manager }}"
            middleName: "{{ middleName }}"
            mobilePhone: "{{ mobilePhone }}"
            nickName: "{{ nickName }}"
            officeLocation: "{{ officeLocation }}"
            otherAddress: "{{ otherAddress }}"
            parentFolderId: "{{ parentFolderId }}"
            personalNotes: "{{ personalNotes }}"
            primaryEmailAddress: "{{ primaryEmailAddress }}"
            profession: "{{ profession }}"
            secondaryEmailAddress: "{{ secondaryEmailAddress }}"
            spouseName: "{{ spouseName }}"
            surname: "{{ surname }}"
            tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
            title: "{{ title }}"
            yomiCompanyName: "{{ yomiCompanyName }}"
            yomiGivenName: "{{ yomiGivenName }}"
            yomiSurname: "{{ yomiSurname }}"
            extensions: "{{ extensions }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            photo: "{{ photo }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        createdObjects:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
        deviceManagementTroubleshootingEvents:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            correlationId: "{{ correlationId }}"
            eventDateTime: "{{ eventDateTime }}"
        directReports:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        drive: "{{ drive }}"
        drives:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            createdBy: "{{ createdBy }}"
            createdDateTime: "{{ createdDateTime }}"
            description: "{{ description }}"
            eTag: "{{ eTag }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            name: "{{ name }}"
            parentReference: "{{ parentReference }}"
            webUrl: "{{ webUrl }}"
            createdByUser: "{{ createdByUser }}"
            lastModifiedByUser: "{{ lastModifiedByUser }}"
            driveType: "{{ driveType }}"
            owner: "{{ owner }}"
            quota: "{{ quota }}"
            sharePointIds: "{{ sharePointIds }}"
            system: "{{ system }}"
            bundles: "{{ bundles }}"
            following: "{{ following }}"
            items: "{{ items }}"
            list: "{{ list }}"
            root: "{{ root }}"
            special: "{{ special }}"
        employeeExperience: "{{ employeeExperience }}"
        events:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            allowNewTimeProposals: {{ allowNewTimeProposals }}
            attendees: "{{ attendees }}"
            body: "{{ body }}"
            bodyPreview: "{{ bodyPreview }}"
            cancelledOccurrences: "{{ cancelledOccurrences }}"
            end: "{{ end }}"
            hasAttachments: {{ hasAttachments }}
            hideAttendees: {{ hideAttendees }}
            iCalUId: "{{ iCalUId }}"
            importance: "{{ importance }}"
            isAllDay: {{ isAllDay }}
            isCancelled: {{ isCancelled }}
            isDraft: {{ isDraft }}
            isOnlineMeeting: {{ isOnlineMeeting }}
            isOrganizer: {{ isOrganizer }}
            isReminderOn: {{ isReminderOn }}
            location: "{{ location }}"
            locations: "{{ locations }}"
            onlineMeeting: "{{ onlineMeeting }}"
            onlineMeetingProvider: "{{ onlineMeetingProvider }}"
            onlineMeetingUrl: "{{ onlineMeetingUrl }}"
            organizer: "{{ organizer }}"
            originalEndTimeZone: "{{ originalEndTimeZone }}"
            originalStart: "{{ originalStart }}"
            originalStartTimeZone: "{{ originalStartTimeZone }}"
            recurrence: "{{ recurrence }}"
            reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
            responseRequested: {{ responseRequested }}
            responseStatus: "{{ responseStatus }}"
            sensitivity: "{{ sensitivity }}"
            seriesMasterId: "{{ seriesMasterId }}"
            showAs: "{{ showAs }}"
            start: "{{ start }}"
            subject: "{{ subject }}"
            transactionId: "{{ transactionId }}"
            type: "{{ type }}"
            webLink: "{{ webLink }}"
            attachments: "{{ attachments }}"
            calendar: "{{ calendar }}"
            exceptionOccurrences: "{{ exceptionOccurrences }}"
            extensions: "{{ extensions }}"
            instances: "{{ instances }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        extensions:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
        followedSites:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            createdBy: "{{ createdBy }}"
            createdDateTime: "{{ createdDateTime }}"
            description: "{{ description }}"
            eTag: "{{ eTag }}"
            lastModifiedBy: "{{ lastModifiedBy }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            name: "{{ name }}"
            parentReference: "{{ parentReference }}"
            webUrl: "{{ webUrl }}"
            createdByUser: "{{ createdByUser }}"
            lastModifiedByUser: "{{ lastModifiedByUser }}"
            displayName: "{{ displayName }}"
            error: "{{ error }}"
            isPersonalSite: {{ isPersonalSite }}
            root: "{{ root }}"
            sharepointIds: "{{ sharepointIds }}"
            siteCollection: "{{ siteCollection }}"
            analytics: "{{ analytics }}"
            columns: "{{ columns }}"
            contentTypes: "{{ contentTypes }}"
            drive: "{{ drive }}"
            drives: "{{ drives }}"
            externalColumns: "{{ externalColumns }}"
            items: "{{ items }}"
            lists: "{{ lists }}"
            onenote: "{{ onenote }}"
            operations: "{{ operations }}"
            pages: "{{ pages }}"
            permissions: "{{ permissions }}"
            sites: "{{ sites }}"
            termStore: "{{ termStore }}"
            termStores: "{{ termStores }}"
        inferenceClassification: "{{ inferenceClassification }}"
        insights: "{{ insights }}"
        joinedTeams:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            classification: "{{ classification }}"
            createdDateTime: "{{ createdDateTime }}"
            description: "{{ description }}"
            displayName: "{{ displayName }}"
            firstChannelName: "{{ firstChannelName }}"
            funSettings: "{{ funSettings }}"
            guestSettings: "{{ guestSettings }}"
            internalId: "{{ internalId }}"
            isArchived: {{ isArchived }}
            memberSettings: "{{ memberSettings }}"
            messagingSettings: "{{ messagingSettings }}"
            specialization: "{{ specialization }}"
            summary: "{{ summary }}"
            tenantId: "{{ tenantId }}"
            visibility: "{{ visibility }}"
            webUrl: "{{ webUrl }}"
            allChannels: "{{ allChannels }}"
            channels: "{{ channels }}"
            group: "{{ group }}"
            incomingChannels: "{{ incomingChannels }}"
            installedApps: "{{ installedApps }}"
            members: "{{ members }}"
            operations: "{{ operations }}"
            permissionGrants: "{{ permissionGrants }}"
            photo: "{{ photo }}"
            primaryChannel: "{{ primaryChannel }}"
            schedule: "{{ schedule }}"
            tags: "{{ tags }}"
            template: "{{ template }}"
        licenseDetails:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            servicePlans: "{{ servicePlans }}"
            skuId: "{{ skuId }}"
            skuPartNumber: "{{ skuPartNumber }}"
        mailFolders:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            childFolderCount: {{ childFolderCount }}
            displayName: "{{ displayName }}"
            isHidden: {{ isHidden }}
            parentFolderId: "{{ parentFolderId }}"
            totalItemCount: {{ totalItemCount }}
            unreadItemCount: {{ unreadItemCount }}
            childFolders: "{{ childFolders }}"
            messageRules: "{{ messageRules }}"
            messages: "{{ messages }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        managedAppRegistrations:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            appIdentifier: "{{ appIdentifier }}"
            applicationVersion: "{{ applicationVersion }}"
            createdDateTime: "{{ createdDateTime }}"
            deviceName: "{{ deviceName }}"
            deviceTag: "{{ deviceTag }}"
            deviceType: "{{ deviceType }}"
            flaggedReasons: "{{ flaggedReasons }}"
            lastSyncDateTime: "{{ lastSyncDateTime }}"
            managementSdkVersion: "{{ managementSdkVersion }}"
            platformVersion: "{{ platformVersion }}"
            userId: "{{ userId }}"
            version: "{{ version }}"
            appliedPolicies: "{{ appliedPolicies }}"
            intendedPolicies: "{{ intendedPolicies }}"
            operations: "{{ operations }}"
        managedDevices:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            activationLockBypassCode: "{{ activationLockBypassCode }}"
            androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
            azureADDeviceId: "{{ azureADDeviceId }}"
            azureADRegistered: {{ azureADRegistered }}
            complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
            complianceState: "{{ complianceState }}"
            configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
            deviceActionResults: "{{ deviceActionResults }}"
            deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
            deviceEnrollmentType: "{{ deviceEnrollmentType }}"
            deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
            deviceName: "{{ deviceName }}"
            deviceRegistrationState: "{{ deviceRegistrationState }}"
            easActivated: {{ easActivated }}
            easActivationDateTime: "{{ easActivationDateTime }}"
            easDeviceId: "{{ easDeviceId }}"
            emailAddress: "{{ emailAddress }}"
            enrolledDateTime: "{{ enrolledDateTime }}"
            enrollmentProfileName: "{{ enrollmentProfileName }}"
            ethernetMacAddress: "{{ ethernetMacAddress }}"
            exchangeAccessState: "{{ exchangeAccessState }}"
            exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
            exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
            freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
            iccid: "{{ iccid }}"
            imei: "{{ imei }}"
            isEncrypted: {{ isEncrypted }}
            isSupervised: {{ isSupervised }}
            jailBroken: "{{ jailBroken }}"
            lastSyncDateTime: "{{ lastSyncDateTime }}"
            managedDeviceName: "{{ managedDeviceName }}"
            managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
            managementAgent: "{{ managementAgent }}"
            managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
            managementState: "{{ managementState }}"
            manufacturer: "{{ manufacturer }}"
            meid: "{{ meid }}"
            model: "{{ model }}"
            notes: "{{ notes }}"
            operatingSystem: "{{ operatingSystem }}"
            osVersion: "{{ osVersion }}"
            partnerReportedThreatState: "{{ partnerReportedThreatState }}"
            phoneNumber: "{{ phoneNumber }}"
            physicalMemoryInBytes: {{ physicalMemoryInBytes }}
            remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
            remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
            requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
            serialNumber: "{{ serialNumber }}"
            subscriberCarrier: "{{ subscriberCarrier }}"
            totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
            udid: "{{ udid }}"
            userDisplayName: "{{ userDisplayName }}"
            userId: "{{ userId }}"
            userPrincipalName: "{{ userPrincipalName }}"
            wiFiMacAddress: "{{ wiFiMacAddress }}"
            deviceCategory: "{{ deviceCategory }}"
            deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
            deviceConfigurationStates: "{{ deviceConfigurationStates }}"
            logCollectionRequests: "{{ logCollectionRequests }}"
            users: "{{ users }}"
            windowsProtectionState: "{{ windowsProtectionState }}"
        manager: "{{ manager }}"
        memberOf:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        messages:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            categories: "{{ categories }}"
            changeKey: "{{ changeKey }}"
            createdDateTime: "{{ createdDateTime }}"
            lastModifiedDateTime: "{{ lastModifiedDateTime }}"
            bccRecipients: "{{ bccRecipients }}"
            body: "{{ body }}"
            bodyPreview: "{{ bodyPreview }}"
            ccRecipients: "{{ ccRecipients }}"
            conversationId: "{{ conversationId }}"
            conversationIndex: "{{ conversationIndex }}"
            flag: "{{ flag }}"
            from: "{{ from }}"
            hasAttachments: {{ hasAttachments }}
            importance: "{{ importance }}"
            inferenceClassification: "{{ inferenceClassification }}"
            internetMessageHeaders: "{{ internetMessageHeaders }}"
            internetMessageId: "{{ internetMessageId }}"
            isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
            isDraft: {{ isDraft }}
            isRead: {{ isRead }}
            isReadReceiptRequested: {{ isReadReceiptRequested }}
            parentFolderId: "{{ parentFolderId }}"
            receivedDateTime: "{{ receivedDateTime }}"
            replyTo: "{{ replyTo }}"
            sender: "{{ sender }}"
            sentDateTime: "{{ sentDateTime }}"
            subject: "{{ subject }}"
            toRecipients: "{{ toRecipients }}"
            uniqueBody: "{{ uniqueBody }}"
            webLink: "{{ webLink }}"
            attachments: "{{ attachments }}"
            extensions: "{{ extensions }}"
            multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
            singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
        oauth2PermissionGrants:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            clientId: "{{ clientId }}"
            consentType: "{{ consentType }}"
            principalId: "{{ principalId }}"
            resourceId: "{{ resourceId }}"
            scope: "{{ scope }}"
        onenote: "{{ onenote }}"
        onlineMeetings:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
            allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
            allowBreakoutRooms: {{ allowBreakoutRooms }}
            allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
            allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
            allowedPresenters: "{{ allowedPresenters }}"
            allowLiveShare: "{{ allowLiveShare }}"
            allowMeetingChat: "{{ allowMeetingChat }}"
            allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
            allowPowerPointSharing: {{ allowPowerPointSharing }}
            allowRecording: {{ allowRecording }}
            allowTeamworkReactions: {{ allowTeamworkReactions }}
            allowTranscription: {{ allowTranscription }}
            allowWhiteboard: {{ allowWhiteboard }}
            audioConferencing: "{{ audioConferencing }}"
            chatInfo: "{{ chatInfo }}"
            chatRestrictions: "{{ chatRestrictions }}"
            expiryDateTime: "{{ expiryDateTime }}"
            isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
            isEntryExitAnnounced: {{ isEntryExitAnnounced }}
            joinInformation: "{{ joinInformation }}"
            joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
            joinWebUrl: "{{ joinWebUrl }}"
            lobbyBypassSettings: "{{ lobbyBypassSettings }}"
            meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
            meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
            recordAutomatically: {{ recordAutomatically }}
            sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
            shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
            subject: "{{ subject }}"
            videoTeleconferenceId: "{{ videoTeleconferenceId }}"
            watermarkProtection: "{{ watermarkProtection }}"
            attendanceReports: "{{ attendanceReports }}"
            attendeeReport: "{{ attendeeReport }}"
            broadcastSettings: "{{ broadcastSettings }}"
            creationDateTime: "{{ creationDateTime }}"
            endDateTime: "{{ endDateTime }}"
            externalId: "{{ externalId }}"
            isBroadcast: {{ isBroadcast }}
            meetingTemplateId: "{{ meetingTemplateId }}"
            participants: "{{ participants }}"
            startDateTime: "{{ startDateTime }}"
            recordings: "{{ recordings }}"
            transcripts: "{{ transcripts }}"
        onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
        outlook: "{{ outlook }}"
        ownedDevices:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        ownedObjects:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        people:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            birthday: "{{ birthday }}"
            companyName: "{{ companyName }}"
            department: "{{ department }}"
            displayName: "{{ displayName }}"
            givenName: "{{ givenName }}"
            imAddress: "{{ imAddress }}"
            isFavorite: {{ isFavorite }}
            jobTitle: "{{ jobTitle }}"
            officeLocation: "{{ officeLocation }}"
            personNotes: "{{ personNotes }}"
            personType: "{{ personType }}"
            phones: "{{ phones }}"
            postalAddresses: "{{ postalAddresses }}"
            profession: "{{ profession }}"
            scoredEmailAddresses: "{{ scoredEmailAddresses }}"
            surname: "{{ surname }}"
            userPrincipalName: "{{ userPrincipalName }}"
            websites: "{{ websites }}"
            yomiCompany: "{{ yomiCompany }}"
        permissionGrants:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            clientAppId: "{{ clientAppId }}"
            clientId: "{{ clientId }}"
            permission: "{{ permission }}"
            permissionType: "{{ permissionType }}"
            resourceAppId: "{{ resourceAppId }}"
        photo: "{{ photo }}"
        photos:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            height: {{ height }}
            width: {{ width }}
        planner: "{{ planner }}"
        presence: "{{ presence }}"
        registeredDevices:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        scopedRoleMemberOf:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            administrativeUnitId: "{{ administrativeUnitId }}"
            roleId: "{{ roleId }}"
            roleMemberInfo:
              displayName: "{{ displayName }}"
              id: "{{ id }}"
              @odata.type: "{{ @odata.type }}"
        settings: "{{ settings }}"
        solutions: "{{ solutions }}"
        sponsors:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
        teamwork: "{{ teamwork }}"
        todo: "{{ todo }}"
        transitiveMemberOf:
          - id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
    - name: tasks
      description: |
        The tasks in the workflow.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          arguments: "{{ arguments }}"
          category: "{{ category }}"
          continueOnError: {{ continueOnError }}
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          executionSequence: {{ executionSequence }}
          isEnabled: {{ isEnabled }}
          taskDefinitionId: "{{ taskDefinitionId }}"
          taskProcessingResults: "{{ taskProcessingResults }}"
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    - name: id
      value: "{{ id }}"
      description: |
        Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.
    - name: nextScheduleRunDateTime
      value: "{{ nextScheduleRunDateTime }}"
      description: |
        The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderby.
    - name: version
      value: {{ version }}
      description: |
        The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    - name: executionScope
      description: |
        The list of users that meet the workflowExecutionConditions of a workflow.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          completedDateTime: "{{ completedDateTime }}"
          failedTasksCount: {{ failedTasksCount }}
          processingStatus: "{{ processingStatus }}"
          scheduledDateTime: "{{ scheduledDateTime }}"
          startedDateTime: "{{ startedDateTime }}"
          totalTasksCount: {{ totalTasksCount }}
          totalUnprocessedTasksCount: {{ totalUnprocessedTasksCount }}
          workflowExecutionType: "{{ workflowExecutionType }}"
          workflowVersion: {{ workflowVersion }}
          reprocessedRuns: "{{ reprocessedRuns }}"
          subject:
            id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            aboutMe: "{{ aboutMe }}"
            accountEnabled: {{ accountEnabled }}
            ageGroup: "{{ ageGroup }}"
            assignedLicenses:
              - disabledPlans: "{{ disabledPlans }}"
                skuId: "{{ skuId }}"
                @odata.type: "{{ @odata.type }}"
            assignedPlans:
              - assignedDateTime: "{{ assignedDateTime }}"
                capabilityStatus: "{{ capabilityStatus }}"
                service: "{{ service }}"
                servicePlanId: "{{ servicePlanId }}"
                @odata.type: "{{ @odata.type }}"
            authorizationInfo: "{{ authorizationInfo }}"
            birthday: "{{ birthday }}"
            businessPhones:
              - "{{ businessPhones }}"
            city: "{{ city }}"
            companyName: "{{ companyName }}"
            consentProvidedForMinor: "{{ consentProvidedForMinor }}"
            country: "{{ country }}"
            createdDateTime: "{{ createdDateTime }}"
            creationType: "{{ creationType }}"
            customSecurityAttributes: "{{ customSecurityAttributes }}"
            department: "{{ department }}"
            deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
            displayName: "{{ displayName }}"
            employeeHireDate: "{{ employeeHireDate }}"
            employeeId: "{{ employeeId }}"
            employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
            employeeOrgData: "{{ employeeOrgData }}"
            employeeType: "{{ employeeType }}"
            externalUserState: "{{ externalUserState }}"
            externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
            faxNumber: "{{ faxNumber }}"
            givenName: "{{ givenName }}"
            hireDate: "{{ hireDate }}"
            identities:
              - issuer: "{{ issuer }}"
                issuerAssignedId: "{{ issuerAssignedId }}"
                signInType: "{{ signInType }}"
                @odata.type: "{{ @odata.type }}"
            identityParentId: "{{ identityParentId }}"
            imAddresses:
              - "{{ imAddresses }}"
            interests:
              - "{{ interests }}"
            isManagementRestricted: {{ isManagementRestricted }}
            isResourceAccount: {{ isResourceAccount }}
            jobTitle: "{{ jobTitle }}"
            lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
            legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
            licenseAssignmentStates:
              - assignedByGroup: "{{ assignedByGroup }}"
                disabledPlans: "{{ disabledPlans }}"
                error: "{{ error }}"
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                skuId: "{{ skuId }}"
                state: "{{ state }}"
                @odata.type: "{{ @odata.type }}"
            mail: "{{ mail }}"
            mailboxSettings: "{{ mailboxSettings }}"
            mailNickname: "{{ mailNickname }}"
            mobilePhone: "{{ mobilePhone }}"
            mySite: "{{ mySite }}"
            officeLocation: "{{ officeLocation }}"
            onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
            onPremisesDomainName: "{{ onPremisesDomainName }}"
            onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
            onPremisesImmutableId: "{{ onPremisesImmutableId }}"
            onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
            onPremisesProvisioningErrors:
              - category: "{{ category }}"
                occurredDateTime: "{{ occurredDateTime }}"
                propertyCausingError: "{{ propertyCausingError }}"
                value: "{{ value }}"
                @odata.type: "{{ @odata.type }}"
            onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
            onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
            onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
            onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
            otherMails:
              - "{{ otherMails }}"
            passwordPolicies: "{{ passwordPolicies }}"
            passwordProfile: "{{ passwordProfile }}"
            pastProjects:
              - "{{ pastProjects }}"
            postalCode: "{{ postalCode }}"
            preferredDataLocation: "{{ preferredDataLocation }}"
            preferredLanguage: "{{ preferredLanguage }}"
            preferredName: "{{ preferredName }}"
            print: "{{ print }}"
            provisionedPlans:
              - capabilityStatus: "{{ capabilityStatus }}"
                provisioningStatus: "{{ provisioningStatus }}"
                service: "{{ service }}"
                @odata.type: "{{ @odata.type }}"
            proxyAddresses:
              - "{{ proxyAddresses }}"
            responsibilities:
              - "{{ responsibilities }}"
            schools:
              - "{{ schools }}"
            securityIdentifier: "{{ securityIdentifier }}"
            serviceProvisioningErrors:
              - createdDateTime: "{{ createdDateTime }}"
                isResolved: {{ isResolved }}
                serviceInstance: "{{ serviceInstance }}"
                @odata.type: "{{ @odata.type }}"
            showInAddressList: {{ showInAddressList }}
            signInActivity: "{{ signInActivity }}"
            signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
            skills:
              - "{{ skills }}"
            state: "{{ state }}"
            streetAddress: "{{ streetAddress }}"
            surname: "{{ surname }}"
            usageLocation: "{{ usageLocation }}"
            userPrincipalName: "{{ userPrincipalName }}"
            userType: "{{ userType }}"
            activities:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationUrl: "{{ activationUrl }}"
                activitySourceHost: "{{ activitySourceHost }}"
                appActivityId: "{{ appActivityId }}"
                appDisplayName: "{{ appDisplayName }}"
                contentInfo: "{{ contentInfo }}"
                contentUrl: "{{ contentUrl }}"
                createdDateTime: "{{ createdDateTime }}"
                expirationDateTime: "{{ expirationDateTime }}"
                fallbackUrl: "{{ fallbackUrl }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                status: "{{ status }}"
                userTimezone: "{{ userTimezone }}"
                visualElements:
                  attribution:
                    addImageQuery: {{ addImageQuery }}
                    alternateText: "{{ alternateText }}"
                    alternativeText: "{{ alternativeText }}"
                    iconUrl: "{{ iconUrl }}"
                    @odata.type: "{{ @odata.type }}"
                  backgroundColor: "{{ backgroundColor }}"
                  content: "{{ content }}"
                  description: "{{ description }}"
                  displayText: "{{ displayText }}"
                  @odata.type: "{{ @odata.type }}"
                historyItems: "{{ historyItems }}"
            adhocCalls:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            agreementAcceptances:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                agreementFileId: "{{ agreementFileId }}"
                agreementId: "{{ agreementId }}"
                deviceDisplayName: "{{ deviceDisplayName }}"
                deviceId: "{{ deviceId }}"
                deviceOSType: "{{ deviceOSType }}"
                deviceOSVersion: "{{ deviceOSVersion }}"
                expirationDateTime: "{{ expirationDateTime }}"
                recordedDateTime: "{{ recordedDateTime }}"
                state: "{{ state }}"
                userDisplayName: "{{ userDisplayName }}"
                userEmail: "{{ userEmail }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
            appRoleAssignments:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                appRoleId: "{{ appRoleId }}"
                createdDateTime: "{{ createdDateTime }}"
                principalDisplayName: "{{ principalDisplayName }}"
                principalId: "{{ principalId }}"
                principalType: "{{ principalType }}"
                resourceDisplayName: "{{ resourceDisplayName }}"
                resourceId: "{{ resourceId }}"
            authentication: "{{ authentication }}"
            calendar: "{{ calendar }}"
            calendarGroups:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                changeKey: "{{ changeKey }}"
                classId: "{{ classId }}"
                name: "{{ name }}"
                calendars: "{{ calendars }}"
            calendars:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
                canEdit: {{ canEdit }}
                canShare: {{ canShare }}
                canViewPrivateItems: {{ canViewPrivateItems }}
                changeKey: "{{ changeKey }}"
                color: "{{ color }}"
                defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
                hexColor: "{{ hexColor }}"
                isDefaultCalendar: {{ isDefaultCalendar }}
                isRemovable: {{ isRemovable }}
                isTallyingResponses: {{ isTallyingResponses }}
                name: "{{ name }}"
                owner: "{{ owner }}"
                calendarPermissions: "{{ calendarPermissions }}"
                calendarView: "{{ calendarView }}"
                events: "{{ events }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            calendarView:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            chats:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                chatType: "{{ chatType }}"
                createdDateTime: "{{ createdDateTime }}"
                isHiddenForAllMembers: {{ isHiddenForAllMembers }}
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                migrationMode: "{{ migrationMode }}"
                onlineMeetingInfo: "{{ onlineMeetingInfo }}"
                originalCreatedDateTime: "{{ originalCreatedDateTime }}"
                tenantId: "{{ tenantId }}"
                topic: "{{ topic }}"
                viewpoint: "{{ viewpoint }}"
                webUrl: "{{ webUrl }}"
                installedApps: "{{ installedApps }}"
                lastMessagePreview: "{{ lastMessagePreview }}"
                members: "{{ members }}"
                messages: "{{ messages }}"
                permissionGrants: "{{ permissionGrants }}"
                pinnedMessages: "{{ pinnedMessages }}"
                tabs: "{{ tabs }}"
            cloudClipboard: "{{ cloudClipboard }}"
            cloudPCs:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                aadDeviceId: "{{ aadDeviceId }}"
                displayName: "{{ displayName }}"
                gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
                imageDisplayName: "{{ imageDisplayName }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                managedDeviceId: "{{ managedDeviceId }}"
                managedDeviceName: "{{ managedDeviceName }}"
                onPremisesConnectionName: "{{ onPremisesConnectionName }}"
                provisioningPolicyId: "{{ provisioningPolicyId }}"
                provisioningPolicyName: "{{ provisioningPolicyName }}"
                provisioningType: "{{ provisioningType }}"
                servicePlanId: "{{ servicePlanId }}"
                servicePlanName: "{{ servicePlanName }}"
                userPrincipalName: "{{ userPrincipalName }}"
            contactFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                displayName: "{{ displayName }}"
                parentFolderId: "{{ parentFolderId }}"
                childFolders: "{{ childFolders }}"
                contacts: "{{ contacts }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            contacts:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                assistantName: "{{ assistantName }}"
                birthday: "{{ birthday }}"
                businessAddress: "{{ businessAddress }}"
                businessHomePage: "{{ businessHomePage }}"
                businessPhones: "{{ businessPhones }}"
                children: "{{ children }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                emailAddresses: "{{ emailAddresses }}"
                fileAs: "{{ fileAs }}"
                generation: "{{ generation }}"
                givenName: "{{ givenName }}"
                homeAddress: "{{ homeAddress }}"
                homePhones: "{{ homePhones }}"
                imAddresses: "{{ imAddresses }}"
                initials: "{{ initials }}"
                jobTitle: "{{ jobTitle }}"
                manager: "{{ manager }}"
                middleName: "{{ middleName }}"
                mobilePhone: "{{ mobilePhone }}"
                nickName: "{{ nickName }}"
                officeLocation: "{{ officeLocation }}"
                otherAddress: "{{ otherAddress }}"
                parentFolderId: "{{ parentFolderId }}"
                personalNotes: "{{ personalNotes }}"
                primaryEmailAddress: "{{ primaryEmailAddress }}"
                profession: "{{ profession }}"
                secondaryEmailAddress: "{{ secondaryEmailAddress }}"
                spouseName: "{{ spouseName }}"
                surname: "{{ surname }}"
                tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
                title: "{{ title }}"
                yomiCompanyName: "{{ yomiCompanyName }}"
                yomiGivenName: "{{ yomiGivenName }}"
                yomiSurname: "{{ yomiSurname }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                photo: "{{ photo }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            createdObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
            deviceManagementTroubleshootingEvents:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                correlationId: "{{ correlationId }}"
                eventDateTime: "{{ eventDateTime }}"
            directReports:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            drive: "{{ drive }}"
            drives:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                driveType: "{{ driveType }}"
                owner: "{{ owner }}"
                quota: "{{ quota }}"
                sharePointIds: "{{ sharePointIds }}"
                system: "{{ system }}"
                bundles: "{{ bundles }}"
                following: "{{ following }}"
                items: "{{ items }}"
                list: "{{ list }}"
                root: "{{ root }}"
                special: "{{ special }}"
            employeeExperience: "{{ employeeExperience }}"
            events:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            extensions:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
            followedSites:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                displayName: "{{ displayName }}"
                error: "{{ error }}"
                isPersonalSite: {{ isPersonalSite }}
                root: "{{ root }}"
                sharepointIds: "{{ sharepointIds }}"
                siteCollection: "{{ siteCollection }}"
                analytics: "{{ analytics }}"
                columns: "{{ columns }}"
                contentTypes: "{{ contentTypes }}"
                drive: "{{ drive }}"
                drives: "{{ drives }}"
                externalColumns: "{{ externalColumns }}"
                items: "{{ items }}"
                lists: "{{ lists }}"
                onenote: "{{ onenote }}"
                operations: "{{ operations }}"
                pages: "{{ pages }}"
                permissions: "{{ permissions }}"
                sites: "{{ sites }}"
                termStore: "{{ termStore }}"
                termStores: "{{ termStores }}"
            inferenceClassification: "{{ inferenceClassification }}"
            insights: "{{ insights }}"
            joinedTeams:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                classification: "{{ classification }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                displayName: "{{ displayName }}"
                firstChannelName: "{{ firstChannelName }}"
                funSettings: "{{ funSettings }}"
                guestSettings: "{{ guestSettings }}"
                internalId: "{{ internalId }}"
                isArchived: {{ isArchived }}
                memberSettings: "{{ memberSettings }}"
                messagingSettings: "{{ messagingSettings }}"
                specialization: "{{ specialization }}"
                summary: "{{ summary }}"
                tenantId: "{{ tenantId }}"
                visibility: "{{ visibility }}"
                webUrl: "{{ webUrl }}"
                allChannels: "{{ allChannels }}"
                channels: "{{ channels }}"
                group: "{{ group }}"
                incomingChannels: "{{ incomingChannels }}"
                installedApps: "{{ installedApps }}"
                members: "{{ members }}"
                operations: "{{ operations }}"
                permissionGrants: "{{ permissionGrants }}"
                photo: "{{ photo }}"
                primaryChannel: "{{ primaryChannel }}"
                schedule: "{{ schedule }}"
                tags: "{{ tags }}"
                template: "{{ template }}"
            licenseDetails:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                servicePlans: "{{ servicePlans }}"
                skuId: "{{ skuId }}"
                skuPartNumber: "{{ skuPartNumber }}"
            mailFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                childFolderCount: {{ childFolderCount }}
                displayName: "{{ displayName }}"
                isHidden: {{ isHidden }}
                parentFolderId: "{{ parentFolderId }}"
                totalItemCount: {{ totalItemCount }}
                unreadItemCount: {{ unreadItemCount }}
                childFolders: "{{ childFolders }}"
                messageRules: "{{ messageRules }}"
                messages: "{{ messages }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            managedAppRegistrations:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                appIdentifier: "{{ appIdentifier }}"
                applicationVersion: "{{ applicationVersion }}"
                createdDateTime: "{{ createdDateTime }}"
                deviceName: "{{ deviceName }}"
                deviceTag: "{{ deviceTag }}"
                deviceType: "{{ deviceType }}"
                flaggedReasons: "{{ flaggedReasons }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managementSdkVersion: "{{ managementSdkVersion }}"
                platformVersion: "{{ platformVersion }}"
                userId: "{{ userId }}"
                version: "{{ version }}"
                appliedPolicies: "{{ appliedPolicies }}"
                intendedPolicies: "{{ intendedPolicies }}"
                operations: "{{ operations }}"
            managedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationLockBypassCode: "{{ activationLockBypassCode }}"
                androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
                azureADDeviceId: "{{ azureADDeviceId }}"
                azureADRegistered: {{ azureADRegistered }}
                complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
                complianceState: "{{ complianceState }}"
                configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
                deviceActionResults: "{{ deviceActionResults }}"
                deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
                deviceEnrollmentType: "{{ deviceEnrollmentType }}"
                deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
                deviceName: "{{ deviceName }}"
                deviceRegistrationState: "{{ deviceRegistrationState }}"
                easActivated: {{ easActivated }}
                easActivationDateTime: "{{ easActivationDateTime }}"
                easDeviceId: "{{ easDeviceId }}"
                emailAddress: "{{ emailAddress }}"
                enrolledDateTime: "{{ enrolledDateTime }}"
                enrollmentProfileName: "{{ enrollmentProfileName }}"
                ethernetMacAddress: "{{ ethernetMacAddress }}"
                exchangeAccessState: "{{ exchangeAccessState }}"
                exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
                exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
                freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
                iccid: "{{ iccid }}"
                imei: "{{ imei }}"
                isEncrypted: {{ isEncrypted }}
                isSupervised: {{ isSupervised }}
                jailBroken: "{{ jailBroken }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managedDeviceName: "{{ managedDeviceName }}"
                managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
                managementAgent: "{{ managementAgent }}"
                managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
                managementState: "{{ managementState }}"
                manufacturer: "{{ manufacturer }}"
                meid: "{{ meid }}"
                model: "{{ model }}"
                notes: "{{ notes }}"
                operatingSystem: "{{ operatingSystem }}"
                osVersion: "{{ osVersion }}"
                partnerReportedThreatState: "{{ partnerReportedThreatState }}"
                phoneNumber: "{{ phoneNumber }}"
                physicalMemoryInBytes: {{ physicalMemoryInBytes }}
                remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
                remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
                requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
                serialNumber: "{{ serialNumber }}"
                subscriberCarrier: "{{ subscriberCarrier }}"
                totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
                udid: "{{ udid }}"
                userDisplayName: "{{ userDisplayName }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
                wiFiMacAddress: "{{ wiFiMacAddress }}"
                deviceCategory: "{{ deviceCategory }}"
                deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
                deviceConfigurationStates: "{{ deviceConfigurationStates }}"
                logCollectionRequests: "{{ logCollectionRequests }}"
                users: "{{ users }}"
                windowsProtectionState: "{{ windowsProtectionState }}"
            manager: "{{ manager }}"
            memberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            messages:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                bccRecipients: "{{ bccRecipients }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                ccRecipients: "{{ ccRecipients }}"
                conversationId: "{{ conversationId }}"
                conversationIndex: "{{ conversationIndex }}"
                flag: "{{ flag }}"
                from: "{{ from }}"
                hasAttachments: {{ hasAttachments }}
                importance: "{{ importance }}"
                inferenceClassification: "{{ inferenceClassification }}"
                internetMessageHeaders: "{{ internetMessageHeaders }}"
                internetMessageId: "{{ internetMessageId }}"
                isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
                isDraft: {{ isDraft }}
                isRead: {{ isRead }}
                isReadReceiptRequested: {{ isReadReceiptRequested }}
                parentFolderId: "{{ parentFolderId }}"
                receivedDateTime: "{{ receivedDateTime }}"
                replyTo: "{{ replyTo }}"
                sender: "{{ sender }}"
                sentDateTime: "{{ sentDateTime }}"
                subject: "{{ subject }}"
                toRecipients: "{{ toRecipients }}"
                uniqueBody: "{{ uniqueBody }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            oauth2PermissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                clientId: "{{ clientId }}"
                consentType: "{{ consentType }}"
                principalId: "{{ principalId }}"
                resourceId: "{{ resourceId }}"
                scope: "{{ scope }}"
            onenote: "{{ onenote }}"
            onlineMeetings:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
                allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
                allowBreakoutRooms: {{ allowBreakoutRooms }}
                allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
                allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
                allowedPresenters: "{{ allowedPresenters }}"
                allowLiveShare: "{{ allowLiveShare }}"
                allowMeetingChat: "{{ allowMeetingChat }}"
                allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
                allowPowerPointSharing: {{ allowPowerPointSharing }}
                allowRecording: {{ allowRecording }}
                allowTeamworkReactions: {{ allowTeamworkReactions }}
                allowTranscription: {{ allowTranscription }}
                allowWhiteboard: {{ allowWhiteboard }}
                audioConferencing: "{{ audioConferencing }}"
                chatInfo: "{{ chatInfo }}"
                chatRestrictions: "{{ chatRestrictions }}"
                expiryDateTime: "{{ expiryDateTime }}"
                isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
                isEntryExitAnnounced: {{ isEntryExitAnnounced }}
                joinInformation: "{{ joinInformation }}"
                joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
                joinWebUrl: "{{ joinWebUrl }}"
                lobbyBypassSettings: "{{ lobbyBypassSettings }}"
                meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
                meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
                recordAutomatically: {{ recordAutomatically }}
                sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
                shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
                subject: "{{ subject }}"
                videoTeleconferenceId: "{{ videoTeleconferenceId }}"
                watermarkProtection: "{{ watermarkProtection }}"
                attendanceReports: "{{ attendanceReports }}"
                attendeeReport: "{{ attendeeReport }}"
                broadcastSettings: "{{ broadcastSettings }}"
                creationDateTime: "{{ creationDateTime }}"
                endDateTime: "{{ endDateTime }}"
                externalId: "{{ externalId }}"
                isBroadcast: {{ isBroadcast }}
                meetingTemplateId: "{{ meetingTemplateId }}"
                participants: "{{ participants }}"
                startDateTime: "{{ startDateTime }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
            outlook: "{{ outlook }}"
            ownedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            ownedObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            people:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                birthday: "{{ birthday }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                givenName: "{{ givenName }}"
                imAddress: "{{ imAddress }}"
                isFavorite: {{ isFavorite }}
                jobTitle: "{{ jobTitle }}"
                officeLocation: "{{ officeLocation }}"
                personNotes: "{{ personNotes }}"
                personType: "{{ personType }}"
                phones: "{{ phones }}"
                postalAddresses: "{{ postalAddresses }}"
                profession: "{{ profession }}"
                scoredEmailAddresses: "{{ scoredEmailAddresses }}"
                surname: "{{ surname }}"
                userPrincipalName: "{{ userPrincipalName }}"
                websites: "{{ websites }}"
                yomiCompany: "{{ yomiCompany }}"
            permissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                clientAppId: "{{ clientAppId }}"
                clientId: "{{ clientId }}"
                permission: "{{ permission }}"
                permissionType: "{{ permissionType }}"
                resourceAppId: "{{ resourceAppId }}"
            photo: "{{ photo }}"
            photos:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                height: {{ height }}
                width: {{ width }}
            planner: "{{ planner }}"
            presence: "{{ presence }}"
            registeredDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            scopedRoleMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                administrativeUnitId: "{{ administrativeUnitId }}"
                roleId: "{{ roleId }}"
                roleMemberInfo:
                  displayName: "{{ displayName }}"
                  id: "{{ id }}"
                  @odata.type: "{{ @odata.type }}"
            settings: "{{ settings }}"
            solutions: "{{ solutions }}"
            sponsors:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            teamwork: "{{ teamwork }}"
            todo: "{{ todo }}"
            transitiveMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
          taskProcessingResults: "{{ taskProcessingResults }}"
    - name: runs
      description: |
        Workflow runs.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          activatedOnScope: "{{ activatedOnScope }}"
          completedDateTime: "{{ completedDateTime }}"
          failedTasksCount: {{ failedTasksCount }}
          failedUsersCount: {{ failedUsersCount }}
          lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
          processingStatus: "{{ processingStatus }}"
          scheduledDateTime: "{{ scheduledDateTime }}"
          startedDateTime: "{{ startedDateTime }}"
          successfulUsersCount: {{ successfulUsersCount }}
          totalTasksCount: {{ totalTasksCount }}
          totalUnprocessedTasksCount: {{ totalUnprocessedTasksCount }}
          totalUsersCount: {{ totalUsersCount }}
          workflowExecutionType: "{{ workflowExecutionType }}"
          reprocessedRuns: "{{ reprocessedRuns }}"
          taskProcessingResults: "{{ taskProcessingResults }}"
          userProcessingResults: "{{ userProcessingResults }}"
    - name: taskReports
      description: |
        Represents the aggregation of task execution data for tasks within a workflow object.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          completedDateTime: "{{ completedDateTime }}"
          failedUsersCount: {{ failedUsersCount }}
          lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
          processingStatus: "{{ processingStatus }}"
          runId: "{{ runId }}"
          startedDateTime: "{{ startedDateTime }}"
          successfulUsersCount: {{ successfulUsersCount }}
          totalUsersCount: {{ totalUsersCount }}
          unprocessedUsersCount: {{ unprocessedUsersCount }}
          task:
            id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            arguments:
              - name: "{{ name }}"
                value: "{{ value }}"
                @odata.type: "{{ @odata.type }}"
            category: "{{ category }}"
            continueOnError: {{ continueOnError }}
            description: "{{ description }}"
            displayName: "{{ displayName }}"
            executionSequence: {{ executionSequence }}
            isEnabled: {{ isEnabled }}
            taskDefinitionId: "{{ taskDefinitionId }}"
            taskProcessingResults:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                completedDateTime: "{{ completedDateTime }}"
                createdDateTime: "{{ createdDateTime }}"
                failureReason: "{{ failureReason }}"
                processingInfo: "{{ processingInfo }}"
                processingStatus: "{{ processingStatus }}"
                startedDateTime: "{{ startedDateTime }}"
                subject:
                  id: "{{ id }}"
                  @odata.type: "{{ @odata.type }}"
                  deletedDateTime: "{{ deletedDateTime }}"
                  aboutMe: "{{ aboutMe }}"
                  accountEnabled: {{ accountEnabled }}
                  ageGroup: "{{ ageGroup }}"
                  assignedLicenses:
                    - disabledPlans: "{{ disabledPlans }}"
                      skuId: "{{ skuId }}"
                      @odata.type: "{{ @odata.type }}"
                  assignedPlans:
                    - assignedDateTime: "{{ assignedDateTime }}"
                      capabilityStatus: "{{ capabilityStatus }}"
                      service: "{{ service }}"
                      servicePlanId: "{{ servicePlanId }}"
                      @odata.type: "{{ @odata.type }}"
                  authorizationInfo: "{{ authorizationInfo }}"
                  birthday: "{{ birthday }}"
                  businessPhones:
                    - "{{ businessPhones }}"
                  city: "{{ city }}"
                  companyName: "{{ companyName }}"
                  consentProvidedForMinor: "{{ consentProvidedForMinor }}"
                  country: "{{ country }}"
                  createdDateTime: "{{ createdDateTime }}"
                  creationType: "{{ creationType }}"
                  customSecurityAttributes: "{{ customSecurityAttributes }}"
                  department: "{{ department }}"
                  deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
                  displayName: "{{ displayName }}"
                  employeeHireDate: "{{ employeeHireDate }}"
                  employeeId: "{{ employeeId }}"
                  employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
                  employeeOrgData: "{{ employeeOrgData }}"
                  employeeType: "{{ employeeType }}"
                  externalUserState: "{{ externalUserState }}"
                  externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
                  faxNumber: "{{ faxNumber }}"
                  givenName: "{{ givenName }}"
                  hireDate: "{{ hireDate }}"
                  identities:
                    - issuer: "{{ issuer }}"
                      issuerAssignedId: "{{ issuerAssignedId }}"
                      signInType: "{{ signInType }}"
                      @odata.type: "{{ @odata.type }}"
                  identityParentId: "{{ identityParentId }}"
                  imAddresses:
                    - "{{ imAddresses }}"
                  interests:
                    - "{{ interests }}"
                  isManagementRestricted: {{ isManagementRestricted }}
                  isResourceAccount: {{ isResourceAccount }}
                  jobTitle: "{{ jobTitle }}"
                  lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
                  legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
                  licenseAssignmentStates:
                    - assignedByGroup: "{{ assignedByGroup }}"
                      disabledPlans: "{{ disabledPlans }}"
                      error: "{{ error }}"
                      lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                      skuId: "{{ skuId }}"
                      state: "{{ state }}"
                      @odata.type: "{{ @odata.type }}"
                  mail: "{{ mail }}"
                  mailboxSettings: "{{ mailboxSettings }}"
                  mailNickname: "{{ mailNickname }}"
                  mobilePhone: "{{ mobilePhone }}"
                  mySite: "{{ mySite }}"
                  officeLocation: "{{ officeLocation }}"
                  onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
                  onPremisesDomainName: "{{ onPremisesDomainName }}"
                  onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
                  onPremisesImmutableId: "{{ onPremisesImmutableId }}"
                  onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
                  onPremisesProvisioningErrors:
                    - category: "{{ category }}"
                      occurredDateTime: "{{ occurredDateTime }}"
                      propertyCausingError: "{{ propertyCausingError }}"
                      value: "{{ value }}"
                      @odata.type: "{{ @odata.type }}"
                  onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
                  onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
                  onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
                  onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
                  otherMails:
                    - "{{ otherMails }}"
                  passwordPolicies: "{{ passwordPolicies }}"
                  passwordProfile: "{{ passwordProfile }}"
                  pastProjects:
                    - "{{ pastProjects }}"
                  postalCode: "{{ postalCode }}"
                  preferredDataLocation: "{{ preferredDataLocation }}"
                  preferredLanguage: "{{ preferredLanguage }}"
                  preferredName: "{{ preferredName }}"
                  print: "{{ print }}"
                  provisionedPlans:
                    - capabilityStatus: "{{ capabilityStatus }}"
                      provisioningStatus: "{{ provisioningStatus }}"
                      service: "{{ service }}"
                      @odata.type: "{{ @odata.type }}"
                  proxyAddresses:
                    - "{{ proxyAddresses }}"
                  responsibilities:
                    - "{{ responsibilities }}"
                  schools:
                    - "{{ schools }}"
                  securityIdentifier: "{{ securityIdentifier }}"
                  serviceProvisioningErrors:
                    - createdDateTime: "{{ createdDateTime }}"
                      isResolved: {{ isResolved }}
                      serviceInstance: "{{ serviceInstance }}"
                      @odata.type: "{{ @odata.type }}"
                  showInAddressList: {{ showInAddressList }}
                  signInActivity: "{{ signInActivity }}"
                  signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
                  skills:
                    - "{{ skills }}"
                  state: "{{ state }}"
                  streetAddress: "{{ streetAddress }}"
                  surname: "{{ surname }}"
                  usageLocation: "{{ usageLocation }}"
                  userPrincipalName: "{{ userPrincipalName }}"
                  userType: "{{ userType }}"
                  activities:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      activationUrl: "{{ activationUrl }}"
                      activitySourceHost: "{{ activitySourceHost }}"
                      appActivityId: "{{ appActivityId }}"
                      appDisplayName: "{{ appDisplayName }}"
                      contentInfo: "{{ contentInfo }}"
                      contentUrl: "{{ contentUrl }}"
                      createdDateTime: "{{ createdDateTime }}"
                      expirationDateTime: "{{ expirationDateTime }}"
                      fallbackUrl: "{{ fallbackUrl }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      status: "{{ status }}"
                      userTimezone: "{{ userTimezone }}"
                      visualElements:
                        attribution: "{{ attribution }}"
                        backgroundColor: "{{ backgroundColor }}"
                        content: "{{ content }}"
                        description: "{{ description }}"
                        displayText: "{{ displayText }}"
                        @odata.type: "{{ @odata.type }}"
                      historyItems: "{{ historyItems }}"
                  adhocCalls:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      recordings: "{{ recordings }}"
                      transcripts: "{{ transcripts }}"
                  agreementAcceptances:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      agreementFileId: "{{ agreementFileId }}"
                      agreementId: "{{ agreementId }}"
                      deviceDisplayName: "{{ deviceDisplayName }}"
                      deviceId: "{{ deviceId }}"
                      deviceOSType: "{{ deviceOSType }}"
                      deviceOSVersion: "{{ deviceOSVersion }}"
                      expirationDateTime: "{{ expirationDateTime }}"
                      recordedDateTime: "{{ recordedDateTime }}"
                      state: "{{ state }}"
                      userDisplayName: "{{ userDisplayName }}"
                      userEmail: "{{ userEmail }}"
                      userId: "{{ userId }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                  appRoleAssignments:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                      appRoleId: "{{ appRoleId }}"
                      createdDateTime: "{{ createdDateTime }}"
                      principalDisplayName: "{{ principalDisplayName }}"
                      principalId: "{{ principalId }}"
                      principalType: "{{ principalType }}"
                      resourceDisplayName: "{{ resourceDisplayName }}"
                      resourceId: "{{ resourceId }}"
                  authentication: "{{ authentication }}"
                  calendar: "{{ calendar }}"
                  calendarGroups:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      changeKey: "{{ changeKey }}"
                      classId: "{{ classId }}"
                      name: "{{ name }}"
                      calendars: "{{ calendars }}"
                  calendars:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
                      canEdit: {{ canEdit }}
                      canShare: {{ canShare }}
                      canViewPrivateItems: {{ canViewPrivateItems }}
                      changeKey: "{{ changeKey }}"
                      color: "{{ color }}"
                      defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
                      hexColor: "{{ hexColor }}"
                      isDefaultCalendar: {{ isDefaultCalendar }}
                      isRemovable: {{ isRemovable }}
                      isTallyingResponses: {{ isTallyingResponses }}
                      name: "{{ name }}"
                      owner: "{{ owner }}"
                      calendarPermissions: "{{ calendarPermissions }}"
                      calendarView: "{{ calendarView }}"
                      events: "{{ events }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  calendarView:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      allowNewTimeProposals: {{ allowNewTimeProposals }}
                      attendees: "{{ attendees }}"
                      body: "{{ body }}"
                      bodyPreview: "{{ bodyPreview }}"
                      cancelledOccurrences: "{{ cancelledOccurrences }}"
                      end: "{{ end }}"
                      hasAttachments: {{ hasAttachments }}
                      hideAttendees: {{ hideAttendees }}
                      iCalUId: "{{ iCalUId }}"
                      importance: "{{ importance }}"
                      isAllDay: {{ isAllDay }}
                      isCancelled: {{ isCancelled }}
                      isDraft: {{ isDraft }}
                      isOnlineMeeting: {{ isOnlineMeeting }}
                      isOrganizer: {{ isOrganizer }}
                      isReminderOn: {{ isReminderOn }}
                      location: "{{ location }}"
                      locations: "{{ locations }}"
                      onlineMeeting: "{{ onlineMeeting }}"
                      onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                      onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                      organizer: "{{ organizer }}"
                      originalEndTimeZone: "{{ originalEndTimeZone }}"
                      originalStart: "{{ originalStart }}"
                      originalStartTimeZone: "{{ originalStartTimeZone }}"
                      recurrence: "{{ recurrence }}"
                      reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                      responseRequested: {{ responseRequested }}
                      responseStatus: "{{ responseStatus }}"
                      sensitivity: "{{ sensitivity }}"
                      seriesMasterId: "{{ seriesMasterId }}"
                      showAs: "{{ showAs }}"
                      start: "{{ start }}"
                      subject: "{{ subject }}"
                      transactionId: "{{ transactionId }}"
                      type: "{{ type }}"
                      webLink: "{{ webLink }}"
                      attachments: "{{ attachments }}"
                      calendar: "{{ calendar }}"
                      exceptionOccurrences: "{{ exceptionOccurrences }}"
                      extensions: "{{ extensions }}"
                      instances: "{{ instances }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  chats:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      chatType: "{{ chatType }}"
                      createdDateTime: "{{ createdDateTime }}"
                      isHiddenForAllMembers: {{ isHiddenForAllMembers }}
                      lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                      migrationMode: "{{ migrationMode }}"
                      onlineMeetingInfo: "{{ onlineMeetingInfo }}"
                      originalCreatedDateTime: "{{ originalCreatedDateTime }}"
                      tenantId: "{{ tenantId }}"
                      topic: "{{ topic }}"
                      viewpoint: "{{ viewpoint }}"
                      webUrl: "{{ webUrl }}"
                      installedApps: "{{ installedApps }}"
                      lastMessagePreview: "{{ lastMessagePreview }}"
                      members: "{{ members }}"
                      messages: "{{ messages }}"
                      permissionGrants: "{{ permissionGrants }}"
                      pinnedMessages: "{{ pinnedMessages }}"
                      tabs: "{{ tabs }}"
                  cloudClipboard: "{{ cloudClipboard }}"
                  cloudPCs:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      aadDeviceId: "{{ aadDeviceId }}"
                      displayName: "{{ displayName }}"
                      gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
                      imageDisplayName: "{{ imageDisplayName }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      managedDeviceId: "{{ managedDeviceId }}"
                      managedDeviceName: "{{ managedDeviceName }}"
                      onPremisesConnectionName: "{{ onPremisesConnectionName }}"
                      provisioningPolicyId: "{{ provisioningPolicyId }}"
                      provisioningPolicyName: "{{ provisioningPolicyName }}"
                      provisioningType: "{{ provisioningType }}"
                      servicePlanId: "{{ servicePlanId }}"
                      servicePlanName: "{{ servicePlanName }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                  contactFolders:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      displayName: "{{ displayName }}"
                      parentFolderId: "{{ parentFolderId }}"
                      childFolders: "{{ childFolders }}"
                      contacts: "{{ contacts }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  contacts:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      assistantName: "{{ assistantName }}"
                      birthday: "{{ birthday }}"
                      businessAddress: "{{ businessAddress }}"
                      businessHomePage: "{{ businessHomePage }}"
                      businessPhones: "{{ businessPhones }}"
                      children: "{{ children }}"
                      companyName: "{{ companyName }}"
                      department: "{{ department }}"
                      displayName: "{{ displayName }}"
                      emailAddresses: "{{ emailAddresses }}"
                      fileAs: "{{ fileAs }}"
                      generation: "{{ generation }}"
                      givenName: "{{ givenName }}"
                      homeAddress: "{{ homeAddress }}"
                      homePhones: "{{ homePhones }}"
                      imAddresses: "{{ imAddresses }}"
                      initials: "{{ initials }}"
                      jobTitle: "{{ jobTitle }}"
                      manager: "{{ manager }}"
                      middleName: "{{ middleName }}"
                      mobilePhone: "{{ mobilePhone }}"
                      nickName: "{{ nickName }}"
                      officeLocation: "{{ officeLocation }}"
                      otherAddress: "{{ otherAddress }}"
                      parentFolderId: "{{ parentFolderId }}"
                      personalNotes: "{{ personalNotes }}"
                      primaryEmailAddress: "{{ primaryEmailAddress }}"
                      profession: "{{ profession }}"
                      secondaryEmailAddress: "{{ secondaryEmailAddress }}"
                      spouseName: "{{ spouseName }}"
                      surname: "{{ surname }}"
                      tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
                      title: "{{ title }}"
                      yomiCompanyName: "{{ yomiCompanyName }}"
                      yomiGivenName: "{{ yomiGivenName }}"
                      yomiSurname: "{{ yomiSurname }}"
                      extensions: "{{ extensions }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      photo: "{{ photo }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  createdObjects:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
                  deviceManagementTroubleshootingEvents:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      correlationId: "{{ correlationId }}"
                      eventDateTime: "{{ eventDateTime }}"
                  directReports:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  drive: "{{ drive }}"
                  drives:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      createdBy: "{{ createdBy }}"
                      createdDateTime: "{{ createdDateTime }}"
                      description: "{{ description }}"
                      eTag: "{{ eTag }}"
                      lastModifiedBy: "{{ lastModifiedBy }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      name: "{{ name }}"
                      parentReference: "{{ parentReference }}"
                      webUrl: "{{ webUrl }}"
                      createdByUser: "{{ createdByUser }}"
                      lastModifiedByUser: "{{ lastModifiedByUser }}"
                      driveType: "{{ driveType }}"
                      owner: "{{ owner }}"
                      quota: "{{ quota }}"
                      sharePointIds: "{{ sharePointIds }}"
                      system: "{{ system }}"
                      bundles: "{{ bundles }}"
                      following: "{{ following }}"
                      items: "{{ items }}"
                      list: "{{ list }}"
                      root: "{{ root }}"
                      special: "{{ special }}"
                  employeeExperience: "{{ employeeExperience }}"
                  events:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      allowNewTimeProposals: {{ allowNewTimeProposals }}
                      attendees: "{{ attendees }}"
                      body: "{{ body }}"
                      bodyPreview: "{{ bodyPreview }}"
                      cancelledOccurrences: "{{ cancelledOccurrences }}"
                      end: "{{ end }}"
                      hasAttachments: {{ hasAttachments }}
                      hideAttendees: {{ hideAttendees }}
                      iCalUId: "{{ iCalUId }}"
                      importance: "{{ importance }}"
                      isAllDay: {{ isAllDay }}
                      isCancelled: {{ isCancelled }}
                      isDraft: {{ isDraft }}
                      isOnlineMeeting: {{ isOnlineMeeting }}
                      isOrganizer: {{ isOrganizer }}
                      isReminderOn: {{ isReminderOn }}
                      location: "{{ location }}"
                      locations: "{{ locations }}"
                      onlineMeeting: "{{ onlineMeeting }}"
                      onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                      onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                      organizer: "{{ organizer }}"
                      originalEndTimeZone: "{{ originalEndTimeZone }}"
                      originalStart: "{{ originalStart }}"
                      originalStartTimeZone: "{{ originalStartTimeZone }}"
                      recurrence: "{{ recurrence }}"
                      reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                      responseRequested: {{ responseRequested }}
                      responseStatus: "{{ responseStatus }}"
                      sensitivity: "{{ sensitivity }}"
                      seriesMasterId: "{{ seriesMasterId }}"
                      showAs: "{{ showAs }}"
                      start: "{{ start }}"
                      subject: "{{ subject }}"
                      transactionId: "{{ transactionId }}"
                      type: "{{ type }}"
                      webLink: "{{ webLink }}"
                      attachments: "{{ attachments }}"
                      calendar: "{{ calendar }}"
                      exceptionOccurrences: "{{ exceptionOccurrences }}"
                      extensions: "{{ extensions }}"
                      instances: "{{ instances }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  extensions:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                  followedSites:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      createdBy: "{{ createdBy }}"
                      createdDateTime: "{{ createdDateTime }}"
                      description: "{{ description }}"
                      eTag: "{{ eTag }}"
                      lastModifiedBy: "{{ lastModifiedBy }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      name: "{{ name }}"
                      parentReference: "{{ parentReference }}"
                      webUrl: "{{ webUrl }}"
                      createdByUser: "{{ createdByUser }}"
                      lastModifiedByUser: "{{ lastModifiedByUser }}"
                      displayName: "{{ displayName }}"
                      error: "{{ error }}"
                      isPersonalSite: {{ isPersonalSite }}
                      root: "{{ root }}"
                      sharepointIds: "{{ sharepointIds }}"
                      siteCollection: "{{ siteCollection }}"
                      analytics: "{{ analytics }}"
                      columns: "{{ columns }}"
                      contentTypes: "{{ contentTypes }}"
                      drive: "{{ drive }}"
                      drives: "{{ drives }}"
                      externalColumns: "{{ externalColumns }}"
                      items: "{{ items }}"
                      lists: "{{ lists }}"
                      onenote: "{{ onenote }}"
                      operations: "{{ operations }}"
                      pages: "{{ pages }}"
                      permissions: "{{ permissions }}"
                      sites: "{{ sites }}"
                      termStore: "{{ termStore }}"
                      termStores: "{{ termStores }}"
                  inferenceClassification: "{{ inferenceClassification }}"
                  insights: "{{ insights }}"
                  joinedTeams:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      classification: "{{ classification }}"
                      createdDateTime: "{{ createdDateTime }}"
                      description: "{{ description }}"
                      displayName: "{{ displayName }}"
                      firstChannelName: "{{ firstChannelName }}"
                      funSettings: "{{ funSettings }}"
                      guestSettings: "{{ guestSettings }}"
                      internalId: "{{ internalId }}"
                      isArchived: {{ isArchived }}
                      memberSettings: "{{ memberSettings }}"
                      messagingSettings: "{{ messagingSettings }}"
                      specialization: "{{ specialization }}"
                      summary: "{{ summary }}"
                      tenantId: "{{ tenantId }}"
                      visibility: "{{ visibility }}"
                      webUrl: "{{ webUrl }}"
                      allChannels: "{{ allChannels }}"
                      channels: "{{ channels }}"
                      group: "{{ group }}"
                      incomingChannels: "{{ incomingChannels }}"
                      installedApps: "{{ installedApps }}"
                      members: "{{ members }}"
                      operations: "{{ operations }}"
                      permissionGrants: "{{ permissionGrants }}"
                      photo: "{{ photo }}"
                      primaryChannel: "{{ primaryChannel }}"
                      schedule: "{{ schedule }}"
                      tags: "{{ tags }}"
                      template: "{{ template }}"
                  licenseDetails:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      servicePlans: "{{ servicePlans }}"
                      skuId: "{{ skuId }}"
                      skuPartNumber: "{{ skuPartNumber }}"
                  mailFolders:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      childFolderCount: {{ childFolderCount }}
                      displayName: "{{ displayName }}"
                      isHidden: {{ isHidden }}
                      parentFolderId: "{{ parentFolderId }}"
                      totalItemCount: {{ totalItemCount }}
                      unreadItemCount: {{ unreadItemCount }}
                      childFolders: "{{ childFolders }}"
                      messageRules: "{{ messageRules }}"
                      messages: "{{ messages }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  managedAppRegistrations:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      appIdentifier: "{{ appIdentifier }}"
                      applicationVersion: "{{ applicationVersion }}"
                      createdDateTime: "{{ createdDateTime }}"
                      deviceName: "{{ deviceName }}"
                      deviceTag: "{{ deviceTag }}"
                      deviceType: "{{ deviceType }}"
                      flaggedReasons: "{{ flaggedReasons }}"
                      lastSyncDateTime: "{{ lastSyncDateTime }}"
                      managementSdkVersion: "{{ managementSdkVersion }}"
                      platformVersion: "{{ platformVersion }}"
                      userId: "{{ userId }}"
                      version: "{{ version }}"
                      appliedPolicies: "{{ appliedPolicies }}"
                      intendedPolicies: "{{ intendedPolicies }}"
                      operations: "{{ operations }}"
                  managedDevices:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      activationLockBypassCode: "{{ activationLockBypassCode }}"
                      androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
                      azureADDeviceId: "{{ azureADDeviceId }}"
                      azureADRegistered: {{ azureADRegistered }}
                      complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
                      complianceState: "{{ complianceState }}"
                      configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
                      deviceActionResults: "{{ deviceActionResults }}"
                      deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
                      deviceEnrollmentType: "{{ deviceEnrollmentType }}"
                      deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
                      deviceName: "{{ deviceName }}"
                      deviceRegistrationState: "{{ deviceRegistrationState }}"
                      easActivated: {{ easActivated }}
                      easActivationDateTime: "{{ easActivationDateTime }}"
                      easDeviceId: "{{ easDeviceId }}"
                      emailAddress: "{{ emailAddress }}"
                      enrolledDateTime: "{{ enrolledDateTime }}"
                      enrollmentProfileName: "{{ enrollmentProfileName }}"
                      ethernetMacAddress: "{{ ethernetMacAddress }}"
                      exchangeAccessState: "{{ exchangeAccessState }}"
                      exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
                      exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
                      freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
                      iccid: "{{ iccid }}"
                      imei: "{{ imei }}"
                      isEncrypted: {{ isEncrypted }}
                      isSupervised: {{ isSupervised }}
                      jailBroken: "{{ jailBroken }}"
                      lastSyncDateTime: "{{ lastSyncDateTime }}"
                      managedDeviceName: "{{ managedDeviceName }}"
                      managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
                      managementAgent: "{{ managementAgent }}"
                      managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
                      managementState: "{{ managementState }}"
                      manufacturer: "{{ manufacturer }}"
                      meid: "{{ meid }}"
                      model: "{{ model }}"
                      notes: "{{ notes }}"
                      operatingSystem: "{{ operatingSystem }}"
                      osVersion: "{{ osVersion }}"
                      partnerReportedThreatState: "{{ partnerReportedThreatState }}"
                      phoneNumber: "{{ phoneNumber }}"
                      physicalMemoryInBytes: {{ physicalMemoryInBytes }}
                      remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
                      remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
                      requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
                      serialNumber: "{{ serialNumber }}"
                      subscriberCarrier: "{{ subscriberCarrier }}"
                      totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
                      udid: "{{ udid }}"
                      userDisplayName: "{{ userDisplayName }}"
                      userId: "{{ userId }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                      wiFiMacAddress: "{{ wiFiMacAddress }}"
                      deviceCategory: "{{ deviceCategory }}"
                      deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
                      deviceConfigurationStates: "{{ deviceConfigurationStates }}"
                      logCollectionRequests: "{{ logCollectionRequests }}"
                      users: "{{ users }}"
                      windowsProtectionState: "{{ windowsProtectionState }}"
                  manager: "{{ manager }}"
                  memberOf:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  messages:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      bccRecipients: "{{ bccRecipients }}"
                      body: "{{ body }}"
                      bodyPreview: "{{ bodyPreview }}"
                      ccRecipients: "{{ ccRecipients }}"
                      conversationId: "{{ conversationId }}"
                      conversationIndex: "{{ conversationIndex }}"
                      flag: "{{ flag }}"
                      from: "{{ from }}"
                      hasAttachments: {{ hasAttachments }}
                      importance: "{{ importance }}"
                      inferenceClassification: "{{ inferenceClassification }}"
                      internetMessageHeaders: "{{ internetMessageHeaders }}"
                      internetMessageId: "{{ internetMessageId }}"
                      isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
                      isDraft: {{ isDraft }}
                      isRead: {{ isRead }}
                      isReadReceiptRequested: {{ isReadReceiptRequested }}
                      parentFolderId: "{{ parentFolderId }}"
                      receivedDateTime: "{{ receivedDateTime }}"
                      replyTo: "{{ replyTo }}"
                      sender: "{{ sender }}"
                      sentDateTime: "{{ sentDateTime }}"
                      subject: "{{ subject }}"
                      toRecipients: "{{ toRecipients }}"
                      uniqueBody: "{{ uniqueBody }}"
                      webLink: "{{ webLink }}"
                      attachments: "{{ attachments }}"
                      extensions: "{{ extensions }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  oauth2PermissionGrants:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      clientId: "{{ clientId }}"
                      consentType: "{{ consentType }}"
                      principalId: "{{ principalId }}"
                      resourceId: "{{ resourceId }}"
                      scope: "{{ scope }}"
                  onenote: "{{ onenote }}"
                  onlineMeetings:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
                      allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
                      allowBreakoutRooms: {{ allowBreakoutRooms }}
                      allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
                      allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
                      allowedPresenters: "{{ allowedPresenters }}"
                      allowLiveShare: "{{ allowLiveShare }}"
                      allowMeetingChat: "{{ allowMeetingChat }}"
                      allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
                      allowPowerPointSharing: {{ allowPowerPointSharing }}
                      allowRecording: {{ allowRecording }}
                      allowTeamworkReactions: {{ allowTeamworkReactions }}
                      allowTranscription: {{ allowTranscription }}
                      allowWhiteboard: {{ allowWhiteboard }}
                      audioConferencing: "{{ audioConferencing }}"
                      chatInfo: "{{ chatInfo }}"
                      chatRestrictions: "{{ chatRestrictions }}"
                      expiryDateTime: "{{ expiryDateTime }}"
                      isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
                      isEntryExitAnnounced: {{ isEntryExitAnnounced }}
                      joinInformation: "{{ joinInformation }}"
                      joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
                      joinWebUrl: "{{ joinWebUrl }}"
                      lobbyBypassSettings: "{{ lobbyBypassSettings }}"
                      meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
                      meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
                      recordAutomatically: {{ recordAutomatically }}
                      sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
                      shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
                      subject: "{{ subject }}"
                      videoTeleconferenceId: "{{ videoTeleconferenceId }}"
                      watermarkProtection: "{{ watermarkProtection }}"
                      attendanceReports: "{{ attendanceReports }}"
                      attendeeReport: "{{ attendeeReport }}"
                      broadcastSettings: "{{ broadcastSettings }}"
                      creationDateTime: "{{ creationDateTime }}"
                      endDateTime: "{{ endDateTime }}"
                      externalId: "{{ externalId }}"
                      isBroadcast: {{ isBroadcast }}
                      meetingTemplateId: "{{ meetingTemplateId }}"
                      participants: "{{ participants }}"
                      startDateTime: "{{ startDateTime }}"
                      recordings: "{{ recordings }}"
                      transcripts: "{{ transcripts }}"
                  onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
                  outlook: "{{ outlook }}"
                  ownedDevices:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  ownedObjects:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  people:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      birthday: "{{ birthday }}"
                      companyName: "{{ companyName }}"
                      department: "{{ department }}"
                      displayName: "{{ displayName }}"
                      givenName: "{{ givenName }}"
                      imAddress: "{{ imAddress }}"
                      isFavorite: {{ isFavorite }}
                      jobTitle: "{{ jobTitle }}"
                      officeLocation: "{{ officeLocation }}"
                      personNotes: "{{ personNotes }}"
                      personType: "{{ personType }}"
                      phones: "{{ phones }}"
                      postalAddresses: "{{ postalAddresses }}"
                      profession: "{{ profession }}"
                      scoredEmailAddresses: "{{ scoredEmailAddresses }}"
                      surname: "{{ surname }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                      websites: "{{ websites }}"
                      yomiCompany: "{{ yomiCompany }}"
                  permissionGrants:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                      clientAppId: "{{ clientAppId }}"
                      clientId: "{{ clientId }}"
                      permission: "{{ permission }}"
                      permissionType: "{{ permissionType }}"
                      resourceAppId: "{{ resourceAppId }}"
                  photo: "{{ photo }}"
                  photos:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      height: {{ height }}
                      width: {{ width }}
                  planner: "{{ planner }}"
                  presence: "{{ presence }}"
                  registeredDevices:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  scopedRoleMemberOf:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      administrativeUnitId: "{{ administrativeUnitId }}"
                      roleId: "{{ roleId }}"
                      roleMemberInfo:
                        displayName: "{{ displayName }}"
                        id: "{{ id }}"
                        @odata.type: "{{ @odata.type }}"
                  settings: "{{ settings }}"
                  solutions: "{{ solutions }}"
                  sponsors:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  teamwork: "{{ teamwork }}"
                  todo: "{{ todo }}"
                  transitiveMemberOf:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                task:
                  id: "{{ id }}"
                  @odata.type: "{{ @odata.type }}"
                  arguments:
                    - name: "{{ name }}"
                      value: "{{ value }}"
                      @odata.type: "{{ @odata.type }}"
                  category: "{{ category }}"
                  continueOnError: {{ continueOnError }}
                  description: "{{ description }}"
                  displayName: "{{ displayName }}"
                  executionSequence: {{ executionSequence }}
                  isEnabled: {{ isEnabled }}
                  taskDefinitionId: "{{ taskDefinitionId }}"
                  taskProcessingResults:
                    - id: "{{ id }}"
                      @odata.type: "{{ @odata.type }}"
                      completedDateTime: "{{ completedDateTime }}"
                      createdDateTime: "{{ createdDateTime }}"
                      failureReason: "{{ failureReason }}"
                      processingInfo: "{{ processingInfo }}"
                      processingStatus: "{{ processingStatus }}"
                      startedDateTime: "{{ startedDateTime }}"
                      subject:
                        id: "{{ id }}"
                        @odata.type: "{{ @odata.type }}"
                        deletedDateTime: "{{ deletedDateTime }}"
                        aboutMe: "{{ aboutMe }}"
                        accountEnabled: {{ accountEnabled }}
                        ageGroup: "{{ ageGroup }}"
                        assignedLicenses: "{{ assignedLicenses }}"
                        assignedPlans: "{{ assignedPlans }}"
                        authorizationInfo: "{{ authorizationInfo }}"
                        birthday: "{{ birthday }}"
                        businessPhones: "{{ businessPhones }}"
                        city: "{{ city }}"
                        companyName: "{{ companyName }}"
                        consentProvidedForMinor: "{{ consentProvidedForMinor }}"
                        country: "{{ country }}"
                        createdDateTime: "{{ createdDateTime }}"
                        creationType: "{{ creationType }}"
                        customSecurityAttributes: "{{ customSecurityAttributes }}"
                        department: "{{ department }}"
                        deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
                        displayName: "{{ displayName }}"
                        employeeHireDate: "{{ employeeHireDate }}"
                        employeeId: "{{ employeeId }}"
                        employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
                        employeeOrgData: "{{ employeeOrgData }}"
                        employeeType: "{{ employeeType }}"
                        externalUserState: "{{ externalUserState }}"
                        externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
                        faxNumber: "{{ faxNumber }}"
                        givenName: "{{ givenName }}"
                        hireDate: "{{ hireDate }}"
                        identities: "{{ identities }}"
                        identityParentId: "{{ identityParentId }}"
                        imAddresses: "{{ imAddresses }}"
                        interests: "{{ interests }}"
                        isManagementRestricted: {{ isManagementRestricted }}
                        isResourceAccount: {{ isResourceAccount }}
                        jobTitle: "{{ jobTitle }}"
                        lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
                        legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
                        licenseAssignmentStates: "{{ licenseAssignmentStates }}"
                        mail: "{{ mail }}"
                        mailboxSettings: "{{ mailboxSettings }}"
                        mailNickname: "{{ mailNickname }}"
                        mobilePhone: "{{ mobilePhone }}"
                        mySite: "{{ mySite }}"
                        officeLocation: "{{ officeLocation }}"
                        onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
                        onPremisesDomainName: "{{ onPremisesDomainName }}"
                        onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
                        onPremisesImmutableId: "{{ onPremisesImmutableId }}"
                        onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
                        onPremisesProvisioningErrors: "{{ onPremisesProvisioningErrors }}"
                        onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
                        onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
                        onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
                        onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
                        otherMails: "{{ otherMails }}"
                        passwordPolicies: "{{ passwordPolicies }}"
                        passwordProfile: "{{ passwordProfile }}"
                        pastProjects: "{{ pastProjects }}"
                        postalCode: "{{ postalCode }}"
                        preferredDataLocation: "{{ preferredDataLocation }}"
                        preferredLanguage: "{{ preferredLanguage }}"
                        preferredName: "{{ preferredName }}"
                        print: "{{ print }}"
                        provisionedPlans: "{{ provisionedPlans }}"
                        proxyAddresses: "{{ proxyAddresses }}"
                        responsibilities: "{{ responsibilities }}"
                        schools: "{{ schools }}"
                        securityIdentifier: "{{ securityIdentifier }}"
                        serviceProvisioningErrors: "{{ serviceProvisioningErrors }}"
                        showInAddressList: {{ showInAddressList }}
                        signInActivity: "{{ signInActivity }}"
                        signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
                        skills: "{{ skills }}"
                        state: "{{ state }}"
                        streetAddress: "{{ streetAddress }}"
                        surname: "{{ surname }}"
                        usageLocation: "{{ usageLocation }}"
                        userPrincipalName: "{{ userPrincipalName }}"
                        userType: "{{ userType }}"
                        activities: "{{ activities }}"
                        adhocCalls: "{{ adhocCalls }}"
                        agreementAcceptances: "{{ agreementAcceptances }}"
                        appRoleAssignments: "{{ appRoleAssignments }}"
                        authentication: "{{ authentication }}"
                        calendar: "{{ calendar }}"
                        calendarGroups: "{{ calendarGroups }}"
                        calendars: "{{ calendars }}"
                        calendarView: "{{ calendarView }}"
                        chats: "{{ chats }}"
                        cloudClipboard: "{{ cloudClipboard }}"
                        cloudPCs: "{{ cloudPCs }}"
                        contactFolders: "{{ contactFolders }}"
                        contacts: "{{ contacts }}"
                        createdObjects: "{{ createdObjects }}"
                        dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
                        deviceManagementTroubleshootingEvents: "{{ deviceManagementTroubleshootingEvents }}"
                        directReports: "{{ directReports }}"
                        drive: "{{ drive }}"
                        drives: "{{ drives }}"
                        employeeExperience: "{{ employeeExperience }}"
                        events: "{{ events }}"
                        extensions: "{{ extensions }}"
                        followedSites: "{{ followedSites }}"
                        inferenceClassification: "{{ inferenceClassification }}"
                        insights: "{{ insights }}"
                        joinedTeams: "{{ joinedTeams }}"
                        licenseDetails: "{{ licenseDetails }}"
                        mailFolders: "{{ mailFolders }}"
                        managedAppRegistrations: "{{ managedAppRegistrations }}"
                        managedDevices: "{{ managedDevices }}"
                        manager: "{{ manager }}"
                        memberOf: "{{ memberOf }}"
                        messages: "{{ messages }}"
                        oauth2PermissionGrants: "{{ oauth2PermissionGrants }}"
                        onenote: "{{ onenote }}"
                        onlineMeetings: "{{ onlineMeetings }}"
                        onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
                        outlook: "{{ outlook }}"
                        ownedDevices: "{{ ownedDevices }}"
                        ownedObjects: "{{ ownedObjects }}"
                        people: "{{ people }}"
                        permissionGrants: "{{ permissionGrants }}"
                        photo: "{{ photo }}"
                        photos: "{{ photos }}"
                        planner: "{{ planner }}"
                        presence: "{{ presence }}"
                        registeredDevices: "{{ registeredDevices }}"
                        scopedRoleMemberOf: "{{ scopedRoleMemberOf }}"
                        settings: "{{ settings }}"
                        solutions: "{{ solutions }}"
                        sponsors: "{{ sponsors }}"
                        teamwork: "{{ teamwork }}"
                        todo: "{{ todo }}"
                        transitiveMemberOf: "{{ transitiveMemberOf }}"
                      task:
                        id: "{{ id }}"
                        @odata.type: "{{ @odata.type }}"
                        arguments: "{{ arguments }}"
                        category: "{{ category }}"
                        continueOnError: {{ continueOnError }}
                        description: "{{ description }}"
                        displayName: "{{ displayName }}"
                        executionSequence: {{ executionSequence }}
                        isEnabled: {{ isEnabled }}
                        taskDefinitionId: "{{ taskDefinitionId }}"
                        taskProcessingResults: "{{ taskProcessingResults }}"
          taskDefinition:
            id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            category: "{{ category }}"
            continueOnError: {{ continueOnError }}
            description: "{{ description }}"
            displayName: "{{ displayName }}"
            parameters:
              - name: "{{ name }}"
                values: "{{ values }}"
                valueType: "{{ valueType }}"
                @odata.type: "{{ @odata.type }}"
            version: {{ version }}
          taskProcessingResults: "{{ taskProcessingResults }}"
    - name: userProcessingResults
      description: |
        Per-user workflow execution results.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          completedDateTime: "{{ completedDateTime }}"
          failedTasksCount: {{ failedTasksCount }}
          processingStatus: "{{ processingStatus }}"
          scheduledDateTime: "{{ scheduledDateTime }}"
          startedDateTime: "{{ startedDateTime }}"
          totalTasksCount: {{ totalTasksCount }}
          totalUnprocessedTasksCount: {{ totalUnprocessedTasksCount }}
          workflowExecutionType: "{{ workflowExecutionType }}"
          workflowVersion: {{ workflowVersion }}
          reprocessedRuns: "{{ reprocessedRuns }}"
          subject:
            id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            aboutMe: "{{ aboutMe }}"
            accountEnabled: {{ accountEnabled }}
            ageGroup: "{{ ageGroup }}"
            assignedLicenses:
              - disabledPlans: "{{ disabledPlans }}"
                skuId: "{{ skuId }}"
                @odata.type: "{{ @odata.type }}"
            assignedPlans:
              - assignedDateTime: "{{ assignedDateTime }}"
                capabilityStatus: "{{ capabilityStatus }}"
                service: "{{ service }}"
                servicePlanId: "{{ servicePlanId }}"
                @odata.type: "{{ @odata.type }}"
            authorizationInfo: "{{ authorizationInfo }}"
            birthday: "{{ birthday }}"
            businessPhones:
              - "{{ businessPhones }}"
            city: "{{ city }}"
            companyName: "{{ companyName }}"
            consentProvidedForMinor: "{{ consentProvidedForMinor }}"
            country: "{{ country }}"
            createdDateTime: "{{ createdDateTime }}"
            creationType: "{{ creationType }}"
            customSecurityAttributes: "{{ customSecurityAttributes }}"
            department: "{{ department }}"
            deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
            displayName: "{{ displayName }}"
            employeeHireDate: "{{ employeeHireDate }}"
            employeeId: "{{ employeeId }}"
            employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
            employeeOrgData: "{{ employeeOrgData }}"
            employeeType: "{{ employeeType }}"
            externalUserState: "{{ externalUserState }}"
            externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
            faxNumber: "{{ faxNumber }}"
            givenName: "{{ givenName }}"
            hireDate: "{{ hireDate }}"
            identities:
              - issuer: "{{ issuer }}"
                issuerAssignedId: "{{ issuerAssignedId }}"
                signInType: "{{ signInType }}"
                @odata.type: "{{ @odata.type }}"
            identityParentId: "{{ identityParentId }}"
            imAddresses:
              - "{{ imAddresses }}"
            interests:
              - "{{ interests }}"
            isManagementRestricted: {{ isManagementRestricted }}
            isResourceAccount: {{ isResourceAccount }}
            jobTitle: "{{ jobTitle }}"
            lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
            legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
            licenseAssignmentStates:
              - assignedByGroup: "{{ assignedByGroup }}"
                disabledPlans: "{{ disabledPlans }}"
                error: "{{ error }}"
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                skuId: "{{ skuId }}"
                state: "{{ state }}"
                @odata.type: "{{ @odata.type }}"
            mail: "{{ mail }}"
            mailboxSettings: "{{ mailboxSettings }}"
            mailNickname: "{{ mailNickname }}"
            mobilePhone: "{{ mobilePhone }}"
            mySite: "{{ mySite }}"
            officeLocation: "{{ officeLocation }}"
            onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
            onPremisesDomainName: "{{ onPremisesDomainName }}"
            onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
            onPremisesImmutableId: "{{ onPremisesImmutableId }}"
            onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
            onPremisesProvisioningErrors:
              - category: "{{ category }}"
                occurredDateTime: "{{ occurredDateTime }}"
                propertyCausingError: "{{ propertyCausingError }}"
                value: "{{ value }}"
                @odata.type: "{{ @odata.type }}"
            onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
            onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
            onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
            onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
            otherMails:
              - "{{ otherMails }}"
            passwordPolicies: "{{ passwordPolicies }}"
            passwordProfile: "{{ passwordProfile }}"
            pastProjects:
              - "{{ pastProjects }}"
            postalCode: "{{ postalCode }}"
            preferredDataLocation: "{{ preferredDataLocation }}"
            preferredLanguage: "{{ preferredLanguage }}"
            preferredName: "{{ preferredName }}"
            print: "{{ print }}"
            provisionedPlans:
              - capabilityStatus: "{{ capabilityStatus }}"
                provisioningStatus: "{{ provisioningStatus }}"
                service: "{{ service }}"
                @odata.type: "{{ @odata.type }}"
            proxyAddresses:
              - "{{ proxyAddresses }}"
            responsibilities:
              - "{{ responsibilities }}"
            schools:
              - "{{ schools }}"
            securityIdentifier: "{{ securityIdentifier }}"
            serviceProvisioningErrors:
              - createdDateTime: "{{ createdDateTime }}"
                isResolved: {{ isResolved }}
                serviceInstance: "{{ serviceInstance }}"
                @odata.type: "{{ @odata.type }}"
            showInAddressList: {{ showInAddressList }}
            signInActivity: "{{ signInActivity }}"
            signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
            skills:
              - "{{ skills }}"
            state: "{{ state }}"
            streetAddress: "{{ streetAddress }}"
            surname: "{{ surname }}"
            usageLocation: "{{ usageLocation }}"
            userPrincipalName: "{{ userPrincipalName }}"
            userType: "{{ userType }}"
            activities:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationUrl: "{{ activationUrl }}"
                activitySourceHost: "{{ activitySourceHost }}"
                appActivityId: "{{ appActivityId }}"
                appDisplayName: "{{ appDisplayName }}"
                contentInfo: "{{ contentInfo }}"
                contentUrl: "{{ contentUrl }}"
                createdDateTime: "{{ createdDateTime }}"
                expirationDateTime: "{{ expirationDateTime }}"
                fallbackUrl: "{{ fallbackUrl }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                status: "{{ status }}"
                userTimezone: "{{ userTimezone }}"
                visualElements:
                  attribution:
                    addImageQuery: {{ addImageQuery }}
                    alternateText: "{{ alternateText }}"
                    alternativeText: "{{ alternativeText }}"
                    iconUrl: "{{ iconUrl }}"
                    @odata.type: "{{ @odata.type }}"
                  backgroundColor: "{{ backgroundColor }}"
                  content: "{{ content }}"
                  description: "{{ description }}"
                  displayText: "{{ displayText }}"
                  @odata.type: "{{ @odata.type }}"
                historyItems: "{{ historyItems }}"
            adhocCalls:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            agreementAcceptances:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                agreementFileId: "{{ agreementFileId }}"
                agreementId: "{{ agreementId }}"
                deviceDisplayName: "{{ deviceDisplayName }}"
                deviceId: "{{ deviceId }}"
                deviceOSType: "{{ deviceOSType }}"
                deviceOSVersion: "{{ deviceOSVersion }}"
                expirationDateTime: "{{ expirationDateTime }}"
                recordedDateTime: "{{ recordedDateTime }}"
                state: "{{ state }}"
                userDisplayName: "{{ userDisplayName }}"
                userEmail: "{{ userEmail }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
            appRoleAssignments:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                appRoleId: "{{ appRoleId }}"
                createdDateTime: "{{ createdDateTime }}"
                principalDisplayName: "{{ principalDisplayName }}"
                principalId: "{{ principalId }}"
                principalType: "{{ principalType }}"
                resourceDisplayName: "{{ resourceDisplayName }}"
                resourceId: "{{ resourceId }}"
            authentication: "{{ authentication }}"
            calendar: "{{ calendar }}"
            calendarGroups:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                changeKey: "{{ changeKey }}"
                classId: "{{ classId }}"
                name: "{{ name }}"
                calendars: "{{ calendars }}"
            calendars:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
                canEdit: {{ canEdit }}
                canShare: {{ canShare }}
                canViewPrivateItems: {{ canViewPrivateItems }}
                changeKey: "{{ changeKey }}"
                color: "{{ color }}"
                defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
                hexColor: "{{ hexColor }}"
                isDefaultCalendar: {{ isDefaultCalendar }}
                isRemovable: {{ isRemovable }}
                isTallyingResponses: {{ isTallyingResponses }}
                name: "{{ name }}"
                owner: "{{ owner }}"
                calendarPermissions: "{{ calendarPermissions }}"
                calendarView: "{{ calendarView }}"
                events: "{{ events }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            calendarView:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            chats:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                chatType: "{{ chatType }}"
                createdDateTime: "{{ createdDateTime }}"
                isHiddenForAllMembers: {{ isHiddenForAllMembers }}
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                migrationMode: "{{ migrationMode }}"
                onlineMeetingInfo: "{{ onlineMeetingInfo }}"
                originalCreatedDateTime: "{{ originalCreatedDateTime }}"
                tenantId: "{{ tenantId }}"
                topic: "{{ topic }}"
                viewpoint: "{{ viewpoint }}"
                webUrl: "{{ webUrl }}"
                installedApps: "{{ installedApps }}"
                lastMessagePreview: "{{ lastMessagePreview }}"
                members: "{{ members }}"
                messages: "{{ messages }}"
                permissionGrants: "{{ permissionGrants }}"
                pinnedMessages: "{{ pinnedMessages }}"
                tabs: "{{ tabs }}"
            cloudClipboard: "{{ cloudClipboard }}"
            cloudPCs:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                aadDeviceId: "{{ aadDeviceId }}"
                displayName: "{{ displayName }}"
                gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
                imageDisplayName: "{{ imageDisplayName }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                managedDeviceId: "{{ managedDeviceId }}"
                managedDeviceName: "{{ managedDeviceName }}"
                onPremisesConnectionName: "{{ onPremisesConnectionName }}"
                provisioningPolicyId: "{{ provisioningPolicyId }}"
                provisioningPolicyName: "{{ provisioningPolicyName }}"
                provisioningType: "{{ provisioningType }}"
                servicePlanId: "{{ servicePlanId }}"
                servicePlanName: "{{ servicePlanName }}"
                userPrincipalName: "{{ userPrincipalName }}"
            contactFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                displayName: "{{ displayName }}"
                parentFolderId: "{{ parentFolderId }}"
                childFolders: "{{ childFolders }}"
                contacts: "{{ contacts }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            contacts:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                assistantName: "{{ assistantName }}"
                birthday: "{{ birthday }}"
                businessAddress: "{{ businessAddress }}"
                businessHomePage: "{{ businessHomePage }}"
                businessPhones: "{{ businessPhones }}"
                children: "{{ children }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                emailAddresses: "{{ emailAddresses }}"
                fileAs: "{{ fileAs }}"
                generation: "{{ generation }}"
                givenName: "{{ givenName }}"
                homeAddress: "{{ homeAddress }}"
                homePhones: "{{ homePhones }}"
                imAddresses: "{{ imAddresses }}"
                initials: "{{ initials }}"
                jobTitle: "{{ jobTitle }}"
                manager: "{{ manager }}"
                middleName: "{{ middleName }}"
                mobilePhone: "{{ mobilePhone }}"
                nickName: "{{ nickName }}"
                officeLocation: "{{ officeLocation }}"
                otherAddress: "{{ otherAddress }}"
                parentFolderId: "{{ parentFolderId }}"
                personalNotes: "{{ personalNotes }}"
                primaryEmailAddress: "{{ primaryEmailAddress }}"
                profession: "{{ profession }}"
                secondaryEmailAddress: "{{ secondaryEmailAddress }}"
                spouseName: "{{ spouseName }}"
                surname: "{{ surname }}"
                tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
                title: "{{ title }}"
                yomiCompanyName: "{{ yomiCompanyName }}"
                yomiGivenName: "{{ yomiGivenName }}"
                yomiSurname: "{{ yomiSurname }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                photo: "{{ photo }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            createdObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
            deviceManagementTroubleshootingEvents:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                correlationId: "{{ correlationId }}"
                eventDateTime: "{{ eventDateTime }}"
            directReports:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            drive: "{{ drive }}"
            drives:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                driveType: "{{ driveType }}"
                owner: "{{ owner }}"
                quota: "{{ quota }}"
                sharePointIds: "{{ sharePointIds }}"
                system: "{{ system }}"
                bundles: "{{ bundles }}"
                following: "{{ following }}"
                items: "{{ items }}"
                list: "{{ list }}"
                root: "{{ root }}"
                special: "{{ special }}"
            employeeExperience: "{{ employeeExperience }}"
            events:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            extensions:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
            followedSites:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                displayName: "{{ displayName }}"
                error: "{{ error }}"
                isPersonalSite: {{ isPersonalSite }}
                root: "{{ root }}"
                sharepointIds: "{{ sharepointIds }}"
                siteCollection: "{{ siteCollection }}"
                analytics: "{{ analytics }}"
                columns: "{{ columns }}"
                contentTypes: "{{ contentTypes }}"
                drive: "{{ drive }}"
                drives: "{{ drives }}"
                externalColumns: "{{ externalColumns }}"
                items: "{{ items }}"
                lists: "{{ lists }}"
                onenote: "{{ onenote }}"
                operations: "{{ operations }}"
                pages: "{{ pages }}"
                permissions: "{{ permissions }}"
                sites: "{{ sites }}"
                termStore: "{{ termStore }}"
                termStores: "{{ termStores }}"
            inferenceClassification: "{{ inferenceClassification }}"
            insights: "{{ insights }}"
            joinedTeams:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                classification: "{{ classification }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                displayName: "{{ displayName }}"
                firstChannelName: "{{ firstChannelName }}"
                funSettings: "{{ funSettings }}"
                guestSettings: "{{ guestSettings }}"
                internalId: "{{ internalId }}"
                isArchived: {{ isArchived }}
                memberSettings: "{{ memberSettings }}"
                messagingSettings: "{{ messagingSettings }}"
                specialization: "{{ specialization }}"
                summary: "{{ summary }}"
                tenantId: "{{ tenantId }}"
                visibility: "{{ visibility }}"
                webUrl: "{{ webUrl }}"
                allChannels: "{{ allChannels }}"
                channels: "{{ channels }}"
                group: "{{ group }}"
                incomingChannels: "{{ incomingChannels }}"
                installedApps: "{{ installedApps }}"
                members: "{{ members }}"
                operations: "{{ operations }}"
                permissionGrants: "{{ permissionGrants }}"
                photo: "{{ photo }}"
                primaryChannel: "{{ primaryChannel }}"
                schedule: "{{ schedule }}"
                tags: "{{ tags }}"
                template: "{{ template }}"
            licenseDetails:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                servicePlans: "{{ servicePlans }}"
                skuId: "{{ skuId }}"
                skuPartNumber: "{{ skuPartNumber }}"
            mailFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                childFolderCount: {{ childFolderCount }}
                displayName: "{{ displayName }}"
                isHidden: {{ isHidden }}
                parentFolderId: "{{ parentFolderId }}"
                totalItemCount: {{ totalItemCount }}
                unreadItemCount: {{ unreadItemCount }}
                childFolders: "{{ childFolders }}"
                messageRules: "{{ messageRules }}"
                messages: "{{ messages }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            managedAppRegistrations:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                appIdentifier: "{{ appIdentifier }}"
                applicationVersion: "{{ applicationVersion }}"
                createdDateTime: "{{ createdDateTime }}"
                deviceName: "{{ deviceName }}"
                deviceTag: "{{ deviceTag }}"
                deviceType: "{{ deviceType }}"
                flaggedReasons: "{{ flaggedReasons }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managementSdkVersion: "{{ managementSdkVersion }}"
                platformVersion: "{{ platformVersion }}"
                userId: "{{ userId }}"
                version: "{{ version }}"
                appliedPolicies: "{{ appliedPolicies }}"
                intendedPolicies: "{{ intendedPolicies }}"
                operations: "{{ operations }}"
            managedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationLockBypassCode: "{{ activationLockBypassCode }}"
                androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
                azureADDeviceId: "{{ azureADDeviceId }}"
                azureADRegistered: {{ azureADRegistered }}
                complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
                complianceState: "{{ complianceState }}"
                configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
                deviceActionResults: "{{ deviceActionResults }}"
                deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
                deviceEnrollmentType: "{{ deviceEnrollmentType }}"
                deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
                deviceName: "{{ deviceName }}"
                deviceRegistrationState: "{{ deviceRegistrationState }}"
                easActivated: {{ easActivated }}
                easActivationDateTime: "{{ easActivationDateTime }}"
                easDeviceId: "{{ easDeviceId }}"
                emailAddress: "{{ emailAddress }}"
                enrolledDateTime: "{{ enrolledDateTime }}"
                enrollmentProfileName: "{{ enrollmentProfileName }}"
                ethernetMacAddress: "{{ ethernetMacAddress }}"
                exchangeAccessState: "{{ exchangeAccessState }}"
                exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
                exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
                freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
                iccid: "{{ iccid }}"
                imei: "{{ imei }}"
                isEncrypted: {{ isEncrypted }}
                isSupervised: {{ isSupervised }}
                jailBroken: "{{ jailBroken }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managedDeviceName: "{{ managedDeviceName }}"
                managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
                managementAgent: "{{ managementAgent }}"
                managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
                managementState: "{{ managementState }}"
                manufacturer: "{{ manufacturer }}"
                meid: "{{ meid }}"
                model: "{{ model }}"
                notes: "{{ notes }}"
                operatingSystem: "{{ operatingSystem }}"
                osVersion: "{{ osVersion }}"
                partnerReportedThreatState: "{{ partnerReportedThreatState }}"
                phoneNumber: "{{ phoneNumber }}"
                physicalMemoryInBytes: {{ physicalMemoryInBytes }}
                remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
                remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
                requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
                serialNumber: "{{ serialNumber }}"
                subscriberCarrier: "{{ subscriberCarrier }}"
                totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
                udid: "{{ udid }}"
                userDisplayName: "{{ userDisplayName }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
                wiFiMacAddress: "{{ wiFiMacAddress }}"
                deviceCategory: "{{ deviceCategory }}"
                deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
                deviceConfigurationStates: "{{ deviceConfigurationStates }}"
                logCollectionRequests: "{{ logCollectionRequests }}"
                users: "{{ users }}"
                windowsProtectionState: "{{ windowsProtectionState }}"
            manager: "{{ manager }}"
            memberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            messages:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                bccRecipients: "{{ bccRecipients }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                ccRecipients: "{{ ccRecipients }}"
                conversationId: "{{ conversationId }}"
                conversationIndex: "{{ conversationIndex }}"
                flag: "{{ flag }}"
                from: "{{ from }}"
                hasAttachments: {{ hasAttachments }}
                importance: "{{ importance }}"
                inferenceClassification: "{{ inferenceClassification }}"
                internetMessageHeaders: "{{ internetMessageHeaders }}"
                internetMessageId: "{{ internetMessageId }}"
                isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
                isDraft: {{ isDraft }}
                isRead: {{ isRead }}
                isReadReceiptRequested: {{ isReadReceiptRequested }}
                parentFolderId: "{{ parentFolderId }}"
                receivedDateTime: "{{ receivedDateTime }}"
                replyTo: "{{ replyTo }}"
                sender: "{{ sender }}"
                sentDateTime: "{{ sentDateTime }}"
                subject: "{{ subject }}"
                toRecipients: "{{ toRecipients }}"
                uniqueBody: "{{ uniqueBody }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            oauth2PermissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                clientId: "{{ clientId }}"
                consentType: "{{ consentType }}"
                principalId: "{{ principalId }}"
                resourceId: "{{ resourceId }}"
                scope: "{{ scope }}"
            onenote: "{{ onenote }}"
            onlineMeetings:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
                allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
                allowBreakoutRooms: {{ allowBreakoutRooms }}
                allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
                allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
                allowedPresenters: "{{ allowedPresenters }}"
                allowLiveShare: "{{ allowLiveShare }}"
                allowMeetingChat: "{{ allowMeetingChat }}"
                allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
                allowPowerPointSharing: {{ allowPowerPointSharing }}
                allowRecording: {{ allowRecording }}
                allowTeamworkReactions: {{ allowTeamworkReactions }}
                allowTranscription: {{ allowTranscription }}
                allowWhiteboard: {{ allowWhiteboard }}
                audioConferencing: "{{ audioConferencing }}"
                chatInfo: "{{ chatInfo }}"
                chatRestrictions: "{{ chatRestrictions }}"
                expiryDateTime: "{{ expiryDateTime }}"
                isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
                isEntryExitAnnounced: {{ isEntryExitAnnounced }}
                joinInformation: "{{ joinInformation }}"
                joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
                joinWebUrl: "{{ joinWebUrl }}"
                lobbyBypassSettings: "{{ lobbyBypassSettings }}"
                meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
                meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
                recordAutomatically: {{ recordAutomatically }}
                sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
                shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
                subject: "{{ subject }}"
                videoTeleconferenceId: "{{ videoTeleconferenceId }}"
                watermarkProtection: "{{ watermarkProtection }}"
                attendanceReports: "{{ attendanceReports }}"
                attendeeReport: "{{ attendeeReport }}"
                broadcastSettings: "{{ broadcastSettings }}"
                creationDateTime: "{{ creationDateTime }}"
                endDateTime: "{{ endDateTime }}"
                externalId: "{{ externalId }}"
                isBroadcast: {{ isBroadcast }}
                meetingTemplateId: "{{ meetingTemplateId }}"
                participants: "{{ participants }}"
                startDateTime: "{{ startDateTime }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
            outlook: "{{ outlook }}"
            ownedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            ownedObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            people:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                birthday: "{{ birthday }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                givenName: "{{ givenName }}"
                imAddress: "{{ imAddress }}"
                isFavorite: {{ isFavorite }}
                jobTitle: "{{ jobTitle }}"
                officeLocation: "{{ officeLocation }}"
                personNotes: "{{ personNotes }}"
                personType: "{{ personType }}"
                phones: "{{ phones }}"
                postalAddresses: "{{ postalAddresses }}"
                profession: "{{ profession }}"
                scoredEmailAddresses: "{{ scoredEmailAddresses }}"
                surname: "{{ surname }}"
                userPrincipalName: "{{ userPrincipalName }}"
                websites: "{{ websites }}"
                yomiCompany: "{{ yomiCompany }}"
            permissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                clientAppId: "{{ clientAppId }}"
                clientId: "{{ clientId }}"
                permission: "{{ permission }}"
                permissionType: "{{ permissionType }}"
                resourceAppId: "{{ resourceAppId }}"
            photo: "{{ photo }}"
            photos:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                height: {{ height }}
                width: {{ width }}
            planner: "{{ planner }}"
            presence: "{{ presence }}"
            registeredDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            scopedRoleMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                administrativeUnitId: "{{ administrativeUnitId }}"
                roleId: "{{ roleId }}"
                roleMemberInfo:
                  displayName: "{{ displayName }}"
                  id: "{{ id }}"
                  @odata.type: "{{ @odata.type }}"
            settings: "{{ settings }}"
            solutions: "{{ solutions }}"
            sponsors:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            teamwork: "{{ teamwork }}"
            todo: "{{ todo }}"
            transitiveMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
          taskProcessingResults: "{{ taskProcessingResults }}"
    - name: versions
      description: |
        The workflow versions that are available.
      value:
        - category: "{{ category }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          executionConditions:
            @odata.type: "{{ @odata.type }}"
          isEnabled: {{ isEnabled }}
          isSchedulingEnabled: {{ isSchedulingEnabled }}
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          administrationScopeTargets: "{{ administrationScopeTargets }}"
          createdBy:
            id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            aboutMe: "{{ aboutMe }}"
            accountEnabled: {{ accountEnabled }}
            ageGroup: "{{ ageGroup }}"
            assignedLicenses:
              - disabledPlans: "{{ disabledPlans }}"
                skuId: "{{ skuId }}"
                @odata.type: "{{ @odata.type }}"
            assignedPlans:
              - assignedDateTime: "{{ assignedDateTime }}"
                capabilityStatus: "{{ capabilityStatus }}"
                service: "{{ service }}"
                servicePlanId: "{{ servicePlanId }}"
                @odata.type: "{{ @odata.type }}"
            authorizationInfo: "{{ authorizationInfo }}"
            birthday: "{{ birthday }}"
            businessPhones:
              - "{{ businessPhones }}"
            city: "{{ city }}"
            companyName: "{{ companyName }}"
            consentProvidedForMinor: "{{ consentProvidedForMinor }}"
            country: "{{ country }}"
            createdDateTime: "{{ createdDateTime }}"
            creationType: "{{ creationType }}"
            customSecurityAttributes: "{{ customSecurityAttributes }}"
            department: "{{ department }}"
            deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
            displayName: "{{ displayName }}"
            employeeHireDate: "{{ employeeHireDate }}"
            employeeId: "{{ employeeId }}"
            employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
            employeeOrgData: "{{ employeeOrgData }}"
            employeeType: "{{ employeeType }}"
            externalUserState: "{{ externalUserState }}"
            externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
            faxNumber: "{{ faxNumber }}"
            givenName: "{{ givenName }}"
            hireDate: "{{ hireDate }}"
            identities:
              - issuer: "{{ issuer }}"
                issuerAssignedId: "{{ issuerAssignedId }}"
                signInType: "{{ signInType }}"
                @odata.type: "{{ @odata.type }}"
            identityParentId: "{{ identityParentId }}"
            imAddresses:
              - "{{ imAddresses }}"
            interests:
              - "{{ interests }}"
            isManagementRestricted: {{ isManagementRestricted }}
            isResourceAccount: {{ isResourceAccount }}
            jobTitle: "{{ jobTitle }}"
            lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
            legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
            licenseAssignmentStates:
              - assignedByGroup: "{{ assignedByGroup }}"
                disabledPlans: "{{ disabledPlans }}"
                error: "{{ error }}"
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                skuId: "{{ skuId }}"
                state: "{{ state }}"
                @odata.type: "{{ @odata.type }}"
            mail: "{{ mail }}"
            mailboxSettings: "{{ mailboxSettings }}"
            mailNickname: "{{ mailNickname }}"
            mobilePhone: "{{ mobilePhone }}"
            mySite: "{{ mySite }}"
            officeLocation: "{{ officeLocation }}"
            onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
            onPremisesDomainName: "{{ onPremisesDomainName }}"
            onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
            onPremisesImmutableId: "{{ onPremisesImmutableId }}"
            onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
            onPremisesProvisioningErrors:
              - category: "{{ category }}"
                occurredDateTime: "{{ occurredDateTime }}"
                propertyCausingError: "{{ propertyCausingError }}"
                value: "{{ value }}"
                @odata.type: "{{ @odata.type }}"
            onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
            onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
            onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
            onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
            otherMails:
              - "{{ otherMails }}"
            passwordPolicies: "{{ passwordPolicies }}"
            passwordProfile: "{{ passwordProfile }}"
            pastProjects:
              - "{{ pastProjects }}"
            postalCode: "{{ postalCode }}"
            preferredDataLocation: "{{ preferredDataLocation }}"
            preferredLanguage: "{{ preferredLanguage }}"
            preferredName: "{{ preferredName }}"
            print: "{{ print }}"
            provisionedPlans:
              - capabilityStatus: "{{ capabilityStatus }}"
                provisioningStatus: "{{ provisioningStatus }}"
                service: "{{ service }}"
                @odata.type: "{{ @odata.type }}"
            proxyAddresses:
              - "{{ proxyAddresses }}"
            responsibilities:
              - "{{ responsibilities }}"
            schools:
              - "{{ schools }}"
            securityIdentifier: "{{ securityIdentifier }}"
            serviceProvisioningErrors:
              - createdDateTime: "{{ createdDateTime }}"
                isResolved: {{ isResolved }}
                serviceInstance: "{{ serviceInstance }}"
                @odata.type: "{{ @odata.type }}"
            showInAddressList: {{ showInAddressList }}
            signInActivity: "{{ signInActivity }}"
            signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
            skills:
              - "{{ skills }}"
            state: "{{ state }}"
            streetAddress: "{{ streetAddress }}"
            surname: "{{ surname }}"
            usageLocation: "{{ usageLocation }}"
            userPrincipalName: "{{ userPrincipalName }}"
            userType: "{{ userType }}"
            activities:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationUrl: "{{ activationUrl }}"
                activitySourceHost: "{{ activitySourceHost }}"
                appActivityId: "{{ appActivityId }}"
                appDisplayName: "{{ appDisplayName }}"
                contentInfo: "{{ contentInfo }}"
                contentUrl: "{{ contentUrl }}"
                createdDateTime: "{{ createdDateTime }}"
                expirationDateTime: "{{ expirationDateTime }}"
                fallbackUrl: "{{ fallbackUrl }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                status: "{{ status }}"
                userTimezone: "{{ userTimezone }}"
                visualElements:
                  attribution:
                    addImageQuery: {{ addImageQuery }}
                    alternateText: "{{ alternateText }}"
                    alternativeText: "{{ alternativeText }}"
                    iconUrl: "{{ iconUrl }}"
                    @odata.type: "{{ @odata.type }}"
                  backgroundColor: "{{ backgroundColor }}"
                  content: "{{ content }}"
                  description: "{{ description }}"
                  displayText: "{{ displayText }}"
                  @odata.type: "{{ @odata.type }}"
                historyItems: "{{ historyItems }}"
            adhocCalls:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            agreementAcceptances:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                agreementFileId: "{{ agreementFileId }}"
                agreementId: "{{ agreementId }}"
                deviceDisplayName: "{{ deviceDisplayName }}"
                deviceId: "{{ deviceId }}"
                deviceOSType: "{{ deviceOSType }}"
                deviceOSVersion: "{{ deviceOSVersion }}"
                expirationDateTime: "{{ expirationDateTime }}"
                recordedDateTime: "{{ recordedDateTime }}"
                state: "{{ state }}"
                userDisplayName: "{{ userDisplayName }}"
                userEmail: "{{ userEmail }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
            appRoleAssignments:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                appRoleId: "{{ appRoleId }}"
                createdDateTime: "{{ createdDateTime }}"
                principalDisplayName: "{{ principalDisplayName }}"
                principalId: "{{ principalId }}"
                principalType: "{{ principalType }}"
                resourceDisplayName: "{{ resourceDisplayName }}"
                resourceId: "{{ resourceId }}"
            authentication: "{{ authentication }}"
            calendar: "{{ calendar }}"
            calendarGroups:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                changeKey: "{{ changeKey }}"
                classId: "{{ classId }}"
                name: "{{ name }}"
                calendars: "{{ calendars }}"
            calendars:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
                canEdit: {{ canEdit }}
                canShare: {{ canShare }}
                canViewPrivateItems: {{ canViewPrivateItems }}
                changeKey: "{{ changeKey }}"
                color: "{{ color }}"
                defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
                hexColor: "{{ hexColor }}"
                isDefaultCalendar: {{ isDefaultCalendar }}
                isRemovable: {{ isRemovable }}
                isTallyingResponses: {{ isTallyingResponses }}
                name: "{{ name }}"
                owner: "{{ owner }}"
                calendarPermissions: "{{ calendarPermissions }}"
                calendarView: "{{ calendarView }}"
                events: "{{ events }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            calendarView:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            chats:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                chatType: "{{ chatType }}"
                createdDateTime: "{{ createdDateTime }}"
                isHiddenForAllMembers: {{ isHiddenForAllMembers }}
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                migrationMode: "{{ migrationMode }}"
                onlineMeetingInfo: "{{ onlineMeetingInfo }}"
                originalCreatedDateTime: "{{ originalCreatedDateTime }}"
                tenantId: "{{ tenantId }}"
                topic: "{{ topic }}"
                viewpoint: "{{ viewpoint }}"
                webUrl: "{{ webUrl }}"
                installedApps: "{{ installedApps }}"
                lastMessagePreview: "{{ lastMessagePreview }}"
                members: "{{ members }}"
                messages: "{{ messages }}"
                permissionGrants: "{{ permissionGrants }}"
                pinnedMessages: "{{ pinnedMessages }}"
                tabs: "{{ tabs }}"
            cloudClipboard: "{{ cloudClipboard }}"
            cloudPCs:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                aadDeviceId: "{{ aadDeviceId }}"
                displayName: "{{ displayName }}"
                gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
                imageDisplayName: "{{ imageDisplayName }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                managedDeviceId: "{{ managedDeviceId }}"
                managedDeviceName: "{{ managedDeviceName }}"
                onPremisesConnectionName: "{{ onPremisesConnectionName }}"
                provisioningPolicyId: "{{ provisioningPolicyId }}"
                provisioningPolicyName: "{{ provisioningPolicyName }}"
                provisioningType: "{{ provisioningType }}"
                servicePlanId: "{{ servicePlanId }}"
                servicePlanName: "{{ servicePlanName }}"
                userPrincipalName: "{{ userPrincipalName }}"
            contactFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                displayName: "{{ displayName }}"
                parentFolderId: "{{ parentFolderId }}"
                childFolders: "{{ childFolders }}"
                contacts: "{{ contacts }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            contacts:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                assistantName: "{{ assistantName }}"
                birthday: "{{ birthday }}"
                businessAddress: "{{ businessAddress }}"
                businessHomePage: "{{ businessHomePage }}"
                businessPhones: "{{ businessPhones }}"
                children: "{{ children }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                emailAddresses: "{{ emailAddresses }}"
                fileAs: "{{ fileAs }}"
                generation: "{{ generation }}"
                givenName: "{{ givenName }}"
                homeAddress: "{{ homeAddress }}"
                homePhones: "{{ homePhones }}"
                imAddresses: "{{ imAddresses }}"
                initials: "{{ initials }}"
                jobTitle: "{{ jobTitle }}"
                manager: "{{ manager }}"
                middleName: "{{ middleName }}"
                mobilePhone: "{{ mobilePhone }}"
                nickName: "{{ nickName }}"
                officeLocation: "{{ officeLocation }}"
                otherAddress: "{{ otherAddress }}"
                parentFolderId: "{{ parentFolderId }}"
                personalNotes: "{{ personalNotes }}"
                primaryEmailAddress: "{{ primaryEmailAddress }}"
                profession: "{{ profession }}"
                secondaryEmailAddress: "{{ secondaryEmailAddress }}"
                spouseName: "{{ spouseName }}"
                surname: "{{ surname }}"
                tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
                title: "{{ title }}"
                yomiCompanyName: "{{ yomiCompanyName }}"
                yomiGivenName: "{{ yomiGivenName }}"
                yomiSurname: "{{ yomiSurname }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                photo: "{{ photo }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            createdObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
            deviceManagementTroubleshootingEvents:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                correlationId: "{{ correlationId }}"
                eventDateTime: "{{ eventDateTime }}"
            directReports:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            drive: "{{ drive }}"
            drives:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                driveType: "{{ driveType }}"
                owner: "{{ owner }}"
                quota: "{{ quota }}"
                sharePointIds: "{{ sharePointIds }}"
                system: "{{ system }}"
                bundles: "{{ bundles }}"
                following: "{{ following }}"
                items: "{{ items }}"
                list: "{{ list }}"
                root: "{{ root }}"
                special: "{{ special }}"
            employeeExperience: "{{ employeeExperience }}"
            events:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            extensions:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
            followedSites:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                displayName: "{{ displayName }}"
                error: "{{ error }}"
                isPersonalSite: {{ isPersonalSite }}
                root: "{{ root }}"
                sharepointIds: "{{ sharepointIds }}"
                siteCollection: "{{ siteCollection }}"
                analytics: "{{ analytics }}"
                columns: "{{ columns }}"
                contentTypes: "{{ contentTypes }}"
                drive: "{{ drive }}"
                drives: "{{ drives }}"
                externalColumns: "{{ externalColumns }}"
                items: "{{ items }}"
                lists: "{{ lists }}"
                onenote: "{{ onenote }}"
                operations: "{{ operations }}"
                pages: "{{ pages }}"
                permissions: "{{ permissions }}"
                sites: "{{ sites }}"
                termStore: "{{ termStore }}"
                termStores: "{{ termStores }}"
            inferenceClassification: "{{ inferenceClassification }}"
            insights: "{{ insights }}"
            joinedTeams:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                classification: "{{ classification }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                displayName: "{{ displayName }}"
                firstChannelName: "{{ firstChannelName }}"
                funSettings: "{{ funSettings }}"
                guestSettings: "{{ guestSettings }}"
                internalId: "{{ internalId }}"
                isArchived: {{ isArchived }}
                memberSettings: "{{ memberSettings }}"
                messagingSettings: "{{ messagingSettings }}"
                specialization: "{{ specialization }}"
                summary: "{{ summary }}"
                tenantId: "{{ tenantId }}"
                visibility: "{{ visibility }}"
                webUrl: "{{ webUrl }}"
                allChannels: "{{ allChannels }}"
                channels: "{{ channels }}"
                group: "{{ group }}"
                incomingChannels: "{{ incomingChannels }}"
                installedApps: "{{ installedApps }}"
                members: "{{ members }}"
                operations: "{{ operations }}"
                permissionGrants: "{{ permissionGrants }}"
                photo: "{{ photo }}"
                primaryChannel: "{{ primaryChannel }}"
                schedule: "{{ schedule }}"
                tags: "{{ tags }}"
                template: "{{ template }}"
            licenseDetails:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                servicePlans: "{{ servicePlans }}"
                skuId: "{{ skuId }}"
                skuPartNumber: "{{ skuPartNumber }}"
            mailFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                childFolderCount: {{ childFolderCount }}
                displayName: "{{ displayName }}"
                isHidden: {{ isHidden }}
                parentFolderId: "{{ parentFolderId }}"
                totalItemCount: {{ totalItemCount }}
                unreadItemCount: {{ unreadItemCount }}
                childFolders: "{{ childFolders }}"
                messageRules: "{{ messageRules }}"
                messages: "{{ messages }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            managedAppRegistrations:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                appIdentifier: "{{ appIdentifier }}"
                applicationVersion: "{{ applicationVersion }}"
                createdDateTime: "{{ createdDateTime }}"
                deviceName: "{{ deviceName }}"
                deviceTag: "{{ deviceTag }}"
                deviceType: "{{ deviceType }}"
                flaggedReasons: "{{ flaggedReasons }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managementSdkVersion: "{{ managementSdkVersion }}"
                platformVersion: "{{ platformVersion }}"
                userId: "{{ userId }}"
                version: "{{ version }}"
                appliedPolicies: "{{ appliedPolicies }}"
                intendedPolicies: "{{ intendedPolicies }}"
                operations: "{{ operations }}"
            managedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationLockBypassCode: "{{ activationLockBypassCode }}"
                androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
                azureADDeviceId: "{{ azureADDeviceId }}"
                azureADRegistered: {{ azureADRegistered }}
                complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
                complianceState: "{{ complianceState }}"
                configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
                deviceActionResults: "{{ deviceActionResults }}"
                deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
                deviceEnrollmentType: "{{ deviceEnrollmentType }}"
                deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
                deviceName: "{{ deviceName }}"
                deviceRegistrationState: "{{ deviceRegistrationState }}"
                easActivated: {{ easActivated }}
                easActivationDateTime: "{{ easActivationDateTime }}"
                easDeviceId: "{{ easDeviceId }}"
                emailAddress: "{{ emailAddress }}"
                enrolledDateTime: "{{ enrolledDateTime }}"
                enrollmentProfileName: "{{ enrollmentProfileName }}"
                ethernetMacAddress: "{{ ethernetMacAddress }}"
                exchangeAccessState: "{{ exchangeAccessState }}"
                exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
                exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
                freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
                iccid: "{{ iccid }}"
                imei: "{{ imei }}"
                isEncrypted: {{ isEncrypted }}
                isSupervised: {{ isSupervised }}
                jailBroken: "{{ jailBroken }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managedDeviceName: "{{ managedDeviceName }}"
                managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
                managementAgent: "{{ managementAgent }}"
                managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
                managementState: "{{ managementState }}"
                manufacturer: "{{ manufacturer }}"
                meid: "{{ meid }}"
                model: "{{ model }}"
                notes: "{{ notes }}"
                operatingSystem: "{{ operatingSystem }}"
                osVersion: "{{ osVersion }}"
                partnerReportedThreatState: "{{ partnerReportedThreatState }}"
                phoneNumber: "{{ phoneNumber }}"
                physicalMemoryInBytes: {{ physicalMemoryInBytes }}
                remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
                remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
                requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
                serialNumber: "{{ serialNumber }}"
                subscriberCarrier: "{{ subscriberCarrier }}"
                totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
                udid: "{{ udid }}"
                userDisplayName: "{{ userDisplayName }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
                wiFiMacAddress: "{{ wiFiMacAddress }}"
                deviceCategory: "{{ deviceCategory }}"
                deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
                deviceConfigurationStates: "{{ deviceConfigurationStates }}"
                logCollectionRequests: "{{ logCollectionRequests }}"
                users: "{{ users }}"
                windowsProtectionState: "{{ windowsProtectionState }}"
            manager: "{{ manager }}"
            memberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            messages:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                bccRecipients: "{{ bccRecipients }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                ccRecipients: "{{ ccRecipients }}"
                conversationId: "{{ conversationId }}"
                conversationIndex: "{{ conversationIndex }}"
                flag: "{{ flag }}"
                from: "{{ from }}"
                hasAttachments: {{ hasAttachments }}
                importance: "{{ importance }}"
                inferenceClassification: "{{ inferenceClassification }}"
                internetMessageHeaders: "{{ internetMessageHeaders }}"
                internetMessageId: "{{ internetMessageId }}"
                isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
                isDraft: {{ isDraft }}
                isRead: {{ isRead }}
                isReadReceiptRequested: {{ isReadReceiptRequested }}
                parentFolderId: "{{ parentFolderId }}"
                receivedDateTime: "{{ receivedDateTime }}"
                replyTo: "{{ replyTo }}"
                sender: "{{ sender }}"
                sentDateTime: "{{ sentDateTime }}"
                subject: "{{ subject }}"
                toRecipients: "{{ toRecipients }}"
                uniqueBody: "{{ uniqueBody }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            oauth2PermissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                clientId: "{{ clientId }}"
                consentType: "{{ consentType }}"
                principalId: "{{ principalId }}"
                resourceId: "{{ resourceId }}"
                scope: "{{ scope }}"
            onenote: "{{ onenote }}"
            onlineMeetings:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
                allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
                allowBreakoutRooms: {{ allowBreakoutRooms }}
                allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
                allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
                allowedPresenters: "{{ allowedPresenters }}"
                allowLiveShare: "{{ allowLiveShare }}"
                allowMeetingChat: "{{ allowMeetingChat }}"
                allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
                allowPowerPointSharing: {{ allowPowerPointSharing }}
                allowRecording: {{ allowRecording }}
                allowTeamworkReactions: {{ allowTeamworkReactions }}
                allowTranscription: {{ allowTranscription }}
                allowWhiteboard: {{ allowWhiteboard }}
                audioConferencing: "{{ audioConferencing }}"
                chatInfo: "{{ chatInfo }}"
                chatRestrictions: "{{ chatRestrictions }}"
                expiryDateTime: "{{ expiryDateTime }}"
                isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
                isEntryExitAnnounced: {{ isEntryExitAnnounced }}
                joinInformation: "{{ joinInformation }}"
                joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
                joinWebUrl: "{{ joinWebUrl }}"
                lobbyBypassSettings: "{{ lobbyBypassSettings }}"
                meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
                meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
                recordAutomatically: {{ recordAutomatically }}
                sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
                shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
                subject: "{{ subject }}"
                videoTeleconferenceId: "{{ videoTeleconferenceId }}"
                watermarkProtection: "{{ watermarkProtection }}"
                attendanceReports: "{{ attendanceReports }}"
                attendeeReport: "{{ attendeeReport }}"
                broadcastSettings: "{{ broadcastSettings }}"
                creationDateTime: "{{ creationDateTime }}"
                endDateTime: "{{ endDateTime }}"
                externalId: "{{ externalId }}"
                isBroadcast: {{ isBroadcast }}
                meetingTemplateId: "{{ meetingTemplateId }}"
                participants: "{{ participants }}"
                startDateTime: "{{ startDateTime }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
            outlook: "{{ outlook }}"
            ownedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            ownedObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            people:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                birthday: "{{ birthday }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                givenName: "{{ givenName }}"
                imAddress: "{{ imAddress }}"
                isFavorite: {{ isFavorite }}
                jobTitle: "{{ jobTitle }}"
                officeLocation: "{{ officeLocation }}"
                personNotes: "{{ personNotes }}"
                personType: "{{ personType }}"
                phones: "{{ phones }}"
                postalAddresses: "{{ postalAddresses }}"
                profession: "{{ profession }}"
                scoredEmailAddresses: "{{ scoredEmailAddresses }}"
                surname: "{{ surname }}"
                userPrincipalName: "{{ userPrincipalName }}"
                websites: "{{ websites }}"
                yomiCompany: "{{ yomiCompany }}"
            permissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                clientAppId: "{{ clientAppId }}"
                clientId: "{{ clientId }}"
                permission: "{{ permission }}"
                permissionType: "{{ permissionType }}"
                resourceAppId: "{{ resourceAppId }}"
            photo: "{{ photo }}"
            photos:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                height: {{ height }}
                width: {{ width }}
            planner: "{{ planner }}"
            presence: "{{ presence }}"
            registeredDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            scopedRoleMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                administrativeUnitId: "{{ administrativeUnitId }}"
                roleId: "{{ roleId }}"
                roleMemberInfo:
                  displayName: "{{ displayName }}"
                  id: "{{ id }}"
                  @odata.type: "{{ @odata.type }}"
            settings: "{{ settings }}"
            solutions: "{{ solutions }}"
            sponsors:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            teamwork: "{{ teamwork }}"
            todo: "{{ todo }}"
            transitiveMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
          lastModifiedBy:
            id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
            deletedDateTime: "{{ deletedDateTime }}"
            aboutMe: "{{ aboutMe }}"
            accountEnabled: {{ accountEnabled }}
            ageGroup: "{{ ageGroup }}"
            assignedLicenses:
              - disabledPlans: "{{ disabledPlans }}"
                skuId: "{{ skuId }}"
                @odata.type: "{{ @odata.type }}"
            assignedPlans:
              - assignedDateTime: "{{ assignedDateTime }}"
                capabilityStatus: "{{ capabilityStatus }}"
                service: "{{ service }}"
                servicePlanId: "{{ servicePlanId }}"
                @odata.type: "{{ @odata.type }}"
            authorizationInfo: "{{ authorizationInfo }}"
            birthday: "{{ birthday }}"
            businessPhones:
              - "{{ businessPhones }}"
            city: "{{ city }}"
            companyName: "{{ companyName }}"
            consentProvidedForMinor: "{{ consentProvidedForMinor }}"
            country: "{{ country }}"
            createdDateTime: "{{ createdDateTime }}"
            creationType: "{{ creationType }}"
            customSecurityAttributes: "{{ customSecurityAttributes }}"
            department: "{{ department }}"
            deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
            displayName: "{{ displayName }}"
            employeeHireDate: "{{ employeeHireDate }}"
            employeeId: "{{ employeeId }}"
            employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
            employeeOrgData: "{{ employeeOrgData }}"
            employeeType: "{{ employeeType }}"
            externalUserState: "{{ externalUserState }}"
            externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
            faxNumber: "{{ faxNumber }}"
            givenName: "{{ givenName }}"
            hireDate: "{{ hireDate }}"
            identities:
              - issuer: "{{ issuer }}"
                issuerAssignedId: "{{ issuerAssignedId }}"
                signInType: "{{ signInType }}"
                @odata.type: "{{ @odata.type }}"
            identityParentId: "{{ identityParentId }}"
            imAddresses:
              - "{{ imAddresses }}"
            interests:
              - "{{ interests }}"
            isManagementRestricted: {{ isManagementRestricted }}
            isResourceAccount: {{ isResourceAccount }}
            jobTitle: "{{ jobTitle }}"
            lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
            legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
            licenseAssignmentStates:
              - assignedByGroup: "{{ assignedByGroup }}"
                disabledPlans: "{{ disabledPlans }}"
                error: "{{ error }}"
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                skuId: "{{ skuId }}"
                state: "{{ state }}"
                @odata.type: "{{ @odata.type }}"
            mail: "{{ mail }}"
            mailboxSettings: "{{ mailboxSettings }}"
            mailNickname: "{{ mailNickname }}"
            mobilePhone: "{{ mobilePhone }}"
            mySite: "{{ mySite }}"
            officeLocation: "{{ officeLocation }}"
            onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
            onPremisesDomainName: "{{ onPremisesDomainName }}"
            onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
            onPremisesImmutableId: "{{ onPremisesImmutableId }}"
            onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
            onPremisesProvisioningErrors:
              - category: "{{ category }}"
                occurredDateTime: "{{ occurredDateTime }}"
                propertyCausingError: "{{ propertyCausingError }}"
                value: "{{ value }}"
                @odata.type: "{{ @odata.type }}"
            onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
            onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
            onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
            onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
            otherMails:
              - "{{ otherMails }}"
            passwordPolicies: "{{ passwordPolicies }}"
            passwordProfile: "{{ passwordProfile }}"
            pastProjects:
              - "{{ pastProjects }}"
            postalCode: "{{ postalCode }}"
            preferredDataLocation: "{{ preferredDataLocation }}"
            preferredLanguage: "{{ preferredLanguage }}"
            preferredName: "{{ preferredName }}"
            print: "{{ print }}"
            provisionedPlans:
              - capabilityStatus: "{{ capabilityStatus }}"
                provisioningStatus: "{{ provisioningStatus }}"
                service: "{{ service }}"
                @odata.type: "{{ @odata.type }}"
            proxyAddresses:
              - "{{ proxyAddresses }}"
            responsibilities:
              - "{{ responsibilities }}"
            schools:
              - "{{ schools }}"
            securityIdentifier: "{{ securityIdentifier }}"
            serviceProvisioningErrors:
              - createdDateTime: "{{ createdDateTime }}"
                isResolved: {{ isResolved }}
                serviceInstance: "{{ serviceInstance }}"
                @odata.type: "{{ @odata.type }}"
            showInAddressList: {{ showInAddressList }}
            signInActivity: "{{ signInActivity }}"
            signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
            skills:
              - "{{ skills }}"
            state: "{{ state }}"
            streetAddress: "{{ streetAddress }}"
            surname: "{{ surname }}"
            usageLocation: "{{ usageLocation }}"
            userPrincipalName: "{{ userPrincipalName }}"
            userType: "{{ userType }}"
            activities:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationUrl: "{{ activationUrl }}"
                activitySourceHost: "{{ activitySourceHost }}"
                appActivityId: "{{ appActivityId }}"
                appDisplayName: "{{ appDisplayName }}"
                contentInfo: "{{ contentInfo }}"
                contentUrl: "{{ contentUrl }}"
                createdDateTime: "{{ createdDateTime }}"
                expirationDateTime: "{{ expirationDateTime }}"
                fallbackUrl: "{{ fallbackUrl }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                status: "{{ status }}"
                userTimezone: "{{ userTimezone }}"
                visualElements:
                  attribution:
                    addImageQuery: {{ addImageQuery }}
                    alternateText: "{{ alternateText }}"
                    alternativeText: "{{ alternativeText }}"
                    iconUrl: "{{ iconUrl }}"
                    @odata.type: "{{ @odata.type }}"
                  backgroundColor: "{{ backgroundColor }}"
                  content: "{{ content }}"
                  description: "{{ description }}"
                  displayText: "{{ displayText }}"
                  @odata.type: "{{ @odata.type }}"
                historyItems: "{{ historyItems }}"
            adhocCalls:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            agreementAcceptances:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                agreementFileId: "{{ agreementFileId }}"
                agreementId: "{{ agreementId }}"
                deviceDisplayName: "{{ deviceDisplayName }}"
                deviceId: "{{ deviceId }}"
                deviceOSType: "{{ deviceOSType }}"
                deviceOSVersion: "{{ deviceOSVersion }}"
                expirationDateTime: "{{ expirationDateTime }}"
                recordedDateTime: "{{ recordedDateTime }}"
                state: "{{ state }}"
                userDisplayName: "{{ userDisplayName }}"
                userEmail: "{{ userEmail }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
            appRoleAssignments:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                appRoleId: "{{ appRoleId }}"
                createdDateTime: "{{ createdDateTime }}"
                principalDisplayName: "{{ principalDisplayName }}"
                principalId: "{{ principalId }}"
                principalType: "{{ principalType }}"
                resourceDisplayName: "{{ resourceDisplayName }}"
                resourceId: "{{ resourceId }}"
            authentication: "{{ authentication }}"
            calendar: "{{ calendar }}"
            calendarGroups:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                changeKey: "{{ changeKey }}"
                classId: "{{ classId }}"
                name: "{{ name }}"
                calendars: "{{ calendars }}"
            calendars:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
                canEdit: {{ canEdit }}
                canShare: {{ canShare }}
                canViewPrivateItems: {{ canViewPrivateItems }}
                changeKey: "{{ changeKey }}"
                color: "{{ color }}"
                defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
                hexColor: "{{ hexColor }}"
                isDefaultCalendar: {{ isDefaultCalendar }}
                isRemovable: {{ isRemovable }}
                isTallyingResponses: {{ isTallyingResponses }}
                name: "{{ name }}"
                owner: "{{ owner }}"
                calendarPermissions: "{{ calendarPermissions }}"
                calendarView: "{{ calendarView }}"
                events: "{{ events }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            calendarView:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            chats:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                chatType: "{{ chatType }}"
                createdDateTime: "{{ createdDateTime }}"
                isHiddenForAllMembers: {{ isHiddenForAllMembers }}
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                migrationMode: "{{ migrationMode }}"
                onlineMeetingInfo: "{{ onlineMeetingInfo }}"
                originalCreatedDateTime: "{{ originalCreatedDateTime }}"
                tenantId: "{{ tenantId }}"
                topic: "{{ topic }}"
                viewpoint: "{{ viewpoint }}"
                webUrl: "{{ webUrl }}"
                installedApps: "{{ installedApps }}"
                lastMessagePreview: "{{ lastMessagePreview }}"
                members: "{{ members }}"
                messages: "{{ messages }}"
                permissionGrants: "{{ permissionGrants }}"
                pinnedMessages: "{{ pinnedMessages }}"
                tabs: "{{ tabs }}"
            cloudClipboard: "{{ cloudClipboard }}"
            cloudPCs:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                aadDeviceId: "{{ aadDeviceId }}"
                displayName: "{{ displayName }}"
                gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
                imageDisplayName: "{{ imageDisplayName }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                managedDeviceId: "{{ managedDeviceId }}"
                managedDeviceName: "{{ managedDeviceName }}"
                onPremisesConnectionName: "{{ onPremisesConnectionName }}"
                provisioningPolicyId: "{{ provisioningPolicyId }}"
                provisioningPolicyName: "{{ provisioningPolicyName }}"
                provisioningType: "{{ provisioningType }}"
                servicePlanId: "{{ servicePlanId }}"
                servicePlanName: "{{ servicePlanName }}"
                userPrincipalName: "{{ userPrincipalName }}"
            contactFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                displayName: "{{ displayName }}"
                parentFolderId: "{{ parentFolderId }}"
                childFolders: "{{ childFolders }}"
                contacts: "{{ contacts }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            contacts:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                assistantName: "{{ assistantName }}"
                birthday: "{{ birthday }}"
                businessAddress: "{{ businessAddress }}"
                businessHomePage: "{{ businessHomePage }}"
                businessPhones: "{{ businessPhones }}"
                children: "{{ children }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                emailAddresses: "{{ emailAddresses }}"
                fileAs: "{{ fileAs }}"
                generation: "{{ generation }}"
                givenName: "{{ givenName }}"
                homeAddress: "{{ homeAddress }}"
                homePhones: "{{ homePhones }}"
                imAddresses: "{{ imAddresses }}"
                initials: "{{ initials }}"
                jobTitle: "{{ jobTitle }}"
                manager: "{{ manager }}"
                middleName: "{{ middleName }}"
                mobilePhone: "{{ mobilePhone }}"
                nickName: "{{ nickName }}"
                officeLocation: "{{ officeLocation }}"
                otherAddress: "{{ otherAddress }}"
                parentFolderId: "{{ parentFolderId }}"
                personalNotes: "{{ personalNotes }}"
                primaryEmailAddress: "{{ primaryEmailAddress }}"
                profession: "{{ profession }}"
                secondaryEmailAddress: "{{ secondaryEmailAddress }}"
                spouseName: "{{ spouseName }}"
                surname: "{{ surname }}"
                tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
                title: "{{ title }}"
                yomiCompanyName: "{{ yomiCompanyName }}"
                yomiGivenName: "{{ yomiGivenName }}"
                yomiSurname: "{{ yomiSurname }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                photo: "{{ photo }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            createdObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
            deviceManagementTroubleshootingEvents:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                correlationId: "{{ correlationId }}"
                eventDateTime: "{{ eventDateTime }}"
            directReports:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            drive: "{{ drive }}"
            drives:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                driveType: "{{ driveType }}"
                owner: "{{ owner }}"
                quota: "{{ quota }}"
                sharePointIds: "{{ sharePointIds }}"
                system: "{{ system }}"
                bundles: "{{ bundles }}"
                following: "{{ following }}"
                items: "{{ items }}"
                list: "{{ list }}"
                root: "{{ root }}"
                special: "{{ special }}"
            employeeExperience: "{{ employeeExperience }}"
            events:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            extensions:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
            followedSites:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                displayName: "{{ displayName }}"
                error: "{{ error }}"
                isPersonalSite: {{ isPersonalSite }}
                root: "{{ root }}"
                sharepointIds: "{{ sharepointIds }}"
                siteCollection: "{{ siteCollection }}"
                analytics: "{{ analytics }}"
                columns: "{{ columns }}"
                contentTypes: "{{ contentTypes }}"
                drive: "{{ drive }}"
                drives: "{{ drives }}"
                externalColumns: "{{ externalColumns }}"
                items: "{{ items }}"
                lists: "{{ lists }}"
                onenote: "{{ onenote }}"
                operations: "{{ operations }}"
                pages: "{{ pages }}"
                permissions: "{{ permissions }}"
                sites: "{{ sites }}"
                termStore: "{{ termStore }}"
                termStores: "{{ termStores }}"
            inferenceClassification: "{{ inferenceClassification }}"
            insights: "{{ insights }}"
            joinedTeams:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                classification: "{{ classification }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                displayName: "{{ displayName }}"
                firstChannelName: "{{ firstChannelName }}"
                funSettings: "{{ funSettings }}"
                guestSettings: "{{ guestSettings }}"
                internalId: "{{ internalId }}"
                isArchived: {{ isArchived }}
                memberSettings: "{{ memberSettings }}"
                messagingSettings: "{{ messagingSettings }}"
                specialization: "{{ specialization }}"
                summary: "{{ summary }}"
                tenantId: "{{ tenantId }}"
                visibility: "{{ visibility }}"
                webUrl: "{{ webUrl }}"
                allChannels: "{{ allChannels }}"
                channels: "{{ channels }}"
                group: "{{ group }}"
                incomingChannels: "{{ incomingChannels }}"
                installedApps: "{{ installedApps }}"
                members: "{{ members }}"
                operations: "{{ operations }}"
                permissionGrants: "{{ permissionGrants }}"
                photo: "{{ photo }}"
                primaryChannel: "{{ primaryChannel }}"
                schedule: "{{ schedule }}"
                tags: "{{ tags }}"
                template: "{{ template }}"
            licenseDetails:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                servicePlans: "{{ servicePlans }}"
                skuId: "{{ skuId }}"
                skuPartNumber: "{{ skuPartNumber }}"
            mailFolders:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                childFolderCount: {{ childFolderCount }}
                displayName: "{{ displayName }}"
                isHidden: {{ isHidden }}
                parentFolderId: "{{ parentFolderId }}"
                totalItemCount: {{ totalItemCount }}
                unreadItemCount: {{ unreadItemCount }}
                childFolders: "{{ childFolders }}"
                messageRules: "{{ messageRules }}"
                messages: "{{ messages }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            managedAppRegistrations:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                appIdentifier: "{{ appIdentifier }}"
                applicationVersion: "{{ applicationVersion }}"
                createdDateTime: "{{ createdDateTime }}"
                deviceName: "{{ deviceName }}"
                deviceTag: "{{ deviceTag }}"
                deviceType: "{{ deviceType }}"
                flaggedReasons: "{{ flaggedReasons }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managementSdkVersion: "{{ managementSdkVersion }}"
                platformVersion: "{{ platformVersion }}"
                userId: "{{ userId }}"
                version: "{{ version }}"
                appliedPolicies: "{{ appliedPolicies }}"
                intendedPolicies: "{{ intendedPolicies }}"
                operations: "{{ operations }}"
            managedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                activationLockBypassCode: "{{ activationLockBypassCode }}"
                androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
                azureADDeviceId: "{{ azureADDeviceId }}"
                azureADRegistered: {{ azureADRegistered }}
                complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
                complianceState: "{{ complianceState }}"
                configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
                deviceActionResults: "{{ deviceActionResults }}"
                deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
                deviceEnrollmentType: "{{ deviceEnrollmentType }}"
                deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
                deviceName: "{{ deviceName }}"
                deviceRegistrationState: "{{ deviceRegistrationState }}"
                easActivated: {{ easActivated }}
                easActivationDateTime: "{{ easActivationDateTime }}"
                easDeviceId: "{{ easDeviceId }}"
                emailAddress: "{{ emailAddress }}"
                enrolledDateTime: "{{ enrolledDateTime }}"
                enrollmentProfileName: "{{ enrollmentProfileName }}"
                ethernetMacAddress: "{{ ethernetMacAddress }}"
                exchangeAccessState: "{{ exchangeAccessState }}"
                exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
                exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
                freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
                iccid: "{{ iccid }}"
                imei: "{{ imei }}"
                isEncrypted: {{ isEncrypted }}
                isSupervised: {{ isSupervised }}
                jailBroken: "{{ jailBroken }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managedDeviceName: "{{ managedDeviceName }}"
                managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
                managementAgent: "{{ managementAgent }}"
                managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
                managementState: "{{ managementState }}"
                manufacturer: "{{ manufacturer }}"
                meid: "{{ meid }}"
                model: "{{ model }}"
                notes: "{{ notes }}"
                operatingSystem: "{{ operatingSystem }}"
                osVersion: "{{ osVersion }}"
                partnerReportedThreatState: "{{ partnerReportedThreatState }}"
                phoneNumber: "{{ phoneNumber }}"
                physicalMemoryInBytes: {{ physicalMemoryInBytes }}
                remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
                remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
                requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
                serialNumber: "{{ serialNumber }}"
                subscriberCarrier: "{{ subscriberCarrier }}"
                totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
                udid: "{{ udid }}"
                userDisplayName: "{{ userDisplayName }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
                wiFiMacAddress: "{{ wiFiMacAddress }}"
                deviceCategory: "{{ deviceCategory }}"
                deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
                deviceConfigurationStates: "{{ deviceConfigurationStates }}"
                logCollectionRequests: "{{ logCollectionRequests }}"
                users: "{{ users }}"
                windowsProtectionState: "{{ windowsProtectionState }}"
            manager: "{{ manager }}"
            memberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            messages:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                bccRecipients: "{{ bccRecipients }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                ccRecipients: "{{ ccRecipients }}"
                conversationId: "{{ conversationId }}"
                conversationIndex: "{{ conversationIndex }}"
                flag: "{{ flag }}"
                from: "{{ from }}"
                hasAttachments: {{ hasAttachments }}
                importance: "{{ importance }}"
                inferenceClassification: "{{ inferenceClassification }}"
                internetMessageHeaders: "{{ internetMessageHeaders }}"
                internetMessageId: "{{ internetMessageId }}"
                isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
                isDraft: {{ isDraft }}
                isRead: {{ isRead }}
                isReadReceiptRequested: {{ isReadReceiptRequested }}
                parentFolderId: "{{ parentFolderId }}"
                receivedDateTime: "{{ receivedDateTime }}"
                replyTo: "{{ replyTo }}"
                sender: "{{ sender }}"
                sentDateTime: "{{ sentDateTime }}"
                subject: "{{ subject }}"
                toRecipients: "{{ toRecipients }}"
                uniqueBody: "{{ uniqueBody }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            oauth2PermissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                clientId: "{{ clientId }}"
                consentType: "{{ consentType }}"
                principalId: "{{ principalId }}"
                resourceId: "{{ resourceId }}"
                scope: "{{ scope }}"
            onenote: "{{ onenote }}"
            onlineMeetings:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
                allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
                allowBreakoutRooms: {{ allowBreakoutRooms }}
                allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
                allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
                allowedPresenters: "{{ allowedPresenters }}"
                allowLiveShare: "{{ allowLiveShare }}"
                allowMeetingChat: "{{ allowMeetingChat }}"
                allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
                allowPowerPointSharing: {{ allowPowerPointSharing }}
                allowRecording: {{ allowRecording }}
                allowTeamworkReactions: {{ allowTeamworkReactions }}
                allowTranscription: {{ allowTranscription }}
                allowWhiteboard: {{ allowWhiteboard }}
                audioConferencing: "{{ audioConferencing }}"
                chatInfo: "{{ chatInfo }}"
                chatRestrictions: "{{ chatRestrictions }}"
                expiryDateTime: "{{ expiryDateTime }}"
                isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
                isEntryExitAnnounced: {{ isEntryExitAnnounced }}
                joinInformation: "{{ joinInformation }}"
                joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
                joinWebUrl: "{{ joinWebUrl }}"
                lobbyBypassSettings: "{{ lobbyBypassSettings }}"
                meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
                meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
                recordAutomatically: {{ recordAutomatically }}
                sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
                shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
                subject: "{{ subject }}"
                videoTeleconferenceId: "{{ videoTeleconferenceId }}"
                watermarkProtection: "{{ watermarkProtection }}"
                attendanceReports: "{{ attendanceReports }}"
                attendeeReport: "{{ attendeeReport }}"
                broadcastSettings: "{{ broadcastSettings }}"
                creationDateTime: "{{ creationDateTime }}"
                endDateTime: "{{ endDateTime }}"
                externalId: "{{ externalId }}"
                isBroadcast: {{ isBroadcast }}
                meetingTemplateId: "{{ meetingTemplateId }}"
                participants: "{{ participants }}"
                startDateTime: "{{ startDateTime }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
            outlook: "{{ outlook }}"
            ownedDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            ownedObjects:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            people:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                birthday: "{{ birthday }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                givenName: "{{ givenName }}"
                imAddress: "{{ imAddress }}"
                isFavorite: {{ isFavorite }}
                jobTitle: "{{ jobTitle }}"
                officeLocation: "{{ officeLocation }}"
                personNotes: "{{ personNotes }}"
                personType: "{{ personType }}"
                phones: "{{ phones }}"
                postalAddresses: "{{ postalAddresses }}"
                profession: "{{ profession }}"
                scoredEmailAddresses: "{{ scoredEmailAddresses }}"
                surname: "{{ surname }}"
                userPrincipalName: "{{ userPrincipalName }}"
                websites: "{{ websites }}"
                yomiCompany: "{{ yomiCompany }}"
            permissionGrants:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
                clientAppId: "{{ clientAppId }}"
                clientId: "{{ clientId }}"
                permission: "{{ permission }}"
                permissionType: "{{ permissionType }}"
                resourceAppId: "{{ resourceAppId }}"
            photo: "{{ photo }}"
            photos:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                height: {{ height }}
                width: {{ width }}
            planner: "{{ planner }}"
            presence: "{{ presence }}"
            registeredDevices:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            scopedRoleMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                administrativeUnitId: "{{ administrativeUnitId }}"
                roleId: "{{ roleId }}"
                roleMemberInfo:
                  displayName: "{{ displayName }}"
                  id: "{{ id }}"
                  @odata.type: "{{ @odata.type }}"
            settings: "{{ settings }}"
            solutions: "{{ solutions }}"
            sponsors:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
            teamwork: "{{ teamwork }}"
            todo: "{{ todo }}"
            transitiveMemberOf:
              - id: "{{ id }}"
                @odata.type: "{{ @odata.type }}"
                deletedDateTime: "{{ deletedDateTime }}"
          tasks: "{{ tasks }}"
          @odata.type: "{{ @odata.type }}"
          versionNumber: {{ versionNumber }}
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

Update the properties of a workflow object. Only the properties listed in the request body table can be updated. To update any other workflow properties, see workflow: createNewVersion.

```sql
UPDATE entra_id.identity_governance.lifecycle_workflows_workflows
SET 
category = '{{ category }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
executionConditions = '{{ executionConditions }}',
isEnabled = {{ isEnabled }},
isSchedulingEnabled = {{ isSchedulingEnabled }},
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
administrationScopeTargets = '{{ administrationScopeTargets }}',
createdBy = '{{ createdBy }}',
lastModifiedBy = '{{ lastModifiedBy }}',
tasks = '{{ tasks }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
id = '{{ id }}',
nextScheduleRunDateTime = '{{ nextScheduleRunDateTime }}',
version = {{ version }},
executionScope = '{{ executionScope }}',
runs = '{{ runs }}',
taskReports = '{{ taskReports }}',
userProcessingResults = '{{ userProcessingResults }}',
versions = '{{ versions }}'
WHERE 
workflow-id = '{{ workflow-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
administrationScopeTargets,
category,
createdBy,
createdDateTime,
deletedDateTime,
description,
displayName,
executionConditions,
executionScope,
isEnabled,
isSchedulingEnabled,
lastModifiedBy,
lastModifiedDateTime,
nextScheduleRunDateTime,
runs,
taskReports,
tasks,
userProcessingResults,
version,
versions;
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

Delete a workflow object and its associated tasks, taskProcessingResults and versions. You can restore a deleted workflow and its associated objects within 30 days of deletion.

```sql
DELETE FROM entra_id.identity_governance.lifecycle_workflows_workflows
WHERE workflow-id = '{{ workflow-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
