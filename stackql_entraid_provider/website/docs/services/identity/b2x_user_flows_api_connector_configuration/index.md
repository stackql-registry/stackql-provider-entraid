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
        { label: 'get', value: 'get' }
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
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td>Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.</td>
</tr>
<tr>
    <td><a href="#get_post_attribute_collection"><CopyableCode code="get_post_attribute_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update_post_attribute_collection"><CopyableCode code="update_post_attribute_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_post_attribute_collection"><CopyableCode code="delete_post_attribute_collection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_post_federation_signup"><CopyableCode code="get_post_federation_signup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update_post_federation_signup"><CopyableCode code="update_post_federation_signup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_post_federation_signup"><CopyableCode code="delete_post_federation_signup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
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
<tr id="parameter-b2x_identity_user_flow_id">
    <td><CopyableCode code="b2x_identity_user_flow_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of b2xIdentityUserFlow</td>
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

Get the apiConnectorConfiguration property in a b2xIdentityUserFlow to detail the API connectors enabled for the user flow.

```sql
SELECT
postAttributeCollection,
postFederationSignup
FROM entra_id.identity.b2x_user_flows_api_connector_configuration
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_post_attribute_collection"
    values={[
        { label: 'get_post_attribute_collection', value: 'get_post_attribute_collection' },
        { label: 'update_post_attribute_collection', value: 'update_post_attribute_collection' },
        { label: 'delete_post_attribute_collection', value: 'delete_post_attribute_collection' },
        { label: 'get_post_federation_signup', value: 'get_post_federation_signup' },
        { label: 'update_post_federation_signup', value: 'update_post_federation_signup' },
        { label: 'delete_post_federation_signup', value: 'delete_post_federation_signup' }
    ]}
>
<TabItem value="get_post_attribute_collection">

Retrieved navigation property

```sql
EXEC entra_id.identity.b2x_user_flows_api_connector_configuration.get_post_attribute_collection 
@b2x_identity_user_flow_id='{{ b2x_identity_user_flow_id }}' --required, 
@$select='{{ $select }}', 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="update_post_attribute_collection">

Success

```sql
EXEC entra_id.identity.b2x_user_flows_api_connector_configuration.update_post_attribute_collection 
@b2x_identity_user_flow_id='{{ b2x_identity_user_flow_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"authenticationConfiguration": "{{ authenticationConfiguration }}", 
"displayName": "{{ displayName }}", 
"targetUrl": "{{ targetUrl }}"
}'
;
```
</TabItem>
<TabItem value="delete_post_attribute_collection">

Success

```sql
EXEC entra_id.identity.b2x_user_flows_api_connector_configuration.delete_post_attribute_collection 
@b2x_identity_user_flow_id='{{ b2x_identity_user_flow_id }}' --required, 
@If-Match='{{ If-Match }}'
;
```
</TabItem>
<TabItem value="get_post_federation_signup">

Retrieved navigation property

```sql
EXEC entra_id.identity.b2x_user_flows_api_connector_configuration.get_post_federation_signup 
@b2x_identity_user_flow_id='{{ b2x_identity_user_flow_id }}' --required, 
@$select='{{ $select }}', 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="update_post_federation_signup">

Success

```sql
EXEC entra_id.identity.b2x_user_flows_api_connector_configuration.update_post_federation_signup 
@b2x_identity_user_flow_id='{{ b2x_identity_user_flow_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"authenticationConfiguration": "{{ authenticationConfiguration }}", 
"displayName": "{{ displayName }}", 
"targetUrl": "{{ targetUrl }}"
}'
;
```
</TabItem>
<TabItem value="delete_post_federation_signup">

Success

```sql
EXEC entra_id.identity.b2x_user_flows_api_connector_configuration.delete_post_federation_signup 
@b2x_identity_user_flow_id='{{ b2x_identity_user_flow_id }}' --required, 
@If-Match='{{ If-Match }}'
;
```
</TabItem>
</Tabs>
