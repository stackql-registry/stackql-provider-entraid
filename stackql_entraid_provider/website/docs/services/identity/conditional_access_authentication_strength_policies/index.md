--- 
title: conditional_access_authentication_strength_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - conditional_access_authentication_strength_policies
  - identity
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

Creates, updates, deletes, gets or lists a <code>conditional_access_authentication_strength_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="conditional_access_authentication_strength_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.conditional_access_authentication_strength_policies" /></td></tr>
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
    <td>The datetime when this policy was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The datetime when this policy was last modified. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The datetime when this policy was created. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The datetime when this policy was last modified. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a></td>
    <td></td>
    <td>A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.</td>
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
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update_allowed_combinations"><CopyableCode code="update_allowed_combinations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-authentication_strength_policy_id"><code>authentication_strength_policy_id</code></a></td>
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

A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.

```sql
SELECT
id,
allowedCombinations,
combinationConfigurations,
createdDateTime,
description,
displayName,
modifiedDateTime,
policyType,
requirementsSatisfied
FROM entra_id.identity.conditional_access_authentication_strength_policies
WHERE authentication_strength_policy_id = '{{ authentication_strength_policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.

```sql
SELECT
id,
allowedCombinations,
combinationConfigurations,
createdDateTime,
description,
displayName,
modifiedDateTime,
policyType,
requirementsSatisfied
FROM entra_id.identity.conditional_access_authentication_strength_policies
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
INSERT INTO entra_id.identity.conditional_access_authentication_strength_policies (
id,
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
UPDATE entra_id.identity.conditional_access_authentication_strength_policies
SET 
id = '{{ id }}',
allowedCombinations = '{{ allowedCombinations }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
modifiedDateTime = '{{ modifiedDateTime }}',
policyType = '{{ policyType }}',
requirementsSatisfied = '{{ requirementsSatisfied }}',
combinationConfigurations = '{{ combinationConfigurations }}'
WHERE 
authentication_strength_policy_id = '{{ authentication_strength_policy_id }}' --required
RETURNING
id,
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
DELETE FROM entra_id.identity.conditional_access_authentication_strength_policies
WHERE authentication_strength_policy_id = '{{ authentication_strength_policy_id }}' --required
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
EXEC entra_id.identity.conditional_access_authentication_strength_policies.update_allowed_combinations 
@authentication_strength_policy_id='{{ authentication_strength_policy_id }}' --required 
@@json=
'{
"allowedCombinations": "{{ allowedCombinations }}"
}'
;
```
</TabItem>
</Tabs>
