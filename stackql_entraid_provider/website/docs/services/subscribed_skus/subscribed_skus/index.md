--- 
title: subscribed_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - subscribed_skus
  - subscribed_skus
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

Creates, updates, deletes, gets or lists a <code>subscribed_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscribed_skus" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.subscribed_skus.subscribed_skus" /></td></tr>
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

Retrieved entity

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
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the account this SKU belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="accountName" /></td>
    <td><code>string</code></td>
    <td>The name of the account this SKU belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="appliesTo" /></td>
    <td><code>string</code></td>
    <td>The target class for this SKU. Only SKUs with target class User are assignable. The possible values are: User, Company.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilityStatus" /></td>
    <td><code>string</code></td>
    <td>Enabled indicates that the prepaidUnits property has at least one unit that is enabled. LockedOut indicates that the customer canceled their subscription. The possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.</td>
</tr>
<tr>
    <td><CopyableCode code="consumedUnits" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of licenses that have been assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="prepaidUnits" /></td>
    <td><code></code></td>
    <td>Information about the number and status of prepaid licenses.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePlans" /></td>
    <td><code>array</code></td>
    <td>Information about the service plans that are available with the SKU. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (GUID) for the service SKU. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="skuPartNumber" /></td>
    <td><code>string</code></td>
    <td>The SKU part number; for example: AAD_PREMIUM or RMSBASIC. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionIds" /></td>
    <td><code>array</code></td>
    <td>A list of all subscription IDs associated with this SKU.</td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="accountId" /></td>
    <td><code>string</code></td>
    <td>The unique ID of the account this SKU belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="accountName" /></td>
    <td><code>string</code></td>
    <td>The name of the account this SKU belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="appliesTo" /></td>
    <td><code>string</code></td>
    <td>The target class for this SKU. Only SKUs with target class User are assignable. The possible values are: User, Company.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilityStatus" /></td>
    <td><code>string</code></td>
    <td>Enabled indicates that the prepaidUnits property has at least one unit that is enabled. LockedOut indicates that the customer canceled their subscription. The possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.</td>
</tr>
<tr>
    <td><CopyableCode code="consumedUnits" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of licenses that have been assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="prepaidUnits" /></td>
    <td><code></code></td>
    <td>Information about the number and status of prepaid licenses.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePlans" /></td>
    <td><code>array</code></td>
    <td>Information about the service plans that are available with the SKU. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string (uuid)</code></td>
    <td>The unique identifier (GUID) for the service SKU. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="skuPartNumber" /></td>
    <td><code>string</code></td>
    <td>The SKU part number; for example: AAD_PREMIUM or RMSBASIC. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionIds" /></td>
    <td><code>array</code></td>
    <td>A list of all subscription IDs associated with this SKU.</td>
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
    <td><a href="#parameter-subscribedSku-id"><code>subscribedSku-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a></td>
    <td>Get a specific commercial subscription that an organization has acquired.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the list of commercial subscriptions that an organization has acquired. For the mapping of license names as displayed on the Microsoft Entra admin center or the Microsoft 365 admin center against their Microsoft Graph skuId and skuPartNumber properties, see Product names and service plan identifiers for licensing.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-subscribedSku-id"><code>subscribedSku-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-subscribedSku-id"><code>subscribedSku-id</code></a></td>
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
<tr id="parameter-subscribedSku-id">
    <td><CopyableCode code="subscribedSku-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of subscribedSku</td>
</tr>
<tr id="parameter-$count">
    <td><CopyableCode code="$count" /></td>
    <td><code>boolean</code></td>
    <td>Include count of items</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter items by property values</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>array</code></td>
    <td>Order items by property values</td>
</tr>
<tr id="parameter-$search">
    <td><CopyableCode code="$search" /></td>
    <td><code>string</code></td>
    <td>Search items by search phrases</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
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

Get a specific commercial subscription that an organization has acquired.

```sql
SELECT
id,
@odata.type,
accountId,
accountName,
appliesTo,
capabilityStatus,
consumedUnits,
prepaidUnits,
servicePlans,
skuId,
skuPartNumber,
subscriptionIds
FROM entra_id.subscribed_skus.subscribed_skus
WHERE subscribedSku-id = '{{ subscribedSku-id }}' -- required
AND $select = '{{ $select }}'
;
```
</TabItem>
<TabItem value="list">

Get the list of commercial subscriptions that an organization has acquired. For the mapping of license names as displayed on the Microsoft Entra admin center or the Microsoft 365 admin center against their Microsoft Graph skuId and skuPartNumber properties, see Product names and service plan identifiers for licensing.

```sql
SELECT
id,
@odata.type,
accountId,
accountName,
appliesTo,
capabilityStatus,
consumedUnits,
prepaidUnits,
servicePlans,
skuId,
skuPartNumber,
subscriptionIds
FROM entra_id.subscribed_skus.subscribed_skus
WHERE $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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
INSERT INTO entra_id.subscribed_skus.subscribed_skus (
id,
@odata.type,
accountId,
accountName,
appliesTo,
capabilityStatus,
consumedUnits,
prepaidUnits,
servicePlans,
skuId,
skuPartNumber,
subscriptionIds
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ accountId }}',
'{{ accountName }}',
'{{ appliesTo }}',
'{{ capabilityStatus }}',
{{ consumedUnits }},
'{{ prepaidUnits }}',
'{{ servicePlans }}',
'{{ skuId }}',
'{{ skuPartNumber }}',
'{{ subscriptionIds }}'
RETURNING
id,
@odata.type,
accountId,
accountName,
appliesTo,
capabilityStatus,
consumedUnits,
prepaidUnits,
servicePlans,
skuId,
skuPartNumber,
subscriptionIds
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: subscribed_skus
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: accountId
      value: "{{ accountId }}"
      description: |
        The unique ID of the account this SKU belongs to.
    - name: accountName
      value: "{{ accountName }}"
      description: |
        The name of the account this SKU belongs to.
    - name: appliesTo
      value: "{{ appliesTo }}"
      description: |
        The target class for this SKU. Only SKUs with target class User are assignable. The possible values are: User, Company.
    - name: capabilityStatus
      value: "{{ capabilityStatus }}"
      description: |
        Enabled indicates that the prepaidUnits property has at least one unit that is enabled. LockedOut indicates that the customer canceled their subscription. The possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.
    - name: consumedUnits
      value: {{ consumedUnits }}
      description: |
        The number of licenses that have been assigned.
    - name: prepaidUnits
      value: "{{ prepaidUnits }}"
      description: |
        Information about the number and status of prepaid licenses.
    - name: servicePlans
      description: |
        Information about the service plans that are available with the SKU. Not nullable.
      value:
        - appliesTo: "{{ appliesTo }}"
          provisioningStatus: "{{ provisioningStatus }}"
          servicePlanId: "{{ servicePlanId }}"
          servicePlanName: "{{ servicePlanName }}"
          @odata.type: "{{ @odata.type }}"
    - name: skuId
      value: "{{ skuId }}"
      description: |
        The unique identifier (GUID) for the service SKU.
    - name: skuPartNumber
      value: "{{ skuPartNumber }}"
      description: |
        The SKU part number; for example: AAD_PREMIUM or RMSBASIC. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.
    - name: subscriptionIds
      value:
        - "{{ subscriptionIds }}"
      description: |
        A list of all subscription IDs associated with this SKU.
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
UPDATE entra_id.subscribed_skus.subscribed_skus
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
accountId = '{{ accountId }}',
accountName = '{{ accountName }}',
appliesTo = '{{ appliesTo }}',
capabilityStatus = '{{ capabilityStatus }}',
consumedUnits = {{ consumedUnits }},
prepaidUnits = '{{ prepaidUnits }}',
servicePlans = '{{ servicePlans }}',
skuId = '{{ skuId }}',
skuPartNumber = '{{ skuPartNumber }}',
subscriptionIds = '{{ subscriptionIds }}'
WHERE 
subscribedSku-id = '{{ subscribedSku-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
accountId,
accountName,
appliesTo,
capabilityStatus,
consumedUnits,
prepaidUnits,
servicePlans,
skuId,
skuPartNumber,
subscriptionIds;
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
DELETE FROM entra_id.subscribed_skus.subscribed_skus
WHERE subscribedSku-id = '{{ subscribedSku-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
