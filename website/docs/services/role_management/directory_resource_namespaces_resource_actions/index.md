--- 
title: directory_resource_namespaces_resource_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_resource_namespaces_resource_actions
  - role_management
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

Creates, updates, deletes, gets or lists a <code>directory_resource_namespaces_resource_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="directory_resource_namespaces_resource_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.role_management.directory_resource_namespaces_resource_actions" /></td></tr>
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
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="actionVerb" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authenticationContextId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isAuthenticationContextSettable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resourceScopeId" /></td>
    <td><code>string</code></td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="actionVerb" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="authenticationContextId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isAuthenticationContextSettable" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resourceScopeId" /></td>
    <td><code>string</code></td>
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
    <td><a href="#parameter-unifiedRbacResourceNamespace-id"><code>unifiedRbacResourceNamespace-id</code></a>, <a href="#parameter-unifiedRbacResourceAction-id"><code>unifiedRbacResourceAction-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-unifiedRbacResourceNamespace-id"><code>unifiedRbacResourceNamespace-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-unifiedRbacResourceNamespace-id"><code>unifiedRbacResourceNamespace-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unifiedRbacResourceNamespace-id"><code>unifiedRbacResourceNamespace-id</code></a>, <a href="#parameter-unifiedRbacResourceAction-id"><code>unifiedRbacResourceAction-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unifiedRbacResourceNamespace-id"><code>unifiedRbacResourceNamespace-id</code></a>, <a href="#parameter-unifiedRbacResourceAction-id"><code>unifiedRbacResourceAction-id</code></a></td>
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
<tr id="parameter-unifiedRbacResourceAction-id">
    <td><CopyableCode code="unifiedRbacResourceAction-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRbacResourceAction</td>
</tr>
<tr id="parameter-unifiedRbacResourceNamespace-id">
    <td><CopyableCode code="unifiedRbacResourceNamespace-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRbacResourceNamespace</td>
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

Retrieved navigation property

```sql
SELECT
id,
name,
@odata.type,
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
resourceScopeId
FROM entraid.role_management.directory_resource_namespaces_resource_actions
WHERE unifiedRbacResourceNamespace-id = '{{ unifiedRbacResourceNamespace-id }}' -- required
AND unifiedRbacResourceAction-id = '{{ unifiedRbacResourceAction-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
name,
@odata.type,
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
resourceScopeId
FROM entraid.role_management.directory_resource_namespaces_resource_actions
WHERE unifiedRbacResourceNamespace-id = '{{ unifiedRbacResourceNamespace-id }}' -- required
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
INSERT INTO entraid.role_management.directory_resource_namespaces_resource_actions (
id,
@odata.type,
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
name,
resourceScopeId,
unifiedRbacResourceNamespace-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ actionVerb }}',
'{{ authenticationContextId }}',
'{{ description }}',
{{ isAuthenticationContextSettable }},
'{{ name }}',
'{{ resourceScopeId }}',
'{{ unifiedRbacResourceNamespace-id }}'
RETURNING
id,
name,
@odata.type,
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
resourceScopeId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: directory_resource_namespaces_resource_actions
  props:
    - name: unifiedRbacResourceNamespace-id
      value: "{{ unifiedRbacResourceNamespace-id }}"
      description: Required parameter for the directory_resource_namespaces_resource_actions resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: actionVerb
      value: "{{ actionVerb }}"
    - name: authenticationContextId
      value: "{{ authenticationContextId }}"
    - name: description
      value: "{{ description }}"
    - name: isAuthenticationContextSettable
      value: {{ isAuthenticationContextSettable }}
    - name: name
      value: "{{ name }}"
    - name: resourceScopeId
      value: "{{ resourceScopeId }}"
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
UPDATE entraid.role_management.directory_resource_namespaces_resource_actions
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
actionVerb = '{{ actionVerb }}',
authenticationContextId = '{{ authenticationContextId }}',
description = '{{ description }}',
isAuthenticationContextSettable = {{ isAuthenticationContextSettable }},
name = '{{ name }}',
resourceScopeId = '{{ resourceScopeId }}'
WHERE 
unifiedRbacResourceNamespace-id = '{{ unifiedRbacResourceNamespace-id }}' --required
AND unifiedRbacResourceAction-id = '{{ unifiedRbacResourceAction-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
name,
@odata.type,
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
resourceScopeId;
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
DELETE FROM entraid.role_management.directory_resource_namespaces_resource_actions
WHERE unifiedRbacResourceNamespace-id = '{{ unifiedRbacResourceNamespace-id }}' --required
AND unifiedRbacResourceAction-id = '{{ unifiedRbacResourceAction-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
