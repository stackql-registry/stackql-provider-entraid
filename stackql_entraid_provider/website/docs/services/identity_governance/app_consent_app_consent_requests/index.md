--- 
title: app_consent_app_consent_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - app_consent_app_consent_requests
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

Creates, updates, deletes, gets or lists an <code>app_consent_app_consent_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_consent_app_consent_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.app_consent_app_consent_requests" /></td></tr>
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
    <td><CopyableCode code="appDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the application. Required. Supports $filter (eq only) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="pendingScopes" /></td>
    <td><code>array</code></td>
    <td>A list of pending scopes waiting for approval. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userConsentRequests" /></td>
    <td><code>array</code></td>
    <td>A list of pending user consent requests. Supports $filter (eq).</td>
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
    <td><CopyableCode code="appDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the application. Required. Supports $filter (eq only) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="pendingScopes" /></td>
    <td><code>array</code></td>
    <td>A list of pending scopes waiting for approval. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="userConsentRequests" /></td>
    <td><code>array</code></td>
    <td>A list of pending user consent requests. Supports $filter (eq).</td>
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
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of an appConsentRequest object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve appConsentRequest objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a></td>
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

Read the properties and relationships of an appConsentRequest object.

```sql
SELECT
id,
appDisplayName,
appId,
pendingScopes,
userConsentRequests
FROM entra_id.identity_governance.app_consent_app_consent_requests
WHERE app_consent_request_id = '{{ app_consent_request_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve appConsentRequest objects and their properties.

```sql
SELECT
id,
appDisplayName,
appId,
pendingScopes,
userConsentRequests
FROM entra_id.identity_governance.app_consent_app_consent_requests
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
INSERT INTO entra_id.identity_governance.app_consent_app_consent_requests (
id,
appDisplayName,
appId,
pendingScopes,
userConsentRequests
)
SELECT 
'{{ id }}',
'{{ appDisplayName }}',
'{{ appId }}',
'{{ pendingScopes }}',
'{{ userConsentRequests }}'
RETURNING
id,
appDisplayName,
appId,
pendingScopes,
userConsentRequests
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_consent_app_consent_requests
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: appDisplayName
      value: "{{ appDisplayName }}"
      description: |
        The display name of the app for which consent is requested. Required. Supports $filter (eq only) and $orderby.
    - name: appId
      value: "{{ appId }}"
      description: |
        The identifier of the application. Required. Supports $filter (eq only) and $orderby.
    - name: pendingScopes
      description: |
        A list of pending scopes waiting for approval. Required.
      value:
        - displayName: "{{ displayName }}"
    - name: userConsentRequests
      description: |
        A list of pending user consent requests. Supports $filter (eq).
      value:
        - id: "{{ id }}"
          approvalId: "{{ approvalId }}"
          completedDateTime: "{{ completedDateTime }}"
          createdBy: "{{ createdBy }}"
          createdDateTime: "{{ createdDateTime }}"
          customData: "{{ customData }}"
          status: "{{ status }}"
          reason: "{{ reason }}"
          approval: "{{ approval }}"
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
UPDATE entra_id.identity_governance.app_consent_app_consent_requests
SET 
id = '{{ id }}',
appDisplayName = '{{ appDisplayName }}',
appId = '{{ appId }}',
pendingScopes = '{{ pendingScopes }}',
userConsentRequests = '{{ userConsentRequests }}'
WHERE 
app_consent_request_id = '{{ app_consent_request_id }}' --required
RETURNING
id,
appDisplayName,
appId,
pendingScopes,
userConsentRequests;
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
DELETE FROM entra_id.identity_governance.app_consent_app_consent_requests
WHERE app_consent_request_id = '{{ app_consent_request_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
