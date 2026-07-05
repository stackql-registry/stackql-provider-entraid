--- 
title: access_reviews_definitions_instances_stages_decisions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_definitions_instances_stages_decisions
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

Creates, updates, deletes, gets or lists an <code>access_reviews_definitions_instances_stages_decisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_definitions_instances_stages_decisions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions" /></td></tr>
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
    <td><CopyableCode code="accessReviewId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the accessReviewInstance parent. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedBy" /></td>
    <td><code></code></td>
    <td>The identifier of the user who applied the decision. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the approval decision was applied.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="applyResult" /></td>
    <td><code>string</code></td>
    <td>The result of applying the decision. Possible values: New, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound and ApplyNotSupported. Supports $select, $orderby, and $filter (eq only). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>Result of the review. Possible values: Approve, Deny, NotReviewed, or DontKnow. Supports $select, $orderby, and $filter (eq only).</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>array</code></td>
    <td>Insights are recommendations to reviewers on whether to approve or deny a decision. There can be multiple insights associated with an accessReviewInstanceDecisionItem.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification left by the reviewer when they made the decision.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is 'Bob' and the resource is 'Sales'. Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="principalLink" /></td>
    <td><code>string</code></td>
    <td>A link to the principal object. For example, https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendation" /></td>
    <td><code>string</code></td>
    <td>A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. The value is Approve if the sign-in is fewer than 30 days after the start of review, Deny if the sign-in is greater than 30 days after, or NoInfoAvailable. Possible values: Approve, Deny, or NoInfoAvailable. Supports $select, $orderby, and $filter (eq only). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code></code></td>
    <td>Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is Bob and the resource is 'Sales'. Resources can be of multiple types. See accessReviewInstanceDecisionItemResource. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLink" /></td>
    <td><code>string</code></td>
    <td>A link to the resource. For example, https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code></code></td>
    <td>The identifier of the reviewer.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the review decision occurred. Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><CopyableCode code="accessReviewId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the accessReviewInstance parent. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedBy" /></td>
    <td><code></code></td>
    <td>The identifier of the user who applied the decision. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the approval decision was applied.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="applyResult" /></td>
    <td><code>string</code></td>
    <td>The result of applying the decision. Possible values: New, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound and ApplyNotSupported. Supports $select, $orderby, and $filter (eq only). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="decision" /></td>
    <td><code>string</code></td>
    <td>Result of the review. Possible values: Approve, Deny, NotReviewed, or DontKnow. Supports $select, $orderby, and $filter (eq only).</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>array</code></td>
    <td>Insights are recommendations to reviewers on whether to approve or deny a decision. There can be multiple insights associated with an accessReviewInstanceDecisionItem.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>Justification left by the reviewer when they made the decision.</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is 'Bob' and the resource is 'Sales'. Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="principalLink" /></td>
    <td><code>string</code></td>
    <td>A link to the principal object. For example, https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendation" /></td>
    <td><code>string</code></td>
    <td>A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. The value is Approve if the sign-in is fewer than 30 days after the start of review, Deny if the sign-in is greater than 30 days after, or NoInfoAvailable. Possible values: Approve, Deny, or NoInfoAvailable. Supports $select, $orderby, and $filter (eq only). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code></code></td>
    <td>Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is Bob and the resource is 'Sales'. Resources can be of multiple types. See accessReviewInstanceDecisionItemResource. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceLink" /></td>
    <td><code>string</code></td>
    <td>A link to the resource. For example, https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedBy" /></td>
    <td><code></code></td>
    <td>The identifier of the reviewer.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the review decision occurred. Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_stage_id"><code>access_review_stage_id</code></a>, <a href="#parameter-access_review_instance_decision_item_id"><code>access_review_instance_decision_item_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of an accessReviewInstanceDecisionItem object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_stage_id"><code>access_review_stage_id</code></a></td>
    <td></td>
    <td>Get the decisions from a stage in a multi-stage access review. The decisions in an accessReviewStage object are represented by an accessReviewInstanceDecisionItem object.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_stage_id"><code>access_review_stage_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_stage_id"><code>access_review_stage_id</code></a>, <a href="#parameter-access_review_instance_decision_item_id"><code>access_review_instance_decision_item_id</code></a></td>
    <td></td>
    <td>Update access decisions, known as accessReviewInstanceDecisionItems, for which the user is the reviewer.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_stage_id"><code>access_review_stage_id</code></a>, <a href="#parameter-access_review_instance_decision_item_id"><code>access_review_instance_decision_item_id</code></a></td>
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
<tr id="parameter-access_review_instance_decision_item_id">
    <td><CopyableCode code="access_review_instance_decision_item_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewInstanceDecisionItem</td>
</tr>
<tr id="parameter-access_review_instance_id">
    <td><CopyableCode code="access_review_instance_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewInstance</td>
</tr>
<tr id="parameter-access_review_schedule_definition_id">
    <td><CopyableCode code="access_review_schedule_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewScheduleDefinition</td>
</tr>
<tr id="parameter-access_review_stage_id">
    <td><CopyableCode code="access_review_stage_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewStage</td>
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

Read the properties and relationships of an accessReviewInstanceDecisionItem object.

```sql
SELECT
id,
accessReviewId,
appliedBy,
appliedDateTime,
applyResult,
decision,
insights,
justification,
principal,
principalLink,
recommendation,
resource,
resourceLink,
reviewedBy,
reviewedDateTime
FROM entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' -- required
AND access_review_instance_id = '{{ access_review_instance_id }}' -- required
AND access_review_stage_id = '{{ access_review_stage_id }}' -- required
AND access_review_instance_decision_item_id = '{{ access_review_instance_decision_item_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the decisions from a stage in a multi-stage access review. The decisions in an accessReviewStage object are represented by an accessReviewInstanceDecisionItem object.

```sql
SELECT
id,
accessReviewId,
appliedBy,
appliedDateTime,
applyResult,
decision,
insights,
justification,
principal,
principalLink,
recommendation,
resource,
resourceLink,
reviewedBy,
reviewedDateTime
FROM entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' -- required
AND access_review_instance_id = '{{ access_review_instance_id }}' -- required
AND access_review_stage_id = '{{ access_review_stage_id }}' -- required
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
INSERT INTO entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions (
id,
accessReviewId,
appliedBy,
appliedDateTime,
applyResult,
decision,
justification,
principal,
principalLink,
recommendation,
resource,
resourceLink,
reviewedBy,
reviewedDateTime,
insights,
access_review_schedule_definition_id,
access_review_instance_id,
access_review_stage_id
)
SELECT 
'{{ id }}',
'{{ accessReviewId }}',
'{{ appliedBy }}',
'{{ appliedDateTime }}',
'{{ applyResult }}',
'{{ decision }}',
'{{ justification }}',
'{{ principal }}',
'{{ principalLink }}',
'{{ recommendation }}',
'{{ resource }}',
'{{ resourceLink }}',
'{{ reviewedBy }}',
'{{ reviewedDateTime }}',
'{{ insights }}',
'{{ access_review_schedule_definition_id }}',
'{{ access_review_instance_id }}',
'{{ access_review_stage_id }}'
RETURNING
id,
accessReviewId,
appliedBy,
appliedDateTime,
applyResult,
decision,
insights,
justification,
principal,
principalLink,
recommendation,
resource,
resourceLink,
reviewedBy,
reviewedDateTime
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_definitions_instances_stages_decisions
  props:
    - name: access_review_schedule_definition_id
      value: "{{ access_review_schedule_definition_id }}"
      description: Required parameter for the access_reviews_definitions_instances_stages_decisions resource.
    - name: access_review_instance_id
      value: "{{ access_review_instance_id }}"
      description: Required parameter for the access_reviews_definitions_instances_stages_decisions resource.
    - name: access_review_stage_id
      value: "{{ access_review_stage_id }}"
      description: Required parameter for the access_reviews_definitions_instances_stages_decisions resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: accessReviewId
      value: "{{ accessReviewId }}"
      description: |
        The identifier of the accessReviewInstance parent. Supports $select. Read-only.
    - name: appliedBy
      value: "{{ appliedBy }}"
      description: |
        The identifier of the user who applied the decision. Read-only.
    - name: appliedDateTime
      value: "{{ appliedDateTime }}"
      description: |
        The timestamp when the approval decision was applied.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't applied the decision or it was automatically applied. The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  Supports $select. Read-only.
    - name: applyResult
      value: "{{ applyResult }}"
      description: |
        The result of applying the decision. Possible values: New, AppliedSuccessfully, AppliedWithUnknownFailure, AppliedSuccessfullyButObjectNotFound and ApplyNotSupported. Supports $select, $orderby, and $filter (eq only). Read-only.
    - name: decision
      value: "{{ decision }}"
      description: |
        Result of the review. Possible values: Approve, Deny, NotReviewed, or DontKnow. Supports $select, $orderby, and $filter (eq only).
    - name: justification
      value: "{{ justification }}"
      description: |
        Justification left by the reviewer when they made the decision.
    - name: principal
      value: "{{ principal }}"
      description: |
        Every decision item in an access review represents a principal's access to a resource. This property represents details of the principal. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is 'Bob' and the resource is 'Sales'. Principals can be of two types - userIdentity and servicePrincipalIdentity. Supports $select. Read-only.
    - name: principalLink
      value: "{{ principalLink }}"
      description: |
        A link to the principal object. For example, https://graph.microsoft.com/v1.0/users/a6c7aecb-cbfd-4763-87ef-e91b4bd509d9. Read-only.
    - name: recommendation
      value: "{{ recommendation }}"
      description: |
        A system-generated recommendation for the approval decision based off last interactive sign-in to tenant. The value is Approve if the sign-in is fewer than 30 days after the start of review, Deny if the sign-in is greater than 30 days after, or NoInfoAvailable. Possible values: Approve, Deny, or NoInfoAvailable. Supports $select, $orderby, and $filter (eq only). Read-only.
    - name: resource
      value: "{{ resource }}"
      description: |
        Every decision item in an access review represents a principal's access to a resource. This property represents details of the resource. For example, if a decision item represents access of User 'Bob' to Group 'Sales' - The principal is Bob and the resource is 'Sales'. Resources can be of multiple types. See accessReviewInstanceDecisionItemResource. Read-only.
    - name: resourceLink
      value: "{{ resourceLink }}"
      description: |
        A link to the resource. For example, https://graph.microsoft.com/v1.0/servicePrincipals/c86300f3-8695-4320-9f6e-32a2555f5ff8. Supports $select. Read-only.
    - name: reviewedBy
      value: "{{ reviewedBy }}"
      description: |
        The identifier of the reviewer.00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Supports $select. Read-only.
    - name: reviewedDateTime
      value: "{{ reviewedDateTime }}"
      description: |
        The timestamp when the review decision occurred. Supports $select. Read-only.
    - name: insights
      description: |
        Insights are recommendations to reviewers on whether to approve or deny a decision. There can be multiple insights associated with an accessReviewInstanceDecisionItem.
      value:
        - id: "{{ id }}"
          insightCreatedDateTime: "{{ insightCreatedDateTime }}"
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

Update access decisions, known as accessReviewInstanceDecisionItems, for which the user is the reviewer.

```sql
UPDATE entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions
SET 
id = '{{ id }}',
accessReviewId = '{{ accessReviewId }}',
appliedBy = '{{ appliedBy }}',
appliedDateTime = '{{ appliedDateTime }}',
applyResult = '{{ applyResult }}',
decision = '{{ decision }}',
justification = '{{ justification }}',
principal = '{{ principal }}',
principalLink = '{{ principalLink }}',
recommendation = '{{ recommendation }}',
resource = '{{ resource }}',
resourceLink = '{{ resourceLink }}',
reviewedBy = '{{ reviewedBy }}',
reviewedDateTime = '{{ reviewedDateTime }}',
insights = '{{ insights }}'
WHERE 
access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' --required
AND access_review_instance_id = '{{ access_review_instance_id }}' --required
AND access_review_stage_id = '{{ access_review_stage_id }}' --required
AND access_review_instance_decision_item_id = '{{ access_review_instance_decision_item_id }}' --required
RETURNING
id,
accessReviewId,
appliedBy,
appliedDateTime,
applyResult,
decision,
insights,
justification,
principal,
principalLink,
recommendation,
resource,
resourceLink,
reviewedBy,
reviewedDateTime;
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
DELETE FROM entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' --required
AND access_review_instance_id = '{{ access_review_instance_id }}' --required
AND access_review_stage_id = '{{ access_review_stage_id }}' --required
AND access_review_instance_decision_item_id = '{{ access_review_instance_decision_item_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
