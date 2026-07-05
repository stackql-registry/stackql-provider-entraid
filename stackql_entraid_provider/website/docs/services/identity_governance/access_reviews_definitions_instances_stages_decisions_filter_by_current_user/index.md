--- 
title: access_reviews_definitions_instances_stages_decisions_filter_by_current_user
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_definitions_instances_stages_decisions_filter_by_current_user
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

Creates, updates, deletes, gets or lists an <code>access_reviews_definitions_instances_stages_decisions_filter_by_current_user</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_definitions_instances_stages_decisions_filter_by_current_user" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions_filter_by_current_user" /></td></tr>
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
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_stage_id"><code>access_review_stage_id</code></a>, <a href="#parameter-on"><code>on</code></a></td>
    <td></td>
    <td>Retrieve all decision items for an instance of an access review or a stage of an instance of a multi-stage access review, for which the calling user is the reviewer. The decision items are represented by accessReviewInstanceDecisionItem objects on a given accessReviewInstance or accessReviewStage for which the calling user is the reviewer.</td>
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
<tr id="parameter-on">
    <td><CopyableCode code="on" /></td>
    <td><code>string</code></td>
    <td>Usage: on='&#123;on&#125;'</td>
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

Retrieve all decision items for an instance of an access review or a stage of an instance of a multi-stage access review, for which the calling user is the reviewer. The decision items are represented by accessReviewInstanceDecisionItem objects on a given accessReviewInstance or accessReviewStage for which the calling user is the reviewer.

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
FROM entra_id.identity_governance.access_reviews_definitions_instances_stages_decisions_filter_by_current_user
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' -- required
AND access_review_instance_id = '{{ access_review_instance_id }}' -- required
AND access_review_stage_id = '{{ access_review_stage_id }}' -- required
AND on = '{{ on }}' -- required
;
```
</TabItem>
</Tabs>
