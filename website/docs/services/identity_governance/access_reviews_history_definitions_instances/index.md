--- 
title: access_reviews_history_definitions_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_history_definitions_instances
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

Creates, updates, deletes, gets or lists an <code>access_reviews_history_definitions_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_history_definitions_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.access_reviews_history_definitions_instances" /></td></tr>
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
    <td><CopyableCode code="downloadUri" /></td>
    <td><code>string</code></td>
    <td>Uri that can be used to retrieve review history data. This URI will be active for 24 hours after being generated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this instance and associated data expires and the history is deleted. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="fulfilledDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when all of the available data for this instance was collected and is set after this instance's status is set to done. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp reviews ending on or before this date will be included in the fetched history data. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp reviews starting on or after this date will be included in the fetched history data. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="runDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the instance's history data is scheduled to be generated. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue. Once the status has been marked as done, a link can be generated to retrieve the instance's data by calling generateDownloadUri method.</td>
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
    <td><CopyableCode code="downloadUri" /></td>
    <td><code>string</code></td>
    <td>Uri that can be used to retrieve review history data. This URI will be active for 24 hours after being generated. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this instance and associated data expires and the history is deleted. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="fulfilledDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when all of the available data for this instance was collected and is set after this instance's status is set to done. Required. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodEndDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp reviews ending on or before this date will be included in the fetched history data. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewHistoryPeriodStartDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp reviews starting on or after this date will be included in the fetched history data. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="runDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the instance's history data is scheduled to be generated. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue. Once the status has been marked as done, a link can be generated to retrieve the instance's data by calling generateDownloadUri method.</td>
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
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a>, <a href="#parameter-accessReviewHistoryInstance-id"><code>accessReviewHistoryInstance-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that doesn't recur will have exactly one instance.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the instances of an access review history definition created in the last 30 days.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a>, <a href="#parameter-accessReviewHistoryInstance-id"><code>accessReviewHistoryInstance-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a>, <a href="#parameter-accessReviewHistoryInstance-id"><code>accessReviewHistoryInstance-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#generate_download_uri"><CopyableCode code="generate_download_uri" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessReviewHistoryDefinition-id"><code>accessReviewHistoryDefinition-id</code></a>, <a href="#parameter-accessReviewHistoryInstance-id"><code>accessReviewHistoryInstance-id</code></a></td>
    <td></td>
    <td>Generates a URI for an accessReviewHistoryInstance object the status for which is done. Each URI can be used to retrieve the instance's review history data. Each URI is valid for 24 hours and can be retrieved by fetching the downloadUri property from the accessReviewHistoryInstance object.</td>
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
<tr id="parameter-accessReviewHistoryInstance-id">
    <td><CopyableCode code="accessReviewHistoryInstance-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewHistoryInstance</td>
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

If the accessReviewHistoryDefinition is a recurring definition, instances represent each recurrence. A definition that doesn't recur will have exactly one instance.

```sql
SELECT
id,
@odata.type,
downloadUri,
expirationDateTime,
fulfilledDateTime,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
runDateTime,
status
FROM entra_id.identity_governance.access_reviews_history_definitions_instances
WHERE accessReviewHistoryDefinition-id = '{{ accessReviewHistoryDefinition-id }}' -- required
AND accessReviewHistoryInstance-id = '{{ accessReviewHistoryInstance-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve the instances of an access review history definition created in the last 30 days.

```sql
SELECT
id,
@odata.type,
downloadUri,
expirationDateTime,
fulfilledDateTime,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
runDateTime,
status
FROM entra_id.identity_governance.access_reviews_history_definitions_instances
WHERE accessReviewHistoryDefinition-id = '{{ accessReviewHistoryDefinition-id }}' -- required
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
INSERT INTO entra_id.identity_governance.access_reviews_history_definitions_instances (
id,
@odata.type,
downloadUri,
expirationDateTime,
fulfilledDateTime,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
runDateTime,
status,
accessReviewHistoryDefinition-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ downloadUri }}',
'{{ expirationDateTime }}',
'{{ fulfilledDateTime }}',
'{{ reviewHistoryPeriodEndDateTime }}',
'{{ reviewHistoryPeriodStartDateTime }}',
'{{ runDateTime }}',
'{{ status }}',
'{{ accessReviewHistoryDefinition-id }}'
RETURNING
id,
@odata.type,
downloadUri,
expirationDateTime,
fulfilledDateTime,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
runDateTime,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_history_definitions_instances
  props:
    - name: accessReviewHistoryDefinition-id
      value: "{{ accessReviewHistoryDefinition-id }}"
      description: Required parameter for the access_reviews_history_definitions_instances resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: downloadUri
      value: "{{ downloadUri }}"
      description: |
        Uri that can be used to retrieve review history data. This URI will be active for 24 hours after being generated. Required.
    - name: expirationDateTime
      value: "{{ expirationDateTime }}"
      description: |
        Timestamp when this instance and associated data expires and the history is deleted. Required.
    - name: fulfilledDateTime
      value: "{{ fulfilledDateTime }}"
      description: |
        Timestamp when all of the available data for this instance was collected and is set after this instance's status is set to done. Required.
    - name: reviewHistoryPeriodEndDateTime
      value: "{{ reviewHistoryPeriodEndDateTime }}"
      description: |
        Timestamp reviews ending on or before this date will be included in the fetched history data.
    - name: reviewHistoryPeriodStartDateTime
      value: "{{ reviewHistoryPeriodStartDateTime }}"
      description: |
        Timestamp reviews starting on or after this date will be included in the fetched history data.
    - name: runDateTime
      value: "{{ runDateTime }}"
      description: |
        Timestamp when the instance's history data is scheduled to be generated.
    - name: status
      value: "{{ status }}"
      description: |
        Represents the status of the review history data collection. The possible values are: done, inProgress, error, requested, unknownFutureValue. Once the status has been marked as done, a link can be generated to retrieve the instance's data by calling generateDownloadUri method.
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
UPDATE entra_id.identity_governance.access_reviews_history_definitions_instances
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
downloadUri = '{{ downloadUri }}',
expirationDateTime = '{{ expirationDateTime }}',
fulfilledDateTime = '{{ fulfilledDateTime }}',
reviewHistoryPeriodEndDateTime = '{{ reviewHistoryPeriodEndDateTime }}',
reviewHistoryPeriodStartDateTime = '{{ reviewHistoryPeriodStartDateTime }}',
runDateTime = '{{ runDateTime }}',
status = '{{ status }}'
WHERE 
accessReviewHistoryDefinition-id = '{{ accessReviewHistoryDefinition-id }}' --required
AND accessReviewHistoryInstance-id = '{{ accessReviewHistoryInstance-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
downloadUri,
expirationDateTime,
fulfilledDateTime,
reviewHistoryPeriodEndDateTime,
reviewHistoryPeriodStartDateTime,
runDateTime,
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
DELETE FROM entra_id.identity_governance.access_reviews_history_definitions_instances
WHERE accessReviewHistoryDefinition-id = '{{ accessReviewHistoryDefinition-id }}' --required
AND accessReviewHistoryInstance-id = '{{ accessReviewHistoryInstance-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_download_uri"
    values={[
        { label: 'generate_download_uri', value: 'generate_download_uri' }
    ]}
>
<TabItem value="generate_download_uri">

Generates a URI for an accessReviewHistoryInstance object the status for which is done. Each URI can be used to retrieve the instance's review history data. Each URI is valid for 24 hours and can be retrieved by fetching the downloadUri property from the accessReviewHistoryInstance object.

```sql
EXEC entra_id.identity_governance.access_reviews_history_definitions_instances.generate_download_uri 
@accessReviewHistoryDefinition-id='{{ accessReviewHistoryDefinition-id }}' --required, 
@accessReviewHistoryInstance-id='{{ accessReviewHistoryInstance-id }}' --required
;
```
</TabItem>
</Tabs>
