--- 
title: b2x_user_flows_languages_default_pages
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_languages_default_pages
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_languages_default_pages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_languages_default_pages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_languages_default_pages" /></td></tr>
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
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a>, <a href="#parameter-user_flow_language_page_id"><code>user_flow_language_page_id</code></a></td>
    <td></td>
    <td>Collection of pages with the default content to display in a user flow for a specified language. This collection doesn't allow any kind of modification.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a></td>
    <td></td>
    <td>Read the values in a userFlowLanguagePage object for a language in a user flow. These values are shown to a user during a user journey defined by a user flow.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a>, <a href="#parameter-user_flow_language_page_id"><code>user_flow_language_page_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-b2x_identity_user_flow_id"><code>b2x_identity_user_flow_id</code></a>, <a href="#parameter-user_flow_language_configuration_id"><code>user_flow_language_configuration_id</code></a>, <a href="#parameter-user_flow_language_page_id"><code>user_flow_language_page_id</code></a></td>
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
<tr id="parameter-user_flow_language_page_id">
    <td><CopyableCode code="user_flow_language_page_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of userFlowLanguagePage</td>
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

Collection of pages with the default content to display in a user flow for a specified language. This collection doesn't allow any kind of modification.

```sql
SELECT
id
FROM entra_id.identity.b2x_user_flows_languages_default_pages
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
AND user_flow_language_configuration_id = '{{ user_flow_language_configuration_id }}' -- required
AND user_flow_language_page_id = '{{ user_flow_language_page_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Read the values in a userFlowLanguagePage object for a language in a user flow. These values are shown to a user during a user journey defined by a user flow.

```sql
SELECT
id
FROM entra_id.identity.b2x_user_flows_languages_default_pages
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' -- required
AND user_flow_language_configuration_id = '{{ user_flow_language_configuration_id }}' -- required
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
INSERT INTO entra_id.identity.b2x_user_flows_languages_default_pages (
id,
b2x_identity_user_flow_id,
user_flow_language_configuration_id
)
SELECT 
'{{ id }}',
'{{ b2x_identity_user_flow_id }}',
'{{ user_flow_language_configuration_id }}'
RETURNING
id
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: b2x_user_flows_languages_default_pages
  props:
    - name: b2x_identity_user_flow_id
      value: "{{ b2x_identity_user_flow_id }}"
      description: Required parameter for the b2x_user_flows_languages_default_pages resource.
    - name: user_flow_language_configuration_id
      value: "{{ user_flow_language_configuration_id }}"
      description: Required parameter for the b2x_user_flows_languages_default_pages resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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
UPDATE entra_id.identity.b2x_user_flows_languages_default_pages
SET 
id = '{{ id }}',
WHERE 
b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' --required
AND user_flow_language_configuration_id = '{{ user_flow_language_configuration_id }}' --required
AND user_flow_language_page_id = '{{ user_flow_language_page_id }}' --required
RETURNING
id,
@odata.type;
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
DELETE FROM entra_id.identity.b2x_user_flows_languages_default_pages
WHERE b2x_identity_user_flow_id = '{{ b2x_identity_user_flow_id }}' --required
AND user_flow_language_configuration_id = '{{ user_flow_language_configuration_id }}' --required
AND user_flow_language_page_id = '{{ user_flow_language_page_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
