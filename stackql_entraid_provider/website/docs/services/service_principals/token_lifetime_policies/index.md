--- 
title: token_lifetime_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - token_lifetime_policies
  - service_principals
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

Creates, updates, deletes, gets or lists a <code>token_lifetime_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="token_lifetime_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.token_lifetime_policies" /></td></tr>
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
    <td><CopyableCode code="appliesTo" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>array</code></td>
    <td>A string collection containing a JSON string that defines the rules and settings for a policy. The syntax for the definition differs for each derived policy type. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name for this policy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="isOrganizationDefault" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, activates this policy. There can be many policies for the same policy type, but only one can be activated as the organization default. Optional, default value is false.</td>
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
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>List the tokenLifetimePolicy objects that are assigned to a servicePrincipal. Only one object is returned in the collection because only one tokenLifetimePolicy can be assigned to a service principal.</td>
</tr>
<tr>
    <td><a href="#add_ref"><CopyableCode code="add_ref" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td></td>
    <td>Assign a tokenLifetimePolicy to a servicePrincipal. You can have multiple tokenLifetimePolicy policies in a tenant but can assign only one tokenLifetimePolicy per service principal.</td>
</tr>
<tr>
    <td><a href="#remove_ref"><CopyableCode code="remove_ref" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a>, <a href="#parameter-token_lifetime_policy_id"><code>token_lifetime_policy_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a tokenLifetimePolicy object from a service principal.</td>
</tr>
<tr>
    <td><a href="#remove_ref_2"><CopyableCode code="remove_ref_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_principal_id"><code>service_principal_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove a tokenLifetimePolicy object from a service principal.</td>
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
<tr id="parameter-service_principal_id">
    <td><CopyableCode code="service_principal_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
</tr>
<tr id="parameter-token_lifetime_policy_id">
    <td><CopyableCode code="token_lifetime_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of tokenLifetimePolicy</td>
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

List the tokenLifetimePolicy objects that are assigned to a servicePrincipal. Only one object is returned in the collection because only one tokenLifetimePolicy can be assigned to a service principal.

```sql
SELECT
id,
appliesTo,
definition,
deletedDateTime,
description,
displayName,
isOrganizationDefault
FROM entra_id.service_principals.token_lifetime_policies
WHERE service_principal_id = '{{ service_principal_id }}' -- required
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

Assign a tokenLifetimePolicy to a servicePrincipal. You can have multiple tokenLifetimePolicy policies in a tenant but can assign only one tokenLifetimePolicy per service principal.

```sql
INSERT INTO entra_id.service_principals.token_lifetime_policies (
directoryObjectId,
service_principal_id
)
SELECT 
'{{ directoryObjectId }}',
'{{ service_principal_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: token_lifetime_policies
  props:
    - name: service_principal_id
      value: "{{ service_principal_id }}"
      description: Required parameter for the token_lifetime_policies resource.
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

Remove a tokenLifetimePolicy object from a service principal.

```sql
DELETE FROM entra_id.service_principals.token_lifetime_policies
WHERE service_principal_id = '{{ service_principal_id }}' --required
AND token_lifetime_policy_id = '{{ token_lifetime_policy_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="remove_ref_2">

Remove a tokenLifetimePolicy object from a service principal.

```sql
DELETE FROM entra_id.service_principals.token_lifetime_policies
AND service_principal_id = '{{ service_principal_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
