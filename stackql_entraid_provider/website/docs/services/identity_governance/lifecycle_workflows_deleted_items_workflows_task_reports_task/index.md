--- 
title: lifecycle_workflows_deleted_items_workflows_task_reports_task
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_deleted_items_workflows_task_reports_task
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_deleted_items_workflows_task_reports_task</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_deleted_items_workflows_task_reports_task" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_task_reports_task" /></td></tr>
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
    <td><CopyableCode code="arguments" /></td>
    <td><code>array</code></td>
    <td>Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td> (joiner, leaver, unknownFutureValue, mover) (title: lifecycleTaskCategory)</td>
</tr>
<tr>
    <td><CopyableCode code="continueOnError" /></td>
    <td><code>boolean</code></td>
    <td>A Boolean value that specifies whether, if this task fails, the workflow stops, and subsequent tasks aren't run. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A string that describes the purpose of the task for administrative use. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.</td>
</tr>
<tr>
    <td><CopyableCode code="executionSequence" /></td>
    <td><code>number (int32)</code></td>
    <td>An integer that states in what order the task runs in a workflow.Supports $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>A Boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.</td>
</tr>
<tr>
    <td><CopyableCode code="taskDefinitionId" /></td>
    <td><code>string</code></td>
    <td>A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.Supports $filter(eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="taskProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The result of processing the task.</td>
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
    <td>The related lifecycle workflow task.Supports $filter(eq, ne) and $expand.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

The related lifecycle workflow task.Supports $filter(eq, ne) and $expand.

```sql
SELECT
id,
arguments,
category,
continueOnError,
description,
displayName,
executionSequence,
isEnabled,
taskDefinitionId,
taskProcessingResults
FROM entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_task_reports_task
WHERE workflow_id = '{{ workflow_id }}' -- required
AND task_report_id = '{{ task_report_id }}' -- required
;
```
</TabItem>
</Tabs>
