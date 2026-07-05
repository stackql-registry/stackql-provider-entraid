--- 
title: entitlement_management_catalogs_resource_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_catalogs_resource_scopes
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_catalogs_resource_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_catalogs_resource_scopes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_catalogs_resource_scopes" /></td></tr>
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
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
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
<tr id="parameter-access_package_catalog_id">
    <td><CopyableCode code="access_package_catalog_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageCatalog</td>
</tr>
<tr id="parameter-access_package_resource_scope_id">
    <td><CopyableCode code="access_package_resource_scope_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceScope</td>
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

Retrieved navigation property

```sql
SELECT
id,
description,
displayName,
isRootScope,
originId,
originSystem,
resource
FROM entra_id.identity_governance.entitlement_management_catalogs_resource_scopes
WHERE access_package_catalog_id = '{{ access_package_catalog_id }}' -- required
AND access_package_resource_scope_id = '{{ access_package_resource_scope_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
description,
displayName,
isRootScope,
originId,
originSystem,
resource
FROM entra_id.identity_governance.entitlement_management_catalogs_resource_scopes
WHERE access_package_catalog_id = '{{ access_package_catalog_id }}' -- required
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
INSERT INTO entra_id.identity_governance.entitlement_management_catalogs_resource_scopes (
id,
description,
displayName,
isRootScope,
originId,
originSystem,
resource,
access_package_catalog_id
)
SELECT 
'{{ id }}',
'{{ description }}',
'{{ displayName }}',
{{ isRootScope }},
'{{ originId }}',
'{{ originSystem }}',
'{{ resource }}',
'{{ access_package_catalog_id }}'
RETURNING
id,
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
- name: entitlement_management_catalogs_resource_scopes
  props:
    - name: access_package_catalog_id
      value: "{{ access_package_catalog_id }}"
      description: Required parameter for the entitlement_management_catalogs_resource_scopes resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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
UPDATE entra_id.identity_governance.entitlement_management_catalogs_resource_scopes
SET 
id = '{{ id }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isRootScope = {{ isRootScope }},
originId = '{{ originId }}',
originSystem = '{{ originSystem }}',
resource = '{{ resource }}'
WHERE 
access_package_catalog_id = '{{ access_package_catalog_id }}' --required
AND access_package_resource_scope_id = '{{ access_package_resource_scope_id }}' --required
RETURNING
id,
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
DELETE FROM entra_id.identity_governance.entitlement_management_catalogs_resource_scopes
WHERE access_package_catalog_id = '{{ access_package_catalog_id }}' --required
AND access_package_resource_scope_id = '{{ access_package_resource_scope_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
