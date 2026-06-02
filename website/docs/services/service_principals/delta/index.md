--- 
title: delta
hide_title: false
hide_table_of_contents: false
keywords:
  - delta
  - service_principals
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

Creates, updates, deletes, gets or lists a <code>delta</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delta" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.delta" /></td></tr>
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
    <td><CopyableCode code="accountEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the service principal account is enabled; otherwise, false. If set to false, then no users are able to sign in to this app, even if they're assigned to it. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="addIns" /></td>
    <td><code>array</code></td>
    <td>Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.</td>
</tr>
<tr>
    <td><CopyableCode code="alternativeNames" /></td>
    <td><code>array</code></td>
    <td>Used to retrieve service principals by subscription, identify resource group and full resource IDs for managed identities. Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="appDescription" /></td>
    <td><code>string</code></td>
    <td>The description exposed by the associated application.</td>
</tr>
<tr>
    <td><CopyableCode code="appDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name exposed by the associated application. Maximum length is 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated application (its appId property). Alternate key. Supports $filter (eq, ne, not, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="appManagementPolicies" /></td>
    <td><code>array</code></td>
    <td>The appManagementPolicy applied to this application.</td>
</tr>
<tr>
    <td><CopyableCode code="appOwnerOrganizationId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Contains the tenant ID where the application is registered. This is applicable only to service principals backed by applications. Supports $filter (eq, ne, NOT, ge, le). (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignedTo" /></td>
    <td><code>array</code></td>
    <td>App role assignments for this app or service, granted to users, groups, and other service principals. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignmentRequired" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable. Supports $filter (eq, ne, NOT).</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignments" /></td>
    <td><code>array</code></td>
    <td>App role assignment for another app or service, granted to this service principal. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoles" /></td>
    <td><code>array</code></td>
    <td>The roles exposed by the application that's linked to this service principal. For more information, see the appRoles property definition on the application entity. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTemplateId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the service principal wasn't created from an application template.</td>
</tr>
<tr>
    <td><CopyableCode code="claimsMappingPolicies" /></td>
    <td><code>array</code></td>
    <td>The claimsMappingPolicies assigned to this service principal. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByAppId" /></td>
    <td><code>string</code></td>
    <td>The appId of the application that created this service principal. Set internally by Microsoft Entra ID. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects created by this service principal. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="customSecurityAttributes" /></td>
    <td><code></code></td>
    <td>An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedPermissionClassifications" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Free text field to provide an internal end-user facing description of the service principal. End-user portals such MyApps displays the application description in this field. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledByMicrosoftStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the service principal. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="federatedIdentityCredentials" /></td>
    <td><code>array</code></td>
    <td>Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="homeRealmDiscoveryPolicies" /></td>
    <td><code>array</code></td>
    <td>The homeRealmDiscoveryPolicies assigned to this service principal. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="homepage" /></td>
    <td><code>string</code></td>
    <td>Home page or landing page of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="info" /></td>
    <td><code></code></td>
    <td>Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="keyCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of key credentials associated with the service principal. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="loginUrl" /></td>
    <td><code>string</code></td>
    <td>Specifies the URL where the service provider redirects the user to Microsoft Entra ID to authenticate. Microsoft Entra ID uses the URL to launch the application from Microsoft 365 or the Microsoft Entra My Apps. When blank, Microsoft Entra ID performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Microsoft Entra My Apps, or the Microsoft Entra SSO URL.</td>
</tr>
<tr>
    <td><CopyableCode code="logoutUrl" /></td>
    <td><code>string</code></td>
    <td>Specifies the URL that the Microsoft's authorization service uses to sign out a user using OpenID Connect front-channel, back-channel, or SAML sign out protocols.</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1,024 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationEmailAddresses" /></td>
    <td><code>array</code></td>
    <td>Specifies the list of email addresses where Microsoft Entra ID sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Microsoft Entra Gallery applications.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2PermissionGrants" /></td>
    <td><code>array</code></td>
    <td>Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2PermissionScopes" /></td>
    <td><code>array</code></td>
    <td>The delegated permissions exposed by the application. For more information, see the oauth2PermissionScopes property on the application entity's api property. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="ownedObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects that this service principal owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>Directory objects that are owners of this servicePrincipal. The owners are a set of nonadmin users or servicePrincipals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of password credentials associated with the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredSingleSignOnMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the single sign-on mode configured for this application. Microsoft Entra ID uses the preferred single sign-on mode to launch the application from Microsoft 365 or the My Apps portal. The supported values are password, saml, notSupported, and oidc. Note: This field might be null for older SAML apps and for OIDC applications where it isn't set automatically.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredTokenSigningKeyThumbprint" /></td>
    <td><code>string</code></td>
    <td>This property can be used on SAML applications (apps that have preferredSingleSignOnMode set to saml) to control which certificate is used to sign the SAML responses. For applications that aren't SAML, don't write or otherwise rely on this property.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDesktopSecurityConfiguration" /></td>
    <td><code></code></td>
    <td>The remoteDesktopSecurityConfiguration object applied to this service principal. Supports $filter (eq) for isRemoteDesktopProtocolEnabled property.</td>
</tr>
<tr>
    <td><CopyableCode code="replyUrls" /></td>
    <td><code>array</code></td>
    <td>The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceSpecificApplicationPermissions" /></td>
    <td><code>array</code></td>
    <td>The resource-specific application permissions exposed by this application. Currently, resource-specific permissions are only supported for Teams apps accessing to specific chats and teams using Microsoft Graph. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="samlSingleSignOnSettings" /></td>
    <td><code></code></td>
    <td>The collection for settings related to saml single sign-on.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalNames" /></td>
    <td><code>array</code></td>
    <td>Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Microsoft Entra ID. For example,Client apps can specify a resource URI that is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalType" /></td>
    <td><code>string</code></td>
    <td>Identifies whether the service principal represents an application, a managed identity, or a legacy application. This property is set by Microsoft Entra ID internally. The servicePrincipalType property can be set to three different values: Application - A service principal that represents an application or service. The appId property identifies the associated app registration, and matches the appId of an application, possibly from a different tenant. If the associated app registration is missing, tokens aren't issued for the service principal.ManagedIdentity - A service principal that represents a managed identity. Service principals representing managed identities can be granted access and permissions, but can't be updated or modified directly.Legacy - A service principal that represents an app created before app registrations, or through legacy experiences. A legacy service principal can have credentials, service principal names, reply URLs, and other properties that are editable by an authorized user, but doesn't have an associated app registration. The appId value doesn't associate the service principal with an app registration. The service principal can only be used in the tenant where it was created.ServiceIdentity - A service principal that represents an agent identity.SocialIdp - For internal use.</td>
</tr>
<tr>
    <td><CopyableCode code="signInAudience" /></td>
    <td><code>string</code></td>
    <td>Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization's Microsoft Entra tenant (single-tenant).AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization's Microsoft Entra tenant (multitenant).AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization's Microsoft Entra tenant.PersonalMicrosoftAccount: Users with a personal Microsoft account only.</td>
</tr>
<tr>
    <td><CopyableCode code="synchronization" /></td>
    <td><code></code></td>
    <td>Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Custom strings that can be used to categorize and identify the service principal. Not nullable. The value is the union of strings set here and on the associated application entity's tags property.Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="tokenEncryptionKeyId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user. (pattern: <code>^[0-9a-fA-F]&#123;8&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;4&#125;-[0-9a-fA-F]&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuancePolicies" /></td>
    <td><code>array</code></td>
    <td>The tokenIssuancePolicies assigned to this service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenLifetimePolicies" /></td>
    <td><code>array</code></td>
    <td>The tokenLifetimePolicies assigned to this service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="verifiedPublisher" /></td>
    <td><code></code></td>
    <td>Specifies the verified publisher of the application that's linked to this service principal.</td>
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
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get newly created, updated, or deleted service principals without having to perform a full read of the entire resource collection. For more information, see Use delta query to track changes in Microsoft Graph data for details.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get newly created, updated, or deleted service principals without having to perform a full read of the entire resource collection. For more information, see Use delta query to track changes in Microsoft Graph data for details.

```sql
SELECT
id,
@odata.type,
accountEnabled,
addIns,
alternativeNames,
appDescription,
appDisplayName,
appId,
appManagementPolicies,
appOwnerOrganizationId,
appRoleAssignedTo,
appRoleAssignmentRequired,
appRoleAssignments,
appRoles,
applicationTemplateId,
claimsMappingPolicies,
createdByAppId,
createdObjects,
customSecurityAttributes,
delegatedPermissionClassifications,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
endpoints,
federatedIdentityCredentials,
homeRealmDiscoveryPolicies,
homepage,
info,
isDisabled,
keyCredentials,
loginUrl,
logoutUrl,
memberOf,
notes,
notificationEmailAddresses,
oauth2PermissionGrants,
oauth2PermissionScopes,
ownedObjects,
owners,
passwordCredentials,
preferredSingleSignOnMode,
preferredTokenSigningKeyThumbprint,
remoteDesktopSecurityConfiguration,
replyUrls,
resourceSpecificApplicationPermissions,
samlSingleSignOnSettings,
servicePrincipalNames,
servicePrincipalType,
signInAudience,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
transitiveMemberOf,
verifiedPublisher
FROM entra_id.service_principals.delta
WHERE $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $select = '{{ $select }}'
AND $orderby = '{{ $orderby }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
