--- 
title: tenant_relationships
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_relationships
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

Creates, updates, deletes, gets or lists a <code>tenant_relationships</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tenant_relationships" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.tenant_relationships.tenant_relationships" /></td></tr>
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
    <td><CopyableCode code="delegatedAdminCustomers" /></td>
    <td><code>array</code></td>
    <td>The customer who has a delegated admin relationship with a Microsoft partner.</td>
</tr>
<tr>
    <td><CopyableCode code="delegatedAdminRelationships" /></td>
    <td><code>array</code></td>
    <td>The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="multiTenantOrganization" /></td>
    <td><code>object</code></td>
    <td>Defines an organization with more than one instance of Microsoft Entra ID. (x-ms-discriminator-value: #microsoft.graph.multiTenantOrganization, title: entity)</td>
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
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
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

Retrieved entity

```sql
SELECT
delegatedAdminCustomers,
delegatedAdminRelationships,
multiTenantOrganization
FROM entra_id.tenant_relationships.tenant_relationships
;
```
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
UPDATE entra_id.tenant_relationships.tenant_relationships
SET 
delegatedAdminCustomers = '{{ delegatedAdminCustomers }}',
delegatedAdminRelationships = '{{ delegatedAdminRelationships }}',
multiTenantOrganization = '{{ multiTenantOrganization }}'
RETURNING
delegatedAdminCustomers,
delegatedAdminRelationships,
multiTenantOrganization;
```
</TabItem>
</Tabs>
