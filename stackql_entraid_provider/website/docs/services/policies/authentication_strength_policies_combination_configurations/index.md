--- 
title: authentication_strength_policies_combination_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_strength_policies_combination_configurations
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

Creates, updates, deletes, gets or lists an <code>authentication_strength_policies_combination_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_strength_policies_combination_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.authentication_strength_policies_combination_configurations" /></td></tr>
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
    <td><CopyableCode code="appliesToCombinations" /></td>
    <td><code>array</code></td>
    <td>Which authentication method combinations this configuration applies to. Must be an allowedCombinations object, part of the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.</td>
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
    <td><CopyableCode code="appliesToCombinations" /></td>
    <td><code>array</code></td>
    <td>Which authentication method combinations this configuration applies to. Must be an allowedCombinations object, part of the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.</td>
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
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a>, <a href="#parameter-authentication_combination_configuration_id"><code>authentication_combination_configuration_id</code></a></td>
    <td></td>
    <td>Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a></td>
    <td></td>
    <td>Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a>, <a href="#parameter-authentication_combination_configuration_id"><code>authentication_combination_configuration_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a>, <a href="#parameter-authentication_combination_configuration_id"><code>authentication_combination_configuration_id</code></a></td>
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
<tr id="parameter-authentication_combination_configuration_id">
    <td><CopyableCode code="authentication_combination_configuration_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of authenticationCombinationConfiguration</td>
</tr>
<tr id="parameter-authentication_strength_policy_id">
    <td><CopyableCode code="authentication_strength_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of authenticationStrengthPolicy</td>
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

Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.

```sql
SELECT
id,
appliesToCombinations
FROM entra_id.policies.authentication_strength_policies_combination_configurations
WHERE authentication_strength_policy_id = '{{ authentication_strength_policy_id }}' -- required
AND authentication_combination_configuration_id = '{{ authentication_combination_configuration_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.

```sql
SELECT
id,
appliesToCombinations
FROM entra_id.policies.authentication_strength_policies_combination_configurations
WHERE authentication_strength_policy_id = '{{ authentication_strength_policy_id }}' -- required
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
INSERT INTO entra_id.policies.authentication_strength_policies_combination_configurations (
id,
appliesToCombinations,
authentication_strength_policy_id
)
SELECT 
'{{ id }}',
'{{ appliesToCombinations }}',
'{{ authentication_strength_policy_id }}'
RETURNING
id,
appliesToCombinations
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: authentication_strength_policies_combination_configurations
  props:
    - name: authentication_strength_policy_id
      value: "{{ authentication_strength_policy_id }}"
      description: Required parameter for the authentication_strength_policies_combination_configurations resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: appliesToCombinations
      value:
        - "{{ appliesToCombinations }}"
      description: |
        Which authentication method combinations this configuration applies to. Must be an allowedCombinations object, part of the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
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
UPDATE entra_id.policies.authentication_strength_policies_combination_configurations
SET 
id = '{{ id }}',
appliesToCombinations = '{{ appliesToCombinations }}'
WHERE 
authentication_strength_policy_id = '{{ authentication_strength_policy_id }}' --required
AND authentication_combination_configuration_id = '{{ authentication_combination_configuration_id }}' --required
RETURNING
id,
appliesToCombinations;
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
DELETE FROM entra_id.policies.authentication_strength_policies_combination_configurations
WHERE authentication_strength_policy_id = '{{ authentication_strength_policy_id }}' --required
AND authentication_combination_configuration_id = '{{ authentication_combination_configuration_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
