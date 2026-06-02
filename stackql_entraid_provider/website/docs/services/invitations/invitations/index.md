--- 
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - invitations
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

Creates, updates, deletes, gets or lists an <code>invitations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invitations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.invitations.invitations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="inviteRedeemUrl" /></td>
    <td><code>string</code></td>
    <td>The URL the user can use to redeem their invitation. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="inviteRedirectUrl" /></td>
    <td><code>string</code></td>
    <td>The URL the user should be redirected to after the invitation is redeemed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="invitedUser" /></td>
    <td><code></code></td>
    <td>The user created as part of the invitation creation. Read-only. The id property is required in the request body to reset a redemption status.</td>
</tr>
<tr>
    <td><CopyableCode code="invitedUserDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user being invited.</td>
</tr>
<tr>
    <td><CopyableCode code="invitedUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user being invited. Required. The following special characters aren't permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces (&#123; &#125;)Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (&lt; &gt;)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name, including at the beginning or end of the name.</td>
</tr>
<tr>
    <td><CopyableCode code="invitedUserMessageInfo" /></td>
    <td><code></code></td>
    <td>Contains configuration for the message being sent to the invited user, including customizing message text, language, and cc recipient list.</td>
</tr>
<tr>
    <td><CopyableCode code="invitedUserSponsors" /></td>
    <td><code>array</code></td>
    <td>The users or groups who are sponsors of the invited user. Sponsors are users and groups that are responsible for guest users' privileges in the tenant and for keeping the guest users' information and access up to date.</td>
</tr>
<tr>
    <td><CopyableCode code="invitedUserType" /></td>
    <td><code>string</code></td>
    <td>The userType of the user being invited. By default, this is Guest. You can invite as Member if you're a company administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="resetRedemption" /></td>
    <td><code>boolean</code></td>
    <td>Reset the user's redemption status and reinvite a user while retaining their user identifier, group memberships, and app assignments. This property allows you to enable a user to sign-in using a different email address from the one in the previous invitation. When true, the invitedUser/id relationship is required. For more information about using this property, see Reset redemption status for a guest user.</td>
</tr>
<tr>
    <td><CopyableCode code="sendInvitationMessage" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether an email should be sent to the user being invited. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the invitation. The possible values are: PendingAcceptance, Completed, InProgress, and Error.</td>
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
    <td>Use this API to create a new invitation or reset the redemption status for a guest user who already redeemed their invitation. The invitation adds the external user to the organization as part of B2B collaboration. B2B collaboration is supported in both Microsoft Entra External ID in workforce and external tenants. When creating a new invitation, you have several options available:</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
@odata.type,
inviteRedeemUrl,
inviteRedirectUrl,
invitedUser,
invitedUserDisplayName,
invitedUserEmailAddress,
invitedUserMessageInfo,
invitedUserSponsors,
invitedUserType,
resetRedemption,
sendInvitationMessage,
status
FROM entra_id.invitations.invitations
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

Use this API to create a new invitation or reset the redemption status for a guest user who already redeemed their invitation. The invitation adds the external user to the organization as part of B2B collaboration. B2B collaboration is supported in both Microsoft Entra External ID in workforce and external tenants. When creating a new invitation, you have several options available:

```sql
INSERT INTO entra_id.invitations.invitations (
id,
@odata.type,
invitedUserDisplayName,
invitedUserEmailAddress,
invitedUserMessageInfo,
invitedUserType,
inviteRedeemUrl,
inviteRedirectUrl,
resetRedemption,
sendInvitationMessage,
status,
invitedUser,
invitedUserSponsors
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ invitedUserDisplayName }}',
'{{ invitedUserEmailAddress }}',
'{{ invitedUserMessageInfo }}',
'{{ invitedUserType }}',
'{{ inviteRedeemUrl }}',
'{{ inviteRedirectUrl }}',
{{ resetRedemption }},
{{ sendInvitationMessage }},
'{{ status }}',
'{{ invitedUser }}',
'{{ invitedUserSponsors }}'
RETURNING
id,
@odata.type,
inviteRedeemUrl,
inviteRedirectUrl,
invitedUser,
invitedUserDisplayName,
invitedUserEmailAddress,
invitedUserMessageInfo,
invitedUserSponsors,
invitedUserType,
resetRedemption,
sendInvitationMessage,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: invitations
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: invitedUserDisplayName
      value: "{{ invitedUserDisplayName }}"
      description: |
        The display name of the user being invited.
    - name: invitedUserEmailAddress
      value: "{{ invitedUserEmailAddress }}"
      description: |
        The email address of the user being invited. Required. The following special characters aren't permitted in the email address:Tilde (~)Exclamation point (!)Number sign (#)Dollar sign ($)Percent (%)Circumflex (^)Ampersand (&)Asterisk (*)Parentheses (( ))Plus sign (+)Equal sign (=)Brackets ([ ])Braces ({ })Backslash (/)Slash mark (/)Pipe (/|)Semicolon (;)Colon (:)Quotation marks (')Angle brackets (< >)Question mark (?)Comma (,)However, the following exceptions apply:A period (.) or a hyphen (-) is permitted anywhere in the user name, except at the beginning or end of the name.An underscore (_) is permitted anywhere in the user name, including at the beginning or end of the name.
    - name: invitedUserMessageInfo
      value: "{{ invitedUserMessageInfo }}"
      description: |
        Contains configuration for the message being sent to the invited user, including customizing message text, language, and cc recipient list.
    - name: invitedUserType
      value: "{{ invitedUserType }}"
      description: |
        The userType of the user being invited. By default, this is Guest. You can invite as Member if you're a company administrator.
    - name: inviteRedeemUrl
      value: "{{ inviteRedeemUrl }}"
      description: |
        The URL the user can use to redeem their invitation. Read-only.
    - name: inviteRedirectUrl
      value: "{{ inviteRedirectUrl }}"
      description: |
        The URL the user should be redirected to after the invitation is redeemed. Required.
    - name: resetRedemption
      value: {{ resetRedemption }}
      description: |
        Reset the user's redemption status and reinvite a user while retaining their user identifier, group memberships, and app assignments. This property allows you to enable a user to sign-in using a different email address from the one in the previous invitation. When true, the invitedUser/id relationship is required. For more information about using this property, see Reset redemption status for a guest user.
    - name: sendInvitationMessage
      value: {{ sendInvitationMessage }}
      description: |
        Indicates whether an email should be sent to the user being invited. The default is false.
    - name: status
      value: "{{ status }}"
      description: |
        The status of the invitation. The possible values are: PendingAcceptance, Completed, InProgress, and Error.
    - name: invitedUser
      value: "{{ invitedUser }}"
      description: |
        The user created as part of the invitation creation. Read-only. The id property is required in the request body to reset a redemption status.
    - name: invitedUserSponsors
      description: |
        The users or groups who are sponsors of the invited user. Sponsors are users and groups that are responsible for guest users' privileges in the tenant and for keeping the guest users' information and access up to date.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
`}</CodeBlock>

</TabItem>
</Tabs>
