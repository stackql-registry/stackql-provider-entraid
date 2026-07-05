--- 
title: directory_audits
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_audits
  - audit_logs
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

Creates, updates, deletes, gets or lists a <code>directory_audits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="directory_audits" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.audit_logs.directory_audits" /></td></tr>
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
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="activityDisplayName" /></td>
    <td><code>string</code></td>
    <td>Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For a list of activities logged, refer to Microsoft Entra audit log categories and activities. Supports $filter (eq, startswith).</td>
</tr>
<tr>
    <td><CopyableCode code="additionalDetails" /></td>
    <td><code>array</code></td>
    <td>Indicates additional details on the activity.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement. For a list of categories for activities logged, refer to Microsoft Entra audit log categories and activities.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedBy" /></td>
    <td><code>object</code></td>
    <td> (title: auditActivityInitiator)</td>
</tr>
<tr>
    <td><CopyableCode code="loggedByService" /></td>
    <td><code>string</code></td>
    <td>Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="operationType" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code></code></td>
    <td>Indicates the result of the activity. The possible values are: success, failure, timeout, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="resultReason" /></td>
    <td><code>string</code></td>
    <td>Indicates the reason for failure if the result is failure or timeout.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResources" /></td>
    <td><code>array</code></td>
    <td>Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other. Supports $filter (eq) for id and displayName; and $filter (startswith) for displayName.</td>
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
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and $orderby. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="activityDisplayName" /></td>
    <td><code>string</code></td>
    <td>Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For a list of activities logged, refer to Microsoft Entra audit log categories and activities. Supports $filter (eq, startswith).</td>
</tr>
<tr>
    <td><CopyableCode code="additionalDetails" /></td>
    <td><code>array</code></td>
    <td>Indicates additional details on the activity.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement. For a list of categories for activities logged, refer to Microsoft Entra audit log categories and activities.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedBy" /></td>
    <td><code>object</code></td>
    <td> (title: auditActivityInitiator)</td>
</tr>
<tr>
    <td><CopyableCode code="loggedByService" /></td>
    <td><code>string</code></td>
    <td>Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="operationType" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.</td>
</tr>
<tr>
    <td><CopyableCode code="result" /></td>
    <td><code></code></td>
    <td>Indicates the result of the activity. The possible values are: success, failure, timeout, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="resultReason" /></td>
    <td><code>string</code></td>
    <td>Indicates the reason for failure if the result is failure or timeout.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResources" /></td>
    <td><code>array</code></td>
    <td>Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other. Supports $filter (eq) for id and displayName; and $filter (startswith) for displayName.</td>
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
    <td><a href="#parameter-directory_audit_id"><code>directory_audit_id</code></a></td>
    <td></td>
    <td>Get a specific Microsoft Entra audit log item. This includes an audit log item generated by various services within Microsoft Entra ID like user, application, device and group management, privileged identity management (PIM), access reviews, terms of use, identity protection, password management (self-service and admin password resets), self-service group management, and so on.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get the list of audit logs generated by Microsoft Entra ID. This includes audit logs generated by various services within Microsoft Entra ID, including user, app, device and group Management, privileged identity management (PIM), access reviews, terms of use, identity protection, password management (self-service and admin password resets), and self- service group management, and so on.</td>
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
    <td><a href="#parameter-directory_audit_id"><code>directory_audit_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-directory_audit_id"><code>directory_audit_id</code></a></td>
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
<tr id="parameter-directory_audit_id">
    <td><CopyableCode code="directory_audit_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryAudit</td>
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

Get a specific Microsoft Entra audit log item. This includes an audit log item generated by various services within Microsoft Entra ID like user, application, device and group management, privileged identity management (PIM), access reviews, terms of use, identity protection, password management (self-service and admin password resets), self-service group management, and so on.

```sql
SELECT
id,
activityDateTime,
activityDisplayName,
additionalDetails,
category,
correlationId,
initiatedBy,
loggedByService,
operationType,
result,
resultReason,
targetResources
FROM entra_id.audit_logs.directory_audits
WHERE directory_audit_id = '{{ directory_audit_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the list of audit logs generated by Microsoft Entra ID. This includes audit logs generated by various services within Microsoft Entra ID, including user, app, device and group Management, privileged identity management (PIM), access reviews, terms of use, identity protection, password management (self-service and admin password resets), and self- service group management, and so on.

```sql
SELECT
id,
activityDateTime,
activityDisplayName,
additionalDetails,
category,
correlationId,
initiatedBy,
loggedByService,
operationType,
result,
resultReason,
targetResources
FROM entra_id.audit_logs.directory_audits
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
INSERT INTO entra_id.audit_logs.directory_audits (
id,
activityDateTime,
activityDisplayName,
additionalDetails,
category,
correlationId,
initiatedBy,
loggedByService,
operationType,
result,
resultReason,
targetResources
)
SELECT 
'{{ id }}',
'{{ activityDateTime }}',
'{{ activityDisplayName }}',
'{{ additionalDetails }}',
'{{ category }}',
'{{ correlationId }}',
'{{ initiatedBy }}',
'{{ loggedByService }}',
'{{ operationType }}',
'{{ result }}',
'{{ resultReason }}',
'{{ targetResources }}'
RETURNING
id,
activityDateTime,
activityDisplayName,
additionalDetails,
category,
correlationId,
initiatedBy,
loggedByService,
operationType,
result,
resultReason,
targetResources
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: directory_audits
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: activityDateTime
      value: "{{ activityDateTime }}"
      description: |
        Indicates the date and time the activity was performed. The Timestamp type is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ge, le) and $orderby.
    - name: activityDisplayName
      value: "{{ activityDisplayName }}"
      description: |
        Indicates the activity name or the operation name (examples: 'Create User' and 'Add member to group'). For a list of activities logged, refer to Microsoft Entra audit log categories and activities. Supports $filter (eq, startswith).
    - name: additionalDetails
      description: |
        Indicates additional details on the activity.
      value:
        - key: "{{ key }}"
          value: "{{ value }}"
    - name: category
      value: "{{ category }}"
      description: |
        Indicates which resource category that's targeted by the activity. For example: UserManagement, GroupManagement, ApplicationManagement, RoleManagement. For a list of categories for activities logged, refer to Microsoft Entra audit log categories and activities.
    - name: correlationId
      value: "{{ correlationId }}"
      description: |
        Indicates a unique ID that helps correlate activities that span across various services. Can be used to trace logs across services. Supports $filter (eq).
    - name: initiatedBy
      value:
        app:
          appId: "{{ appId }}"
          displayName: "{{ displayName }}"
          servicePrincipalId: "{{ servicePrincipalId }}"
          servicePrincipalName: "{{ servicePrincipalName }}"
        user:
          displayName: "{{ displayName }}"
          id: "{{ id }}"
          ipAddress: "{{ ipAddress }}"
          userPrincipalName: "{{ userPrincipalName }}"
    - name: loggedByService
      value: "{{ loggedByService }}"
      description: |
        Indicates information on which service initiated the activity (For example: Self-service Password Management, Core Directory, B2C, Invited Users, Microsoft Identity Manager, Privileged Identity Management. Supports $filter (eq).
    - name: operationType
      value: "{{ operationType }}"
      description: |
        Indicates the type of operation that was performed. The possible values include but are not limited to the following: Add, Assign, Update, Unassign, and Delete.
    - name: result
      value: "{{ result }}"
      description: |
        Indicates the result of the activity. The possible values are: success, failure, timeout, unknownFutureValue.
    - name: resultReason
      value: "{{ resultReason }}"
      description: |
        Indicates the reason for failure if the result is failure or timeout.
    - name: targetResources
      description: |
        Indicates information on which resource was changed due to the activity. Target Resource Type can be User, Device, Directory, App, Role, Group, Policy or Other. Supports $filter (eq) for id and displayName; and $filter (startswith) for displayName.
      value:
        - displayName: "{{ displayName }}"
          groupType: "{{ groupType }}"
          id: "{{ id }}"
          modifiedProperties: "{{ modifiedProperties }}"
          type: "{{ type }}"
          userPrincipalName: "{{ userPrincipalName }}"
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
UPDATE entra_id.audit_logs.directory_audits
SET 
id = '{{ id }}',
activityDateTime = '{{ activityDateTime }}',
activityDisplayName = '{{ activityDisplayName }}',
additionalDetails = '{{ additionalDetails }}',
category = '{{ category }}',
correlationId = '{{ correlationId }}',
initiatedBy = '{{ initiatedBy }}',
loggedByService = '{{ loggedByService }}',
operationType = '{{ operationType }}',
result = '{{ result }}',
resultReason = '{{ resultReason }}',
targetResources = '{{ targetResources }}'
WHERE 
directory_audit_id = '{{ directory_audit_id }}' --required
RETURNING
id,
activityDateTime,
activityDisplayName,
additionalDetails,
category,
correlationId,
initiatedBy,
loggedByService,
operationType,
result,
resultReason,
targetResources;
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
DELETE FROM entra_id.audit_logs.directory_audits
WHERE directory_audit_id = '{{ directory_audit_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
