--- 
title: agreement_acceptances
hide_title: false
hide_table_of_contents: false
keywords:
  - agreement_acceptances
  - agreement_acceptances
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

Creates, updates, deletes, gets or lists an <code>agreement_acceptances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="agreement_acceptances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.agreement_acceptances.agreement_acceptances" /></td></tr>
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
    <td><CopyableCode code="agreementFileId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the agreement file accepted by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="agreementId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the device used for accepting the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the device used for accepting the agreement. Supports $filter (eq) and eq for null values.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceOSType" /></td>
    <td><code>string</code></td>
    <td>The operating system used to accept the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceOSVersion" /></td>
    <td><code>string</code></td>
    <td>The operating system version of the device used to accept the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date time of the acceptance. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and eq for null values. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="recordedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the agreement acceptance. The possible values are: accepted, declined. Supports $filter (eq). (accepted, declined, unknownFutureValue) (title: agreementAcceptanceState)</td>
</tr>
<tr>
    <td><CopyableCode code="userDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the user when the acceptance was recorded.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the user when the acceptance was recorded.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the user who accepted the agreement. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>UPN of the user when the acceptance was recorded.</td>
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
    <td><CopyableCode code="agreementFileId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the agreement file accepted by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="agreementId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the device used for accepting the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the device used for accepting the agreement. Supports $filter (eq) and eq for null values.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceOSType" /></td>
    <td><code>string</code></td>
    <td>The operating system used to accept the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceOSVersion" /></td>
    <td><code>string</code></td>
    <td>The operating system version of the device used to accept the agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The expiration date time of the acceptance. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and eq for null values. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="recordedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state of the agreement acceptance. The possible values are: accepted, declined. Supports $filter (eq). (accepted, declined, unknownFutureValue) (title: agreementAcceptanceState)</td>
</tr>
<tr>
    <td><CopyableCode code="userDisplayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the user when the acceptance was recorded.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmail" /></td>
    <td><code>string</code></td>
    <td>Email of the user when the acceptance was recorded.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the user who accepted the agreement. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>UPN of the user when the acceptance was recorded.</td>
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
    <td><a href="#parameter-agreementAcceptance-id"><code>agreementAcceptance-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
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
    <td><a href="#parameter-agreementAcceptance-id"><code>agreementAcceptance-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-agreementAcceptance-id"><code>agreementAcceptance-id</code></a></td>
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
<tr id="parameter-agreementAcceptance-id">
    <td><CopyableCode code="agreementAcceptance-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of agreementAcceptance</td>
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

Retrieved entity

```sql
SELECT
id,
@odata.type,
agreementFileId,
agreementId,
deviceDisplayName,
deviceId,
deviceOSType,
deviceOSVersion,
expirationDateTime,
recordedDateTime,
state,
userDisplayName,
userEmail,
userId,
userPrincipalName
FROM entra_id.agreement_acceptances.agreement_acceptances
WHERE agreementAcceptance-id = '{{ agreementAcceptance-id }}' -- required
AND $select = '{{ $select }}'
;
```
</TabItem>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
@odata.type,
agreementFileId,
agreementId,
deviceDisplayName,
deviceId,
deviceOSType,
deviceOSVersion,
expirationDateTime,
recordedDateTime,
state,
userDisplayName,
userEmail,
userId,
userPrincipalName
FROM entra_id.agreement_acceptances.agreement_acceptances
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
INSERT INTO entra_id.agreement_acceptances.agreement_acceptances (
id,
@odata.type,
agreementFileId,
agreementId,
deviceDisplayName,
deviceId,
deviceOSType,
deviceOSVersion,
expirationDateTime,
recordedDateTime,
state,
userDisplayName,
userEmail,
userId,
userPrincipalName
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ agreementFileId }}',
'{{ agreementId }}',
'{{ deviceDisplayName }}',
'{{ deviceId }}',
'{{ deviceOSType }}',
'{{ deviceOSVersion }}',
'{{ expirationDateTime }}',
'{{ recordedDateTime }}',
'{{ state }}',
'{{ userDisplayName }}',
'{{ userEmail }}',
'{{ userId }}',
'{{ userPrincipalName }}'
RETURNING
id,
@odata.type,
agreementFileId,
agreementId,
deviceDisplayName,
deviceId,
deviceOSType,
deviceOSVersion,
expirationDateTime,
recordedDateTime,
state,
userDisplayName,
userEmail,
userId,
userPrincipalName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: agreement_acceptances
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: agreementFileId
      value: "{{ agreementFileId }}"
      description: |
        The identifier of the agreement file accepted by the user.
    - name: agreementId
      value: "{{ agreementId }}"
      description: |
        The identifier of the agreement.
    - name: deviceDisplayName
      value: "{{ deviceDisplayName }}"
      description: |
        The display name of the device used for accepting the agreement.
    - name: deviceId
      value: "{{ deviceId }}"
      description: |
        The unique identifier of the device used for accepting the agreement. Supports $filter (eq) and eq for null values.
    - name: deviceOSType
      value: "{{ deviceOSType }}"
      description: |
        The operating system used to accept the agreement.
    - name: deviceOSVersion
      value: "{{ deviceOSVersion }}"
      description: |
        The operating system version of the device used to accept the agreement.
    - name: expirationDateTime
      value: "{{ expirationDateTime }}"
      description: |
        The expiration date time of the acceptance. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and eq for null values.
    - name: recordedDateTime
      value: "{{ recordedDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: state
      value: "{{ state }}"
      description: |
        The state of the agreement acceptance. The possible values are: accepted, declined. Supports $filter (eq).
      valid_values: ['accepted', 'declined', 'unknownFutureValue']
    - name: userDisplayName
      value: "{{ userDisplayName }}"
      description: |
        Display name of the user when the acceptance was recorded.
    - name: userEmail
      value: "{{ userEmail }}"
      description: |
        Email of the user when the acceptance was recorded.
    - name: userId
      value: "{{ userId }}"
      description: |
        The identifier of the user who accepted the agreement. Supports $filter (eq).
    - name: userPrincipalName
      value: "{{ userPrincipalName }}"
      description: |
        UPN of the user when the acceptance was recorded.
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
UPDATE entra_id.agreement_acceptances.agreement_acceptances
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
agreementFileId = '{{ agreementFileId }}',
agreementId = '{{ agreementId }}',
deviceDisplayName = '{{ deviceDisplayName }}',
deviceId = '{{ deviceId }}',
deviceOSType = '{{ deviceOSType }}',
deviceOSVersion = '{{ deviceOSVersion }}',
expirationDateTime = '{{ expirationDateTime }}',
recordedDateTime = '{{ recordedDateTime }}',
state = '{{ state }}',
userDisplayName = '{{ userDisplayName }}',
userEmail = '{{ userEmail }}',
userId = '{{ userId }}',
userPrincipalName = '{{ userPrincipalName }}'
WHERE 
agreementAcceptance-id = '{{ agreementAcceptance-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
agreementFileId,
agreementId,
deviceDisplayName,
deviceId,
deviceOSType,
deviceOSVersion,
expirationDateTime,
recordedDateTime,
state,
userDisplayName,
userEmail,
userId,
userPrincipalName;
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
DELETE FROM entra_id.agreement_acceptances.agreement_acceptances
WHERE agreementAcceptance-id = '{{ agreementAcceptance-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
