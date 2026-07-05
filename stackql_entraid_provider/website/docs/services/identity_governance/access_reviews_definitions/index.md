--- 
title: access_reviews_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_reviews_definitions
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

Creates, updates, deletes, gets or lists an <code>access_reviews_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="access_reviews_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.access_reviews_definitions" /></td></tr>
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
    <td><CopyableCode code="additionalNotificationRecipients" /></td>
    <td><code>array</code></td>
    <td>Defines the list of additional users or group members to be notified of the access review progress.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>User who created this review. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the access review series was created. Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionForAdmins" /></td>
    <td><code>string</code></td>
    <td>Description provided by review creators to provide more context of the review to admins. Supports $select.</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionForReviewers" /></td>
    <td><code>string</code></td>
    <td>Description provided  by review creators to provide more context of the review to reviewers. Reviewers see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of the access review series. Supports $select and $orderby. Required on create.</td>
</tr>
<tr>
    <td><CopyableCode code="fallbackReviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceEnumerationScope" /></td>
    <td><code></code></td>
    <td>This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group becomes a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>If the accessReviewScheduleDefinition is a recurring access review, instances represent each recurrence. A review that doesn't recur will have exactly one instance. Instances also represent each unique resource under review in the accessReviewScheduleDefinition. If a review has multiple resources and multiple instances, each resource has a unique instance for each recurrence.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the access review series was last modified. Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code></code></td>
    <td>Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code></code></td>
    <td>The settings for an access review series, see type definition below. Supports $select. Required on create.</td>
</tr>
<tr>
    <td><CopyableCode code="stageSettings" /></td>
    <td><code>array</code></td>
    <td>Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages are created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.</td>
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
    <td><CopyableCode code="additionalNotificationRecipients" /></td>
    <td><code>array</code></td>
    <td>Defines the list of additional users or group members to be notified of the access review progress.</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>User who created this review. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the access review series was created. Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionForAdmins" /></td>
    <td><code>string</code></td>
    <td>Description provided by review creators to provide more context of the review to admins. Supports $select.</td>
</tr>
<tr>
    <td><CopyableCode code="descriptionForReviewers" /></td>
    <td><code>string</code></td>
    <td>Description provided  by review creators to provide more context of the review to reviewers. Reviewers see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Name of the access review series. Supports $select and $orderby. Required on create.</td>
</tr>
<tr>
    <td><CopyableCode code="fallbackReviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceEnumerationScope" /></td>
    <td><code></code></td>
    <td>This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group becomes a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>If the accessReviewScheduleDefinition is a recurring access review, instances represent each recurrence. A review that doesn't recur will have exactly one instance. Instances also represent each unique resource under review in the accessReviewScheduleDefinition. If a review has multiple resources and multiple instances, each resource has a unique instance for each recurrence.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the access review series was last modified. Supports $select. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code></code></td>
    <td>Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code></code></td>
    <td>The settings for an access review series, see type definition below. Supports $select. Required on create.</td>
</tr>
<tr>
    <td><CopyableCode code="stageSettings" /></td>
    <td><code>array</code></td>
    <td>Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages are created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.</td>
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
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of an accessReviewScheduleDefinition object. To retrieve the instances of the access review series, use the list accessReviewInstance API.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the accessReviewScheduleDefinition objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new accessReviewScheduleDefinition object.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a></td>
    <td></td>
    <td>Update an existing accessReviewScheduleDefinition object to change one or more of its properties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes an accessReviewScheduleDefinition object.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-access_review_schedule_definition_id"><code>access_review_schedule_definition_id</code></a></td>
    <td></td>
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

Read the properties and relationships of an accessReviewScheduleDefinition object. To retrieve the instances of the access review series, use the list accessReviewInstance API.

```sql
SELECT
id,
additionalNotificationRecipients,
createdBy,
createdDateTime,
descriptionForAdmins,
descriptionForReviewers,
displayName,
fallbackReviewers,
instanceEnumerationScope,
instances,
lastModifiedDateTime,
reviewers,
scope,
settings,
stageSettings,
status
FROM entra_id.identity_governance.access_reviews_definitions
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the accessReviewScheduleDefinition objects and their properties.

```sql
SELECT
id,
additionalNotificationRecipients,
createdBy,
createdDateTime,
descriptionForAdmins,
descriptionForReviewers,
displayName,
fallbackReviewers,
instanceEnumerationScope,
instances,
lastModifiedDateTime,
reviewers,
scope,
settings,
stageSettings,
status
FROM entra_id.identity_governance.access_reviews_definitions
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

Create a new accessReviewScheduleDefinition object.

```sql
INSERT INTO entra_id.identity_governance.access_reviews_definitions (
id,
additionalNotificationRecipients,
createdBy,
createdDateTime,
descriptionForAdmins,
descriptionForReviewers,
displayName,
fallbackReviewers,
instanceEnumerationScope,
lastModifiedDateTime,
reviewers,
scope,
settings,
stageSettings,
status,
instances
)
SELECT 
'{{ id }}',
'{{ additionalNotificationRecipients }}',
'{{ createdBy }}',
'{{ createdDateTime }}',
'{{ descriptionForAdmins }}',
'{{ descriptionForReviewers }}',
'{{ displayName }}',
'{{ fallbackReviewers }}',
'{{ instanceEnumerationScope }}',
'{{ lastModifiedDateTime }}',
'{{ reviewers }}',
'{{ scope }}',
'{{ settings }}',
'{{ stageSettings }}',
'{{ status }}',
'{{ instances }}'
RETURNING
id,
additionalNotificationRecipients,
createdBy,
createdDateTime,
descriptionForAdmins,
descriptionForReviewers,
displayName,
fallbackReviewers,
instanceEnumerationScope,
instances,
lastModifiedDateTime,
reviewers,
scope,
settings,
stageSettings,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: access_reviews_definitions
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: additionalNotificationRecipients
      description: |
        Defines the list of additional users or group members to be notified of the access review progress.
      value:
        - notificationRecipientScope:
          notificationTemplateType: "{{ notificationTemplateType }}"
    - name: createdBy
      value: "{{ createdBy }}"
      description: |
        User who created this review. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        Timestamp when the access review series was created. Supports $select. Read-only.
    - name: descriptionForAdmins
      value: "{{ descriptionForAdmins }}"
      description: |
        Description provided by review creators to provide more context of the review to admins. Supports $select.
    - name: descriptionForReviewers
      value: "{{ descriptionForReviewers }}"
      description: |
        Description provided  by review creators to provide more context of the review to reviewers. Reviewers see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Name of the access review series. Supports $select and $orderby. Required on create.
    - name: fallbackReviewers
      description: |
        This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.
      value:
        - query: "{{ query }}"
          queryRoot: "{{ queryRoot }}"
          queryType: "{{ queryType }}"
    - name: instanceEnumerationScope
      value: "{{ instanceEnumerationScope }}"
      description: |
        This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group becomes a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        Timestamp when the access review series was last modified. Supports $select. Read-only.
    - name: reviewers
      description: |
        This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.
      value:
        - query: "{{ query }}"
          queryRoot: "{{ queryRoot }}"
          queryType: "{{ queryType }}"
    - name: scope
      value: "{{ scope }}"
      description: |
        Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.
    - name: settings
      value: "{{ settings }}"
      description: |
        The settings for an access review series, see type definition below. Supports $select. Required on create.
    - name: stageSettings
      description: |
        Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages are created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.
      value:
        - decisionsThatWillMoveToNextStage: "{{ decisionsThatWillMoveToNextStage }}"
          dependsOn: "{{ dependsOn }}"
          durationInDays: {{ durationInDays }}
          fallbackReviewers: "{{ fallbackReviewers }}"
          recommendationInsightSettings: "{{ recommendationInsightSettings }}"
          recommendationsEnabled: {{ recommendationsEnabled }}
          reviewers: "{{ reviewers }}"
          stageId: "{{ stageId }}"
    - name: status
      value: "{{ status }}"
      description: |
        This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.
    - name: instances
      description: |
        If the accessReviewScheduleDefinition is a recurring access review, instances represent each recurrence. A review that doesn't recur will have exactly one instance. Instances also represent each unique resource under review in the accessReviewScheduleDefinition. If a review has multiple resources and multiple instances, each resource has a unique instance for each recurrence.
      value:
        - id: "{{ id }}"
          endDateTime: "{{ endDateTime }}"
          fallbackReviewers: "{{ fallbackReviewers }}"
          reviewers: "{{ reviewers }}"
          scope: "{{ scope }}"
          startDateTime: "{{ startDateTime }}"
          status: "{{ status }}"
          contactedReviewers: "{{ contactedReviewers }}"
          decisions: "{{ decisions }}"
          stages: "{{ stages }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

Update an existing accessReviewScheduleDefinition object to change one or more of its properties.

```sql
REPLACE entra_id.identity_governance.access_reviews_definitions
SET 
id = '{{ id }}',
additionalNotificationRecipients = '{{ additionalNotificationRecipients }}',
createdBy = '{{ createdBy }}',
createdDateTime = '{{ createdDateTime }}',
descriptionForAdmins = '{{ descriptionForAdmins }}',
descriptionForReviewers = '{{ descriptionForReviewers }}',
displayName = '{{ displayName }}',
fallbackReviewers = '{{ fallbackReviewers }}',
instanceEnumerationScope = '{{ instanceEnumerationScope }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
reviewers = '{{ reviewers }}',
scope = '{{ scope }}',
settings = '{{ settings }}',
stageSettings = '{{ stageSettings }}',
status = '{{ status }}',
instances = '{{ instances }}'
WHERE 
access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' --required
RETURNING
id,
additionalNotificationRecipients,
createdBy,
createdDateTime,
descriptionForAdmins,
descriptionForReviewers,
displayName,
fallbackReviewers,
instanceEnumerationScope,
instances,
lastModifiedDateTime,
reviewers,
scope,
settings,
stageSettings,
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

Deletes an accessReviewScheduleDefinition object.

```sql
DELETE FROM entra_id.identity_governance.access_reviews_definitions
WHERE access_review_schedule_definition_id = '{{ access_review_schedule_definition_id }}' --required
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

Success

```sql
EXEC entra_id.identity_governance.access_reviews_definitions.stop 
@access_review_schedule_definition_id='{{ access_review_schedule_definition_id }}' --required
;
```
</TabItem>
</Tabs>
