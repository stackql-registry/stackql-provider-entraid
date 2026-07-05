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
    <td><a href="#parameter-risky_service_principal_id"><code>risky_service_principal_id</code></a>, <a href="#parameter-risky_service_principal_history_item_id"><code>risky_service_principal_history_item_id</code></a></td>
    <td></td>
    <td>Represents the risk history of Microsoft Entra service principals.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-risky_service_principal_id"><code>risky_service_principal_id</code></a></td>
    <td></td>
    <td>Get the risk history of a riskyServicePrincipal object.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-risky_service_principal_id"><code>risky_service_principal_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-risky_service_principal_id"><code>risky_service_principal_id</code></a>, <a href="#parameter-risky_service_principal_history_item_id"><code>risky_service_principal_history_item_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-risky_service_principal_id"><code>risky_service_principal_id</code></a>, <a href="#parameter-risky_service_principal_history_item_id"><code>risky_service_principal_history_item_id</code></a></td>
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
<tr id="parameter-risky_service_principal_history_item_id">
    <td><CopyableCode code="risky_service_principal_history_item_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of riskyServicePrincipalHistoryItem</td>
</tr>
<tr id="parameter-risky_service_principal_id">
    <td><CopyableCode code="risky_service_principal_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of riskyServicePrincipal</td>
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
WHERE risky_service_principal_id = '{{ risky_service_principal_id }}' -- required
AND risky_service_principal_history_item_id = '{{ risky_service_principal_history_item_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the risk history of a riskyServicePrincipal object.

```sql
SELECT
id,
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
WHERE risky_service_principal_id = '{{ risky_service_principal_id }}' -- required
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
risky_service_principal_id
)
SELECT 
'{{ id }}',
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
'{{ risky_service_principal_id }}'
RETURNING
id,
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
    - name: risky_service_principal_id
      value: "{{ risky_service_principal_id }}"
      description: Required parameter for the risky_service_principals_history resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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
risky_service_principal_id = '{{ risky_service_principal_id }}' --required
AND risky_service_principal_history_item_id = '{{ risky_service_principal_history_item_id }}' --required
RETURNING
id,
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
WHERE risky_service_principal_id = '{{ risky_service_principal_id }}' --required
AND risky_service_principal_history_item_id = '{{ risky_service_principal_history_item_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
