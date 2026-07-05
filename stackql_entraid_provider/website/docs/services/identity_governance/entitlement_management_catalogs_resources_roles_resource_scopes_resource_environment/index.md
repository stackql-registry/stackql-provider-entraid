--- 
title: entitlement_management_catalogs_resources_roles_resource_scopes_resource_environment
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_catalogs_resources_roles_resource_scopes_resource_environment
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_catalogs_resources_roles_resource_scopes_resource_environment</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_catalogs_resources_roles_resource_scopes_resource_environment" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_catalogs_resources_roles_resource_scopes_resource_environment" /></td></tr>
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
    <td><CopyableCode code="connectionInfo" /></td>
    <td><code></code></td>
    <td>Connection information of an environment used to connect to a resource.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that this object was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of this object.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of this object.</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultEnvironment" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether this is default environment or not. It is set to true for all static origin systems, such as Microsoft Entra groups and Microsoft Entra Applications.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time that this object was last modified. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="originId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of this environment in the origin system.</td>
</tr>
<tr>
    <td><CopyableCode code="originSystem" /></td>
    <td><code>string</code></td>
    <td>The type of the resource in the origin system, that is, SharePointOnline. Requires $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>Read-only. Required.</td>
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
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a>, <a href="#parameter-access_package_resource_id"><code>access_package_resource_id</code></a>, <a href="#parameter-access_package_resource_role_id"><code>access_package_resource_role_id</code></a>, <a href="#parameter-access_package_resource_scope_id"><code>access_package_resource_scope_id</code></a></td>
    <td></td>
    <td>Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.</td>
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
<tr id="parameter-access_package_catalog_id">
    <td><CopyableCode code="access_package_catalog_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageCatalog</td>
</tr>
<tr id="parameter-access_package_resource_id">
    <td><CopyableCode code="access_package_resource_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResource</td>
</tr>
<tr id="parameter-access_package_resource_role_id">
    <td><CopyableCode code="access_package_resource_role_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceRole</td>
</tr>
<tr id="parameter-access_package_resource_scope_id">
    <td><CopyableCode code="access_package_resource_scope_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResourceScope</td>
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

Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.

```sql
SELECT
id,
connectionInfo,
createdDateTime,
description,
displayName,
isDefaultEnvironment,
modifiedDateTime,
originId,
originSystem,
resources
FROM entra_id.identity_governance.entitlement_management_catalogs_resources_roles_resource_scopes_resource_environment
WHERE access_package_catalog_id = '{{ access_package_catalog_id }}' -- required
AND access_package_resource_id = '{{ access_package_resource_id }}' -- required
AND access_package_resource_role_id = '{{ access_package_resource_role_id }}' -- required
AND access_package_resource_scope_id = '{{ access_package_resource_scope_id }}' -- required
;
```
</TabItem>
</Tabs>
