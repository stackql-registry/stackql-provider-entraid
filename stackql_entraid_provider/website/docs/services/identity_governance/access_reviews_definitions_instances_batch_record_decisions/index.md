--- 
title: access_reviews_definitions_instances_batch_record_decisions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_definitions_instances_batch_record_decisions
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

Creates, updates, deletes, gets or lists an <code>access_reviews_definitions_instances_batch_record_decisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_definitions_instances_batch_record_decisions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.access_reviews_definitions_instances_batch_record_decisions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td></td>
    <td>Enables reviewers to review all accessReviewInstanceDecisionItem objects in batches by using principalId, resourceId, or neither.</td>
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
<tr id="parameter-accessReviewInstance-id">
    <td><CopyableCode code="accessReviewInstance-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewInstance</td>
</tr>
<tr id="parameter-accessReviewScheduleDefinition-id">
    <td><CopyableCode code="accessReviewScheduleDefinition-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewScheduleDefinition</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="insert"
    values={[
        { label: 'insert', value: 'insert' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="insert">

Enables reviewers to review all accessReviewInstanceDecisionItem objects in batches by using principalId, resourceId, or neither.

```sql
INSERT INTO entra_id.identity_governance.access_reviews_definitions_instances_batch_record_decisions (
decision,
justification,
principalId,
resourceId,
accessReviewScheduleDefinition-id,
accessReviewInstance-id
)
SELECT 
'{{ decision }}',
'{{ justification }}',
'{{ principalId }}',
'{{ resourceId }}',
'{{ accessReviewScheduleDefinition-id }}',
'{{ accessReviewInstance-id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_definitions_instances_batch_record_decisions
  props:
    - name: accessReviewScheduleDefinition-id
      value: "{{ accessReviewScheduleDefinition-id }}"
      description: Required parameter for the access_reviews_definitions_instances_batch_record_decisions resource.
    - name: accessReviewInstance-id
      value: "{{ accessReviewInstance-id }}"
      description: Required parameter for the access_reviews_definitions_instances_batch_record_decisions resource.
    - name: decision
      value: "{{ decision }}"
    - name: justification
      value: "{{ justification }}"
    - name: principalId
      value: "{{ principalId }}"
    - name: resourceId
      value: "{{ resourceId }}"
`}</CodeBlock>

</TabItem>
</Tabs>
