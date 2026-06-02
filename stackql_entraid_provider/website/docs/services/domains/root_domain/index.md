--- 
title: root_domain
hide_title: false
hide_table_of_contents: false
keywords:
  - root_domain
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

Creates, updates, deletes, gets or lists a <code>root_domain</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="root_domain" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.domains.root_domain" /></td></tr>
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
    <td>Get the root domain of a subdomain. This API returns a single object.</td>
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

Get the root domain of a subdomain. This API returns a single object.

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
FROM entra_id.domains.root_domain
WHERE domain-id = '{{ domain-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
