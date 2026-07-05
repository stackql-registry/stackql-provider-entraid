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
    <td>The duration after which the user must reaccept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq). (pattern: <code>^-?P(&#91;0-9&#93;+D)?(T(&#91;0-9&#93;+H)?(&#91;0-9&#93;+M)?(&#91;0-9&#93;+(&#91;.&#93;&#91;0-9&#93;+)?S)?)?$</code>)</td>
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
    <td>The duration after which the user must reaccept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq). (pattern: <code>^-?P(&#91;0-9&#93;+D)?(T(&#91;0-9&#93;+H)?(&#91;0-9&#93;+M)?(&#91;0-9&#93;+(&#91;.&#93;&#91;0-9&#93;+)?S)?)?$</code>)</td>
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
    <td><a href="#parameter-agreement_id"><code>agreement_id</code></a></td>
    <td></td>
    <td>Retrieve the properties and relationships of an agreement object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of agreement objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new agreement object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-agreement_id"><code>agreement_id</code></a></td>
    <td></td>
    <td>Update the properties of an agreement object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-agreement_id"><code>agreement_id</code></a></td>
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
<tr id="parameter-agreement_id">
    <td><CopyableCode code="agreement_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of agreement</td>
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
acceptances,
displayName,
file,
files,
isPerDeviceAcceptanceRequired,
isViewingBeforeAcceptanceRequired,
termsExpiration,
userReacceptRequiredFrequency
FROM entra_id.identity_governance.terms_of_use_agreements
WHERE agreement_id = '{{ agreement_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of agreement objects.

```sql
SELECT
id,
acceptances,
displayName,
file,
files,
isPerDeviceAcceptanceRequired,
isViewingBeforeAcceptanceRequired,
termsExpiration,
userReacceptRequiredFrequency
FROM entra_id.identity_governance.terms_of_use_agreements
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
displayName = '{{ displayName }}',
isPerDeviceAcceptanceRequired = {{ isPerDeviceAcceptanceRequired }},
isViewingBeforeAcceptanceRequired = {{ isViewingBeforeAcceptanceRequired }},
termsExpiration = '{{ termsExpiration }}',
userReacceptRequiredFrequency = '{{ userReacceptRequiredFrequency }}',
acceptances = '{{ acceptances }}',
file = '{{ file }}',
files = '{{ files }}'
WHERE 
agreement_id = '{{ agreement_id }}' --required
RETURNING
id,
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
WHERE agreement_id = '{{ agreement_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
