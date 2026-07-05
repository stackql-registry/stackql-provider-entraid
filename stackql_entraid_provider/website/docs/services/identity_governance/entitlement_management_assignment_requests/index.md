--- 
title: entitlement_management_assignment_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_assignment_requests
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_assignment_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_assignment_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_assignment_requests" /></td></tr>
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
    <td>The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="answers" /></td>
    <td><code>array</code></td>
    <td>Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.</td>
</tr>
<tr>
    <td><CopyableCode code="assignment" /></td>
    <td><code></code></td>
    <td>For a requestType of userAdd or adminAdd, this is an access package assignment requested to be created. For a requestType of userRemove, adminRemove, approverRemove, or systemRemove, this has the id property of an existing assignment to be removed.   Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customExtensionCalloutInstances" /></td>
    <td><code>array</code></td>
    <td>Information about all the custom extension calls that were made during the access package assignment workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>The requestor's supplied justification.</td>
</tr>
<tr>
    <td><CopyableCode code="requestType" /></td>
    <td><code></code></td>
    <td>The type of the request. The possible values are: notSpecified, userAdd, userUpdate, userRemove, adminAdd, adminUpdate, adminRemove, systemAdd, systemUpdate, systemRemove, onBehalfAdd (not supported), unknownFutureValue. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: approverRemove. Requests from the user have a requestType of userAdd, userUpdate, or userRemove. This property can't be changed once set.</td>
</tr>
<tr>
    <td><CopyableCode code="requestor" /></td>
    <td><code></code></td>
    <td>The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code></code></td>
    <td>The range of dates that access is to be assigned to the requestor. This property can't be changed once set, but a new schedule for an assignment can be included in another userUpdate or adminUpdate assignment request.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The state of the request. The possible values are: submitted, pendingApproval, delivering, delivered, deliveryFailed, denied, scheduled, canceled, partiallyDelivered, unknownFutureValue. Read-only. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>More information on the request processing status. Read-only.</td>
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
    <td>The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="answers" /></td>
    <td><code>array</code></td>
    <td>Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.</td>
</tr>
<tr>
    <td><CopyableCode code="assignment" /></td>
    <td><code></code></td>
    <td>For a requestType of userAdd or adminAdd, this is an access package assignment requested to be created. For a requestType of userRemove, adminRemove, approverRemove, or systemRemove, this has the id property of an existing assignment to be removed.   Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="completedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customExtensionCalloutInstances" /></td>
    <td><code>array</code></td>
    <td>Information about all the custom extension calls that were made during the access package assignment workflow.</td>
</tr>
<tr>
    <td><CopyableCode code="justification" /></td>
    <td><code>string</code></td>
    <td>The requestor's supplied justification.</td>
</tr>
<tr>
    <td><CopyableCode code="requestType" /></td>
    <td><code></code></td>
    <td>The type of the request. The possible values are: notSpecified, userAdd, userUpdate, userRemove, adminAdd, adminUpdate, adminRemove, systemAdd, systemUpdate, systemRemove, onBehalfAdd (not supported), unknownFutureValue. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: approverRemove. Requests from the user have a requestType of userAdd, userUpdate, or userRemove. This property can't be changed once set.</td>
</tr>
<tr>
    <td><CopyableCode code="requestor" /></td>
    <td><code></code></td>
    <td>The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code></code></td>
    <td>The range of dates that access is to be assigned to the requestor. This property can't be changed once set, but a new schedule for an assignment can be included in another userUpdate or adminUpdate assignment request.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The state of the request. The possible values are: submitted, pendingApproval, delivering, delivered, deliveryFailed, denied, scheduled, canceled, partiallyDelivered, unknownFutureValue. Read-only. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>More information on the request processing status. Read-only.</td>
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
    <td><a href="#parameter-access_package_assignment_request_id"><code>access_package_assignment_request_id</code></a></td>
    <td></td>
    <td>In Microsoft Entra entitlement management, retrieve the properties and relationships of an  accessPackageAssignmentRequest object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>In Microsoft Entra entitlement management, retrieve a list of accessPackageAssignmentRequest objects.  The resulting list includes all the assignment requests, current and well as expired, that the caller has access to read, across all catalogs and access packages.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>In Microsoft Entra Entitlement Management, create a new accessPackageAssignmentRequest object. This operation is used to assign a user to an access package, update the assignment, or to remove an access package assignment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_assignment_request_id"><code>access_package_assignment_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_assignment_request_id"><code>access_package_assignment_request_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an accessPackageAssignmentRequest object. This request can be made to remove a denied or completed request.  You cannot delete an access package assignment request if it has any accessPackageAssignment objects.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-access_package_assignment_request_id"><code>access_package_assignment_request_id</code></a></td>
    <td></td>
    <td>In Microsoft Entra Entitlement Management, cancel accessPackageAssignmentRequest objects that are in a cancellable state: accepted, pendingApproval, pendingNotBefore, pendingApprovalEscalated.</td>
</tr>
<tr>
    <td><a href="#reprocess"><CopyableCode code="reprocess" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-access_package_assignment_request_id"><code>access_package_assignment_request_id</code></a></td>
    <td></td>
    <td>In Microsoft Entra entitlement management, callers can automatically retry a user's request for access to an access package. It's performed on an accessPackageAssignmentRequest object whose requestState is in a DeliveryFailed or PartiallyDelivered state.  You can only reprocess a request within 14 days from the time the original request was completed. For requests completed more than 14 days, you will need to ask the users to cancel the request(s) and make a new request in the MyAccess portal.</td>
</tr>
<tr>
    <td><a href="#resume"><CopyableCode code="resume" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-access_package_assignment_request_id"><code>access_package_assignment_request_id</code></a></td>
    <td></td>
    <td>Resume a user's access package request after waiting for a callback from a custom extension. In Microsoft Entra entitlement management, when an access package policy has been enabled to call out a custom extension and the request processing is waiting for the callback from the customer, the customer can initiate a resume action. It's performed on an accessPackageAssignmentRequest object whose requestStatus is in a WaitingForCallback state.</td>
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
<tr id="parameter-access_package_assignment_request_id">
    <td><CopyableCode code="access_package_assignment_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageAssignmentRequest</td>
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

In Microsoft Entra entitlement management, retrieve the properties and relationships of an  accessPackageAssignmentRequest object.

```sql
SELECT
id,
accessPackage,
answers,
assignment,
completedDateTime,
createdDateTime,
customExtensionCalloutInstances,
justification,
requestType,
requestor,
schedule,
state,
status
FROM entra_id.identity_governance.entitlement_management_assignment_requests
WHERE access_package_assignment_request_id = '{{ access_package_assignment_request_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

In Microsoft Entra entitlement management, retrieve a list of accessPackageAssignmentRequest objects.  The resulting list includes all the assignment requests, current and well as expired, that the caller has access to read, across all catalogs and access packages.

```sql
SELECT
id,
accessPackage,
answers,
assignment,
completedDateTime,
createdDateTime,
customExtensionCalloutInstances,
justification,
requestType,
requestor,
schedule,
state,
status
FROM entra_id.identity_governance.entitlement_management_assignment_requests
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

In Microsoft Entra Entitlement Management, create a new accessPackageAssignmentRequest object. This operation is used to assign a user to an access package, update the assignment, or to remove an access package assignment.

```sql
INSERT INTO entra_id.identity_governance.entitlement_management_assignment_requests (
id,
answers,
completedDateTime,
createdDateTime,
customExtensionCalloutInstances,
justification,
requestType,
schedule,
state,
status,
accessPackage,
assignment,
requestor
)
SELECT 
'{{ id }}',
'{{ answers }}',
'{{ completedDateTime }}',
'{{ createdDateTime }}',
'{{ customExtensionCalloutInstances }}',
'{{ justification }}',
'{{ requestType }}',
'{{ schedule }}',
'{{ state }}',
'{{ status }}',
'{{ accessPackage }}',
'{{ assignment }}',
'{{ requestor }}'
RETURNING
id,
accessPackage,
answers,
assignment,
completedDateTime,
createdDateTime,
customExtensionCalloutInstances,
justification,
requestType,
requestor,
schedule,
state,
status
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_assignment_requests
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: answers
      description: |
        Answers provided by the requestor to accessPackageQuestions asked of them at the time of request.
      value:
        - displayValue: "{{ displayValue }}"
          answeredQuestion:
            id: "{{ id }}"
            isAnswerEditable: {{ isAnswerEditable }}
            isRequired: {{ isRequired }}
            localizations:
              - languageCode: "{{ languageCode }}"
                text: "{{ text }}"
            sequence: {{ sequence }}
            text: "{{ text }}"
    - name: completedDateTime
      value: "{{ completedDateTime }}"
      description: |
        The date of the end of processing, either successful or failure, of a request. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter.
    - name: customExtensionCalloutInstances
      description: |
        Information about all the custom extension calls that were made during the access package assignment workflow.
      value:
        - customExtensionId: "{{ customExtensionId }}"
          detail: "{{ detail }}"
          externalCorrelationId: "{{ externalCorrelationId }}"
          id: "{{ id }}"
          status: "{{ status }}"
    - name: justification
      value: "{{ justification }}"
      description: |
        The requestor's supplied justification.
    - name: requestType
      value: "{{ requestType }}"
      description: |
        The type of the request. The possible values are: notSpecified, userAdd, userUpdate, userRemove, adminAdd, adminUpdate, adminRemove, systemAdd, systemUpdate, systemRemove, onBehalfAdd (not supported), unknownFutureValue. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: approverRemove. Requests from the user have a requestType of userAdd, userUpdate, or userRemove. This property can't be changed once set.
    - name: schedule
      value: "{{ schedule }}"
      description: |
        The range of dates that access is to be assigned to the requestor. This property can't be changed once set, but a new schedule for an assignment can be included in another userUpdate or adminUpdate assignment request.
    - name: state
      value: "{{ state }}"
      description: |
        The state of the request. The possible values are: submitted, pendingApproval, delivering, delivered, deliveryFailed, denied, scheduled, canceled, partiallyDelivered, unknownFutureValue. Read-only. Supports $filter (eq).
    - name: status
      value: "{{ status }}"
      description: |
        More information on the request processing status. Read-only.
    - name: accessPackage
      value: "{{ accessPackage }}"
      description: |
        The access package associated with the accessPackageAssignmentRequest. An access package defines the collections of resource roles and the policies for how one or more users can get access to those resources. Read-only. Nullable.  Supports $expand.
    - name: assignment
      value: "{{ assignment }}"
      description: |
        For a requestType of userAdd or adminAdd, this is an access package assignment requested to be created. For a requestType of userRemove, adminRemove, approverRemove, or systemRemove, this has the id property of an existing assignment to be removed.   Supports $expand.
    - name: requestor
      value: "{{ requestor }}"
      description: |
        The subject who requested or, if a direct assignment, was assigned. Read-only. Nullable. Supports $expand.
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
UPDATE entra_id.identity_governance.entitlement_management_assignment_requests
SET 
id = '{{ id }}',
answers = '{{ answers }}',
completedDateTime = '{{ completedDateTime }}',
createdDateTime = '{{ createdDateTime }}',
customExtensionCalloutInstances = '{{ customExtensionCalloutInstances }}',
justification = '{{ justification }}',
requestType = '{{ requestType }}',
schedule = '{{ schedule }}',
state = '{{ state }}',
status = '{{ status }}',
accessPackage = '{{ accessPackage }}',
assignment = '{{ assignment }}',
requestor = '{{ requestor }}'
WHERE 
access_package_assignment_request_id = '{{ access_package_assignment_request_id }}' --required
RETURNING
id,
accessPackage,
answers,
assignment,
completedDateTime,
createdDateTime,
customExtensionCalloutInstances,
justification,
requestType,
requestor,
schedule,
state,
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

Delete an accessPackageAssignmentRequest object. This request can be made to remove a denied or completed request.  You cannot delete an access package assignment request if it has any accessPackageAssignment objects.

```sql
DELETE FROM entra_id.identity_governance.entitlement_management_assignment_requests
WHERE access_package_assignment_request_id = '{{ access_package_assignment_request_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'reprocess', value: 'reprocess' },
        { label: 'resume', value: 'resume' }
    ]}
>
<TabItem value="cancel">

In Microsoft Entra Entitlement Management, cancel accessPackageAssignmentRequest objects that are in a cancellable state: accepted, pendingApproval, pendingNotBefore, pendingApprovalEscalated.

```sql
EXEC entra_id.identity_governance.entitlement_management_assignment_requests.cancel 
@access_package_assignment_request_id='{{ access_package_assignment_request_id }}' --required
;
```
</TabItem>
<TabItem value="reprocess">

In Microsoft Entra entitlement management, callers can automatically retry a user's request for access to an access package. It's performed on an accessPackageAssignmentRequest object whose requestState is in a DeliveryFailed or PartiallyDelivered state.  You can only reprocess a request within 14 days from the time the original request was completed. For requests completed more than 14 days, you will need to ask the users to cancel the request(s) and make a new request in the MyAccess portal.

```sql
EXEC entra_id.identity_governance.entitlement_management_assignment_requests.reprocess 
@access_package_assignment_request_id='{{ access_package_assignment_request_id }}' --required
;
```
</TabItem>
<TabItem value="resume">

Resume a user's access package request after waiting for a callback from a custom extension. In Microsoft Entra entitlement management, when an access package policy has been enabled to call out a custom extension and the request processing is waiting for the callback from the customer, the customer can initiate a resume action. It's performed on an accessPackageAssignmentRequest object whose requestStatus is in a WaitingForCallback state.

```sql
EXEC entra_id.identity_governance.entitlement_management_assignment_requests.resume 
@access_package_assignment_request_id='{{ access_package_assignment_request_id }}' --required 
@@json=
'{
"source": "{{ source }}", 
"type": "{{ type }}", 
"data": "{{ data }}"
}'
;
```
</TabItem>
</Tabs>
