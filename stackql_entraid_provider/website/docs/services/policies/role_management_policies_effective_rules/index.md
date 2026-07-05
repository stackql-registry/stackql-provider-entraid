--- 
title: role_management_policies_effective_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - role_management_policies_effective_rules
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

Creates, updates, deletes, gets or lists a <code>role_management_policies_effective_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_management_policies_effective_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.role_management_policies_effective_rules" /></td></tr>
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
    <td><CopyableCode code="target" /></td>
    <td><code></code></td>
    <td>Defines details of scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. Supports $filter (eq, ne).</td>
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
    <td><CopyableCode code="target" /></td>
    <td><code></code></td>
    <td>Defines details of scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. Supports $filter (eq, ne).</td>
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
    <td><a href="#parameter-unified_role_management_policy_id"><code>unified_role_management_policy_id</code></a>, <a href="#parameter-unified_role_management_policy_rule_id"><code>unified_role_management_policy_rule_id</code></a></td>
    <td></td>
    <td>The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-unified_role_management_policy_id"><code>unified_role_management_policy_id</code></a></td>
    <td></td>
    <td>The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-unified_role_management_policy_id"><code>unified_role_management_policy_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unified_role_management_policy_id"><code>unified_role_management_policy_id</code></a>, <a href="#parameter-unified_role_management_policy_rule_id"><code>unified_role_management_policy_rule_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unified_role_management_policy_id"><code>unified_role_management_policy_id</code></a>, <a href="#parameter-unified_role_management_policy_rule_id"><code>unified_role_management_policy_rule_id</code></a></td>
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
<tr id="parameter-unified_role_management_policy_id">
    <td><CopyableCode code="unified_role_management_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleManagementPolicy</td>
</tr>
<tr id="parameter-unified_role_management_policy_rule_id">
    <td><CopyableCode code="unified_role_management_policy_rule_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleManagementPolicyRule</td>
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

The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.

```sql
SELECT
id,
target
FROM entra_id.policies.role_management_policies_effective_rules
WHERE unified_role_management_policy_id = '{{ unified_role_management_policy_id }}' -- required
AND unified_role_management_policy_rule_id = '{{ unified_role_management_policy_rule_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.

```sql
SELECT
id,
target
FROM entra_id.policies.role_management_policies_effective_rules
WHERE unified_role_management_policy_id = '{{ unified_role_management_policy_id }}' -- required
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
INSERT INTO entra_id.policies.role_management_policies_effective_rules (
id,
target,
unified_role_management_policy_id
)
SELECT 
'{{ id }}',
'{{ target }}',
'{{ unified_role_management_policy_id }}'
RETURNING
id,
target
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: role_management_policies_effective_rules
  props:
    - name: unified_role_management_policy_id
      value: "{{ unified_role_management_policy_id }}"
      description: Required parameter for the role_management_policies_effective_rules resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: target
      value: "{{ target }}"
      description: |
        Defines details of scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. Supports $filter (eq, ne).
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
UPDATE entra_id.policies.role_management_policies_effective_rules
SET 
id = '{{ id }}',
target = '{{ target }}'
WHERE 
unified_role_management_policy_id = '{{ unified_role_management_policy_id }}' --required
AND unified_role_management_policy_rule_id = '{{ unified_role_management_policy_rule_id }}' --required
RETURNING
id,
target;
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
DELETE FROM entra_id.policies.role_management_policies_effective_rules
WHERE unified_role_management_policy_id = '{{ unified_role_management_policy_id }}' --required
AND unified_role_management_policy_rule_id = '{{ unified_role_management_policy_rule_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
