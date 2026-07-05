--- 
title: entitlement_management_resource_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_resource_requests
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_resource_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_resource_requests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_resource_requests" /></td></tr>
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
    <td><CopyableCode code="catalog" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="requestType" /></td>
    <td><code></code></td>
    <td>The type of the request. Use adminAdd to add a resource, if the caller is an administrator or resource owner, adminUpdate to update a resource, or adminRemove to remove a resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The outcome of whether the service was able to add the resource to the catalog. The value is delivered if the resource was added or removed, and deliveryFailed if it couldn't be added or removed. Read-only.</td>
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
    <td><CopyableCode code="catalog" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="requestType" /></td>
    <td><code></code></td>
    <td>The type of the request. Use adminAdd to add a resource, if the caller is an administrator or resource owner, adminUpdate to update a resource, or adminRemove to remove a resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resource" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>The outcome of whether the service was able to add the resource to the catalog. The value is delivered if the resource was added or removed, and deliveryFailed if it couldn't be added or removed. Read-only.</td>
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
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a></td>
    <td></td>
    <td>Represents a request to add or remove a resource to or from a catalog respectively.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of accessPackageResourceRequest objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new accessPackageResourceRequest object to request the addition of a resource to an access package catalog, update of a resource, or the removal of a resource from a catalog.  A resource must be included in an access package catalog before a role of that resource can be added to an access package.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a></td>
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
<tr id="parameter-access_package_resource_request_id">
    <td><CopyableCode code="access_package_resource_request_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceRequest</td>
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

Represents a request to add or remove a resource to or from a catalog respectively.

```sql
SELECT
id,
catalog,
createdDateTime,
requestType,
resource,
state
FROM entra_id.identity_governance.entitlement_management_resource_requests
WHERE access_package_resource_request_id = '{{ access_package_resource_request_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of accessPackageResourceRequest objects.

```sql
SELECT
id,
catalog,
createdDateTime,
requestType,
resource,
state
FROM entra_id.identity_governance.entitlement_management_resource_requests
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

Create a new accessPackageResourceRequest object to request the addition of a resource to an access package catalog, update of a resource, or the removal of a resource from a catalog.  A resource must be included in an access package catalog before a role of that resource can be added to an access package.

```sql
INSERT INTO entra_id.identity_governance.entitlement_management_resource_requests (
id,
createdDateTime,
requestType,
state,
catalog,
resource
)
SELECT 
'{{ id }}',
'{{ createdDateTime }}',
'{{ requestType }}',
'{{ state }}',
'{{ catalog }}',
'{{ resource }}'
RETURNING
id,
catalog,
createdDateTime,
requestType,
resource,
state
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_resource_requests
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: requestType
      value: "{{ requestType }}"
      description: |
        The type of the request. Use adminAdd to add a resource, if the caller is an administrator or resource owner, adminUpdate to update a resource, or adminRemove to remove a resource.
    - name: state
      value: "{{ state }}"
      description: |
        The outcome of whether the service was able to add the resource to the catalog. The value is delivered if the resource was added or removed, and deliveryFailed if it couldn't be added or removed. Read-only.
    - name: catalog
      value: "{{ catalog }}"
    - name: resource
      value: "{{ resource }}"
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
UPDATE entra_id.identity_governance.entitlement_management_resource_requests
SET 
id = '{{ id }}',
createdDateTime = '{{ createdDateTime }}',
requestType = '{{ requestType }}',
state = '{{ state }}',
catalog = '{{ catalog }}',
resource = '{{ resource }}'
WHERE 
access_package_resource_request_id = '{{ access_package_resource_request_id }}' --required
RETURNING
id,
catalog,
createdDateTime,
requestType,
resource,
state;
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
DELETE FROM entra_id.identity_governance.entitlement_management_resource_requests
WHERE access_package_resource_request_id = '{{ access_package_resource_request_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
