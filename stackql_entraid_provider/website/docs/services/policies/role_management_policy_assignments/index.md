--- 
title: role_management_policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_management_policy_assignments
  - policies
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

Creates, updates, deletes, gets or lists a <code>role_management_policy_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_management_policy_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.role_management_policy_assignments" /></td></tr>
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
    <td><CopyableCode code="policy" /></td>
    <td><code></code></td>
    <td>The policy that's associated with a policy assignment. Supports $expand and a nested $expand of the rules and effectiveRules relationships for the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The id of the policy. Inherited from entity.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>For Microsoft Entra roles policy, it's the identifier of the role definition object where the policy applies. For PIM for Groups membership and ownership, it's either member or owner. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="scopeId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the scope where the policy is assigned. Can be / for the tenant or a group ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeType" /></td>
    <td><code>string</code></td>
    <td>The type of the scope where the policy is assigned. One of Directory, DirectoryRole, Group. Required.</td>
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
    <td><CopyableCode code="policy" /></td>
    <td><code></code></td>
    <td>The policy that's associated with a policy assignment. Supports $expand and a nested $expand of the rules and effectiveRules relationships for the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policyId" /></td>
    <td><code>string</code></td>
    <td>The id of the policy. Inherited from entity.</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>For Microsoft Entra roles policy, it's the identifier of the role definition object where the policy applies. For PIM for Groups membership and ownership, it's either member or owner. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="scopeId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the scope where the policy is assigned. Can be / for the tenant or a group ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeType" /></td>
    <td><code>string</code></td>
    <td>The type of the scope where the policy is assigned. One of Directory, DirectoryRole, Group. Required.</td>
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
    <td><a href="#parameter-unified_role_management_policy_assignment_id"><code>unified_role_management_policy_assignment_id</code></a></td>
    <td></td>
    <td>Get the details of a policy assignment in PIM that's assigned to Microsoft Entra roles or group membership or ownership.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get the details of all role management policy assignments made in PIM for Microsoft Entra roles and PIM for Groups.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unified_role_management_policy_assignment_id"><code>unified_role_management_policy_assignment_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_role_management_policy_assignment_id"><code>unified_role_management_policy_assignment_id</code></a></td>
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
<tr id="parameter-unified_role_management_policy_assignment_id">
    <td><CopyableCode code="unified_role_management_policy_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleManagementPolicyAssignment</td>
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

Get the details of a policy assignment in PIM that's assigned to Microsoft Entra roles or group membership or ownership.

```sql
SELECT
id,
policy,
policyId,
roleDefinitionId,
scopeId,
scopeType
FROM entra_id.policies.role_management_policy_assignments
WHERE unified_role_management_policy_assignment_id = '{{ unified_role_management_policy_assignment_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the details of all role management policy assignments made in PIM for Microsoft Entra roles and PIM for Groups.

```sql
SELECT
id,
policy,
policyId,
roleDefinitionId,
scopeId,
scopeType
FROM entra_id.policies.role_management_policy_assignments
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
INSERT INTO entra_id.policies.role_management_policy_assignments (
id,
policyId,
roleDefinitionId,
scopeId,
scopeType,
policy
)
SELECT 
'{{ id }}',
'{{ policyId }}',
'{{ roleDefinitionId }}',
'{{ scopeId }}',
'{{ scopeType }}',
'{{ policy }}'
RETURNING
id,
policy,
policyId,
roleDefinitionId,
scopeId,
scopeType
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: role_management_policy_assignments
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: policyId
      value: "{{ policyId }}"
      description: |
        The id of the policy. Inherited from entity.
    - name: roleDefinitionId
      value: "{{ roleDefinitionId }}"
      description: |
        For Microsoft Entra roles policy, it's the identifier of the role definition object where the policy applies. For PIM for Groups membership and ownership, it's either member or owner. Supports $filter (eq).
    - name: scopeId
      value: "{{ scopeId }}"
      description: |
        The identifier of the scope where the policy is assigned. Can be / for the tenant or a group ID. Required.
    - name: scopeType
      value: "{{ scopeType }}"
      description: |
        The type of the scope where the policy is assigned. One of Directory, DirectoryRole, Group. Required.
    - name: policy
      value: "{{ policy }}"
      description: |
        The policy that's associated with a policy assignment. Supports $expand and a nested $expand of the rules and effectiveRules relationships for the policy.
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
UPDATE entra_id.policies.role_management_policy_assignments
SET 
id = '{{ id }}',
policyId = '{{ policyId }}',
roleDefinitionId = '{{ roleDefinitionId }}',
scopeId = '{{ scopeId }}',
scopeType = '{{ scopeType }}',
policy = '{{ policy }}'
WHERE 
unified_role_management_policy_assignment_id = '{{ unified_role_management_policy_assignment_id }}' --required
RETURNING
id,
policy,
policyId,
roleDefinitionId,
scopeId,
scopeType;
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
DELETE FROM entra_id.policies.role_management_policy_assignments
WHERE unified_role_management_policy_assignment_id = '{{ unified_role_management_policy_assignment_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
