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
    <td>The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="autoExtendDuration" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration by which the validity of the relationship is automatically extended, denoted in ISO 8601 format. Supported values are: P0D, PT0S, P180D. The default value is PT0S. PT0S indicates that the relationship expires when the endDateTime is reached and it isn't automatically extended. (pattern: <code>^-?P(&#91;0-9&#93;+D)?(T(&#91;0-9&#93;+H)?(&#91;0-9&#93;+M)?(&#91;0-9&#93;+(&#91;.&#93;&#91;0-9&#93;+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and can't be changed by the customer. (pattern: <code>^-?P(&#91;0-9&#93;+D)?(T(&#91;0-9&#93;+H)?(&#91;0-9&#93;+M)?(&#91;0-9&#93;+(&#91;.&#93;&#91;0-9&#93;+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The date and time in ISO 8601 format and in UTC time when the relationship became active. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="autoExtendDuration" /></td>
    <td><code>string (duration)</code></td>
    <td>The duration by which the validity of the relationship is automatically extended, denoted in ISO 8601 format. Supported values are: P0D, PT0S, P180D. The default value is PT0S. PT0S indicates that the relationship expires when the endDateTime is reached and it isn't automatically extended. (pattern: <code>^-?P(&#91;0-9&#93;+D)?(T(&#91;0-9&#93;+H)?(&#91;0-9&#93;+M)?(&#91;0-9&#93;+(&#91;.&#93;&#91;0-9&#93;+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was created. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The duration of the relationship in ISO 8601 format. Must be a value between P1D and P2Y inclusive. This is set by the partner only when the relationship is in the created status and can't be changed by the customer. (pattern: <code>^-?P(&#91;0-9&#93;+D)?(T(&#91;0-9&#93;+H)?(&#91;0-9&#93;+M)?(&#91;0-9&#93;+(&#91;.&#93;&#91;0-9&#93;+)?S)?)?$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="endDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the status of relationship changes to either terminated or expired. Calculated as endDateTime = activatedDateTime + duration. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time in ISO 8601 format and in UTC time when the relationship was last modified. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a></td>
    <td></td>
    <td>Read the properties of a delegatedAdminRelationship object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the delegatedAdminRelationship objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new delegatedAdminRelationship object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a></td>
    <td></td>
    <td>Update the properties of a delegatedAdminRelationship object.  The following restrictions apply:<br />- You can update this relationship when its status property is created.<br />- You can update the autoExtendDuration property when status is either created or active.<br />- You can only remove the Microsoft Entra Global Administrator role when the status property is active, which indicates a long-running operation.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-delegated_admin_relationship_id"><code>delegated_admin_relationship_id</code></a></td>
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

Read the properties of a delegatedAdminRelationship object.

```sql
SELECT
id,
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
WHERE delegated_admin_relationship_id = '{{ delegated_admin_relationship_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the delegatedAdminRelationship objects and their properties.

```sql
SELECT
id,
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
    - name: accessDetails
      value:
        unifiedRoles:
          - roleDefinitionId: "{{ roleDefinitionId }}"
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
          accessContainer:
            accessContainerId: "{{ accessContainerId }}"
            accessContainerType: "{{ accessContainerType }}"
          accessDetails:
            unifiedRoles:
              - roleDefinitionId: "{{ roleDefinitionId }}"
          createdDateTime: "{{ createdDateTime }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          status: "{{ status }}"
    - name: operations
      description: |
        The long running operations associated with the delegated admin relationship.
      value:
        - id: "{{ id }}"
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
delegated_admin_relationship_id = '{{ delegated_admin_relationship_id }}' --required
RETURNING
id,
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
WHERE delegated_admin_relationship_id = '{{ delegated_admin_relationship_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
