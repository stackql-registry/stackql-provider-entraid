--- 
title: authentication_fido2_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_fido2_methods
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

Creates, updates, deletes, gets or lists an <code>authentication_fido2_methods</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_fido2_methods" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.authentication_fido2_methods" /></td></tr>
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
    <td><CopyableCode code="aaGuid" /></td>
    <td><code>string</code></td>
    <td>Authenticator Attestation GUID, an identifier that indicates the type (such as make and model) of the authenticator.</td>
</tr>
<tr>
    <td><CopyableCode code="attestationCertificates" /></td>
    <td><code>array</code></td>
    <td>The attestation certificate or certificates attached to this passkey.</td>
</tr>
<tr>
    <td><CopyableCode code="attestationLevel" /></td>
    <td><code></code></td>
    <td>The attestation level of this passkey (FIDO2). The possible values are: attested, notAttested, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the date and time when an entity was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the key as given by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The manufacturer-assigned model of the FIDO2 passkey.</td>
</tr>
<tr>
    <td><CopyableCode code="passkeyType" /></td>
    <td><code></code></td>
    <td>The type of passkey. The possible values are: deviceBound, synced, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKeyCredential" /></td>
    <td><code></code></td>
    <td></td>
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
    <td><CopyableCode code="aaGuid" /></td>
    <td><code>string</code></td>
    <td>Authenticator Attestation GUID, an identifier that indicates the type (such as make and model) of the authenticator.</td>
</tr>
<tr>
    <td><CopyableCode code="attestationCertificates" /></td>
    <td><code>array</code></td>
    <td>The attestation certificate or certificates attached to this passkey.</td>
</tr>
<tr>
    <td><CopyableCode code="attestationLevel" /></td>
    <td><code></code></td>
    <td>The attestation level of this passkey (FIDO2). The possible values are: attested, notAttested, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the date and time when an entity was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the key as given by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>The manufacturer-assigned model of the FIDO2 passkey.</td>
</tr>
<tr>
    <td><CopyableCode code="passkeyType" /></td>
    <td><code></code></td>
    <td>The type of passkey. The possible values are: deviceBound, synced, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKeyCredential" /></td>
    <td><code></code></td>
    <td></td>
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
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-fido2_authentication_method_id"><code>fido2_authentication_method_id</code></a></td>
    <td></td>
    <td>Represents the FIDO2 security keys registered to a user for authentication.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>Represents the FIDO2 security keys registered to a user for authentication.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-fido2_authentication_method_id"><code>fido2_authentication_method_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes a user's FIDO2 security key authentication method object.</td>
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
<tr id="parameter-fido2_authentication_method_id">
    <td><CopyableCode code="fido2_authentication_method_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of fido2AuthenticationMethod</td>
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

Represents the FIDO2 security keys registered to a user for authentication.

```sql
SELECT
id,
aaGuid,
attestationCertificates,
attestationLevel,
createdDateTime,
displayName,
model,
passkeyType,
publicKeyCredential
FROM entra_id.users.authentication_fido2_methods
WHERE user_id = '{{ user_id }}' -- required
AND fido2_authentication_method_id = '{{ fido2_authentication_method_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Represents the FIDO2 security keys registered to a user for authentication.

```sql
SELECT
id,
aaGuid,
attestationCertificates,
attestationLevel,
createdDateTime,
displayName,
model,
passkeyType,
publicKeyCredential
FROM entra_id.users.authentication_fido2_methods
WHERE user_id = '{{ user_id }}' -- required
;
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

Deletes a user's FIDO2 security key authentication method object.

```sql
DELETE FROM entra_id.users.authentication_fido2_methods
WHERE user_id = '{{ user_id }}' --required
AND fido2_authentication_method_id = '{{ fido2_authentication_method_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
