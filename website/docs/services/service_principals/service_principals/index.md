--- 
title: service_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principals
  - service_principals
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

Creates, updates, deletes, gets or lists a <code>service_principals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_principals" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.service_principals.service_principals" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_2', value: 'get_2' },
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
<TabItem value="get_2">

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
    <td><a href="#parameter-appId"><code>appId</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of a servicePrincipal object. This API can be used to get agentIdentityBlueprintPrincipal objects as well by their ID.</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of a servicePrincipal object. This API can be used to get agentIdentityBlueprintPrincipal objects as well by their ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of servicePrincipal objects. This API also returns agentIdentityBlueprintPrincipal objects, which are identified by the @odata.type property of #microsoft.graph.agentIdentityBlueprintPrincipal.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new servicePrincipal object. This API can also create an agentIdentityBlueprintPrincipal object from an agentIdentityBlueprint when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprintPrincipal.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-appId"><code>appId</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new servicePrincipal object if it doesn't exist, or update the properties of an existing servicePrincipal object. This API can also create an agentIdentityBlueprintPrincipal object from an agentIdentityBlueprint if it doesn't exist, or update properties of an existing agentIdentityBlueprintPrincipal, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprintPrincipal.</td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new servicePrincipal object if it doesn't exist, or update the properties of an existing servicePrincipal object. This API can also create an agentIdentityBlueprintPrincipal object from an agentIdentityBlueprint if it doesn't exist, or update properties of an existing agentIdentityBlueprintPrincipal, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprintPrincipal.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-appId"><code>appId</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a servicePrincipal object. This API can also delete an agentIdentityBlueprintPrincipal object by its ID.</td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a servicePrincipal object. This API can also delete an agentIdentityBlueprintPrincipal object by its ID.</td>
</tr>
<tr>
    <td><a href="#get_available_extension_properties"><CopyableCode code="get_available_extension_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:</td>
</tr>
<tr>
    <td><a href="#get_by_ids"><CopyableCode code="get_by_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Return the directory objects specified in a list of IDs. Only a subset of user properties are returned by default in v1.0. Some common uses for this function are to:</td>
</tr>
<tr>
    <td><a href="#validate_properties"><CopyableCode code="validate_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Validate that a Microsoft 365 group's display name or mail nickname complies with naming policies. Clients can use this API to determine whether a display name or mail nickname is valid before trying to create a Microsoft 365 group. To validate the properties of an existing group, use the group: validateProperties function. The following policy validations are performed for the display name and mail nickname properties:<br />1. Validate the prefix and suffix naming policy<br />2. Validate the custom banned words policy<br />3. Validate that the mail nickname is unique This API only returns the first validation failure that is encountered. If the properties fail multiple validations, only the first validation failure is returned. However, you can validate both the mail nickname and the display name and receive a collection of validation errors if you're only validating the prefix and suffix naming policy. To learn more about configuring naming policies, see Configure naming policy.</td>
</tr>
<tr>
    <td><a href="#add_key"><CopyableCode code="add_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Adds a key credential to a servicePrincipal. This method along with removeKey can be used by a servicePrincipal to automate rolling its expiring keys. As part of the request validation for this method, a proof of possession of an existing key is verified before the action can be performed.  ServicePrincipals that don't have any existing valid certificates (i.e.: no certificates have been added yet, or all certificates have expired), won't be able to use this service action. Update servicePrincipal can be used to perform an update instead.</td>
</tr>
<tr>
    <td><a href="#add_password"><CopyableCode code="add_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Add a strong password or secret to a servicePrincipal object.</td>
</tr>
<tr>
    <td><a href="#add_token_signing_certificate"><CopyableCode code="add_token_signing_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Create a self-signed signing certificate and return a selfSignedCertificate object, which is the public part of the generated certificate.  The self-signed signing certificate is composed of the following objects, which are added to the servicePrincipal: <br />+ The keyCredentials object with the following objects:<br />    + A private key object with usage set to Sign.<br />    + A public key object with usage set to Verify.<br />+ The passwordCredentials object.  All the objects have the same value of customKeyIdentifier. The passwordCredential is used to open the PFX file (private key). It and the associated private key object have the same value of keyId. When set during creation through the displayName property, the subject of the certificate cannot be updated. The startDateTime is set to the same time the certificate is created using the action. The endDateTime can be up to three years after the certificate is created.</td>
</tr>
<tr>
    <td><a href="#check_member_groups"><CopyableCode code="check_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.</td>
</tr>
<tr>
    <td><a href="#check_member_objects"><CopyableCode code="check_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_member_groups"><CopyableCode code="get_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.</td>
</tr>
<tr>
    <td><a href="#get_member_objects"><CopyableCode code="get_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.</td>
</tr>
<tr>
    <td><a href="#remove_key"><CopyableCode code="remove_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Remove a key credential from a servicePrincipal. This method along with addKey can be used by a servicePrincipal to automate rolling its expiring keys. As part of the request validation for this method, a proof of possession of an existing key is verified before the action can be performed.</td>
</tr>
<tr>
    <td><a href="#remove_password"><CopyableCode code="remove_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Remove a password from a servicePrincipal object.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td></td>
    <td>Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.</td>
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
<tr id="parameter-appId">
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>Alternate key of servicePrincipal</td>
</tr>
<tr id="parameter-servicePrincipal-id">
    <td><CopyableCode code="servicePrincipal-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
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
<tr id="parameter-ConsistencyLevel">
    <td><CopyableCode code="ConsistencyLevel" /></td>
    <td><code>string</code></td>
    <td>Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries</td>
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
        { label: 'get_2', value: 'get_2' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieve the properties and relationships of a servicePrincipal object. This API can be used to get agentIdentityBlueprintPrincipal objects as well by their ID.

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
FROM entraid.service_principals.service_principals
WHERE appId = '{{ appId }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_2">

Retrieve the properties and relationships of a servicePrincipal object. This API can be used to get agentIdentityBlueprintPrincipal objects as well by their ID.

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
FROM entraid.service_principals.service_principals
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of servicePrincipal objects. This API also returns agentIdentityBlueprintPrincipal objects, which are identified by the @odata.type property of #microsoft.graph.agentIdentityBlueprintPrincipal.

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
FROM entraid.service_principals.service_principals
WHERE ConsistencyLevel = '{{ ConsistencyLevel }}'
AND $top = '{{ $top }}'
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

Create a new servicePrincipal object. This API can also create an agentIdentityBlueprintPrincipal object from an agentIdentityBlueprint when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprintPrincipal.

```sql
INSERT INTO entraid.service_principals.service_principals (
id,
@odata.type,
deletedDateTime,
accountEnabled,
addIns,
alternativeNames,
appDescription,
appDisplayName,
appId,
applicationTemplateId,
appOwnerOrganizationId,
appRoleAssignmentRequired,
appRoles,
createdByAppId,
customSecurityAttributes,
description,
disabledByMicrosoftStatus,
displayName,
homepage,
info,
isDisabled,
keyCredentials,
loginUrl,
logoutUrl,
notes,
notificationEmailAddresses,
oauth2PermissionScopes,
passwordCredentials,
preferredSingleSignOnMode,
preferredTokenSigningKeyThumbprint,
replyUrls,
resourceSpecificApplicationPermissions,
samlSingleSignOnSettings,
servicePrincipalNames,
servicePrincipalType,
signInAudience,
tags,
tokenEncryptionKeyId,
verifiedPublisher,
appManagementPolicies,
appRoleAssignedTo,
appRoleAssignments,
claimsMappingPolicies,
createdObjects,
delegatedPermissionClassifications,
endpoints,
federatedIdentityCredentials,
homeRealmDiscoveryPolicies,
memberOf,
oauth2PermissionGrants,
ownedObjects,
owners,
remoteDesktopSecurityConfiguration,
synchronization,
tokenIssuancePolicies,
tokenLifetimePolicies,
transitiveMemberOf
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
{{ accountEnabled }},
'{{ addIns }}',
'{{ alternativeNames }}',
'{{ appDescription }}',
'{{ appDisplayName }}',
'{{ appId }}',
'{{ applicationTemplateId }}',
'{{ appOwnerOrganizationId }}',
{{ appRoleAssignmentRequired }},
'{{ appRoles }}',
'{{ createdByAppId }}',
'{{ customSecurityAttributes }}',
'{{ description }}',
'{{ disabledByMicrosoftStatus }}',
'{{ displayName }}',
'{{ homepage }}',
'{{ info }}',
{{ isDisabled }},
'{{ keyCredentials }}',
'{{ loginUrl }}',
'{{ logoutUrl }}',
'{{ notes }}',
'{{ notificationEmailAddresses }}',
'{{ oauth2PermissionScopes }}',
'{{ passwordCredentials }}',
'{{ preferredSingleSignOnMode }}',
'{{ preferredTokenSigningKeyThumbprint }}',
'{{ replyUrls }}',
'{{ resourceSpecificApplicationPermissions }}',
'{{ samlSingleSignOnSettings }}',
'{{ servicePrincipalNames }}',
'{{ servicePrincipalType }}',
'{{ signInAudience }}',
'{{ tags }}',
'{{ tokenEncryptionKeyId }}',
'{{ verifiedPublisher }}',
'{{ appManagementPolicies }}',
'{{ appRoleAssignedTo }}',
'{{ appRoleAssignments }}',
'{{ claimsMappingPolicies }}',
'{{ createdObjects }}',
'{{ delegatedPermissionClassifications }}',
'{{ endpoints }}',
'{{ federatedIdentityCredentials }}',
'{{ homeRealmDiscoveryPolicies }}',
'{{ memberOf }}',
'{{ oauth2PermissionGrants }}',
'{{ ownedObjects }}',
'{{ owners }}',
'{{ remoteDesktopSecurityConfiguration }}',
'{{ synchronization }}',
'{{ tokenIssuancePolicies }}',
'{{ tokenLifetimePolicies }}',
'{{ transitiveMemberOf }}'
RETURNING
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
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: service_principals
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: accountEnabled
      value: {{ accountEnabled }}
      description: |
        true if the service principal account is enabled; otherwise, false. If set to false, then no users are able to sign in to this app, even if they're assigned to it. Supports $filter (eq, ne, not, in).
    - name: addIns
      description: |
        Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams may set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.
      value:
        - id: "{{ id }}"
          properties: "{{ properties }}"
          type: "{{ type }}"
          @odata.type: "{{ @odata.type }}"
    - name: alternativeNames
      value:
        - "{{ alternativeNames }}"
      description: |
        Used to retrieve service principals by subscription, identify resource group and full resource IDs for managed identities. Supports $filter (eq, not, ge, le, startsWith).
    - name: appDescription
      value: "{{ appDescription }}"
      description: |
        The description exposed by the associated application.
    - name: appDisplayName
      value: "{{ appDisplayName }}"
      description: |
        The display name exposed by the associated application. Maximum length is 256 characters.
    - name: appId
      value: "{{ appId }}"
      description: |
        The unique identifier for the associated application (its appId property). Alternate key. Supports $filter (eq, ne, not, in, startsWith).
    - name: applicationTemplateId
      value: "{{ applicationTemplateId }}"
      description: |
        Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the service principal wasn't created from an application template.
    - name: appOwnerOrganizationId
      value: "{{ appOwnerOrganizationId }}"
      description: |
        Contains the tenant ID where the application is registered. This is applicable only to service principals backed by applications. Supports $filter (eq, ne, NOT, ge, le).
    - name: appRoleAssignmentRequired
      value: {{ appRoleAssignmentRequired }}
      description: |
        Specifies whether users or other service principals need to be granted an app role assignment for this service principal before users can sign in or apps can get tokens. The default value is false. Not nullable. Supports $filter (eq, ne, NOT).
    - name: appRoles
      description: |
        The roles exposed by the application that's linked to this service principal. For more information, see the appRoles property definition on the application entity. Not nullable.
      value:
        - allowedMemberTypes: "{{ allowedMemberTypes }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          id: "{{ id }}"
          isEnabled: {{ isEnabled }}
          origin: "{{ origin }}"
          value: "{{ value }}"
          @odata.type: "{{ @odata.type }}"
    - name: createdByAppId
      value: "{{ createdByAppId }}"
      description: |
        The appId of the application that created this service principal. Set internally by Microsoft Entra ID. Read-only.
    - name: customSecurityAttributes
      value: "{{ customSecurityAttributes }}"
      description: |
        An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, startsWith). Filter value is case sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.
    - name: description
      value: "{{ description }}"
      description: |
        Free text field to provide an internal end-user facing description of the service principal. End-user portals such MyApps displays the application description in this field. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    - name: disabledByMicrosoftStatus
      value: "{{ disabledByMicrosoftStatus }}"
      description: |
        Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the service principal. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    - name: homepage
      value: "{{ homepage }}"
      description: |
        Home page or landing page of the application.
    - name: info
      value: "{{ info }}"
      description: |
        Basic profile information of the acquired application such as app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
    - name: isDisabled
      value: {{ isDisabled }}
    - name: keyCredentials
      description: |
        The collection of key credentials associated with the service principal. Not nullable. Supports $filter (eq, not, ge, le).
      value:
        - customKeyIdentifier: "{{ customKeyIdentifier }}"
          displayName: "{{ displayName }}"
          endDateTime: "{{ endDateTime }}"
          key: "{{ key }}"
          keyId: "{{ keyId }}"
          startDateTime: "{{ startDateTime }}"
          type: "{{ type }}"
          usage: "{{ usage }}"
          @odata.type: "{{ @odata.type }}"
    - name: loginUrl
      value: "{{ loginUrl }}"
      description: |
        Specifies the URL where the service provider redirects the user to Microsoft Entra ID to authenticate. Microsoft Entra ID uses the URL to launch the application from Microsoft 365 or the Microsoft Entra My Apps. When blank, Microsoft Entra ID performs IdP-initiated sign-on for applications configured with SAML-based single sign-on. The user launches the application from Microsoft 365, the Microsoft Entra My Apps, or the Microsoft Entra SSO URL.
    - name: logoutUrl
      value: "{{ logoutUrl }}"
      description: |
        Specifies the URL that the Microsoft's authorization service uses to sign out a user using OpenID Connect front-channel, back-channel, or SAML sign out protocols.
    - name: notes
      value: "{{ notes }}"
      description: |
        Free text field to capture information about the service principal, typically used for operational purposes. Maximum allowed size is 1,024 characters.
    - name: notificationEmailAddresses
      value:
        - "{{ notificationEmailAddresses }}"
      description: |
        Specifies the list of email addresses where Microsoft Entra ID sends a notification when the active certificate is near the expiration date. This is only for the certificates used to sign the SAML token issued for Microsoft Entra Gallery applications.
    - name: oauth2PermissionScopes
      description: |
        The delegated permissions exposed by the application. For more information, see the oauth2PermissionScopes property on the application entity's api property. Not nullable.
      value:
        - adminConsentDescription: "{{ adminConsentDescription }}"
          adminConsentDisplayName: "{{ adminConsentDisplayName }}"
          id: "{{ id }}"
          isEnabled: {{ isEnabled }}
          origin: "{{ origin }}"
          type: "{{ type }}"
          userConsentDescription: "{{ userConsentDescription }}"
          userConsentDisplayName: "{{ userConsentDisplayName }}"
          value: "{{ value }}"
          @odata.type: "{{ @odata.type }}"
    - name: passwordCredentials
      description: |
        The collection of password credentials associated with the application. Not nullable.
      value:
        - customKeyIdentifier: "{{ customKeyIdentifier }}"
          displayName: "{{ displayName }}"
          endDateTime: "{{ endDateTime }}"
          hint: "{{ hint }}"
          keyId: "{{ keyId }}"
          secretText: "{{ secretText }}"
          startDateTime: "{{ startDateTime }}"
          @odata.type: "{{ @odata.type }}"
    - name: preferredSingleSignOnMode
      value: "{{ preferredSingleSignOnMode }}"
      description: |
        Specifies the single sign-on mode configured for this application. Microsoft Entra ID uses the preferred single sign-on mode to launch the application from Microsoft 365 or the My Apps portal. The supported values are password, saml, notSupported, and oidc. Note: This field might be null for older SAML apps and for OIDC applications where it isn't set automatically.
    - name: preferredTokenSigningKeyThumbprint
      value: "{{ preferredTokenSigningKeyThumbprint }}"
      description: |
        This property can be used on SAML applications (apps that have preferredSingleSignOnMode set to saml) to control which certificate is used to sign the SAML responses. For applications that aren't SAML, don't write or otherwise rely on this property.
    - name: replyUrls
      value:
        - "{{ replyUrls }}"
      description: |
        The URLs that user tokens are sent to for sign in with the associated application, or the redirect URIs that OAuth 2.0 authorization codes and access tokens are sent to for the associated application. Not nullable.
    - name: resourceSpecificApplicationPermissions
      description: |
        The resource-specific application permissions exposed by this application. Currently, resource-specific permissions are only supported for Teams apps accessing to specific chats and teams using Microsoft Graph. Read-only.
      value:
        - description: "{{ description }}"
          displayName: "{{ displayName }}"
          id: "{{ id }}"
          isEnabled: {{ isEnabled }}
          value: "{{ value }}"
          @odata.type: "{{ @odata.type }}"
    - name: samlSingleSignOnSettings
      value: "{{ samlSingleSignOnSettings }}"
      description: |
        The collection for settings related to saml single sign-on.
    - name: servicePrincipalNames
      value:
        - "{{ servicePrincipalNames }}"
      description: |
        Contains the list of identifiersUris, copied over from the associated application. Additional values can be added to hybrid applications. These values can be used to identify the permissions exposed by this app within Microsoft Entra ID. For example,Client apps can specify a resource URI that is based on the values of this property to acquire an access token, which is the URI returned in the 'aud' claim.The any operator is required for filter expressions on multi-valued properties. Not nullable.  Supports $filter (eq, not, ge, le, startsWith).
    - name: servicePrincipalType
      value: "{{ servicePrincipalType }}"
      description: |
        Identifies whether the service principal represents an application, a managed identity, or a legacy application. This property is set by Microsoft Entra ID internally. The servicePrincipalType property can be set to three different values: Application - A service principal that represents an application or service. The appId property identifies the associated app registration, and matches the appId of an application, possibly from a different tenant. If the associated app registration is missing, tokens aren't issued for the service principal.ManagedIdentity - A service principal that represents a managed identity. Service principals representing managed identities can be granted access and permissions, but can't be updated or modified directly.Legacy - A service principal that represents an app created before app registrations, or through legacy experiences. A legacy service principal can have credentials, service principal names, reply URLs, and other properties that are editable by an authorized user, but doesn't have an associated app registration. The appId value doesn't associate the service principal with an app registration. The service principal can only be used in the tenant where it was created.ServiceIdentity - A service principal that represents an agent identity.SocialIdp - For internal use.
    - name: signInAudience
      value: "{{ signInAudience }}"
      description: |
        Specifies the Microsoft accounts that are supported for the current application. Read-only. Supported values are:AzureADMyOrg: Users with a Microsoft work or school account in my organization's Microsoft Entra tenant (single-tenant).AzureADMultipleOrgs: Users with a Microsoft work or school account in any organization's Microsoft Entra tenant (multitenant).AzureADandPersonalMicrosoftAccount: Users with a personal Microsoft account, or a work or school account in any organization's Microsoft Entra tenant.PersonalMicrosoftAccount: Users with a personal Microsoft account only.
    - name: tags
      value:
        - "{{ tags }}"
      description: |
        Custom strings that can be used to categorize and identify the service principal. Not nullable. The value is the union of strings set here and on the associated application entity's tags property.Supports $filter (eq, not, ge, le, startsWith).
    - name: tokenEncryptionKeyId
      value: "{{ tokenEncryptionKeyId }}"
      description: |
        Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID issues tokens for this application encrypted using the key specified by this property. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
    - name: verifiedPublisher
      value: "{{ verifiedPublisher }}"
      description: |
        Specifies the verified publisher of the application that's linked to this service principal.
    - name: appManagementPolicies
      description: |
        The appManagementPolicy applied to this application.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          isEnabled: {{ isEnabled }}
          restrictions: "{{ restrictions }}"
          appliesTo: "{{ appliesTo }}"
    - name: appRoleAssignedTo
      description: |
        App role assignments for this app or service, granted to users, groups, and other service principals. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          appRoleId: "{{ appRoleId }}"
          createdDateTime: "{{ createdDateTime }}"
          principalDisplayName: "{{ principalDisplayName }}"
          principalId: "{{ principalId }}"
          principalType: "{{ principalType }}"
          resourceDisplayName: "{{ resourceDisplayName }}"
          resourceId: "{{ resourceId }}"
    - name: appRoleAssignments
      description: |
        App role assignment for another app or service, granted to this service principal. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          appRoleId: "{{ appRoleId }}"
          createdDateTime: "{{ createdDateTime }}"
          principalDisplayName: "{{ principalDisplayName }}"
          principalId: "{{ principalId }}"
          principalType: "{{ principalType }}"
          resourceDisplayName: "{{ resourceDisplayName }}"
          resourceId: "{{ resourceId }}"
    - name: claimsMappingPolicies
      description: |
        The claimsMappingPolicies assigned to this service principal. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          definition: "{{ definition }}"
          isOrganizationDefault: {{ isOrganizationDefault }}
          appliesTo: "{{ appliesTo }}"
    - name: createdObjects
      description: |
        Directory objects created by this service principal. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: delegatedPermissionClassifications
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          classification: "{{ classification }}"
          permissionId: "{{ permissionId }}"
          permissionName: "{{ permissionName }}"
    - name: endpoints
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          capability: "{{ capability }}"
          providerId: "{{ providerId }}"
          providerName: "{{ providerName }}"
          providerResourceId: "{{ providerResourceId }}"
          uri: "{{ uri }}"
    - name: federatedIdentityCredentials
      description: |
        Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          audiences: "{{ audiences }}"
          description: "{{ description }}"
          issuer: "{{ issuer }}"
          name: "{{ name }}"
          subject: "{{ subject }}"
    - name: homeRealmDiscoveryPolicies
      description: |
        The homeRealmDiscoveryPolicies assigned to this service principal. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          definition: "{{ definition }}"
          isOrganizationDefault: {{ isOrganizationDefault }}
          appliesTo: "{{ appliesTo }}"
    - name: memberOf
      description: |
        Roles that this service principal is a member of. HTTP Methods: GET Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: oauth2PermissionGrants
      description: |
        Delegated permission grants authorizing this service principal to access an API on behalf of a signed-in user. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          clientId: "{{ clientId }}"
          consentType: "{{ consentType }}"
          principalId: "{{ principalId }}"
          resourceId: "{{ resourceId }}"
          scope: "{{ scope }}"
    - name: ownedObjects
      description: |
        Directory objects that this service principal owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: owners
      description: |
        Directory objects that are owners of this servicePrincipal. The owners are a set of nonadmin users or servicePrincipals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: remoteDesktopSecurityConfiguration
      value: "{{ remoteDesktopSecurityConfiguration }}"
      description: |
        The remoteDesktopSecurityConfiguration object applied to this service principal. Supports $filter (eq) for isRemoteDesktopProtocolEnabled property.
    - name: synchronization
      value: "{{ synchronization }}"
      description: |
        Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.
    - name: tokenIssuancePolicies
      description: |
        The tokenIssuancePolicies assigned to this service principal.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          definition: "{{ definition }}"
          isOrganizationDefault: {{ isOrganizationDefault }}
          appliesTo: "{{ appliesTo }}"
    - name: tokenLifetimePolicies
      description: |
        The tokenLifetimePolicies assigned to this service principal.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          definition: "{{ definition }}"
          isOrganizationDefault: {{ isOrganizationDefault }}
          appliesTo: "{{ appliesTo }}"
    - name: transitiveMemberOf
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'update_2', value: 'update_2' }
    ]}
>
<TabItem value="update">

Create a new servicePrincipal object if it doesn't exist, or update the properties of an existing servicePrincipal object. This API can also create an agentIdentityBlueprintPrincipal object from an agentIdentityBlueprint if it doesn't exist, or update properties of an existing agentIdentityBlueprintPrincipal, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprintPrincipal.

```sql
UPDATE entraid.service_principals.service_principals
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
accountEnabled = {{ accountEnabled }},
addIns = '{{ addIns }}',
alternativeNames = '{{ alternativeNames }}',
appDescription = '{{ appDescription }}',
appDisplayName = '{{ appDisplayName }}',
appId = '{{ appId }}',
applicationTemplateId = '{{ applicationTemplateId }}',
appOwnerOrganizationId = '{{ appOwnerOrganizationId }}',
appRoleAssignmentRequired = {{ appRoleAssignmentRequired }},
appRoles = '{{ appRoles }}',
createdByAppId = '{{ createdByAppId }}',
customSecurityAttributes = '{{ customSecurityAttributes }}',
description = '{{ description }}',
disabledByMicrosoftStatus = '{{ disabledByMicrosoftStatus }}',
displayName = '{{ displayName }}',
homepage = '{{ homepage }}',
info = '{{ info }}',
isDisabled = {{ isDisabled }},
keyCredentials = '{{ keyCredentials }}',
loginUrl = '{{ loginUrl }}',
logoutUrl = '{{ logoutUrl }}',
notes = '{{ notes }}',
notificationEmailAddresses = '{{ notificationEmailAddresses }}',
oauth2PermissionScopes = '{{ oauth2PermissionScopes }}',
passwordCredentials = '{{ passwordCredentials }}',
preferredSingleSignOnMode = '{{ preferredSingleSignOnMode }}',
preferredTokenSigningKeyThumbprint = '{{ preferredTokenSigningKeyThumbprint }}',
replyUrls = '{{ replyUrls }}',
resourceSpecificApplicationPermissions = '{{ resourceSpecificApplicationPermissions }}',
samlSingleSignOnSettings = '{{ samlSingleSignOnSettings }}',
servicePrincipalNames = '{{ servicePrincipalNames }}',
servicePrincipalType = '{{ servicePrincipalType }}',
signInAudience = '{{ signInAudience }}',
tags = '{{ tags }}',
tokenEncryptionKeyId = '{{ tokenEncryptionKeyId }}',
verifiedPublisher = '{{ verifiedPublisher }}',
appManagementPolicies = '{{ appManagementPolicies }}',
appRoleAssignedTo = '{{ appRoleAssignedTo }}',
appRoleAssignments = '{{ appRoleAssignments }}',
claimsMappingPolicies = '{{ claimsMappingPolicies }}',
createdObjects = '{{ createdObjects }}',
delegatedPermissionClassifications = '{{ delegatedPermissionClassifications }}',
endpoints = '{{ endpoints }}',
federatedIdentityCredentials = '{{ federatedIdentityCredentials }}',
homeRealmDiscoveryPolicies = '{{ homeRealmDiscoveryPolicies }}',
memberOf = '{{ memberOf }}',
oauth2PermissionGrants = '{{ oauth2PermissionGrants }}',
ownedObjects = '{{ ownedObjects }}',
owners = '{{ owners }}',
remoteDesktopSecurityConfiguration = '{{ remoteDesktopSecurityConfiguration }}',
synchronization = '{{ synchronization }}',
tokenIssuancePolicies = '{{ tokenIssuancePolicies }}',
tokenLifetimePolicies = '{{ tokenLifetimePolicies }}',
transitiveMemberOf = '{{ transitiveMemberOf }}'
WHERE 
appId = '{{ appId }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
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
verifiedPublisher;
```
</TabItem>
<TabItem value="update_2">

Create a new servicePrincipal object if it doesn't exist, or update the properties of an existing servicePrincipal object. This API can also create an agentIdentityBlueprintPrincipal object from an agentIdentityBlueprint if it doesn't exist, or update properties of an existing agentIdentityBlueprintPrincipal, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprintPrincipal.

```sql
UPDATE entraid.service_principals.service_principals
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
accountEnabled = {{ accountEnabled }},
addIns = '{{ addIns }}',
alternativeNames = '{{ alternativeNames }}',
appDescription = '{{ appDescription }}',
appDisplayName = '{{ appDisplayName }}',
appId = '{{ appId }}',
applicationTemplateId = '{{ applicationTemplateId }}',
appOwnerOrganizationId = '{{ appOwnerOrganizationId }}',
appRoleAssignmentRequired = {{ appRoleAssignmentRequired }},
appRoles = '{{ appRoles }}',
createdByAppId = '{{ createdByAppId }}',
customSecurityAttributes = '{{ customSecurityAttributes }}',
description = '{{ description }}',
disabledByMicrosoftStatus = '{{ disabledByMicrosoftStatus }}',
displayName = '{{ displayName }}',
homepage = '{{ homepage }}',
info = '{{ info }}',
isDisabled = {{ isDisabled }},
keyCredentials = '{{ keyCredentials }}',
loginUrl = '{{ loginUrl }}',
logoutUrl = '{{ logoutUrl }}',
notes = '{{ notes }}',
notificationEmailAddresses = '{{ notificationEmailAddresses }}',
oauth2PermissionScopes = '{{ oauth2PermissionScopes }}',
passwordCredentials = '{{ passwordCredentials }}',
preferredSingleSignOnMode = '{{ preferredSingleSignOnMode }}',
preferredTokenSigningKeyThumbprint = '{{ preferredTokenSigningKeyThumbprint }}',
replyUrls = '{{ replyUrls }}',
resourceSpecificApplicationPermissions = '{{ resourceSpecificApplicationPermissions }}',
samlSingleSignOnSettings = '{{ samlSingleSignOnSettings }}',
servicePrincipalNames = '{{ servicePrincipalNames }}',
servicePrincipalType = '{{ servicePrincipalType }}',
signInAudience = '{{ signInAudience }}',
tags = '{{ tags }}',
tokenEncryptionKeyId = '{{ tokenEncryptionKeyId }}',
verifiedPublisher = '{{ verifiedPublisher }}',
appManagementPolicies = '{{ appManagementPolicies }}',
appRoleAssignedTo = '{{ appRoleAssignedTo }}',
appRoleAssignments = '{{ appRoleAssignments }}',
claimsMappingPolicies = '{{ claimsMappingPolicies }}',
createdObjects = '{{ createdObjects }}',
delegatedPermissionClassifications = '{{ delegatedPermissionClassifications }}',
endpoints = '{{ endpoints }}',
federatedIdentityCredentials = '{{ federatedIdentityCredentials }}',
homeRealmDiscoveryPolicies = '{{ homeRealmDiscoveryPolicies }}',
memberOf = '{{ memberOf }}',
oauth2PermissionGrants = '{{ oauth2PermissionGrants }}',
ownedObjects = '{{ ownedObjects }}',
owners = '{{ owners }}',
remoteDesktopSecurityConfiguration = '{{ remoteDesktopSecurityConfiguration }}',
synchronization = '{{ synchronization }}',
tokenIssuancePolicies = '{{ tokenIssuancePolicies }}',
tokenLifetimePolicies = '{{ tokenLifetimePolicies }}',
transitiveMemberOf = '{{ transitiveMemberOf }}'
WHERE 
servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
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
verifiedPublisher;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_2', value: 'delete_2' }
    ]}
>
<TabItem value="delete">

Delete a servicePrincipal object. This API can also delete an agentIdentityBlueprintPrincipal object by its ID.

```sql
DELETE FROM entraid.service_principals.service_principals
WHERE appId = '{{ appId }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

Delete a servicePrincipal object. This API can also delete an agentIdentityBlueprintPrincipal object by its ID.

```sql
DELETE FROM entraid.service_principals.service_principals
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_available_extension_properties"
    values={[
        { label: 'get_available_extension_properties', value: 'get_available_extension_properties' },
        { label: 'get_by_ids', value: 'get_by_ids' },
        { label: 'validate_properties', value: 'validate_properties' },
        { label: 'add_key', value: 'add_key' },
        { label: 'add_password', value: 'add_password' },
        { label: 'add_token_signing_certificate', value: 'add_token_signing_certificate' },
        { label: 'check_member_groups', value: 'check_member_groups' },
        { label: 'check_member_objects', value: 'check_member_objects' },
        { label: 'get_member_groups', value: 'get_member_groups' },
        { label: 'get_member_objects', value: 'get_member_objects' },
        { label: 'remove_key', value: 'remove_key' },
        { label: 'remove_password', value: 'remove_password' },
        { label: 'restore', value: 'restore' }
    ]}
>
<TabItem value="get_available_extension_properties">

Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:

```sql
EXEC entraid.service_principals.service_principals.get_available_extension_properties 
@@json=
'{
"isSyncedFromOnPremises": {{ isSyncedFromOnPremises }}
}'
;
```
</TabItem>
<TabItem value="get_by_ids">

Return the directory objects specified in a list of IDs. Only a subset of user properties are returned by default in v1.0. Some common uses for this function are to:

```sql
EXEC entraid.service_principals.service_principals.get_by_ids 
@@json=
'{
"ids": "{{ ids }}", 
"types": "{{ types }}"
}'
;
```
</TabItem>
<TabItem value="validate_properties">

Validate that a Microsoft 365 group's display name or mail nickname complies with naming policies. Clients can use this API to determine whether a display name or mail nickname is valid before trying to create a Microsoft 365 group. To validate the properties of an existing group, use the group: validateProperties function. The following policy validations are performed for the display name and mail nickname properties:<br />1. Validate the prefix and suffix naming policy<br />2. Validate the custom banned words policy<br />3. Validate that the mail nickname is unique This API only returns the first validation failure that is encountered. If the properties fail multiple validations, only the first validation failure is returned. However, you can validate both the mail nickname and the display name and receive a collection of validation errors if you're only validating the prefix and suffix naming policy. To learn more about configuring naming policies, see Configure naming policy.

```sql
EXEC entraid.service_principals.service_principals.validate_properties 
@@json=
'{
"entityType": "{{ entityType }}", 
"displayName": "{{ displayName }}", 
"mailNickname": "{{ mailNickname }}", 
"onBehalfOfUserId": "{{ onBehalfOfUserId }}"
}'
;
```
</TabItem>
<TabItem value="add_key">

Adds a key credential to a servicePrincipal. This method along with removeKey can be used by a servicePrincipal to automate rolling its expiring keys. As part of the request validation for this method, a proof of possession of an existing key is verified before the action can be performed.  ServicePrincipals that don't have any existing valid certificates (i.e.: no certificates have been added yet, or all certificates have expired), won't be able to use this service action. Update servicePrincipal can be used to perform an update instead.

```sql
EXEC entraid.service_principals.service_principals.add_key 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"keyCredential": "{{ keyCredential }}", 
"passwordCredential": "{{ passwordCredential }}", 
"proof": "{{ proof }}"
}'
;
```
</TabItem>
<TabItem value="add_password">

Add a strong password or secret to a servicePrincipal object.

```sql
EXEC entraid.service_principals.service_principals.add_password 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"passwordCredential": "{{ passwordCredential }}"
}'
;
```
</TabItem>
<TabItem value="add_token_signing_certificate">

Create a self-signed signing certificate and return a selfSignedCertificate object, which is the public part of the generated certificate.  The self-signed signing certificate is composed of the following objects, which are added to the servicePrincipal: <br />+ The keyCredentials object with the following objects:<br />    + A private key object with usage set to Sign.<br />    + A public key object with usage set to Verify.<br />+ The passwordCredentials object.  All the objects have the same value of customKeyIdentifier. The passwordCredential is used to open the PFX file (private key). It and the associated private key object have the same value of keyId. When set during creation through the displayName property, the subject of the certificate cannot be updated. The startDateTime is set to the same time the certificate is created using the action. The endDateTime can be up to three years after the certificate is created.

```sql
EXEC entraid.service_principals.service_principals.add_token_signing_certificate 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"displayName": "{{ displayName }}", 
"endDateTime": "{{ endDateTime }}"
}'
;
```
</TabItem>
<TabItem value="check_member_groups">

Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.

```sql
EXEC entraid.service_principals.service_principals.check_member_groups 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"groupIds": "{{ groupIds }}"
}'
;
```
</TabItem>
<TabItem value="check_member_objects">

Success

```sql
EXEC entraid.service_principals.service_principals.check_member_objects 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="get_member_groups">

Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.

```sql
EXEC entraid.service_principals.service_principals.get_member_groups 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"securityEnabledOnly": {{ securityEnabledOnly }}
}'
;
```
</TabItem>
<TabItem value="get_member_objects">

Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.

```sql
EXEC entraid.service_principals.service_principals.get_member_objects 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"securityEnabledOnly": {{ securityEnabledOnly }}
}'
;
```
</TabItem>
<TabItem value="remove_key">

Remove a key credential from a servicePrincipal. This method along with addKey can be used by a servicePrincipal to automate rolling its expiring keys. As part of the request validation for this method, a proof of possession of an existing key is verified before the action can be performed.

```sql
EXEC entraid.service_principals.service_principals.remove_key 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"keyId": "{{ keyId }}", 
"proof": "{{ proof }}"
}'
;
```
</TabItem>
<TabItem value="remove_password">

Remove a password from a servicePrincipal object.

```sql
EXEC entraid.service_principals.service_principals.remove_password 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"keyId": "{{ keyId }}"
}'
;
```
</TabItem>
<TabItem value="restore">

Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.

```sql
EXEC entraid.service_principals.service_principals.restore 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required
;
```
</TabItem>
</Tabs>
