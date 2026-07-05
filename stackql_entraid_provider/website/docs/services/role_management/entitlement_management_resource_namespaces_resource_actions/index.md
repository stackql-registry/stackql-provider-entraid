--- 
title: entitlement_management_resource_namespaces_resource_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_resource_namespaces_resource_actions
  - role_management
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_resource_namespaces_resource_actions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_resource_namespaces_resource_actions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.entitlement_management_resource_namespaces_resource_actions" /></td></tr>
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
    <td><a href="#parameter-unified_rbac_resource_namespace_id"><code>unified_rbac_resource_namespace_id</code></a>, <a href="#parameter-unified_rbac_resource_action_id"><code>unified_rbac_resource_action_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-unified_rbac_resource_namespace_id"><code>unified_rbac_resource_namespace_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-unified_rbac_resource_namespace_id"><code>unified_rbac_resource_namespace_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unified_rbac_resource_namespace_id"><code>unified_rbac_resource_namespace_id</code></a>, <a href="#parameter-unified_rbac_resource_action_id"><code>unified_rbac_resource_action_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_rbac_resource_namespace_id"><code>unified_rbac_resource_namespace_id</code></a>, <a href="#parameter-unified_rbac_resource_action_id"><code>unified_rbac_resource_action_id</code></a></td>
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
<tr id="parameter-unified_rbac_resource_action_id">
    <td><CopyableCode code="unified_rbac_resource_action_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRbacResourceAction</td>
</tr>
<tr id="parameter-unified_rbac_resource_namespace_id">
    <td><CopyableCode code="unified_rbac_resource_namespace_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRbacResourceNamespace</td>
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
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
resourceScopeId
FROM entra_id.role_management.entitlement_management_resource_namespaces_resource_actions
WHERE unified_rbac_resource_namespace_id = '{{ unified_rbac_resource_namespace_id }}' -- required
AND unified_rbac_resource_action_id = '{{ unified_rbac_resource_action_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
name,
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
resourceScopeId
FROM entra_id.role_management.entitlement_management_resource_namespaces_resource_actions
WHERE unified_rbac_resource_namespace_id = '{{ unified_rbac_resource_namespace_id }}' -- required
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
INSERT INTO entra_id.role_management.entitlement_management_resource_namespaces_resource_actions (
id,
actionVerb,
authenticationContextId,
description,
isAuthenticationContextSettable,
name,
resourceScopeId,
unified_rbac_resource_namespace_id
)
SELECT 
'{{ id }}',
'{{ actionVerb }}',
'{{ authenticationContextId }}',
'{{ description }}',
{{ isAuthenticationContextSettable }},
'{{ name }}',
'{{ resourceScopeId }}',
'{{ unified_rbac_resource_namespace_id }}'
RETURNING
id,
name,
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
- name: entitlement_management_resource_namespaces_resource_actions
  props:
    - name: unified_rbac_resource_namespace_id
      value: "{{ unified_rbac_resource_namespace_id }}"
      description: Required parameter for the entitlement_management_resource_namespaces_resource_actions resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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
UPDATE entra_id.role_management.entitlement_management_resource_namespaces_resource_actions
SET 
id = '{{ id }}',
actionVerb = '{{ actionVerb }}',
authenticationContextId = '{{ authenticationContextId }}',
description = '{{ description }}',
isAuthenticationContextSettable = {{ isAuthenticationContextSettable }},
name = '{{ name }}',
resourceScopeId = '{{ resourceScopeId }}'
WHERE 
unified_rbac_resource_namespace_id = '{{ unified_rbac_resource_namespace_id }}' --required
AND unified_rbac_resource_action_id = '{{ unified_rbac_resource_action_id }}' --required
RETURNING
id,
name,
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
DELETE FROM entra_id.role_management.entitlement_management_resource_namespaces_resource_actions
WHERE unified_rbac_resource_namespace_id = '{{ unified_rbac_resource_namespace_id }}' --required
AND unified_rbac_resource_action_id = '{{ unified_rbac_resource_action_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
