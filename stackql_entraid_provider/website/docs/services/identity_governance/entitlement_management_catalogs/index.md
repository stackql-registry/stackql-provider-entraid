--- 
title: entitlement_management_catalogs
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_catalogs
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_catalogs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_catalogs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_catalogs" /></td></tr>
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
    <td><CopyableCode code="accessPackages" /></td>
    <td><code>array</code></td>
    <td>The access packages in this catalog. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="catalogType" /></td>
    <td><code></code></td>
    <td>Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customWorkflowExtensions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the access package catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the access package catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="isExternallyVisible" /></td>
    <td><code>boolean</code></td>
    <td>Whether the access packages in this catalog can be requested by users outside of the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRoles" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resourceScopes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>Access package resources in this catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.</td>
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
    <td><CopyableCode code="accessPackages" /></td>
    <td><code>array</code></td>
    <td>The access packages in this catalog. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="catalogType" /></td>
    <td><code></code></td>
    <td>Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customWorkflowExtensions" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the access package catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the access package catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="isExternallyVisible" /></td>
    <td><code>boolean</code></td>
    <td>Whether the access packages in this catalog can be requested by users outside of the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRoles" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resourceScopes" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="resources" /></td>
    <td><code>array</code></td>
    <td>Access package resources in this catalog.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code></code></td>
    <td>Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.</td>
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
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a></td>
    <td></td>
    <td>Retrieve the properties and relationships of an accessPackageCatalog object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of accessPackageCatalog objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new accessPackageCatalog object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a></td>
    <td></td>
    <td>Update an existing accessPackageCatalog object to change one or more of its properties, such as the display name or description.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_catalog_id"><code>access_package_catalog_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an accessPackageCatalog.</td>
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

Retrieve the properties and relationships of an accessPackageCatalog object.

```sql
SELECT
id,
accessPackages,
catalogType,
createdDateTime,
customWorkflowExtensions,
description,
displayName,
isExternallyVisible,
modifiedDateTime,
resourceRoles,
resourceScopes,
resources,
state
FROM entra_id.identity_governance.entitlement_management_catalogs
WHERE access_package_catalog_id = '{{ access_package_catalog_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of accessPackageCatalog objects.

```sql
SELECT
id,
accessPackages,
catalogType,
createdDateTime,
customWorkflowExtensions,
description,
displayName,
isExternallyVisible,
modifiedDateTime,
resourceRoles,
resourceScopes,
resources,
state
FROM entra_id.identity_governance.entitlement_management_catalogs
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

Create a new accessPackageCatalog object.

```sql
INSERT INTO entra_id.identity_governance.entitlement_management_catalogs (
id,
catalogType,
createdDateTime,
description,
displayName,
isExternallyVisible,
modifiedDateTime,
state,
accessPackages,
customWorkflowExtensions,
resourceRoles,
resources,
resourceScopes
)
SELECT 
'{{ id }}',
'{{ catalogType }}',
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
{{ isExternallyVisible }},
'{{ modifiedDateTime }}',
'{{ state }}',
'{{ accessPackages }}',
'{{ customWorkflowExtensions }}',
'{{ resourceRoles }}',
'{{ resources }}',
'{{ resourceScopes }}'
RETURNING
id,
accessPackages,
catalogType,
createdDateTime,
customWorkflowExtensions,
description,
displayName,
isExternallyVisible,
modifiedDateTime,
resourceRoles,
resourceScopes,
resources,
state
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_catalogs
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: catalogType
      value: "{{ catalogType }}"
      description: |
        Whether the catalog is created by a user or entitlement management. The possible values are: userManaged, serviceDefault, serviceManaged, unknownFutureValue.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the access package catalog.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the access package catalog.
    - name: isExternallyVisible
      value: {{ isExternallyVisible }}
      description: |
        Whether the access packages in this catalog can be requested by users outside of the tenant.
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: state
      value: "{{ state }}"
      description: |
        Has the value published if the access packages are available for management. The possible values are: unpublished, published, unknownFutureValue.
    - name: accessPackages
      description: |
        The access packages in this catalog. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          isHidden: {{ isHidden }}
          modifiedDateTime: "{{ modifiedDateTime }}"
          accessPackagesIncompatibleWith: "{{ accessPackagesIncompatibleWith }}"
          assignmentPolicies: "{{ assignmentPolicies }}"
          catalog: "{{ catalog }}"
          incompatibleAccessPackages: "{{ incompatibleAccessPackages }}"
          incompatibleGroups: "{{ incompatibleGroups }}"
          resourceRoleScopes: "{{ resourceRoleScopes }}"
    - name: customWorkflowExtensions
      value:
        - id: "{{ id }}"
          authenticationConfiguration: "{{ authenticationConfiguration }}"
          clientConfiguration: "{{ clientConfiguration }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          endpointConfiguration: "{{ endpointConfiguration }}"
    - name: resourceRoles
      value:
        - id: "{{ id }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          originId: "{{ originId }}"
          originSystem: "{{ originSystem }}"
          resource: "{{ resource }}"
    - name: resources
      description: |
        Access package resources in this catalog.
      value:
        - id: "{{ id }}"
          attributes: "{{ attributes }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          modifiedDateTime: "{{ modifiedDateTime }}"
          originId: "{{ originId }}"
          originSystem: "{{ originSystem }}"
          environment: "{{ environment }}"
          roles: "{{ roles }}"
          scopes: "{{ scopes }}"
    - name: resourceScopes
      value:
        - id: "{{ id }}"
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

Update an existing accessPackageCatalog object to change one or more of its properties, such as the display name or description.

```sql
UPDATE entra_id.identity_governance.entitlement_management_catalogs
SET 
id = '{{ id }}',
catalogType = '{{ catalogType }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isExternallyVisible = {{ isExternallyVisible }},
modifiedDateTime = '{{ modifiedDateTime }}',
state = '{{ state }}',
accessPackages = '{{ accessPackages }}',
customWorkflowExtensions = '{{ customWorkflowExtensions }}',
resourceRoles = '{{ resourceRoles }}',
resources = '{{ resources }}',
resourceScopes = '{{ resourceScopes }}'
WHERE 
access_package_catalog_id = '{{ access_package_catalog_id }}' --required
RETURNING
id,
accessPackages,
catalogType,
createdDateTime,
customWorkflowExtensions,
description,
displayName,
isExternallyVisible,
modifiedDateTime,
resourceRoles,
resourceScopes,
resources,
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

Delete an accessPackageCatalog.

```sql
DELETE FROM entra_id.identity_governance.entitlement_management_catalogs
WHERE access_package_catalog_id = '{{ access_package_catalog_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
