--- 
title: privileged_access_group_assignment_approvals_stages
hide_title: false
hide_table_of_contents: false
keywords:
  - privileged_access_group_assignment_approvals_stages
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

Creates, updates, deletes, gets or lists a <code>privileged_access_group_assignment_approvals_stages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="privileged_access_group_assignment_approvals_stages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.privileged_access_group_assignment_approvals_stages" /></td></tr>
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
    <td><CopyableCode code="assignedToMe" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the stage is assigned to the calling user to review. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The label provided by the policy creator to identify an approval stage. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>The justification associated with the approval stage decision.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewResult" /></td>
    <td><code>string</code></td>
    <td>The result of this approval record. Possible values include: NotReviewed, Approved, Denied.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code></code></td>
    <td>The identifier of the reviewer. 00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when a decision was recorded. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The stage status. Possible values: InProgress, Initializing, Completed, Expired. Read-only.</td>
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
    <td><CopyableCode code="assignedToMe" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the stage is assigned to the calling user to review. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The label provided by the policy creator to identify an approval stage. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>The justification associated with the approval stage decision.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewResult" /></td>
    <td><code>string</code></td>
    <td>The result of this approval record. Possible values include: NotReviewed, Approved, Denied.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code></code></td>
    <td>The identifier of the reviewer. 00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when a decision was recorded. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The stage status. Possible values: InProgress, Initializing, Completed, Expired. Read-only.</td>
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
    <td><a href="#parameter-approval_id"><code>approval_id</code></a>, <a href="#parameter-approval_stage_id"><code>approval_stage_id</code></a></td>
    <td></td>
    <td>A collection of stages in the approval decision.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-approval_id"><code>approval_id</code></a></td>
    <td></td>
    <td>A collection of stages in the approval decision.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-approval_id"><code>approval_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-approval_id"><code>approval_id</code></a>, <a href="#parameter-approval_stage_id"><code>approval_stage_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-approval_id"><code>approval_id</code></a>, <a href="#parameter-approval_stage_id"><code>approval_stage_id</code></a></td>
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
<tr id="parameter-approval_id">
    <td><CopyableCode code="approval_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of approval</td>
</tr>
<tr id="parameter-approval_stage_id">
    <td><CopyableCode code="approval_stage_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of approvalStage</td>
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

A collection of stages in the approval decision.

```sql
SELECT
id,
assignedToMe,
displayName,
justification,
reviewResult,
reviewedBy,
reviewedDateTime,
status
FROM entra_id.identity_governance.privileged_access_group_assignment_approvals_stages
WHERE approval_id = '{{ approval_id }}' -- required
AND approval_stage_id = '{{ approval_stage_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

A collection of stages in the approval decision.

```sql
SELECT
id,
assignedToMe,
displayName,
justification,
reviewResult,
reviewedBy,
reviewedDateTime,
status
FROM entra_id.identity_governance.privileged_access_group_assignment_approvals_stages
WHERE approval_id = '{{ approval_id }}' -- required
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
INSERT INTO entra_id.identity_governance.privileged_access_group_assignment_approvals_stages (
id,
assignedToMe,
displayName,
justification,
reviewedBy,
reviewedDateTime,
reviewResult,
status,
approval_id
)
SELECT 
'{{ id }}',
{{ assignedToMe }},
'{{ displayName }}',
'{{ justification }}',
'{{ reviewedBy }}',
'{{ reviewedDateTime }}',
'{{ reviewResult }}',
'{{ status }}',
'{{ approval_id }}'
RETURNING
id,
assignedToMe,
displayName,
justification,
reviewResult,
reviewedBy,
reviewedDateTime,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: privileged_access_group_assignment_approvals_stages
  props:
    - name: approval_id
      value: "{{ approval_id }}"
      description: Required parameter for the privileged_access_group_assignment_approvals_stages resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: assignedToMe
      value: {{ assignedToMe }}
      description: |
        Indicates whether the stage is assigned to the calling user to review. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The label provided by the policy creator to identify an approval stage. Read-only.
    - name: justification
      value: "{{ justification }}"
      description: |
        The justification associated with the approval stage decision.
    - name: reviewedBy
      value: "{{ reviewedBy }}"
      description: |
        The identifier of the reviewer. 00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Read-only.
    - name: reviewedDateTime
      value: "{{ reviewedDateTime }}"
      description: |
        The date and time when a decision was recorded. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: reviewResult
      value: "{{ reviewResult }}"
      description: |
        The result of this approval record. Possible values include: NotReviewed, Approved, Denied.
    - name: status
      value: "{{ status }}"
      description: |
        The stage status. Possible values: InProgress, Initializing, Completed, Expired. Read-only.
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
UPDATE entra_id.identity_governance.privileged_access_group_assignment_approvals_stages
SET 
id = '{{ id }}',
assignedToMe = {{ assignedToMe }},
displayName = '{{ displayName }}',
justification = '{{ justification }}',
reviewedBy = '{{ reviewedBy }}',
reviewedDateTime = '{{ reviewedDateTime }}',
reviewResult = '{{ reviewResult }}',
status = '{{ status }}'
WHERE 
approval_id = '{{ approval_id }}' --required
AND approval_stage_id = '{{ approval_stage_id }}' --required
RETURNING
id,
assignedToMe,
displayName,
justification,
reviewResult,
reviewedBy,
reviewedDateTime,
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
DELETE FROM entra_id.identity_governance.privileged_access_group_assignment_approvals_stages
WHERE approval_id = '{{ approval_id }}' --required
AND approval_stage_id = '{{ approval_stage_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
