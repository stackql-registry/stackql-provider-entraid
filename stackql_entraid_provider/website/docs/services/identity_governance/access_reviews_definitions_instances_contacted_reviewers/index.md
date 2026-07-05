--- 
title: access_reviews_definitions_instances_contacted_reviewers
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_definitions_instances_contacted_reviewers
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

Creates, updates, deletes, gets or lists an <code>access_reviews_definitions_instances_contacted_reviewers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_definitions_instances_contacted_reviewers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.access_reviews_definitions_instances_contacted_reviewers" /></td></tr>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the reviewer was added for the access review. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of reviewer.</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>User principal name of the reviewer.</td>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date when the reviewer was added for the access review. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of reviewer.</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>User principal name of the reviewer.</td>
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
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_reviewer_id"><code>access_review_reviewer_id</code></a></td>
    <td></td>
    <td>Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a></td>
    <td></td>
    <td>Get the reviewers for an access review instance, irrespective of whether or not they have received a notification. The reviewers are represented by an accessReviewReviewer object. A list of zero or more objects are returned, including all of their nested properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_reviewer_id"><code>access_review_reviewer_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a>, <a href="#parameter-access_review_instance_id"><code>access_review_instance_id</code></a>, <a href="#parameter-access_review_reviewer_id"><code>access_review_reviewer_id</code></a></td>
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
<tr id="parameter-access_review_instance_id">
    <td><CopyableCode code="access_review_instance_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewInstance</td>
</tr>
<tr id="parameter-access_review_reviewer_id">
    <td><CopyableCode code="access_review_reviewer_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewReviewer</td>
</tr>
<tr id="parameter-access_review_schedule_definition_id">
    <td><CopyableCode code="access_review_schedule_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessReviewScheduleDefinition</td>
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

Returns the collection of reviewers who were contacted to complete this review. While the reviewers and fallbackReviewers properties of the accessReviewScheduleDefinition might specify group owners or managers as reviewers, contactedReviewers returns their individual identities. Supports $select. Read-only.

```sql
SELECT
id,
createdDateTime,
displayName,
userPrincipalName
FROM entra_id.identity_governance.access_reviews_definitions_instances_contacted_reviewers
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' -- required
AND access_review_instance_id = '{{ access_review_instance_id }}' -- required
AND access_review_reviewer_id = '{{ access_review_reviewer_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the reviewers for an access review instance, irrespective of whether or not they have received a notification. The reviewers are represented by an accessReviewReviewer object. A list of zero or more objects are returned, including all of their nested properties.

```sql
SELECT
id,
createdDateTime,
displayName,
userPrincipalName
FROM entra_id.identity_governance.access_reviews_definitions_instances_contacted_reviewers
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' -- required
AND access_review_instance_id = '{{ access_review_instance_id }}' -- required
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
INSERT INTO entra_id.identity_governance.access_reviews_definitions_instances_contacted_reviewers (
id,
createdDateTime,
displayName,
userPrincipalName,
access_review_schedule_definition_id,
access_review_instance_id
)
SELECT 
'{{ id }}',
'{{ createdDateTime }}',
'{{ displayName }}',
'{{ userPrincipalName }}',
'{{ access_review_schedule_definition_id }}',
'{{ access_review_instance_id }}'
RETURNING
id,
createdDateTime,
displayName,
userPrincipalName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_definitions_instances_contacted_reviewers
  props:
    - name: access_review_schedule_definition_id
      value: "{{ access_review_schedule_definition_id }}"
      description: Required parameter for the access_reviews_definitions_instances_contacted_reviewers resource.
    - name: access_review_instance_id
      value: "{{ access_review_instance_id }}"
      description: Required parameter for the access_reviews_definitions_instances_contacted_reviewers resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The date when the reviewer was added for the access review.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Name of reviewer.
    - name: userPrincipalName
      value: "{{ userPrincipalName }}"
      description: |
        User principal name of the reviewer.
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
UPDATE entra_id.identity_governance.access_reviews_definitions_instances_contacted_reviewers
SET 
id = '{{ id }}',
createdDateTime = '{{ createdDateTime }}',
displayName = '{{ displayName }}',
userPrincipalName = '{{ userPrincipalName }}'
WHERE 
access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' --required
AND access_review_instance_id = '{{ access_review_instance_id }}' --required
AND access_review_reviewer_id = '{{ access_review_reviewer_id }}' --required
RETURNING
id,
createdDateTime,
displayName,
userPrincipalName;
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
DELETE FROM entra_id.identity_governance.access_reviews_definitions_instances_contacted_reviewers
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' --required
AND access_review_instance_id = '{{ access_review_instance_id }}' --required
AND access_review_reviewer_id = '{{ access_review_reviewer_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
