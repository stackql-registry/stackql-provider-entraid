--- 
title: authentication
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication
  - users
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

Creates, updates, deletes, gets or lists an <code>authentication</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.users.authentication" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="emailMethods" /></td>
    <td><code>array</code></td>
    <td>The email address registered to a user for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="externalAuthenticationMethods" /></td>
    <td><code>array</code></td>
    <td>Represents the external MFA registered to a user for authentication using an external identity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="fido2Methods" /></td>
    <td><code>array</code></td>
    <td>Represents the FIDO2 security keys registered to a user for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="methods" /></td>
    <td><code>array</code></td>
    <td>Represents all authentication methods registered to a user.</td>
</tr>
<tr>
    <td><CopyableCode code="microsoftAuthenticatorMethods" /></td>
    <td><code>array</code></td>
    <td>The details of the Microsoft Authenticator app registered to a user for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="operations" /></td>
    <td><code>array</code></td>
    <td>Represents the status of a long-running operation, such as a password reset operation.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordMethods" /></td>
    <td><code>array</code></td>
    <td>Represents the password registered to a user for authentication. For security, the password itself is never returned in the object, but action can be taken to reset a password.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneMethods" /></td>
    <td><code>array</code></td>
    <td>The phone numbers registered to a user for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="platformCredentialMethods" /></td>
    <td><code>array</code></td>
    <td>Represents a platform credential instance registered to a user on Mac OS.</td>
</tr>
<tr>
    <td><CopyableCode code="softwareOathMethods" /></td>
    <td><code>array</code></td>
    <td>The software OATH time-based one-time password (TOTP) applications registered to a user for authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="temporaryAccessPassMethods" /></td>
    <td><code>array</code></td>
    <td>Represents a Temporary Access Pass registered to a user for authentication through time-limited passcodes.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsHelloForBusinessMethods" /></td>
    <td><code>array</code></td>
    <td>Represents the Windows Hello for Business authentication method registered to a user for authentication.</td>
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
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The authentication methods that are supported for the user.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
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
<tr id="parameter-user-id">
    <td><CopyableCode code="user-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of user</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
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

The authentication methods that are supported for the user.

```sql
SELECT
id,
@odata.type,
emailMethods,
externalAuthenticationMethods,
fido2Methods,
methods,
microsoftAuthenticatorMethods,
operations,
passwordMethods,
phoneMethods,
platformCredentialMethods,
softwareOathMethods,
temporaryAccessPassMethods,
windowsHelloForBusinessMethods
FROM entraid.users.authentication
WHERE user-id = '{{ user-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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
UPDATE entraid.users.authentication
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
emailMethods = '{{ emailMethods }}',
externalAuthenticationMethods = '{{ externalAuthenticationMethods }}',
fido2Methods = '{{ fido2Methods }}',
methods = '{{ methods }}',
microsoftAuthenticatorMethods = '{{ microsoftAuthenticatorMethods }}',
operations = '{{ operations }}',
passwordMethods = '{{ passwordMethods }}',
phoneMethods = '{{ phoneMethods }}',
platformCredentialMethods = '{{ platformCredentialMethods }}',
softwareOathMethods = '{{ softwareOathMethods }}',
temporaryAccessPassMethods = '{{ temporaryAccessPassMethods }}',
windowsHelloForBusinessMethods = '{{ windowsHelloForBusinessMethods }}'
WHERE 
user-id = '{{ user-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
emailMethods,
externalAuthenticationMethods,
fido2Methods,
methods,
microsoftAuthenticatorMethods,
operations,
passwordMethods,
phoneMethods,
platformCredentialMethods,
softwareOathMethods,
temporaryAccessPassMethods,
windowsHelloForBusinessMethods;
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
DELETE FROM entraid.users.authentication
WHERE user-id = '{{ user-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
