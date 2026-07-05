--- 
title: authentication_temporary_access_pass_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_temporary_access_pass_methods
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

Creates, updates, deletes, gets or lists an <code>authentication_temporary_access_pass_methods</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_temporary_access_pass_methods" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.authentication_temporary_access_pass_methods" /></td></tr>
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
    <td><CopyableCode code="isUsable" /></td>
    <td><code>boolean</code></td>
    <td>The state of the authentication method that indicates whether it's currently usable by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="isUsableOnce" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.</td>
</tr>
<tr>
    <td><CopyableCode code="lifetimeInMinutes" /></td>
    <td><code>number (int32)</code></td>
    <td>The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).</td>
</tr>
<tr>
    <td><CopyableCode code="methodUsabilityReason" /></td>
    <td><code>string</code></td>
    <td>Details about the usability state (isUsable). Reasons can include: EnabledByPolicy, DisabledByPolicy, Expired, NotYetValid, OneTimeUsed.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="temporaryAccessPass" /></td>
    <td><code>string</code></td>
    <td>The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.</td>
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
    <td><CopyableCode code="isUsable" /></td>
    <td><code>boolean</code></td>
    <td>The state of the authentication method that indicates whether it's currently usable by the user.</td>
</tr>
<tr>
    <td><CopyableCode code="isUsableOnce" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.</td>
</tr>
<tr>
    <td><CopyableCode code="lifetimeInMinutes" /></td>
    <td><code>number (int32)</code></td>
    <td>The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).</td>
</tr>
<tr>
    <td><CopyableCode code="methodUsabilityReason" /></td>
    <td><code>string</code></td>
    <td>Details about the usability state (isUsable). Reasons can include: EnabledByPolicy, DisabledByPolicy, Expired, NotYetValid, OneTimeUsed.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="temporaryAccessPass" /></td>
    <td><code>string</code></td>
    <td>The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.</td>
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
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-temporary_access_pass_authentication_method_id"><code>temporary_access_pass_authentication_method_id</code></a></td>
    <td></td>
    <td>Retrieve a user's single temporaryAccessPassAuthenticationMethod object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>Retrieve a list of a user's temporaryAccessPassAuthenticationMethod objects and their properties. This API will only return a single object in the collection as a user can have only one Temporary Access Pass method.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a></td>
    <td></td>
    <td>Create a new temporaryAccessPassAuthenticationMethod object on a user. A user can only have one Temporary Access Pass that's usable within its specified lifetime. If the user requires a new Temporary Access Pass while the current Temporary Access Pass is valid, the admin can create a new Temporary Access Pass for the user, the previous Temporary Access Pass will be deleted, and a new Temporary Access Pass will be created.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user_id"><code>user_id</code></a>, <a href="#parameter-temporary_access_pass_authentication_method_id"><code>temporary_access_pass_authentication_method_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a users's temporaryAccessPassAuthenticationMethod object.</td>
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
<tr id="parameter-temporary_access_pass_authentication_method_id">
    <td><CopyableCode code="temporary_access_pass_authentication_method_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of temporaryAccessPassAuthenticationMethod</td>
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

Retrieve a user's single temporaryAccessPassAuthenticationMethod object.

```sql
SELECT
id,
createdDateTime,
isUsable,
isUsableOnce,
lifetimeInMinutes,
methodUsabilityReason,
startDateTime,
temporaryAccessPass
FROM entra_id.users.authentication_temporary_access_pass_methods
WHERE user_id = '{{ user_id }}' -- required
AND temporary_access_pass_authentication_method_id = '{{ temporary_access_pass_authentication_method_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of a user's temporaryAccessPassAuthenticationMethod objects and their properties. This API will only return a single object in the collection as a user can have only one Temporary Access Pass method.

```sql
SELECT
id,
createdDateTime,
isUsable,
isUsableOnce,
lifetimeInMinutes,
methodUsabilityReason,
startDateTime,
temporaryAccessPass
FROM entra_id.users.authentication_temporary_access_pass_methods
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

Create a new temporaryAccessPassAuthenticationMethod object on a user. A user can only have one Temporary Access Pass that's usable within its specified lifetime. If the user requires a new Temporary Access Pass while the current Temporary Access Pass is valid, the admin can create a new Temporary Access Pass for the user, the previous Temporary Access Pass will be deleted, and a new Temporary Access Pass will be created.

```sql
INSERT INTO entra_id.users.authentication_temporary_access_pass_methods (
id,
createdDateTime,
isUsable,
isUsableOnce,
lifetimeInMinutes,
methodUsabilityReason,
startDateTime,
temporaryAccessPass,
user_id
)
SELECT 
'{{ id }}',
'{{ createdDateTime }}',
{{ isUsable }},
{{ isUsableOnce }},
{{ lifetimeInMinutes }},
'{{ methodUsabilityReason }}',
'{{ startDateTime }}',
'{{ temporaryAccessPass }}',
'{{ user_id }}'
RETURNING
id,
createdDateTime,
isUsable,
isUsableOnce,
lifetimeInMinutes,
methodUsabilityReason,
startDateTime,
temporaryAccessPass
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: authentication_temporary_access_pass_methods
  props:
    - name: user_id
      value: "{{ user_id }}"
      description: Required parameter for the authentication_temporary_access_pass_methods resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        Represents the date and time when an entity was created. Read-only.
    - name: isUsable
      value: {{ isUsable }}
      description: |
        The state of the authentication method that indicates whether it's currently usable by the user.
    - name: isUsableOnce
      value: {{ isUsableOnce }}
      description: |
        Determines whether the pass is limited to a one-time use. If true, the pass can be used once; if false, the pass can be used multiple times within the Temporary Access Pass lifetime.
    - name: lifetimeInMinutes
      value: {{ lifetimeInMinutes }}
      description: |
        The lifetime of the Temporary Access Pass in minutes starting at startDateTime. Must be between 10 and 43200 inclusive (equivalent to 30 days).
    - name: methodUsabilityReason
      value: "{{ methodUsabilityReason }}"
      description: |
        Details about the usability state (isUsable). Reasons can include: EnabledByPolicy, DisabledByPolicy, Expired, NotYetValid, OneTimeUsed.
    - name: startDateTime
      value: "{{ startDateTime }}"
      description: |
        The date and time when the Temporary Access Pass becomes available to use and when isUsable is true is enforced.
    - name: temporaryAccessPass
      value: "{{ temporaryAccessPass }}"
      description: |
        The Temporary Access Pass used to authenticate. Returned only on creation of a new temporaryAccessPassAuthenticationMethod object; Hidden in subsequent read operations and returned as null with GET.
`}</CodeBlock>

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

Delete a users's temporaryAccessPassAuthenticationMethod object.

```sql
DELETE FROM entra_id.users.authentication_temporary_access_pass_methods
WHERE user_id = '{{ user_id }}' --required
AND temporary_access_pass_authentication_method_id = '{{ temporary_access_pass_authentication_method_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
