--- 
title: public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities
hide_title: false
hide_table_of_contents: false
keywords:
  - public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities
  - directory
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

Creates, updates, deletes, gets or lists a <code>public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="certificate" /></td>
    <td><code>string (base64url)</code></td>
    <td>The public key of the certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateAuthorityType" /></td>
    <td><code></code></td>
    <td>The type of certificate authority. The possible values are: root, intermediate, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="certificateRevocationListUrl" /></td>
    <td><code>string</code></td>
    <td>The URL to check if the certificate is revoked.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the certificate authority was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deltaCertificateRevocationListUrl" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the certificate authority expires. Supports $filter (eq) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isIssuerHintEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the certificate picker presents the certificate authority to the user to use for authentication. Default value is false. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The issuer of the certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="issuerSubjectKeyIdentifier" /></td>
    <td><code>string</code></td>
    <td>The subject key identifier of certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>The thumbprint of certificate authority certificate. Supports $filter (eq, startswith).</td>
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
    <td><CopyableCode code="certificate" /></td>
    <td><code>string (base64url)</code></td>
    <td>The public key of the certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateAuthorityType" /></td>
    <td><code></code></td>
    <td>The type of certificate authority. The possible values are: root, intermediate, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="certificateRevocationListUrl" /></td>
    <td><code>string</code></td>
    <td>The URL to check if the certificate is revoked.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the certificate authority was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deltaCertificateRevocationListUrl" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the certificate authority expires. Supports $filter (eq) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="isIssuerHintEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the certificate picker presents the certificate authority to the user to use for authentication. Default value is false. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The issuer of the certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="issuerSubjectKeyIdentifier" /></td>
    <td><code>string</code></td>
    <td>The subject key identifier of certificate authority.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>The thumbprint of certificate authority certificate. Supports $filter (eq, startswith).</td>
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
    <td><a href="#parameter-certificateBasedAuthPki-id"><code>certificateBasedAuthPki-id</code></a>, <a href="#parameter-certificateAuthorityDetail-id"><code>certificateAuthorityDetail-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The collection of certificate authorities contained in this public key infrastructure resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-certificateBasedAuthPki-id"><code>certificateBasedAuthPki-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of the certificateAuthorityDetail objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-certificateBasedAuthPki-id"><code>certificateBasedAuthPki-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new certificateAuthorityDetail object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-certificateBasedAuthPki-id"><code>certificateBasedAuthPki-id</code></a>, <a href="#parameter-certificateAuthorityDetail-id"><code>certificateAuthorityDetail-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-certificateBasedAuthPki-id"><code>certificateBasedAuthPki-id</code></a>, <a href="#parameter-certificateAuthorityDetail-id"><code>certificateAuthorityDetail-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a certificateAuthorityDetail object.</td>
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
<tr id="parameter-certificateAuthorityDetail-id">
    <td><CopyableCode code="certificateAuthorityDetail-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of certificateAuthorityDetail</td>
</tr>
<tr id="parameter-certificateBasedAuthPki-id">
    <td><CopyableCode code="certificateBasedAuthPki-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of certificateBasedAuthPki</td>
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

The collection of certificate authorities contained in this public key infrastructure resource.

```sql
SELECT
id,
@odata.type,
certificate,
certificateAuthorityType,
certificateRevocationListUrl,
createdDateTime,
deletedDateTime,
deltaCertificateRevocationListUrl,
displayName,
expirationDateTime,
isIssuerHintEnabled,
issuer,
issuerSubjectKeyIdentifier,
thumbprint
FROM entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities
WHERE certificateBasedAuthPki-id = '{{ certificateBasedAuthPki-id }}' -- required
AND certificateAuthorityDetail-id = '{{ certificateAuthorityDetail-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of the certificateAuthorityDetail objects and their properties.

```sql
SELECT
id,
@odata.type,
certificate,
certificateAuthorityType,
certificateRevocationListUrl,
createdDateTime,
deletedDateTime,
deltaCertificateRevocationListUrl,
displayName,
expirationDateTime,
isIssuerHintEnabled,
issuer,
issuerSubjectKeyIdentifier,
thumbprint
FROM entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities
WHERE certificateBasedAuthPki-id = '{{ certificateBasedAuthPki-id }}' -- required
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

Create a new certificateAuthorityDetail object.

```sql
INSERT INTO entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities (
id,
@odata.type,
deletedDateTime,
certificate,
certificateAuthorityType,
certificateRevocationListUrl,
createdDateTime,
deltaCertificateRevocationListUrl,
displayName,
expirationDateTime,
isIssuerHintEnabled,
issuer,
issuerSubjectKeyIdentifier,
thumbprint,
certificateBasedAuthPki-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
'{{ certificate }}',
'{{ certificateAuthorityType }}',
'{{ certificateRevocationListUrl }}',
'{{ createdDateTime }}',
'{{ deltaCertificateRevocationListUrl }}',
'{{ displayName }}',
'{{ expirationDateTime }}',
{{ isIssuerHintEnabled }},
'{{ issuer }}',
'{{ issuerSubjectKeyIdentifier }}',
'{{ thumbprint }}',
'{{ certificateBasedAuthPki-id }}'
RETURNING
id,
@odata.type,
certificate,
certificateAuthorityType,
certificateRevocationListUrl,
createdDateTime,
deletedDateTime,
deltaCertificateRevocationListUrl,
displayName,
expirationDateTime,
isIssuerHintEnabled,
issuer,
issuerSubjectKeyIdentifier,
thumbprint
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities
  props:
    - name: certificateBasedAuthPki-id
      value: "{{ certificateBasedAuthPki-id }}"
      description: Required parameter for the public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities resource.
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
    - name: certificate
      value: "{{ certificate }}"
      description: |
        The public key of the certificate authority.
    - name: certificateAuthorityType
      value: "{{ certificateAuthorityType }}"
      description: |
        The type of certificate authority. The possible values are: root, intermediate, unknownFutureValue. Supports $filter (eq).
    - name: certificateRevocationListUrl
      value: "{{ certificateRevocationListUrl }}"
      description: |
        The URL to check if the certificate is revoked.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The date and time when the certificate authority was created.
    - name: deltaCertificateRevocationListUrl
      value: "{{ deltaCertificateRevocationListUrl }}"
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the certificate authority.
    - name: expirationDateTime
      value: "{{ expirationDateTime }}"
      description: |
        The date and time when the certificate authority expires. Supports $filter (eq) and $orderby.
    - name: isIssuerHintEnabled
      value: {{ isIssuerHintEnabled }}
      description: |
        Indicates whether the certificate picker presents the certificate authority to the user to use for authentication. Default value is false. Optional.
    - name: issuer
      value: "{{ issuer }}"
      description: |
        The issuer of the certificate authority.
    - name: issuerSubjectKeyIdentifier
      value: "{{ issuerSubjectKeyIdentifier }}"
      description: |
        The subject key identifier of certificate authority.
    - name: thumbprint
      value: "{{ thumbprint }}"
      description: |
        The thumbprint of certificate authority certificate. Supports $filter (eq, startswith).
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

No description available.

```sql
UPDATE entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
certificate = '{{ certificate }}',
certificateAuthorityType = '{{ certificateAuthorityType }}',
certificateRevocationListUrl = '{{ certificateRevocationListUrl }}',
createdDateTime = '{{ createdDateTime }}',
deltaCertificateRevocationListUrl = '{{ deltaCertificateRevocationListUrl }}',
displayName = '{{ displayName }}',
expirationDateTime = '{{ expirationDateTime }}',
isIssuerHintEnabled = {{ isIssuerHintEnabled }},
issuer = '{{ issuer }}',
issuerSubjectKeyIdentifier = '{{ issuerSubjectKeyIdentifier }}',
thumbprint = '{{ thumbprint }}'
WHERE 
certificateBasedAuthPki-id = '{{ certificateBasedAuthPki-id }}' --required
AND certificateAuthorityDetail-id = '{{ certificateAuthorityDetail-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
certificate,
certificateAuthorityType,
certificateRevocationListUrl,
createdDateTime,
deletedDateTime,
deltaCertificateRevocationListUrl,
displayName,
expirationDateTime,
isIssuerHintEnabled,
issuer,
issuerSubjectKeyIdentifier,
thumbprint;
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

Delete a certificateAuthorityDetail object.

```sql
DELETE FROM entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations_certificate_authorities
WHERE certificateBasedAuthPki-id = '{{ certificateBasedAuthPki-id }}' --required
AND certificateAuthorityDetail-id = '{{ certificateAuthorityDetail-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
