--- 
title: reminder_view
hide_title: false
hide_table_of_contents: false
keywords:
  - reminder_view
  - users
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

Creates, updates, deletes, gets or lists a <code>reminder_view</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reminder_view" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.reminder_view" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="changeKey" /></td>
    <td><code>string</code></td>
    <td>Identifies the version of the reminder. Every time the reminder is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object.</td>
</tr>
<tr>
    <td><CopyableCode code="eventEndTime" /></td>
    <td><code>object</code></td>
    <td>The date, time and time zone that the event ends. (title: dateTimeTimeZone)</td>
</tr>
<tr>
    <td><CopyableCode code="eventId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the event. Read only.</td>
</tr>
<tr>
    <td><CopyableCode code="eventLocation" /></td>
    <td><code>object</code></td>
    <td>The location of the event. (title: location)</td>
</tr>
<tr>
    <td><CopyableCode code="eventStartTime" /></td>
    <td><code>object</code></td>
    <td>The date, time, and time zone that the event starts. (title: dateTimeTimeZone)</td>
</tr>
<tr>
    <td><CopyableCode code="eventSubject" /></td>
    <td><code>string</code></td>
    <td>The text of the event's subject line.</td>
</tr>
<tr>
    <td><CopyableCode code="eventWebLink" /></td>
    <td><code>string</code></td>
    <td>The URL to open the event in Outlook on the web.The event opens in the browser if you're logged in to your mailbox via Outlook on the web. You're prompted to log in if you aren't already logged in with the browser.This URL can't be accessed from within an iFrame.</td>
</tr>
<tr>
    <td><CopyableCode code="reminderFireTime" /></td>
    <td><code>object</code></td>
    <td>The date, time, and time zone that the reminder is set to occur. (title: dateTimeTimeZone)</td>
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
    <td><a href="#parameter-user-id"><code>user-id</code></a>, <a href="#parameter-StartDateTime"><code>StartDateTime</code></a>, <a href="#parameter-EndDateTime"><code>EndDateTime</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a></td>
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
<tr id="parameter-EndDateTime">
    <td><CopyableCode code="EndDateTime" /></td>
    <td><code>string</code></td>
    <td>Usage: EndDateTime='&#123;EndDateTime&#125;'</td>
</tr>
<tr id="parameter-StartDateTime">
    <td><CopyableCode code="StartDateTime" /></td>
    <td><code>string</code></td>
    <td>Usage: StartDateTime='&#123;StartDateTime&#125;'</td>
</tr>
<tr id="parameter-user-id">
    <td><CopyableCode code="user-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of user</td>
</tr>
<tr id="parameter-$count">
    <td><CopyableCode code="$count" /></td>
    <td><code>boolean</code></td>
    <td>Include count of items</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter items by property values</td>
</tr>
<tr id="parameter-$search">
    <td><CopyableCode code="$search" /></td>
    <td><code>string</code></td>
    <td>Search items by search phrases</td>
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

Success

```sql
SELECT
@odata.type,
changeKey,
eventEndTime,
eventId,
eventLocation,
eventStartTime,
eventSubject,
eventWebLink,
reminderFireTime
FROM entra_id.users.reminder_view
WHERE user-id = '{{ user-id }}' -- required
AND StartDateTime = '{{ StartDateTime }}' -- required
AND EndDateTime = '{{ EndDateTime }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
;
```
</TabItem>
</Tabs>
