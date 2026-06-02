--- 
title: access_reviews_definitions_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_definitions_instances
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

Creates, updates, deletes, gets or lists an <code>access_reviews_definitions_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_definitions_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.access_reviews_definitions_instances" /></td></tr>
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
    <td><CopyableCode code="contactedReviewers" /></td>
    <td><code>array</code></td>
    <td>Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="decisions" /></td>
    <td><code>array</code></td>
    <td>Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when review instance is scheduled to end.The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="fallbackReviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. Supports $select.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of access review scopes is used to define who the reviewers are. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code></code></td>
    <td>Created based on scope and instanceEnumerationScope at the accessReviewScheduleDefinition level. Defines the scope of users reviewed in a group. Supports $select and $filter (contains only). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>If the instance has multiple stages, this returns the collection of stages. A new stage will only be created when the previous stage ends. The existence, number, and settings of stages on a review instance are created based on the accessReviewStageSettings on the parent accessReviewScheduleDefinition.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when review instance is scheduled to start. May be in the future. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies the status of an accessReview. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $select, $orderby, and $filter (eq only). Read-only.</td>
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
    <td><CopyableCode code="contactedReviewers" /></td>
    <td><code>array</code></td>
    <td>Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="decisions" /></td>
    <td><code>array</code></td>
    <td>Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when review instance is scheduled to end.The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="fallbackReviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. Supports $select.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of access review scopes is used to define who the reviewers are. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code></code></td>
    <td>Created based on scope and instanceEnumerationScope at the accessReviewScheduleDefinition level. Defines the scope of users reviewed in a group. Supports $select and $filter (contains only). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>If the instance has multiple stages, this returns the collection of stages. A new stage will only be created when the previous stage ends. The existence, number, and settings of stages on a review instance are created based on the accessReviewStageSettings on the parent accessReviewScheduleDefinition.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime when review instance is scheduled to start. May be in the future. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies the status of an accessReview. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $select, $orderby, and $filter (eq only). Read-only.</td>
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
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of an accessReviewInstance object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of the accessReviewInstance objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of an accessReviewInstance object. Only the reviewers and fallbackReviewers properties can be updated but the scope property is also required in the request body. You can only add reviewers to the fallbackReviewers property but can't remove existing fallbackReviewers. To update an accessReviewInstance, it's status must be InProgress.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#accept_recommendations"><CopyableCode code="accept_recommendations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td></td>
    <td>Allows the acceptance of recommendations on all accessReviewInstanceDecisionItem objects that haven't been reviewed on an accessReviewInstance object for which the calling user is a reviewer.</td>
</tr>
<tr>
    <td><a href="#apply_decisions"><CopyableCode code="apply_decisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td></td>
    <td>Apply review decisions on an accessReviewInstance if the decisions were not applied automatically because the autoApplyDecisionsEnabled property is false in the review's accessReviewScheduleSettings. The status of the accessReviewInstance must be Completed to call this method.</td>
</tr>
<tr>
    <td><a href="#reset_decisions"><CopyableCode code="reset_decisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td></td>
    <td>Resets all accessReviewInstanceDecisionItem objects on an accessReviewInstance to notReviewed.</td>
</tr>
<tr>
    <td><a href="#send_reminder"><CopyableCode code="send_reminder" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td></td>
    <td>Send a reminder to the reviewers of an active accessReviewInstance.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td></td>
    <td>Stop a currently active accessReviewInstance. After the access review instance stops, the instance status is marked as Completed, the reviewers can no longer give input, and the access review decisions are applied. Stopping an instance will not stop future instances. To prevent a recurring access review from starting future instances, update the schedule definition to change its scheduled end date.</td>
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

Read the properties and relationships of an accessReviewInstance object.

```sql
SELECT
id,
@odata.type,
contactedReviewers,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
scope,
stages,
startDateTime,
status
FROM entraid.identity_governance.access_reviews_definitions_instances
WHERE accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' -- required
AND accessReviewInstance-id = '{{ accessReviewInstance-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of the accessReviewInstance objects and their properties.

```sql
SELECT
id,
@odata.type,
contactedReviewers,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
scope,
stages,
startDateTime,
status
FROM entraid.identity_governance.access_reviews_definitions_instances
WHERE accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' -- required
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
INSERT INTO entraid.identity_governance.access_reviews_definitions_instances (
id,
@odata.type,
endDateTime,
fallbackReviewers,
reviewers,
scope,
startDateTime,
status,
contactedReviewers,
decisions,
stages,
accessReviewScheduleDefinition-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ endDateTime }}',
'{{ fallbackReviewers }}',
'{{ reviewers }}',
'{{ scope }}',
'{{ startDateTime }}',
'{{ status }}',
'{{ contactedReviewers }}',
'{{ decisions }}',
'{{ stages }}',
'{{ accessReviewScheduleDefinition-id }}'
RETURNING
id,
@odata.type,
contactedReviewers,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
scope,
stages,
startDateTime,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_definitions_instances
  props:
    - name: accessReviewScheduleDefinition-id
      value: "{{ accessReviewScheduleDefinition-id }}"
      description: Required parameter for the access_reviews_definitions_instances resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: endDateTime
      value: "{{ endDateTime }}"
      description: |
        DateTime when review instance is scheduled to end.The DatetimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
    - name: fallbackReviewers
      description: |
        This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. Supports $select.
      value:
        - query: "{{ query }}"
          queryRoot: "{{ queryRoot }}"
          queryType: "{{ queryType }}"
          @odata.type: "{{ @odata.type }}"
    - name: reviewers
      description: |
        This collection of access review scopes is used to define who the reviewers are. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
      value:
        - query: "{{ query }}"
          queryRoot: "{{ queryRoot }}"
          queryType: "{{ queryType }}"
          @odata.type: "{{ @odata.type }}"
    - name: scope
      value: "{{ scope }}"
      description: |
        Created based on scope and instanceEnumerationScope at the accessReviewScheduleDefinition level. Defines the scope of users reviewed in a group. Supports $select and $filter (contains only). Read-only.
    - name: startDateTime
      value: "{{ startDateTime }}"
      description: |
        DateTime when review instance is scheduled to start. May be in the future. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $select. Read-only.
    - name: status
      value: "{{ status }}"
      description: |
        Specifies the status of an accessReview. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $select, $orderby, and $filter (eq only). Read-only.
    - name: contactedReviewers
      description: |
        Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdDateTime: "{{ createdDateTime }}"
          displayName: "{{ displayName }}"
          userPrincipalName: "{{ userPrincipalName }}"
    - name: decisions
      description: |
        Each user reviewed in an accessReviewInstance has a decision item representing if they were approved, denied, or not yet reviewed.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          accessReviewId: "{{ accessReviewId }}"
          appliedBy: "{{ appliedBy }}"
          appliedDateTime: "{{ appliedDateTime }}"
          applyResult: "{{ applyResult }}"
          decision: "{{ decision }}"
          justification: "{{ justification }}"
          principal: "{{ principal }}"
          principalLink: "{{ principalLink }}"
          recommendation: "{{ recommendation }}"
          resource: "{{ resource }}"
          resourceLink: "{{ resourceLink }}"
          reviewedBy: "{{ reviewedBy }}"
          reviewedDateTime: "{{ reviewedDateTime }}"
          insights: "{{ insights }}"
    - name: stages
      description: |
        If the instance has multiple stages, this returns the collection of stages. A new stage will only be created when the previous stage ends. The existence, number, and settings of stages on a review instance are created based on the accessReviewStageSettings on the parent accessReviewScheduleDefinition.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          endDateTime: "{{ endDateTime }}"
          fallbackReviewers: "{{ fallbackReviewers }}"
          reviewers: "{{ reviewers }}"
          startDateTime: "{{ startDateTime }}"
          status: "{{ status }}"
          decisions: "{{ decisions }}"
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

Update the properties of an accessReviewInstance object. Only the reviewers and fallbackReviewers properties can be updated but the scope property is also required in the request body. You can only add reviewers to the fallbackReviewers property but can't remove existing fallbackReviewers. To update an accessReviewInstance, it's status must be InProgress.

```sql
UPDATE entraid.identity_governance.access_reviews_definitions_instances
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
endDateTime = '{{ endDateTime }}',
fallbackReviewers = '{{ fallbackReviewers }}',
reviewers = '{{ reviewers }}',
scope = '{{ scope }}',
startDateTime = '{{ startDateTime }}',
status = '{{ status }}',
contactedReviewers = '{{ contactedReviewers }}',
decisions = '{{ decisions }}',
stages = '{{ stages }}'
WHERE 
accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' --required
AND accessReviewInstance-id = '{{ accessReviewInstance-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
contactedReviewers,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
scope,
stages,
startDateTime,
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
DELETE FROM entraid.identity_governance.access_reviews_definitions_instances
WHERE accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' --required
AND accessReviewInstance-id = '{{ accessReviewInstance-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="accept_recommendations"
    values={[
        { label: 'accept_recommendations', value: 'accept_recommendations' },
        { label: 'apply_decisions', value: 'apply_decisions' },
        { label: 'reset_decisions', value: 'reset_decisions' },
        { label: 'send_reminder', value: 'send_reminder' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="accept_recommendations">

Allows the acceptance of recommendations on all accessReviewInstanceDecisionItem objects that haven't been reviewed on an accessReviewInstance object for which the calling user is a reviewer.

```sql
EXEC entraid.identity_governance.access_reviews_definitions_instances.accept_recommendations 
@accessReviewScheduleDefinition-id='{{ accessReviewScheduleDefinition-id }}' --required, 
@accessReviewInstance-id='{{ accessReviewInstance-id }}' --required
;
```
</TabItem>
<TabItem value="apply_decisions">

Apply review decisions on an accessReviewInstance if the decisions were not applied automatically because the autoApplyDecisionsEnabled property is false in the review's accessReviewScheduleSettings. The status of the accessReviewInstance must be Completed to call this method.

```sql
EXEC entraid.identity_governance.access_reviews_definitions_instances.apply_decisions 
@accessReviewScheduleDefinition-id='{{ accessReviewScheduleDefinition-id }}' --required, 
@accessReviewInstance-id='{{ accessReviewInstance-id }}' --required
;
```
</TabItem>
<TabItem value="reset_decisions">

Resets all accessReviewInstanceDecisionItem objects on an accessReviewInstance to notReviewed.

```sql
EXEC entraid.identity_governance.access_reviews_definitions_instances.reset_decisions 
@accessReviewScheduleDefinition-id='{{ accessReviewScheduleDefinition-id }}' --required, 
@accessReviewInstance-id='{{ accessReviewInstance-id }}' --required
;
```
</TabItem>
<TabItem value="send_reminder">

Send a reminder to the reviewers of an active accessReviewInstance.

```sql
EXEC entraid.identity_governance.access_reviews_definitions_instances.send_reminder 
@accessReviewScheduleDefinition-id='{{ accessReviewScheduleDefinition-id }}' --required, 
@accessReviewInstance-id='{{ accessReviewInstance-id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop a currently active accessReviewInstance. After the access review instance stops, the instance status is marked as Completed, the reviewers can no longer give input, and the access review decisions are applied. Stopping an instance will not stop future instances. To prevent a recurring access review from starting future instances, update the schedule definition to change its scheduled end date.

```sql
EXEC entraid.identity_governance.access_reviews_definitions_instances.stop 
@accessReviewScheduleDefinition-id='{{ accessReviewScheduleDefinition-id }}' --required, 
@accessReviewInstance-id='{{ accessReviewInstance-id }}' --required
;
```
</TabItem>
</Tabs>
