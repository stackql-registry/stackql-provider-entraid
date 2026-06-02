--- 
title: entitlement_management_assignment_policies_questions
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_assignment_policies_questions
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_assignment_policies_questions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_assignment_policies_questions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.entitlement_management_assignment_policies_questions" /></td></tr>
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
    <td><CopyableCode code="isAnswerEditable" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.</td>
</tr>
<tr>
    <td><CopyableCode code="isRequired" /></td>
    <td><code>boolean</code></td>
    <td>Whether the requestor is required to supply an answer or not.</td>
</tr>
<tr>
    <td><CopyableCode code="localizations" /></td>
    <td><code>array</code></td>
    <td>The text of the question represented in a format for a specific locale.</td>
</tr>
<tr>
    <td><CopyableCode code="sequence" /></td>
    <td><code>number (int32)</code></td>
    <td>Relative position of this question when displaying a list of questions to the requestor.</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>The text of the question to show to the requestor.</td>
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
    <td><CopyableCode code="isAnswerEditable" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.</td>
</tr>
<tr>
    <td><CopyableCode code="isRequired" /></td>
    <td><code>boolean</code></td>
    <td>Whether the requestor is required to supply an answer or not.</td>
</tr>
<tr>
    <td><CopyableCode code="localizations" /></td>
    <td><code>array</code></td>
    <td>The text of the question represented in a format for a specific locale.</td>
</tr>
<tr>
    <td><CopyableCode code="sequence" /></td>
    <td><code>number (int32)</code></td>
    <td>Relative position of this question when displaying a list of questions to the requestor.</td>
</tr>
<tr>
    <td><CopyableCode code="text" /></td>
    <td><code>string</code></td>
    <td>The text of the question to show to the requestor.</td>
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
    <td><a href="#parameter-accessPackageAssignmentPolicy-id"><code>accessPackageAssignmentPolicy-id</code></a>, <a href="#parameter-accessPackageQuestion-id"><code>accessPackageQuestion-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Questions that are posed to the  requestor.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-accessPackageAssignmentPolicy-id"><code>accessPackageAssignmentPolicy-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Questions that are posed to the  requestor.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-accessPackageAssignmentPolicy-id"><code>accessPackageAssignmentPolicy-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessPackageAssignmentPolicy-id"><code>accessPackageAssignmentPolicy-id</code></a>, <a href="#parameter-accessPackageQuestion-id"><code>accessPackageQuestion-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessPackageAssignmentPolicy-id"><code>accessPackageAssignmentPolicy-id</code></a>, <a href="#parameter-accessPackageQuestion-id"><code>accessPackageQuestion-id</code></a></td>
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
<tr id="parameter-accessPackageAssignmentPolicy-id">
    <td><CopyableCode code="accessPackageAssignmentPolicy-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageAssignmentPolicy</td>
</tr>
<tr id="parameter-accessPackageQuestion-id">
    <td><CopyableCode code="accessPackageQuestion-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageQuestion</td>
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

Questions that are posed to the  requestor.

```sql
SELECT
id,
@odata.type,
isAnswerEditable,
isRequired,
localizations,
sequence,
text
FROM entraid.identity_governance.entitlement_management_assignment_policies_questions
WHERE accessPackageAssignmentPolicy-id = '{{ accessPackageAssignmentPolicy-id }}' -- required
AND accessPackageQuestion-id = '{{ accessPackageQuestion-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Questions that are posed to the  requestor.

```sql
SELECT
id,
@odata.type,
isAnswerEditable,
isRequired,
localizations,
sequence,
text
FROM entraid.identity_governance.entitlement_management_assignment_policies_questions
WHERE accessPackageAssignmentPolicy-id = '{{ accessPackageAssignmentPolicy-id }}' -- required
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
INSERT INTO entraid.identity_governance.entitlement_management_assignment_policies_questions (
id,
@odata.type,
isAnswerEditable,
isRequired,
localizations,
sequence,
text,
accessPackageAssignmentPolicy-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
{{ isAnswerEditable }},
{{ isRequired }},
'{{ localizations }}',
{{ sequence }},
'{{ text }}',
'{{ accessPackageAssignmentPolicy-id }}'
RETURNING
id,
@odata.type,
isAnswerEditable,
isRequired,
localizations,
sequence,
text
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_assignment_policies_questions
  props:
    - name: accessPackageAssignmentPolicy-id
      value: "{{ accessPackageAssignmentPolicy-id }}"
      description: Required parameter for the entitlement_management_assignment_policies_questions resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: isAnswerEditable
      value: {{ isAnswerEditable }}
      description: |
        Specifies whether the requestor is allowed to edit answers to questions for an assignment by posting an update to accessPackageAssignmentRequest.
    - name: isRequired
      value: {{ isRequired }}
      description: |
        Whether the requestor is required to supply an answer or not.
    - name: localizations
      description: |
        The text of the question represented in a format for a specific locale.
      value:
        - languageCode: "{{ languageCode }}"
          text: "{{ text }}"
          @odata.type: "{{ @odata.type }}"
    - name: sequence
      value: {{ sequence }}
      description: |
        Relative position of this question when displaying a list of questions to the requestor.
    - name: text
      value: "{{ text }}"
      description: |
        The text of the question to show to the requestor.
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
UPDATE entraid.identity_governance.entitlement_management_assignment_policies_questions
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
isAnswerEditable = {{ isAnswerEditable }},
isRequired = {{ isRequired }},
localizations = '{{ localizations }}',
sequence = {{ sequence }},
text = '{{ text }}'
WHERE 
accessPackageAssignmentPolicy-id = '{{ accessPackageAssignmentPolicy-id }}' --required
AND accessPackageQuestion-id = '{{ accessPackageQuestion-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
isAnswerEditable,
isRequired,
localizations,
sequence,
text;
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
DELETE FROM entraid.identity_governance.entitlement_management_assignment_policies_questions
WHERE accessPackageAssignmentPolicy-id = '{{ accessPackageAssignmentPolicy-id }}' --required
AND accessPackageQuestion-id = '{{ accessPackageQuestion-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
