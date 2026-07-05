--- 
title: risk_prevention
hide_title: false
hide_table_of_contents: false
keywords:
  - risk_prevention
  - identity
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

Creates, updates, deletes, gets or lists a <code>risk_prevention</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="risk_prevention" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.risk_prevention" /></td></tr>
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
    <td><CopyableCode code="fraudProtectionProviders" /></td>
    <td><code>array</code></td>
    <td>Represents entry point for fraud protection provider configurations for Microsoft Entra External ID tenants.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallProviders" /></td>
    <td><code>array</code></td>
    <td>Collection of WAF provider configurations registered in the External ID tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallVerifications" /></td>
    <td><code>array</code></td>
    <td>Collection of verification operations performed for domains or hosts with WAF providers registered in the External ID tenant.</td>
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
    <td>Represents the entry point for fraud and risk prevention configurations in Microsoft Entra External ID, including third-party provider settings.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Represents the entry point for fraud and risk prevention configurations in Microsoft Entra External ID, including third-party provider settings.

```sql
SELECT
fraudProtectionProviders,
webApplicationFirewallProviders,
webApplicationFirewallVerifications
FROM entra_id.identity.risk_prevention
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
UPDATE entra_id.identity.risk_prevention
SET 
fraudProtectionProviders = '{{ fraudProtectionProviders }}',
webApplicationFirewallProviders = '{{ webApplicationFirewallProviders }}',
webApplicationFirewallVerifications = '{{ webApplicationFirewallVerifications }}'
RETURNING
fraudProtectionProviders,
webApplicationFirewallProviders,
webApplicationFirewallVerifications;
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
DELETE FROM entra_id.identity.risk_prevention
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
