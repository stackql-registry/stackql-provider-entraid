--- 
title: b2x_user_flows_languages_overrides_pages
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_languages_overrides_pages
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_languages_overrides_pages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_languages_overrides_pages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_languages_overrides_pages" /></td></tr>
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
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-userFlowLanguageConfiguration-id"><code>userFlowLanguageConfiguration-id</code></a>, <a href="#parameter-userFlowLanguagePage-id"><code>userFlowLanguagePage-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows you to modify the content of the page, any other modification isn't allowed (creation or deletion of pages).</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-userFlowLanguageConfiguration-id"><code>userFlowLanguageConfiguration-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the userFlowLanguagePage resources from the overridesPages navigation property. These pages are used to customize the values shown to the user during a user journey in a user flow.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-userFlowLanguageConfiguration-id"><code>userFlowLanguageConfiguration-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-userFlowLanguageConfiguration-id"><code>userFlowLanguageConfiguration-id</code></a>, <a href="#parameter-userFlowLanguagePage-id"><code>userFlowLanguagePage-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the values in an userFlowLanguagePage object. You may only update the values in an overridesPage, which is used to customize the values shown to a user during a user journey defined by a user flow.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-userFlowLanguageConfiguration-id"><code>userFlowLanguageConfiguration-id</code></a>, <a href="#parameter-userFlowLanguagePage-id"><code>userFlowLanguagePage-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes the values in an userFlowLanguagePage object. You may only delete the values in an overridesPage, which is used to customize the values shown to a user during a user journey defined by a user flow.</td>
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
<tr id="parameter-b2xIdentityUserFlow-id">
    <td><CopyableCode code="b2xIdentityUserFlow-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of b2xIdentityUserFlow</td>
</tr>
<tr id="parameter-userFlowLanguageConfiguration-id">
    <td><CopyableCode code="userFlowLanguageConfiguration-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of userFlowLanguageConfiguration</td>
</tr>
<tr id="parameter-userFlowLanguagePage-id">
    <td><CopyableCode code="userFlowLanguagePage-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of userFlowLanguagePage</td>
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

Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows you to modify the content of the page, any other modification isn't allowed (creation or deletion of pages).

```sql
SELECT
id,
@odata.type
FROM entra_id.identity.b2x_user_flows_languages_overrides_pages
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' -- required
AND userFlowLanguageConfiguration-id = '{{ userFlowLanguageConfiguration-id }}' -- required
AND userFlowLanguagePage-id = '{{ userFlowLanguagePage-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get the userFlowLanguagePage resources from the overridesPages navigation property. These pages are used to customize the values shown to the user during a user journey in a user flow.

```sql
SELECT
id,
@odata.type
FROM entra_id.identity.b2x_user_flows_languages_overrides_pages
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' -- required
AND userFlowLanguageConfiguration-id = '{{ userFlowLanguageConfiguration-id }}' -- required
AND $top = '{{ $top }}'
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
INSERT INTO entra_id.identity.b2x_user_flows_languages_overrides_pages (
id,
@odata.type,
b2xIdentityUserFlow-id,
userFlowLanguageConfiguration-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ b2xIdentityUserFlow-id }}',
'{{ userFlowLanguageConfiguration-id }}'
RETURNING
id,
@odata.type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: b2x_user_flows_languages_overrides_pages
  props:
    - name: b2xIdentityUserFlow-id
      value: "{{ b2xIdentityUserFlow-id }}"
      description: Required parameter for the b2x_user_flows_languages_overrides_pages resource.
    - name: userFlowLanguageConfiguration-id
      value: "{{ userFlowLanguageConfiguration-id }}"
      description: Required parameter for the b2x_user_flows_languages_overrides_pages resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
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

Update the values in an userFlowLanguagePage object. You may only update the values in an overridesPage, which is used to customize the values shown to a user during a user journey defined by a user flow.

```sql
UPDATE entra_id.identity.b2x_user_flows_languages_overrides_pages
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}'
WHERE 
b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' --required
AND userFlowLanguageConfiguration-id = '{{ userFlowLanguageConfiguration-id }}' --required
AND userFlowLanguagePage-id = '{{ userFlowLanguagePage-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
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

Deletes the values in an userFlowLanguagePage object. You may only delete the values in an overridesPage, which is used to customize the values shown to a user during a user journey defined by a user flow.

```sql
DELETE FROM entra_id.identity.b2x_user_flows_languages_overrides_pages
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' --required
AND userFlowLanguageConfiguration-id = '{{ userFlowLanguageConfiguration-id }}' --required
AND userFlowLanguagePage-id = '{{ userFlowLanguagePage-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
