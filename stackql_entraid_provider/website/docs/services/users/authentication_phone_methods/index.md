--- 
title: authentication_phone_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_phone_methods
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

Creates, updates, deletes, gets or lists an <code>authentication_phone_methods</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_phone_methods" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.authentication_phone_methods" /></td></tr>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the date and time when an entity was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumber" /></td>
    <td><code>string</code></td>
    <td>The phone number to text or call for authentication. Phone numbers use the format +&#123;country code&#125; &#123;number&#125;x&#123;extension&#125;, with extension optional. For example, +1 5555551234 or +1 5555551234x123 are valid. Numbers are rejected when creating or updating if they don't match the required format.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneType" /></td>
    <td><code></code></td>
    <td>The type of this phone. The possible values are: mobile, alternateMobile, or office.</td>
</tr>
<tr>
    <td><CopyableCode code="smsSignInState" /></td>
    <td><code></code></td>
    <td>Whether a phone is ready to be used for SMS sign-in or not. The possible values are: notSupported, notAllowedByPolicy, notEnabled, phoneNumberNotUnique, ready, or notConfigured, unknownFutureValue.</td>
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents the date and time when an entity was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumber" /></td>
    <td><code>string</code></td>
    <td>The phone number to text or call for authentication. Phone numbers use the format +&#123;country code&#125; &#123;number&#125;x&#123;extension&#125;, with extension optional. For example, +1 5555551234 or +1 5555551234x123 are valid. Numbers are rejected when creating or updating if they don't match the required format.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneType" /></td>
    <td><code></code></td>
    <td>The type of this phone. The possible values are: mobile, alternateMobile, or office.</td>
</tr>
<tr>
    <td><CopyableCode code="smsSignInState" /></td>
    <td><code></code></td>
    <td>Whether a phone is ready to be used for SMS sign-in or not. The possible values are: notSupported, notAllowedByPolicy, notEnabled, phoneNumberNotUnique, ready, or notConfigured, unknownFutureValue.</td>
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
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-phone_authentication_method_id"><code>phone_authentication_method_id</code></a></td>
    <td></td>
    <td>The phone numbers registered to a user for authentication.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>The phone numbers registered to a user for authentication.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>Add a new phone authentication method for a user. A user may only have one phone of each type, captured in the phoneType property. This means, for example, adding a mobile phone to a user with a pre-existing mobile phone fails. Additionally, a user must always have a mobile phone before adding an alternateMobile phone. Adding a phone number makes it available for use in both Azure multi-factor authentication (MFA) and self-service password reset (SSPR), if enabled. Additionally, if a user is enabled by policy to use SMS sign-in and a mobile number is added, the system attempts to register the number for use in that system.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-phone_authentication_method_id"><code>phone_authentication_method_id</code></a></td>
    <td></td>
    <td>Update a user's phone number associated with a phone authentication method object. You can't change a phone's type. To change a phone's type, add a new number of the desired type and then delete the object with the original type. If a user is enabled by policy to use SMS to sign in and the mobile number is changed, the system will attempt to register the number for use in that system. Self-service operations aren't supported.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-phone_authentication_method_id"><code>phone_authentication_method_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#disable_sms_sign_in"><CopyableCode code="disable_sms_sign_in" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-phone_authentication_method_id"><code>phone_authentication_method_id</code></a></td>
    <td></td>
    <td>Disable SMS sign-in for an existing mobile phone number registered to a user. The number will no longer be available for SMS sign-in, which can prevent your user from signing in.</td>
</tr>
<tr>
    <td><a href="#enable_sms_sign_in"><CopyableCode code="enable_sms_sign_in" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-phone_authentication_method_id"><code>phone_authentication_method_id</code></a></td>
    <td></td>
    <td>Enable SMS sign-in for an existing mobile phone number registered to a user. To be successfully enabled:</td>
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
<tr id="parameter-phone_authentication_method_id">
    <td><CopyableCode code="phone_authentication_method_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of phoneAuthenticationMethod</td>
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

The phone numbers registered to a user for authentication.

```sql
SELECT
id,
createdDateTime,
phoneNumber,
phoneType,
smsSignInState
FROM entra_id.users.authentication_phone_methods
WHERE user_id = '{{ user_id }}' -- required
AND phone_authentication_method_id = '{{ phone_authentication_method_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The phone numbers registered to a user for authentication.

```sql
SELECT
id,
createdDateTime,
phoneNumber,
phoneType,
smsSignInState
FROM entra_id.users.authentication_phone_methods
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

Add a new phone authentication method for a user. A user may only have one phone of each type, captured in the phoneType property. This means, for example, adding a mobile phone to a user with a pre-existing mobile phone fails. Additionally, a user must always have a mobile phone before adding an alternateMobile phone. Adding a phone number makes it available for use in both Azure multi-factor authentication (MFA) and self-service password reset (SSPR), if enabled. Additionally, if a user is enabled by policy to use SMS sign-in and a mobile number is added, the system attempts to register the number for use in that system.

```sql
INSERT INTO entra_id.users.authentication_phone_methods (
id,
createdDateTime,
phoneNumber,
phoneType,
smsSignInState,
user_id
)
SELECT 
'{{ id }}',
'{{ createdDateTime }}',
'{{ phoneNumber }}',
'{{ phoneType }}',
'{{ smsSignInState }}',
'{{ user_id }}'
RETURNING
id,
createdDateTime,
phoneNumber,
phoneType,
smsSignInState
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: authentication_phone_methods
  props:
    - name: user_id
      value: "{{ user_id }}"
      description: Required parameter for the authentication_phone_methods resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        Represents the date and time when an entity was created. Read-only.
    - name: phoneNumber
      value: "{{ phoneNumber }}"
      description: |
        The phone number to text or call for authentication. Phone numbers use the format +{country code} {number}x{extension}, with extension optional. For example, +1 5555551234 or +1 5555551234x123 are valid. Numbers are rejected when creating or updating if they don't match the required format.
    - name: phoneType
      value: "{{ phoneType }}"
      description: |
        The type of this phone. The possible values are: mobile, alternateMobile, or office.
    - name: smsSignInState
      value: "{{ smsSignInState }}"
      description: |
        Whether a phone is ready to be used for SMS sign-in or not. The possible values are: notSupported, notAllowedByPolicy, notEnabled, phoneNumberNotUnique, ready, or notConfigured, unknownFutureValue.
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

Update a user's phone number associated with a phone authentication method object. You can't change a phone's type. To change a phone's type, add a new number of the desired type and then delete the object with the original type. If a user is enabled by policy to use SMS to sign in and the mobile number is changed, the system will attempt to register the number for use in that system. Self-service operations aren't supported.

```sql
UPDATE entra_id.users.authentication_phone_methods
SET 
id = '{{ id }}',
createdDateTime = '{{ createdDateTime }}',
phoneNumber = '{{ phoneNumber }}',
phoneType = '{{ phoneType }}',
smsSignInState = '{{ smsSignInState }}'
WHERE 
user_id = '{{ user_id }}' --required
AND phone_authentication_method_id = '{{ phone_authentication_method_id }}' --required
RETURNING
id,
createdDateTime,
phoneNumber,
phoneType,
smsSignInState;
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
DELETE FROM entra_id.users.authentication_phone_methods
WHERE user_id = '{{ user_id }}' --required
AND phone_authentication_method_id = '{{ phone_authentication_method_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="disable_sms_sign_in"
    values={[
        { label: 'disable_sms_sign_in', value: 'disable_sms_sign_in' },
        { label: 'enable_sms_sign_in', value: 'enable_sms_sign_in' }
    ]}
>
<TabItem value="disable_sms_sign_in">

Disable SMS sign-in for an existing mobile phone number registered to a user. The number will no longer be available for SMS sign-in, which can prevent your user from signing in.

```sql
EXEC entra_id.users.authentication_phone_methods.disable_sms_sign_in 
@user_id='{{ user_id }}' --required, 
@phone_authentication_method_id='{{ phone_authentication_method_id }}' --required
;
```
</TabItem>
<TabItem value="enable_sms_sign_in">

Enable SMS sign-in for an existing mobile phone number registered to a user. To be successfully enabled:

```sql
EXEC entra_id.users.authentication_phone_methods.enable_sms_sign_in 
@user_id='{{ user_id }}' --required, 
@phone_authentication_method_id='{{ phone_authentication_method_id }}' --required
;
```
</TabItem>
</Tabs>
