--- 
title: directory
hide_title: false
hide_table_of_contents: false
keywords:
  - directory
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

Creates, updates, deletes, gets or lists a <code>directory</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="directory" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.directory" /></td></tr>
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
    <td><CopyableCode code="administrativeUnits" /></td>
    <td><code>array</code></td>
    <td>Conceptual container for user and group directory objects.</td>
</tr>
<tr>
    <td><CopyableCode code="attributeSets" /></td>
    <td><code>array</code></td>
    <td>Group of related custom security attribute definitions.</td>
</tr>
<tr>
    <td><CopyableCode code="customSecurityAttributeDefinitions" /></td>
    <td><code>array</code></td>
    <td>Schema of a custom security attributes (key-value pairs).</td>
</tr>
<tr>
    <td><CopyableCode code="deletedItems" /></td>
    <td><code>array</code></td>
    <td>Recently deleted items. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceLocalCredentials" /></td>
    <td><code>array</code></td>
    <td>The credentials of the device's local administrator account backed up to Microsoft Entra ID.</td>
</tr>
<tr>
    <td><CopyableCode code="federationConfigurations" /></td>
    <td><code>array</code></td>
    <td>Configure domain federation with organizations whose identity provider (IdP) supports either the SAML or WS-Fed protocol.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSynchronization" /></td>
    <td><code>array</code></td>
    <td>A container for on-premises directory synchronization functionalities that are available for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKeyInfrastructure" /></td>
    <td><code></code></td>
    <td>The collection of public key infrastructure instances for the certificate-based authentication feature for users in a Microsoft Entra tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptions" /></td>
    <td><code>array</code></td>
    <td>List of commercial subscriptions that an organization acquired.</td>
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
id,
administrativeUnits,
attributeSets,
customSecurityAttributeDefinitions,
deletedItems,
deviceLocalCredentials,
federationConfigurations,
onPremisesSynchronization,
publicKeyInfrastructure,
subscriptions
FROM entra_id.directory.directory
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
UPDATE entra_id.directory.directory
SET 
id = '{{ id }}',
administrativeUnits = '{{ administrativeUnits }}',
attributeSets = '{{ attributeSets }}',
customSecurityAttributeDefinitions = '{{ customSecurityAttributeDefinitions }}',
deletedItems = '{{ deletedItems }}',
deviceLocalCredentials = '{{ deviceLocalCredentials }}',
federationConfigurations = '{{ federationConfigurations }}',
onPremisesSynchronization = '{{ onPremisesSynchronization }}',
publicKeyInfrastructure = '{{ publicKeyInfrastructure }}',
subscriptions = '{{ subscriptions }}'
RETURNING
id,
administrativeUnits,
attributeSets,
customSecurityAttributeDefinitions,
deletedItems,
deviceLocalCredentials,
federationConfigurations,
onPremisesSynchronization,
publicKeyInfrastructure,
subscriptions;
```
</TabItem>
</Tabs>
