--- 
title: entitlement_management_assignments_target
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_assignments_target
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_assignments_target</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_assignments_target" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_assignments_target" /></td></tr>
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
    <td><CopyableCode code="connectedOrganization" /></td>
    <td><code></code></td>
    <td>The connected organization of the subject. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the subject.</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>The email address of the subject.</td>
</tr>
<tr>
    <td><CopyableCode code="objectId" /></td>
    <td><code>string</code></td>
    <td>The object identifier of the subject. null if the subject isn't yet a user in the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>A string representation of the principal's security identifier, if known, or null if the subject doesn't have a security identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="principalName" /></td>
    <td><code>string</code></td>
    <td>The principal name, if known, of the subject.</td>
</tr>
<tr>
    <td><CopyableCode code="subjectType" /></td>
    <td><code></code></td>
    <td>The resource type of the subject. The possible values are: notSpecified, user, servicePrincipal, unknownFutureValue.</td>
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
    <td><a href="#parameter-access_package_assignment_id"><code>access_package_assignment_id</code></a></td>
    <td></td>
    <td>The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.</td>
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
<tr id="parameter-access_package_assignment_id">
    <td><CopyableCode code="access_package_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageAssignment</td>
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

The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.

```sql
SELECT
id,
connectedOrganization,
displayName,
email,
objectId,
onPremisesSecurityIdentifier,
principalName,
subjectType
FROM entra_id.identity_governance.entitlement_management_assignments_target
WHERE access_package_assignment_id = '{{ access_package_assignment_id }}' -- required
;
```
</TabItem>
</Tabs>
