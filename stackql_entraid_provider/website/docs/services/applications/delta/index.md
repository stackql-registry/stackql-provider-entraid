--- 
title: delta
hide_title: false
hide_table_of_contents: false
keywords:
  - delta
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

Creates, updates, deletes, gets or lists a <code>delta</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delta" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.applications.delta" /></td></tr>
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
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get newly created, updated, or deleted applications without performing a full read of the entire resource collection. For more information, see Use delta query to track changes in Microsoft Graph data for details.</td>
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

Get newly created, updated, or deleted applications without performing a full read of the entire resource collection. For more information, see Use delta query to track changes in Microsoft Graph data for details.

```sql
SELECT
id,
@odata.type,
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
FROM entra_id.applications.delta
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
