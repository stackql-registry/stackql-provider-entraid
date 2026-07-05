--- 
title: b2x_user_flows_languages
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_languages
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_languages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_languages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_languages" /></td></tr>
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
    <td><CopyableCode code="defaultPages" /></td>
    <td><code>array</code></td>
    <td>Collection of pages with the default content to display in a user flow for a specified language. This collection doesn't allow any kind of modification.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The language name to display. This property is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the language is enabled within the user flow.</td>
</tr>
<tr>
    <td><CopyableCode code="overridesPages" /></td>
    <td><code>array</code></td>
    <td>Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows you to modify the content of the page, any other modification isn't allowed (creation or deletion of pages).</td>
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
    <td><CopyableCode code="defaultPages" /></td>
    <td><code>array</code></td>
    <td>Collection of pages with the default content to display in a user flow for a specified language. This collection doesn't allow any kind of modification.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The language name to display. This property is read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the language is enabled within the user flow.</td>
</tr>
<tr>
    <td><CopyableCode code="overridesPages" /></td>
    <td><code>array</code></td>
    <td>Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows you to modify the content of the page, any other modification isn't allowed (creation or deletion of pages).</td>
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
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a userFlowLanguageConfiguration object. These objects represent a language available in a user flow. Note: Language customization is enabled by default in Microsoft Entra user flows.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td>Retrieve a list of languages supported for customization in a B2X user flow.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a></td>
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
<tr id="parameter-b2x_identity_user_flow_id">
    <td><CopyableCode code="b2x_identity_user_flow_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of b2xIdentityUserFlow</td>
</tr>
<tr id="parameter-user_flow_language_configuration_id">
    <td><CopyableCode code="user_flow_language_configuration_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of userFlowLanguageConfiguration</td>
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

Read the properties and relationships of a userFlowLanguageConfiguration object. These objects represent a language available in a user flow. Note: Language customization is enabled by default in Microsoft Entra user flows.

```sql
SELECT
id,
defaultPages,
displayName,
isEnabled,
overridesPages
FROM entra_id.identity.b2x_user_flows_languages
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
AND user_flow_language_configuration_id = '{{ user_flow_language_configuration_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of languages supported for customization in a B2X user flow.

```sql
SELECT
id,
defaultPages,
displayName,
isEnabled,
overridesPages
FROM entra_id.identity.b2x_user_flows_languages
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
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
INSERT INTO entra_id.identity.b2x_user_flows_languages (
id,
displayName,
isEnabled,
defaultPages,
overridesPages,
b2x_identity_user_flow_id
)
SELECT 
'{{ id }}',
'{{ displayName }}',
{{ isEnabled }},
'{{ defaultPages }}',
'{{ overridesPages }}',
'{{ b2x_identity_user_flow_id }}'
RETURNING
id,
defaultPages,
displayName,
isEnabled,
overridesPages
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: b2x_user_flows_languages
  props:
    - name: b2x_identity_user_flow_id
      value: "{{ b2x_identity_user_flow_id }}"
      description: Required parameter for the b2x_user_flows_languages resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The language name to display. This property is read-only.
    - name: isEnabled
      value: {{ isEnabled }}
      description: |
        Indicates whether the language is enabled within the user flow.
    - name: defaultPages
      description: |
        Collection of pages with the default content to display in a user flow for a specified language. This collection doesn't allow any kind of modification.
      value:
        - id: "{{ id }}"
    - name: overridesPages
      description: |
        Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows you to modify the content of the page, any other modification isn't allowed (creation or deletion of pages).
      value:
        - id: "{{ id }}"
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
UPDATE entra_id.identity.b2x_user_flows_languages
SET 
id = '{{ id }}',
displayName = '{{ displayName }}',
isEnabled = {{ isEnabled }},
defaultPages = '{{ defaultPages }}',
overridesPages = '{{ overridesPages }}'
WHERE 
b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' --required
AND user_flow_language_configuration_id = '{{ user_flow_language_configuration_id }}' --required
RETURNING
id,
defaultPages,
displayName,
isEnabled,
overridesPages;
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
DELETE FROM entra_id.identity.b2x_user_flows_languages
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' --required
AND user_flow_language_configuration_id = '{{ user_flow_language_configuration_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
