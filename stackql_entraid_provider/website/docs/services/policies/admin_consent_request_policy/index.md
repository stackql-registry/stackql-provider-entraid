--- 
title: admin_consent_request_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - admin_consent_request_policy
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

Creates, updates, deletes, gets or lists an <code>admin_consent_request_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="admin_consent_request_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.admin_consent_request_policy" /></td></tr>
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
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the admin consent request feature is enabled or disabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifyReviewers" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether reviewers will receive notifications. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remindersEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether reviewers will receive reminder emails. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="requestDurationInDays" /></td>
    <td><code>number (int32)</code></td>
    <td>Specifies the duration the request is active before it automatically expires if no decision is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewers" /></td>
    <td><code>array</code></td>
    <td>The list of reviewers for the admin consent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>number (int32)</code></td>
    <td>Specifies the version of this policy. When the policy is updated, this version is updated. Read-only.</td>
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
    <td>Read the properties and relationships of an adminConsentRequestPolicy object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of an adminConsentRequestPolicy object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Read the properties and relationships of an adminConsentRequestPolicy object.

```sql
SELECT
id,
@odata.type,
isEnabled,
notifyReviewers,
remindersEnabled,
requestDurationInDays,
reviewers,
version
FROM entra_id.policies.admin_consent_request_policy
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

Update the properties of an adminConsentRequestPolicy object.

```sql
UPDATE entra_id.policies.admin_consent_request_policy
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
isEnabled = {{ isEnabled }},
notifyReviewers = {{ notifyReviewers }},
remindersEnabled = {{ remindersEnabled }},
requestDurationInDays = {{ requestDurationInDays }},
reviewers = '{{ reviewers }}',
version = {{ version }}
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
isEnabled,
notifyReviewers,
remindersEnabled,
requestDurationInDays,
reviewers,
version;
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
DELETE FROM entra_id.policies.admin_consent_request_policy
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
