--- 
title: audit_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - audit_logs
  - audit_logs
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

Creates, updates, deletes, gets or lists an <code>audit_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="audit_logs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.audit_logs.audit_logs" /></td></tr>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for an entity. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryAudits" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provisioning" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="signIns" /></td>
    <td><code>array</code></td>
    <td></td>
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
<tr>
    <td><a href="#sign_ins"><CopyableCode code="sign_ins" /></a></td>
    <td><CopyableCode code="exec" /></td>
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
id,
directoryAudits,
provisioning,
signIns
FROM entra_id.audit_logs.audit_logs
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
UPDATE entra_id.audit_logs.audit_logs
SET 
id = '{{ id }}',
directoryAudits = '{{ directoryAudits }}',
provisioning = '{{ provisioning }}',
signIns = '{{ signIns }}'
RETURNING
id,
directoryAudits,
provisioning,
signIns;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="sign_ins"
    values={[
        { label: 'sign_ins', value: 'sign_ins' }
    ]}
>
<TabItem value="sign_ins">

Created navigation property.

```sql
EXEC entra_id.audit_logs.audit_logs.sign_ins 
@@json=
'{
"id": "{{ id }}", 
"appDisplayName": "{{ appDisplayName }}", 
"appId": "{{ appId }}", 
"appliedConditionalAccessPolicies": "{{ appliedConditionalAccessPolicies }}", 
"clientAppUsed": "{{ clientAppUsed }}", 
"conditionalAccessStatus": "{{ conditionalAccessStatus }}", 
"correlationId": "{{ correlationId }}", 
"createdDateTime": "{{ createdDateTime }}", 
"deviceDetail": "{{ deviceDetail }}", 
"ipAddress": "{{ ipAddress }}", 
"isInteractive": {{ isInteractive }}, 
"location": "{{ location }}", 
"resourceDisplayName": "{{ resourceDisplayName }}", 
"resourceId": "{{ resourceId }}", 
"riskDetail": "{{ riskDetail }}", 
"riskEventTypes": "{{ riskEventTypes }}", 
"riskEventTypes_v2": "{{ riskEventTypes_v2 }}", 
"riskLevelAggregated": "{{ riskLevelAggregated }}", 
"riskLevelDuringSignIn": "{{ riskLevelDuringSignIn }}", 
"riskState": "{{ riskState }}", 
"status": "{{ status }}", 
"userDisplayName": "{{ userDisplayName }}", 
"userId": "{{ userId }}", 
"userPrincipalName": "{{ userPrincipalName }}"
}'
;
```
</TabItem>
</Tabs>
