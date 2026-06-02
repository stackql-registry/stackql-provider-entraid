--- 
title: access_reviews_history_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_history_definitions
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

Creates, updates, deletes, gets or lists an <code>access_reviews_history_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_history_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.access_reviews_history_definitions" /></td></tr>
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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.userIdentity, title: identity)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the access review definition was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="decisions" /></td>
    <td><code>array</code></td>
    <td>Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions are included by default if no decisions are provided on create. The possible values are: approve, deny, dontKnow, notReviewed, and notNotified.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name for the access review history data collection. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that doesn't recur will have exactly one instance.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleSettings" /></td>
    <td><code></code></td>
    <td>The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime aren't defined. Not supported yet.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.</td>
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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.userIdentity, title: identity)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the access review definition was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="decisions" /></td>
    <td><code>array</code></td>
    <td>Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions are included by default if no decisions are provided on create. The possible values are: approve, deny, dontKnow, notReviewed, and notNotified.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name for the access review history data collection. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that doesn't recur will have exactly one instance.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleSettings" /></td>
    <td><code></code></td>
    <td>The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime aren't defined. Not supported yet.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.</td>
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
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve an accessReviewHistoryDefinition object by its identifier. All the properties of the access review history definition object are returned. If the definition is 30 days or older, a 404 Not Found error is returned.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the accessReviewHistoryDefinition objects created in the last 30 days, including all nested properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new accessReviewHistoryDefinition object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a></td>
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
<tr id="parameter-accessReviewHistoryDefinition-id">
    <td><CopyableCode code="accessReviewHistoryDefinition-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewHistoryDefinition</td>
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

Retrieve an accessReviewHistoryDefinition object by its identifier. All the properties of the access review history definition object are returned. If the definition is 30 days or older, a 404 Not Found error is returned.

```sql
SELECT
id,
@odata.type,
createdBy,
createdDateTime,
decisions,
displayName,
instances,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
scheduleSettings,
scopes,
status
FROM entra_id.identity_governance.access_reviews_history_definitions
WHERE accessReviewHistoryDefinition-id = '{{ accessReviewHistoryDefinition-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve the accessReviewHistoryDefinition objects created in the last 30 days, including all nested properties.

```sql
SELECT
id,
@odata.type,
createdBy,
createdDateTime,
decisions,
displayName,
instances,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
scheduleSettings,
scopes,
status
FROM entra_id.identity_governance.access_reviews_history_definitions
WHERE $top = '{{ $top }}'
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

Create a new accessReviewHistoryDefinition object.

```sql
INSERT INTO entra_id.identity_governance.access_reviews_history_definitions (
id,
@odata.type,
createdBy,
createdDateTime,
decisions,
displayName,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
scheduleSettings,
scopes,
status,
instances
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ createdBy }}',
'{{ createdDateTime }}',
'{{ decisions }}',
'{{ displayName }}',
'{{ reviewHistoryPeriodEndDateTime }}',
'{{ reviewHistoryPeriodStartDateTime }}',
'{{ scheduleSettings }}',
'{{ scopes }}',
'{{ status }}',
'{{ instances }}'
RETURNING
id,
@odata.type,
createdBy,
createdDateTime,
decisions,
displayName,
instances,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
scheduleSettings,
scopes,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_history_definitions
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: createdBy
      value:
        displayName: "{{ displayName }}"
        id: "{{ id }}"
        @odata.type: "{{ @odata.type }}"
        ipAddress: "{{ ipAddress }}"
        userPrincipalName: "{{ userPrincipalName }}"
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        Timestamp when the access review definition was created.
    - name: decisions
      value: "{{ decisions }}"
      description: |
        Determines which review decisions will be included in the fetched review history data if specified. Optional on create. All decisions are included by default if no decisions are provided on create. The possible values are: approve, deny, dontKnow, notReviewed, and notNotified.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Name for the access review history data collection. Required.
    - name: reviewHistoryPeriodEndDateTime
      value: "{{ reviewHistoryPeriodEndDateTime }}"
      description: |
        A timestamp. Reviews ending on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined.
    - name: reviewHistoryPeriodStartDateTime
      value: "{{ reviewHistoryPeriodStartDateTime }}"
      description: |
        A timestamp. Reviews starting on or before this date will be included in the fetched history data. Only required if scheduleSettings isn't defined.
    - name: scheduleSettings
      value: "{{ scheduleSettings }}"
      description: |
        The settings for a recurring access review history definition series. Only required if reviewHistoryPeriodStartDateTime or reviewHistoryPeriodEndDateTime aren't defined. Not supported yet.
    - name: scopes
      description: |
        Used to scope what reviews are included in the fetched history data. Fetches reviews whose scope matches with this provided scope. Required.
      value:
        - @odata.type: "{{ @odata.type }}"
    - name: status
      value: "{{ status }}"
      description: |
        Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue.
    - name: instances
      description: |
        If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that doesn't recur will have exactly one instance.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          downloadUri: "{{ downloadUri }}"
          expirationDateTime: "{{ expirationDateTime }}"
          fulfilledDateTime: "{{ fulfilledDateTime }}"
          reviewHistoryPeriodEndDateTime: "{{ reviewHistoryPeriodEndDateTime }}"
          reviewHistoryPeriodStartDateTime: "{{ reviewHistoryPeriodStartDateTime }}"
          runDateTime: "{{ runDateTime }}"
          status: "{{ status }}"
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
UPDATE entra_id.identity_governance.access_reviews_history_definitions
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
createdBy = '{{ createdBy }}',
createdDateTime = '{{ createdDateTime }}',
decisions = '{{ decisions }}',
displayName = '{{ displayName }}',
reviewHistoryPeriodEndDateTime = '{{ reviewHistoryPeriodEndDateTime }}',
reviewHistoryPeriodStartDateTime = '{{ reviewHistoryPeriodStartDateTime }}',
scheduleSettings = '{{ scheduleSettings }}',
scopes = '{{ scopes }}',
status = '{{ status }}',
instances = '{{ instances }}'
WHERE 
accessReviewHistoryDefinition-id = '{{ accessReviewHistoryDefinition-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
createdBy,
createdDateTime,
decisions,
displayName,
instances,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
scheduleSettings,
scopes,
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
DELETE FROM entra_id.identity_governance.access_reviews_history_definitions
WHERE accessReviewHistoryDefinition-id = '{{ accessReviewHistoryDefinition-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
