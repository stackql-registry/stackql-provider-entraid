--- 
title: risky_users
hide_title: false
hide_table_of_contents: false
keywords:
  - risky_users
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

Creates, updates, deletes, gets or lists a <code>risky_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="risky_users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_protection.risky_users" /></td></tr>
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
    <td><CopyableCode code="history" /></td>
    <td><code>array</code></td>
    <td>The activity related to user risk level change</td>
</tr>
<tr>
    <td><CopyableCode code="isDeleted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the user is deleted. The possible values are: true, false.</td>
</tr>
<tr>
    <td><CopyableCode code="isProcessing" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the backend is processing a user's risky state.</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the risky user was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risky user. The possible values are: low, medium, high, hidden, none, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>State of the user's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="userDisplayName" /></td>
    <td><code>string</code></td>
    <td>Risky user display name.</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>Risky user principal name.</td>
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
    <td><CopyableCode code="history" /></td>
    <td><code>array</code></td>
    <td>The activity related to user risk level change</td>
</tr>
<tr>
    <td><CopyableCode code="isDeleted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the user is deleted. The possible values are: true, false.</td>
</tr>
<tr>
    <td><CopyableCode code="isProcessing" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the backend is processing a user's risky state.</td>
</tr>
<tr>
    <td><CopyableCode code="riskDetail" /></td>
    <td><code></code></td>
    <td>Details of the detected risk.</td>
</tr>
<tr>
    <td><CopyableCode code="riskLastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that the risky user was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="riskLevel" /></td>
    <td><code></code></td>
    <td>Level of the detected risky user. The possible values are: low, medium, high, hidden, none, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="riskState" /></td>
    <td><code></code></td>
    <td>State of the user's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="userDisplayName" /></td>
    <td><code>string</code></td>
    <td>Risky user display name.</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>Risky user principal name.</td>
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
    <td><a href="#parameter-risky_user_id"><code>risky_user_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a riskyUser object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the riskyUser objects and their properties.</td>
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
    <td><a href="#parameter-risky_user_id"><code>risky_user_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-risky_user_id"><code>risky_user_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#confirm_compromised"><CopyableCode code="confirm_compromised" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Confirm one or more riskyUser objects as compromised. This action sets the targeted user's risk level to high.</td>
</tr>
<tr>
    <td><a href="#confirm_safe"><CopyableCode code="confirm_safe" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Confirm one or more riskyUser objects as safe. This action sets the targeted user's risk level to none.</td>
</tr>
<tr>
    <td><a href="#dismiss"><CopyableCode code="dismiss" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Dismiss the risk of one or more riskyUser objects. This action sets the targeted user's risk level to none.</td>
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
<tr id="parameter-risky_user_id">
    <td><CopyableCode code="risky_user_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of riskyUser</td>
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

Read the properties and relationships of a riskyUser object.

```sql
SELECT
id,
history,
isDeleted,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
userDisplayName,
userPrincipalName
FROM entra_id.identity_protection.risky_users
WHERE risky_user_id = '{{ risky_user_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the riskyUser objects and their properties.

```sql
SELECT
id,
history,
isDeleted,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
userDisplayName,
userPrincipalName
FROM entra_id.identity_protection.risky_users
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
INSERT INTO entra_id.identity_protection.risky_users (
id,
isDeleted,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
userDisplayName,
userPrincipalName,
history
)
SELECT 
'{{ id }}',
{{ isDeleted }},
{{ isProcessing }},
'{{ riskDetail }}',
'{{ riskLastUpdatedDateTime }}',
'{{ riskLevel }}',
'{{ riskState }}',
'{{ userDisplayName }}',
'{{ userPrincipalName }}',
'{{ history }}'
RETURNING
id,
history,
isDeleted,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
userDisplayName,
userPrincipalName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: risky_users
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: isDeleted
      value: {{ isDeleted }}
      description: |
        Indicates whether the user is deleted. The possible values are: true, false.
    - name: isProcessing
      value: {{ isProcessing }}
      description: |
        Indicates whether the backend is processing a user's risky state.
    - name: riskDetail
      value: "{{ riskDetail }}"
      description: |
        Details of the detected risk.
    - name: riskLastUpdatedDateTime
      value: "{{ riskLastUpdatedDateTime }}"
      description: |
        The date and time that the risky user was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: riskLevel
      value: "{{ riskLevel }}"
      description: |
        Level of the detected risky user. The possible values are: low, medium, high, hidden, none, unknownFutureValue.
    - name: riskState
      value: "{{ riskState }}"
      description: |
        State of the user's risk. The possible values are: none, confirmedSafe, remediated, dismissed, atRisk, confirmedCompromised, unknownFutureValue.
    - name: userDisplayName
      value: "{{ userDisplayName }}"
      description: |
        Risky user display name.
    - name: userPrincipalName
      value: "{{ userPrincipalName }}"
      description: |
        Risky user principal name.
    - name: history
      description: |
        The activity related to user risk level change
      value:
        - id: "{{ id }}"
          isDeleted: {{ isDeleted }}
          isProcessing: {{ isProcessing }}
          riskDetail: "{{ riskDetail }}"
          riskLastUpdatedDateTime: "{{ riskLastUpdatedDateTime }}"
          riskLevel: "{{ riskLevel }}"
          riskState: "{{ riskState }}"
          userDisplayName: "{{ userDisplayName }}"
          userPrincipalName: "{{ userPrincipalName }}"
          history: "{{ history }}"
          activity: "{{ activity }}"
          initiatedBy: "{{ initiatedBy }}"
          userId: "{{ userId }}"
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
UPDATE entra_id.identity_protection.risky_users
SET 
id = '{{ id }}',
isDeleted = {{ isDeleted }},
isProcessing = {{ isProcessing }},
riskDetail = '{{ riskDetail }}',
riskLastUpdatedDateTime = '{{ riskLastUpdatedDateTime }}',
riskLevel = '{{ riskLevel }}',
riskState = '{{ riskState }}',
userDisplayName = '{{ userDisplayName }}',
userPrincipalName = '{{ userPrincipalName }}',
history = '{{ history }}'
WHERE 
risky_user_id = '{{ risky_user_id }}' --required
RETURNING
id,
history,
isDeleted,
isProcessing,
riskDetail,
riskLastUpdatedDateTime,
riskLevel,
riskState,
userDisplayName,
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
DELETE FROM entra_id.identity_protection.risky_users
WHERE risky_user_id = '{{ risky_user_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="confirm_compromised"
    values={[
        { label: 'confirm_compromised', value: 'confirm_compromised' },
        { label: 'confirm_safe', value: 'confirm_safe' },
        { label: 'dismiss', value: 'dismiss' }
    ]}
>
<TabItem value="confirm_compromised">

Confirm one or more riskyUser objects as compromised. This action sets the targeted user's risk level to high.

```sql
EXEC entra_id.identity_protection.risky_users.confirm_compromised 
@@json=
'{
"userIds": "{{ userIds }}"
}'
;
```
</TabItem>
<TabItem value="confirm_safe">

Confirm one or more riskyUser objects as safe. This action sets the targeted user's risk level to none.

```sql
EXEC entra_id.identity_protection.risky_users.confirm_safe 
@@json=
'{
"userIds": "{{ userIds }}"
}'
;
```
</TabItem>
<TabItem value="dismiss">

Dismiss the risk of one or more riskyUser objects. This action sets the targeted user's risk level to none.

```sql
EXEC entra_id.identity_protection.risky_users.dismiss 
@@json=
'{
"userIds": "{{ userIds }}"
}'
;
```
</TabItem>
</Tabs>
