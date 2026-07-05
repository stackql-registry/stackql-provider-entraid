--- 
title: risk_prevention_fraud_protection_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - risk_prevention_fraud_protection_providers
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

Creates, updates, deletes, gets or lists a <code>risk_prevention_fraud_protection_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="risk_prevention_fraud_protection_providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.risk_prevention_fraud_protection_providers" /></td></tr>
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
    <td>The display name of the fraud protection provider configuration.</td>
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
    <td>The display name of the fraud protection provider configuration.</td>
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
    <td><a href="#parameter-fraud_protection_provider_id"><code>fraud_protection_provider_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of fraudProtectionProvider object. The following derived types are currently supported.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the fraudProtectionProvider object and their properties. The following derived types are supported:</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new fraudProtectionProvider object. You can create one of the following subtypes that are derived from fraudProtectionProvider.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-fraud_protection_provider_id"><code>fraud_protection_provider_id</code></a></td>
    <td></td>
    <td>Update the properties of a fraudProtectionProvider object. The following derived types are currently supported.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-fraud_protection_provider_id"><code>fraud_protection_provider_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a fraudProtectionProvider object.</td>
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
<tr id="parameter-fraud_protection_provider_id">
    <td><CopyableCode code="fraud_protection_provider_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of fraudProtectionProvider</td>
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

Read the properties and relationships of fraudProtectionProvider object. The following derived types are currently supported.

```sql
SELECT
id,
displayName
FROM entra_id.identity.risk_prevention_fraud_protection_providers
WHERE fraud_protection_provider_id = '{{ fraud_protection_provider_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the fraudProtectionProvider object and their properties. The following derived types are supported:

```sql
SELECT
id,
displayName
FROM entra_id.identity.risk_prevention_fraud_protection_providers
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

Create a new fraudProtectionProvider object. You can create one of the following subtypes that are derived from fraudProtectionProvider.

```sql
INSERT INTO entra_id.identity.risk_prevention_fraud_protection_providers (
id,
displayName
)
SELECT 
'{{ id }}',
'{{ displayName }}'
RETURNING
id,
displayName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: risk_prevention_fraud_protection_providers
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the fraud protection provider configuration.
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

Update the properties of a fraudProtectionProvider object. The following derived types are currently supported.

```sql
UPDATE entra_id.identity.risk_prevention_fraud_protection_providers
SET 
id = '{{ id }}',
displayName = '{{ displayName }}'
WHERE 
fraud_protection_provider_id = '{{ fraud_protection_provider_id }}' --required
RETURNING
id,
displayName;
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

Delete a fraudProtectionProvider object.

```sql
DELETE FROM entra_id.identity.risk_prevention_fraud_protection_providers
WHERE fraud_protection_provider_id = '{{ fraud_protection_provider_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
