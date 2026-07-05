--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - applications
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

Creates, updates, deletes, gets or lists an <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.applications.applications" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_2', value: 'get_2' },
        { label: 'get_3', value: 'get_3' },
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
    <td><CopyableCode code="addIns" /></td>
    <td><code>array</code></td>
    <td>Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams can set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.</td>
</tr>
<tr>
    <td><CopyableCode code="api" /></td>
    <td><code></code></td>
    <td>Specifies settings for an application that implements a web API.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the application that is assigned to an application by Microsoft Entra ID. Not nullable. Read-only. Alternate key. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="appManagementPolicies" /></td>
    <td><code>array</code></td>
    <td>The appManagementPolicy applied to this application.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoles" /></td>
    <td><code>array</code></td>
    <td>The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTemplateId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the app wasn't created from an application template.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationBehaviors" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="certification" /></td>
    <td><code></code></td>
    <td>Specifies the certification status of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByAppId" /></td>
    <td><code>string</code></td>
    <td>The appId of the application that created this application. Set internally by Microsoft Entra ID. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOnBehalfOf" /></td>
    <td><code></code></td>
    <td>Supports $filter (/$count eq 0, /$count ne 0). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultRedirectUri" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Free text field to provide a description of the application object to end users. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledByMicrosoftStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the application. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionProperties" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="federatedIdentityCredentials" /></td>
    <td><code>array</code></td>
    <td>Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="groupMembershipClaims" /></td>
    <td><code>string</code></td>
    <td>Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Microsoft Entra roles), All (this gets all of the security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of).</td>
</tr>
<tr>
    <td><CopyableCode code="homeRealmDiscoveryPolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="identifierUris" /></td>
    <td><code>array</code></td>
    <td>Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. For more information on valid identifierUris patterns and best practices, see Microsoft Entra application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="info" /></td>
    <td><code></code></td>
    <td>Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="isDeviceOnlyAuthSupported" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this application supports device authentication without a user. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isFallbackPublicClient" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false, which means the fallback application type is confidential client such as a web app. There are certain scenarios where Microsoft Entra ID can't determine the client application type. For example, the ROPC flow where it's configured without specifying a redirect URI. In those cases, Microsoft Entra ID interprets the application type based on the value of this property.</td>
</tr>
<tr>
    <td><CopyableCode code="keyCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="logo" /></td>
    <td><code>string (base64url)</code></td>
    <td>The main logo for the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="managerApplications" /></td>
    <td><code>array</code></td>
    <td>A collection of application IDs for Microsoft first-party applications designated as managers. Manager applications can create service principals, agent identities, and agent users for managed agent blueprints. Limited to a maximum of 10 entries. Not nullable. Only supported on agentIdentityBlueprint objects; attempts to set this property on non-agent-blueprint applications return an error. Not returned by default; must be explicitly requested via $select.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeAuthenticationApisEnabled" /></td>
    <td><code></code></td>
    <td>Specifies whether the Native Authentication APIs are enabled for the application. The possible values are: none and all. Default is none. For more information, see Native Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes relevant for the management of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2RequirePostResponse" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="optionalClaims" /></td>
    <td><code></code></td>
    <td>Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>Directory objects that are owners of this application. The owners are a set of nonadmin users or service principals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="parentalControlSettings" /></td>
    <td><code></code></td>
    <td>Specifies parental control settings for an application.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of password credentials associated with the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="publicClient" /></td>
    <td><code></code></td>
    <td>Specifies settings for installed clients such as desktop or mobile devices.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDomain" /></td>
    <td><code>string</code></td>
    <td>The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="requestSignatureVerification" /></td>
    <td><code></code></td>
    <td>Specifies whether this application requires Microsoft Entra ID to verify the signed authentication requests.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredResourceAccess" /></td>
    <td><code>array</code></td>
    <td>Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="samlMetadataUrl" /></td>
    <td><code>string</code></td>
    <td>The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceManagementReference" /></td>
    <td><code>string</code></td>
    <td>References application or service contact information from a Service or Asset Management database. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalLockConfiguration" /></td>
    <td><code></code></td>
    <td>Specifies whether sensitive properties of a multitenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.</td>
</tr>
<tr>
    <td><CopyableCode code="signInAudience" /></td>
    <td><code>string</code></td>
    <td>Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg (default), AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount, and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you might need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="spa" /></td>
    <td><code></code></td>
    <td>Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.</td>
</tr>
<tr>
    <td><CopyableCode code="synchronization" /></td>
    <td><code></code></td>
    <td>Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenEncryptionKeyId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuancePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokenLifetimePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>The unique identifier that can be assigned to an application and used as an alternate key. Immutable. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedPublisher" /></td>
    <td><code></code></td>
    <td>Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.</td>
</tr>
<tr>
    <td><CopyableCode code="web" /></td>
    <td><code></code></td>
    <td>Specifies settings for a web application.</td>
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
    <td><CopyableCode code="addIns" /></td>
    <td><code>array</code></td>
    <td>Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams can set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.</td>
</tr>
<tr>
    <td><CopyableCode code="api" /></td>
    <td><code></code></td>
    <td>Specifies settings for an application that implements a web API.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the application that is assigned to an application by Microsoft Entra ID. Not nullable. Read-only. Alternate key. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="appManagementPolicies" /></td>
    <td><code>array</code></td>
    <td>The appManagementPolicy applied to this application.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoles" /></td>
    <td><code>array</code></td>
    <td>The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTemplateId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the app wasn't created from an application template.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationBehaviors" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="certification" /></td>
    <td><code></code></td>
    <td>Specifies the certification status of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByAppId" /></td>
    <td><code>string</code></td>
    <td>The appId of the application that created this application. Set internally by Microsoft Entra ID. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOnBehalfOf" /></td>
    <td><code></code></td>
    <td>Supports $filter (/$count eq 0, /$count ne 0). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultRedirectUri" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Free text field to provide a description of the application object to end users. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledByMicrosoftStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the application. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionProperties" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="federatedIdentityCredentials" /></td>
    <td><code>array</code></td>
    <td>Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="groupMembershipClaims" /></td>
    <td><code>string</code></td>
    <td>Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Microsoft Entra roles), All (this gets all of the security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of).</td>
</tr>
<tr>
    <td><CopyableCode code="homeRealmDiscoveryPolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="identifierUris" /></td>
    <td><code>array</code></td>
    <td>Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. For more information on valid identifierUris patterns and best practices, see Microsoft Entra application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="info" /></td>
    <td><code></code></td>
    <td>Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="isDeviceOnlyAuthSupported" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this application supports device authentication without a user. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isFallbackPublicClient" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false, which means the fallback application type is confidential client such as a web app. There are certain scenarios where Microsoft Entra ID can't determine the client application type. For example, the ROPC flow where it's configured without specifying a redirect URI. In those cases, Microsoft Entra ID interprets the application type based on the value of this property.</td>
</tr>
<tr>
    <td><CopyableCode code="keyCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="logo" /></td>
    <td><code>string (base64url)</code></td>
    <td>The main logo for the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="managerApplications" /></td>
    <td><code>array</code></td>
    <td>A collection of application IDs for Microsoft first-party applications designated as managers. Manager applications can create service principals, agent identities, and agent users for managed agent blueprints. Limited to a maximum of 10 entries. Not nullable. Only supported on agentIdentityBlueprint objects; attempts to set this property on non-agent-blueprint applications return an error. Not returned by default; must be explicitly requested via $select.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeAuthenticationApisEnabled" /></td>
    <td><code></code></td>
    <td>Specifies whether the Native Authentication APIs are enabled for the application. The possible values are: none and all. Default is none. For more information, see Native Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes relevant for the management of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2RequirePostResponse" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="optionalClaims" /></td>
    <td><code></code></td>
    <td>Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>Directory objects that are owners of this application. The owners are a set of nonadmin users or service principals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="parentalControlSettings" /></td>
    <td><code></code></td>
    <td>Specifies parental control settings for an application.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of password credentials associated with the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="publicClient" /></td>
    <td><code></code></td>
    <td>Specifies settings for installed clients such as desktop or mobile devices.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDomain" /></td>
    <td><code>string</code></td>
    <td>The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="requestSignatureVerification" /></td>
    <td><code></code></td>
    <td>Specifies whether this application requires Microsoft Entra ID to verify the signed authentication requests.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredResourceAccess" /></td>
    <td><code>array</code></td>
    <td>Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="samlMetadataUrl" /></td>
    <td><code>string</code></td>
    <td>The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceManagementReference" /></td>
    <td><code>string</code></td>
    <td>References application or service contact information from a Service or Asset Management database. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalLockConfiguration" /></td>
    <td><code></code></td>
    <td>Specifies whether sensitive properties of a multitenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.</td>
</tr>
<tr>
    <td><CopyableCode code="signInAudience" /></td>
    <td><code>string</code></td>
    <td>Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg (default), AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount, and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you might need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="spa" /></td>
    <td><code></code></td>
    <td>Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.</td>
</tr>
<tr>
    <td><CopyableCode code="synchronization" /></td>
    <td><code></code></td>
    <td>Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenEncryptionKeyId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuancePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokenLifetimePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>The unique identifier that can be assigned to an application and used as an alternate key. Immutable. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedPublisher" /></td>
    <td><code></code></td>
    <td>Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.</td>
</tr>
<tr>
    <td><CopyableCode code="web" /></td>
    <td><code></code></td>
    <td>Specifies settings for a web application.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_3">

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
    <td><CopyableCode code="addIns" /></td>
    <td><code>array</code></td>
    <td>Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams can set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.</td>
</tr>
<tr>
    <td><CopyableCode code="api" /></td>
    <td><code></code></td>
    <td>Specifies settings for an application that implements a web API.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the application that is assigned to an application by Microsoft Entra ID. Not nullable. Read-only. Alternate key. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="appManagementPolicies" /></td>
    <td><code>array</code></td>
    <td>The appManagementPolicy applied to this application.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoles" /></td>
    <td><code>array</code></td>
    <td>The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTemplateId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the app wasn't created from an application template.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationBehaviors" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="certification" /></td>
    <td><code></code></td>
    <td>Specifies the certification status of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByAppId" /></td>
    <td><code>string</code></td>
    <td>The appId of the application that created this application. Set internally by Microsoft Entra ID. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOnBehalfOf" /></td>
    <td><code></code></td>
    <td>Supports $filter (/$count eq 0, /$count ne 0). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultRedirectUri" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Free text field to provide a description of the application object to end users. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledByMicrosoftStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the application. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionProperties" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="federatedIdentityCredentials" /></td>
    <td><code>array</code></td>
    <td>Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="groupMembershipClaims" /></td>
    <td><code>string</code></td>
    <td>Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Microsoft Entra roles), All (this gets all of the security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of).</td>
</tr>
<tr>
    <td><CopyableCode code="homeRealmDiscoveryPolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="identifierUris" /></td>
    <td><code>array</code></td>
    <td>Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. For more information on valid identifierUris patterns and best practices, see Microsoft Entra application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="info" /></td>
    <td><code></code></td>
    <td>Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="isDeviceOnlyAuthSupported" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this application supports device authentication without a user. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isFallbackPublicClient" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false, which means the fallback application type is confidential client such as a web app. There are certain scenarios where Microsoft Entra ID can't determine the client application type. For example, the ROPC flow where it's configured without specifying a redirect URI. In those cases, Microsoft Entra ID interprets the application type based on the value of this property.</td>
</tr>
<tr>
    <td><CopyableCode code="keyCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="logo" /></td>
    <td><code>string (base64url)</code></td>
    <td>The main logo for the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="managerApplications" /></td>
    <td><code>array</code></td>
    <td>A collection of application IDs for Microsoft first-party applications designated as managers. Manager applications can create service principals, agent identities, and agent users for managed agent blueprints. Limited to a maximum of 10 entries. Not nullable. Only supported on agentIdentityBlueprint objects; attempts to set this property on non-agent-blueprint applications return an error. Not returned by default; must be explicitly requested via $select.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeAuthenticationApisEnabled" /></td>
    <td><code></code></td>
    <td>Specifies whether the Native Authentication APIs are enabled for the application. The possible values are: none and all. Default is none. For more information, see Native Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes relevant for the management of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2RequirePostResponse" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="optionalClaims" /></td>
    <td><code></code></td>
    <td>Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>Directory objects that are owners of this application. The owners are a set of nonadmin users or service principals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="parentalControlSettings" /></td>
    <td><code></code></td>
    <td>Specifies parental control settings for an application.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of password credentials associated with the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="publicClient" /></td>
    <td><code></code></td>
    <td>Specifies settings for installed clients such as desktop or mobile devices.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDomain" /></td>
    <td><code>string</code></td>
    <td>The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="requestSignatureVerification" /></td>
    <td><code></code></td>
    <td>Specifies whether this application requires Microsoft Entra ID to verify the signed authentication requests.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredResourceAccess" /></td>
    <td><code>array</code></td>
    <td>Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="samlMetadataUrl" /></td>
    <td><code>string</code></td>
    <td>The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceManagementReference" /></td>
    <td><code>string</code></td>
    <td>References application or service contact information from a Service or Asset Management database. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalLockConfiguration" /></td>
    <td><code></code></td>
    <td>Specifies whether sensitive properties of a multitenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.</td>
</tr>
<tr>
    <td><CopyableCode code="signInAudience" /></td>
    <td><code>string</code></td>
    <td>Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg (default), AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount, and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you might need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="spa" /></td>
    <td><code></code></td>
    <td>Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.</td>
</tr>
<tr>
    <td><CopyableCode code="synchronization" /></td>
    <td><code></code></td>
    <td>Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenEncryptionKeyId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuancePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokenLifetimePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>The unique identifier that can be assigned to an application and used as an alternate key. Immutable. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedPublisher" /></td>
    <td><code></code></td>
    <td>Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.</td>
</tr>
<tr>
    <td><CopyableCode code="web" /></td>
    <td><code></code></td>
    <td>Specifies settings for a web application.</td>
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
    <td><CopyableCode code="addIns" /></td>
    <td><code>array</code></td>
    <td>Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams can set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.</td>
</tr>
<tr>
    <td><CopyableCode code="api" /></td>
    <td><code></code></td>
    <td>Specifies settings for an application that implements a web API.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the application that is assigned to an application by Microsoft Entra ID. Not nullable. Read-only. Alternate key. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="appManagementPolicies" /></td>
    <td><code>array</code></td>
    <td>The appManagementPolicy applied to this application.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoles" /></td>
    <td><code>array</code></td>
    <td>The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationTemplateId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the app wasn't created from an application template.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationBehaviors" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="certification" /></td>
    <td><code></code></td>
    <td>Specifies the certification status of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByAppId" /></td>
    <td><code>string</code></td>
    <td>The appId of the application that created this application. Set internally by Microsoft Entra ID. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOnBehalfOf" /></td>
    <td><code></code></td>
    <td>Supports $filter (/$count eq 0, /$count ne 0). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultRedirectUri" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Free text field to provide a description of the application object to end users. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledByMicrosoftStatus" /></td>
    <td><code>string</code></td>
    <td>Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the application. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionProperties" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="federatedIdentityCredentials" /></td>
    <td><code>array</code></td>
    <td>Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="groupMembershipClaims" /></td>
    <td><code>string</code></td>
    <td>Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Microsoft Entra roles), All (this gets all of the security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of).</td>
</tr>
<tr>
    <td><CopyableCode code="homeRealmDiscoveryPolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="identifierUris" /></td>
    <td><code>array</code></td>
    <td>Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. For more information on valid identifierUris patterns and best practices, see Microsoft Entra application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="info" /></td>
    <td><code></code></td>
    <td>Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="isDeviceOnlyAuthSupported" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether this application supports device authentication without a user. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isFallbackPublicClient" /></td>
    <td><code>boolean</code></td>
    <td>Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false, which means the fallback application type is confidential client such as a web app. There are certain scenarios where Microsoft Entra ID can't determine the client application type. For example, the ROPC flow where it's configured without specifying a redirect URI. In those cases, Microsoft Entra ID interprets the application type based on the value of this property.</td>
</tr>
<tr>
    <td><CopyableCode code="keyCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="logo" /></td>
    <td><code>string (base64url)</code></td>
    <td>The main logo for the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="managerApplications" /></td>
    <td><code>array</code></td>
    <td>A collection of application IDs for Microsoft first-party applications designated as managers. Manager applications can create service principals, agent identities, and agent users for managed agent blueprints. Limited to a maximum of 10 entries. Not nullable. Only supported on agentIdentityBlueprint objects; attempts to set this property on non-agent-blueprint applications return an error. Not returned by default; must be explicitly requested via $select.</td>
</tr>
<tr>
    <td><CopyableCode code="nativeAuthenticationApisEnabled" /></td>
    <td><code></code></td>
    <td>Specifies whether the Native Authentication APIs are enabled for the application. The possible values are: none and all. Default is none. For more information, see Native Authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="notes" /></td>
    <td><code>string</code></td>
    <td>Notes relevant for the management of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2RequirePostResponse" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="optionalClaims" /></td>
    <td><code></code></td>
    <td>Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.</td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>Directory objects that are owners of this application. The owners are a set of nonadmin users or service principals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="parentalControlSettings" /></td>
    <td><code></code></td>
    <td>Specifies parental control settings for an application.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordCredentials" /></td>
    <td><code>array</code></td>
    <td>The collection of password credentials associated with the application. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="publicClient" /></td>
    <td><code></code></td>
    <td>Specifies settings for installed clients such as desktop or mobile devices.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDomain" /></td>
    <td><code>string</code></td>
    <td>The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="requestSignatureVerification" /></td>
    <td><code></code></td>
    <td>Specifies whether this application requires Microsoft Entra ID to verify the signed authentication requests.</td>
</tr>
<tr>
    <td><CopyableCode code="requiredResourceAccess" /></td>
    <td><code>array</code></td>
    <td>Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="samlMetadataUrl" /></td>
    <td><code>string</code></td>
    <td>The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceManagementReference" /></td>
    <td><code>string</code></td>
    <td>References application or service contact information from a Service or Asset Management database. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalLockConfiguration" /></td>
    <td><code></code></td>
    <td>Specifies whether sensitive properties of a multitenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.</td>
</tr>
<tr>
    <td><CopyableCode code="signInAudience" /></td>
    <td><code>string</code></td>
    <td>Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg (default), AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount, and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you might need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="spa" /></td>
    <td><code></code></td>
    <td>Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.</td>
</tr>
<tr>
    <td><CopyableCode code="synchronization" /></td>
    <td><code></code></td>
    <td>Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenEncryptionKeyId" /></td>
    <td><code>string (uuid)</code></td>
    <td>Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user. (pattern: <code>^&#91;0-9a-fA-F&#93;&#123;8&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;4&#125;-&#91;0-9a-fA-F&#93;&#123;12&#125;$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuancePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="tokenLifetimePolicies" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>The unique identifier that can be assigned to an application and used as an alternate key. Immutable. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedPublisher" /></td>
    <td><code></code></td>
    <td>Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.</td>
</tr>
<tr>
    <td><CopyableCode code="web" /></td>
    <td><code></code></td>
    <td>Specifies settings for a web application.</td>
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
    <td><a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Get the properties and relationships of an application object. This API can be used to get agentIdentityBlueprint objects as well by their ID.</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-unique_name"><code>unique_name</code></a></td>
    <td></td>
    <td>Get the properties and relationships of an application object. This API can be used to get agentIdentityBlueprint objects as well by their ID.</td>
</tr>
<tr>
    <td><a href="#get_3"><CopyableCode code="get_3" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Get the properties and relationships of an application object. This API can be used to get agentIdentityBlueprint objects as well by their ID.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a></td>
    <td>Get the list of applications in this organization. This API also returns agentIdentityBlueprint objects, which are identified by the @odata.type property of #microsoft.graph.agentIdentityBlueprint.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new application object. This API can also create an agentIdentityBlueprint object when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a></td>
    <td></td>
    <td>Create a new application object if it doesn't exist, or update the properties of an existing application object. This API can also create an agentIdentityBlueprint object if it doesn't exist, or update properties of an existing agentIdentityBlueprint, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.</td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unique_name"><code>unique_name</code></a></td>
    <td></td>
    <td>Create a new application object if it doesn't exist, or update the properties of an existing application object. This API can also create an agentIdentityBlueprint object if it doesn't exist, or update properties of an existing agentIdentityBlueprint, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.</td>
</tr>
<tr>
    <td><a href="#update_3"><CopyableCode code="update_3" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Create a new application object if it doesn't exist, or update the properties of an existing application object. This API can also create an agentIdentityBlueprint object if it doesn't exist, or update properties of an existing agentIdentityBlueprint, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_id"><code>app_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted. This API can also delete an agentIdentityBlueprint object by its ID.</td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unique_name"><code>unique_name</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted. This API can also delete an agentIdentityBlueprint object by its ID.</td>
</tr>
<tr>
    <td><a href="#delete_3"><CopyableCode code="delete_3" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted. This API can also delete an agentIdentityBlueprint object by its ID.</td>
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
    <td><a href="#logo"><CopyableCode code="logo" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>The main logo for the application. Not nullable.</td>
</tr>
<tr>
    <td><a href="#logo_2"><CopyableCode code="logo_2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>The main logo for the application. Not nullable.</td>
</tr>
<tr>
    <td><a href="#add_key"><CopyableCode code="add_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Add a key credential to an application. This method, along with removeKey can be used by an application to automate rolling its expiring keys. As part of the request validation for this method, a proof of possession of an existing key is verified before the action can be performed.  Applications that don't have any existing valid certificates (no certificates have been added yet, or all certificates have expired), won't be able to use this service action. You can use the Update application operation to perform an update instead.</td>
</tr>
<tr>
    <td><a href="#add_password"><CopyableCode code="add_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Adds a strong password or secret to an application. You can also add passwords while creating the application.</td>
</tr>
<tr>
    <td><a href="#check_member_groups"><CopyableCode code="check_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.</td>
</tr>
<tr>
    <td><a href="#check_member_objects"><CopyableCode code="check_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_member_groups"><CopyableCode code="get_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.</td>
</tr>
<tr>
    <td><a href="#get_member_objects"><CopyableCode code="get_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.</td>
</tr>
<tr>
    <td><a href="#remove_key"><CopyableCode code="remove_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Remove a key credential from an agentIdentityBlueprint. This method along with addKey can be used to automate rolling its expiring keys.</td>
</tr>
<tr>
    <td><a href="#remove_password"><CopyableCode code="remove_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Remove a password from an application.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.</td>
</tr>
<tr>
    <td><a href="#set_verified_publisher"><CopyableCode code="set_verified_publisher" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Set the the verifiedPublisher on an agentIdentityBlueprint. For more information, including prerequisites to setting a verified publisher, see Publisher verification.</td>
</tr>
<tr>
    <td><a href="#unset_verified_publisher"><CopyableCode code="unset_verified_publisher" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Unset the verifiedPublisher previously set on an agentIdentityBlueprint, removing all verified publisher properties. For more information, see Publisher verification.</td>
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
<tr id="parameter-app_id">
    <td><CopyableCode code="app_id" /></td>
    <td><code>string</code></td>
    <td>Alternate key of application</td>
</tr>
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of application</td>
</tr>
<tr id="parameter-unique_name">
    <td><CopyableCode code="unique_name" /></td>
    <td><code>string</code></td>
    <td>Alternate key of application</td>
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
        { label: 'get_3', value: 'get_3' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the properties and relationships of an application object. This API can be used to get agentIdentityBlueprint objects as well by their ID.

```sql
SELECT
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web
FROM entra_id.applications.applications
WHERE app_id = '{{ app_id }}' -- required
;
```
</TabItem>
<TabItem value="get_2">

Get the properties and relationships of an application object. This API can be used to get agentIdentityBlueprint objects as well by their ID.

```sql
SELECT
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web
FROM entra_id.applications.applications
WHERE unique_name = '{{ unique_name }}' -- required
;
```
</TabItem>
<TabItem value="get_3">

Get the properties and relationships of an application object. This API can be used to get agentIdentityBlueprint objects as well by their ID.

```sql
SELECT
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web
FROM entra_id.applications.applications
WHERE application_id = '{{ application_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the list of applications in this organization. This API also returns agentIdentityBlueprint objects, which are identified by the @odata.type property of #microsoft.graph.agentIdentityBlueprint.

```sql
SELECT
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web
FROM entra_id.applications.applications
WHERE ConsistencyLevel = '{{ ConsistencyLevel }}'
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

Create a new application object. This API can also create an agentIdentityBlueprint object when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.

```sql
INSERT INTO entra_id.applications.applications (
id,
deletedDateTime,
addIns,
api,
appId,
applicationTemplateId,
appRoles,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
defaultRedirectUri,
description,
disabledByMicrosoftStatus,
displayName,
groupMembershipClaims,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
tags,
tokenEncryptionKeyId,
uniqueName,
verifiedPublisher,
web,
appManagementPolicies,
createdOnBehalfOf,
extensionProperties,
federatedIdentityCredentials,
homeRealmDiscoveryPolicies,
owners,
synchronization,
tokenIssuancePolicies,
tokenLifetimePolicies
)
SELECT 
'{{ id }}',
'{{ deletedDateTime }}',
'{{ addIns }}',
'{{ api }}',
'{{ appId }}',
'{{ applicationTemplateId }}',
'{{ appRoles }}',
'{{ authenticationBehaviors }}',
'{{ certification }}',
'{{ createdByAppId }}',
'{{ createdDateTime }}',
'{{ defaultRedirectUri }}',
'{{ description }}',
'{{ disabledByMicrosoftStatus }}',
'{{ displayName }}',
'{{ groupMembershipClaims }}',
'{{ identifierUris }}',
'{{ info }}',
{{ isDeviceOnlyAuthSupported }},
{{ isDisabled }},
{{ isFallbackPublicClient }},
'{{ keyCredentials }}',
'{{ logo }}',
'{{ managerApplications }}',
'{{ nativeAuthenticationApisEnabled }}',
'{{ notes }}',
{{ oauth2RequirePostResponse }},
'{{ optionalClaims }}',
'{{ parentalControlSettings }}',
'{{ passwordCredentials }}',
'{{ publicClient }}',
'{{ publisherDomain }}',
'{{ requestSignatureVerification }}',
'{{ requiredResourceAccess }}',
'{{ samlMetadataUrl }}',
'{{ serviceManagementReference }}',
'{{ servicePrincipalLockConfiguration }}',
'{{ signInAudience }}',
'{{ spa }}',
'{{ tags }}',
'{{ tokenEncryptionKeyId }}',
'{{ uniqueName }}',
'{{ verifiedPublisher }}',
'{{ web }}',
'{{ appManagementPolicies }}',
'{{ createdOnBehalfOf }}',
'{{ extensionProperties }}',
'{{ federatedIdentityCredentials }}',
'{{ homeRealmDiscoveryPolicies }}',
'{{ owners }}',
'{{ synchronization }}',
'{{ tokenIssuancePolicies }}',
'{{ tokenLifetimePolicies }}'
RETURNING
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: applications
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: addIns
      description: |
        Defines custom behavior that a consuming service can use to call an app in specific contexts. For example, applications that can render file streams can set the addIns property for its 'FileHandler' functionality. This lets services like Microsoft 365 call the application in the context of a document the user is working on.
      value:
        - id: "{{ id }}"
          properties: "{{ properties }}"
          type: "{{ type }}"
    - name: api
      value: "{{ api }}"
      description: |
        Specifies settings for an application that implements a web API.
    - name: appId
      value: "{{ appId }}"
      description: |
        The unique identifier for the application that is assigned to an application by Microsoft Entra ID. Not nullable. Read-only. Alternate key. Supports $filter (eq).
    - name: applicationTemplateId
      value: "{{ applicationTemplateId }}"
      description: |
        Unique identifier of the applicationTemplate. Supports $filter (eq, not, ne). Read-only. null if the app wasn't created from an application template.
    - name: appRoles
      description: |
        The collection of roles defined for the application. With app role assignments, these roles can be assigned to users, groups, or service principals associated with other applications. Not nullable.
      value:
        - allowedMemberTypes: "{{ allowedMemberTypes }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          id: "{{ id }}"
          isEnabled: {{ isEnabled }}
          origin: "{{ origin }}"
          value: "{{ value }}"
    - name: authenticationBehaviors
      value: "{{ authenticationBehaviors }}"
    - name: certification
      value: "{{ certification }}"
      description: |
        Specifies the certification status of the application.
    - name: createdByAppId
      value: "{{ createdByAppId }}"
      description: |
        The appId of the application that created this application. Set internally by Microsoft Entra ID. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The date and time the application was registered. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.  Supports $filter (eq, ne, not, ge, le, in, and eq on null values) and $orderby.
    - name: defaultRedirectUri
      value: "{{ defaultRedirectUri }}"
    - name: description
      value: "{{ description }}"
      description: |
        Free text field to provide a description of the application object to end users. The maximum allowed size is 1,024 characters. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    - name: disabledByMicrosoftStatus
      value: "{{ disabledByMicrosoftStatus }}"
      description: |
        Specifies whether Microsoft has disabled the registered application. The possible values are: null (default value), NotDisabled, and DisabledDueToViolationOfServicesAgreement (reasons include suspicious, abusive, or malicious activity, or a violation of the Microsoft Services Agreement).  Supports $filter (eq, ne, not).
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the application. Maximum length is 256 characters. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    - name: groupMembershipClaims
      value: "{{ groupMembershipClaims }}"
      description: |
        Configures the groups claim issued in a user or OAuth 2.0 access token that the application expects. To set this attribute, use one of the following valid string values: None, SecurityGroup (for security groups and Microsoft Entra roles), All (this gets all of the security groups, distribution groups, and Microsoft Entra directory roles that the signed-in user is a member of).
    - name: identifierUris
      value:
        - "{{ identifierUris }}"
      description: |
        Also known as App ID URI, this value is set when an application is used as a resource app. The identifierUris acts as the prefix for the scopes you reference in your API's code, and it must be globally unique across Microsoft Entra ID. For more information on valid identifierUris patterns and best practices, see Microsoft Entra application registration security best practices. Not nullable. Supports $filter (eq, ne, ge, le, startsWith).
    - name: info
      value: "{{ info }}"
      description: |
        Basic profile information of the application such as  app's marketing, support, terms of service and privacy statement URLs. The terms of service and privacy statement are surfaced to users through the user consent experience. For more info, see How to: Add Terms of service and privacy statement for registered Microsoft Entra apps. Supports $filter (eq, ne, not, ge, le, and eq on null values).
    - name: isDeviceOnlyAuthSupported
      value: {{ isDeviceOnlyAuthSupported }}
      description: |
        Specifies whether this application supports device authentication without a user. The default is false.
    - name: isDisabled
      value: {{ isDisabled }}
    - name: isFallbackPublicClient
      value: {{ isFallbackPublicClient }}
      description: |
        Specifies the fallback application type as public client, such as an installed application running on a mobile device. The default value is false, which means the fallback application type is confidential client such as a web app. There are certain scenarios where Microsoft Entra ID can't determine the client application type. For example, the ROPC flow where it's configured without specifying a redirect URI. In those cases, Microsoft Entra ID interprets the application type based on the value of this property.
    - name: keyCredentials
      description: |
        The collection of key credentials associated with the application. Not nullable. Supports $filter (eq, not, ge, le).
      value:
        - customKeyIdentifier: "{{ customKeyIdentifier }}"
          displayName: "{{ displayName }}"
          endDateTime: "{{ endDateTime }}"
          key: "{{ key }}"
          keyId: "{{ keyId }}"
          startDateTime: "{{ startDateTime }}"
          type: "{{ type }}"
          usage: "{{ usage }}"
    - name: logo
      value: "{{ logo }}"
      description: |
        The main logo for the application. Not nullable.
    - name: managerApplications
      value:
        - "{{ managerApplications }}"
      description: |
        A collection of application IDs for Microsoft first-party applications designated as managers. Manager applications can create service principals, agent identities, and agent users for managed agent blueprints. Limited to a maximum of 10 entries. Not nullable. Only supported on agentIdentityBlueprint objects; attempts to set this property on non-agent-blueprint applications return an error. Not returned by default; must be explicitly requested via $select.
    - name: nativeAuthenticationApisEnabled
      value: "{{ nativeAuthenticationApisEnabled }}"
      description: |
        Specifies whether the Native Authentication APIs are enabled for the application. The possible values are: none and all. Default is none. For more information, see Native Authentication.
    - name: notes
      value: "{{ notes }}"
      description: |
        Notes relevant for the management of the application.
    - name: oauth2RequirePostResponse
      value: {{ oauth2RequirePostResponse }}
    - name: optionalClaims
      value: "{{ optionalClaims }}"
      description: |
        Application developers can configure optional claims in their Microsoft Entra applications to specify the claims that are sent to their application by the Microsoft security token service. For more information, see How to: Provide optional claims to your app.
    - name: parentalControlSettings
      value: "{{ parentalControlSettings }}"
      description: |
        Specifies parental control settings for an application.
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
    - name: publicClient
      value: "{{ publicClient }}"
      description: |
        Specifies settings for installed clients such as desktop or mobile devices.
    - name: publisherDomain
      value: "{{ publisherDomain }}"
      description: |
        The verified publisher domain for the application. Read-only. For more information, see How to: Configure an application's publisher domain. Supports $filter (eq, ne, ge, le, startsWith).
    - name: requestSignatureVerification
      value: "{{ requestSignatureVerification }}"
      description: |
        Specifies whether this application requires Microsoft Entra ID to verify the signed authentication requests.
    - name: requiredResourceAccess
      description: |
        Specifies the resources that the application needs to access. This property also specifies the set of delegated permissions and application roles that it needs for each of those resources. This configuration of access to the required resources drives the consent experience. No more than 50 resource services (APIs) can be configured. Beginning mid-October 2021, the total number of required permissions must not exceed 400. For more information, see Limits on requested permissions per app. Not nullable. Supports $filter (eq, not, ge, le).
      value:
        - resourceAccess: "{{ resourceAccess }}"
          resourceAppId: "{{ resourceAppId }}"
    - name: samlMetadataUrl
      value: "{{ samlMetadataUrl }}"
      description: |
        The URL where the service exposes SAML metadata for federation. This property is valid only for single-tenant applications. Nullable.
    - name: serviceManagementReference
      value: "{{ serviceManagementReference }}"
      description: |
        References application or service contact information from a Service or Asset Management database. Nullable.
    - name: servicePrincipalLockConfiguration
      value: "{{ servicePrincipalLockConfiguration }}"
      description: |
        Specifies whether sensitive properties of a multitenant application should be locked for editing after the application is provisioned in a tenant. Nullable. null by default.
    - name: signInAudience
      value: "{{ signInAudience }}"
      description: |
        Specifies the Microsoft accounts that are supported for the current application. The possible values are: AzureADMyOrg (default), AzureADMultipleOrgs, AzureADandPersonalMicrosoftAccount, and PersonalMicrosoftAccount. See more in the table. The value of this object also limits the number of permissions an app can request. For more information, see Limits on requested permissions per app. The value for this property has implications on other app object properties. As a result, if you change this property, you might need to change other properties first. For more information, see Validation differences for signInAudience.Supports $filter (eq, ne, not).
    - name: spa
      value: "{{ spa }}"
      description: |
        Specifies settings for a single-page application, including sign out URLs and redirect URIs for authorization codes and access tokens.
    - name: tags
      value:
        - "{{ tags }}"
      description: |
        Custom strings that can be used to categorize and identify the application. Not nullable. Strings added here will also appear in the tags property of any associated service principals.Supports $filter (eq, not, ge, le, startsWith) and $search.
    - name: tokenEncryptionKeyId
      value: "{{ tokenEncryptionKeyId }}"
      description: |
        Specifies the keyId of a public key from the keyCredentials collection. When configured, Microsoft Entra ID encrypts all the tokens it emits by using the key this property points to. The application code that receives the encrypted token must use the matching private key to decrypt the token before it can be used for the signed-in user.
    - name: uniqueName
      value: "{{ uniqueName }}"
      description: |
        The unique identifier that can be assigned to an application and used as an alternate key. Immutable. Read-only.
    - name: verifiedPublisher
      value: "{{ verifiedPublisher }}"
      description: |
        Specifies the verified publisher of the application. For more information about how publisher verification helps support application security, trustworthiness, and compliance, see Publisher verification.
    - name: web
      value: "{{ web }}"
      description: |
        Specifies settings for a web application.
    - name: appManagementPolicies
      description: |
        The appManagementPolicy applied to this application.
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          isEnabled: {{ isEnabled }}
          restrictions: "{{ restrictions }}"
          appliesTo: "{{ appliesTo }}"
    - name: createdOnBehalfOf
      value: "{{ createdOnBehalfOf }}"
      description: |
        Supports $filter (/$count eq 0, /$count ne 0). Read-only.
    - name: extensionProperties
      description: |
        Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0).
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
          appDisplayName: "{{ appDisplayName }}"
          dataType: "{{ dataType }}"
          isMultiValued: {{ isMultiValued }}
          isSyncedFromOnPremises: {{ isSyncedFromOnPremises }}
          name: "{{ name }}"
          targetObjects: "{{ targetObjects }}"
    - name: federatedIdentityCredentials
      description: |
        Federated identities for applications. Supports $expand and $filter (startsWith, /$count eq 0, /$count ne 0).
      value:
        - id: "{{ id }}"
          audiences: "{{ audiences }}"
          description: "{{ description }}"
          issuer: "{{ issuer }}"
          name: "{{ name }}"
          subject: "{{ subject }}"
    - name: homeRealmDiscoveryPolicies
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          definition: "{{ definition }}"
          isOrganizationDefault: {{ isOrganizationDefault }}
          appliesTo: "{{ appliesTo }}"
    - name: owners
      description: |
        Directory objects that are owners of this application. The owners are a set of nonadmin users or service principals who are allowed to modify this object. Supports $expand, $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1), and $select nested in $expand.
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: synchronization
      value: "{{ synchronization }}"
      description: |
        Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.
    - name: tokenIssuancePolicies
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          definition: "{{ definition }}"
          isOrganizationDefault: {{ isOrganizationDefault }}
          appliesTo: "{{ appliesTo }}"
    - name: tokenLifetimePolicies
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          definition: "{{ definition }}"
          isOrganizationDefault: {{ isOrganizationDefault }}
          appliesTo: "{{ appliesTo }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'update_2', value: 'update_2' },
        { label: 'update_3', value: 'update_3' }
    ]}
>
<TabItem value="update">

Create a new application object if it doesn't exist, or update the properties of an existing application object. This API can also create an agentIdentityBlueprint object if it doesn't exist, or update properties of an existing agentIdentityBlueprint, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.

```sql
UPDATE entra_id.applications.applications
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
addIns = '{{ addIns }}',
api = '{{ api }}',
appId = '{{ appId }}',
applicationTemplateId = '{{ applicationTemplateId }}',
appRoles = '{{ appRoles }}',
authenticationBehaviors = '{{ authenticationBehaviors }}',
certification = '{{ certification }}',
createdByAppId = '{{ createdByAppId }}',
createdDateTime = '{{ createdDateTime }}',
defaultRedirectUri = '{{ defaultRedirectUri }}',
description = '{{ description }}',
disabledByMicrosoftStatus = '{{ disabledByMicrosoftStatus }}',
displayName = '{{ displayName }}',
groupMembershipClaims = '{{ groupMembershipClaims }}',
identifierUris = '{{ identifierUris }}',
info = '{{ info }}',
isDeviceOnlyAuthSupported = {{ isDeviceOnlyAuthSupported }},
isDisabled = {{ isDisabled }},
isFallbackPublicClient = {{ isFallbackPublicClient }},
keyCredentials = '{{ keyCredentials }}',
logo = '{{ logo }}',
managerApplications = '{{ managerApplications }}',
nativeAuthenticationApisEnabled = '{{ nativeAuthenticationApisEnabled }}',
notes = '{{ notes }}',
oauth2RequirePostResponse = {{ oauth2RequirePostResponse }},
optionalClaims = '{{ optionalClaims }}',
parentalControlSettings = '{{ parentalControlSettings }}',
passwordCredentials = '{{ passwordCredentials }}',
publicClient = '{{ publicClient }}',
publisherDomain = '{{ publisherDomain }}',
requestSignatureVerification = '{{ requestSignatureVerification }}',
requiredResourceAccess = '{{ requiredResourceAccess }}',
samlMetadataUrl = '{{ samlMetadataUrl }}',
serviceManagementReference = '{{ serviceManagementReference }}',
servicePrincipalLockConfiguration = '{{ servicePrincipalLockConfiguration }}',
signInAudience = '{{ signInAudience }}',
spa = '{{ spa }}',
tags = '{{ tags }}',
tokenEncryptionKeyId = '{{ tokenEncryptionKeyId }}',
uniqueName = '{{ uniqueName }}',
verifiedPublisher = '{{ verifiedPublisher }}',
web = '{{ web }}',
appManagementPolicies = '{{ appManagementPolicies }}',
createdOnBehalfOf = '{{ createdOnBehalfOf }}',
extensionProperties = '{{ extensionProperties }}',
federatedIdentityCredentials = '{{ federatedIdentityCredentials }}',
homeRealmDiscoveryPolicies = '{{ homeRealmDiscoveryPolicies }}',
owners = '{{ owners }}',
synchronization = '{{ synchronization }}',
tokenIssuancePolicies = '{{ tokenIssuancePolicies }}',
tokenLifetimePolicies = '{{ tokenLifetimePolicies }}'
WHERE 
app_id = '{{ app_id }}' --required
RETURNING
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web;
```
</TabItem>
<TabItem value="update_2">

Create a new application object if it doesn't exist, or update the properties of an existing application object. This API can also create an agentIdentityBlueprint object if it doesn't exist, or update properties of an existing agentIdentityBlueprint, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.

```sql
UPDATE entra_id.applications.applications
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
addIns = '{{ addIns }}',
api = '{{ api }}',
appId = '{{ appId }}',
applicationTemplateId = '{{ applicationTemplateId }}',
appRoles = '{{ appRoles }}',
authenticationBehaviors = '{{ authenticationBehaviors }}',
certification = '{{ certification }}',
createdByAppId = '{{ createdByAppId }}',
createdDateTime = '{{ createdDateTime }}',
defaultRedirectUri = '{{ defaultRedirectUri }}',
description = '{{ description }}',
disabledByMicrosoftStatus = '{{ disabledByMicrosoftStatus }}',
displayName = '{{ displayName }}',
groupMembershipClaims = '{{ groupMembershipClaims }}',
identifierUris = '{{ identifierUris }}',
info = '{{ info }}',
isDeviceOnlyAuthSupported = {{ isDeviceOnlyAuthSupported }},
isDisabled = {{ isDisabled }},
isFallbackPublicClient = {{ isFallbackPublicClient }},
keyCredentials = '{{ keyCredentials }}',
logo = '{{ logo }}',
managerApplications = '{{ managerApplications }}',
nativeAuthenticationApisEnabled = '{{ nativeAuthenticationApisEnabled }}',
notes = '{{ notes }}',
oauth2RequirePostResponse = {{ oauth2RequirePostResponse }},
optionalClaims = '{{ optionalClaims }}',
parentalControlSettings = '{{ parentalControlSettings }}',
passwordCredentials = '{{ passwordCredentials }}',
publicClient = '{{ publicClient }}',
publisherDomain = '{{ publisherDomain }}',
requestSignatureVerification = '{{ requestSignatureVerification }}',
requiredResourceAccess = '{{ requiredResourceAccess }}',
samlMetadataUrl = '{{ samlMetadataUrl }}',
serviceManagementReference = '{{ serviceManagementReference }}',
servicePrincipalLockConfiguration = '{{ servicePrincipalLockConfiguration }}',
signInAudience = '{{ signInAudience }}',
spa = '{{ spa }}',
tags = '{{ tags }}',
tokenEncryptionKeyId = '{{ tokenEncryptionKeyId }}',
uniqueName = '{{ uniqueName }}',
verifiedPublisher = '{{ verifiedPublisher }}',
web = '{{ web }}',
appManagementPolicies = '{{ appManagementPolicies }}',
createdOnBehalfOf = '{{ createdOnBehalfOf }}',
extensionProperties = '{{ extensionProperties }}',
federatedIdentityCredentials = '{{ federatedIdentityCredentials }}',
homeRealmDiscoveryPolicies = '{{ homeRealmDiscoveryPolicies }}',
owners = '{{ owners }}',
synchronization = '{{ synchronization }}',
tokenIssuancePolicies = '{{ tokenIssuancePolicies }}',
tokenLifetimePolicies = '{{ tokenLifetimePolicies }}'
WHERE 
unique_name = '{{ unique_name }}' --required
RETURNING
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web;
```
</TabItem>
<TabItem value="update_3">

Create a new application object if it doesn't exist, or update the properties of an existing application object. This API can also create an agentIdentityBlueprint object if it doesn't exist, or update properties of an existing agentIdentityBlueprint, when the @odata.type property is set to #microsoft.graph.agentIdentityBlueprint.

```sql
UPDATE entra_id.applications.applications
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
addIns = '{{ addIns }}',
api = '{{ api }}',
appId = '{{ appId }}',
applicationTemplateId = '{{ applicationTemplateId }}',
appRoles = '{{ appRoles }}',
authenticationBehaviors = '{{ authenticationBehaviors }}',
certification = '{{ certification }}',
createdByAppId = '{{ createdByAppId }}',
createdDateTime = '{{ createdDateTime }}',
defaultRedirectUri = '{{ defaultRedirectUri }}',
description = '{{ description }}',
disabledByMicrosoftStatus = '{{ disabledByMicrosoftStatus }}',
displayName = '{{ displayName }}',
groupMembershipClaims = '{{ groupMembershipClaims }}',
identifierUris = '{{ identifierUris }}',
info = '{{ info }}',
isDeviceOnlyAuthSupported = {{ isDeviceOnlyAuthSupported }},
isDisabled = {{ isDisabled }},
isFallbackPublicClient = {{ isFallbackPublicClient }},
keyCredentials = '{{ keyCredentials }}',
logo = '{{ logo }}',
managerApplications = '{{ managerApplications }}',
nativeAuthenticationApisEnabled = '{{ nativeAuthenticationApisEnabled }}',
notes = '{{ notes }}',
oauth2RequirePostResponse = {{ oauth2RequirePostResponse }},
optionalClaims = '{{ optionalClaims }}',
parentalControlSettings = '{{ parentalControlSettings }}',
passwordCredentials = '{{ passwordCredentials }}',
publicClient = '{{ publicClient }}',
publisherDomain = '{{ publisherDomain }}',
requestSignatureVerification = '{{ requestSignatureVerification }}',
requiredResourceAccess = '{{ requiredResourceAccess }}',
samlMetadataUrl = '{{ samlMetadataUrl }}',
serviceManagementReference = '{{ serviceManagementReference }}',
servicePrincipalLockConfiguration = '{{ servicePrincipalLockConfiguration }}',
signInAudience = '{{ signInAudience }}',
spa = '{{ spa }}',
tags = '{{ tags }}',
tokenEncryptionKeyId = '{{ tokenEncryptionKeyId }}',
uniqueName = '{{ uniqueName }}',
verifiedPublisher = '{{ verifiedPublisher }}',
web = '{{ web }}',
appManagementPolicies = '{{ appManagementPolicies }}',
createdOnBehalfOf = '{{ createdOnBehalfOf }}',
extensionProperties = '{{ extensionProperties }}',
federatedIdentityCredentials = '{{ federatedIdentityCredentials }}',
homeRealmDiscoveryPolicies = '{{ homeRealmDiscoveryPolicies }}',
owners = '{{ owners }}',
synchronization = '{{ synchronization }}',
tokenIssuancePolicies = '{{ tokenIssuancePolicies }}',
tokenLifetimePolicies = '{{ tokenLifetimePolicies }}'
WHERE 
application_id = '{{ application_id }}' --required
RETURNING
id,
addIns,
api,
appId,
appManagementPolicies,
appRoles,
applicationTemplateId,
authenticationBehaviors,
certification,
createdByAppId,
createdDateTime,
createdOnBehalfOf,
defaultRedirectUri,
deletedDateTime,
description,
disabledByMicrosoftStatus,
displayName,
extensionProperties,
federatedIdentityCredentials,
groupMembershipClaims,
homeRealmDiscoveryPolicies,
identifierUris,
info,
isDeviceOnlyAuthSupported,
isDisabled,
isFallbackPublicClient,
keyCredentials,
logo,
managerApplications,
nativeAuthenticationApisEnabled,
notes,
oauth2RequirePostResponse,
optionalClaims,
owners,
parentalControlSettings,
passwordCredentials,
publicClient,
publisherDomain,
requestSignatureVerification,
requiredResourceAccess,
samlMetadataUrl,
serviceManagementReference,
servicePrincipalLockConfiguration,
signInAudience,
spa,
synchronization,
tags,
tokenEncryptionKeyId,
tokenIssuancePolicies,
tokenLifetimePolicies,
uniqueName,
verifiedPublisher,
web;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_2', value: 'delete_2' },
        { label: 'delete_3', value: 'delete_3' }
    ]}
>
<TabItem value="delete">

Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted. This API can also delete an agentIdentityBlueprint object by its ID.

```sql
DELETE FROM entra_id.applications.applications
WHERE app_id = '{{ app_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted. This API can also delete an agentIdentityBlueprint object by its ID.

```sql
DELETE FROM entra_id.applications.applications
WHERE unique_name = '{{ unique_name }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_3">

Delete an application object. When deleted, apps are moved to a temporary container and can be restored within 30 days. After that time, they are permanently deleted. This API can also delete an agentIdentityBlueprint object by its ID.

```sql
DELETE FROM entra_id.applications.applications
WHERE application_id = '{{ application_id }}' --required
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
        { label: 'logo', value: 'logo' },
        { label: 'logo_2', value: 'logo_2' },
        { label: 'add_key', value: 'add_key' },
        { label: 'add_password', value: 'add_password' },
        { label: 'check_member_groups', value: 'check_member_groups' },
        { label: 'check_member_objects', value: 'check_member_objects' },
        { label: 'get_member_groups', value: 'get_member_groups' },
        { label: 'get_member_objects', value: 'get_member_objects' },
        { label: 'remove_key', value: 'remove_key' },
        { label: 'remove_password', value: 'remove_password' },
        { label: 'restore', value: 'restore' },
        { label: 'set_verified_publisher', value: 'set_verified_publisher' },
        { label: 'unset_verified_publisher', value: 'unset_verified_publisher' }
    ]}
>
<TabItem value="get_available_extension_properties">

Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:

```sql
EXEC entra_id.applications.applications.get_available_extension_properties 
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
EXEC entra_id.applications.applications.get_by_ids 
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
EXEC entra_id.applications.applications.validate_properties 
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
<TabItem value="logo">

The main logo for the application. Not nullable.

```sql
EXEC entra_id.applications.applications.logo 
@application_id='{{ application_id }}' --required
;
```
</TabItem>
<TabItem value="logo_2">

The main logo for the application. Not nullable.

```sql
EXEC entra_id.applications.applications.logo_2 
@application_id='{{ application_id }}' --required, 
@If-Match='{{ If-Match }}'
;
```
</TabItem>
<TabItem value="add_key">

Add a key credential to an application. This method, along with removeKey can be used by an application to automate rolling its expiring keys. As part of the request validation for this method, a proof of possession of an existing key is verified before the action can be performed.  Applications that don't have any existing valid certificates (no certificates have been added yet, or all certificates have expired), won't be able to use this service action. You can use the Update application operation to perform an update instead.

```sql
EXEC entra_id.applications.applications.add_key 
@application_id='{{ application_id }}' --required 
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

Adds a strong password or secret to an application. You can also add passwords while creating the application.

```sql
EXEC entra_id.applications.applications.add_password 
@application_id='{{ application_id }}' --required 
@@json=
'{
"passwordCredential": "{{ passwordCredential }}"
}'
;
```
</TabItem>
<TabItem value="check_member_groups">

Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.

```sql
EXEC entra_id.applications.applications.check_member_groups 
@application_id='{{ application_id }}' --required 
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
EXEC entra_id.applications.applications.check_member_objects 
@application_id='{{ application_id }}' --required 
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
EXEC entra_id.applications.applications.get_member_groups 
@application_id='{{ application_id }}' --required 
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
EXEC entra_id.applications.applications.get_member_objects 
@application_id='{{ application_id }}' --required 
@@json=
'{
"securityEnabledOnly": {{ securityEnabledOnly }}
}'
;
```
</TabItem>
<TabItem value="remove_key">

Remove a key credential from an agentIdentityBlueprint. This method along with addKey can be used to automate rolling its expiring keys.

```sql
EXEC entra_id.applications.applications.remove_key 
@application_id='{{ application_id }}' --required 
@@json=
'{
"keyId": "{{ keyId }}", 
"proof": "{{ proof }}"
}'
;
```
</TabItem>
<TabItem value="remove_password">

Remove a password from an application.

```sql
EXEC entra_id.applications.applications.remove_password 
@application_id='{{ application_id }}' --required 
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
EXEC entra_id.applications.applications.restore 
@application_id='{{ application_id }}' --required
;
```
</TabItem>
<TabItem value="set_verified_publisher">

Set the the verifiedPublisher on an agentIdentityBlueprint. For more information, including prerequisites to setting a verified publisher, see Publisher verification.

```sql
EXEC entra_id.applications.applications.set_verified_publisher 
@application_id='{{ application_id }}' --required 
@@json=
'{
"verifiedPublisherId": "{{ verifiedPublisherId }}"
}'
;
```
</TabItem>
<TabItem value="unset_verified_publisher">

Unset the verifiedPublisher previously set on an agentIdentityBlueprint, removing all verified publisher properties. For more information, see Publisher verification.

```sql
EXEC entra_id.applications.applications.unset_verified_publisher 
@application_id='{{ application_id }}' --required
;
```
</TabItem>
</Tabs>
