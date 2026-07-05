--- 
title: feature_rollout_policies_applies_to
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_rollout_policies_applies_to
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

Creates, updates, deletes, gets or lists a <code>feature_rollout_policies_applies_to</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="feature_rollout_policies_applies_to" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.feature_rollout_policies_applies_to" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a></td>
    <td></td>
    <td>Nullable. Specifies a list of directoryObject resources that feature is enabled for.</td>
</tr>
<tr>
    <td><a href="#add_ref"><CopyableCode code="add_ref" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a></td>
    <td></td>
    <td>Add an appliesTo on a featureRolloutPolicy object to specify the directoryObject to which the featureRolloutPolicy should be applied.</td>
</tr>
<tr>
    <td><a href="#remove_ref"><CopyableCode code="remove_ref" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a>, <a href="#parameter-directory_object_id"><code>directory_object_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove an appliesTo on a featureRolloutPolicy object to remove the directoryObject from feature rollout.</td>
</tr>
<tr>
    <td><a href="#remove_ref_2"><CopyableCode code="remove_ref_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove an appliesTo on a featureRolloutPolicy object to remove the directoryObject from feature rollout.</td>
</tr>
<tr>
    <td><a href="#create_applies_to"><CopyableCode code="create_applies_to" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-feature_rollout_policy_id"><code>feature_rollout_policy_id</code></a></td>
    <td></td>
    <td>Add an appliesTo on a featureRolloutPolicy object to specify the directoryObject to which the featureRolloutPolicy should be applied.</td>
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
<tr id="parameter-directory_object_id">
    <td><CopyableCode code="directory_object_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryObject</td>
</tr>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Nullable. Specifies a list of directoryObject resources that feature is enabled for.

```sql
SELECT
id,
deletedDateTime
FROM entra_id.policies.feature_rollout_policies_applies_to
WHERE feature_rollout_policy_id = '{{ feature_rollout_policy_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="add_ref"
    values={[
        { label: 'add_ref', value: 'add_ref' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="add_ref">

Add an appliesTo on a featureRolloutPolicy object to specify the directoryObject to which the featureRolloutPolicy should be applied.

```sql
INSERT INTO entra_id.policies.feature_rollout_policies_applies_to (
directoryObjectId,
feature_rollout_policy_id
)
SELECT 
'{{ directoryObjectId }}',
'{{ feature_rollout_policy_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: feature_rollout_policies_applies_to
  props:
    - name: feature_rollout_policy_id
      value: "{{ feature_rollout_policy_id }}"
      description: Required parameter for the feature_rollout_policies_applies_to resource.
    - name: directoryObjectId
      value: "{{ directoryObjectId }}"
      description: |
        The id of the directory object to reference (a user, group, service principal, device, ...). Sent on the wire as '@odata.id': 'https://graph.microsoft.com/v1.0/directoryObjects/{id}'.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="remove_ref"
    values={[
        { label: 'remove_ref', value: 'remove_ref' },
        { label: 'remove_ref_2', value: 'remove_ref_2' }
    ]}
>
<TabItem value="remove_ref">

Remove an appliesTo on a featureRolloutPolicy object to remove the directoryObject from feature rollout.

```sql
DELETE FROM entra_id.policies.feature_rollout_policies_applies_to
WHERE feature_rollout_policy_id = '{{ feature_rollout_policy_id }}' --required
AND directory_object_id = '{{ directory_object_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="remove_ref_2">

Remove an appliesTo on a featureRolloutPolicy object to remove the directoryObject from feature rollout.

```sql
DELETE FROM entra_id.policies.feature_rollout_policies_applies_to
AND feature_rollout_policy_id = '{{ feature_rollout_policy_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="create_applies_to"
    values={[
        { label: 'create_applies_to', value: 'create_applies_to' }
    ]}
>
<TabItem value="create_applies_to">

Add an appliesTo on a featureRolloutPolicy object to specify the directoryObject to which the featureRolloutPolicy should be applied.

```sql
EXEC entra_id.policies.feature_rollout_policies_applies_to.create_applies_to 
@feature_rollout_policy_id='{{ feature_rollout_policy_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
"deletedDateTime": "{{ deletedDateTime }}"
}'
;
```
</TabItem>
</Tabs>
