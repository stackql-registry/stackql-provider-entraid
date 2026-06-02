--- 
title: provisioning
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning
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

Creates, updates, deletes, gets or lists a <code>provisioning</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provisioning" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.audit_logs.provisioning" /></td></tr>
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
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  SUpports $filter (eq, gt, lt) and orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="changeId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of this change in this cycle. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="cycleId" /></td>
    <td><code>string</code></td>
    <td>Unique ID per job iteration. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="durationInMilliseconds" /></td>
    <td><code>number (int32)</code></td>
    <td>Indicates how long this provisioning action took to finish. Measured in milliseconds.</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedBy" /></td>
    <td><code></code></td>
    <td>Details of who initiated this provisioning. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>The unique ID for the whole provisioning job. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedProperties" /></td>
    <td><code>array</code></td>
    <td>Details of each property that was modified in this provisioning action on this object.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningAction" /></td>
    <td><code></code></td>
    <td>Indicates the activity name or the operation name. The possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Microsoft Entra activity list. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusInfo" /></td>
    <td><code></code></td>
    <td>Details of provisioning status.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSteps" /></td>
    <td><code>array</code></td>
    <td>Details of each step in provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code></code></td>
    <td>Represents the service principal used for provisioning. Supports $filter (eq) for id and name.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceIdentity" /></td>
    <td><code></code></td>
    <td>Details of source object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSystem" /></td>
    <td><code></code></td>
    <td>Details of source system of the object being provisioned. Supports $filter (eq, contains) for displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="targetIdentity" /></td>
    <td><code></code></td>
    <td>Details of target object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSystem" /></td>
    <td><code></code></td>
    <td>Details of target system of the object being provisioned. Supports $filter (eq, contains) for displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Unique Microsoft Entra tenant ID. Supports $filter (eq, contains).</td>
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
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  SUpports $filter (eq, gt, lt) and orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="changeId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of this change in this cycle. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="cycleId" /></td>
    <td><code>string</code></td>
    <td>Unique ID per job iteration. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="durationInMilliseconds" /></td>
    <td><code>number (int32)</code></td>
    <td>Indicates how long this provisioning action took to finish. Measured in milliseconds.</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedBy" /></td>
    <td><code></code></td>
    <td>Details of who initiated this provisioning. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="jobId" /></td>
    <td><code>string</code></td>
    <td>The unique ID for the whole provisioning job. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedProperties" /></td>
    <td><code>array</code></td>
    <td>Details of each property that was modified in this provisioning action on this object.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningAction" /></td>
    <td><code></code></td>
    <td>Indicates the activity name or the operation name. The possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Microsoft Entra activity list. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusInfo" /></td>
    <td><code></code></td>
    <td>Details of provisioning status.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSteps" /></td>
    <td><code>array</code></td>
    <td>Details of each step in provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code></code></td>
    <td>Represents the service principal used for provisioning. Supports $filter (eq) for id and name.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceIdentity" /></td>
    <td><code></code></td>
    <td>Details of source object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSystem" /></td>
    <td><code></code></td>
    <td>Details of source system of the object being provisioned. Supports $filter (eq, contains) for displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="targetIdentity" /></td>
    <td><code></code></td>
    <td>Details of target object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="targetSystem" /></td>
    <td><code></code></td>
    <td>Details of target system of the object being provisioned. Supports $filter (eq, contains) for displayName.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Unique Microsoft Entra tenant ID. Supports $filter (eq, contains).</td>
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
    <td><a href="#parameter-provisioningObjectSummary-id"><code>provisioningObjectSummary-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get all provisioning events that occurred in your tenant, such as the deletion of a group in a target application or the creation of a user when provisioning user accounts from your HR system. </td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-provisioningObjectSummary-id"><code>provisioningObjectSummary-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-provisioningObjectSummary-id"><code>provisioningObjectSummary-id</code></a></td>
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
<tr id="parameter-provisioningObjectSummary-id">
    <td><CopyableCode code="provisioningObjectSummary-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of provisioningObjectSummary</td>
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

Retrieved navigation property

```sql
SELECT
id,
@odata.type,
activityDateTime,
changeId,
cycleId,
durationInMilliseconds,
initiatedBy,
jobId,
modifiedProperties,
provisioningAction,
provisioningStatusInfo,
provisioningSteps,
servicePrincipal,
sourceIdentity,
sourceSystem,
targetIdentity,
targetSystem,
tenantId
FROM entra_id.audit_logs.provisioning
WHERE provisioningObjectSummary-id = '{{ provisioningObjectSummary-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get all provisioning events that occurred in your tenant, such as the deletion of a group in a target application or the creation of a user when provisioning user accounts from your HR system. 

```sql
SELECT
id,
@odata.type,
activityDateTime,
changeId,
cycleId,
durationInMilliseconds,
initiatedBy,
jobId,
modifiedProperties,
provisioningAction,
provisioningStatusInfo,
provisioningSteps,
servicePrincipal,
sourceIdentity,
sourceSystem,
targetIdentity,
targetSystem,
tenantId
FROM entra_id.audit_logs.provisioning
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

No description available.

```sql
INSERT INTO entra_id.audit_logs.provisioning (
id,
@odata.type,
activityDateTime,
changeId,
cycleId,
durationInMilliseconds,
initiatedBy,
jobId,
modifiedProperties,
provisioningAction,
provisioningStatusInfo,
provisioningSteps,
servicePrincipal,
sourceIdentity,
sourceSystem,
targetIdentity,
targetSystem,
tenantId
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ activityDateTime }}',
'{{ changeId }}',
'{{ cycleId }}',
{{ durationInMilliseconds }},
'{{ initiatedBy }}',
'{{ jobId }}',
'{{ modifiedProperties }}',
'{{ provisioningAction }}',
'{{ provisioningStatusInfo }}',
'{{ provisioningSteps }}',
'{{ servicePrincipal }}',
'{{ sourceIdentity }}',
'{{ sourceSystem }}',
'{{ targetIdentity }}',
'{{ targetSystem }}',
'{{ tenantId }}'
RETURNING
id,
@odata.type,
activityDateTime,
changeId,
cycleId,
durationInMilliseconds,
initiatedBy,
jobId,
modifiedProperties,
provisioningAction,
provisioningStatusInfo,
provisioningSteps,
servicePrincipal,
sourceIdentity,
sourceSystem,
targetIdentity,
targetSystem,
tenantId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: provisioning
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: activityDateTime
      value: "{{ activityDateTime }}"
      description: |
        Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.  SUpports $filter (eq, gt, lt) and orderby.
    - name: changeId
      value: "{{ changeId }}"
      description: |
        Unique ID of this change in this cycle. Supports $filter (eq, contains).
    - name: cycleId
      value: "{{ cycleId }}"
      description: |
        Unique ID per job iteration. Supports $filter (eq, contains).
    - name: durationInMilliseconds
      value: {{ durationInMilliseconds }}
      description: |
        Indicates how long this provisioning action took to finish. Measured in milliseconds.
    - name: initiatedBy
      value: "{{ initiatedBy }}"
      description: |
        Details of who initiated this provisioning. Supports $filter (eq, contains).
    - name: jobId
      value: "{{ jobId }}"
      description: |
        The unique ID for the whole provisioning job. Supports $filter (eq, contains).
    - name: modifiedProperties
      description: |
        Details of each property that was modified in this provisioning action on this object.
      value:
        - displayName: "{{ displayName }}"
          newValue: "{{ newValue }}"
          oldValue: "{{ oldValue }}"
          @odata.type: "{{ @odata.type }}"
    - name: provisioningAction
      value: "{{ provisioningAction }}"
      description: |
        Indicates the activity name or the operation name. The possible values are: create, update, delete, stageddelete, disable, other and unknownFutureValue. For a list of activities logged, refer to Microsoft Entra activity list. Supports $filter (eq, contains).
    - name: provisioningStatusInfo
      value: "{{ provisioningStatusInfo }}"
      description: |
        Details of provisioning status.
    - name: provisioningSteps
      description: |
        Details of each step in provisioning.
      value:
        - description: "{{ description }}"
          details:
            @odata.type: "{{ @odata.type }}"
          name: "{{ name }}"
          provisioningStepType: "{{ provisioningStepType }}"
          status: "{{ status }}"
          @odata.type: "{{ @odata.type }}"
    - name: servicePrincipal
      value: "{{ servicePrincipal }}"
      description: |
        Represents the service principal used for provisioning. Supports $filter (eq) for id and name.
    - name: sourceIdentity
      value: "{{ sourceIdentity }}"
      description: |
        Details of source object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.
    - name: sourceSystem
      value: "{{ sourceSystem }}"
      description: |
        Details of source system of the object being provisioned. Supports $filter (eq, contains) for displayName.
    - name: targetIdentity
      value: "{{ targetIdentity }}"
      description: |
        Details of target object being provisioned. Supports $filter (eq, contains) for identityType, id, and displayName.
    - name: targetSystem
      value: "{{ targetSystem }}"
      description: |
        Details of target system of the object being provisioned. Supports $filter (eq, contains) for displayName.
    - name: tenantId
      value: "{{ tenantId }}"
      description: |
        Unique Microsoft Entra tenant ID. Supports $filter (eq, contains).
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
UPDATE entra_id.audit_logs.provisioning
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
activityDateTime = '{{ activityDateTime }}',
changeId = '{{ changeId }}',
cycleId = '{{ cycleId }}',
durationInMilliseconds = {{ durationInMilliseconds }},
initiatedBy = '{{ initiatedBy }}',
jobId = '{{ jobId }}',
modifiedProperties = '{{ modifiedProperties }}',
provisioningAction = '{{ provisioningAction }}',
provisioningStatusInfo = '{{ provisioningStatusInfo }}',
provisioningSteps = '{{ provisioningSteps }}',
servicePrincipal = '{{ servicePrincipal }}',
sourceIdentity = '{{ sourceIdentity }}',
sourceSystem = '{{ sourceSystem }}',
targetIdentity = '{{ targetIdentity }}',
targetSystem = '{{ targetSystem }}',
tenantId = '{{ tenantId }}'
WHERE 
provisioningObjectSummary-id = '{{ provisioningObjectSummary-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
activityDateTime,
changeId,
cycleId,
durationInMilliseconds,
initiatedBy,
jobId,
modifiedProperties,
provisioningAction,
provisioningStatusInfo,
provisioningSteps,
servicePrincipal,
sourceIdentity,
sourceSystem,
targetIdentity,
targetSystem,
tenantId;
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
DELETE FROM entra_id.audit_logs.provisioning
WHERE provisioningObjectSummary-id = '{{ provisioningObjectSummary-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
