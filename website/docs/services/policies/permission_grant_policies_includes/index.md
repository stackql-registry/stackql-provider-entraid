--- 
title: permission_grant_policies_includes
hide_title: false
hide_table_of_contents: false
keywords:
  - permission_grant_policies_includes
  - policies
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

Creates, updates, deletes, gets or lists a <code>permission_grant_policies_includes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="permission_grant_policies_includes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.permission_grant_policies_includes" /></td></tr>
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
    <td><CopyableCode code="clientApplicationIds" /></td>
    <td><code>array</code></td>
    <td>A list of appId values for the client applications to match with, or a list with the single value all to match any client application. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="clientApplicationPublisherIds" /></td>
    <td><code>array</code></td>
    <td>A list of Microsoft Partner Network (MPN) IDs for verified publishers of the client application, or a list with the single value all to match with client apps from any publisher. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="clientApplicationTenantIds" /></td>
    <td><code>array</code></td>
    <td>A list of Microsoft Entra tenant IDs in which the client application is registered, or a list with the single value all to match with client apps registered in any tenant. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="clientApplicationsFromVerifiedPublisherOnly" /></td>
    <td><code>boolean</code></td>
    <td>Set to true to only match on client applications with a verified publisher. Set to false to match on any client app, even if it doesn't have a verified publisher. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionClassification" /></td>
    <td><code>string</code></td>
    <td>The permission classification for the permission being granted, or all to match with any permission classification (including permissions that aren't classified). Default is all.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionType" /></td>
    <td><code></code></td>
    <td>The permission type of the permission being granted. Possible values: application for application permissions (for example app roles), or delegated for delegated permissions. The value delegatedUserConsentable indicates delegated permissions that haven't been configured by the API publisher to require admin consent—this value may be used in built-in permission grant policies, but can't be used in custom permission grant policies. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>The list of id values for the specific permissions to match with, or a list with the single value all to match with any permission. The id of delegated permissions can be found in the oauth2PermissionScopes property of the API's servicePrincipal object. The id of application permissions can be found in the appRoles property of the API's servicePrincipal object. The id of resource-specific application permissions can be found in the resourceSpecificApplicationPermissions property of the API's servicePrincipal object. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceApplication" /></td>
    <td><code>string</code></td>
    <td>The appId of the resource application (for example the API) for which a permission is being granted, or any to match with any resource application or API. Default is any.</td>
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
    <td><CopyableCode code="clientApplicationIds" /></td>
    <td><code>array</code></td>
    <td>A list of appId values for the client applications to match with, or a list with the single value all to match any client application. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="clientApplicationPublisherIds" /></td>
    <td><code>array</code></td>
    <td>A list of Microsoft Partner Network (MPN) IDs for verified publishers of the client application, or a list with the single value all to match with client apps from any publisher. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="clientApplicationTenantIds" /></td>
    <td><code>array</code></td>
    <td>A list of Microsoft Entra tenant IDs in which the client application is registered, or a list with the single value all to match with client apps registered in any tenant. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="clientApplicationsFromVerifiedPublisherOnly" /></td>
    <td><code>boolean</code></td>
    <td>Set to true to only match on client applications with a verified publisher. Set to false to match on any client app, even if it doesn't have a verified publisher. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionClassification" /></td>
    <td><code>string</code></td>
    <td>The permission classification for the permission being granted, or all to match with any permission classification (including permissions that aren't classified). Default is all.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionType" /></td>
    <td><code></code></td>
    <td>The permission type of the permission being granted. Possible values: application for application permissions (for example app roles), or delegated for delegated permissions. The value delegatedUserConsentable indicates delegated permissions that haven't been configured by the API publisher to require admin consent—this value may be used in built-in permission grant policies, but can't be used in custom permission grant policies. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>array</code></td>
    <td>The list of id values for the specific permissions to match with, or a list with the single value all to match with any permission. The id of delegated permissions can be found in the oauth2PermissionScopes property of the API's servicePrincipal object. The id of application permissions can be found in the appRoles property of the API's servicePrincipal object. The id of resource-specific application permissions can be found in the resourceSpecificApplicationPermissions property of the API's servicePrincipal object. Default is the single value all.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceApplication" /></td>
    <td><code>string</code></td>
    <td>The appId of the resource application (for example the API) for which a permission is being granted, or any to match with any resource application or API. Default is any.</td>
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
    <td><a href="#parameter-permissionGrantPolicy-id"><code>permissionGrantPolicy-id</code></a>, <a href="#parameter-permissionGrantConditionSet-id"><code>permissionGrantConditionSet-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Condition sets that are included in this permission grant policy. Automatically expanded on GET.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-permissionGrantPolicy-id"><code>permissionGrantPolicy-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the condition sets which are *included* in a permissionGrantPolicy.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-permissionGrantPolicy-id"><code>permissionGrantPolicy-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Add conditions under which a permission grant event is *included* in a permission grant policy. You do this by adding a permissionGrantConditionSet to the includes collection of a  permissionGrantPolicy.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-permissionGrantPolicy-id"><code>permissionGrantPolicy-id</code></a>, <a href="#parameter-permissionGrantConditionSet-id"><code>permissionGrantConditionSet-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-permissionGrantPolicy-id"><code>permissionGrantPolicy-id</code></a>, <a href="#parameter-permissionGrantConditionSet-id"><code>permissionGrantConditionSet-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Deletes a permissionGrantConditionSet from the includes collection of a permissionGrantPolicy.</td>
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
<tr id="parameter-permissionGrantConditionSet-id">
    <td><CopyableCode code="permissionGrantConditionSet-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of permissionGrantConditionSet</td>
</tr>
<tr id="parameter-permissionGrantPolicy-id">
    <td><CopyableCode code="permissionGrantPolicy-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of permissionGrantPolicy</td>
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

Condition sets that are included in this permission grant policy. Automatically expanded on GET.

```sql
SELECT
id,
@odata.type,
clientApplicationIds,
clientApplicationPublisherIds,
clientApplicationTenantIds,
clientApplicationsFromVerifiedPublisherOnly,
permissionClassification,
permissionType,
permissions,
resourceApplication
FROM entra_id.policies.permission_grant_policies_includes
WHERE permissionGrantPolicy-id = '{{ permissionGrantPolicy-id }}' -- required
AND permissionGrantConditionSet-id = '{{ permissionGrantConditionSet-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve the condition sets which are *included* in a permissionGrantPolicy.

```sql
SELECT
id,
@odata.type,
clientApplicationIds,
clientApplicationPublisherIds,
clientApplicationTenantIds,
clientApplicationsFromVerifiedPublisherOnly,
permissionClassification,
permissionType,
permissions,
resourceApplication
FROM entra_id.policies.permission_grant_policies_includes
WHERE permissionGrantPolicy-id = '{{ permissionGrantPolicy-id }}' -- required
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

Add conditions under which a permission grant event is *included* in a permission grant policy. You do this by adding a permissionGrantConditionSet to the includes collection of a  permissionGrantPolicy.

```sql
INSERT INTO entra_id.policies.permission_grant_policies_includes (
id,
@odata.type,
clientApplicationIds,
clientApplicationPublisherIds,
clientApplicationsFromVerifiedPublisherOnly,
clientApplicationTenantIds,
permissionClassification,
permissions,
permissionType,
resourceApplication,
permissionGrantPolicy-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ clientApplicationIds }}',
'{{ clientApplicationPublisherIds }}',
{{ clientApplicationsFromVerifiedPublisherOnly }},
'{{ clientApplicationTenantIds }}',
'{{ permissionClassification }}',
'{{ permissions }}',
'{{ permissionType }}',
'{{ resourceApplication }}',
'{{ permissionGrantPolicy-id }}'
RETURNING
id,
@odata.type,
clientApplicationIds,
clientApplicationPublisherIds,
clientApplicationTenantIds,
clientApplicationsFromVerifiedPublisherOnly,
permissionClassification,
permissionType,
permissions,
resourceApplication
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: permission_grant_policies_includes
  props:
    - name: permissionGrantPolicy-id
      value: "{{ permissionGrantPolicy-id }}"
      description: Required parameter for the permission_grant_policies_includes resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: clientApplicationIds
      value:
        - "{{ clientApplicationIds }}"
      description: |
        A list of appId values for the client applications to match with, or a list with the single value all to match any client application. Default is the single value all.
    - name: clientApplicationPublisherIds
      value:
        - "{{ clientApplicationPublisherIds }}"
      description: |
        A list of Microsoft Partner Network (MPN) IDs for verified publishers of the client application, or a list with the single value all to match with client apps from any publisher. Default is the single value all.
    - name: clientApplicationsFromVerifiedPublisherOnly
      value: {{ clientApplicationsFromVerifiedPublisherOnly }}
      description: |
        Set to true to only match on client applications with a verified publisher. Set to false to match on any client app, even if it doesn't have a verified publisher. Default is false.
    - name: clientApplicationTenantIds
      value:
        - "{{ clientApplicationTenantIds }}"
      description: |
        A list of Microsoft Entra tenant IDs in which the client application is registered, or a list with the single value all to match with client apps registered in any tenant. Default is the single value all.
    - name: permissionClassification
      value: "{{ permissionClassification }}"
      description: |
        The permission classification for the permission being granted, or all to match with any permission classification (including permissions that aren't classified). Default is all.
    - name: permissions
      value:
        - "{{ permissions }}"
      description: |
        The list of id values for the specific permissions to match with, or a list with the single value all to match with any permission. The id of delegated permissions can be found in the oauth2PermissionScopes property of the API's servicePrincipal object. The id of application permissions can be found in the appRoles property of the API's servicePrincipal object. The id of resource-specific application permissions can be found in the resourceSpecificApplicationPermissions property of the API's servicePrincipal object. Default is the single value all.
    - name: permissionType
      value: "{{ permissionType }}"
      description: |
        The permission type of the permission being granted. Possible values: application for application permissions (for example app roles), or delegated for delegated permissions. The value delegatedUserConsentable indicates delegated permissions that haven't been configured by the API publisher to require admin consent—this value may be used in built-in permission grant policies, but can't be used in custom permission grant policies. Required.
    - name: resourceApplication
      value: "{{ resourceApplication }}"
      description: |
        The appId of the resource application (for example the API) for which a permission is being granted, or any to match with any resource application or API. Default is any.
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
UPDATE entra_id.policies.permission_grant_policies_includes
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
clientApplicationIds = '{{ clientApplicationIds }}',
clientApplicationPublisherIds = '{{ clientApplicationPublisherIds }}',
clientApplicationsFromVerifiedPublisherOnly = {{ clientApplicationsFromVerifiedPublisherOnly }},
clientApplicationTenantIds = '{{ clientApplicationTenantIds }}',
permissionClassification = '{{ permissionClassification }}',
permissions = '{{ permissions }}',
permissionType = '{{ permissionType }}',
resourceApplication = '{{ resourceApplication }}'
WHERE 
permissionGrantPolicy-id = '{{ permissionGrantPolicy-id }}' --required
AND permissionGrantConditionSet-id = '{{ permissionGrantConditionSet-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
clientApplicationIds,
clientApplicationPublisherIds,
clientApplicationTenantIds,
clientApplicationsFromVerifiedPublisherOnly,
permissionClassification,
permissionType,
permissions,
resourceApplication;
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

Deletes a permissionGrantConditionSet from the includes collection of a permissionGrantPolicy.

```sql
DELETE FROM entra_id.policies.permission_grant_policies_includes
WHERE permissionGrantPolicy-id = '{{ permissionGrantPolicy-id }}' --required
AND permissionGrantConditionSet-id = '{{ permissionGrantConditionSet-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
