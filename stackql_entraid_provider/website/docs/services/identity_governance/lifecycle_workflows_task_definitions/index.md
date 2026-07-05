--- 
title: lifecycle_workflows_task_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_task_definitions
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_task_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_task_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_task_definitions" /></td></tr>
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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td> (joiner, leaver, unknownFutureValue, mover) (title: lifecycleTaskCategory)</td>
</tr>
<tr>
    <td><CopyableCode code="continueOnError" /></td>
    <td><code>boolean</code></td>
    <td>Defines if the workflow will continue if the task has an error.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the taskDefinition.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the taskDefinition.Supports $filter(eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>The parameters that must be supplied when creating a workflow task object.Supports $filter(any).</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>number (int32)</code></td>
    <td>The version number of the taskDefinition. New records are pushed when we add support for new parameters.Supports $filter(ge, gt, le, lt, eq, ne) and $orderby.</td>
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
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td> (joiner, leaver, unknownFutureValue, mover) (title: lifecycleTaskCategory)</td>
</tr>
<tr>
    <td><CopyableCode code="continueOnError" /></td>
    <td><code>boolean</code></td>
    <td>Defines if the workflow will continue if the task has an error.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the taskDefinition.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the taskDefinition.Supports $filter(eq, ne) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>The parameters that must be supplied when creating a workflow task object.Supports $filter(any).</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>number (int32)</code></td>
    <td>The version number of the taskDefinition. New records are pushed when we add support for new parameters.Supports $filter(ge, gt, le, lt, eq, ne) and $orderby.</td>
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
    <td><a href="#parameter-task_definition_id"><code>task_definition_id</code></a></td>
    <td></td>
    <td>Read the details of a built-in workflow task in Lifecycle Workflows.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of built-in tasks in Lifecycle Workflows. A task is represented by the taskDefinition object.</td>
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
<tr id="parameter-task_definition_id">
    <td><CopyableCode code="task_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of taskDefinition</td>
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

Read the details of a built-in workflow task in Lifecycle Workflows.

```sql
SELECT
id,
category,
continueOnError,
description,
displayName,
parameters,
version
FROM entra_id.identity_governance.lifecycle_workflows_task_definitions
WHERE task_definition_id = '{{ task_definition_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of built-in tasks in Lifecycle Workflows. A task is represented by the taskDefinition object.

```sql
SELECT
id,
category,
continueOnError,
description,
displayName,
parameters,
version
FROM entra_id.identity_governance.lifecycle_workflows_task_definitions
;
```
</TabItem>
</Tabs>
