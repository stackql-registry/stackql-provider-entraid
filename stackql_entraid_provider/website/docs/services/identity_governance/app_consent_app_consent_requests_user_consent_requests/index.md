--- 
title: app_consent_app_consent_requests_user_consent_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - app_consent_app_consent_requests_user_consent_requests
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

Creates, updates, deletes, gets or lists an <code>app_consent_app_consent_requests_user_consent_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_consent_app_consent_requests_user_consent_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests" /></td></tr>
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
    <td><CopyableCode code="approval" /></td>
    <td><code></code></td>
    <td>Approval decisions associated with a request.</td>
</tr>
<tr>
    <td><CopyableCode code="approvalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the approval of the request.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request completion date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>The principal that created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request creation date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customData" /></td>
    <td><code>string</code></td>
    <td>Free text field to define any custom data for the request. Not used.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.</td>
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
    <td><CopyableCode code="approval" /></td>
    <td><code></code></td>
    <td>Approval decisions associated with a request.</td>
</tr>
<tr>
    <td><CopyableCode code="approvalId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the approval of the request.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request completion date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code></code></td>
    <td>The principal that created the request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The request creation date time. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customData" /></td>
    <td><code>string</code></td>
    <td>Free text field to define any custom data for the request. Not used.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.</td>
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
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a>, <a href="#parameter-user_consent_request_id"><code>user_consent_request_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of a userConsentRequest object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a></td>
    <td></td>
    <td>Retrieve a collection of userConsentRequest objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a>, <a href="#parameter-user_consent_request_id"><code>user_consent_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-app_consent_request_id"><code>app_consent_request_id</code></a>, <a href="#parameter-user_consent_request_id"><code>user_consent_request_id</code></a></td>
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
<tr id="parameter-app_consent_request_id">
    <td><CopyableCode code="app_consent_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of appConsentRequest</td>
</tr>
<tr id="parameter-user_consent_request_id">
    <td><CopyableCode code="user_consent_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of userConsentRequest</td>
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

Read the properties and relationships of a userConsentRequest object.

```sql
SELECT
id,
approval,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
reason,
status
FROM entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests
WHERE app_consent_request_id = '{{ app_consent_request_id }}' -- required
AND user_consent_request_id = '{{ user_consent_request_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a collection of userConsentRequest objects and their properties.

```sql
SELECT
id,
approval,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
reason,
status
FROM entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests
WHERE app_consent_request_id = '{{ app_consent_request_id }}' -- required
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
INSERT INTO entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests (
id,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
status,
reason,
approval,
app_consent_request_id
)
SELECT 
'{{ id }}',
'{{ approvalId }}',
'{{ completedDateTime }}',
'{{ createdBy }}',
'{{ createdDateTime }}',
'{{ customData }}',
'{{ status }}',
'{{ reason }}',
'{{ approval }}',
'{{ app_consent_request_id }}'
RETURNING
id,
approval,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
reason,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_consent_app_consent_requests_user_consent_requests
  props:
    - name: app_consent_request_id
      value: "{{ app_consent_request_id }}"
      description: Required parameter for the app_consent_app_consent_requests_user_consent_requests resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: approvalId
      value: "{{ approvalId }}"
      description: |
        The identifier of the approval of the request.
    - name: completedDateTime
      value: "{{ completedDateTime }}"
      description: |
        The request completion date time.
    - name: createdBy
      value: "{{ createdBy }}"
      description: |
        The principal that created the request.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The request creation date time.
    - name: customData
      value: "{{ customData }}"
      description: |
        Free text field to define any custom data for the request. Not used.
    - name: status
      value: "{{ status }}"
      description: |
        The status of the request. Not nullable. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable.
    - name: reason
      value: "{{ reason }}"
      description: |
        The user's justification for requiring access to the app. Supports $filter (eq only) and $orderby.
    - name: approval
      value: "{{ approval }}"
      description: |
        Approval decisions associated with a request.
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
UPDATE entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests
SET 
id = '{{ id }}',
approvalId = '{{ approvalId }}',
completedDateTime = '{{ completedDateTime }}',
createdBy = '{{ createdBy }}',
createdDateTime = '{{ createdDateTime }}',
customData = '{{ customData }}',
status = '{{ status }}',
reason = '{{ reason }}',
approval = '{{ approval }}'
WHERE 
app_consent_request_id = '{{ app_consent_request_id }}' --required
AND user_consent_request_id = '{{ user_consent_request_id }}' --required
RETURNING
id,
approval,
approvalId,
completedDateTime,
createdBy,
createdDateTime,
customData,
reason,
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

No description available.

```sql
DELETE FROM entra_id.identity_governance.app_consent_app_consent_requests_user_consent_requests
WHERE app_consent_request_id = '{{ app_consent_request_id }}' --required
AND user_consent_request_id = '{{ user_consent_request_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
