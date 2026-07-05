--- 
title: authentication_events_flows_conditions_applications_include_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_events_flows_conditions_applications_include_applications
  - identity
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

Creates, updates, deletes, gets or lists an <code>authentication_events_flows_conditions_applications_include_applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_events_flows_conditions_applications_include_applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.authentication_events_flows_conditions_applications_include_applications" /></td></tr>
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
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The identifier for an application corresponding to a condition which will trigger an authenticationEventListener.</td>
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
    <td><CopyableCode code="appId" /></td>
    <td><code>string</code></td>
    <td>The identifier for an application corresponding to a condition which will trigger an authenticationEventListener.</td>
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
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a>, <a href="#parameter-authentication_condition_application_app_id"><code>authentication_condition_application_app_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a></td>
    <td></td>
    <td>List the applications linked to an external identities self-service sign up user flow that's represented by an externalUsersSelfServiceSignupEventsFlow object. These are the applications for which the authentication experience that's defined by the user flow is enabled. To find the user flow that's linked to an application, see Example 4: List user flow associated with specific application ID.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a></td>
    <td></td>
    <td>Add or link an application to a user flow, or authenticationEventsFlow. This enables the authentication experience defined by the user flow to be enabled for the application. An application can only be linked to one user flow. The app must have an associated service principal in the tenant.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a>, <a href="#parameter-authentication_condition_application_app_id"><code>authentication_condition_application_app_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a>, <a href="#parameter-authentication_condition_application_app_id"><code>authentication_condition_application_app_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove or unlink an application from an authenticationEventsFlow object. This disables the customized authentication experience defined for the application.</td>
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
<tr id="parameter-authentication_condition_application_app_id">
    <td><CopyableCode code="authentication_condition_application_app_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of authenticationConditionApplication</td>
</tr>
<tr id="parameter-authentication_events_flow_id">
    <td><CopyableCode code="authentication_events_flow_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of authenticationEventsFlow</td>
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
appId
FROM entra_id.identity.authentication_events_flows_conditions_applications_include_applications
WHERE authentication_events_flow_id = '{{ authentication_events_flow_id }}' -- required
AND authentication_condition_application_app_id = '{{ authentication_condition_application_app_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the applications linked to an external identities self-service sign up user flow that's represented by an externalUsersSelfServiceSignupEventsFlow object. These are the applications for which the authentication experience that's defined by the user flow is enabled. To find the user flow that's linked to an application, see Example 4: List user flow associated with specific application ID.

```sql
SELECT
appId
FROM entra_id.identity.authentication_events_flows_conditions_applications_include_applications
WHERE authentication_events_flow_id = '{{ authentication_events_flow_id }}' -- required
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

Add or link an application to a user flow, or authenticationEventsFlow. This enables the authentication experience defined by the user flow to be enabled for the application. An application can only be linked to one user flow. The app must have an associated service principal in the tenant.

```sql
INSERT INTO entra_id.identity.authentication_events_flows_conditions_applications_include_applications (
appId,
authentication_events_flow_id
)
SELECT 
'{{ appId }}',
'{{ authentication_events_flow_id }}'
RETURNING
appId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: authentication_events_flows_conditions_applications_include_applications
  props:
    - name: authentication_events_flow_id
      value: "{{ authentication_events_flow_id }}"
      description: Required parameter for the authentication_events_flows_conditions_applications_include_applications resource.
    - name: appId
      value: "{{ appId }}"
      description: |
        The identifier for an application corresponding to a condition which will trigger an authenticationEventListener.
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
UPDATE entra_id.identity.authentication_events_flows_conditions_applications_include_applications
SET 
appId = '{{ appId }}',
WHERE 
authentication_events_flow_id = '{{ authentication_events_flow_id }}' --required
AND authentication_condition_application_app_id = '{{ authentication_condition_application_app_id }}' --required
RETURNING
appId;
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

Remove or unlink an application from an authenticationEventsFlow object. This disables the customized authentication experience defined for the application.

```sql
DELETE FROM entra_id.identity.authentication_events_flows_conditions_applications_include_applications
WHERE authentication_events_flow_id = '{{ authentication_events_flow_id }}' --required
AND authentication_condition_application_app_id = '{{ authentication_condition_application_app_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
