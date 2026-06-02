--- 
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - directory
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.directory.subscriptions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_2', value: 'get_2' },
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="commerceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of this subscription in the commerce system. Alternate key.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when this subscription was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isTrial" /></td>
    <td><code>boolean</code></td>
    <td>Whether the subscription is a free trial or purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLifecycleDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the subscription will move to the next state (as defined by the status property) if not renewed by the tenant. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="ownerId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the account admin.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerTenantId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the Microsoft partner tenant that created the subscription on a customer tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerType" /></td>
    <td><code>string</code></td>
    <td>Indicates the entity that ownerId belongs to, for example, 'User'.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceStatus" /></td>
    <td><code>array</code></td>
    <td>The provisioning status of each service included in this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the SKU associated with this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="skuPartNumber" /></td>
    <td><code>string</code></td>
    <td>The SKU associated with this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of this subscription. The possible values are: Enabled, Deleted, Suspended, Warning, LockedOut.</td>
</tr>
<tr>
    <td><CopyableCode code="totalLicenses" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of licenses included in this subscription.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_2">

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
    <td><CopyableCode code="commerceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of this subscription in the commerce system. Alternate key.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when this subscription was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isTrial" /></td>
    <td><code>boolean</code></td>
    <td>Whether the subscription is a free trial or purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLifecycleDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the subscription will move to the next state (as defined by the status property) if not renewed by the tenant. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="ownerId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the account admin.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerTenantId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the Microsoft partner tenant that created the subscription on a customer tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerType" /></td>
    <td><code>string</code></td>
    <td>Indicates the entity that ownerId belongs to, for example, 'User'.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceStatus" /></td>
    <td><code>array</code></td>
    <td>The provisioning status of each service included in this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the SKU associated with this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="skuPartNumber" /></td>
    <td><code>string</code></td>
    <td>The SKU associated with this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of this subscription. The possible values are: Enabled, Deleted, Suspended, Warning, LockedOut.</td>
</tr>
<tr>
    <td><CopyableCode code="totalLicenses" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of licenses included in this subscription.</td>
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
    <td><CopyableCode code="commerceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of this subscription in the commerce system. Alternate key.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when this subscription was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isTrial" /></td>
    <td><code>boolean</code></td>
    <td>Whether the subscription is a free trial or purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLifecycleDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the subscription will move to the next state (as defined by the status property) if not renewed by the tenant. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="ownerId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the account admin.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerTenantId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the Microsoft partner tenant that created the subscription on a customer tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerType" /></td>
    <td><code>string</code></td>
    <td>Indicates the entity that ownerId belongs to, for example, 'User'.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceStatus" /></td>
    <td><code>array</code></td>
    <td>The provisioning status of each service included in this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="skuId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the SKU associated with this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="skuPartNumber" /></td>
    <td><code>string</code></td>
    <td>The SKU associated with this subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of this subscription. The possible values are: Enabled, Deleted, Suspended, Warning, LockedOut.</td>
</tr>
<tr>
    <td><CopyableCode code="totalLicenses" /></td>
    <td><code>number (int32)</code></td>
    <td>The number of licenses included in this subscription.</td>
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
    <td><a href="#parameter-commerceSubscriptionId"><code>commerceSubscriptionId</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a specific commercial subscription that an organization acquired.</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-companySubscription-id"><code>companySubscription-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a specific commercial subscription that an organization acquired.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the list of commercial subscriptions that an organization acquired.</td>
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
    <td><a href="#parameter-commerceSubscriptionId"><code>commerceSubscriptionId</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-companySubscription-id"><code>companySubscription-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-commerceSubscriptionId"><code>commerceSubscriptionId</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-companySubscription-id"><code>companySubscription-id</code></a></td>
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
<tr id="parameter-commerceSubscriptionId">
    <td><CopyableCode code="commerceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>Alternate key of companySubscription</td>
</tr>
<tr id="parameter-companySubscription-id">
    <td><CopyableCode code="companySubscription-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of companySubscription</td>
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
        { label: 'get_2', value: 'get_2' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a specific commercial subscription that an organization acquired.

```sql
SELECT
id,
@odata.type,
commerceSubscriptionId,
createdDateTime,
isTrial,
nextLifecycleDateTime,
ownerId,
ownerTenantId,
ownerType,
serviceStatus,
skuId,
skuPartNumber,
status,
totalLicenses
FROM entraid.directory.subscriptions
WHERE commerceSubscriptionId = '{{ commerceSubscriptionId }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_2">

Get a specific commercial subscription that an organization acquired.

```sql
SELECT
id,
@odata.type,
commerceSubscriptionId,
createdDateTime,
isTrial,
nextLifecycleDateTime,
ownerId,
ownerTenantId,
ownerType,
serviceStatus,
skuId,
skuPartNumber,
status,
totalLicenses
FROM entraid.directory.subscriptions
WHERE companySubscription-id = '{{ companySubscription-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get the list of commercial subscriptions that an organization acquired.

```sql
SELECT
id,
@odata.type,
commerceSubscriptionId,
createdDateTime,
isTrial,
nextLifecycleDateTime,
ownerId,
ownerTenantId,
ownerType,
serviceStatus,
skuId,
skuPartNumber,
status,
totalLicenses
FROM entraid.directory.subscriptions
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
INSERT INTO entraid.directory.subscriptions (
id,
@odata.type,
commerceSubscriptionId,
createdDateTime,
isTrial,
nextLifecycleDateTime,
ownerId,
ownerTenantId,
ownerType,
serviceStatus,
skuId,
skuPartNumber,
status,
totalLicenses
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ commerceSubscriptionId }}',
'{{ createdDateTime }}',
{{ isTrial }},
'{{ nextLifecycleDateTime }}',
'{{ ownerId }}',
'{{ ownerTenantId }}',
'{{ ownerType }}',
'{{ serviceStatus }}',
'{{ skuId }}',
'{{ skuPartNumber }}',
'{{ status }}',
{{ totalLicenses }}
RETURNING
id,
@odata.type,
commerceSubscriptionId,
createdDateTime,
isTrial,
nextLifecycleDateTime,
ownerId,
ownerTenantId,
ownerType,
serviceStatus,
skuId,
skuPartNumber,
status,
totalLicenses
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: subscriptions
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: commerceSubscriptionId
      value: "{{ commerceSubscriptionId }}"
      description: |
        The ID of this subscription in the commerce system. Alternate key.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The date and time when this subscription was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: isTrial
      value: {{ isTrial }}
      description: |
        Whether the subscription is a free trial or purchased.
    - name: nextLifecycleDateTime
      value: "{{ nextLifecycleDateTime }}"
      description: |
        The date and time when the subscription will move to the next state (as defined by the status property) if not renewed by the tenant. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: ownerId
      value: "{{ ownerId }}"
      description: |
        The object ID of the account admin.
    - name: ownerTenantId
      value: "{{ ownerTenantId }}"
      description: |
        The unique identifier for the Microsoft partner tenant that created the subscription on a customer tenant.
    - name: ownerType
      value: "{{ ownerType }}"
      description: |
        Indicates the entity that ownerId belongs to, for example, 'User'.
    - name: serviceStatus
      description: |
        The provisioning status of each service included in this subscription.
      value:
        - appliesTo: "{{ appliesTo }}"
          provisioningStatus: "{{ provisioningStatus }}"
          servicePlanId: "{{ servicePlanId }}"
          servicePlanName: "{{ servicePlanName }}"
          @odata.type: "{{ @odata.type }}"
    - name: skuId
      value: "{{ skuId }}"
      description: |
        The object ID of the SKU associated with this subscription.
    - name: skuPartNumber
      value: "{{ skuPartNumber }}"
      description: |
        The SKU associated with this subscription.
    - name: status
      value: "{{ status }}"
      description: |
        The status of this subscription. The possible values are: Enabled, Deleted, Suspended, Warning, LockedOut.
    - name: totalLicenses
      value: {{ totalLicenses }}
      description: |
        The number of licenses included in this subscription.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'update_2', value: 'update_2' }
    ]}
>
<TabItem value="update">

No description available.

```sql
UPDATE entraid.directory.subscriptions
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
commerceSubscriptionId = '{{ commerceSubscriptionId }}',
createdDateTime = '{{ createdDateTime }}',
isTrial = {{ isTrial }},
nextLifecycleDateTime = '{{ nextLifecycleDateTime }}',
ownerId = '{{ ownerId }}',
ownerTenantId = '{{ ownerTenantId }}',
ownerType = '{{ ownerType }}',
serviceStatus = '{{ serviceStatus }}',
skuId = '{{ skuId }}',
skuPartNumber = '{{ skuPartNumber }}',
status = '{{ status }}',
totalLicenses = {{ totalLicenses }}
WHERE 
commerceSubscriptionId = '{{ commerceSubscriptionId }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
commerceSubscriptionId,
createdDateTime,
isTrial,
nextLifecycleDateTime,
ownerId,
ownerTenantId,
ownerType,
serviceStatus,
skuId,
skuPartNumber,
status,
totalLicenses;
```
</TabItem>
<TabItem value="update_2">

No description available.

```sql
UPDATE entraid.directory.subscriptions
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
commerceSubscriptionId = '{{ commerceSubscriptionId }}',
createdDateTime = '{{ createdDateTime }}',
isTrial = {{ isTrial }},
nextLifecycleDateTime = '{{ nextLifecycleDateTime }}',
ownerId = '{{ ownerId }}',
ownerTenantId = '{{ ownerTenantId }}',
ownerType = '{{ ownerType }}',
serviceStatus = '{{ serviceStatus }}',
skuId = '{{ skuId }}',
skuPartNumber = '{{ skuPartNumber }}',
status = '{{ status }}',
totalLicenses = {{ totalLicenses }}
WHERE 
companySubscription-id = '{{ companySubscription-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
commerceSubscriptionId,
createdDateTime,
isTrial,
nextLifecycleDateTime,
ownerId,
ownerTenantId,
ownerType,
serviceStatus,
skuId,
skuPartNumber,
status,
totalLicenses;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_2', value: 'delete_2' }
    ]}
>
<TabItem value="delete">

No description available.

```sql
DELETE FROM entraid.directory.subscriptions
WHERE commerceSubscriptionId = '{{ commerceSubscriptionId }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

No description available.

```sql
DELETE FROM entraid.directory.subscriptions
WHERE companySubscription-id = '{{ companySubscription-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
