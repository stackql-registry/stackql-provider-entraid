--- 
title: b2x_user_flows_api_connector_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_api_connector_configuration
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_api_connector_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_api_connector_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_api_connector_configuration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'post_attribute_collection', value: 'post_attribute_collection' },
        { label: 'post_federation_signup', value: 'post_federation_signup' }
    ]}
>
<TabItem value="get">

Entity result.

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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="postAttributeCollection" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.identityApiConnector, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="postFederationSignup" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.identityApiConnector, title: entity)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="post_attribute_collection">

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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authenticationConfiguration" /></td>
    <td><code></code></td>
    <td>The object which describes the authentication configuration details for calling the API. Basic and PKCS 12 client certificate are supported.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the API connector.</td>
</tr>
<tr>
    <td><CopyableCode code="targetUrl" /></td>
    <td><code>string</code></td>
    <td>The URL of the API endpoint to call.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="post_federation_signup">

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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authenticationConfiguration" /></td>
    <td><code></code></td>
    <td>The object which describes the authentication configuration details for calling the API. Basic and PKCS 12 client certificate are supported.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the API connector.</td>
</tr>
<tr>
    <td><CopyableCode code="targetUrl" /></td>
    <td><code>string</code></td>
    <td>The URL of the API endpoint to call.</td>
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
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.</td>
</tr>
<tr>
    <td><a href="#post_attribute_collection"><CopyableCode code="post_attribute_collection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#post_federation_signup"><CopyableCode code="post_federation_signup" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
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
<tr id="parameter-b2xIdentityUserFlow-id">
    <td><CopyableCode code="b2xIdentityUserFlow-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of b2xIdentityUserFlow</td>
</tr>
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
        { label: 'get', value: 'get' },
        { label: 'post_attribute_collection', value: 'post_attribute_collection' },
        { label: 'post_federation_signup', value: 'post_federation_signup' }
    ]}
>
<TabItem value="get">

Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.

```sql
SELECT
@odata.type,
postAttributeCollection,
postFederationSignup
FROM entra_id.identity.b2x_user_flows_api_connector_configuration
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="post_attribute_collection">

Retrieved navigation property

```sql
SELECT
id,
@odata.type,
authenticationConfiguration,
displayName,
targetUrl
FROM entra_id.identity.b2x_user_flows_api_connector_configuration
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="post_federation_signup">

Retrieved navigation property

```sql
SELECT
id,
@odata.type,
authenticationConfiguration,
displayName,
targetUrl
FROM entra_id.identity.b2x_user_flows_api_connector_configuration
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
