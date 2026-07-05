--- 
title: entitlement_management_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_assignments
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_assignments" /></td></tr>
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
    <td><CopyableCode code="accessPackage" /></td>
    <td><code></code></td>
    <td>Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentPolicy" /></td>
    <td><code></code></td>
    <td>Read-only. Supports $filter (eq) on the id property and $expand query parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="customExtensionCalloutInstances" /></td>
    <td><code>array</code></td>
    <td>Information about all the custom extension calls that were made during the access package assignment workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="expiredDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code></code></td>
    <td>When the access assignment is to be in place. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The state of the access package assignment. The possible values are: delivering, partiallyDelivered, delivered, expired, deliveryFailed, unknownFutureValue. Read-only. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>More information about the assignment lifecycle. Possible values include Delivering, Delivered, AutoAssignmentInGracePeriod, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code></code></td>
    <td>The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.</td>
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
    <td><CopyableCode code="accessPackage" /></td>
    <td><code></code></td>
    <td>Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentPolicy" /></td>
    <td><code></code></td>
    <td>Read-only. Supports $filter (eq) on the id property and $expand query parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="customExtensionCalloutInstances" /></td>
    <td><code>array</code></td>
    <td>Information about all the custom extension calls that were made during the access package assignment workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="expiredDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code></code></td>
    <td>When the access assignment is to be in place. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The state of the access package assignment. The possible values are: delivering, partiallyDelivered, delivered, expired, deliveryFailed, unknownFutureValue. Read-only. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>More information about the assignment lifecycle. Possible values include Delivering, Delivered, AutoAssignmentInGracePeriod, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="target" /></td>
    <td><code></code></td>
    <td>The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.</td>
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
    <td><a href="#parameter-access_package_assignment_id"><code>access_package_assignment_id</code></a></td>
    <td></td>
    <td>In Microsoft Entra entitlement management, retrieve the properties and relationships of an accessPackageAssignment object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>In Microsoft Entra entitlement management, retrieve a list of accessPackageAssignment objects. For directory-wide administrators, the resulting list includes all the assignments, current and well as expired, that the caller has access to read, across all catalogs and access packages.  If the caller is on behalf of a delegated user who is assigned only to catalog-specific delegated administrative roles, the request must supply a filter to indicate a specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_assignment_id"><code>access_package_assignment_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_assignment_id"><code>access_package_assignment_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#reprocess"><CopyableCode code="reprocess" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-access_package_assignment_id"><code>access_package_assignment_id</code></a></td>
    <td></td>
    <td>In Microsoft Entra entitlement management, callers can automatically reevaluate and enforce an accessPackageAssignment object of a user’s assignments for a specific access package. The state of the access package assignment must be Delivered for the administrator to reprocess the user's assignment. Only admins with the Access Package Assignment Manager role, or higher, in Microsoft Entra entitlement management can perform this action.</td>
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
<tr id="parameter-access_package_assignment_id">
    <td><CopyableCode code="access_package_assignment_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageAssignment</td>
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

In Microsoft Entra entitlement management, retrieve the properties and relationships of an accessPackageAssignment object.

```sql
SELECT
id,
accessPackage,
assignmentPolicy,
customExtensionCalloutInstances,
expiredDateTime,
schedule,
state,
status,
target
FROM entra_id.identity_governance.entitlement_management_assignments
WHERE access_package_assignment_id = '{{ access_package_assignment_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

In Microsoft Entra entitlement management, retrieve a list of accessPackageAssignment objects. For directory-wide administrators, the resulting list includes all the assignments, current and well as expired, that the caller has access to read, across all catalogs and access packages.  If the caller is on behalf of a delegated user who is assigned only to catalog-specific delegated administrative roles, the request must supply a filter to indicate a specific access package, such as: $filter=accessPackage/id eq 'a914b616-e04e-476b-aa37-91038f0b165b'.

```sql
SELECT
id,
accessPackage,
assignmentPolicy,
customExtensionCalloutInstances,
expiredDateTime,
schedule,
state,
status,
target
FROM entra_id.identity_governance.entitlement_management_assignments
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
INSERT INTO entra_id.identity_governance.entitlement_management_assignments (
id,
customExtensionCalloutInstances,
expiredDateTime,
schedule,
state,
status,
accessPackage,
assignmentPolicy,
target
)
SELECT 
'{{ id }}',
'{{ customExtensionCalloutInstances }}',
'{{ expiredDateTime }}',
'{{ schedule }}',
'{{ state }}',
'{{ status }}',
'{{ accessPackage }}',
'{{ assignmentPolicy }}',
'{{ target }}'
RETURNING
id,
accessPackage,
assignmentPolicy,
customExtensionCalloutInstances,
expiredDateTime,
schedule,
state,
status,
target
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_assignments
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: customExtensionCalloutInstances
      description: |
        Information about all the custom extension calls that were made during the access package assignment workflow.
      value:
        - customExtensionId: "{{ customExtensionId }}"
          detail: "{{ detail }}"
          externalCorrelationId: "{{ externalCorrelationId }}"
          id: "{{ id }}"
          status: "{{ status }}"
    - name: expiredDateTime
      value: "{{ expiredDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: schedule
      value: "{{ schedule }}"
      description: |
        When the access assignment is to be in place. Read-only.
    - name: state
      value: "{{ state }}"
      description: |
        The state of the access package assignment. The possible values are: delivering, partiallyDelivered, delivered, expired, deliveryFailed, unknownFutureValue. Read-only. Supports $filter (eq).
    - name: status
      value: "{{ status }}"
      description: |
        More information about the assignment lifecycle. Possible values include Delivering, Delivered, AutoAssignmentInGracePeriod, NearExpiry1DayNotificationTriggered, or ExpiredNotificationTriggered. Read-only.
    - name: accessPackage
      value: "{{ accessPackage }}"
      description: |
        Read-only. Nullable. Supports $filter (eq) on the id property and $expand query parameters.
    - name: assignmentPolicy
      value: "{{ assignmentPolicy }}"
      description: |
        Read-only. Supports $filter (eq) on the id property and $expand query parameters.
    - name: target
      value: "{{ target }}"
      description: |
        The subject of the access package assignment. Read-only. Nullable. Supports $expand. Supports $filter (eq) on objectId.
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
UPDATE entra_id.identity_governance.entitlement_management_assignments
SET 
id = '{{ id }}',
customExtensionCalloutInstances = '{{ customExtensionCalloutInstances }}',
expiredDateTime = '{{ expiredDateTime }}',
schedule = '{{ schedule }}',
state = '{{ state }}',
status = '{{ status }}',
accessPackage = '{{ accessPackage }}',
assignmentPolicy = '{{ assignmentPolicy }}',
target = '{{ target }}'
WHERE 
access_package_assignment_id = '{{ access_package_assignment_id }}' --required
RETURNING
id,
accessPackage,
assignmentPolicy,
customExtensionCalloutInstances,
expiredDateTime,
schedule,
state,
status,
target;
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
DELETE FROM entra_id.identity_governance.entitlement_management_assignments
WHERE access_package_assignment_id = '{{ access_package_assignment_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reprocess"
    values={[
        { label: 'reprocess', value: 'reprocess' }
    ]}
>
<TabItem value="reprocess">

In Microsoft Entra entitlement management, callers can automatically reevaluate and enforce an accessPackageAssignment object of a user’s assignments for a specific access package. The state of the access package assignment must be Delivered for the administrator to reprocess the user's assignment. Only admins with the Access Package Assignment Manager role, or higher, in Microsoft Entra entitlement management can perform this action.

```sql
EXEC entra_id.identity_governance.entitlement_management_assignments.reprocess 
@access_package_assignment_id='{{ access_package_assignment_id }}' --required
;
```
</TabItem>
</Tabs>
