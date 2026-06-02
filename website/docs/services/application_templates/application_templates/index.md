--- 
title: application_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - application_templates
  - application_templates
  - entraid
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage entraid resources using SQL
custom_edit_url: null
image: /img/stackql-entraid-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>application_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.application_templates.application_templates" /></td></tr>
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

Retrieved entity

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
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The list of categories for the application. Supported values can be: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.  Supports $filter (contains).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the application. Supports $filter (contains).</td>
</tr>
<tr>
    <td><CopyableCode code="homePageUrl" /></td>
    <td><code>string</code></td>
    <td>The home page URL of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="logoUrl" /></td>
    <td><code>string</code></td>
    <td>The URL to get the logo for this application.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The name of the publisher for this application.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedProvisioningTypes" /></td>
    <td><code>array</code></td>
    <td>The list of provisioning modes supported by this application. The only valid value is sync.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedSingleSignOnModes" /></td>
    <td><code>array</code></td>
    <td>The list of single sign-on modes supported by this application. The supported values are oidc, password, saml, and notSupported.</td>
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
    <td><CopyableCode code="categories" /></td>
    <td><code>array</code></td>
    <td>The list of categories for the application. Supported values can be: Collaboration, Business Management, Consumer, Content management, CRM, Data services, Developer services, E-commerce, Education, ERP, Finance, Health, Human resources, IT infrastructure, Mail, Management, Marketing, Media, Productivity, Project management, Telecommunications, Tools, Travel, and Web design & hosting.  Supports $filter (contains).</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the application. Supports $filter (contains).</td>
</tr>
<tr>
    <td><CopyableCode code="homePageUrl" /></td>
    <td><code>string</code></td>
    <td>The home page URL of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="logoUrl" /></td>
    <td><code>string</code></td>
    <td>The URL to get the logo for this application.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The name of the publisher for this application.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedProvisioningTypes" /></td>
    <td><code>array</code></td>
    <td>The list of provisioning modes supported by this application. The only valid value is sync.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedSingleSignOnModes" /></td>
    <td><code>array</code></td>
    <td>The list of single sign-on modes supported by this application. The supported values are oidc, password, saml, and notSupported.</td>
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
    <td><a href="#parameter-applicationTemplate-id"><code>applicationTemplate-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties of an applicationTemplate object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of applicationTemplate objects from the Microsoft Entra application gallery.</td>
</tr>
<tr>
    <td><a href="#instantiate"><CopyableCode code="instantiate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-applicationTemplate-id"><code>applicationTemplate-id</code></a></td>
    <td></td>
    <td>Add an instance of an application from the Microsoft Entra application gallery into your directory. For non-gallery apps, use an application template with one of the following IDs to configure different single sign-on (SSO) modes like SAML SSO and password-based SSO.</td>
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
<tr id="parameter-applicationTemplate-id">
    <td><CopyableCode code="applicationTemplate-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of applicationTemplate</td>
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

Retrieve the properties of an applicationTemplate object.

```sql
SELECT
id,
@odata.type,
categories,
description,
displayName,
homePageUrl,
logoUrl,
publisher,
supportedProvisioningTypes,
supportedSingleSignOnModes
FROM entraid.application_templates.application_templates
WHERE applicationTemplate-id = '{{ applicationTemplate-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of applicationTemplate objects from the Microsoft Entra application gallery.

```sql
SELECT
id,
@odata.type,
categories,
description,
displayName,
homePageUrl,
logoUrl,
publisher,
supportedProvisioningTypes,
supportedSingleSignOnModes
FROM entraid.application_templates.application_templates
WHERE $top = '{{ $top }}'
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


## Lifecycle Methods

<Tabs
    defaultValue="instantiate"
    values={[
        { label: 'instantiate', value: 'instantiate' }
    ]}
>
<TabItem value="instantiate">

Add an instance of an application from the Microsoft Entra application gallery into your directory. For non-gallery apps, use an application template with one of the following IDs to configure different single sign-on (SSO) modes like SAML SSO and password-based SSO.

```sql
EXEC entraid.application_templates.application_templates.instantiate 
@applicationTemplate-id='{{ applicationTemplate-id }}' --required 
@@json=
'{
"displayName": "{{ displayName }}", 
"serviceManagementReference": "{{ serviceManagementReference }}"
}'
;
```
</TabItem>
</Tabs>
