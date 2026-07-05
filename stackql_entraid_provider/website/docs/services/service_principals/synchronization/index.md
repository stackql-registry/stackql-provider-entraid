--- 
title: synchronization
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization
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

Creates, updates, deletes, gets or lists a <code>synchronization</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.synchronization" /></td></tr>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for an entity. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="jobs" /></td>
    <td><code>array</code></td>
    <td>Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.</td>
</tr>
<tr>
    <td><CopyableCode code="secrets" /></td>
    <td><code>array</code></td>
    <td>Represents a collection of credentials to access provisioned cloud applications.</td>
</tr>
<tr>
    <td><CopyableCode code="templates" /></td>
    <td><code>array</code></td>
    <td>Preconfigured synchronization settings for a particular application.</td>
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
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.</td>
</tr>
<tr>
    <td><a href="#replace"><CopyableCode code="replace" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#acquire_access_token"><CopyableCode code="acquire_access_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Acquire an OAuth access token to authorize the Microsoft Entra provisioning service to provision users into an application.</td>
</tr>
<tr>
    <td><a href="#secrets"><CopyableCode code="secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Provide credentials for establishing connectivity with the target system.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Represents the capability for Microsoft Entra identity synchronization through the Microsoft Graph API.

```sql
SELECT
id,
jobs,
secrets,
templates
FROM entra_id.service_principals.synchronization
WHERE service_principal_id = '{{ service_principal_id }}' -- required
;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="replace"
    values={[
        { label: 'replace', value: 'replace' }
    ]}
>
<TabItem value="replace">

No description available.

```sql
REPLACE entra_id.service_principals.synchronization
SET 
id = '{{ id }}',
secrets = '{{ secrets }}',
jobs = '{{ jobs }}',
templates = '{{ templates }}'
WHERE 
service_principal_id = '{{ service_principal_id }}' --required
RETURNING
id,
jobs,
secrets,
templates;
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
DELETE FROM entra_id.service_principals.synchronization
WHERE service_principal_id = '{{ service_principal_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="acquire_access_token"
    values={[
        { label: 'acquire_access_token', value: 'acquire_access_token' },
        { label: 'secrets', value: 'secrets' }
    ]}
>
<TabItem value="acquire_access_token">

Acquire an OAuth access token to authorize the Microsoft Entra provisioning service to provision users into an application.

```sql
EXEC entra_id.service_principals.synchronization.acquire_access_token 
@service_principal_id='{{ service_principal_id }}' --required 
@@json=
'{
"credentials": "{{ credentials }}"
}'
;
```
</TabItem>
<TabItem value="secrets">

Provide credentials for establishing connectivity with the target system.

```sql
EXEC entra_id.service_principals.synchronization.secrets 
@service_principal_id='{{ service_principal_id }}' --required 
@@json=
'{
"value": "{{ value }}"
}'
;
```
</TabItem>
</Tabs>
