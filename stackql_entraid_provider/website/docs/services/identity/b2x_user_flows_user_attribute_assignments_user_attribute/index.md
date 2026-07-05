--- 
title: b2x_user_flows_user_attribute_assignments_user_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_user_attribute_assignments_user_attribute
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_user_attribute_assignments_user_attribute</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_user_attribute_assignments_user_attribute" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_user_attribute_assignments_user_attribute" /></td></tr>
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
    <td><CopyableCode code="dataType" /></td>
    <td><code>string</code></td>
    <td> (string, boolean, int64, stringCollection, dateTime, unknownFutureValue) (title: identityUserFlowAttributeDataType)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the user flow attribute that's shown to the user at the time of sign up.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the user flow attribute.  Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="userFlowAttributeType" /></td>
    <td><code>string</code></td>
    <td> (builtIn, custom, required, unknownFutureValue) (title: identityUserFlowAttributeType)</td>
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
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-identity_user_flow_attribute_assignment_id"><code>identity_user_flow_attribute_assignment_id</code></a></td>
    <td></td>
    <td>The user attribute that you want to add to your user flow.</td>
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
<tr id="parameter-identity_user_flow_attribute_assignment_id">
    <td><CopyableCode code="identity_user_flow_attribute_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of identityUserFlowAttributeAssignment</td>
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

The user attribute that you want to add to your user flow.

```sql
SELECT
id,
dataType,
description,
displayName,
userFlowAttributeType
FROM entra_id.identity.b2x_user_flows_user_attribute_assignments_user_attribute
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
AND identity_user_flow_attribute_assignment_id = '{{ identity_user_flow_attribute_assignment_id }}' -- required
;
```
</TabItem>
</Tabs>
