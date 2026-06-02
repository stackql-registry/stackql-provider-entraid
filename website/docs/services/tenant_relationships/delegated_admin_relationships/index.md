--- 
title: delegated_admin_relationships
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_admin_relationships
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

Creates, updates, deletes, gets or lists a <code>delegated_admin_relationships</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delegated_admin_relationships" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.tenant_relationships.delegated_admin_relationships" /></td></tr>
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
    <td><CopyableCode code="accessAssignments" /></td>
    <td><code>array</code></td>
    <td>The access assignments associated with the delegated admin relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="accessDetails" /></td>
    <td><code>object</code></td>
    <td> (title: delegatedAdminAccessDetails)</td>
</tr>
<tr>
    <td><CopyableCode code="activatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="autoExtendDuration" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration by which the validity of the relationship is automatically extended, denoted in ISO 8601 format. Supported values are: P0D, PT0S, P180D. The default value is PT0S. PT0S indicates that the relationship expires when the endDateTime is reached and it isn't automatically extended. (pattern: <code>^-?P([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+([.][0-9]+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customer" /></td>
    <td><code></code></td>
    <td>The display name and unique identifier of the customer of the relationship. This is configured either by the partner at the time the relationship is created or by the system after the customer approves the relationship. Can't be changed by the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the relationship used for ease of identification. Must be unique across all delegated admin relationships of the partner and is set by the partner only when the relationship is in the created status and can't be changed by the customer. Maximum length is 50 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and can't be changed by the customer. (pattern: <code>^-?P([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+([.][0-9]+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="operations" /></td>
    <td><code>array</code></td>
    <td>The long running operations associated with the delegated admin relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>array</code></td>
    <td>The requests associated with the delegated admin relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>The status of the relationship. Read Only. The possible values are: activating, active, approvalPending, approved, created, expired, expiring, terminated, terminating, terminationRequested, unknownFutureValue. Supports $orderby.</td>
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
    <td><CopyableCode code="accessAssignments" /></td>
    <td><code>array</code></td>
    <td>The access assignments associated with the delegated admin relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="accessDetails" /></td>
    <td><code>object</code></td>
    <td> (title: delegatedAdminAccessDetails)</td>
</tr>
<tr>
    <td><CopyableCode code="activatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="autoExtendDuration" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration by which the validity of the relationship is automatically extended, denoted in ISO 8601 format. Supported values are: P0D, PT0S, P180D. The default value is PT0S. PT0S indicates that the relationship expires when the endDateTime is reached and it isn't automatically extended. (pattern: <code>^-?P([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+([.][0-9]+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customer" /></td>
    <td><code></code></td>
    <td>The display name and unique identifier of the customer of the relationship. This is configured either by the partner at the time the relationship is created or by the system after the customer approves the relationship. Can't be changed by the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the relationship used for ease of identification. Must be unique across all delegated admin relationships of the partner and is set by the partner only when the relationship is in the created status and can't be changed by the customer. Maximum length is 50 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and can't be changed by the customer. (pattern: <code>^-?P([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+([.][0-9]+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="operations" /></td>
    <td><code>array</code></td>
    <td>The long running operations associated with the delegated admin relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="requests" /></td>
    <td><code>array</code></td>
    <td>The requests associated with the delegated admin relationship.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>The status of the relationship. Read Only. The possible values are: activating, active, approvalPending, approved, created, expired, expiring, terminated, terminating, terminationRequested, unknownFutureValue. Supports $orderby.</td>
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
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties of a delegatedAdminRelationship object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of the delegatedAdminRelationship objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new delegatedAdminRelationship object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a delegatedAdminRelationship object.  The following restrictions apply:<br />- You can update this relationship when its status property is created.<br />- You can update the autoExtendDuration property when status is either created or active.<br />- You can only remove the Microsoft Entra Global Administrator role when the status property is active, which indicates a long-running operation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-delegatedAdminRelationship-id"><code>delegatedAdminRelationship-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a delegatedAdminRelationship object. A relationship can only be deleted if it's in the 'created' status. </td>
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
<tr id="parameter-delegatedAdminRelationship-id">
    <td><CopyableCode code="delegatedAdminRelationship-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of delegatedAdminRelationship</td>
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

Read the properties of a delegatedAdminRelationship object.

```sql
SELECT
id,
@odata.type,
accessAssignments,
accessDetails,
activatedDateTime,
autoExtendDuration,
createdDateTime,
customer,
displayName,
duration,
endDateTime,
lastModifiedDateTime,
operations,
requests,
status
FROM entra_id.tenant_relationships.delegated_admin_relationships
WHERE delegatedAdminRelationship-id = '{{ delegatedAdminRelationship-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of the delegatedAdminRelationship objects and their properties.

```sql
SELECT
id,
@odata.type,
accessAssignments,
accessDetails,
activatedDateTime,
autoExtendDuration,
createdDateTime,
customer,
displayName,
duration,
endDateTime,
lastModifiedDateTime,
operations,
requests,
status
FROM entra_id.tenant_relationships.delegated_admin_relationships
WHERE $top = '{{ $top }}'
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

Create a new delegatedAdminRelationship object.

```sql
INSERT INTO entra_id.tenant_relationships.delegated_admin_relationships (
id,
@odata.type,
accessDetails,
activatedDateTime,
autoExtendDuration,
createdDateTime,
customer,
displayName,
duration,
endDateTime,
lastModifiedDateTime,
status,
accessAssignments,
operations,
requests
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ accessDetails }}',
'{{ activatedDateTime }}',
'{{ autoExtendDuration }}',
'{{ createdDateTime }}',
'{{ customer }}',
'{{ displayName }}',
'{{ duration }}',
'{{ endDateTime }}',
'{{ lastModifiedDateTime }}',
'{{ status }}',
'{{ accessAssignments }}',
'{{ operations }}',
'{{ requests }}'
RETURNING
id,
@odata.type,
accessAssignments,
accessDetails,
activatedDateTime,
autoExtendDuration,
createdDateTime,
customer,
displayName,
duration,
endDateTime,
lastModifiedDateTime,
operations,
requests,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: delegated_admin_relationships
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: accessDetails
      value:
        unifiedRoles:
          - roleDefinitionId: "{{ roleDefinitionId }}"
            @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: activatedDateTime
      value: "{{ activatedDateTime }}"
      description: |
        The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only.
    - name: autoExtendDuration
      value: "{{ autoExtendDuration }}"
      description: |
        The duration by which the validity of the relationship is automatically extended, denoted in ISO 8601 format. Supported values are: P0D, PT0S, P180D. The default value is PT0S. PT0S indicates that the relationship expires when the endDateTime is reached and it isn't automatically extended.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only.
    - name: customer
      value: "{{ customer }}"
      description: |
        The display name and unique identifier of the customer of the relationship. This is configured either by the partner at the time the relationship is created or by the system after the customer approves the relationship. Can't be changed by the customer.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the relationship used for ease of identification. Must be unique across all delegated admin relationships of the partner and is set by the partner only when the relationship is in the created status and can't be changed by the customer. Maximum length is 50 characters.
    - name: duration
      value: "{{ duration }}"
      description: |
        The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and can't be changed by the customer.
    - name: endDateTime
      value: "{{ endDateTime }}"
      description: |
        The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only.
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only.
    - name: status
      value: "{{ status }}"
      description: |
        The status of the relationship. Read Only. The possible values are: activating, active, approvalPending, approved, created, expired, expiring, terminated, terminating, terminationRequested, unknownFutureValue. Supports $orderby.
    - name: accessAssignments
      description: |
        The access assignments associated with the delegated admin relationship.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          accessContainer:
            accessContainerId: "{{ accessContainerId }}"
            accessContainerType: "{{ accessContainerType }}"
            @odata.type: "{{ @odata.type }}"
          accessDetails:
            unifiedRoles:
              - roleDefinitionId: "{{ roleDefinitionId }}"
                @odata.type: "{{ @odata.type }}"
            @odata.type: "{{ @odata.type }}"
          createdDateTime: "{{ createdDateTime }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          status: "{{ status }}"
    - name: operations
      description: |
        The long running operations associated with the delegated admin relationship.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdDateTime: "{{ createdDateTime }}"
          data: "{{ data }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          operationType: "{{ operationType }}"
          status: "{{ status }}"
    - name: requests
      description: |
        The requests associated with the delegated admin relationship.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          action: "{{ action }}"
          createdDateTime: "{{ createdDateTime }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          status: "{{ status }}"
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

Update the properties of a delegatedAdminRelationship object.  The following restrictions apply:<br />- You can update this relationship when its status property is created.<br />- You can update the autoExtendDuration property when status is either created or active.<br />- You can only remove the Microsoft Entra Global Administrator role when the status property is active, which indicates a long-running operation.

```sql
UPDATE entra_id.tenant_relationships.delegated_admin_relationships
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
accessDetails = '{{ accessDetails }}',
activatedDateTime = '{{ activatedDateTime }}',
autoExtendDuration = '{{ autoExtendDuration }}',
createdDateTime = '{{ createdDateTime }}',
customer = '{{ customer }}',
displayName = '{{ displayName }}',
duration = '{{ duration }}',
endDateTime = '{{ endDateTime }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
status = '{{ status }}',
accessAssignments = '{{ accessAssignments }}',
operations = '{{ operations }}',
requests = '{{ requests }}'
WHERE 
delegatedAdminRelationship-id = '{{ delegatedAdminRelationship-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
accessAssignments,
accessDetails,
activatedDateTime,
autoExtendDuration,
createdDateTime,
customer,
displayName,
duration,
endDateTime,
lastModifiedDateTime,
operations,
requests,
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

Delete a delegatedAdminRelationship object. A relationship can only be deleted if it's in the 'created' status. 

```sql
DELETE FROM entra_id.tenant_relationships.delegated_admin_relationships
WHERE delegatedAdminRelationship-id = '{{ delegatedAdminRelationship-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
