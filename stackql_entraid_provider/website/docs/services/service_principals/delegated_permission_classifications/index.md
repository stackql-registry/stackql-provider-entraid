--- 
title: delegated_permission_classifications
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_permission_classifications
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

Creates, updates, deletes, gets or lists a <code>delegated_permission_classifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delegated_permission_classifications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.delegated_permission_classifications" /></td></tr>
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
    <td><CopyableCode code="classification" /></td>
    <td><code></code></td>
    <td>The classification value. Possible values: low, medium (preview), high (preview). Doesn't support $filter.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier (id) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Required on create. Doesn't support $filter.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionName" /></td>
    <td><code>string</code></td>
    <td>The claim value (value) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Doesn't support $filter.</td>
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
    <td><CopyableCode code="classification" /></td>
    <td><code></code></td>
    <td>The classification value. Possible values: low, medium (preview), high (preview). Doesn't support $filter.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier (id) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Required on create. Doesn't support $filter.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionName" /></td>
    <td><code>string</code></td>
    <td>The claim value (value) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Doesn't support $filter.</td>
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
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-delegated_permission_classification_id"><code>delegated_permission_classification_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Retrieve the list of delegatedPermissionClassification currently configured for the delegated permissions exposed by an API.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Classify a delegated permission by adding a delegatedPermissionClassification to the servicePrincipal representing the API.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-delegated_permission_classification_id"><code>delegated_permission_classification_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-delegated_permission_classification_id"><code>delegated_permission_classification_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes a delegatedPermissionClassification which had previously been set for a delegated permission.</td>
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
<tr id="parameter-delegated_permission_classification_id">
    <td><CopyableCode code="delegated_permission_classification_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of delegatedPermissionClassification</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieved navigation property

```sql
SELECT
id,
classification,
permissionId,
permissionName
FROM entra_id.service_principals.delegated_permission_classifications
WHERE service_principal_id = '{{ service_principal_id }}' -- required
AND delegated_permission_classification_id = '{{ delegated_permission_classification_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve the list of delegatedPermissionClassification currently configured for the delegated permissions exposed by an API.

```sql
SELECT
id,
classification,
permissionId,
permissionName
FROM entra_id.service_principals.delegated_permission_classifications
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

Classify a delegated permission by adding a delegatedPermissionClassification to the servicePrincipal representing the API.

```sql
INSERT INTO entra_id.service_principals.delegated_permission_classifications (
id,
classification,
permissionId,
permissionName,
service_principal_id
)
SELECT 
'{{ id }}',
'{{ classification }}',
'{{ permissionId }}',
'{{ permissionName }}',
'{{ service_principal_id }}'
RETURNING
id,
classification,
permissionId,
permissionName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: delegated_permission_classifications
  props:
    - name: service_principal_id
      value: "{{ service_principal_id }}"
      description: Required parameter for the delegated_permission_classifications resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: classification
      value: "{{ classification }}"
      description: |
        The classification value. Possible values: low, medium (preview), high (preview). Doesn't support $filter.
    - name: permissionId
      value: "{{ permissionId }}"
      description: |
        The unique identifier (id) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Required on create. Doesn't support $filter.
    - name: permissionName
      value: "{{ permissionName }}"
      description: |
        The claim value (value) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Doesn't support $filter.
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
UPDATE entra_id.service_principals.delegated_permission_classifications
SET 
id = '{{ id }}',
classification = '{{ classification }}',
permissionId = '{{ permissionId }}',
permissionName = '{{ permissionName }}'
WHERE 
service_principal_id = '{{ service_principal_id }}' --required
AND delegated_permission_classification_id = '{{ delegated_permission_classification_id }}' --required
RETURNING
id,
classification,
permissionId,
permissionName;
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

Deletes a delegatedPermissionClassification which had previously been set for a delegated permission.

```sql
DELETE FROM entra_id.service_principals.delegated_permission_classifications
WHERE service_principal_id = '{{ service_principal_id }}' --required
AND delegated_permission_classification_id = '{{ delegated_permission_classification_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
