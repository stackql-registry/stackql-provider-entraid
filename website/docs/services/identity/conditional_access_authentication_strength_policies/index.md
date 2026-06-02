--- 
title: conditional_access_authentication_strength_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - conditional_access_authentication_strength_policies
  - identity
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

Creates, updates, deletes, gets or lists a <code>conditional_access_authentication_strength_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="conditional_access_authentication_strength_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity.conditional_access_authentication_strength_policies" /></td></tr>
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
    <td><CopyableCode code="allowedCombinations" /></td>
    <td><code>array</code></td>
    <td>A collection of authentication method modes that are required be used to satify this authentication strength.</td>
</tr>
<tr>
    <td><CopyableCode code="combinationConfigurations" /></td>
    <td><code>array</code></td>
    <td>Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime when this policy was created. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The human-readable description of this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The human-readable display name of this policy. Supports $filter (eq, ne, not , and in).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime when this policy was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td> (builtIn, custom, unknownFutureValue) (title: authenticationStrengthPolicyType)</td>
</tr>
<tr>
    <td><CopyableCode code="requirementsSatisfied" /></td>
    <td><code>string</code></td>
    <td> (none, mfa, unknownFutureValue) (title: authenticationStrengthRequirements)</td>
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
    <td><CopyableCode code="allowedCombinations" /></td>
    <td><code>array</code></td>
    <td>A collection of authentication method modes that are required be used to satify this authentication strength.</td>
</tr>
<tr>
    <td><CopyableCode code="combinationConfigurations" /></td>
    <td><code>array</code></td>
    <td>Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime when this policy was created. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The human-readable description of this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The human-readable display name of this policy. Supports $filter (eq, ne, not , and in).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The datetime when this policy was last modified. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="policyType" /></td>
    <td><code>string</code></td>
    <td> (builtIn, custom, unknownFutureValue) (title: authenticationStrengthPolicyType)</td>
</tr>
<tr>
    <td><CopyableCode code="requirementsSatisfied" /></td>
    <td><code>string</code></td>
    <td> (none, mfa, unknownFutureValue) (title: authenticationStrengthRequirements)</td>
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
    <td><a href="#parameter-authenticationStrengthPolicy-id"><code>authenticationStrengthPolicy-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.</td>
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
    <td><a href="#parameter-authenticationStrengthPolicy-id"><code>authenticationStrengthPolicy-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-authenticationStrengthPolicy-id"><code>authenticationStrengthPolicy-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update_allowed_combinations"><CopyableCode code="update_allowed_combinations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-authenticationStrengthPolicy-id"><code>authenticationStrengthPolicy-id</code></a></td>
    <td></td>
    <td>Update the allowedCombinations property of an authenticationStrengthPolicy object. To update other properties of an authenticationStrengthPolicy object, use the Update authenticationStrengthPolicy method.</td>
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
<tr id="parameter-authenticationStrengthPolicy-id">
    <td><CopyableCode code="authenticationStrengthPolicy-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of authenticationStrengthPolicy</td>
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

A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.

```sql
SELECT
id,
@odata.type,
allowedCombinations,
combinationConfigurations,
createdDateTime,
description,
displayName,
modifiedDateTime,
policyType,
requirementsSatisfied
FROM entraid.identity.conditional_access_authentication_strength_policies
WHERE authenticationStrengthPolicy-id = '{{ authenticationStrengthPolicy-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.

```sql
SELECT
id,
@odata.type,
allowedCombinations,
combinationConfigurations,
createdDateTime,
description,
displayName,
modifiedDateTime,
policyType,
requirementsSatisfied
FROM entraid.identity.conditional_access_authentication_strength_policies
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
INSERT INTO entraid.identity.conditional_access_authentication_strength_policies (
id,
@odata.type,
allowedCombinations,
createdDateTime,
description,
displayName,
modifiedDateTime,
policyType,
requirementsSatisfied,
combinationConfigurations
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ allowedCombinations }}',
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ modifiedDateTime }}',
'{{ policyType }}',
'{{ requirementsSatisfied }}',
'{{ combinationConfigurations }}'
RETURNING
id,
@odata.type,
allowedCombinations,
combinationConfigurations,
createdDateTime,
description,
displayName,
modifiedDateTime,
policyType,
requirementsSatisfied
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: conditional_access_authentication_strength_policies
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: allowedCombinations
      value:
        - "{{ allowedCombinations }}"
      description: |
        A collection of authentication method modes that are required be used to satify this authentication strength.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The datetime when this policy was created.
    - name: description
      value: "{{ description }}"
      description: |
        The human-readable description of this policy.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The human-readable display name of this policy. Supports $filter (eq, ne, not , and in).
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        The datetime when this policy was last modified.
    - name: policyType
      value: "{{ policyType }}"
      valid_values: ['builtIn', 'custom', 'unknownFutureValue']
    - name: requirementsSatisfied
      value: "{{ requirementsSatisfied }}"
      valid_values: ['none', 'mfa', 'unknownFutureValue']
    - name: combinationConfigurations
      description: |
        Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          appliesToCombinations: "{{ appliesToCombinations }}"
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
UPDATE entraid.identity.conditional_access_authentication_strength_policies
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
allowedCombinations = '{{ allowedCombinations }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
modifiedDateTime = '{{ modifiedDateTime }}',
policyType = '{{ policyType }}',
requirementsSatisfied = '{{ requirementsSatisfied }}',
combinationConfigurations = '{{ combinationConfigurations }}'
WHERE 
authenticationStrengthPolicy-id = '{{ authenticationStrengthPolicy-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
allowedCombinations,
combinationConfigurations,
createdDateTime,
description,
displayName,
modifiedDateTime,
policyType,
requirementsSatisfied;
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
DELETE FROM entraid.identity.conditional_access_authentication_strength_policies
WHERE authenticationStrengthPolicy-id = '{{ authenticationStrengthPolicy-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_allowed_combinations"
    values={[
        { label: 'update_allowed_combinations', value: 'update_allowed_combinations' }
    ]}
>
<TabItem value="update_allowed_combinations">

Update the allowedCombinations property of an authenticationStrengthPolicy object. To update other properties of an authenticationStrengthPolicy object, use the Update authenticationStrengthPolicy method.

```sql
EXEC entraid.identity.conditional_access_authentication_strength_policies.update_allowed_combinations 
@authenticationStrengthPolicy-id='{{ authenticationStrengthPolicy-id }}' --required 
@@json=
'{
"allowedCombinations": "{{ allowedCombinations }}"
}'
;
```
</TabItem>
</Tabs>
