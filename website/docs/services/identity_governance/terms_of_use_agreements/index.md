--- 
title: terms_of_use_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - terms_of_use_agreements
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

Creates, updates, deletes, gets or lists a <code>terms_of_use_agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="terms_of_use_agreements" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.terms_of_use_agreements" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="acceptances" /></td>
    <td><code>array</code></td>
    <td>Read-only. Information about acceptances of this agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the agreement. The display name is used for internal tracking of the agreement but isn't shown to end users who view the agreement. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="file" /></td>
    <td><code></code></td>
    <td>Default PDF linked to this agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="files" /></td>
    <td><code>array</code></td>
    <td>PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isPerDeviceAcceptanceRequired" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether end users are required to accept this agreement on every device that they access it from. The end user is required to register their device in Microsoft Entra ID, if they haven't already done so. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="isViewingBeforeAcceptanceRequired" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the user has to expand the agreement before accepting. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="termsExpiration" /></td>
    <td><code></code></td>
    <td>Expiration schedule and frequency of agreement for all users. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="userReacceptRequiredFrequency" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration after which the user must reaccept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq). (pattern: <code>^-?P([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+([.][0-9]+)?S)?)?$</code>)</td>
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
    <td><CopyableCode code="acceptances" /></td>
    <td><code>array</code></td>
    <td>Read-only. Information about acceptances of this agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the agreement. The display name is used for internal tracking of the agreement but isn't shown to end users who view the agreement. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="file" /></td>
    <td><code></code></td>
    <td>Default PDF linked to this agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="files" /></td>
    <td><code>array</code></td>
    <td>PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isPerDeviceAcceptanceRequired" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether end users are required to accept this agreement on every device that they access it from. The end user is required to register their device in Microsoft Entra ID, if they haven't already done so. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="isViewingBeforeAcceptanceRequired" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the user has to expand the agreement before accepting. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="termsExpiration" /></td>
    <td><code></code></td>
    <td>Expiration schedule and frequency of agreement for all users. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="userReacceptRequiredFrequency" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration after which the user must reaccept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq). (pattern: <code>^-?P([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+([.][0-9]+)?S)?)?$</code>)</td>
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
    <td><a href="#parameter-agreement-id"><code>agreement-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of an agreement object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of agreement objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new agreement object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-agreement-id"><code>agreement-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of an agreement object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-agreement-id"><code>agreement-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an agreement object.</td>
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
<tr id="parameter-agreement-id">
    <td><CopyableCode code="agreement-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of agreement</td>
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

Retrieve the properties and relationships of an agreement object.

```sql
SELECT
id,
@odata.type,
acceptances,
displayName,
file,
files,
isPerDeviceAcceptanceRequired,
isViewingBeforeAcceptanceRequired,
termsExpiration,
userReacceptRequiredFrequency
FROM entra_id.identity_governance.terms_of_use_agreements
WHERE agreement-id = '{{ agreement-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of agreement objects.

```sql
SELECT
id,
@odata.type,
acceptances,
displayName,
file,
files,
isPerDeviceAcceptanceRequired,
isViewingBeforeAcceptanceRequired,
termsExpiration,
userReacceptRequiredFrequency
FROM entra_id.identity_governance.terms_of_use_agreements
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

Create a new agreement object.

```sql
INSERT INTO entra_id.identity_governance.terms_of_use_agreements (
id,
@odata.type,
displayName,
isPerDeviceAcceptanceRequired,
isViewingBeforeAcceptanceRequired,
termsExpiration,
userReacceptRequiredFrequency,
acceptances,
file,
files
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ displayName }}',
{{ isPerDeviceAcceptanceRequired }},
{{ isViewingBeforeAcceptanceRequired }},
'{{ termsExpiration }}',
'{{ userReacceptRequiredFrequency }}',
'{{ acceptances }}',
'{{ file }}',
'{{ files }}'
RETURNING
id,
@odata.type,
acceptances,
displayName,
file,
files,
isPerDeviceAcceptanceRequired,
isViewingBeforeAcceptanceRequired,
termsExpiration,
userReacceptRequiredFrequency
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: terms_of_use_agreements
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name of the agreement. The display name is used for internal tracking of the agreement but isn't shown to end users who view the agreement. Supports $filter (eq).
    - name: isPerDeviceAcceptanceRequired
      value: {{ isPerDeviceAcceptanceRequired }}
      description: |
        Indicates whether end users are required to accept this agreement on every device that they access it from. The end user is required to register their device in Microsoft Entra ID, if they haven't already done so. Supports $filter (eq).
    - name: isViewingBeforeAcceptanceRequired
      value: {{ isViewingBeforeAcceptanceRequired }}
      description: |
        Indicates whether the user has to expand the agreement before accepting. Supports $filter (eq).
    - name: termsExpiration
      value: "{{ termsExpiration }}"
      description: |
        Expiration schedule and frequency of agreement for all users. Supports $filter (eq).
    - name: userReacceptRequiredFrequency
      value: "{{ userReacceptRequiredFrequency }}"
      description: |
        The duration after which the user must reaccept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq).
    - name: acceptances
      description: |
        Read-only. Information about acceptances of this agreement.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          agreementFileId: "{{ agreementFileId }}"
          agreementId: "{{ agreementId }}"
          deviceDisplayName: "{{ deviceDisplayName }}"
          deviceId: "{{ deviceId }}"
          deviceOSType: "{{ deviceOSType }}"
          deviceOSVersion: "{{ deviceOSVersion }}"
          expirationDateTime: "{{ expirationDateTime }}"
          recordedDateTime: "{{ recordedDateTime }}"
          state: "{{ state }}"
          userDisplayName: "{{ userDisplayName }}"
          userEmail: "{{ userEmail }}"
          userId: "{{ userId }}"
          userPrincipalName: "{{ userPrincipalName }}"
    - name: file
      value: "{{ file }}"
      description: |
        Default PDF linked to this agreement.
    - name: files
      description: |
        PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdDateTime: "{{ createdDateTime }}"
          displayName: "{{ displayName }}"
          fileData: "{{ fileData }}"
          fileName: "{{ fileName }}"
          isDefault: {{ isDefault }}
          isMajorVersion: {{ isMajorVersion }}
          language: "{{ language }}"
          versions: "{{ versions }}"
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

Update the properties of an agreement object.

```sql
UPDATE entra_id.identity_governance.terms_of_use_agreements
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
displayName = '{{ displayName }}',
isPerDeviceAcceptanceRequired = {{ isPerDeviceAcceptanceRequired }},
isViewingBeforeAcceptanceRequired = {{ isViewingBeforeAcceptanceRequired }},
termsExpiration = '{{ termsExpiration }}',
userReacceptRequiredFrequency = '{{ userReacceptRequiredFrequency }}',
acceptances = '{{ acceptances }}',
file = '{{ file }}',
files = '{{ files }}'
WHERE 
agreement-id = '{{ agreement-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
acceptances,
displayName,
file,
files,
isPerDeviceAcceptanceRequired,
isViewingBeforeAcceptanceRequired,
termsExpiration,
userReacceptRequiredFrequency;
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

Delete an agreement object.

```sql
DELETE FROM entra_id.identity_governance.terms_of_use_agreements
WHERE agreement-id = '{{ agreement-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
