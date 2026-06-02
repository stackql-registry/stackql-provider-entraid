--- 
title: role_management_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - role_management_policies
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

Creates, updates, deletes, gets or lists a <code>role_management_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="role_management_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.role_management_policies" /></td></tr>
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
    <td>Description for the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveRules" /></td>
    <td><code>array</code></td>
    <td>The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isOrganizationDefault" /></td>
    <td><code>boolean</code></td>
    <td>This can only be set to true for a single tenant-wide policy which will apply to all scopes and roles. Set the scopeId to / and scopeType to Directory. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code></code></td>
    <td>The identity who last modified the role setting.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the role setting was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>The collection of rules like approval rules and expiration rules. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the scope where the policy is created. Can be / for the tenant or a group ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeType" /></td>
    <td><code>string</code></td>
    <td>The type of the scope where the policy is created. One of Directory, DirectoryRole, Group. Required.</td>
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
    <td>Description for the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveRules" /></td>
    <td><code>array</code></td>
    <td>The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="isOrganizationDefault" /></td>
    <td><code>boolean</code></td>
    <td>This can only be set to true for a single tenant-wide policy which will apply to all scopes and roles. Set the scopeId to / and scopeType to Directory. Supports $filter (eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code></code></td>
    <td>The identity who last modified the role setting.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the role setting was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>array</code></td>
    <td>The collection of rules like approval rules and expiration rules. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the scope where the policy is created. Can be / for the tenant or a group ID. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scopeType" /></td>
    <td><code>string</code></td>
    <td>The type of the scope where the policy is created. One of Directory, DirectoryRole, Group. Required.</td>
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
    <td><a href="#parameter-unifiedRoleManagementPolicy-id"><code>unifiedRoleManagementPolicy-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the details of a role management policy.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the details of the policies in PIM that can be applied to Microsoft Entra roles or group membership or ownership. To retrieve policies that apply to Azure RBAC, use the Azure REST PIM API for role management policies.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-unifiedRoleManagementPolicy-id"><code>unifiedRoleManagementPolicy-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-unifiedRoleManagementPolicy-id"><code>unifiedRoleManagementPolicy-id</code></a></td>
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
<tr id="parameter-unifiedRoleManagementPolicy-id">
    <td><CopyableCode code="unifiedRoleManagementPolicy-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of unifiedRoleManagementPolicy</td>
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

Retrieve the details of a role management policy.

```sql
SELECT
id,
@odata.type,
description,
displayName,
effectiveRules,
isOrganizationDefault,
lastModifiedBy,
lastModifiedDateTime,
rules,
scopeId,
scopeType
FROM entra_id.policies.role_management_policies
WHERE unifiedRoleManagementPolicy-id = '{{ unifiedRoleManagementPolicy-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get the details of the policies in PIM that can be applied to Microsoft Entra roles or group membership or ownership. To retrieve policies that apply to Azure RBAC, use the Azure REST PIM API for role management policies.

```sql
SELECT
id,
@odata.type,
description,
displayName,
effectiveRules,
isOrganizationDefault,
lastModifiedBy,
lastModifiedDateTime,
rules,
scopeId,
scopeType
FROM entra_id.policies.role_management_policies
WHERE $top = '{{ $top }}'
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
INSERT INTO entra_id.policies.role_management_policies (
id,
@odata.type,
description,
displayName,
isOrganizationDefault,
lastModifiedBy,
lastModifiedDateTime,
scopeId,
scopeType,
effectiveRules,
rules
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ description }}',
'{{ displayName }}',
{{ isOrganizationDefault }},
'{{ lastModifiedBy }}',
'{{ lastModifiedDateTime }}',
'{{ scopeId }}',
'{{ scopeType }}',
'{{ effectiveRules }}',
'{{ rules }}'
RETURNING
id,
@odata.type,
description,
displayName,
effectiveRules,
isOrganizationDefault,
lastModifiedBy,
lastModifiedDateTime,
rules,
scopeId,
scopeType
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: role_management_policies
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: description
      value: "{{ description }}"
      description: |
        Description for the policy.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name for the policy.
    - name: isOrganizationDefault
      value: {{ isOrganizationDefault }}
      description: |
        This can only be set to true for a single tenant-wide policy which will apply to all scopes and roles. Set the scopeId to / and scopeType to Directory. Supports $filter (eq, ne).
    - name: lastModifiedBy
      value: "{{ lastModifiedBy }}"
      description: |
        The identity who last modified the role setting.
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        The time when the role setting was last modified.
    - name: scopeId
      value: "{{ scopeId }}"
      description: |
        The identifier of the scope where the policy is created. Can be / for the tenant or a group ID. Required.
    - name: scopeType
      value: "{{ scopeType }}"
      description: |
        The type of the scope where the policy is created. One of Directory, DirectoryRole, Group. Required.
    - name: effectiveRules
      description: |
        The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          target: "{{ target }}"
    - name: rules
      description: |
        The collection of rules like approval rules and expiration rules. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          target: "{{ target }}"
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
UPDATE entra_id.policies.role_management_policies
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isOrganizationDefault = {{ isOrganizationDefault }},
lastModifiedBy = '{{ lastModifiedBy }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
scopeId = '{{ scopeId }}',
scopeType = '{{ scopeType }}',
effectiveRules = '{{ effectiveRules }}',
rules = '{{ rules }}'
WHERE 
unifiedRoleManagementPolicy-id = '{{ unifiedRoleManagementPolicy-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
description,
displayName,
effectiveRules,
isOrganizationDefault,
lastModifiedBy,
lastModifiedDateTime,
rules,
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
DELETE FROM entra_id.policies.role_management_policies
WHERE unifiedRoleManagementPolicy-id = '{{ unifiedRoleManagementPolicy-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
