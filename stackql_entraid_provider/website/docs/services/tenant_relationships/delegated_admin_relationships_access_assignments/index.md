--- 
title: delegated_admin_relationships_access_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_admin_relationships_access_assignments
  - tenant_relationships
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

Creates, updates, deletes, gets or lists a <code>delegated_admin_relationships_access_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delegated_admin_relationships_access_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.tenant_relationships.delegated_admin_relationships_access_assignments" /></td></tr>
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
    <td><CopyableCode code="accessContainer" /></td>
    <td><code>object</code></td>
    <td> (title: delegatedAdminAccessContainer)</td>
</tr>
<tr>
    <td><CopyableCode code="accessDetails" /></td>
    <td><code>object</code></td>
    <td> (title: delegatedAdminAccessDetails)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the access assignment was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 and in UTC time when this access assignment was last modified. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>The status of the access assignment. Read-only. The possible values are: pending, active, deleting, deleted, error, unknownFutureValue.</td>
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
    <td><CopyableCode code="accessContainer" /></td>
    <td><code>object</code></td>
    <td> (title: delegatedAdminAccessContainer)</td>
</tr>
<tr>
    <td><CopyableCode code="accessDetails" /></td>
    <td><code>object</code></td>
    <td> (title: delegatedAdminAccessDetails)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the access assignment was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 and in UTC time when this access assignment was last modified. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>The status of the access assignment. Read-only. The possible values are: pending, active, deleting, deleted, error, unknownFutureValue.</td>
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
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a>, <a href="#parameter-delegated_admin_access_assignment_id"><code>delegated_admin_access_assignment_id</code></a></td>
    <td></td>
    <td>Read the properties of a delegatedAdminAccessAssignment object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a></td>
    <td></td>
    <td>Get a list of the delegatedAdminAccessAssignment objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a></td>
    <td></td>
    <td>Create a new delegatedAdminAccessAssignment object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a>, <a href="#parameter-delegated_admin_access_assignment_id"><code>delegated_admin_access_assignment_id</code></a></td>
    <td></td>
    <td>Update the properties of a delegatedAdminAccessAssignment object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a>, <a href="#parameter-delegated_admin_access_assignment_id"><code>delegated_admin_access_assignment_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a delegatedAdminAccessAssignment object.</td>
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
<tr id="parameter-delegated_admin_access_assignment_id">
    <td><CopyableCode code="delegated_admin_access_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of delegatedAdminAccessAssignment</td>
</tr>
<tr id="parameter-delegated_admin_relationship_id">
    <td><CopyableCode code="delegated_admin_relationship_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of delegatedAdminRelationship</td>
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

Read the properties of a delegatedAdminAccessAssignment object.

```sql
SELECT
id,
accessContainer,
accessDetails,
createdDateTime,
lastModifiedDateTime,
status
FROM entra_id.tenant_relationships.delegated_admin_relationships_access_assignments
WHERE delegated_admin_relationship_id = '{{ delegated_admin_relationship_id }}' -- required
AND delegated_admin_access_assignment_id = '{{ delegated_admin_access_assignment_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the delegatedAdminAccessAssignment objects and their properties.

```sql
SELECT
id,
accessContainer,
accessDetails,
createdDateTime,
lastModifiedDateTime,
status
FROM entra_id.tenant_relationships.delegated_admin_relationships_access_assignments
WHERE delegated_admin_relationship_id = '{{ delegated_admin_relationship_id }}' -- required
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

Create a new delegatedAdminAccessAssignment object.

```sql
INSERT INTO entra_id.tenant_relationships.delegated_admin_relationships_access_assignments (
id,
accessContainer,
accessDetails,
createdDateTime,
lastModifiedDateTime,
status,
delegated_admin_relationship_id
)
SELECT 
'{{ id }}',
'{{ accessContainer }}',
'{{ accessDetails }}',
'{{ createdDateTime }}',
'{{ lastModifiedDateTime }}',
'{{ status }}',
'{{ delegated_admin_relationship_id }}'
RETURNING
id,
accessContainer,
accessDetails,
createdDateTime,
lastModifiedDateTime,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: delegated_admin_relationships_access_assignments
  props:
    - name: delegated_admin_relationship_id
      value: "{{ delegated_admin_relationship_id }}"
      description: Required parameter for the delegated_admin_relationships_access_assignments resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: accessContainer
      value:
        accessContainerId: "{{ accessContainerId }}"
        accessContainerType: "{{ accessContainerType }}"
    - name: accessDetails
      value:
        unifiedRoles:
          - roleDefinitionId: "{{ roleDefinitionId }}"
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The date and time in ISO 8601 format and in UTC time when the access assignment was created. Read-only.
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        The date and time in ISO 8601 and in UTC time when this access assignment was last modified. Read-only.
    - name: status
      value: "{{ status }}"
      description: |
        The status of the access assignment. Read-only. The possible values are: pending, active, deleting, deleted, error, unknownFutureValue.
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

Update the properties of a delegatedAdminAccessAssignment object.

```sql
UPDATE entra_id.tenant_relationships.delegated_admin_relationships_access_assignments
SET 
id = '{{ id }}',
accessContainer = '{{ accessContainer }}',
accessDetails = '{{ accessDetails }}',
createdDateTime = '{{ createdDateTime }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
status = '{{ status }}'
WHERE 
delegated_admin_relationship_id = '{{ delegated_admin_relationship_id }}' --required
AND delegated_admin_access_assignment_id = '{{ delegated_admin_access_assignment_id }}' --required
RETURNING
id,
accessContainer,
accessDetails,
createdDateTime,
lastModifiedDateTime,
status;
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

Delete a delegatedAdminAccessAssignment object.

```sql
DELETE FROM entra_id.tenant_relationships.delegated_admin_relationships_access_assignments
WHERE delegated_admin_relationship_id = '{{ delegated_admin_relationship_id }}' --required
AND delegated_admin_access_assignment_id = '{{ delegated_admin_access_assignment_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
