--- 
title: feature_rollout_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_rollout_policies
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

Creates, updates, deletes, gets or lists a <code>feature_rollout_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_rollout_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.feature_rollout_policies" /></td></tr>
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
    <td><CopyableCode code="appliesTo" /></td>
    <td><code>array</code></td>
    <td>Nullable. Specifies a list of directoryObject resources that feature is enabled for.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for this feature rollout policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for this  feature rollout policy.</td>
</tr>
<tr>
    <td><CopyableCode code="feature" /></td>
    <td><code>string</code></td>
    <td> (passthroughAuthentication, seamlessSso, passwordHashSync, emailAsAlternateId, unknownFutureValue, certificateBasedAuthentication, multiFactorAuthentication) (title: stagedFeatureName)</td>
</tr>
<tr>
    <td><CopyableCode code="isAppliedToOrganization" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this feature rollout policy should be applied to the entire organization.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the feature rollout is enabled.</td>
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
    <td><CopyableCode code="appliesTo" /></td>
    <td><code>array</code></td>
    <td>Nullable. Specifies a list of directoryObject resources that feature is enabled for.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for this feature rollout policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for this  feature rollout policy.</td>
</tr>
<tr>
    <td><CopyableCode code="feature" /></td>
    <td><code>string</code></td>
    <td> (passthroughAuthentication, seamlessSso, passwordHashSync, emailAsAlternateId, unknownFutureValue, certificateBasedAuthentication, multiFactorAuthentication) (title: stagedFeatureName)</td>
</tr>
<tr>
    <td><CopyableCode code="isAppliedToOrganization" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this feature rollout policy should be applied to the entire organization.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the feature rollout is enabled.</td>
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
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a></td>
    <td></td>
    <td>Retrieve the properties and relationships of a featureRolloutPolicy object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of featureRolloutPolicy objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new featureRolloutPolicy object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a></td>
    <td></td>
    <td>Update the properties of featureRolloutPolicy object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a featureRolloutPolicy object.</td>
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
<tr id="parameter-feature_rollout_policy_id">
    <td><CopyableCode code="feature_rollout_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of featureRolloutPolicy</td>
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

Retrieve the properties and relationships of a featureRolloutPolicy object.

```sql
SELECT
id,
appliesTo,
description,
displayName,
feature,
isAppliedToOrganization,
isEnabled
FROM entra_id.policies.feature_rollout_policies
WHERE feature_rollout_policy_id = '{{ feature_rollout_policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of featureRolloutPolicy objects.

```sql
SELECT
id,
appliesTo,
description,
displayName,
feature,
isAppliedToOrganization,
isEnabled
FROM entra_id.policies.feature_rollout_policies
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

Create a new featureRolloutPolicy object.

```sql
INSERT INTO entra_id.policies.feature_rollout_policies (
id,
description,
displayName,
feature,
isAppliedToOrganization,
isEnabled,
appliesTo
)
SELECT 
'{{ id }}',
'{{ description }}',
'{{ displayName }}',
'{{ feature }}',
{{ isAppliedToOrganization }},
{{ isEnabled }},
'{{ appliesTo }}'
RETURNING
id,
appliesTo,
description,
displayName,
feature,
isAppliedToOrganization,
isEnabled
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_rollout_policies
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        A description for this feature rollout policy.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for this  feature rollout policy.
    - name: feature
      value: "{{ feature }}"
      valid_values: ['passthroughAuthentication', 'seamlessSso', 'passwordHashSync', 'emailAsAlternateId', 'unknownFutureValue', 'certificateBasedAuthentication', 'multiFactorAuthentication']
    - name: isAppliedToOrganization
      value: {{ isAppliedToOrganization }}
      description: |
        Indicates whether this feature rollout policy should be applied to the entire organization.
    - name: isEnabled
      value: {{ isEnabled }}
      description: |
        Indicates whether the feature rollout is enabled.
    - name: appliesTo
      description: |
        Nullable. Specifies a list of directoryObject resources that feature is enabled for.
      value:
        - id: "{{ id }}"
          deletedDateTime: "{{ deletedDateTime }}"
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

Update the properties of featureRolloutPolicy object.

```sql
UPDATE entra_id.policies.feature_rollout_policies
SET 
id = '{{ id }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
feature = '{{ feature }}',
isAppliedToOrganization = {{ isAppliedToOrganization }},
isEnabled = {{ isEnabled }},
appliesTo = '{{ appliesTo }}'
WHERE 
feature_rollout_policy_id = '{{ feature_rollout_policy_id }}' --required
RETURNING
id,
appliesTo,
description,
displayName,
feature,
isAppliedToOrganization,
isEnabled;
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

Delete a featureRolloutPolicy object.

```sql
DELETE FROM entra_id.policies.feature_rollout_policies
WHERE feature_rollout_policy_id = '{{ feature_rollout_policy_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
