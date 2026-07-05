--- 
title: authentication_methods_policy_authentication_method_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_methods_policy_authentication_method_configurations
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

Creates, updates, deletes, gets or lists an <code>authentication_methods_policy_authentication_method_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_methods_policy_authentication_method_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.authentication_methods_policy_authentication_method_configurations" /></td></tr>
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
    <td><CopyableCode code="excludeTargets" /></td>
    <td><code>array</code></td>
    <td>Groups of users that are excluded from a policy.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The state of the policy. The possible values are: enabled, disabled.</td>
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
    <td><CopyableCode code="excludeTargets" /></td>
    <td><code>array</code></td>
    <td>Groups of users that are excluded from a policy.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The state of the policy. The possible values are: enabled, disabled.</td>
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
    <td><a href="#parameter-authentication_method_configuration_id"><code>authentication_method_configuration_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of an externalAuthenticationMethodConfiguration object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Read the properties and relationships of an externalAuthenticationMethodConfiguration object.</td>
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
    <td><a href="#parameter-authentication_method_configuration_id"><code>authentication_method_configuration_id</code></a></td>
    <td></td>
    <td>Update the properties of an externalAuthenticationMethodConfiguration object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-authentication_method_configuration_id"><code>authentication_method_configuration_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an externalAuthenticationMethodConfiguration object.</td>
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
<tr id="parameter-authentication_method_configuration_id">
    <td><CopyableCode code="authentication_method_configuration_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of authenticationMethodConfiguration</td>
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

Read the properties and relationships of an externalAuthenticationMethodConfiguration object.

```sql
SELECT
id,
excludeTargets,
state
FROM entra_id.policies.authentication_methods_policy_authentication_method_configurations
WHERE authentication_method_configuration_id = '{{ authentication_method_configuration_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Read the properties and relationships of an externalAuthenticationMethodConfiguration object.

```sql
SELECT
id,
excludeTargets,
state
FROM entra_id.policies.authentication_methods_policy_authentication_method_configurations
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
INSERT INTO entra_id.policies.authentication_methods_policy_authentication_method_configurations (
id,
excludeTargets,
state
)
SELECT 
'{{ id }}',
'{{ excludeTargets }}',
'{{ state }}'
RETURNING
id,
excludeTargets,
state
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: authentication_methods_policy_authentication_method_configurations
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: excludeTargets
      description: |
        Groups of users that are excluded from a policy.
      value:
        - id: "{{ id }}"
          targetType: "{{ targetType }}"
    - name: state
      value: "{{ state }}"
      description: |
        The state of the policy. The possible values are: enabled, disabled.
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

Update the properties of an externalAuthenticationMethodConfiguration object.

```sql
UPDATE entra_id.policies.authentication_methods_policy_authentication_method_configurations
SET 
id = '{{ id }}',
excludeTargets = '{{ excludeTargets }}',
state = '{{ state }}'
WHERE 
authentication_method_configuration_id = '{{ authentication_method_configuration_id }}' --required
RETURNING
id,
excludeTargets,
state;
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

Delete an externalAuthenticationMethodConfiguration object.

```sql
DELETE FROM entra_id.policies.authentication_methods_policy_authentication_method_configurations
WHERE authentication_method_configuration_id = '{{ authentication_method_configuration_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
