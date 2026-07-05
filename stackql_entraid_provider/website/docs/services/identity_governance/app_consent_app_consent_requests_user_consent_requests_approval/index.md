--- 
title: app_consent_app_consent_requests_user_consent_requests_approval
hide_title: false
hide_table_of_contents: false
keywords:
  - app_consent_app_consent_requests_user_consent_requests_approval
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

Creates, updates, deletes, gets or lists an <code>app_consent_app_consent_requests_user_consent_requests_approval</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_consent_app_consent_requests_user_consent_requests_approval" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests_approval" /></td></tr>
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
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>A collection of stages in the approval decision.</td>
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
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a>, <a href="#parameter-user_consent_request_id"><code>user_consent_request_id</code></a></td>
    <td></td>
    <td>Approval decisions associated with a request.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a>, <a href="#parameter-user_consent_request_id"><code>user_consent_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a>, <a href="#parameter-user_consent_request_id"><code>user_consent_request_id</code></a></td>
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
<tr id="parameter-app_consent_request_id">
    <td><CopyableCode code="app_consent_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of appConsentRequest</td>
</tr>
<tr id="parameter-user_consent_request_id">
    <td><CopyableCode code="user_consent_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of userConsentRequest</td>
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

Approval decisions associated with a request.

```sql
SELECT
id,
stages
FROM entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests_approval
WHERE app_consent_request_id = '{{ app_consent_request_id }}' -- required
AND user_consent_request_id = '{{ user_consent_request_id }}' -- required
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
UPDATE entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests_approval
SET 
id = '{{ id }}',
stages = '{{ stages }}'
WHERE 
app_consent_request_id = '{{ app_consent_request_id }}' --required
AND user_consent_request_id = '{{ user_consent_request_id }}' --required
RETURNING
id,
stages;
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
DELETE FROM entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests_approval
WHERE app_consent_request_id = '{{ app_consent_request_id }}' --required
AND user_consent_request_id = '{{ user_consent_request_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
