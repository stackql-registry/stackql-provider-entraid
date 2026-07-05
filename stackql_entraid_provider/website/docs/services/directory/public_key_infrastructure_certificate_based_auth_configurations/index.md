--- 
title: public_key_infrastructure_certificate_based_auth_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - public_key_infrastructure_certificate_based_auth_configurations
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

Creates, updates, deletes, gets or lists a <code>public_key_infrastructure_certificate_based_auth_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="public_key_infrastructure_certificate_based_auth_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations" /></td></tr>
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
    <td><CopyableCode code="certificateAuthorities" /></td>
    <td><code>array</code></td>
    <td>The collection of certificate authorities contained in this public key infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the object. Maximum length is 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the object was created or last modified. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of any asynchronous jobs runs on the object which can be upload or delete.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>The status details of the upload/deleted operation of PKI (Public Key Infrastructure).</td>
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
    <td><CopyableCode code="certificateAuthorities" /></td>
    <td><code>array</code></td>
    <td>The collection of certificate authorities contained in this public key infrastructure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the object. Maximum length is 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the object was created or last modified. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of any asynchronous jobs runs on the object which can be upload or delete.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>The status details of the upload/deleted operation of PKI (Public Key Infrastructure).</td>
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
    <td><a href="#parameter-certificate_based_auth_pki_id"><code>certificate_based_auth_pki_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a certificateBasedAuthPki object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the certificateBasedAuthPki objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new certificateBasedAuthPki object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-certificate_based_auth_pki_id"><code>certificate_based_auth_pki_id</code></a></td>
    <td></td>
    <td>Update the properties of a certificateBasedAuthPki object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-certificate_based_auth_pki_id"><code>certificate_based_auth_pki_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a certificateBasedAuthPki object.</td>
</tr>
<tr>
    <td><a href="#upload"><CopyableCode code="upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-certificate_based_auth_pki_id"><code>certificate_based_auth_pki_id</code></a></td>
    <td></td>
    <td>Append additional certificate authority details to a certificateBasedAuthPki resource. Only one operation can run at a time and this operation can take up to 30 minutes to complete. To know whether another upload is in progress, call the Get certificateBasedAuthPki. The status property will have the value running.</td>
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
<tr id="parameter-certificate_based_auth_pki_id">
    <td><CopyableCode code="certificate_based_auth_pki_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of certificateBasedAuthPki</td>
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

Read the properties and relationships of a certificateBasedAuthPki object.

```sql
SELECT
id,
certificateAuthorities,
deletedDateTime,
displayName,
lastModifiedDateTime,
status,
statusDetails
FROM entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations
WHERE certificate_based_auth_pki_id = '{{ certificate_based_auth_pki_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the certificateBasedAuthPki objects and their properties.

```sql
SELECT
id,
certificateAuthorities,
deletedDateTime,
displayName,
lastModifiedDateTime,
status,
statusDetails
FROM entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations
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

Create a new certificateBasedAuthPki object.

```sql
INSERT INTO entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations (
id,
deletedDateTime,
displayName,
lastModifiedDateTime,
status,
statusDetails,
certificateAuthorities
)
SELECT 
'{{ id }}',
'{{ deletedDateTime }}',
'{{ displayName }}',
'{{ lastModifiedDateTime }}',
'{{ status }}',
'{{ statusDetails }}',
'{{ certificateAuthorities }}'
RETURNING
id,
certificateAuthorities,
deletedDateTime,
displayName,
lastModifiedDateTime,
status,
statusDetails
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: public_key_infrastructure_certificate_based_auth_configurations
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The name of the object. Maximum length is 256 characters.
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        The date and time when the object was created or last modified.
    - name: status
      value: "{{ status }}"
      description: |
        The status of any asynchronous jobs runs on the object which can be upload or delete.
    - name: statusDetails
      value: "{{ statusDetails }}"
      description: |
        The status details of the upload/deleted operation of PKI (Public Key Infrastructure).
    - name: certificateAuthorities
      description: |
        The collection of certificate authorities contained in this public key infrastructure resource.
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
          certificate: "{{ certificate }}"
          certificateAuthorityType: "{{ certificateAuthorityType }}"
          certificateRevocationListUrl: "{{ certificateRevocationListUrl }}"
          createdDateTime: "{{ createdDateTime }}"
          deltaCertificateRevocationListUrl: "{{ deltaCertificateRevocationListUrl }}"
          displayName: "{{ displayName }}"
          expirationDateTime: "{{ expirationDateTime }}"
          isIssuerHintEnabled: {{ isIssuerHintEnabled }}
          issuer: "{{ issuer }}"
          issuerSubjectKeyIdentifier: "{{ issuerSubjectKeyIdentifier }}"
          thumbprint: "{{ thumbprint }}"
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

Update the properties of a certificateBasedAuthPki object.

```sql
UPDATE entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations
SET 
id = '{{ id }}',
deletedDateTime = '{{ deletedDateTime }}',
displayName = '{{ displayName }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
status = '{{ status }}',
statusDetails = '{{ statusDetails }}',
certificateAuthorities = '{{ certificateAuthorities }}'
WHERE 
certificate_based_auth_pki_id = '{{ certificate_based_auth_pki_id }}' --required
RETURNING
id,
certificateAuthorities,
deletedDateTime,
displayName,
lastModifiedDateTime,
status,
statusDetails;
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

Delete a certificateBasedAuthPki object.

```sql
DELETE FROM entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations
WHERE certificate_based_auth_pki_id = '{{ certificate_based_auth_pki_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upload"
    values={[
        { label: 'upload', value: 'upload' }
    ]}
>
<TabItem value="upload">

Append additional certificate authority details to a certificateBasedAuthPki resource. Only one operation can run at a time and this operation can take up to 30 minutes to complete. To know whether another upload is in progress, call the Get certificateBasedAuthPki. The status property will have the value running.

```sql
EXEC entra_id.directory.public_key_infrastructure_certificate_based_auth_configurations.upload 
@certificate_based_auth_pki_id='{{ certificate_based_auth_pki_id }}' --required 
@@json=
'{
"uploadUrl": "{{ uploadUrl }}", 
"sha256FileHash": "{{ sha256FileHash }}"
}'
;
```
</TabItem>
</Tabs>
