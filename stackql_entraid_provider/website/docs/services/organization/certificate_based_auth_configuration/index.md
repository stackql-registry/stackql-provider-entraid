--- 
title: certificate_based_auth_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_based_auth_configuration
  - organization
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

Creates, updates, deletes, gets or lists a <code>certificate_based_auth_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_based_auth_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.organization.certificate_based_auth_configuration" /></td></tr>
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
    <td>Collection of certificate authorities which creates a trusted certificate chain.</td>
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
    <td>Collection of certificate authorities which creates a trusted certificate chain.</td>
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
    <td><a href="#parameter-organization_id"><code>organization_id</code></a>, <a href="#parameter-certificate_based_auth_configuration_id"><code>certificate_based_auth_configuration_id</code></a></td>
    <td></td>
    <td>Get the properties of a certificateBasedAuthConfiguration object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a></td>
    <td></td>
    <td>Get a list of certificateBasedAuthConfiguration objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a></td>
    <td></td>
    <td>Create a new certificateBasedAuthConfiguration object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-organization_id"><code>organization_id</code></a>, <a href="#parameter-certificate_based_auth_configuration_id"><code>certificate_based_auth_configuration_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a certificateBasedAuthConfiguration object.</td>
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
<tr id="parameter-certificate_based_auth_configuration_id">
    <td><CopyableCode code="certificate_based_auth_configuration_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of certificateBasedAuthConfiguration</td>
</tr>
<tr id="parameter-organization_id">
    <td><CopyableCode code="organization_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of organization</td>
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

Get the properties of a certificateBasedAuthConfiguration object.

```sql
SELECT
id,
certificateAuthorities
FROM entra_id.organization.certificate_based_auth_configuration
WHERE organization_id = '{{ organization_id }}' -- required
AND certificate_based_auth_configuration_id = '{{ certificate_based_auth_configuration_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of certificateBasedAuthConfiguration objects.

```sql
SELECT
id,
certificateAuthorities
FROM entra_id.organization.certificate_based_auth_configuration
WHERE organization_id = '{{ organization_id }}' -- required
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

Create a new certificateBasedAuthConfiguration object.

```sql
INSERT INTO entra_id.organization.certificate_based_auth_configuration (
id,
certificateAuthorities,
organization_id
)
SELECT 
'{{ id }}',
'{{ certificateAuthorities }}',
'{{ organization_id }}'
RETURNING
id,
certificateAuthorities
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: certificate_based_auth_configuration
  props:
    - name: organization_id
      value: "{{ organization_id }}"
      description: Required parameter for the certificate_based_auth_configuration resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: certificateAuthorities
      description: |
        Collection of certificate authorities which creates a trusted certificate chain.
      value:
        - certificate: "{{ certificate }}"
          certificateRevocationListUrl: "{{ certificateRevocationListUrl }}"
          deltaCertificateRevocationListUrl: "{{ deltaCertificateRevocationListUrl }}"
          isRootAuthority: {{ isRootAuthority }}
          issuer: "{{ issuer }}"
          issuerSki: "{{ issuerSki }}"
`}</CodeBlock>

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

Delete a certificateBasedAuthConfiguration object.

```sql
DELETE FROM entra_id.organization.certificate_based_auth_configuration
WHERE organization_id = '{{ organization_id }}' --required
AND certificate_based_auth_configuration_id = '{{ certificate_based_auth_configuration_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
