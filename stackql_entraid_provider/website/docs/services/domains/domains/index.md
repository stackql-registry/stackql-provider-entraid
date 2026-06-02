--- 
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domains
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.domains.domains" /></td></tr>
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
    <td><CopyableCode code="authenticationType" /></td>
    <td><code>string</code></td>
    <td>Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Microsoft Entra ID performs user authentication. Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. Not nullable.  To update this property in delegated scenarios, the calling app must be assigned the Domain-InternalFederation.ReadWrite.All permission.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityStatus" /></td>
    <td><code>string</code></td>
    <td>This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="domainNameReferences" /></td>
    <td><code>array</code></td>
    <td>The objects such as users and groups that reference the domain ID. Read-only, Nullable. Doesn't support $expand. Supports $filter by the OData type of objects returned. For example, /domains/&#123;domainId&#125;/domainNameReferences/microsoft.graph.user and /domains/&#123;domainId&#125;/domainNameReferences/microsoft.graph.group.</td>
</tr>
<tr>
    <td><CopyableCode code="federationConfiguration" /></td>
    <td><code>array</code></td>
    <td>Domain settings configured by a customer when federated with Microsoft Entra ID. Doesn't support $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isAdminManaged" /></td>
    <td><code>boolean</code></td>
    <td>The value of the property is false if the DNS record management of the domain is delegated to Microsoft 365. Otherwise, the value is true. Not nullable</td>
</tr>
<tr>
    <td><CopyableCode code="isDefault" /></td>
    <td><code>boolean</code></td>
    <td>true if this is the default domain that is used for user creation. There's only one default domain per company. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="isInitial" /></td>
    <td><code>boolean</code></td>
    <td>true if this is the initial domain created by Microsoft Online Services (contoso.com). There's only one initial domain per company. Not nullable</td>
</tr>
<tr>
    <td><CopyableCode code="isRoot" /></td>
    <td><code>boolean</code></td>
    <td>true if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="isVerified" /></td>
    <td><code>boolean</code></td>
    <td>true if the domain completed domain ownership verification. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="passwordNotificationWindowInDays" /></td>
    <td><code>number (int32)</code></td>
    <td>Specifies the number of days before a user receives notification that their password expires. If the property isn't set, a default value of 14 days is used.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordValidityPeriodInDays" /></td>
    <td><code>number (int32)</code></td>
    <td>Specifies the length of time that a password is valid before it must be changed. If the property isn't set, a default value of 90 days is used.</td>
</tr>
<tr>
    <td><CopyableCode code="rootDomain" /></td>
    <td><code></code></td>
    <td>Root domain of a subdomain. Read-only, Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceConfigurationRecords" /></td>
    <td><code>array</code></td>
    <td>DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Doesn't support $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>Status of asynchronous operations scheduled for the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedServices" /></td>
    <td><code>array</code></td>
    <td>The capabilities assigned to the domain. Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune. The values that you can add or remove using the API include: Email, OfficeCommunicationsOnline, Yammer. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="verificationDnsRecords" /></td>
    <td><code>array</code></td>
    <td>DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Microsoft Entra ID. Read-only, Nullable. Doesn't support $expand.</td>
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
    <td><CopyableCode code="authenticationType" /></td>
    <td><code>string</code></td>
    <td>Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Microsoft Entra ID performs user authentication. Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. Not nullable.  To update this property in delegated scenarios, the calling app must be assigned the Domain-InternalFederation.ReadWrite.All permission.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityStatus" /></td>
    <td><code>string</code></td>
    <td>This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.</td>
</tr>
<tr>
    <td><CopyableCode code="domainNameReferences" /></td>
    <td><code>array</code></td>
    <td>The objects such as users and groups that reference the domain ID. Read-only, Nullable. Doesn't support $expand. Supports $filter by the OData type of objects returned. For example, /domains/&#123;domainId&#125;/domainNameReferences/microsoft.graph.user and /domains/&#123;domainId&#125;/domainNameReferences/microsoft.graph.group.</td>
</tr>
<tr>
    <td><CopyableCode code="federationConfiguration" /></td>
    <td><code>array</code></td>
    <td>Domain settings configured by a customer when federated with Microsoft Entra ID. Doesn't support $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isAdminManaged" /></td>
    <td><code>boolean</code></td>
    <td>The value of the property is false if the DNS record management of the domain is delegated to Microsoft 365. Otherwise, the value is true. Not nullable</td>
</tr>
<tr>
    <td><CopyableCode code="isDefault" /></td>
    <td><code>boolean</code></td>
    <td>true if this is the default domain that is used for user creation. There's only one default domain per company. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="isInitial" /></td>
    <td><code>boolean</code></td>
    <td>true if this is the initial domain created by Microsoft Online Services (contoso.com). There's only one initial domain per company. Not nullable</td>
</tr>
<tr>
    <td><CopyableCode code="isRoot" /></td>
    <td><code>boolean</code></td>
    <td>true if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="isVerified" /></td>
    <td><code>boolean</code></td>
    <td>true if the domain completed domain ownership verification. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="passwordNotificationWindowInDays" /></td>
    <td><code>number (int32)</code></td>
    <td>Specifies the number of days before a user receives notification that their password expires. If the property isn't set, a default value of 14 days is used.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordValidityPeriodInDays" /></td>
    <td><code>number (int32)</code></td>
    <td>Specifies the length of time that a password is valid before it must be changed. If the property isn't set, a default value of 90 days is used.</td>
</tr>
<tr>
    <td><CopyableCode code="rootDomain" /></td>
    <td><code></code></td>
    <td>Root domain of a subdomain. Read-only, Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceConfigurationRecords" /></td>
    <td><code>array</code></td>
    <td>DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Doesn't support $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>Status of asynchronous operations scheduled for the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedServices" /></td>
    <td><code>array</code></td>
    <td>The capabilities assigned to the domain. Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune. The values that you can add or remove using the API include: Email, OfficeCommunicationsOnline, Yammer. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="verificationDnsRecords" /></td>
    <td><code>array</code></td>
    <td>DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Microsoft Entra ID. Read-only, Nullable. Doesn't support $expand.</td>
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
    <td><a href="#parameter-domain-id"><code>domain-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of domain object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of domain objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Adds a domain to the tenant. Important: You cannot use an associated domain with your Microsoft Entra tenant until ownership is verified. See List verificationDnsRecords for details. Root domains require verification. For example, contoso.com requires verification. If a root domain is verified, subdomains of the root domain are automatically verified. For example, subdomain.contoso.com is automatically be verified if contoso.com has been verified.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-domain-id"><code>domain-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of domain object. Only verified domains can be updated.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-domain-id"><code>domain-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a domain from a tenant.</td>
</tr>
<tr>
    <td><a href="#verify"><CopyableCode code="verify" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-domain-id"><code>domain-id</code></a></td>
    <td></td>
    <td>Validate the ownership of a domain. This operation only applies to an unverified domain. For an unverified domain, the isVerified property is false.</td>
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
<tr id="parameter-domain-id">
    <td><CopyableCode code="domain-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of domain</td>
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

Retrieve the properties and relationships of domain object.

```sql
SELECT
id,
@odata.type,
authenticationType,
availabilityStatus,
domainNameReferences,
federationConfiguration,
isAdminManaged,
isDefault,
isInitial,
isRoot,
isVerified,
manufacturer,
model,
passwordNotificationWindowInDays,
passwordValidityPeriodInDays,
rootDomain,
serviceConfigurationRecords,
state,
supportedServices,
verificationDnsRecords
FROM entra_id.domains.domains
WHERE domain-id = '{{ domain-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of domain objects.

```sql
SELECT
id,
@odata.type,
authenticationType,
availabilityStatus,
domainNameReferences,
federationConfiguration,
isAdminManaged,
isDefault,
isInitial,
isRoot,
isVerified,
manufacturer,
model,
passwordNotificationWindowInDays,
passwordValidityPeriodInDays,
rootDomain,
serviceConfigurationRecords,
state,
supportedServices,
verificationDnsRecords
FROM entra_id.domains.domains
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

Adds a domain to the tenant. Important: You cannot use an associated domain with your Microsoft Entra tenant until ownership is verified. See List verificationDnsRecords for details. Root domains require verification. For example, contoso.com requires verification. If a root domain is verified, subdomains of the root domain are automatically verified. For example, subdomain.contoso.com is automatically be verified if contoso.com has been verified.

```sql
INSERT INTO entra_id.domains.domains (
id,
@odata.type,
authenticationType,
availabilityStatus,
isAdminManaged,
isDefault,
isInitial,
isRoot,
isVerified,
manufacturer,
model,
passwordNotificationWindowInDays,
passwordValidityPeriodInDays,
state,
supportedServices,
domainNameReferences,
federationConfiguration,
rootDomain,
serviceConfigurationRecords,
verificationDnsRecords
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ authenticationType }}',
'{{ availabilityStatus }}',
{{ isAdminManaged }},
{{ isDefault }},
{{ isInitial }},
{{ isRoot }},
{{ isVerified }},
'{{ manufacturer }}',
'{{ model }}',
{{ passwordNotificationWindowInDays }},
{{ passwordValidityPeriodInDays }},
'{{ state }}',
'{{ supportedServices }}',
'{{ domainNameReferences }}',
'{{ federationConfiguration }}',
'{{ rootDomain }}',
'{{ serviceConfigurationRecords }}',
'{{ verificationDnsRecords }}'
RETURNING
id,
@odata.type,
authenticationType,
availabilityStatus,
domainNameReferences,
federationConfiguration,
isAdminManaged,
isDefault,
isInitial,
isRoot,
isVerified,
manufacturer,
model,
passwordNotificationWindowInDays,
passwordValidityPeriodInDays,
rootDomain,
serviceConfigurationRecords,
state,
supportedServices,
verificationDnsRecords
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: domains
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: authenticationType
      value: "{{ authenticationType }}"
      description: |
        Indicates the configured authentication type for the domain. The value is either Managed or Federated. Managed indicates a cloud managed domain where Microsoft Entra ID performs user authentication. Federated indicates authentication is federated with an identity provider such as the tenant's on-premises Active Directory via Active Directory Federation Services. Not nullable.  To update this property in delegated scenarios, the calling app must be assigned the Domain-InternalFederation.ReadWrite.All permission.
    - name: availabilityStatus
      value: "{{ availabilityStatus }}"
      description: |
        This property is always null except when the verify action is used. When the verify action is used, a domain entity is returned in the response. The availabilityStatus property of the domain entity in the response is either AvailableImmediately or EmailVerifiedDomainTakeoverScheduled.
    - name: isAdminManaged
      value: {{ isAdminManaged }}
      description: |
        The value of the property is false if the DNS record management of the domain is delegated to Microsoft 365. Otherwise, the value is true. Not nullable
    - name: isDefault
      value: {{ isDefault }}
      description: |
        true if this is the default domain that is used for user creation. There's only one default domain per company. Not nullable.
    - name: isInitial
      value: {{ isInitial }}
      description: |
        true if this is the initial domain created by Microsoft Online Services (contoso.com). There's only one initial domain per company. Not nullable
    - name: isRoot
      value: {{ isRoot }}
      description: |
        true if the domain is a verified root domain. Otherwise, false if the domain is a subdomain or unverified. Not nullable.
    - name: isVerified
      value: {{ isVerified }}
      description: |
        true if the domain completed domain ownership verification. Not nullable.
    - name: manufacturer
      value: "{{ manufacturer }}"
    - name: model
      value: "{{ model }}"
    - name: passwordNotificationWindowInDays
      value: {{ passwordNotificationWindowInDays }}
      description: |
        Specifies the number of days before a user receives notification that their password expires. If the property isn't set, a default value of 14 days is used.
    - name: passwordValidityPeriodInDays
      value: {{ passwordValidityPeriodInDays }}
      description: |
        Specifies the length of time that a password is valid before it must be changed. If the property isn't set, a default value of 90 days is used.
    - name: state
      value: "{{ state }}"
      description: |
        Status of asynchronous operations scheduled for the domain.
    - name: supportedServices
      value:
        - "{{ supportedServices }}"
      description: |
        The capabilities assigned to the domain. Can include 0, 1 or more of following values: Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune. The values that you can add or remove using the API include: Email, OfficeCommunicationsOnline, Yammer. Not nullable.
    - name: domainNameReferences
      description: |
        The objects such as users and groups that reference the domain ID. Read-only, Nullable. Doesn't support $expand. Supports $filter by the OData type of objects returned. For example, /domains/{domainId}/domainNameReferences/microsoft.graph.user and /domains/{domainId}/domainNameReferences/microsoft.graph.group.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: federationConfiguration
      description: |
        Domain settings configured by a customer when federated with Microsoft Entra ID. Doesn't support $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          displayName: "{{ displayName }}"
          issuerUri: "{{ issuerUri }}"
          metadataExchangeUri: "{{ metadataExchangeUri }}"
          passiveSignInUri: "{{ passiveSignInUri }}"
          preferredAuthenticationProtocol: "{{ preferredAuthenticationProtocol }}"
          signingCertificate: "{{ signingCertificate }}"
          activeSignInUri: "{{ activeSignInUri }}"
          federatedIdpMfaBehavior: "{{ federatedIdpMfaBehavior }}"
          isSignedAuthenticationRequestRequired: {{ isSignedAuthenticationRequestRequired }}
          nextSigningCertificate: "{{ nextSigningCertificate }}"
          passwordResetUri: "{{ passwordResetUri }}"
          promptLoginBehavior: "{{ promptLoginBehavior }}"
          signingCertificateUpdateStatus: "{{ signingCertificateUpdateStatus }}"
          signOutUri: "{{ signOutUri }}"
    - name: rootDomain
      value: "{{ rootDomain }}"
      description: |
        Root domain of a subdomain. Read-only, Nullable. Supports $expand.
    - name: serviceConfigurationRecords
      description: |
        DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Doesn't support $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          isOptional: {{ isOptional }}
          label: "{{ label }}"
          recordType: "{{ recordType }}"
          supportedService: "{{ supportedService }}"
          ttl: {{ ttl }}
    - name: verificationDnsRecords
      description: |
        DNS records that the customer adds to the DNS zone file of the domain before the customer can complete domain ownership verification with Microsoft Entra ID. Read-only, Nullable. Doesn't support $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          isOptional: {{ isOptional }}
          label: "{{ label }}"
          recordType: "{{ recordType }}"
          supportedService: "{{ supportedService }}"
          ttl: {{ ttl }}
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

Update the properties of domain object. Only verified domains can be updated.

```sql
UPDATE entra_id.domains.domains
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
authenticationType = '{{ authenticationType }}',
availabilityStatus = '{{ availabilityStatus }}',
isAdminManaged = {{ isAdminManaged }},
isDefault = {{ isDefault }},
isInitial = {{ isInitial }},
isRoot = {{ isRoot }},
isVerified = {{ isVerified }},
manufacturer = '{{ manufacturer }}',
model = '{{ model }}',
passwordNotificationWindowInDays = {{ passwordNotificationWindowInDays }},
passwordValidityPeriodInDays = {{ passwordValidityPeriodInDays }},
state = '{{ state }}',
supportedServices = '{{ supportedServices }}',
domainNameReferences = '{{ domainNameReferences }}',
federationConfiguration = '{{ federationConfiguration }}',
rootDomain = '{{ rootDomain }}',
serviceConfigurationRecords = '{{ serviceConfigurationRecords }}',
verificationDnsRecords = '{{ verificationDnsRecords }}'
WHERE 
domain-id = '{{ domain-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
authenticationType,
availabilityStatus,
domainNameReferences,
federationConfiguration,
isAdminManaged,
isDefault,
isInitial,
isRoot,
isVerified,
manufacturer,
model,
passwordNotificationWindowInDays,
passwordValidityPeriodInDays,
rootDomain,
serviceConfigurationRecords,
state,
supportedServices,
verificationDnsRecords;
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

Delete a domain from a tenant.

```sql
DELETE FROM entra_id.domains.domains
WHERE domain-id = '{{ domain-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="verify"
    values={[
        { label: 'verify', value: 'verify' }
    ]}
>
<TabItem value="verify">

Validate the ownership of a domain. This operation only applies to an unverified domain. For an unverified domain, the isVerified property is false.

```sql
EXEC entra_id.domains.domains.verify 
@domain-id='{{ domain-id }}' --required
;
```
</TabItem>
</Tabs>
