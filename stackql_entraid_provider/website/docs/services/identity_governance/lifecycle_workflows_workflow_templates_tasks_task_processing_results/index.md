--- 
title: lifecycle_workflows_workflow_templates_tasks_task_processing_results
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_workflow_templates_tasks_task_processing_results
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_workflow_templates_tasks_task_processing_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_workflow_templates_tasks_task_processing_results" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_workflow_templates_tasks_task_processing_results" /></td></tr>
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
    <td>The date time when taskProcessingResult execution ended. Value is null if task execution is still in progress.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the taskProcessingResult was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Describes why the taskProcessingResult failed.</td>
</tr>
<tr>
    <td><CopyableCode code="processingInfo" /></td>
    <td><code>string</code></td>
    <td>Additional human-readable context about the task processing outcome. This property contains information about edge cases where the task completed successfully but the expected action wasn't performed because the target was already in the desired state, such as when the user was already a member of the specified group. Returns null when no additional context is needed. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="processingStatus" /></td>
    <td><code>string</code></td>
    <td> (queued, inProgress, completed, completedWithErrors, canceled, failed, unknownFutureValue) (title: lifecycleWorkflowProcessingStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="startedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when taskProcessingResult execution started. Value is null if task execution hasn't started yet.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>object</code></td>
    <td>Represents a Microsoft Entra user account. (title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityGovernance.task, title: entity)</td>
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
    <td>The date time when taskProcessingResult execution ended. Value is null if task execution is still in progress.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when the taskProcessingResult was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="failureReason" /></td>
    <td><code>string</code></td>
    <td>Describes why the taskProcessingResult failed.</td>
</tr>
<tr>
    <td><CopyableCode code="processingInfo" /></td>
    <td><code>string</code></td>
    <td>Additional human-readable context about the task processing outcome. This property contains information about edge cases where the task completed successfully but the expected action wasn't performed because the target was already in the desired state, such as when the user was already a member of the specified group. Returns null when no additional context is needed. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="processingStatus" /></td>
    <td><code>string</code></td>
    <td> (queued, inProgress, completed, completedWithErrors, canceled, failed, unknownFutureValue) (title: lifecycleWorkflowProcessingStatus)</td>
</tr>
<tr>
    <td><CopyableCode code="startedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date time when taskProcessingResult execution started. Value is null if task execution hasn't started yet.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>object</code></td>
    <td>Represents a Microsoft Entra user account. (title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="task" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityGovernance.task, title: entity)</td>
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
    <td><a href="#parameter-workflow_template_id"><code>workflow_template_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a>, <a href="#parameter-task_processing_result_id"><code>task_processing_result_id</code></a></td>
    <td></td>
    <td>The result of processing the task.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workflow_template_id"><code>workflow_template_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a></td>
    <td></td>
    <td>The result of processing the task.</td>
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
<tr id="parameter-task_id">
    <td><CopyableCode code="task_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of task</td>
</tr>
<tr id="parameter-task_processing_result_id">
    <td><CopyableCode code="task_processing_result_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of taskProcessingResult</td>
</tr>
<tr id="parameter-workflow_template_id">
    <td><CopyableCode code="workflow_template_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of workflowTemplate</td>
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

The result of processing the task.

```sql
SELECT
id,
completedDateTime,
createdDateTime,
failureReason,
processingInfo,
processingStatus,
startedDateTime,
subject,
task
FROM entra_id.identity_governance.lifecycle_workflows_workflow_templates_tasks_task_processing_results
WHERE workflow_template_id = '{{ workflow_template_id }}' -- required
AND task_id = '{{ task_id }}' -- required
AND task_processing_result_id = '{{ task_processing_result_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The result of processing the task.

```sql
SELECT
id,
completedDateTime,
createdDateTime,
failureReason,
processingInfo,
processingStatus,
startedDateTime,
subject,
task
FROM entra_id.identity_governance.lifecycle_workflows_workflow_templates_tasks_task_processing_results
WHERE workflow_template_id = '{{ workflow_template_id }}' -- required
AND task_id = '{{ task_id }}' -- required
;
```
</TabItem>
</Tabs>
