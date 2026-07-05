--- 
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - directory
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscriptions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.subscriptions" /></td></tr>
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
    <td><CopyableCode code="commerceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of this subscription in the commerce system. Alternate key.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when this subscription was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isTrial" /></td>
    <td><code>boolean</code></td>
    <td>Whether the subscription is a free trial or purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLifecycleDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the subscription will move to the next state (as defined by the status property) if not renewed by the tenant. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><CopyableCode code="commerceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of this subscription in the commerce system. Alternate key.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when this subscription was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isTrial" /></td>
    <td><code>boolean</code></td>
    <td>Whether the subscription is a free trial or purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLifecycleDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the subscription will move to the next state (as defined by the status property) if not renewed by the tenant. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><CopyableCode code="commerceSubscriptionId" /></td>
    <td><code>string</code></td>
    <td>The ID of this subscription in the commerce system. Alternate key.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when this subscription was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isTrial" /></td>
    <td><code>boolean</code></td>
    <td>Whether the subscription is a free trial or purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="nextLifecycleDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the subscription will move to the next state (as defined by the status property) if not renewed by the tenant. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-commerce_subscription_id"><code>commerce_subscription_id</code></a></td>
    <td></td>
    <td>Get a specific commercial subscription that an organization acquired.</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-company_subscription_id"><code>company_subscription_id</code></a></td>
    <td></td>
    <td>Get a specific commercial subscription that an organization acquired.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get the list of commercial subscriptions that an organization acquired.</td>
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
    <td><a href="#parameter-commerce_subscription_id"><code>commerce_subscription_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-company_subscription_id"><code>company_subscription_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-commerce_subscription_id"><code>commerce_subscription_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-company_subscription_id"><code>company_subscription_id</code></a></td>
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
<tr id="parameter-commerce_subscription_id">
    <td><CopyableCode code="commerce_subscription_id" /></td>
    <td><code>string</code></td>
    <td>Alternate key of companySubscription</td>
</tr>
<tr id="parameter-company_subscription_id">
    <td><CopyableCode code="company_subscription_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of companySubscription</td>
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
FROM entra_id.directory.subscriptions
WHERE commerce_subscription_id = '{{ commerce_subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_2">

Get a specific commercial subscription that an organization acquired.

```sql
SELECT
id,
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
FROM entra_id.directory.subscriptions
WHERE company_subscription_id = '{{ company_subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the list of commercial subscriptions that an organization acquired.

```sql
SELECT
id,
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
FROM entra_id.directory.subscriptions
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
INSERT INTO entra_id.directory.subscriptions (
id,
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
UPDATE entra_id.directory.subscriptions
SET 
id = '{{ id }}',
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
commerce_subscription_id = '{{ commerce_subscription_id }}' --required
RETURNING
id,
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
UPDATE entra_id.directory.subscriptions
SET 
id = '{{ id }}',
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
company_subscription_id = '{{ company_subscription_id }}' --required
RETURNING
id,
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
DELETE FROM entra_id.directory.subscriptions
WHERE commerce_subscription_id = '{{ commerce_subscription_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

No description available.

```sql
DELETE FROM entra_id.directory.subscriptions
WHERE company_subscription_id = '{{ company_subscription_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
