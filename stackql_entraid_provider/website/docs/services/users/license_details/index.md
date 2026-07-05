--- 
title: license_details
hide_title: false
hide_table_of_contents: false
keywords:
  - license_details
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

Creates, updates, deletes, gets or lists a <code>license_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="license_details" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.license_details" /></td></tr>
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
    <td><CopyableCode code="servicePlans" /></td>
    <td><code>array</code></td>
    <td>Information about the service plans assigned with the license. Read-only. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related subscribedSku object. Read-only. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="skuPartNumber" /></td>
    <td><code>string</code></td>
    <td>Unique SKU display name. Equal to the skuPartNumber on the related subscribedSku object; for example, AAD_Premium. Read-only.</td>
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
    <td><CopyableCode code="servicePlans" /></td>
    <td><code>array</code></td>
    <td>Information about the service plans assigned with the license. Read-only. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related subscribedSku object. Read-only. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="skuPartNumber" /></td>
    <td><code>string</code></td>
    <td>Unique SKU display name. Equal to the skuPartNumber on the related subscribedSku object; for example, AAD_Premium. Read-only.</td>
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
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-license_details_id"><code>license_details_id</code></a></td>
    <td></td>
    <td>A collection of this user's license details. Read-only.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>A collection of this user's license details. Read-only.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-license_details_id"><code>license_details_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-license_details_id"><code>license_details_id</code></a></td>
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
<tr id="parameter-license_details_id">
    <td><CopyableCode code="license_details_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of licenseDetails</td>
</tr>
<tr id="parameter-user_id">
    <td><CopyableCode code="user_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of user</td>
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

A collection of this user's license details. Read-only.

```sql
SELECT
id,
servicePlans,
skuId,
skuPartNumber
FROM entra_id.users.license_details
WHERE user_id = '{{ user_id }}' -- required
AND license_details_id = '{{ license_details_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

A collection of this user's license details. Read-only.

```sql
SELECT
id,
servicePlans,
skuId,
skuPartNumber
FROM entra_id.users.license_details
WHERE user_id = '{{ user_id }}' -- required
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
INSERT INTO entra_id.users.license_details (
id,
servicePlans,
skuId,
skuPartNumber,
user_id
)
SELECT 
'{{ id }}',
'{{ servicePlans }}',
'{{ skuId }}',
'{{ skuPartNumber }}',
'{{ user_id }}'
RETURNING
id,
servicePlans,
skuId,
skuPartNumber
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: license_details
  props:
    - name: user_id
      value: "{{ user_id }}"
      description: Required parameter for the license_details resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: servicePlans
      description: |
        Information about the service plans assigned with the license. Read-only. Not nullable.
      value:
        - appliesTo: "{{ appliesTo }}"
          provisioningStatus: "{{ provisioningStatus }}"
          servicePlanId: "{{ servicePlanId }}"
          servicePlanName: "{{ servicePlanName }}"
    - name: skuId
      value: "{{ skuId }}"
      description: |
        Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related subscribedSku object. Read-only.
    - name: skuPartNumber
      value: "{{ skuPartNumber }}"
      description: |
        Unique SKU display name. Equal to the skuPartNumber on the related subscribedSku object; for example, AAD_Premium. Read-only.
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
UPDATE entra_id.users.license_details
SET 
id = '{{ id }}',
servicePlans = '{{ servicePlans }}',
skuId = '{{ skuId }}',
skuPartNumber = '{{ skuPartNumber }}'
WHERE 
user_id = '{{ user_id }}' --required
AND license_details_id = '{{ license_details_id }}' --required
RETURNING
id,
servicePlans,
skuId,
skuPartNumber;
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
DELETE FROM entra_id.users.license_details
WHERE user_id = '{{ user_id }}' --required
AND license_details_id = '{{ license_details_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
