--- 
title: entitlement_management_resource_requests_resource_roles_resource_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_resource_requests_resource_roles_resource_scopes
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_resource_requests_resource_roles_resource_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_resource_requests_resource_roles_resource_scopes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.entitlement_management_resource_requests_resource_roles_resource_scopes" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the scope.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the scope.</td>
</tr>
<tr>
    <td><CopyableCode code="isRootScope" /></td>
    <td><code>boolean</code></td>
    <td>True if the scopes are arranged in a hierarchy and this is the top or root scope of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="originId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the scope in the resource as defined in the origin system.</td>
</tr>
<tr>
    <td><CopyableCode code="originSystem" /></td>
    <td><code>string</code></td>
    <td>The origin system for the scope.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code></code></td>
    <td></td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the scope.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the scope.</td>
</tr>
<tr>
    <td><CopyableCode code="isRootScope" /></td>
    <td><code>boolean</code></td>
    <td>True if the scopes are arranged in a hierarchy and this is the top or root scope of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="originId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the scope in the resource as defined in the origin system.</td>
</tr>
<tr>
    <td><CopyableCode code="originSystem" /></td>
    <td><code>string</code></td>
    <td>The origin system for the scope.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code></code></td>
    <td></td>
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
    <td><a href="#parameter-accessPackageResourceRequest-id"><code>accessPackageResourceRequest-id</code></a>, <a href="#parameter-accessPackageResourceRole-id"><code>accessPackageResourceRole-id</code></a>, <a href="#parameter-accessPackageResourceScope-id"><code>accessPackageResourceScope-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-accessPackageResourceRequest-id"><code>accessPackageResourceRequest-id</code></a>, <a href="#parameter-accessPackageResourceRole-id"><code>accessPackageResourceRole-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-accessPackageResourceRequest-id"><code>accessPackageResourceRequest-id</code></a>, <a href="#parameter-accessPackageResourceRole-id"><code>accessPackageResourceRole-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessPackageResourceRequest-id"><code>accessPackageResourceRequest-id</code></a>, <a href="#parameter-accessPackageResourceRole-id"><code>accessPackageResourceRole-id</code></a>, <a href="#parameter-accessPackageResourceScope-id"><code>accessPackageResourceScope-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessPackageResourceRequest-id"><code>accessPackageResourceRequest-id</code></a>, <a href="#parameter-accessPackageResourceRole-id"><code>accessPackageResourceRole-id</code></a>, <a href="#parameter-accessPackageResourceScope-id"><code>accessPackageResourceScope-id</code></a></td>
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
<tr id="parameter-accessPackageResourceRequest-id">
    <td><CopyableCode code="accessPackageResourceRequest-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceRequest</td>
</tr>
<tr id="parameter-accessPackageResourceRole-id">
    <td><CopyableCode code="accessPackageResourceRole-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceRole</td>
</tr>
<tr id="parameter-accessPackageResourceScope-id">
    <td><CopyableCode code="accessPackageResourceScope-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceScope</td>
</tr>
<tr id="parameter-$count">
    <td><CopyableCode code="$count" /></td>
    <td><code>boolean</code></td>
    <td>Include count of items</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filter items by property values</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>array</code></td>
    <td>Order items by property values</td>
</tr>
<tr id="parameter-$search">
    <td><CopyableCode code="$search" /></td>
    <td><code>string</code></td>
    <td>Search items by search phrases</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Skip the first n items</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Show only the first n items (example: 50)</td>
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

Read-only. Nullable. Supports $expand.

```sql
SELECT
id,
@odata.type,
description,
displayName,
isRootScope,
originId,
originSystem,
resource
FROM entraid.identity_governance.entitlement_management_resource_requests_resource_roles_resource_scopes
WHERE accessPackageResourceRequest-id = '{{ accessPackageResourceRequest-id }}' -- required
AND accessPackageResourceRole-id = '{{ accessPackageResourceRole-id }}' -- required
AND accessPackageResourceScope-id = '{{ accessPackageResourceScope-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Read-only. Nullable. Supports $expand.

```sql
SELECT
id,
@odata.type,
description,
displayName,
isRootScope,
originId,
originSystem,
resource
FROM entraid.identity_governance.entitlement_management_resource_requests_resource_roles_resource_scopes
WHERE accessPackageResourceRequest-id = '{{ accessPackageResourceRequest-id }}' -- required
AND accessPackageResourceRole-id = '{{ accessPackageResourceRole-id }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $orderby = '{{ $orderby }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
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

No description available.

```sql
INSERT INTO entraid.identity_governance.entitlement_management_resource_requests_resource_roles_resource_scopes (
id,
@odata.type,
description,
displayName,
isRootScope,
originId,
originSystem,
resource,
accessPackageResourceRequest-id,
accessPackageResourceRole-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ description }}',
'{{ displayName }}',
{{ isRootScope }},
'{{ originId }}',
'{{ originSystem }}',
'{{ resource }}',
'{{ accessPackageResourceRequest-id }}',
'{{ accessPackageResourceRole-id }}'
RETURNING
id,
@odata.type,
description,
displayName,
isRootScope,
originId,
originSystem,
resource
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_resource_requests_resource_roles_resource_scopes
  props:
    - name: accessPackageResourceRequest-id
      value: "{{ accessPackageResourceRequest-id }}"
      description: Required parameter for the entitlement_management_resource_requests_resource_roles_resource_scopes resource.
    - name: accessPackageResourceRole-id
      value: "{{ accessPackageResourceRole-id }}"
      description: Required parameter for the entitlement_management_resource_requests_resource_roles_resource_scopes resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: description
      value: "{{ description }}"
      description: |
        The description of the scope.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the scope.
    - name: isRootScope
      value: {{ isRootScope }}
      description: |
        True if the scopes are arranged in a hierarchy and this is the top or root scope of the resource.
    - name: originId
      value: "{{ originId }}"
      description: |
        The unique identifier for the scope in the resource as defined in the origin system.
    - name: originSystem
      value: "{{ originSystem }}"
      description: |
        The origin system for the scope.
    - name: resource
      value: "{{ resource }}"
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

No description available.

```sql
UPDATE entraid.identity_governance.entitlement_management_resource_requests_resource_roles_resource_scopes
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isRootScope = {{ isRootScope }},
originId = '{{ originId }}',
originSystem = '{{ originSystem }}',
resource = '{{ resource }}'
WHERE 
accessPackageResourceRequest-id = '{{ accessPackageResourceRequest-id }}' --required
AND accessPackageResourceRole-id = '{{ accessPackageResourceRole-id }}' --required
AND accessPackageResourceScope-id = '{{ accessPackageResourceScope-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
description,
displayName,
isRootScope,
originId,
originSystem,
resource;
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
DELETE FROM entraid.identity_governance.entitlement_management_resource_requests_resource_roles_resource_scopes
WHERE accessPackageResourceRequest-id = '{{ accessPackageResourceRequest-id }}' --required
AND accessPackageResourceRole-id = '{{ accessPackageResourceRole-id }}' --required
AND accessPackageResourceScope-id = '{{ accessPackageResourceScope-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
