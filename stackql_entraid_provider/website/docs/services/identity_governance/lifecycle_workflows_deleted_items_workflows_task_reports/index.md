--- 
title: lifecycle_workflows_deleted_items_workflows_task_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_deleted_items_workflows_task_reports
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_deleted_items_workflows_task_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_deleted_items_workflows_task_reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_task_reports" /></td></tr>
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
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the associated run completed. Value is null if the run has not completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="failedUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users in the run execution for which the associated task failed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the task report was last updated. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="processingStatus" /></td>
    <td><code>string</code></td>
    <td> (queued, inProgress, completed, completedWithErrors, canceled, failed, unknownFutureValue) (title: lifecycleWorkflowProcessingStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="runId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the associated run.</td>
</tr>
<tr>
    <td><CopyableCode code="startedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the associated run started. Value is null if the run has not started. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="successfulUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users in the run execution for which the associated task succeeded.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityGovernance.task, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="taskDefinition" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityGovernance.taskDefinition, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="taskProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The related lifecycle workflow taskProcessingResults.</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The total number of users in the run execution for which the associated task was scheduled to execute.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="unprocessedUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users in the run execution for which the associated task is queued, in progress, or canceled.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
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
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the associated run completed. Value is null if the run has not completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="failedUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users in the run execution for which the associated task failed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the task report was last updated. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="processingStatus" /></td>
    <td><code>string</code></td>
    <td> (queued, inProgress, completed, completedWithErrors, canceled, failed, unknownFutureValue) (title: lifecycleWorkflowProcessingStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="runId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the associated run.</td>
</tr>
<tr>
    <td><CopyableCode code="startedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time that the associated run started. Value is null if the run has not started. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="successfulUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users in the run execution for which the associated task succeeded.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityGovernance.task, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="taskDefinition" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityGovernance.taskDefinition, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="taskProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The related lifecycle workflow taskProcessingResults.</td>
</tr>
<tr>
    <td><CopyableCode code="totalUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The total number of users in the run execution for which the associated task was scheduled to execute.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="unprocessedUsersCount" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of users in the run execution for which the associated task is queued, in progress, or canceled.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.</td>
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
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-task_report_id"><code>task_report_id</code></a></td>
    <td></td>
    <td>Represents the aggregation of task execution data for tasks within a workflow object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a></td>
    <td></td>
    <td>Represents the aggregation of task execution data for tasks within a workflow object.</td>
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
<tr id="parameter-task_report_id">
    <td><CopyableCode code="task_report_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of taskReport</td>
</tr>
<tr id="parameter-workflow_id">
    <td><CopyableCode code="workflow_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of workflow</td>
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

Represents the aggregation of task execution data for tasks within a workflow object.

```sql
SELECT
id,
completedDateTime,
failedUsersCount,
lastUpdatedDateTime,
processingStatus,
runId,
startedDateTime,
successfulUsersCount,
task,
taskDefinition,
taskProcessingResults,
totalUsersCount,
unprocessedUsersCount
FROM entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_task_reports
WHERE workflow_id = '{{ workflow_id }}' -- required
AND task_report_id = '{{ task_report_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Represents the aggregation of task execution data for tasks within a workflow object.

```sql
SELECT
id,
completedDateTime,
failedUsersCount,
lastUpdatedDateTime,
processingStatus,
runId,
startedDateTime,
successfulUsersCount,
task,
taskDefinition,
taskProcessingResults,
totalUsersCount,
unprocessedUsersCount
FROM entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_task_reports
WHERE workflow_id = '{{ workflow_id }}' -- required
;
```
</TabItem>
</Tabs>
