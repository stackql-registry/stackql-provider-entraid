--- 
title: lifecycle_workflows_deleted_items_workflows_versions_created_by_mailbox_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_deleted_items_workflows_versions_created_by_mailbox_settings
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_deleted_items_workflows_versions_created_by_mailbox_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_deleted_items_workflows_versions_created_by_mailbox_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_versions_created_by_mailbox_settings" /></td></tr>
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

Entity result.

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
    <td><CopyableCode code="archiveFolder" /></td>
    <td><code>string</code></td>
    <td>Folder ID of an archive folder for the user.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticRepliesSetting" /></td>
    <td><code>object</code></td>
    <td>Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user. (title: automaticRepliesSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="dateFormat" /></td>
    <td><code>string</code></td>
    <td>The date format for the user's mailbox.</td>
</tr>
<tr>
    <td><CopyableCode code="delegateMeetingMessageDeliveryOptions" /></td>
    <td><code>string</code></td>
    <td>If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. The possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly. (sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly) (title: delegateMeetingMessageDeliveryOptions)</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>object</code></td>
    <td>The locale information for the user, including the preferred language and country/region. (title: localeInfo)</td>
</tr>
<tr>
    <td><CopyableCode code="timeFormat" /></td>
    <td><code>string</code></td>
    <td>The time format for the user's mailbox.</td>
</tr>
<tr>
    <td><CopyableCode code="timeZone" /></td>
    <td><code>string</code></td>
    <td>The default time zone for the user's mailbox.</td>
</tr>
<tr>
    <td><CopyableCode code="userPurpose" /></td>
    <td><code>string</code></td>
    <td>The purpose of the mailbox. Differentiates a mailbox for a single user from a shared mailbox and equipment mailbox in Exchange Online. The possible values are: user, linked, shared, room, equipment, others, unknownFutureValue. Read-only. (user, linked, shared, room, equipment, others, unknownFutureValue) (title: userPurpose)</td>
</tr>
<tr>
    <td><CopyableCode code="workingHours" /></td>
    <td><code>object</code></td>
    <td>The days of the week and hours in a specific time zone that the user works. (title: workingHours)</td>
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
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-workflow_version_version_number"><code>workflow_version_version_number</code></a></td>
    <td></td>
    <td>Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-workflow_version_version_number"><code>workflow_version_version_number</code></a></td>
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
<tr id="parameter-workflow_id">
    <td><CopyableCode code="workflow_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of workflow</td>
</tr>
<tr id="parameter-workflow_version_version_number">
    <td><CopyableCode code="workflow_version_version_number" /></td>
    <td><code>number (int32)</code></td>
    <td>The unique identifier of workflowVersion</td>
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

Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Requires $select to retrieve.

```sql
SELECT
archiveFolder,
automaticRepliesSetting,
dateFormat,
delegateMeetingMessageDeliveryOptions,
language,
timeFormat,
timeZone,
userPurpose,
workingHours
FROM entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_versions_created_by_mailbox_settings
WHERE workflow_id = '{{ workflow_id }}' -- required
AND workflow_version_version_number = '{{ workflow_version_version_number }}' -- required
;
```
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
UPDATE entra_id.identity_governance.lifecycle_workflows_deleted_items_workflows_versions_created_by_mailbox_settings
SET 
archiveFolder = '{{ archiveFolder }}',
automaticRepliesSetting = '{{ automaticRepliesSetting }}',
dateFormat = '{{ dateFormat }}',
delegateMeetingMessageDeliveryOptions = '{{ delegateMeetingMessageDeliveryOptions }}',
language = '{{ language }}',
timeFormat = '{{ timeFormat }}',
timeZone = '{{ timeZone }}',
userPurpose = '{{ userPurpose }}',
workingHours = '{{ workingHours }}',
WHERE 
workflow_id = '{{ workflow_id }}' --required
AND workflow_version_version_number = '{{ workflow_version_version_number }}' --required
RETURNING
archiveFolder,
automaticRepliesSetting,
dateFormat,
delegateMeetingMessageDeliveryOptions,
language,
timeFormat,
timeZone,
userPurpose,
workingHours;
```
</TabItem>
</Tabs>
