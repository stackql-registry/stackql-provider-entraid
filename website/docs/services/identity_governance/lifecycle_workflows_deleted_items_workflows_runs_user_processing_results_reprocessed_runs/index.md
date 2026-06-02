--- 
title: lifecycle_workflows_deleted_items_workflows_runs_user_processing_results_reprocessed_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_deleted_items_workflows_runs_user_processing_results_reprocessed_runs
  - identity_governance
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_deleted_items_workflows_runs_user_processing_results_reprocessed_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_deleted_items_workflows_runs_user_processing_results_reprocessed_runs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.lifecycle_workflows_deleted_items_workflows_runs_user_processing_results_reprocessed_runs" /></td></tr>
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
    <td><CopyableCode code="activatedOnScope" /></td>
    <td><code></code></td>
    <td>The scope for which the workflow runs.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the run completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="failedTasksCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of tasks that failed in the run execution.</td>
</tr>
<tr>
    <td><CopyableCode code="failedUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users that failed in the run execution.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime that the run was last updated.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="processingStatus" /></td>
    <td><code>string</code></td>
    <td> (queued, inProgress, completed, completedWithErrors, canceled, failed, unknownFutureValue) (title: lifecycleWorkflowProcessingStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="reprocessedRuns" /></td>
    <td><code>array</code></td>
    <td>The related reprocessed workflow run.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the run is scheduled to be executed for a workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="startedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the run execution started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="successfulUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of successfully completed users in the run.</td>
</tr>
<tr>
    <td><CopyableCode code="taskProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The related taskProcessingResults.</td>
</tr>
<tr>
    <td><CopyableCode code="totalTasksCount" /></td>
    <td><code>number (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="totalUnprocessedTasksCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The total number of unprocessed tasks in the run execution.</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The total number of users in the workflow execution.</td>
</tr>
<tr>
    <td><CopyableCode code="userProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The associated individual user execution.</td>
</tr>
<tr>
    <td><CopyableCode code="workflowExecutionType" /></td>
    <td><code>string</code></td>
    <td> (scheduled, onDemand, unknownFutureValue, activatedWithScope) (title: workflowExecutionType)</td>
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
    <td><CopyableCode code="activatedOnScope" /></td>
    <td><code></code></td>
    <td>The scope for which the workflow runs.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the run completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="failedTasksCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of tasks that failed in the run execution.</td>
</tr>
<tr>
    <td><CopyableCode code="failedUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users that failed in the run execution.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime that the run was last updated.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="processingStatus" /></td>
    <td><code>string</code></td>
    <td> (queued, inProgress, completed, completedWithErrors, canceled, failed, unknownFutureValue) (title: lifecycleWorkflowProcessingStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="reprocessedRuns" /></td>
    <td><code>array</code></td>
    <td>The related reprocessed workflow run.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduledDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the run is scheduled to be executed for a workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="startedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the run execution started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="successfulUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of successfully completed users in the run.</td>
</tr>
<tr>
    <td><CopyableCode code="taskProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The related taskProcessingResults.</td>
</tr>
<tr>
    <td><CopyableCode code="totalTasksCount" /></td>
    <td><code>number (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="totalUnprocessedTasksCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The total number of unprocessed tasks in the run execution.</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The total number of users in the workflow execution.</td>
</tr>
<tr>
    <td><CopyableCode code="userProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The associated individual user execution.</td>
</tr>
<tr>
    <td><CopyableCode code="workflowExecutionType" /></td>
    <td><code>string</code></td>
    <td> (scheduled, onDemand, unknownFutureValue, activatedWithScope) (title: workflowExecutionType)</td>
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
    <td><a href="#parameter-workflow-id"><code>workflow-id</code></a>, <a href="#parameter-run-id"><code>run-id</code></a>, <a href="#parameter-userProcessingResult-id"><code>userProcessingResult-id</code></a>, <a href="#parameter-run-id1"><code>run-id1</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The related reprocessed workflow run.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workflow-id"><code>workflow-id</code></a>, <a href="#parameter-run-id"><code>run-id</code></a>, <a href="#parameter-userProcessingResult-id"><code>userProcessingResult-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The related reprocessed workflow run.</td>
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
<tr id="parameter-run-id">
    <td><CopyableCode code="run-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of run</td>
</tr>
<tr id="parameter-run-id1">
    <td><CopyableCode code="run-id1" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of run</td>
</tr>
<tr id="parameter-userProcessingResult-id">
    <td><CopyableCode code="userProcessingResult-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of userProcessingResult</td>
</tr>
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

The related reprocessed workflow run.

```sql
SELECT
id,
@odata.type,
activatedOnScope,
completedDateTime,
failedTasksCount,
failedUsersCount,
lastUpdatedDateTime,
processingStatus,
reprocessedRuns,
scheduledDateTime,
startedDateTime,
successfulUsersCount,
taskProcessingResults,
totalTasksCount,
totalUnprocessedTasksCount,
totalUsersCount,
userProcessingResults,
workflowExecutionType
FROM entraid.identity_governance.lifecycle_workflows_deleted_items_workflows_runs_user_processing_results_reprocessed_runs
WHERE workflow-id = '{{ workflow-id }}' -- required
AND run-id = '{{ run-id }}' -- required
AND userProcessingResult-id = '{{ userProcessingResult-id }}' -- required
AND run-id1 = '{{ run-id1 }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

The related reprocessed workflow run.

```sql
SELECT
id,
@odata.type,
activatedOnScope,
completedDateTime,
failedTasksCount,
failedUsersCount,
lastUpdatedDateTime,
processingStatus,
reprocessedRuns,
scheduledDateTime,
startedDateTime,
successfulUsersCount,
taskProcessingResults,
totalTasksCount,
totalUnprocessedTasksCount,
totalUsersCount,
userProcessingResults,
workflowExecutionType
FROM entraid.identity_governance.lifecycle_workflows_deleted_items_workflows_runs_user_processing_results_reprocessed_runs
WHERE workflow-id = '{{ workflow-id }}' -- required
AND run-id = '{{ run-id }}' -- required
AND userProcessingResult-id = '{{ userProcessingResult-id }}' -- required
AND $top = '{{ $top }}'
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
