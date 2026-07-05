--- 
title: b2x_user_flows_identity_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_identity_providers
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_identity_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_identity_providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_identity_providers" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The display name of the identity provider. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>The client ID for the application. This is the client ID obtained when registering the application with the identity provider. Required. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>The client secret for the application. This is the client secret obtained when registering the application with the identity provider. This is write-only. A read operation will return .  Required. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The identity provider type is a required field. For B2B scenario: Google, Facebook. For B2C scenario: Microsoft, Google, Amazon, LinkedIn, Facebook, GitHub, Twitter, Weibo, QQ, WeChat, OpenIDConnect. Not nullable.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The display name of the identity provider. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="clientId" /></td>
    <td><code>string</code></td>
    <td>The client ID for the application. This is the client ID obtained when registering the application with the identity provider. Required. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="clientSecret" /></td>
    <td><code>string</code></td>
    <td>The client secret for the application. This is the client secret obtained when registering the application with the identity provider. This is write-only. A read operation will return .  Required. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The identity provider type is a required field. For B2B scenario: Google, Facebook. For B2C scenario: Microsoft, Google, Amazon, LinkedIn, Facebook, GitHub, Twitter, Weibo, QQ, WeChat, OpenIDConnect. Not nullable.</td>
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
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-identity_provider_id"><code>identity_provider_id</code></a></td>
    <td></td>
    <td>The identity providers included in the user flow.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td>Get the identity providers in a b2xIdentityUserFlow object.</td>
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
<tr id="parameter-identity_provider_id">
    <td><CopyableCode code="identity_provider_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of identityProvider</td>
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

The identity providers included in the user flow.

```sql
SELECT
id,
name,
clientId,
clientSecret,
type
FROM entra_id.identity.b2x_user_flows_identity_providers
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
AND identity_provider_id = '{{ identity_provider_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the identity providers in a b2xIdentityUserFlow object.

```sql
SELECT
id,
name,
clientId,
clientSecret,
type
FROM entra_id.identity.b2x_user_flows_identity_providers
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
;
```
</TabItem>
</Tabs>
