--- 
title: lifecycle_workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows" /></td></tr>
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
    <td><CopyableCode code="customTaskExtensions" /></td>
    <td><code>array</code></td>
    <td>The customTaskExtension instance.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedItems" /></td>
    <td><code></code></td>
    <td>Deleted workflows in your lifecycle workflows instance.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code></code></td>
    <td>The insight container holding workflow insight summaries for a tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityGovernance.lifecycleManagementSettings, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="taskDefinitions" /></td>
    <td><code>array</code></td>
    <td>The definition of tasks within the lifecycle workflows instance.</td>
</tr>
<tr>
    <td><CopyableCode code="workflowTemplates" /></td>
    <td><code>array</code></td>
    <td>The workflow templates in the lifecycle workflow instance.</td>
</tr>
<tr>
    <td><CopyableCode code="workflows" /></td>
    <td><code>array</code></td>
    <td>The workflows in the lifecycle workflows instance.</td>
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
    <td></td>
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

Retrieved navigation property

```sql
SELECT
id,
@odata.type,
customTaskExtensions,
deletedItems,
insights,
settings,
taskDefinitions,
workflowTemplates,
workflows
FROM entra_id.identity_governance.lifecycle_workflows
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
UPDATE entra_id.identity_governance.lifecycle_workflows
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
customTaskExtensions = '{{ customTaskExtensions }}',
deletedItems = '{{ deletedItems }}',
insights = '{{ insights }}',
settings = '{{ settings }}',
taskDefinitions = '{{ taskDefinitions }}',
workflows = '{{ workflows }}',
workflowTemplates = '{{ workflowTemplates }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
customTaskExtensions,
deletedItems,
insights,
settings,
taskDefinitions,
workflowTemplates,
workflows;
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
DELETE FROM entra_id.identity_governance.lifecycle_workflows
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
