--- 
title: lifecycle_workflows_deleted_items_workflows_created_by_mailbox_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_deleted_items_workflows_created_by_mailbox_settings
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_deleted_items_workflows_created_by_mailbox_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_deleted_items_workflows_created_by_mailbox_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.lifecycle_workflows_deleted_items_workflows_created_by_mailbox_settings" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
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
    <td><a href="#parameter-workflow-id"><code>workflow-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workflow-id"><code>workflow-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
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
<tr id="parameter-workflow-id">
    <td><CopyableCode code="workflow-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of workflow</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
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
@odata.type,
archiveFolder,
automaticRepliesSetting,
dateFormat,
delegateMeetingMessageDeliveryOptions,
language,
timeFormat,
timeZone,
userPurpose,
workingHours
FROM entraid.identity_governance.lifecycle_workflows_deleted_items_workflows_created_by_mailbox_settings
WHERE workflow-id = '{{ workflow-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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
UPDATE entraid.identity_governance.lifecycle_workflows_deleted_items_workflows_created_by_mailbox_settings
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
@odata.type = '{{ @odata.type }}'
WHERE 
workflow-id = '{{ workflow-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
@odata.type,
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
