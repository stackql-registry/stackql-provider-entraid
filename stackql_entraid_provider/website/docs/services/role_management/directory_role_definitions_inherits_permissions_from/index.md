--- 
title: directory_role_definitions_inherits_permissions_from
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_role_definitions_inherits_permissions_from
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

Creates, updates, deletes, gets or lists a <code>directory_role_definitions_inherits_permissions_from</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="directory_role_definitions_inherits_permissions_from" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.directory_role_definitions_inherits_permissions_from" /></td></tr>
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
    <td>The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the unifiedRoleDefinition. Read-only when isBuiltIn is true. Required.  Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="inheritsPermissionsFrom" /></td>
    <td><code>array</code></td>
    <td>Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isBuiltIn" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether the role definition is part of the default set included in Microsoft Entra or a custom definition. Read-only. Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceScopes" /></td>
    <td><code>array</code></td>
    <td>List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="rolePermissions" /></td>
    <td><code>array</code></td>
    <td>List of permissions included in the role. Read-only when isBuiltIn is true. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Indicates version of the role definition. Read-only when isBuiltIn is true.</td>
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
    <td>The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the unifiedRoleDefinition. Read-only when isBuiltIn is true. Required.  Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="inheritsPermissionsFrom" /></td>
    <td><code>array</code></td>
    <td>Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isBuiltIn" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether the role definition is part of the default set included in Microsoft Entra or a custom definition. Read-only. Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceScopes" /></td>
    <td><code>array</code></td>
    <td>List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="rolePermissions" /></td>
    <td><code>array</code></td>
    <td>List of permissions included in the role. Read-only when isBuiltIn is true. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Indicates version of the role definition. Read-only when isBuiltIn is true.</td>
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
    <td><a href="#parameter-unified_role_definition_id"><code>unified_role_definition_id</code></a>, <a href="#parameter-unified_role_definition_id1"><code>unified_role_definition_id1</code></a></td>
    <td></td>
    <td>Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-unified_role_definition_id"><code>unified_role_definition_id</code></a></td>
    <td></td>
    <td>Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-unified_role_definition_id"><code>unified_role_definition_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unified_role_definition_id"><code>unified_role_definition_id</code></a>, <a href="#parameter-unified_role_definition_id1"><code>unified_role_definition_id1</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_role_definition_id"><code>unified_role_definition_id</code></a>, <a href="#parameter-unified_role_definition_id1"><code>unified_role_definition_id1</code></a></td>
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
<tr id="parameter-unified_role_definition_id">
    <td><CopyableCode code="unified_role_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleDefinition</td>
</tr>
<tr id="parameter-unified_role_definition_id1">
    <td><CopyableCode code="unified_role_definition_id1" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleDefinition</td>
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

Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.

```sql
SELECT
id,
description,
displayName,
inheritsPermissionsFrom,
isBuiltIn,
isEnabled,
resourceScopes,
rolePermissions,
templateId,
version
FROM entra_id.role_management.directory_role_definitions_inherits_permissions_from
WHERE unified_role_definition_id = '{{ unified_role_definition_id }}' -- required
AND unified_role_definition_id1 = '{{ unified_role_definition_id1 }}' -- required
;
```
</TabItem>
<TabItem value="list">

Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.

```sql
SELECT
id,
description,
displayName,
inheritsPermissionsFrom,
isBuiltIn,
isEnabled,
resourceScopes,
rolePermissions,
templateId,
version
FROM entra_id.role_management.directory_role_definitions_inherits_permissions_from
WHERE unified_role_definition_id = '{{ unified_role_definition_id }}' -- required
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
INSERT INTO entra_id.role_management.directory_role_definitions_inherits_permissions_from (
id,
description,
displayName,
isBuiltIn,
isEnabled,
resourceScopes,
rolePermissions,
templateId,
version,
inheritsPermissionsFrom,
unified_role_definition_id
)
SELECT 
'{{ id }}',
'{{ description }}',
'{{ displayName }}',
{{ isBuiltIn }},
{{ isEnabled }},
'{{ resourceScopes }}',
'{{ rolePermissions }}',
'{{ templateId }}',
'{{ version }}',
'{{ inheritsPermissionsFrom }}',
'{{ unified_role_definition_id }}'
RETURNING
id,
description,
displayName,
inheritsPermissionsFrom,
isBuiltIn,
isEnabled,
resourceScopes,
rolePermissions,
templateId,
version
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: directory_role_definitions_inherits_permissions_from
  props:
    - name: unified_role_definition_id
      value: "{{ unified_role_definition_id }}"
      description: Required parameter for the directory_role_definitions_inherits_permissions_from resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the unifiedRoleDefinition. Read-only when isBuiltIn is true. Required.  Supports $filter (eq, in).
    - name: isBuiltIn
      value: {{ isBuiltIn }}
      description: |
        Flag indicating whether the role definition is part of the default set included in Microsoft Entra or a custom definition. Read-only. Supports $filter (eq, in).
    - name: isEnabled
      value: {{ isEnabled }}
      description: |
        Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.
    - name: resourceScopes
      value:
        - "{{ resourceScopes }}"
      description: |
        List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.
    - name: rolePermissions
      description: |
        List of permissions included in the role. Read-only when isBuiltIn is true. Required.
      value:
        - allowedResourceActions: "{{ allowedResourceActions }}"
          condition: "{{ condition }}"
          excludedResourceActions: "{{ excludedResourceActions }}"
    - name: templateId
      value: "{{ templateId }}"
      description: |
        Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories.
    - name: version
      value: "{{ version }}"
      description: |
        Indicates version of the role definition. Read-only when isBuiltIn is true.
    - name: inheritsPermissionsFrom
      description: |
        Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.
      value:
        - id: "{{ id }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          isBuiltIn: {{ isBuiltIn }}
          isEnabled: {{ isEnabled }}
          resourceScopes: "{{ resourceScopes }}"
          rolePermissions: "{{ rolePermissions }}"
          templateId: "{{ templateId }}"
          version: "{{ version }}"
          inheritsPermissionsFrom: "{{ inheritsPermissionsFrom }}"
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
UPDATE entra_id.role_management.directory_role_definitions_inherits_permissions_from
SET 
id = '{{ id }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isBuiltIn = {{ isBuiltIn }},
isEnabled = {{ isEnabled }},
resourceScopes = '{{ resourceScopes }}',
rolePermissions = '{{ rolePermissions }}',
templateId = '{{ templateId }}',
version = '{{ version }}',
inheritsPermissionsFrom = '{{ inheritsPermissionsFrom }}'
WHERE 
unified_role_definition_id = '{{ unified_role_definition_id }}' --required
AND unified_role_definition_id1 = '{{ unified_role_definition_id1 }}' --required
RETURNING
id,
description,
displayName,
inheritsPermissionsFrom,
isBuiltIn,
isEnabled,
resourceScopes,
rolePermissions,
templateId,
version;
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
DELETE FROM entra_id.role_management.directory_role_definitions_inherits_permissions_from
WHERE unified_role_definition_id = '{{ unified_role_definition_id }}' --required
AND unified_role_definition_id1 = '{{ unified_role_definition_id1 }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
