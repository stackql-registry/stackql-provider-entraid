--- 
title: entitlement_management
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>entitlement_management</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.entitlement_management" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="accessPackageAssignmentApprovals" /></td>
    <td><code>array</code></td>
    <td>Approval stages for decisions associated with access package assignment requests.</td>
</tr>
<tr>
    <td><CopyableCode code="accessPackages" /></td>
    <td><code>array</code></td>
    <td>Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentPolicies" /></td>
    <td><code>array</code></td>
    <td>Access package assignment policies govern which subjects can request or be assigned an access package via an access package assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentRequests" /></td>
    <td><code>array</code></td>
    <td>Access package assignment requests created by or on behalf of a subject.</td>
</tr>
<tr>
    <td><CopyableCode code="assignments" /></td>
    <td><code>array</code></td>
    <td>The assignment of an access package to a subject for a period of time.</td>
</tr>
<tr>
    <td><CopyableCode code="catalogs" /></td>
    <td><code>array</code></td>
    <td>A container for access packages.</td>
</tr>
<tr>
    <td><CopyableCode code="connectedOrganizations" /></td>
    <td><code>array</code></td>
    <td>References to a directory or domain of another organization whose users can request access.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceEnvironments" /></td>
    <td><code>array</code></td>
    <td>A reference to the geolocation environments in which a resource is located.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRequests" /></td>
    <td><code>array</code></td>
    <td>Represents a request to add or remove a resource to or from a catalog respectively.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRoleScopes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>The resources associated with the catalogs.</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code></code></td>
    <td>The settings that control the behavior of Microsoft Entra entitlement management.</td>
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
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td></td>
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

Retrieved navigation property

```sql
SELECT
id,
@odata.type,
accessPackageAssignmentApprovals,
accessPackages,
assignmentPolicies,
assignmentRequests,
assignments,
catalogs,
connectedOrganizations,
resourceEnvironments,
resourceRequests,
resourceRoleScopes,
resources,
settings
FROM entraid.identity_governance.entitlement_management
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
UPDATE entraid.identity_governance.entitlement_management
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
accessPackageAssignmentApprovals = '{{ accessPackageAssignmentApprovals }}',
accessPackages = '{{ accessPackages }}',
assignmentPolicies = '{{ assignmentPolicies }}',
assignmentRequests = '{{ assignmentRequests }}',
assignments = '{{ assignments }}',
catalogs = '{{ catalogs }}',
connectedOrganizations = '{{ connectedOrganizations }}',
resourceEnvironments = '{{ resourceEnvironments }}',
resourceRequests = '{{ resourceRequests }}',
resourceRoleScopes = '{{ resourceRoleScopes }}',
resources = '{{ resources }}',
settings = '{{ settings }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
accessPackageAssignmentApprovals,
accessPackages,
assignmentPolicies,
assignmentRequests,
assignments,
catalogs,
connectedOrganizations,
resourceEnvironments,
resourceRequests,
resourceRoleScopes,
resources,
settings;
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
DELETE FROM entraid.identity_governance.entitlement_management
WHERE If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
