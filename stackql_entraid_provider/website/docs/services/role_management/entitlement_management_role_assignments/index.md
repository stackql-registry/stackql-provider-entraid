--- 
title: entitlement_management_role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_role_assignments
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_role_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.role_management.entitlement_management_role_assignments" /></td></tr>
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
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app specific scope when the assignment scope is app specific. Containment entity. Supports $expand for the entitlement provider only.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by a resource application only. For the entitlement management provider, use this property to specify a catalog. For example, /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997. Supports $filter (eq, in). For example, /roleManagement/entitlementManagement/roleAssignments?$filter=appScopeId eq '/AccessPackageCatalog/&#123;catalog id&#125;'.</td>
</tr>
<tr>
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the assignment. Read-only. Supports $expand for the directory provider.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications, unlike app scopes that are defined and understood by a resource application only. Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>Referencing the assigned principal. Read-only. Supports $expand except for the Exchange provider.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal to which the assignment is granted. Supported principals are users, role-assignable groups, and service principals. Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>The roleDefinition the assignment is for. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq, in).</td>
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
    <td><CopyableCode code="appScope" /></td>
    <td><code></code></td>
    <td>Read-only property with details of the app specific scope when the assignment scope is app specific. Containment entity. Supports $expand for the entitlement provider only.</td>
</tr>
<tr>
    <td><CopyableCode code="appScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by a resource application only. For the entitlement management provider, use this property to specify a catalog. For example, /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997. Supports $filter (eq, in). For example, /roleManagement/entitlementManagement/roleAssignments?$filter=appScopeId eq '/AccessPackageCatalog/&#123;catalog id&#125;'.</td>
</tr>
<tr>
    <td><CopyableCode code="condition" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="directoryScope" /></td>
    <td><code></code></td>
    <td>The directory object that is the scope of the assignment. Read-only. Supports $expand for the directory provider.</td>
</tr>
<tr>
    <td><CopyableCode code="directoryScopeId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications, unlike app scopes that are defined and understood by a resource application only. Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="principal" /></td>
    <td><code></code></td>
    <td>Referencing the assigned principal. Read-only. Supports $expand except for the Exchange provider.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the principal to which the assignment is granted. Supported principals are users, role-assignable groups, and service principals. Supports $filter (eq, in).</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinition" /></td>
    <td><code></code></td>
    <td>The roleDefinition the assignment is for. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq, in).</td>
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
    <td><a href="#parameter-unified_role_assignment_id"><code>unified_role_assignment_id</code></a></td>
    <td></td>
    <td>Resource to grant access to users or groups.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of unifiedRoleAssignment objects for the RBAC provider. The following RBAC providers are currently supported:<br />- directory (Microsoft Entra ID)<br />- entitlement management (Microsoft Entra entitlement management)</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new unifiedRoleAssignment object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unified_role_assignment_id"><code>unified_role_assignment_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_role_assignment_id"><code>unified_role_assignment_id</code></a></td>
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
<tr id="parameter-unified_role_assignment_id">
    <td><CopyableCode code="unified_role_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleAssignment</td>
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

Resource to grant access to users or groups.

```sql
SELECT
id,
appScope,
appScopeId,
condition,
directoryScope,
directoryScopeId,
principal,
principalId,
roleDefinition,
roleDefinitionId
FROM entra_id.role_management.entitlement_management_role_assignments
WHERE unified_role_assignment_id = '{{ unified_role_assignment_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of unifiedRoleAssignment objects for the RBAC provider. The following RBAC providers are currently supported:<br />- directory (Microsoft Entra ID)<br />- entitlement management (Microsoft Entra entitlement management)

```sql
SELECT
id,
appScope,
appScopeId,
condition,
directoryScope,
directoryScopeId,
principal,
principalId,
roleDefinition,
roleDefinitionId
FROM entra_id.role_management.entitlement_management_role_assignments
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

Create a new unifiedRoleAssignment object.

```sql
INSERT INTO entra_id.role_management.entitlement_management_role_assignments (
id,
appScopeId,
condition,
directoryScopeId,
principalId,
roleDefinitionId,
appScope,
directoryScope,
principal,
roleDefinition
)
SELECT 
'{{ id }}',
'{{ appScopeId }}',
'{{ condition }}',
'{{ directoryScopeId }}',
'{{ principalId }}',
'{{ roleDefinitionId }}',
'{{ appScope }}',
'{{ directoryScope }}',
'{{ principal }}',
'{{ roleDefinition }}'
RETURNING
id,
appScope,
appScopeId,
condition,
directoryScope,
directoryScopeId,
principal,
principalId,
roleDefinition,
roleDefinitionId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_role_assignments
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: appScopeId
      value: "{{ appScopeId }}"
      description: |
        Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by a resource application only. For the entitlement management provider, use this property to specify a catalog. For example, /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997. Supports $filter (eq, in). For example, /roleManagement/entitlementManagement/roleAssignments?$filter=appScopeId eq '/AccessPackageCatalog/{catalog id}'.
    - name: condition
      value: "{{ condition }}"
    - name: directoryScopeId
      value: "{{ directoryScopeId }}"
      description: |
        Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications, unlike app scopes that are defined and understood by a resource application only. Supports $filter (eq, in).
    - name: principalId
      value: "{{ principalId }}"
      description: |
        Identifier of the principal to which the assignment is granted. Supported principals are users, role-assignable groups, and service principals. Supports $filter (eq, in).
    - name: roleDefinitionId
      value: "{{ roleDefinitionId }}"
      description: |
        Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq, in).
    - name: appScope
      value: "{{ appScope }}"
      description: |
        Read-only property with details of the app specific scope when the assignment scope is app specific. Containment entity. Supports $expand for the entitlement provider only.
    - name: directoryScope
      value: "{{ directoryScope }}"
      description: |
        The directory object that is the scope of the assignment. Read-only. Supports $expand for the directory provider.
    - name: principal
      value: "{{ principal }}"
      description: |
        Referencing the assigned principal. Read-only. Supports $expand except for the Exchange provider.
    - name: roleDefinition
      value: "{{ roleDefinition }}"
      description: |
        The roleDefinition the assignment is for. Supports $expand.
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
UPDATE entra_id.role_management.entitlement_management_role_assignments
SET 
id = '{{ id }}',
appScopeId = '{{ appScopeId }}',
condition = '{{ condition }}',
directoryScopeId = '{{ directoryScopeId }}',
principalId = '{{ principalId }}',
roleDefinitionId = '{{ roleDefinitionId }}',
appScope = '{{ appScope }}',
directoryScope = '{{ directoryScope }}',
principal = '{{ principal }}',
roleDefinition = '{{ roleDefinition }}'
WHERE 
unified_role_assignment_id = '{{ unified_role_assignment_id }}' --required
RETURNING
id,
appScope,
appScopeId,
condition,
directoryScope,
directoryScopeId,
principal,
principalId,
roleDefinition,
roleDefinitionId;
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
DELETE FROM entra_id.role_management.entitlement_management_role_assignments
WHERE unified_role_assignment_id = '{{ unified_role_assignment_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
