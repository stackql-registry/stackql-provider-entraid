--- 
title: ownerless_group_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - ownerless_group_policy
  - policies
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

Creates, updates, deletes, gets or lists an <code>ownerless_group_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ownerless_group_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.ownerless_group_policy" /></td></tr>
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
    <td><CopyableCode code="emailInfo" /></td>
    <td><code>object</code></td>
    <td> (title: emailDetails)</td>
</tr>
<tr>
    <td><CopyableCode code="enabledGroupIds" /></td>
    <td><code>array</code></td>
    <td>The collection of IDs for groups to which the policy is enabled. If empty, the policy is enabled for all groups in the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the ownerless group policy is enabled in the tenant. Setting this property to false clears the values of all other policy parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="maxMembersToNotify" /></td>
    <td><code>number (int64)</code></td>
    <td>The maximum number of members to notify. Value range is 0-90. Members are prioritized by recent group activity (most active first). If there aren't enough active members to fill the limit, remaining slots are filled with other eligible group members from the directory.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationDurationInWeeks" /></td>
    <td><code>number (int64)</code></td>
    <td>The number of weeks for the notification duration. Value range is 1-7.</td>
</tr>
<tr>
    <td><CopyableCode code="policyWebUrl" /></td>
    <td><code>string</code></td>
    <td>The URL to the policy documentation.</td>
</tr>
<tr>
    <td><CopyableCode code="targetOwners" /></td>
    <td><code>object</code></td>
    <td> (title: targetOwners)</td>
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
    <td></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties of an ownerlessGroupPolicy object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create or update the ownerlessGroupPolicy for the tenant. If the policy doesn't exist, it creates a new one; if the policy exists, it updates the existing policy. To disable the policy, set isEnabled to false. Setting isEnabled to false clears the values of all other policy parameters.</td>
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

Read the properties of an ownerlessGroupPolicy object.

```sql
SELECT
id,
@odata.type,
emailInfo,
enabledGroupIds,
isEnabled,
maxMembersToNotify,
notificationDurationInWeeks,
policyWebUrl,
targetOwners
FROM entra_id.policies.ownerless_group_policy
WHERE $select = '{{ $select }}'
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

Create or update the ownerlessGroupPolicy for the tenant. If the policy doesn't exist, it creates a new one; if the policy exists, it updates the existing policy. To disable the policy, set isEnabled to false. Setting isEnabled to false clears the values of all other policy parameters.

```sql
UPDATE entra_id.policies.ownerless_group_policy
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
emailInfo = '{{ emailInfo }}',
enabledGroupIds = '{{ enabledGroupIds }}',
isEnabled = {{ isEnabled }},
maxMembersToNotify = {{ maxMembersToNotify }},
notificationDurationInWeeks = {{ notificationDurationInWeeks }},
policyWebUrl = '{{ policyWebUrl }}',
targetOwners = '{{ targetOwners }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
emailInfo,
enabledGroupIds,
isEnabled,
maxMembersToNotify,
notificationDurationInWeeks,
policyWebUrl,
targetOwners;
```
</TabItem>
</Tabs>
