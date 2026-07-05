--- 
title: entitlement_management_assignments_additional_access
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_assignments_additional_access
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_assignments_additional_access</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_assignments_additional_access" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_assignments_additional_access" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_2"
    values={[
        { label: 'get_2', value: 'get_2' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_2">

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
<TabItem value="get">

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
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a>, <a href="#parameter-incompatible_access_package_id"><code>incompatible_access_package_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>In Microsoft Entra Entitlement Management, retrieve a collection of accessPackageAssignment objects that indicate a target user has an assignment to a specified access package and also an assignment to another, potentially incompatible, access package.  This can be used to prepare to configure the incompatible access packages for a specific access package.</td>
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
<tr id="parameter-access_package_id">
    <td><CopyableCode code="access_package_id" /></td>
    <td><code>string</code></td>
    <td>Usage: accessPackageId='&#123;accessPackageId&#125;'</td>
</tr>
<tr id="parameter-incompatible_access_package_id">
    <td><CopyableCode code="incompatible_access_package_id" /></td>
    <td><code>string</code></td>
    <td>Usage: incompatibleAccessPackageId='&#123;incompatibleAccessPackageId&#125;'</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_2"
    values={[
        { label: 'get_2', value: 'get_2' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_2">

Success

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
FROM entra_id.identity_governance.entitlement_management_assignments_additional_access
WHERE access_package_id = '{{ access_package_id }}' -- required
AND incompatible_access_package_id = '{{ incompatible_access_package_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

In Microsoft Entra Entitlement Management, retrieve a collection of accessPackageAssignment objects that indicate a target user has an assignment to a specified access package and also an assignment to another, potentially incompatible, access package.  This can be used to prepare to configure the incompatible access packages for a specific access package.

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
FROM entra_id.identity_governance.entitlement_management_assignments_additional_access
;
```
</TabItem>
</Tabs>
