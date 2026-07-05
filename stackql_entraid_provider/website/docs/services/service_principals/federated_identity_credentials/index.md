--- 
title: federated_identity_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - federated_identity_credentials
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

Creates, updates, deletes, gets or lists a <code>federated_identity_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="federated_identity_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.federated_identity_credentials" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. The string is immutable after it's created. Alternate key. Required. Not nullable. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="audiences" /></td>
    <td><code>array</code></td>
    <td>The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Microsoft Entra ID. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Microsoft Entra ID in your external identity provider and has no fixed value across identity providers - you might need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The unvalidated description of the federated identity credential, provided by the user. It has a limit of 600 characters. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The URL of the external identity provider, which must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique within the app. It has a limit of 600 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td>Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format; each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Microsoft Entra ID. The combination of issuer and subject must be unique within the app. It has a limit of 600 characters. Supports $filter (eq).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_2">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. The string is immutable after it's created. Alternate key. Required. Not nullable. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="audiences" /></td>
    <td><code>array</code></td>
    <td>The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Microsoft Entra ID. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Microsoft Entra ID in your external identity provider and has no fixed value across identity providers - you might need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The unvalidated description of the federated identity credential, provided by the user. It has a limit of 600 characters. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The URL of the external identity provider, which must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique within the app. It has a limit of 600 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td>Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format; each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Microsoft Entra ID. The combination of issuer and subject must be unique within the app. It has a limit of 600 characters. Supports $filter (eq).</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. The string is immutable after it's created. Alternate key. Required. Not nullable. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="audiences" /></td>
    <td><code>array</code></td>
    <td>The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Microsoft Entra ID. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Microsoft Entra ID in your external identity provider and has no fixed value across identity providers - you might need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The unvalidated description of the federated identity credential, provided by the user. It has a limit of 600 characters. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>The URL of the external identity provider, which must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique within the app. It has a limit of 600 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td>Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format; each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Microsoft Entra ID. The combination of issuer and subject must be unique within the app. It has a limit of 600 characters. Supports $filter (eq).</td>
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
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-federated_identity_credential_id"><code>federated_identity_credential_id</code></a></td>
    <td></td>
    <td>Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-federated_identity_credential_id"><code>federated_identity_credential_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-federated_identity_credential_id"><code>federated_identity_credential_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
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
<tr id="parameter-federated_identity_credential_id">
    <td><CopyableCode code="federated_identity_credential_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of federatedIdentityCredential</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Alternate key of federatedIdentityCredential</td>
</tr>
<tr id="parameter-service_principal_id">
    <td><CopyableCode code="service_principal_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
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

Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).

```sql
SELECT
id,
name,
audiences,
description,
issuer,
subject
FROM entra_id.service_principals.federated_identity_credentials
WHERE service_principal_id = '{{ service_principal_id }}' -- required
AND federated_identity_credential_id = '{{ federated_identity_credential_id }}' -- required
;
```
</TabItem>
<TabItem value="get_2">

Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).

```sql
SELECT
id,
name,
audiences,
description,
issuer,
subject
FROM entra_id.service_principals.federated_identity_credentials
WHERE service_principal_id = '{{ service_principal_id }}' -- required
AND name = '{{ name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Federated identities for a specific type of service principal - managed identity. Supports $expand and $filter (/$count eq 0, /$count ne 0).

```sql
SELECT
id,
name,
audiences,
description,
issuer,
subject
FROM entra_id.service_principals.federated_identity_credentials
WHERE service_principal_id = '{{ service_principal_id }}' -- required
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

No description available.

```sql
INSERT INTO entra_id.service_principals.federated_identity_credentials (
id,
audiences,
description,
issuer,
name,
subject,
service_principal_id
)
SELECT 
'{{ id }}',
'{{ audiences }}',
'{{ description }}',
'{{ issuer }}',
'{{ name }}',
'{{ subject }}',
'{{ service_principal_id }}'
RETURNING
id,
name,
audiences,
description,
issuer,
subject
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: federated_identity_credentials
  props:
    - name: service_principal_id
      value: "{{ service_principal_id }}"
      description: Required parameter for the federated_identity_credentials resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: audiences
      value:
        - "{{ audiences }}"
      description: |
        The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Microsoft Entra ID. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Microsoft Entra ID in your external identity provider and has no fixed value across identity providers - you might need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.
    - name: description
      value: "{{ description }}"
      description: |
        The unvalidated description of the federated identity credential, provided by the user. It has a limit of 600 characters. Optional.
    - name: issuer
      value: "{{ issuer }}"
      description: |
        The URL of the external identity provider, which must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique within the app. It has a limit of 600 characters. Required.
    - name: name
      value: "{{ name }}"
      description: |
        The unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. The string is immutable after it's created. Alternate key. Required. Not nullable. Supports $filter (eq).
    - name: subject
      value: "{{ subject }}"
      description: |
        Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format; each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Microsoft Entra ID. The combination of issuer and subject must be unique within the app. It has a limit of 600 characters. Supports $filter (eq).
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

No description available.

```sql
UPDATE entra_id.service_principals.federated_identity_credentials
SET 
id = '{{ id }}',
audiences = '{{ audiences }}',
description = '{{ description }}',
issuer = '{{ issuer }}',
name = '{{ name }}',
subject = '{{ subject }}'
WHERE 
service_principal_id = '{{ service_principal_id }}' --required
AND federated_identity_credential_id = '{{ federated_identity_credential_id }}' --required
RETURNING
id,
name,
audiences,
description,
issuer,
subject;
```
</TabItem>
<TabItem value="update_2">

No description available.

```sql
UPDATE entra_id.service_principals.federated_identity_credentials
SET 
id = '{{ id }}',
audiences = '{{ audiences }}',
description = '{{ description }}',
issuer = '{{ issuer }}',
name = '{{ name }}',
subject = '{{ subject }}'
WHERE 
service_principal_id = '{{ service_principal_id }}' --required
AND name = '{{ name }}' --required
RETURNING
id,
name,
audiences,
description,
issuer,
subject;
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

No description available.

```sql
DELETE FROM entra_id.service_principals.federated_identity_credentials
WHERE service_principal_id = '{{ service_principal_id }}' --required
AND federated_identity_credential_id = '{{ federated_identity_credential_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

No description available.

```sql
DELETE FROM entra_id.service_principals.federated_identity_credentials
WHERE service_principal_id = '{{ service_principal_id }}' --required
AND name = '{{ name }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
