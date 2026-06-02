--- 
title: entitlement_management_catalogs_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_catalogs_resources
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_catalogs_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_catalogs_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_catalogs_resources" /></td></tr>
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
    <td><a href="#parameter-accessPackageCatalog-id"><code>accessPackageCatalog-id</code></a>, <a href="#parameter-accessPackageResource-id"><code>accessPackageResource-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Access package resources in this catalog.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-accessPackageCatalog-id"><code>accessPackageCatalog-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of accessPackageResource objects in an accessPackageCatalog.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-accessPackageCatalog-id"><code>accessPackageCatalog-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessPackageCatalog-id"><code>accessPackageCatalog-id</code></a>, <a href="#parameter-accessPackageResource-id"><code>accessPackageResource-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessPackageCatalog-id"><code>accessPackageCatalog-id</code></a>, <a href="#parameter-accessPackageResource-id"><code>accessPackageResource-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#refresh"><CopyableCode code="refresh" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessPackageCatalog-id"><code>accessPackageCatalog-id</code></a>, <a href="#parameter-accessPackageResource-id"><code>accessPackageResource-id</code></a></td>
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
<tr id="parameter-accessPackageCatalog-id">
    <td><CopyableCode code="accessPackageCatalog-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageCatalog</td>
</tr>
<tr id="parameter-accessPackageResource-id">
    <td><CopyableCode code="accessPackageResource-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageResource</td>
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

Access package resources in this catalog.

```sql
SELECT
id,
@odata.type,
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
FROM entra_id.identity_governance.entitlement_management_catalogs_resources
WHERE accessPackageCatalog-id = '{{ accessPackageCatalog-id }}' -- required
AND accessPackageResource-id = '{{ accessPackageResource-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of accessPackageResource objects in an accessPackageCatalog.

```sql
SELECT
id,
@odata.type,
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
FROM entra_id.identity_governance.entitlement_management_catalogs_resources
WHERE accessPackageCatalog-id = '{{ accessPackageCatalog-id }}' -- required
AND $top = '{{ $top }}'
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
INSERT INTO entra_id.identity_governance.entitlement_management_catalogs_resources (
id,
@odata.type,
attributes,
createdDateTime,
description,
displayName,
modifiedDateTime,
originId,
originSystem,
environment,
roles,
scopes,
accessPackageCatalog-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ attributes }}',
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ modifiedDateTime }}',
'{{ originId }}',
'{{ originSystem }}',
'{{ environment }}',
'{{ roles }}',
'{{ scopes }}',
'{{ accessPackageCatalog-id }}'
RETURNING
id,
@odata.type,
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
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_catalogs_resources
  props:
    - name: accessPackageCatalog-id
      value: "{{ accessPackageCatalog-id }}"
      description: Required parameter for the entitlement_management_catalogs_resources resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: attributes
      description: |
        Contains information about the attributes to be collected from the requestor and sent to the resource application.
      value:
        - destination:
            @odata.type: "{{ @odata.type }}"
          isEditable: {{ isEditable }}
          isPersistedOnAssignmentRemoval: {{ isPersistedOnAssignmentRemoval }}
          name: "{{ name }}"
          source:
            @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        A description for the resource.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the resource, such as the application name, group name or site name.
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: originId
      value: "{{ originId }}"
      description: |
        The unique identifier of the resource in the origin system. For a Microsoft Entra group, this is the identifier of the group.
    - name: originSystem
      value: "{{ originSystem }}"
      description: |
        The type of the resource in the origin system, such as SharePointOnline, AadApplication or AadGroup.
    - name: environment
      value: "{{ environment }}"
      description: |
        Contains the environment information for the resource. This can be set using either the @odata.bind annotation or the environment's originId.Supports $expand.
    - name: roles
      description: |
        Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          originId: "{{ originId }}"
          originSystem: "{{ originSystem }}"
          resource: "{{ resource }}"
    - name: scopes
      description: |
        Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          isRootScope: {{ isRootScope }}
          originId: "{{ originId }}"
          originSystem: "{{ originSystem }}"
          resource: "{{ resource }}"
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
UPDATE entra_id.identity_governance.entitlement_management_catalogs_resources
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
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
accessPackageCatalog-id = '{{ accessPackageCatalog-id }}' --required
AND accessPackageResource-id = '{{ accessPackageResource-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
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
DELETE FROM entra_id.identity_governance.entitlement_management_catalogs_resources
WHERE accessPackageCatalog-id = '{{ accessPackageCatalog-id }}' --required
AND accessPackageResource-id = '{{ accessPackageResource-id }}' --required
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
EXEC entra_id.identity_governance.entitlement_management_catalogs_resources.refresh 
@accessPackageCatalog-id='{{ accessPackageCatalog-id }}' --required, 
@accessPackageResource-id='{{ accessPackageResource-id }}' --required
;
```
</TabItem>
</Tabs>
