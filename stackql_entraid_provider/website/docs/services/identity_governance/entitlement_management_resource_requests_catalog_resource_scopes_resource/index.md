--- 
title: entitlement_management_resource_requests_catalog_resource_scopes_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_resource_requests_catalog_resource_scopes_resource
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_resource_requests_catalog_resource_scopes_resource</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_resource_requests_catalog_resource_scopes_resource" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_resource_requests_catalog_resource_scopes_resource" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="attributes" /></td>
    <td><code>array</code></td>
    <td>Contains information about the attributes to be collected from the requestor and sent to the resource application.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the resource, such as the application name, group name or site name.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code></code></td>
    <td>Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="originId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of the resource in the origin system. For a Microsoft Entra group, this is the identifier of the group.</td>
</tr>
<tr>
    <td><CopyableCode code="originSystem" /></td>
    <td><code>string</code></td>
    <td>The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="roles" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="scopes" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand.</td>
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
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#refresh"><CopyableCode code="refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-access_package_resource_request_id"><code>access_package_resource_request_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
    <td></td>
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
<tr id="parameter-access_package_resource_scope_id">
    <td><CopyableCode code="access_package_resource_scope_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceScope</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Retrieved navigation property

```sql
SELECT
id,
attributes,
createdDateTime,
description,
displayName,
environment,
modifiedDateTime,
originId,
originSystem,
roles,
scopes
FROM entra_id.identity_governance.entitlement_management_resource_requests_catalog_resource_scopes_resource
WHERE access_package_resource_request_id = '{{ access_package_resource_request_id }}' -- required
AND access_package_resource_scope_id = '{{ access_package_resource_scope_id }}' -- required
;
```
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
UPDATE entra_id.identity_governance.entitlement_management_resource_requests_catalog_resource_scopes_resource
SET 
id = '{{ id }}',
attributes = '{{ attributes }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
modifiedDateTime = '{{ modifiedDateTime }}',
originId = '{{ originId }}',
originSystem = '{{ originSystem }}',
environment = '{{ environment }}',
roles = '{{ roles }}',
scopes = '{{ scopes }}'
WHERE 
access_package_resource_request_id = '{{ access_package_resource_request_id }}' --required
AND access_package_resource_scope_id = '{{ access_package_resource_scope_id }}' --required
RETURNING
id,
attributes,
createdDateTime,
description,
displayName,
environment,
modifiedDateTime,
originId,
originSystem,
roles,
scopes;
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
DELETE FROM entra_id.identity_governance.entitlement_management_resource_requests_catalog_resource_scopes_resource
WHERE access_package_resource_request_id = '{{ access_package_resource_request_id }}' --required
AND access_package_resource_scope_id = '{{ access_package_resource_scope_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh"
    values={[
        { label: 'refresh', value: 'refresh' }
    ]}
>
<TabItem value="refresh">

Success

```sql
EXEC entra_id.identity_governance.entitlement_management_resource_requests_catalog_resource_scopes_resource.refresh 
@access_package_resource_request_id='{{ access_package_resource_request_id }}' --required, 
@access_package_resource_scope_id='{{ access_package_resource_scope_id }}' --required
;
```
</TabItem>
</Tabs>
