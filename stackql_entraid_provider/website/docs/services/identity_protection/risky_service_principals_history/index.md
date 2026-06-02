--- 
title: risky_service_principals_history
hide_title: false
hide_table_of_contents: false
keywords:
  - risky_service_principals_history
  - identity_protection
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

Creates, updates, deletes, gets or lists a <code>risky_service_principals_history</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="risky_service_principals_history" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_protection.risky_service_principals_history" /></td></tr>
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
    <td><CopyableCode code="activity" /></td>
    <td><code></code></td>
    <td>The activity related to service principal risk level change.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier for the associated application (its appId property), if any.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="history" /></td>
    <td><code>array</code></td>
    <td>Represents the risk history of Microsoft Entra service principals.</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedBy" /></td>
    <td><code>string</code></td>
    <td>The identifier of the actor of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the service principal account is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="isProcessing" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether Microsoft Entra ID is currently processing the service principal's risky state.</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the risk state was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z. Supports $filter (eq). (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risky workload identity. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>State of the service principal's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalType" /></td>
    <td><code>string</code></td>
    <td>Identifies whether the service principal represents an Application, a ManagedIdentity, or a legacy application (socialIdp). This is set by Microsoft Entra ID internally and is inherited from servicePrincipal.</td>
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
    <td><CopyableCode code="activity" /></td>
    <td><code></code></td>
    <td>The activity related to service principal risk level change.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The globally unique identifier for the associated application (its appId property), if any.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="history" /></td>
    <td><code>array</code></td>
    <td>Represents the risk history of Microsoft Entra service principals.</td>
</tr>
<tr>
    <td><CopyableCode code="initiatedBy" /></td>
    <td><code>string</code></td>
    <td>The identifier of the actor of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the service principal account is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="isProcessing" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether Microsoft Entra ID is currently processing the service principal's risky state.</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the risk state was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z. Supports $filter (eq). (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risky workload identity. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>State of the service principal's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalType" /></td>
    <td><code>string</code></td>
    <td>Identifies whether the service principal represents an Application, a ManagedIdentity, or a legacy application (socialIdp). This is set by Microsoft Entra ID internally and is inherited from servicePrincipal.</td>
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
    <td><a href="#parameter-riskyServicePrincipal-id"><code>riskyServicePrincipal-id</code></a>, <a href="#parameter-riskyServicePrincipalHistoryItem-id"><code>riskyServicePrincipalHistoryItem-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Represents the risk history of Microsoft Entra service principals.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-riskyServicePrincipal-id"><code>riskyServicePrincipal-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the risk history of a riskyServicePrincipal object.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-riskyServicePrincipal-id"><code>riskyServicePrincipal-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-riskyServicePrincipal-id"><code>riskyServicePrincipal-id</code></a>, <a href="#parameter-riskyServicePrincipalHistoryItem-id"><code>riskyServicePrincipalHistoryItem-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-riskyServicePrincipal-id"><code>riskyServicePrincipal-id</code></a>, <a href="#parameter-riskyServicePrincipalHistoryItem-id"><code>riskyServicePrincipalHistoryItem-id</code></a></td>
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
<tr id="parameter-riskyServicePrincipal-id">
    <td><CopyableCode code="riskyServicePrincipal-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of riskyServicePrincipal</td>
</tr>
<tr id="parameter-riskyServicePrincipalHistoryItem-id">
    <td><CopyableCode code="riskyServicePrincipalHistoryItem-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of riskyServicePrincipalHistoryItem</td>
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

Represents the risk history of Microsoft Entra service principals.

```sql
SELECT
id,
@odata.type,
activity,
appId,
displayName,
history,
initiatedBy,
isEnabled,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
servicePrincipalType
FROM entra_id.identity_protection.risky_service_principals_history
WHERE riskyServicePrincipal-id = '{{ riskyServicePrincipal-id }}' -- required
AND riskyServicePrincipalHistoryItem-id = '{{ riskyServicePrincipalHistoryItem-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get the risk history of a riskyServicePrincipal object.

```sql
SELECT
id,
@odata.type,
activity,
appId,
displayName,
history,
initiatedBy,
isEnabled,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
servicePrincipalType
FROM entra_id.identity_protection.risky_service_principals_history
WHERE riskyServicePrincipal-id = '{{ riskyServicePrincipal-id }}' -- required
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
INSERT INTO entra_id.identity_protection.risky_service_principals_history (
id,
@odata.type,
appId,
displayName,
isEnabled,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
servicePrincipalType,
history,
activity,
initiatedBy,
riskyServicePrincipal-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ appId }}',
'{{ displayName }}',
{{ isEnabled }},
{{ isProcessing }},
'{{ riskDetail }}',
'{{ riskLastUpdatedDateTime }}',
'{{ riskLevel }}',
'{{ riskState }}',
'{{ servicePrincipalType }}',
'{{ history }}',
'{{ activity }}',
'{{ initiatedBy }}',
'{{ riskyServicePrincipal-id }}'
RETURNING
id,
@odata.type,
activity,
appId,
displayName,
history,
initiatedBy,
isEnabled,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
servicePrincipalType
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: risky_service_principals_history
  props:
    - name: riskyServicePrincipal-id
      value: "{{ riskyServicePrincipal-id }}"
      description: Required parameter for the risky_service_principals_history resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: appId
      value: "{{ appId }}"
      description: |
        The globally unique identifier for the associated application (its appId property), if any.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the service principal.
    - name: isEnabled
      value: {{ isEnabled }}
      description: |
        true if the service principal account is enabled; otherwise, false.
    - name: isProcessing
      value: {{ isProcessing }}
      description: |
        Indicates whether Microsoft Entra ID is currently processing the service principal's risky state.
    - name: riskDetail
      value: "{{ riskDetail }}"
      description: |
        Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.
    - name: riskLastUpdatedDateTime
      value: "{{ riskLastUpdatedDateTime }}"
      description: |
        The date and time that the risk state was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2021 is 2021-01-01T00:00:00Z. Supports $filter (eq).
    - name: riskLevel
      value: "{{ riskLevel }}"
      description: |
        Level of the detected risky workload identity. The possible values are: low, medium, high, hidden, none, unknownFutureValue. Supports $filter (eq).
    - name: riskState
      value: "{{ riskState }}"
      description: |
        State of the service principal's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
    - name: servicePrincipalType
      value: "{{ servicePrincipalType }}"
      description: |
        Identifies whether the service principal represents an Application, a ManagedIdentity, or a legacy application (socialIdp). This is set by Microsoft Entra ID internally and is inherited from servicePrincipal.
    - name: history
      description: |
        Represents the risk history of Microsoft Entra service principals.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          appId: "{{ appId }}"
          displayName: "{{ displayName }}"
          isEnabled: {{ isEnabled }}
          isProcessing: {{ isProcessing }}
          riskDetail: "{{ riskDetail }}"
          riskLastUpdatedDateTime: "{{ riskLastUpdatedDateTime }}"
          riskLevel: "{{ riskLevel }}"
          riskState: "{{ riskState }}"
          servicePrincipalType: "{{ servicePrincipalType }}"
          history: "{{ history }}"
          activity: "{{ activity }}"
          initiatedBy: "{{ initiatedBy }}"
    - name: activity
      value: "{{ activity }}"
      description: |
        The activity related to service principal risk level change.
    - name: initiatedBy
      value: "{{ initiatedBy }}"
      description: |
        The identifier of the actor of the operation.
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
UPDATE entra_id.identity_protection.risky_service_principals_history
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
appId = '{{ appId }}',
displayName = '{{ displayName }}',
isEnabled = {{ isEnabled }},
isProcessing = {{ isProcessing }},
riskDetail = '{{ riskDetail }}',
riskLastUpdatedDateTime = '{{ riskLastUpdatedDateTime }}',
riskLevel = '{{ riskLevel }}',
riskState = '{{ riskState }}',
servicePrincipalType = '{{ servicePrincipalType }}',
history = '{{ history }}',
activity = '{{ activity }}',
initiatedBy = '{{ initiatedBy }}'
WHERE 
riskyServicePrincipal-id = '{{ riskyServicePrincipal-id }}' --required
AND riskyServicePrincipalHistoryItem-id = '{{ riskyServicePrincipalHistoryItem-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
activity,
appId,
displayName,
history,
initiatedBy,
isEnabled,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
servicePrincipalType;
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
DELETE FROM entra_id.identity_protection.risky_service_principals_history
WHERE riskyServicePrincipal-id = '{{ riskyServicePrincipal-id }}' --required
AND riskyServicePrincipalHistoryItem-id = '{{ riskyServicePrincipalHistoryItem-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
