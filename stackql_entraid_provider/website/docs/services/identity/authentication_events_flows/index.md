--- 
title: authentication_events_flows
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_events_flows
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

Creates, updates, deletes, gets or lists an <code>authentication_events_flows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_events_flows" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.authentication_events_flows" /></td></tr>
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
    <td><CopyableCode code="conditions" /></td>
    <td><code></code></td>
    <td>The conditions representing the context of the authentication request that's used to decide whether the events policy is invoked.  Supports $filter (eq). See support for filtering on user flows for syntax information.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the events policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Required. The display name for the events policy.</td>
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
    <td><CopyableCode code="conditions" /></td>
    <td><code></code></td>
    <td>The conditions representing the context of the authentication request that's used to decide whether the events policy is invoked.  Supports $filter (eq). See support for filtering on user flows for syntax information.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the events policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Required. The display name for the events policy.</td>
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
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a></td>
    <td></td>
    <td>Retrieve the properties and relationships of a specific authenticationEventsFlow object by ID. The @odata.type property in the response object indicates the type of the object, which can be one of the following derived subtypes:<br />- externalUsersSelfServiceSignupEventsFlow</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a collection of authentication events policies that are derived from authenticationEventsFlow. The following derived subtypes are supported: <br />- externalUsersSelfServiceSignupEventsFlow</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new authenticationEventsFlow object that is of the type specified in the request body. The following derived subtypes are supported:<br />- externalUsersSelfServiceSignupEventsFlow object type.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a></td>
    <td></td>
    <td>Update the properties of an authenticationEventsFlow object by ID. You must specify the @odata.type property and the value of the authenticationEventsFlow object type to update. The following derived subtypes are supported:<br />- externalUsersSelfServiceSignupEventsFlow</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-authentication_events_flow_id"><code>authentication_events_flow_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a specific authenticationEventsFlow resource by ID. This operation also removes or unlinks all applications from the flow, which disables the customized authentication experience defined for the application.  The following derived subtypes are supported:<br />- externalUsersSelfServiceSignupEventsFlow</td>
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

Retrieve the properties and relationships of a specific authenticationEventsFlow object by ID. The @odata.type property in the response object indicates the type of the object, which can be one of the following derived subtypes:<br />- externalUsersSelfServiceSignupEventsFlow

```sql
SELECT
id,
conditions,
description,
displayName
FROM entra_id.identity.authentication_events_flows
WHERE authentication_events_flow_id = '{{ authentication_events_flow_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a collection of authentication events policies that are derived from authenticationEventsFlow. The following derived subtypes are supported: <br />- externalUsersSelfServiceSignupEventsFlow

```sql
SELECT
id,
conditions,
description,
displayName
FROM entra_id.identity.authentication_events_flows
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

Create a new authenticationEventsFlow object that is of the type specified in the request body. The following derived subtypes are supported:<br />- externalUsersSelfServiceSignupEventsFlow object type.

```sql
INSERT INTO entra_id.identity.authentication_events_flows (
id,
conditions,
description,
displayName
)
SELECT 
'{{ id }}',
'{{ conditions }}',
'{{ description }}',
'{{ displayName }}'
RETURNING
id,
conditions,
description,
displayName
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: authentication_events_flows
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: conditions
      value: "{{ conditions }}"
      description: |
        The conditions representing the context of the authentication request that's used to decide whether the events policy is invoked.  Supports $filter (eq). See support for filtering on user flows for syntax information.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the events policy.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Required. The display name for the events policy.
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

Update the properties of an authenticationEventsFlow object by ID. You must specify the @odata.type property and the value of the authenticationEventsFlow object type to update. The following derived subtypes are supported:<br />- externalUsersSelfServiceSignupEventsFlow

```sql
UPDATE entra_id.identity.authentication_events_flows
SET 
id = '{{ id }}',
conditions = '{{ conditions }}',
description = '{{ description }}',
displayName = '{{ displayName }}'
WHERE 
authentication_events_flow_id = '{{ authentication_events_flow_id }}' --required
RETURNING
id,
conditions,
description,
displayName;
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

Delete a specific authenticationEventsFlow resource by ID. This operation also removes or unlinks all applications from the flow, which disables the customized authentication experience defined for the application.  The following derived subtypes are supported:<br />- externalUsersSelfServiceSignupEventsFlow

```sql
DELETE FROM entra_id.identity.authentication_events_flows
WHERE authentication_events_flow_id = '{{ authentication_events_flow_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
