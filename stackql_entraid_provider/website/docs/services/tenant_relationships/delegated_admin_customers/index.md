--- 
title: delegated_admin_customers
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_admin_customers
  - tenant_relationships
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

Creates, updates, deletes, gets or lists a <code>delegated_admin_customers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delegated_admin_customers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.tenant_relationships.delegated_admin_customers" /></td></tr>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The Microsoft Entra ID display name of the customer tenant. Read-only. Supports $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceManagementDetails" /></td>
    <td><code>array</code></td>
    <td>Contains the management details of a service in the customer tenant that's managed by delegated administration.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Microsoft Entra ID-assigned tenant ID of the customer. Read-only.</td>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The Microsoft Entra ID display name of the customer tenant. Read-only. Supports $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceManagementDetails" /></td>
    <td><code>array</code></td>
    <td>Contains the management details of a service in the customer tenant that's managed by delegated administration.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The Microsoft Entra ID-assigned tenant ID of the customer. Read-only.</td>
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
    <td><a href="#parameter-delegated_admin_customer_id"><code>delegated_admin_customer_id</code></a></td>
    <td></td>
    <td>Read the properties of a delegatedAdminCustomer object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the delegatedAdminCustomer objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-delegated_admin_customer_id"><code>delegated_admin_customer_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-delegated_admin_customer_id"><code>delegated_admin_customer_id</code></a></td>
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
<tr id="parameter-delegated_admin_customer_id">
    <td><CopyableCode code="delegated_admin_customer_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of delegatedAdminCustomer</td>
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

Read the properties of a delegatedAdminCustomer object.

```sql
SELECT
id,
displayName,
serviceManagementDetails,
tenantId
FROM entra_id.tenant_relationships.delegated_admin_customers
WHERE delegated_admin_customer_id = '{{ delegated_admin_customer_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the delegatedAdminCustomer objects and their properties.

```sql
SELECT
id,
displayName,
serviceManagementDetails,
tenantId
FROM entra_id.tenant_relationships.delegated_admin_customers
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
INSERT INTO entra_id.tenant_relationships.delegated_admin_customers (
id,
displayName,
tenantId,
serviceManagementDetails
)
SELECT 
'{{ id }}',
'{{ displayName }}',
'{{ tenantId }}',
'{{ serviceManagementDetails }}'
RETURNING
id,
displayName,
serviceManagementDetails,
tenantId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: delegated_admin_customers
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The Microsoft Entra ID display name of the customer tenant. Read-only. Supports $orderby.
    - name: tenantId
      value: "{{ tenantId }}"
      description: |
        The Microsoft Entra ID-assigned tenant ID of the customer. Read-only.
    - name: serviceManagementDetails
      description: |
        Contains the management details of a service in the customer tenant that's managed by delegated administration.
      value:
        - id: "{{ id }}"
          serviceManagementUrl: "{{ serviceManagementUrl }}"
          serviceName: "{{ serviceName }}"
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
UPDATE entra_id.tenant_relationships.delegated_admin_customers
SET 
id = '{{ id }}',
displayName = '{{ displayName }}',
tenantId = '{{ tenantId }}',
serviceManagementDetails = '{{ serviceManagementDetails }}'
WHERE 
delegated_admin_customer_id = '{{ delegated_admin_customer_id }}' --required
RETURNING
id,
displayName,
serviceManagementDetails,
tenantId;
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

No description available.

```sql
DELETE FROM entra_id.tenant_relationships.delegated_admin_customers
WHERE delegated_admin_customer_id = '{{ delegated_admin_customer_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
