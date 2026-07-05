--- 
title: authorization_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_policy
  - policies
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

Creates, updates, deletes, gets or lists an <code>authorization_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authorization_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.authorization_policy" /></td></tr>
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
    <td><CopyableCode code="allowEmailVerifiedUsersToJoinOrganization" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether a user can join the tenant by email validation.</td>
</tr>
<tr>
    <td><CopyableCode code="allowInvitesFrom" /></td>
    <td><code></code></td>
    <td>Indicates who can invite guests to the organization. The possible values are: none, adminsAndGuestInviters, adminsGuestInvitersAndAllMembers, everyone.  everyone is the default setting for all cloud environments except US Government. For more information, see allowInvitesFrom values.</td>
</tr>
<tr>
    <td><CopyableCode code="allowUserConsentForRiskyApps" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether user consent for risky apps is allowed. We recommend keeping allowUserConsentForRiskyApps as false. Default value is false.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedToSignUpEmailBasedSubscriptions" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether users can sign up for email based subscriptions.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedToUseSSPR" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether administrators of the tenant can use the Self-Service Password Reset (SSPR). For more information, see Self-service password reset for administrators.</td>
</tr>
<tr>
    <td><CopyableCode code="blockMsolPowerShell" /></td>
    <td><code>boolean</code></td>
    <td>To disable the use of MSOL PowerShell, set this property to true. This also disables user-based access to the legacy service endpoint used by MSOL PowerShell. This doesn't affect Microsoft Entra Connect or Microsoft Graph.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultUserRolePermissions" /></td>
    <td><code>object</code></td>
    <td> (title: defaultUserRolePermissions)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="guestUserRoleId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Represents role templateId for the role that should be granted to guests. Currently following roles are supported:  User (a0b1b346-4d3e-4e8b-98f8-753987be4970), Guest User (10dae51f-b6af-4016-8d66-8c2a99b929b3), and Restricted Guest User (2af84b1e-32c8-42b7-82bc-daa82404023b). (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
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
    <td></td>
    <td></td>
    <td>Retrieve the properties of an authorizationPolicy object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Update the properties of an authorizationPolicy object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
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

Retrieve the properties of an authorizationPolicy object.

```sql
SELECT
id,
allowEmailVerifiedUsersToJoinOrganization,
allowInvitesFrom,
allowUserConsentForRiskyApps,
allowedToSignUpEmailBasedSubscriptions,
allowedToUseSSPR,
blockMsolPowerShell,
defaultUserRolePermissions,
deletedDateTime,
description,
displayName,
guestUserRoleId
FROM entra_id.policies.authorization_policy
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

Update the properties of an authorizationPolicy object.

```sql
UPDATE entra_id.policies.authorization_policy
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
allowedToSignUpEmailBasedSubscriptions = {{ allowedToSignUpEmailBasedSubscriptions }},
allowedToUseSSPR = {{ allowedToUseSSPR }},
allowEmailVerifiedUsersToJoinOrganization = {{ allowEmailVerifiedUsersToJoinOrganization }},
allowInvitesFrom = '{{ allowInvitesFrom }}',
allowUserConsentForRiskyApps = {{ allowUserConsentForRiskyApps }},
blockMsolPowerShell = {{ blockMsolPowerShell }},
defaultUserRolePermissions = '{{ defaultUserRolePermissions }}',
guestUserRoleId = '{{ guestUserRoleId }}'
RETURNING
id,
allowEmailVerifiedUsersToJoinOrganization,
allowInvitesFrom,
allowUserConsentForRiskyApps,
allowedToSignUpEmailBasedSubscriptions,
allowedToUseSSPR,
blockMsolPowerShell,
defaultUserRolePermissions,
deletedDateTime,
description,
displayName,
guestUserRoleId;
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
DELETE FROM entra_id.policies.authorization_policy
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
