--- 
title: application_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - application_templates
  - application_templates
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

Creates, updates, deletes, gets or lists an <code>application_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.application_templates.application_templates" /></td></tr>
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
    <td><a href="#parameter-application_template_id"><code>application_template_id</code></a></td>
    <td></td>
    <td>Retrieve the properties of an applicationTemplate object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of applicationTemplate objects from the Microsoft Entra application gallery.</td>
</tr>
<tr>
    <td><a href="#instantiate"><CopyableCode code="instantiate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_template_id"><code>application_template_id</code></a></td>
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
<tr id="parameter-application_template_id">
    <td><CopyableCode code="application_template_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of applicationTemplate</td>
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
categories,
description,
displayName,
homePageUrl,
logoUrl,
publisher,
supportedProvisioningTypes,
supportedSingleSignOnModes
FROM entra_id.application_templates.application_templates
WHERE application_template_id = '{{ application_template_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of applicationTemplate objects from the Microsoft Entra application gallery.

```sql
SELECT
id,
categories,
description,
displayName,
homePageUrl,
logoUrl,
publisher,
supportedProvisioningTypes,
supportedSingleSignOnModes
FROM entra_id.application_templates.application_templates
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
EXEC entra_id.application_templates.application_templates.instantiate 
@application_template_id='{{ application_template_id }}' --required 
@@json=
'{
"displayName": "{{ displayName }}", 
"serviceManagementReference": "{{ serviceManagementReference }}"
}'
;
```
</TabItem>
</Tabs>
