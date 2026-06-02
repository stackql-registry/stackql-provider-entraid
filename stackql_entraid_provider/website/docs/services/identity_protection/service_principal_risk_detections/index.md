--- 
title: service_principal_risk_detections
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principal_risk_detections
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

Creates, updates, deletes, gets or lists a <code>service_principal_risk_detections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_principal_risk_detections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_protection.service_principal_risk_detections" /></td></tr>
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
    <td>Indicates the activity type the detected risk is linked to.</td>
</tr>
<tr>
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="additionalInfo" /></td>
    <td><code>string</code></td>
    <td>Additional information associated with the risk detection. This string value is represented as a JSON object with the quotations escaped.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated application.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Correlation ID of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity.</td>
</tr>
<tr>
    <td><CopyableCode code="detectedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="detectionTimingType" /></td>
    <td><code></code></td>
    <td>Timing of the detected risk , whether real-time or offline. The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Provides the IP address of the client from where the risk occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="keyIds" /></td>
    <td><code>array</code></td>
    <td>The unique identifier for the key credential associated with the risk detection.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the risk detection was last updated. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code></code></td>
    <td>Location from where the sign-in was initiated.</td>
</tr>
<tr>
    <td><CopyableCode code="requestId" /></td>
    <td><code>string</code></td>
    <td>Request identifier of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.</td>
</tr>
<tr>
    <td><CopyableCode code="riskEventType" /></td>
    <td><code>string</code></td>
    <td>The type of risk event detected. The possible values are: investigationsThreatIntelligence, generic, adminConfirmedServicePrincipalCompromised, suspiciousSignins, leakedCredentials, anomalousServicePrincipalActivity, maliciousApplication, suspiciousApplication.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: low, medium, high, hidden, none.</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>The state of a detected risky service principal or sign-in activity. The possible values are: none, dismissed, atRisk, confirmedCompromised.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the service principal. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the risk detection. For example, identityProtection.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuerType" /></td>
    <td><code></code></td>
    <td>Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD.</td>
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
    <td>Indicates the activity type the detected risk is linked to.</td>
</tr>
<tr>
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="additionalInfo" /></td>
    <td><code>string</code></td>
    <td>Additional information associated with the risk detection. This string value is represented as a JSON object with the quotations escaped.</td>
</tr>
<tr>
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the associated application.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Correlation ID of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity.</td>
</tr>
<tr>
    <td><CopyableCode code="detectedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="detectionTimingType" /></td>
    <td><code></code></td>
    <td>Timing of the detected risk , whether real-time or offline. The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Provides the IP address of the client from where the risk occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="keyIds" /></td>
    <td><code>array</code></td>
    <td>The unique identifier for the key credential associated with the risk detection.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the risk detection was last updated. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code></code></td>
    <td>Location from where the sign-in was initiated.</td>
</tr>
<tr>
    <td><CopyableCode code="requestId" /></td>
    <td><code>string</code></td>
    <td>Request identifier of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.</td>
</tr>
<tr>
    <td><CopyableCode code="riskEventType" /></td>
    <td><code>string</code></td>
    <td>The type of risk event detected. The possible values are: investigationsThreatIntelligence, generic, adminConfirmedServicePrincipalCompromised, suspiciousSignins, leakedCredentials, anomalousServicePrincipalActivity, maliciousApplication, suspiciousApplication.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: low, medium, high, hidden, none.</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>The state of a detected risky service principal or sign-in activity. The possible values are: none, dismissed, atRisk, confirmedCompromised.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the service principal.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier for the service principal. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the risk detection. For example, identityProtection.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuerType" /></td>
    <td><code></code></td>
    <td>Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD.</td>
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
    <td><a href="#parameter-servicePrincipalRiskDetection-id"><code>servicePrincipalRiskDetection-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of a servicePrincipalRiskDetection object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties of a collection of servicePrincipalRiskDetection objects.</td>
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
    <td><a href="#parameter-servicePrincipalRiskDetection-id"><code>servicePrincipalRiskDetection-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-servicePrincipalRiskDetection-id"><code>servicePrincipalRiskDetection-id</code></a></td>
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
<tr id="parameter-servicePrincipalRiskDetection-id">
    <td><CopyableCode code="servicePrincipalRiskDetection-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipalRiskDetection</td>
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

Read the properties and relationships of a servicePrincipalRiskDetection object.

```sql
SELECT
id,
@odata.type,
activity,
activityDateTime,
additionalInfo,
appId,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
keyIds,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
servicePrincipalDisplayName,
servicePrincipalId,
source,
tokenIssuerType
FROM entra_id.identity_protection.service_principal_risk_detections
WHERE servicePrincipalRiskDetection-id = '{{ servicePrincipalRiskDetection-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve the properties of a collection of servicePrincipalRiskDetection objects.

```sql
SELECT
id,
@odata.type,
activity,
activityDateTime,
additionalInfo,
appId,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
keyIds,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
servicePrincipalDisplayName,
servicePrincipalId,
source,
tokenIssuerType
FROM entra_id.identity_protection.service_principal_risk_detections
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
INSERT INTO entra_id.identity_protection.service_principal_risk_detections (
id,
@odata.type,
activity,
activityDateTime,
additionalInfo,
appId,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
keyIds,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
servicePrincipalDisplayName,
servicePrincipalId,
source,
tokenIssuerType
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ activity }}',
'{{ activityDateTime }}',
'{{ additionalInfo }}',
'{{ appId }}',
'{{ correlationId }}',
'{{ detectedDateTime }}',
'{{ detectionTimingType }}',
'{{ ipAddress }}',
'{{ keyIds }}',
'{{ lastUpdatedDateTime }}',
'{{ location }}',
'{{ requestId }}',
'{{ riskDetail }}',
'{{ riskEventType }}',
'{{ riskLevel }}',
'{{ riskState }}',
'{{ servicePrincipalDisplayName }}',
'{{ servicePrincipalId }}',
'{{ source }}',
'{{ tokenIssuerType }}'
RETURNING
id,
@odata.type,
activity,
activityDateTime,
additionalInfo,
appId,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
keyIds,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
servicePrincipalDisplayName,
servicePrincipalId,
source,
tokenIssuerType
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: service_principal_risk_detections
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: activity
      value: "{{ activity }}"
      description: |
        Indicates the activity type the detected risk is linked to.
    - name: activityDateTime
      value: "{{ activityDateTime }}"
      description: |
        Date and time when the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    - name: additionalInfo
      value: "{{ additionalInfo }}"
      description: |
        Additional information associated with the risk detection. This string value is represented as a JSON object with the quotations escaped.
    - name: appId
      value: "{{ appId }}"
      description: |
        The unique identifier for the associated application.
    - name: correlationId
      value: "{{ correlationId }}"
      description: |
        Correlation ID of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity.
    - name: detectedDateTime
      value: "{{ detectedDateTime }}"
      description: |
        Date and time when the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: detectionTimingType
      value: "{{ detectionTimingType }}"
      description: |
        Timing of the detected risk , whether real-time or offline. The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
    - name: ipAddress
      value: "{{ ipAddress }}"
      description: |
        Provides the IP address of the client from where the risk occurred.
    - name: keyIds
      value:
        - "{{ keyIds }}"
      description: |
        The unique identifier for the key credential associated with the risk detection.
    - name: lastUpdatedDateTime
      value: "{{ lastUpdatedDateTime }}"
      description: |
        Date and time when the risk detection was last updated.
    - name: location
      value: "{{ location }}"
      description: |
        Location from where the sign-in was initiated.
    - name: requestId
      value: "{{ requestId }}"
      description: |
        Request identifier of the sign-in activity associated with the risk detection. This property is null if the risk detection is not associated with a sign-in activity. Supports $filter (eq).
    - name: riskDetail
      value: "{{ riskDetail }}"
      description: |
        Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden.
    - name: riskEventType
      value: "{{ riskEventType }}"
      description: |
        The type of risk event detected. The possible values are: investigationsThreatIntelligence, generic, adminConfirmedServicePrincipalCompromised, suspiciousSignins, leakedCredentials, anomalousServicePrincipalActivity, maliciousApplication, suspiciousApplication.
    - name: riskLevel
      value: "{{ riskLevel }}"
      description: |
        Level of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: low, medium, high, hidden, none.
    - name: riskState
      value: "{{ riskState }}"
      description: |
        The state of a detected risky service principal or sign-in activity. The possible values are: none, dismissed, atRisk, confirmedCompromised.
    - name: servicePrincipalDisplayName
      value: "{{ servicePrincipalDisplayName }}"
      description: |
        The display name for the service principal.
    - name: servicePrincipalId
      value: "{{ servicePrincipalId }}"
      description: |
        The unique identifier for the service principal. Supports $filter (eq).
    - name: source
      value: "{{ source }}"
      description: |
        Source of the risk detection. For example, identityProtection.
    - name: tokenIssuerType
      value: "{{ tokenIssuerType }}"
      description: |
        Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD.
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
UPDATE entra_id.identity_protection.service_principal_risk_detections
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
activity = '{{ activity }}',
activityDateTime = '{{ activityDateTime }}',
additionalInfo = '{{ additionalInfo }}',
appId = '{{ appId }}',
correlationId = '{{ correlationId }}',
detectedDateTime = '{{ detectedDateTime }}',
detectionTimingType = '{{ detectionTimingType }}',
ipAddress = '{{ ipAddress }}',
keyIds = '{{ keyIds }}',
lastUpdatedDateTime = '{{ lastUpdatedDateTime }}',
location = '{{ location }}',
requestId = '{{ requestId }}',
riskDetail = '{{ riskDetail }}',
riskEventType = '{{ riskEventType }}',
riskLevel = '{{ riskLevel }}',
riskState = '{{ riskState }}',
servicePrincipalDisplayName = '{{ servicePrincipalDisplayName }}',
servicePrincipalId = '{{ servicePrincipalId }}',
source = '{{ source }}',
tokenIssuerType = '{{ tokenIssuerType }}'
WHERE 
servicePrincipalRiskDetection-id = '{{ servicePrincipalRiskDetection-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
activity,
activityDateTime,
additionalInfo,
appId,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
keyIds,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
servicePrincipalDisplayName,
servicePrincipalId,
source,
tokenIssuerType;
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
DELETE FROM entra_id.identity_protection.service_principal_risk_detections
WHERE servicePrincipalRiskDetection-id = '{{ servicePrincipalRiskDetection-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
