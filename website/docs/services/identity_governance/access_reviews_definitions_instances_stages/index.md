--- 
title: access_reviews_definitions_instances_stages
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_definitions_instances_stages
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

Creates, updates, deletes, gets or lists an <code>access_reviews_definitions_instances_stages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_definitions_instances_stages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.access_reviews_definitions_instances_stages" /></td></tr>
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
    <td><CopyableCode code="decisions" /></td>
    <td><code>array</code></td>
    <td>Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and UTC time when the review stage is scheduled to end. This property is the cumulative total of the durationInDays for all stages. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="fallbackReviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of access review scopes is used to define who the reviewers are. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and UTC time when the review stage is scheduled to start. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies the status of an accessReviewStage. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $orderby, and $filter (eq only). Read-only.</td>
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
    <td><CopyableCode code="decisions" /></td>
    <td><code>array</code></td>
    <td>Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and UTC time when the review stage is scheduled to end. This property is the cumulative total of the durationInDays for all stages. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="fallbackReviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of access review scopes is used to define who the reviewers are. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and UTC time when the review stage is scheduled to start. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Specifies the status of an accessReviewStage. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $orderby, and $filter (eq only). Read-only.</td>
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
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a>, <a href="#parameter-accessReviewStage-id"><code>accessReviewStage-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of an accessReviewStage object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the stages in a multi-stage access review instance.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a>, <a href="#parameter-accessReviewStage-id"><code>accessReviewStage-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of an accessReviewStage object. Only the reviewers and fallbackReviewers properties can be updated. You can only add reviewers to the fallbackReviewers property but can't remove existing fallbackReviewers. To update an accessReviewStage, its status must be NotStarted, Initializing, or InProgress.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a>, <a href="#parameter-accessReviewStage-id"><code>accessReviewStage-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessReviewScheduleDefinition-id"><code>accessReviewScheduleDefinition-id</code></a>, <a href="#parameter-accessReviewInstance-id"><code>accessReviewInstance-id</code></a>, <a href="#parameter-accessReviewStage-id"><code>accessReviewStage-id</code></a></td>
    <td></td>
    <td>Stop an access review stage that is inProgress. After the access review stage stops, the stage status will be Completed and the reviewers can no longer give input. If there are subsequent stages that depend on the completed stage, the next stage will be created.  The accessReviewInstanceDecisionItem objects will always reflect the last decisions recorded across all stages at that given time, regardless of the status of the stages.</td>
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
<tr id="parameter-accessReviewStage-id">
    <td><CopyableCode code="accessReviewStage-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewStage</td>
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

Retrieve the properties and relationships of an accessReviewStage object.

```sql
SELECT
id,
@odata.type,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
startDateTime,
status
FROM entraid.identity_governance.access_reviews_definitions_instances_stages
WHERE accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' -- required
AND accessReviewInstance-id = '{{ accessReviewInstance-id }}' -- required
AND accessReviewStage-id = '{{ accessReviewStage-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve the stages in a multi-stage access review instance.

```sql
SELECT
id,
@odata.type,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
startDateTime,
status
FROM entraid.identity_governance.access_reviews_definitions_instances_stages
WHERE accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' -- required
AND accessReviewInstance-id = '{{ accessReviewInstance-id }}' -- required
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
INSERT INTO entraid.identity_governance.access_reviews_definitions_instances_stages (
id,
@odata.type,
endDateTime,
fallbackReviewers,
reviewers,
startDateTime,
status,
decisions,
accessReviewScheduleDefinition-id,
accessReviewInstance-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ endDateTime }}',
'{{ fallbackReviewers }}',
'{{ reviewers }}',
'{{ startDateTime }}',
'{{ status }}',
'{{ decisions }}',
'{{ accessReviewScheduleDefinition-id }}',
'{{ accessReviewInstance-id }}'
RETURNING
id,
@odata.type,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
startDateTime,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_definitions_instances_stages
  props:
    - name: accessReviewScheduleDefinition-id
      value: "{{ accessReviewScheduleDefinition-id }}"
      description: Required parameter for the access_reviews_definitions_instances_stages resource.
    - name: accessReviewInstance-id
      value: "{{ accessReviewInstance-id }}"
      description: Required parameter for the access_reviews_definitions_instances_stages resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: endDateTime
      value: "{{ endDateTime }}"
      description: |
        The date and time in ISO 8601 format and UTC time when the review stage is scheduled to end. This property is the cumulative total of the durationInDays for all stages. Read-only.
    - name: fallbackReviewers
      description: |
        This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist.
      value:
        - query: "{{ query }}"
          queryRoot: "{{ queryRoot }}"
          queryType: "{{ queryType }}"
          @odata.type: "{{ @odata.type }}"
    - name: reviewers
      description: |
        This collection of access review scopes is used to define who the reviewers are. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API.
      value:
        - query: "{{ query }}"
          queryRoot: "{{ queryRoot }}"
          queryType: "{{ queryType }}"
          @odata.type: "{{ @odata.type }}"
    - name: startDateTime
      value: "{{ startDateTime }}"
      description: |
        The date and time in ISO 8601 format and UTC time when the review stage is scheduled to start. Read-only.
    - name: status
      value: "{{ status }}"
      description: |
        Specifies the status of an accessReviewStage. Possible values: Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed. Supports $orderby, and $filter (eq only). Read-only.
    - name: decisions
      description: |
        Each user reviewed in an accessReviewStage has a decision item representing if they were approved, denied, or not yet reviewed.
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

Update the properties of an accessReviewStage object. Only the reviewers and fallbackReviewers properties can be updated. You can only add reviewers to the fallbackReviewers property but can't remove existing fallbackReviewers. To update an accessReviewStage, its status must be NotStarted, Initializing, or InProgress.

```sql
UPDATE entraid.identity_governance.access_reviews_definitions_instances_stages
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
endDateTime = '{{ endDateTime }}',
fallbackReviewers = '{{ fallbackReviewers }}',
reviewers = '{{ reviewers }}',
startDateTime = '{{ startDateTime }}',
status = '{{ status }}',
decisions = '{{ decisions }}'
WHERE 
accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' --required
AND accessReviewInstance-id = '{{ accessReviewInstance-id }}' --required
AND accessReviewStage-id = '{{ accessReviewStage-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
decisions,
endDateTime,
fallbackReviewers,
reviewers,
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
DELETE FROM entraid.identity_governance.access_reviews_definitions_instances_stages
WHERE accessReviewScheduleDefinition-id = '{{ accessReviewScheduleDefinition-id }}' --required
AND accessReviewInstance-id = '{{ accessReviewInstance-id }}' --required
AND accessReviewStage-id = '{{ accessReviewStage-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="stop"
    values={[
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="stop">

Stop an access review stage that is inProgress. After the access review stage stops, the stage status will be Completed and the reviewers can no longer give input. If there are subsequent stages that depend on the completed stage, the next stage will be created.  The accessReviewInstanceDecisionItem objects will always reflect the last decisions recorded across all stages at that given time, regardless of the status of the stages.

```sql
EXEC entraid.identity_governance.access_reviews_definitions_instances_stages.stop 
@accessReviewScheduleDefinition-id='{{ accessReviewScheduleDefinition-id }}' --required, 
@accessReviewInstance-id='{{ accessReviewInstance-id }}' --required, 
@accessReviewStage-id='{{ accessReviewStage-id }}' --required
;
```
</TabItem>
</Tabs>
