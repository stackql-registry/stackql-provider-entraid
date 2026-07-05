--- 
title: federation_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - federation_configuration
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

Creates, updates, deletes, gets or lists a <code>federation_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="federation_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.domains.federation_configuration" /></td></tr>
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
    <td><CopyableCode code="activeSignInUri" /></td>
    <td><code>string</code></td>
    <td>URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Microsoft Entra ID. Corresponds to the ActiveLogOnUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the identity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="federatedIdpMfaBehavior" /></td>
    <td><code></code></td>
    <td>Determines whether Microsoft Entra ID accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.</td>
</tr>
<tr>
    <td><CopyableCode code="isSignedAuthenticationRequestRequired" /></td>
    <td><code>boolean</code></td>
    <td>If true, when SAML authentication requests are sent to the federated SAML IdP, Microsoft Entra ID will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP aren't signed.</td>
</tr>
<tr>
    <td><CopyableCode code="issuerUri" /></td>
    <td><code>string</code></td>
    <td>Issuer URI of the federation server.</td>
</tr>
<tr>
    <td><CopyableCode code="metadataExchangeUri" /></td>
    <td><code>string</code></td>
    <td>URI of the metadata exchange endpoint used for authentication from rich client applications.</td>
</tr>
<tr>
    <td><CopyableCode code="nextSigningCertificate" /></td>
    <td><code>string</code></td>
    <td>Fallback token signing certificate that can also be used to sign tokens, for example when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.</td>
</tr>
<tr>
    <td><CopyableCode code="passiveSignInUri" /></td>
    <td><code>string</code></td>
    <td>URI that web-based clients are directed to when signing in to Microsoft Entra services.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordResetUri" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="preferredAuthenticationProtocol" /></td>
    <td><code></code></td>
    <td>Preferred authentication protocol. The possible values are: wsFed, saml, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="promptLoginBehavior" /></td>
    <td><code></code></td>
    <td>Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="signOutUri" /></td>
    <td><code>string</code></td>
    <td>URI that clients are redirected to when they sign out of Microsoft Entra services. Corresponds to the LogOffUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.</td>
</tr>
<tr>
    <td><CopyableCode code="signingCertificate" /></td>
    <td><code>string</code></td>
    <td>Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Microsoft Entra ID updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Microsoft Entra ID monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.</td>
</tr>
<tr>
    <td><CopyableCode code="signingCertificateUpdateStatus" /></td>
    <td><code></code></td>
    <td>Provides status and timestamp of the last update of the signing certificate.</td>
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
    <td><CopyableCode code="activeSignInUri" /></td>
    <td><code>string</code></td>
    <td>URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Microsoft Entra ID. Corresponds to the ActiveLogOnUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the identity provider.</td>
</tr>
<tr>
    <td><CopyableCode code="federatedIdpMfaBehavior" /></td>
    <td><code></code></td>
    <td>Determines whether Microsoft Entra ID accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.</td>
</tr>
<tr>
    <td><CopyableCode code="isSignedAuthenticationRequestRequired" /></td>
    <td><code>boolean</code></td>
    <td>If true, when SAML authentication requests are sent to the federated SAML IdP, Microsoft Entra ID will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP aren't signed.</td>
</tr>
<tr>
    <td><CopyableCode code="issuerUri" /></td>
    <td><code>string</code></td>
    <td>Issuer URI of the federation server.</td>
</tr>
<tr>
    <td><CopyableCode code="metadataExchangeUri" /></td>
    <td><code>string</code></td>
    <td>URI of the metadata exchange endpoint used for authentication from rich client applications.</td>
</tr>
<tr>
    <td><CopyableCode code="nextSigningCertificate" /></td>
    <td><code>string</code></td>
    <td>Fallback token signing certificate that can also be used to sign tokens, for example when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.</td>
</tr>
<tr>
    <td><CopyableCode code="passiveSignInUri" /></td>
    <td><code>string</code></td>
    <td>URI that web-based clients are directed to when signing in to Microsoft Entra services.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordResetUri" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="preferredAuthenticationProtocol" /></td>
    <td><code></code></td>
    <td>Preferred authentication protocol. The possible values are: wsFed, saml, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="promptLoginBehavior" /></td>
    <td><code></code></td>
    <td>Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="signOutUri" /></td>
    <td><code>string</code></td>
    <td>URI that clients are redirected to when they sign out of Microsoft Entra services. Corresponds to the LogOffUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.</td>
</tr>
<tr>
    <td><CopyableCode code="signingCertificate" /></td>
    <td><code>string</code></td>
    <td>Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Microsoft Entra ID updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Microsoft Entra ID monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.</td>
</tr>
<tr>
    <td><CopyableCode code="signingCertificateUpdateStatus" /></td>
    <td><code></code></td>
    <td>Provides status and timestamp of the last update of the signing certificate.</td>
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
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-internal_domain_federation_id"><code>internal_domain_federation_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of an internalDomainFederation object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a></td>
    <td></td>
    <td>Read the properties of the internalDomainFederation objects for the domain. This API returns only one object in the collection.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a></td>
    <td></td>
    <td>Create a new internalDomainFederation object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-internal_domain_federation_id"><code>internal_domain_federation_id</code></a></td>
    <td></td>
    <td>Update the properties of an internalDomainFederation object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-internal_domain_federation_id"><code>internal_domain_federation_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an internalDomainFederation object.</td>
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
<tr id="parameter-domain_id">
    <td><CopyableCode code="domain_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of domain</td>
</tr>
<tr id="parameter-internal_domain_federation_id">
    <td><CopyableCode code="internal_domain_federation_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of internalDomainFederation</td>
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

Read the properties and relationships of an internalDomainFederation object.

```sql
SELECT
id,
activeSignInUri,
displayName,
federatedIdpMfaBehavior,
isSignedAuthenticationRequestRequired,
issuerUri,
metadataExchangeUri,
nextSigningCertificate,
passiveSignInUri,
passwordResetUri,
preferredAuthenticationProtocol,
promptLoginBehavior,
signOutUri,
signingCertificate,
signingCertificateUpdateStatus
FROM entra_id.domains.federation_configuration
WHERE domain_id = '{{ domain_id }}' -- required
AND internal_domain_federation_id = '{{ internal_domain_federation_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Read the properties of the internalDomainFederation objects for the domain. This API returns only one object in the collection.

```sql
SELECT
id,
activeSignInUri,
displayName,
federatedIdpMfaBehavior,
isSignedAuthenticationRequestRequired,
issuerUri,
metadataExchangeUri,
nextSigningCertificate,
passiveSignInUri,
passwordResetUri,
preferredAuthenticationProtocol,
promptLoginBehavior,
signOutUri,
signingCertificate,
signingCertificateUpdateStatus
FROM entra_id.domains.federation_configuration
WHERE domain_id = '{{ domain_id }}' -- required
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

Create a new internalDomainFederation object.

```sql
INSERT INTO entra_id.domains.federation_configuration (
id,
displayName,
issuerUri,
metadataExchangeUri,
passiveSignInUri,
preferredAuthenticationProtocol,
signingCertificate,
activeSignInUri,
federatedIdpMfaBehavior,
isSignedAuthenticationRequestRequired,
nextSigningCertificate,
passwordResetUri,
promptLoginBehavior,
signingCertificateUpdateStatus,
signOutUri,
domain_id
)
SELECT 
'{{ id }}',
'{{ displayName }}',
'{{ issuerUri }}',
'{{ metadataExchangeUri }}',
'{{ passiveSignInUri }}',
'{{ preferredAuthenticationProtocol }}',
'{{ signingCertificate }}',
'{{ activeSignInUri }}',
'{{ federatedIdpMfaBehavior }}',
{{ isSignedAuthenticationRequestRequired }},
'{{ nextSigningCertificate }}',
'{{ passwordResetUri }}',
'{{ promptLoginBehavior }}',
'{{ signingCertificateUpdateStatus }}',
'{{ signOutUri }}',
'{{ domain_id }}'
RETURNING
id,
activeSignInUri,
displayName,
federatedIdpMfaBehavior,
isSignedAuthenticationRequestRequired,
issuerUri,
metadataExchangeUri,
nextSigningCertificate,
passiveSignInUri,
passwordResetUri,
preferredAuthenticationProtocol,
promptLoginBehavior,
signOutUri,
signingCertificate,
signingCertificateUpdateStatus
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: federation_configuration
  props:
    - name: domain_id
      value: "{{ domain_id }}"
      description: Required parameter for the federation_configuration resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the identity provider.
    - name: issuerUri
      value: "{{ issuerUri }}"
      description: |
        Issuer URI of the federation server.
    - name: metadataExchangeUri
      value: "{{ metadataExchangeUri }}"
      description: |
        URI of the metadata exchange endpoint used for authentication from rich client applications.
    - name: passiveSignInUri
      value: "{{ passiveSignInUri }}"
      description: |
        URI that web-based clients are directed to when signing in to Microsoft Entra services.
    - name: preferredAuthenticationProtocol
      value: "{{ preferredAuthenticationProtocol }}"
      description: |
        Preferred authentication protocol. The possible values are: wsFed, saml, unknownFutureValue.
    - name: signingCertificate
      value: "{{ signingCertificate }}"
      description: |
        Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Microsoft Entra ID updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Microsoft Entra ID monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.
    - name: activeSignInUri
      value: "{{ activeSignInUri }}"
      description: |
        URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Microsoft Entra ID. Corresponds to the ActiveLogOnUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.
    - name: federatedIdpMfaBehavior
      value: "{{ federatedIdpMfaBehavior }}"
      description: |
        Determines whether Microsoft Entra ID accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.
    - name: isSignedAuthenticationRequestRequired
      value: {{ isSignedAuthenticationRequestRequired }}
      description: |
        If true, when SAML authentication requests are sent to the federated SAML IdP, Microsoft Entra ID will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP aren't signed.
    - name: nextSigningCertificate
      value: "{{ nextSigningCertificate }}"
      description: |
        Fallback token signing certificate that can also be used to sign tokens, for example when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.
    - name: passwordResetUri
      value: "{{ passwordResetUri }}"
    - name: promptLoginBehavior
      value: "{{ promptLoginBehavior }}"
      description: |
        Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.
    - name: signingCertificateUpdateStatus
      value: "{{ signingCertificateUpdateStatus }}"
      description: |
        Provides status and timestamp of the last update of the signing certificate.
    - name: signOutUri
      value: "{{ signOutUri }}"
      description: |
        URI that clients are redirected to when they sign out of Microsoft Entra services. Corresponds to the LogOffUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.
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

Update the properties of an internalDomainFederation object.

```sql
UPDATE entra_id.domains.federation_configuration
SET 
id = '{{ id }}',
displayName = '{{ displayName }}',
issuerUri = '{{ issuerUri }}',
metadataExchangeUri = '{{ metadataExchangeUri }}',
passiveSignInUri = '{{ passiveSignInUri }}',
preferredAuthenticationProtocol = '{{ preferredAuthenticationProtocol }}',
signingCertificate = '{{ signingCertificate }}',
activeSignInUri = '{{ activeSignInUri }}',
federatedIdpMfaBehavior = '{{ federatedIdpMfaBehavior }}',
isSignedAuthenticationRequestRequired = {{ isSignedAuthenticationRequestRequired }},
nextSigningCertificate = '{{ nextSigningCertificate }}',
passwordResetUri = '{{ passwordResetUri }}',
promptLoginBehavior = '{{ promptLoginBehavior }}',
signingCertificateUpdateStatus = '{{ signingCertificateUpdateStatus }}',
signOutUri = '{{ signOutUri }}'
WHERE 
domain_id = '{{ domain_id }}' --required
AND internal_domain_federation_id = '{{ internal_domain_federation_id }}' --required
RETURNING
id,
activeSignInUri,
displayName,
federatedIdpMfaBehavior,
isSignedAuthenticationRequestRequired,
issuerUri,
metadataExchangeUri,
nextSigningCertificate,
passiveSignInUri,
passwordResetUri,
preferredAuthenticationProtocol,
promptLoginBehavior,
signOutUri,
signingCertificate,
signingCertificateUpdateStatus;
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

Delete an internalDomainFederation object.

```sql
DELETE FROM entra_id.domains.federation_configuration
WHERE domain_id = '{{ domain_id }}' --required
AND internal_domain_federation_id = '{{ internal_domain_federation_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
