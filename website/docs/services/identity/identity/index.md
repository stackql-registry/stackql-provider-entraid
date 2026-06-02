--- 
title: identity
hide_title: false
hide_table_of_contents: false
keywords:
  - identity
  - identity
  - entraid
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage entraid resources using SQL
custom_edit_url: null
image: /img/stackql-entraid-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>identity</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="identity" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity.identity" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="apiConnectors" /></td>
    <td><code>array</code></td>
    <td>Represents entry point for API connectors.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationEventListeners" /></td>
    <td><code>array</code></td>
    <td>Represents listeners for custom authentication extension events in Azure AD for workforce and customers.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationEventsFlows" /></td>
    <td><code>array</code></td>
    <td>Represents the entry point for self-service sign-up and sign-in user flows in both Microsoft Entra workforce and external tenants.</td>
</tr>
<tr>
    <td><CopyableCode code="b2xUserFlows" /></td>
    <td><code>array</code></td>
    <td>Represents entry point for B2X/self-service sign-up identity userflows.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionalAccess" /></td>
    <td><code></code></td>
    <td>the entry point for the Conditional Access (CA) object model.</td>
</tr>
<tr>
    <td><CopyableCode code="customAuthenticationExtensions" /></td>
    <td><code>array</code></td>
    <td>Represents custom extensions to authentication flows in Azure AD for workforce and customers.</td>
</tr>
<tr>
    <td><CopyableCode code="identityProviders" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="riskPrevention" /></td>
    <td><code></code></td>
    <td>Represents the entry point for fraud and risk prevention configurations in Microsoft Entra External ID, including third-party provider settings.</td>
</tr>
<tr>
    <td><CopyableCode code="userFlowAttributes" /></td>
    <td><code>array</code></td>
    <td>Represents entry point for identity userflow attributes.</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedId" /></td>
    <td><code>object</code></td>
    <td> (x-ms-discriminator-value: #microsoft.graph.identityVerifiedIdRoot, title: entity)</td>
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
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
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

Retrieved entity

```sql
SELECT
id,
@odata.type,
apiConnectors,
authenticationEventListeners,
authenticationEventsFlows,
b2xUserFlows,
conditionalAccess,
customAuthenticationExtensions,
identityProviders,
riskPrevention,
userFlowAttributes,
verifiedId
FROM entraid.identity.identity
WHERE $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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
UPDATE entraid.identity.identity
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
apiConnectors = '{{ apiConnectors }}',
authenticationEventListeners = '{{ authenticationEventListeners }}',
authenticationEventsFlows = '{{ authenticationEventsFlows }}',
b2xUserFlows = '{{ b2xUserFlows }}',
conditionalAccess = '{{ conditionalAccess }}',
customAuthenticationExtensions = '{{ customAuthenticationExtensions }}',
identityProviders = '{{ identityProviders }}',
riskPrevention = '{{ riskPrevention }}',
userFlowAttributes = '{{ userFlowAttributes }}',
verifiedId = '{{ verifiedId }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
apiConnectors,
authenticationEventListeners,
authenticationEventsFlows,
b2xUserFlows,
conditionalAccess,
customAuthenticationExtensions,
identityProviders,
riskPrevention,
userFlowAttributes,
verifiedId;
```
</TabItem>
</Tabs>
