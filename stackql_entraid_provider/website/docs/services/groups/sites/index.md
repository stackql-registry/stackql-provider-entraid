--- 
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - groups
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

Creates, updates, deletes, gets or lists a <code>sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sites" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.groups.sites" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_path_2"
    values={[
        { label: 'get_by_path_2', value: 'get_by_path_2' },
        { label: 'get_by_path_3', value: 'get_by_path_3' },
        { label: 'get_by_path', value: 'get_by_path' }
    ]}
>
<TabItem value="get_by_path_2">

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
    <td><CopyableCode code="access" /></td>
    <td><code></code></td>
    <td>Statistics about the access actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="activities" /></td>
    <td><code>array</code></td>
    <td>Exposes the itemActivities represented in this itemActivityStat resource.</td>
</tr>
<tr>
    <td><CopyableCode code="create" /></td>
    <td><code></code></td>
    <td>Statistics about the create actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="delete" /></td>
    <td><code></code></td>
    <td>Statistics about the delete actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="edit" /></td>
    <td><code></code></td>
    <td>Statistics about the edit actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the interval ends. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="incompleteData" /></td>
    <td><code></code></td>
    <td>Indicates that the statistics in this interval are based on incomplete data. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="isTrending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the item is 'trending.' Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="move" /></td>
    <td><code></code></td>
    <td>Statistics about the move actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the interval starts. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_path_3">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the content type.</td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="associatedHubsUrls" /></td>
    <td><code>array</code></td>
    <td>List of canonical URLs for hub sites with which this content type is associated to. This will contain all hub sites where this content type is queued to be enforced or is already enforced. Enforcing a content type means that the content type is applied to the lists in the enforced sites.</td>
</tr>
<tr>
    <td><CopyableCode code="base" /></td>
    <td><code></code></td>
    <td>Parent contentType from which this content type is derived.</td>
</tr>
<tr>
    <td><CopyableCode code="baseTypes" /></td>
    <td><code>array</code></td>
    <td>The collection of content types that are ancestors of this content type.</td>
</tr>
<tr>
    <td><CopyableCode code="columnLinks" /></td>
    <td><code>array</code></td>
    <td>The collection of columns that are required by this content type.</td>
</tr>
<tr>
    <td><CopyableCode code="columnPositions" /></td>
    <td><code>array</code></td>
    <td>Column order information in a content type.</td>
</tr>
<tr>
    <td><CopyableCode code="columns" /></td>
    <td><code>array</code></td>
    <td>The collection of column definitions for this content type.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The descriptive text for the item.</td>
</tr>
<tr>
    <td><CopyableCode code="documentSet" /></td>
    <td><code></code></td>
    <td>Document Set metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="documentTemplate" /></td>
    <td><code></code></td>
    <td>Document template metadata. To make sure that documents have consistent content across a site and its subsites, you can associate a Word, Excel, or PowerPoint template with a site content type.</td>
</tr>
<tr>
    <td><CopyableCode code="group" /></td>
    <td><code>string</code></td>
    <td>The name of the group this content type belongs to. Helps organize related content types.</td>
</tr>
<tr>
    <td><CopyableCode code="hidden" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the content type is hidden in the list's 'New' menu.</td>
</tr>
<tr>
    <td><CopyableCode code="inheritedFrom" /></td>
    <td><code></code></td>
    <td>If this content type is inherited from another scope (like a site), provides a reference to the item where the content type is defined.</td>
</tr>
<tr>
    <td><CopyableCode code="isBuiltIn" /></td>
    <td><code>boolean</code></td>
    <td>Specifies if a content type is a built-in content type.</td>
</tr>
<tr>
    <td><CopyableCode code="order" /></td>
    <td><code></code></td>
    <td>Specifies the order in which the content type appears in the selection UI.</td>
</tr>
<tr>
    <td><CopyableCode code="parentId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the content type.</td>
</tr>
<tr>
    <td><CopyableCode code="propagateChanges" /></td>
    <td><code>boolean</code></td>
    <td>If true, any changes made to the content type are pushed to inherited content types and lists that implement the content type.</td>
</tr>
<tr>
    <td><CopyableCode code="readOnly" /></td>
    <td><code>boolean</code></td>
    <td>If true, the content type can't be modified unless this value is first set to false.</td>
</tr>
<tr>
    <td><CopyableCode code="sealed" /></td>
    <td><code>boolean</code></td>
    <td>If true, the content type can't be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_path">

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
    <td><CopyableCode code="access" /></td>
    <td><code></code></td>
    <td>Statistics about the access actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="activities" /></td>
    <td><code>array</code></td>
    <td>Exposes the itemActivities represented in this itemActivityStat resource.</td>
</tr>
<tr>
    <td><CopyableCode code="create" /></td>
    <td><code></code></td>
    <td>Statistics about the create actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="delete" /></td>
    <td><code></code></td>
    <td>Statistics about the delete actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="edit" /></td>
    <td><code></code></td>
    <td>Statistics about the edit actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the interval ends. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="incompleteData" /></td>
    <td><code></code></td>
    <td>Indicates that the statistics in this interval are based on incomplete data. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="isTrending" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the item is 'trending.' Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="move" /></td>
    <td><code></code></td>
    <td>Statistics about the move actions in this interval. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the interval starts. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#get_by_path_2"><CopyableCode code="get_by_path_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-site-id"><code>site-id</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-startDateTime"><code>startDateTime</code></a>, <a href="#parameter-endDateTime"><code>endDateTime</code></a>, <a href="#parameter-interval"><code>interval</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_by_path_3"><CopyableCode code="get_by_path_3" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-site-id"><code>site-id</code></a>, <a href="#parameter-path"><code>path</code></a>, <a href="#parameter-listId"><code>listId</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get site contentTypes that can be added to a list.</td>
</tr>
<tr>
    <td><a href="#get_by_path"><CopyableCode code="get_by_path" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-site-id"><code>site-id</code></a>, <a href="#parameter-path"><code>path</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
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
<tr id="parameter-endDateTime">
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string</code></td>
    <td>Usage: endDateTime='&#123;endDateTime&#125;'</td>
</tr>
<tr id="parameter-group-id">
    <td><CopyableCode code="group-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of group</td>
</tr>
<tr id="parameter-interval">
    <td><CopyableCode code="interval" /></td>
    <td><code>string</code></td>
    <td>Usage: interval='&#123;interval&#125;'</td>
</tr>
<tr id="parameter-listId">
    <td><CopyableCode code="listId" /></td>
    <td><code>string</code></td>
    <td>Usage: listId='&#123;listId&#125;'</td>
</tr>
<tr id="parameter-path">
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Usage: path='&#123;path&#125;'</td>
</tr>
<tr id="parameter-site-id">
    <td><CopyableCode code="site-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of site</td>
</tr>
<tr id="parameter-startDateTime">
    <td><CopyableCode code="startDateTime" /></td>
    <td><code>string</code></td>
    <td>Usage: startDateTime='&#123;startDateTime&#125;'</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_path_2"
    values={[
        { label: 'get_by_path_2', value: 'get_by_path_2' },
        { label: 'get_by_path_3', value: 'get_by_path_3' },
        { label: 'get_by_path', value: 'get_by_path' }
    ]}
>
<TabItem value="get_by_path_2">

Success

```sql
SELECT
id,
@odata.type,
access,
activities,
create,
delete,
edit,
endDateTime,
incompleteData,
isTrending,
move,
startDateTime
FROM entra_id.groups.sites
WHERE group-id = '{{ group-id }}' -- required
AND site-id = '{{ site-id }}' -- required
AND path = '{{ path }}' -- required
AND startDateTime = '{{ startDateTime }}' -- required
AND endDateTime = '{{ endDateTime }}' -- required
AND interval = '{{ interval }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $select = '{{ $select }}'
AND $orderby = '{{ $orderby }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_by_path_3">

Get site contentTypes that can be added to a list.

```sql
SELECT
id,
name,
@odata.type,
associatedHubsUrls,
base,
baseTypes,
columnLinks,
columnPositions,
columns,
description,
documentSet,
documentTemplate,
group,
hidden,
inheritedFrom,
isBuiltIn,
order,
parentId,
propagateChanges,
readOnly,
sealed
FROM entra_id.groups.sites
WHERE group-id = '{{ group-id }}' -- required
AND site-id = '{{ site-id }}' -- required
AND path = '{{ path }}' -- required
AND listId = '{{ listId }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $select = '{{ $select }}'
AND $orderby = '{{ $orderby }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_by_path">

Success

```sql
SELECT
id,
@odata.type,
access,
activities,
create,
delete,
edit,
endDateTime,
incompleteData,
isTrending,
move,
startDateTime
FROM entra_id.groups.sites
WHERE group-id = '{{ group-id }}' -- required
AND site-id = '{{ site-id }}' -- required
AND path = '{{ path }}' -- required
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $select = '{{ $select }}'
AND $orderby = '{{ $orderby }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
