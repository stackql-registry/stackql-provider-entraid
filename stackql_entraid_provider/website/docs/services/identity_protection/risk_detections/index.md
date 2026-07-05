--- 
title: risk_detections
hide_title: false
hide_table_of_contents: false
keywords:
  - risk_detections
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

Creates, updates, deletes, gets or lists a <code>risk_detections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="risk_detections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_protection.risk_detections" /></td></tr>
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
    <td>Indicates the activity type the detected risk is linked to.</td>
</tr>
<tr>
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="additionalInfo" /></td>
    <td><code>string</code></td>
    <td>Additional information associated with the risk detection in JSON format. For example, '[&#123;/'Key/':/'userAgent/',/'Value/':/'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36/'&#125;]'. Possible keys in the additionalInfo JSON string are: userAgent, alertUrl, relatedEventTimeInUtc, relatedUserAgent, deviceInformation, relatedLocation, requestId, correlationId, lastActivityTimeInUtc, malwareName, clientLocation, clientIp, riskReasons. For more information about riskReasons and possible values, see riskReasons values.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="detectedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="detectionTimingType" /></td>
    <td><code></code></td>
    <td>Timing of the detected risk (real-time/offline). The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Provides the IP address of the client from where the risk occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time that the risk detection was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code></code></td>
    <td>Location of the sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="requestId" /></td>
    <td><code>string</code></td>
    <td>Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk.</td>
</tr>
<tr>
    <td><CopyableCode code="riskEventType" /></td>
    <td><code>string</code></td>
    <td>The type of risk event detected. The possible values are adminConfirmedUserCompromised, anomalousToken, anomalousUserActivity, anonymizedIPAddress, generic, impossibleTravel, investigationsThreatIntelligence, suspiciousSendingPatterns, leakedCredentials, maliciousIPAddress,malwareInfectedIPAddress, mcasSuspiciousInboxManipulationRules, newCountry, passwordSpray,riskyIPAddress, suspiciousAPITraffic, suspiciousBrowser,suspiciousInboxForwarding, suspiciousIPAddress, tokenIssuerAnomaly, unfamiliarFeatures, unlikelyTravel. If the risk detection is a premium detection, will show generic. For more information about each value, see Risk types and detection.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risk. The possible values are: low, medium, high, hidden, none, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>The state of a detected risky user or sign-in. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the risk detection. For example, activeDirectory.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuerType" /></td>
    <td><code></code></td>
    <td>Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD, ADFederationServices, UnknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="userDisplayName" /></td>
    <td><code>string</code></td>
    <td>The user principal name (UPN) of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name (UPN) of the user.</td>
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
    <td>Indicates the activity type the detected risk is linked to.</td>
</tr>
<tr>
    <td><CopyableCode code="activityDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="additionalInfo" /></td>
    <td><code>string</code></td>
    <td>Additional information associated with the risk detection in JSON format. For example, '[&#123;/'Key/':/'userAgent/',/'Value/':/'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36/'&#125;]'. Possible keys in the additionalInfo JSON string are: userAgent, alertUrl, relatedEventTimeInUtc, relatedUserAgent, deviceInformation, relatedLocation, requestId, correlationId, lastActivityTimeInUtc, malwareName, clientLocation, clientIp, riskReasons. For more information about riskReasons and possible values, see riskReasons values.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="detectedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="detectionTimingType" /></td>
    <td><code></code></td>
    <td>Timing of the detected risk (real-time/offline). The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Provides the IP address of the client from where the risk occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time that the risk detection was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code></code></td>
    <td>Location of the sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="requestId" /></td>
    <td><code>string</code></td>
    <td>Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk.</td>
</tr>
<tr>
    <td><CopyableCode code="riskEventType" /></td>
    <td><code>string</code></td>
    <td>The type of risk event detected. The possible values are adminConfirmedUserCompromised, anomalousToken, anomalousUserActivity, anonymizedIPAddress, generic, impossibleTravel, investigationsThreatIntelligence, suspiciousSendingPatterns, leakedCredentials, maliciousIPAddress,malwareInfectedIPAddress, mcasSuspiciousInboxManipulationRules, newCountry, passwordSpray,riskyIPAddress, suspiciousAPITraffic, suspiciousBrowser,suspiciousInboxForwarding, suspiciousIPAddress, tokenIssuerAnomaly, unfamiliarFeatures, unlikelyTravel. If the risk detection is a premium detection, will show generic. For more information about each value, see Risk types and detection.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risk. The possible values are: low, medium, high, hidden, none, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>The state of a detected risky user or sign-in. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Source of the risk detection. For example, activeDirectory.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuerType" /></td>
    <td><code></code></td>
    <td>Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD, ADFederationServices, UnknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="userDisplayName" /></td>
    <td><code>string</code></td>
    <td>The user principal name (UPN) of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="userId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of the user.</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name (UPN) of the user.</td>
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
    <td><a href="#parameter-risk_detection_id"><code>risk_detection_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a riskDetection object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the riskDetection objects and their properties.</td>
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
    <td><a href="#parameter-risk_detection_id"><code>risk_detection_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-risk_detection_id"><code>risk_detection_id</code></a></td>
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
<tr id="parameter-risk_detection_id">
    <td><CopyableCode code="risk_detection_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of riskDetection</td>
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

Read the properties and relationships of a riskDetection object.

```sql
SELECT
id,
activity,
activityDateTime,
additionalInfo,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
source,
tokenIssuerType,
userDisplayName,
userId,
userPrincipalName
FROM entra_id.identity_protection.risk_detections
WHERE risk_detection_id = '{{ risk_detection_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the riskDetection objects and their properties.

```sql
SELECT
id,
activity,
activityDateTime,
additionalInfo,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
source,
tokenIssuerType,
userDisplayName,
userId,
userPrincipalName
FROM entra_id.identity_protection.risk_detections
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
INSERT INTO entra_id.identity_protection.risk_detections (
id,
activity,
activityDateTime,
additionalInfo,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
source,
tokenIssuerType,
userDisplayName,
userId,
userPrincipalName
)
SELECT 
'{{ id }}',
'{{ activity }}',
'{{ activityDateTime }}',
'{{ additionalInfo }}',
'{{ correlationId }}',
'{{ detectedDateTime }}',
'{{ detectionTimingType }}',
'{{ ipAddress }}',
'{{ lastUpdatedDateTime }}',
'{{ location }}',
'{{ requestId }}',
'{{ riskDetail }}',
'{{ riskEventType }}',
'{{ riskLevel }}',
'{{ riskState }}',
'{{ source }}',
'{{ tokenIssuerType }}',
'{{ userDisplayName }}',
'{{ userId }}',
'{{ userPrincipalName }}'
RETURNING
id,
activity,
activityDateTime,
additionalInfo,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
source,
tokenIssuerType,
userDisplayName,
userId,
userPrincipalName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: risk_detections
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: activity
      value: "{{ activity }}"
      description: |
        Indicates the activity type the detected risk is linked to.
    - name: activityDateTime
      value: "{{ activityDateTime }}"
      description: |
        Date and time that the risky activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
    - name: additionalInfo
      value: "{{ additionalInfo }}"
      description: |
        Additional information associated with the risk detection in JSON format. For example, '[{/'Key/':/'userAgent/',/'Value/':/'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36/'}]'. Possible keys in the additionalInfo JSON string are: userAgent, alertUrl, relatedEventTimeInUtc, relatedUserAgent, deviceInformation, relatedLocation, requestId, correlationId, lastActivityTimeInUtc, malwareName, clientLocation, clientIp, riskReasons. For more information about riskReasons and possible values, see riskReasons values.
    - name: correlationId
      value: "{{ correlationId }}"
      description: |
        Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
    - name: detectedDateTime
      value: "{{ detectedDateTime }}"
      description: |
        Date and time that the risk was detected. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: 2014-01-01T00:00:00Z
    - name: detectionTimingType
      value: "{{ detectionTimingType }}"
      description: |
        Timing of the detected risk (real-time/offline). The possible values are: notDefined, realtime, nearRealtime, offline, unknownFutureValue.
    - name: ipAddress
      value: "{{ ipAddress }}"
      description: |
        Provides the IP address of the client from where the risk occurred.
    - name: lastUpdatedDateTime
      value: "{{ lastUpdatedDateTime }}"
      description: |
        Date and time that the risk detection was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is look like this: 2014-01-01T00:00:00Z
    - name: location
      value: "{{ location }}"
      description: |
        Location of the sign-in.
    - name: requestId
      value: "{{ requestId }}"
      description: |
        Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in.
    - name: riskDetail
      value: "{{ riskDetail }}"
      description: |
        Details of the detected risk.
    - name: riskEventType
      value: "{{ riskEventType }}"
      description: |
        The type of risk event detected. The possible values are adminConfirmedUserCompromised, anomalousToken, anomalousUserActivity, anonymizedIPAddress, generic, impossibleTravel, investigationsThreatIntelligence, suspiciousSendingPatterns, leakedCredentials, maliciousIPAddress,malwareInfectedIPAddress, mcasSuspiciousInboxManipulationRules, newCountry, passwordSpray,riskyIPAddress, suspiciousAPITraffic, suspiciousBrowser,suspiciousInboxForwarding, suspiciousIPAddress, tokenIssuerAnomaly, unfamiliarFeatures, unlikelyTravel. If the risk detection is a premium detection, will show generic. For more information about each value, see Risk types and detection.
    - name: riskLevel
      value: "{{ riskLevel }}"
      description: |
        Level of the detected risk. The possible values are: low, medium, high, hidden, none, unknownFutureValue.
    - name: riskState
      value: "{{ riskState }}"
      description: |
        The state of a detected risky user or sign-in. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
    - name: source
      value: "{{ source }}"
      description: |
        Source of the risk detection. For example, activeDirectory.
    - name: tokenIssuerType
      value: "{{ tokenIssuerType }}"
      description: |
        Indicates the type of token issuer for the detected sign-in risk. The possible values are: AzureAD, ADFederationServices, UnknownFutureValue.
    - name: userDisplayName
      value: "{{ userDisplayName }}"
      description: |
        The user principal name (UPN) of the user.
    - name: userId
      value: "{{ userId }}"
      description: |
        Unique ID of the user.
    - name: userPrincipalName
      value: "{{ userPrincipalName }}"
      description: |
        The user principal name (UPN) of the user.
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
UPDATE entra_id.identity_protection.risk_detections
SET 
id = '{{ id }}',
activity = '{{ activity }}',
activityDateTime = '{{ activityDateTime }}',
additionalInfo = '{{ additionalInfo }}',
correlationId = '{{ correlationId }}',
detectedDateTime = '{{ detectedDateTime }}',
detectionTimingType = '{{ detectionTimingType }}',
ipAddress = '{{ ipAddress }}',
lastUpdatedDateTime = '{{ lastUpdatedDateTime }}',
location = '{{ location }}',
requestId = '{{ requestId }}',
riskDetail = '{{ riskDetail }}',
riskEventType = '{{ riskEventType }}',
riskLevel = '{{ riskLevel }}',
riskState = '{{ riskState }}',
source = '{{ source }}',
tokenIssuerType = '{{ tokenIssuerType }}',
userDisplayName = '{{ userDisplayName }}',
userId = '{{ userId }}',
userPrincipalName = '{{ userPrincipalName }}'
WHERE 
risk_detection_id = '{{ risk_detection_id }}' --required
RETURNING
id,
activity,
activityDateTime,
additionalInfo,
correlationId,
detectedDateTime,
detectionTimingType,
ipAddress,
lastUpdatedDateTime,
location,
requestId,
riskDetail,
riskEventType,
riskLevel,
riskState,
source,
tokenIssuerType,
userDisplayName,
userId,
userPrincipalName;
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
DELETE FROM entra_id.identity_protection.risk_detections
WHERE risk_detection_id = '{{ risk_detection_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
