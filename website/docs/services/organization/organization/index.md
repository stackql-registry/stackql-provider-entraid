--- 
title: organization
hide_title: false
hide_table_of_contents: false
keywords:
  - organization
  - organization
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

Creates, updates, deletes, gets or lists an <code>organization</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="organization" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.organization.organization" /></td></tr>
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
    <td><CopyableCode code="assignedPlans" /></td>
    <td><code>array</code></td>
    <td>The collection of service plans associated with the tenant. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="branding" /></td>
    <td><code></code></td>
    <td>Branding for the organization. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="businessPhones" /></td>
    <td><code>array</code></td>
    <td>Telephone number for the organization. Although this property is a string collection, only one number can be set.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateBasedAuthConfiguration" /></td>
    <td><code>array</code></td>
    <td>Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.</td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>City name of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Country or region name of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="countryLetterCode" /></td>
    <td><code>string</code></td>
    <td>Country or region abbreviation for the organization in ISO 3166-2 format.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the organization was created. The value can't be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultUsageLocation" /></td>
    <td><code>string</code></td>
    <td>Two-letter ISO 3166 country code indicating the default service usage location of an organization.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the organization. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="marketingNotificationEmails" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mobileDeviceManagementAuthority" /></td>
    <td><code>string</code></td>
    <td>Mobile device management authority. (unknown, intune, sccm, office365) (title: mdmAuthority)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time and date at which the tenant was last synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced. Nullable. null if this object isn't synced from on-premises active directory (default).</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTenantType" /></td>
    <td><code></code></td>
    <td>The type of partnership this tenant has with Microsoft. The possible values are: microsoftSupport, syndicatePartner, breadthPartner, breadthPartnerDelegatedAdmin, resellerPartnerDelegatedAdmin, valueAddedResellerPartnerDelegatedAdmin, unknownFutureValue. Nullable. For more information about the possible types, see partnerTenantType values.</td>
</tr>
<tr>
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>Postal code of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for the organization. Should follow ISO 639-1 Code; for example, en.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyProfile" /></td>
    <td><code></code></td>
    <td>The privacy profile of an organization.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedPlans" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="securityComplianceNotificationMails" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="securityComplianceNotificationPhones" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State name of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="street" /></td>
    <td><code>string</code></td>
    <td>Street name of the address for organization.</td>
</tr>
<tr>
    <td><CopyableCode code="technicalNotificationMails" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantType" /></td>
    <td><code>string</code></td>
    <td>Not nullable. Can be one of the following types:  AAD - An enterprise identity access management (IAM) service that serves business-to-employee and business-to-business (B2B) scenarios.  AAD B2C An identity access management (IAM) service that serves business-to-consumer (B2C) scenarios.   CIAM - A customer identity & access management (CIAM) solution that provides an integrated platform to serve consumers, partners, and citizen scenarios.</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedDomains" /></td>
    <td><code>array</code></td>
    <td>The collection of domains associated with this tenant. Not nullable.</td>
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
    <td><CopyableCode code="assignedPlans" /></td>
    <td><code>array</code></td>
    <td>The collection of service plans associated with the tenant. Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="branding" /></td>
    <td><code></code></td>
    <td>Branding for the organization. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="businessPhones" /></td>
    <td><code>array</code></td>
    <td>Telephone number for the organization. Although this property is a string collection, only one number can be set.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateBasedAuthConfiguration" /></td>
    <td><code>array</code></td>
    <td>Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.</td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>City name of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Country or region name of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="countryLetterCode" /></td>
    <td><code>string</code></td>
    <td>Country or region abbreviation for the organization in ISO 3166-2 format.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the organization was created. The value can't be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="defaultUsageLocation" /></td>
    <td><code>string</code></td>
    <td>Two-letter ISO 3166 country code indicating the default service usage location of an organization.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the organization. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="marketingNotificationEmails" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mobileDeviceManagementAuthority" /></td>
    <td><code>string</code></td>
    <td>Mobile device management authority. (unknown, intune, sccm, office365) (title: mdmAuthority)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time and date at which the tenant was last synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced. Nullable. null if this object isn't synced from on-premises active directory (default).</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTenantType" /></td>
    <td><code></code></td>
    <td>The type of partnership this tenant has with Microsoft. The possible values are: microsoftSupport, syndicatePartner, breadthPartner, breadthPartnerDelegatedAdmin, resellerPartnerDelegatedAdmin, valueAddedResellerPartnerDelegatedAdmin, unknownFutureValue. Nullable. For more information about the possible types, see partnerTenantType values.</td>
</tr>
<tr>
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>Postal code of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for the organization. Should follow ISO 639-1 Code; for example, en.</td>
</tr>
<tr>
    <td><CopyableCode code="privacyProfile" /></td>
    <td><code></code></td>
    <td>The privacy profile of an organization.</td>
</tr>
<tr>
    <td><CopyableCode code="provisionedPlans" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="securityComplianceNotificationMails" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="securityComplianceNotificationPhones" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>State name of the address for the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="street" /></td>
    <td><code>string</code></td>
    <td>Street name of the address for organization.</td>
</tr>
<tr>
    <td><CopyableCode code="technicalNotificationMails" /></td>
    <td><code>array</code></td>
    <td>Not nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantType" /></td>
    <td><code>string</code></td>
    <td>Not nullable. Can be one of the following types:  AAD - An enterprise identity access management (IAM) service that serves business-to-employee and business-to-business (B2B) scenarios.  AAD B2C An identity access management (IAM) service that serves business-to-consumer (B2C) scenarios.   CIAM - A customer identity & access management (CIAM) solution that provides an integrated platform to serve consumers, partners, and citizen scenarios.</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedDomains" /></td>
    <td><code>array</code></td>
    <td>The collection of domains associated with this tenant. Not nullable.</td>
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
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the properties and relationships of the currently authenticated organization. Since the organization resource supports extensions, you can also use the GET operation to get custom properties and extension data in an organization instance.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of organization objects. There's only one organization object in the collection.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of the currently authenticated organization. In this case, organization is defined as a collection of exactly one record, and so its ID must be specified in the request.  The ID is also known as the tenantId of the organization.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_available_extension_properties"><CopyableCode code="get_available_extension_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:</td>
</tr>
<tr>
    <td><a href="#get_by_ids"><CopyableCode code="get_by_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Return the directory objects specified in a list of IDs. Only a subset of user properties are returned by default in v1.0. Some common uses for this function are to:</td>
</tr>
<tr>
    <td><a href="#validate_properties"><CopyableCode code="validate_properties" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Validate that a Microsoft 365 group's display name or mail nickname complies with naming policies. Clients can use this API to determine whether a display name or mail nickname is valid before trying to create a Microsoft 365 group. To validate the properties of an existing group, use the group: validateProperties function. The following policy validations are performed for the display name and mail nickname properties:<br />1. Validate the prefix and suffix naming policy<br />2. Validate the custom banned words policy<br />3. Validate that the mail nickname is unique This API only returns the first validation failure that is encountered. If the properties fail multiple validations, only the first validation failure is returned. However, you can validate both the mail nickname and the display name and receive a collection of validation errors if you're only validating the prefix and suffix naming policy. To learn more about configuring naming policies, see Configure naming policy.</td>
</tr>
<tr>
    <td><a href="#check_member_groups"><CopyableCode code="check_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td></td>
    <td>Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.</td>
</tr>
<tr>
    <td><a href="#check_member_objects"><CopyableCode code="check_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_member_groups"><CopyableCode code="get_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td></td>
    <td>Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.</td>
</tr>
<tr>
    <td><a href="#get_member_objects"><CopyableCode code="get_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td></td>
    <td>Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td></td>
    <td>Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.</td>
</tr>
<tr>
    <td><a href="#set_mobile_device_management_authority"><CopyableCode code="set_mobile_device_management_authority" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td></td>
    <td>Set mobile device management authority</td>
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
<tr id="parameter-organization-id">
    <td><CopyableCode code="organization-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of organization</td>
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

Get the properties and relationships of the currently authenticated organization. Since the organization resource supports extensions, you can also use the GET operation to get custom properties and extension data in an organization instance.

```sql
SELECT
id,
@odata.type,
assignedPlans,
branding,
businessPhones,
certificateBasedAuthConfiguration,
city,
country,
countryLetterCode,
createdDateTime,
defaultUsageLocation,
deletedDateTime,
displayName,
extensions,
marketingNotificationEmails,
mobileDeviceManagementAuthority,
onPremisesLastSyncDateTime,
onPremisesSyncEnabled,
partnerTenantType,
postalCode,
preferredLanguage,
privacyProfile,
provisionedPlans,
securityComplianceNotificationMails,
securityComplianceNotificationPhones,
state,
street,
technicalNotificationMails,
tenantType,
verifiedDomains
FROM entraid.organization.organization
WHERE organization-id = '{{ organization-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of organization objects. There's only one organization object in the collection.

```sql
SELECT
id,
@odata.type,
assignedPlans,
branding,
businessPhones,
certificateBasedAuthConfiguration,
city,
country,
countryLetterCode,
createdDateTime,
defaultUsageLocation,
deletedDateTime,
displayName,
extensions,
marketingNotificationEmails,
mobileDeviceManagementAuthority,
onPremisesLastSyncDateTime,
onPremisesSyncEnabled,
partnerTenantType,
postalCode,
preferredLanguage,
privacyProfile,
provisionedPlans,
securityComplianceNotificationMails,
securityComplianceNotificationPhones,
state,
street,
technicalNotificationMails,
tenantType,
verifiedDomains
FROM entraid.organization.organization
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
INSERT INTO entraid.organization.organization (
id,
@odata.type,
deletedDateTime,
assignedPlans,
businessPhones,
city,
country,
countryLetterCode,
createdDateTime,
defaultUsageLocation,
displayName,
marketingNotificationEmails,
mobileDeviceManagementAuthority,
onPremisesLastSyncDateTime,
onPremisesSyncEnabled,
partnerTenantType,
postalCode,
preferredLanguage,
privacyProfile,
provisionedPlans,
securityComplianceNotificationMails,
securityComplianceNotificationPhones,
state,
street,
technicalNotificationMails,
tenantType,
verifiedDomains,
branding,
certificateBasedAuthConfiguration,
extensions
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
'{{ assignedPlans }}',
'{{ businessPhones }}',
'{{ city }}',
'{{ country }}',
'{{ countryLetterCode }}',
'{{ createdDateTime }}',
'{{ defaultUsageLocation }}',
'{{ displayName }}',
'{{ marketingNotificationEmails }}',
'{{ mobileDeviceManagementAuthority }}',
'{{ onPremisesLastSyncDateTime }}',
{{ onPremisesSyncEnabled }},
'{{ partnerTenantType }}',
'{{ postalCode }}',
'{{ preferredLanguage }}',
'{{ privacyProfile }}',
'{{ provisionedPlans }}',
'{{ securityComplianceNotificationMails }}',
'{{ securityComplianceNotificationPhones }}',
'{{ state }}',
'{{ street }}',
'{{ technicalNotificationMails }}',
'{{ tenantType }}',
'{{ verifiedDomains }}',
'{{ branding }}',
'{{ certificateBasedAuthConfiguration }}',
'{{ extensions }}'
RETURNING
id,
@odata.type,
assignedPlans,
branding,
businessPhones,
certificateBasedAuthConfiguration,
city,
country,
countryLetterCode,
createdDateTime,
defaultUsageLocation,
deletedDateTime,
displayName,
extensions,
marketingNotificationEmails,
mobileDeviceManagementAuthority,
onPremisesLastSyncDateTime,
onPremisesSyncEnabled,
partnerTenantType,
postalCode,
preferredLanguage,
privacyProfile,
provisionedPlans,
securityComplianceNotificationMails,
securityComplianceNotificationPhones,
state,
street,
technicalNotificationMails,
tenantType,
verifiedDomains
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: organization
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
      description: |
        Date and time when this object was deleted. Always null when the object hasn't been deleted.
    - name: assignedPlans
      description: |
        The collection of service plans associated with the tenant. Not nullable.
      value:
        - assignedDateTime: "{{ assignedDateTime }}"
          capabilityStatus: "{{ capabilityStatus }}"
          service: "{{ service }}"
          servicePlanId: "{{ servicePlanId }}"
          @odata.type: "{{ @odata.type }}"
    - name: businessPhones
      value:
        - "{{ businessPhones }}"
      description: |
        Telephone number for the organization. Although this property is a string collection, only one number can be set.
    - name: city
      value: "{{ city }}"
      description: |
        City name of the address for the organization.
    - name: country
      value: "{{ country }}"
      description: |
        Country or region name of the address for the organization.
    - name: countryLetterCode
      value: "{{ countryLetterCode }}"
      description: |
        Country or region abbreviation for the organization in ISO 3166-2 format.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        Timestamp of when the organization was created. The value can't be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: defaultUsageLocation
      value: "{{ defaultUsageLocation }}"
      description: |
        Two-letter ISO 3166 country code indicating the default service usage location of an organization.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the tenant.
    - name: marketingNotificationEmails
      value:
        - "{{ marketingNotificationEmails }}"
      description: |
        Not nullable.
    - name: mobileDeviceManagementAuthority
      value: "{{ mobileDeviceManagementAuthority }}"
      description: |
        Mobile device management authority.
      valid_values: ['unknown', 'intune', 'sccm', 'office365']
    - name: onPremisesLastSyncDateTime
      value: "{{ onPremisesLastSyncDateTime }}"
      description: |
        The time and date at which the tenant was last synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: onPremisesSyncEnabled
      value: {{ onPremisesSyncEnabled }}
      description: |
        true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced. Nullable. null if this object isn't synced from on-premises active directory (default).
    - name: partnerTenantType
      value: "{{ partnerTenantType }}"
      description: |
        The type of partnership this tenant has with Microsoft. The possible values are: microsoftSupport, syndicatePartner, breadthPartner, breadthPartnerDelegatedAdmin, resellerPartnerDelegatedAdmin, valueAddedResellerPartnerDelegatedAdmin, unknownFutureValue. Nullable. For more information about the possible types, see partnerTenantType values.
    - name: postalCode
      value: "{{ postalCode }}"
      description: |
        Postal code of the address for the organization.
    - name: preferredLanguage
      value: "{{ preferredLanguage }}"
      description: |
        The preferred language for the organization. Should follow ISO 639-1 Code; for example, en.
    - name: privacyProfile
      value: "{{ privacyProfile }}"
      description: |
        The privacy profile of an organization.
    - name: provisionedPlans
      description: |
        Not nullable.
      value:
        - capabilityStatus: "{{ capabilityStatus }}"
          provisioningStatus: "{{ provisioningStatus }}"
          service: "{{ service }}"
          @odata.type: "{{ @odata.type }}"
    - name: securityComplianceNotificationMails
      value:
        - "{{ securityComplianceNotificationMails }}"
      description: |
        Not nullable.
    - name: securityComplianceNotificationPhones
      value:
        - "{{ securityComplianceNotificationPhones }}"
      description: |
        Not nullable.
    - name: state
      value: "{{ state }}"
      description: |
        State name of the address for the organization.
    - name: street
      value: "{{ street }}"
      description: |
        Street name of the address for organization.
    - name: technicalNotificationMails
      value:
        - "{{ technicalNotificationMails }}"
      description: |
        Not nullable.
    - name: tenantType
      value: "{{ tenantType }}"
      description: |
        Not nullable. Can be one of the following types:  AAD - An enterprise identity access management (IAM) service that serves business-to-employee and business-to-business (B2B) scenarios.  AAD B2C An identity access management (IAM) service that serves business-to-consumer (B2C) scenarios.   CIAM - A customer identity & access management (CIAM) solution that provides an integrated platform to serve consumers, partners, and citizen scenarios.
    - name: verifiedDomains
      description: |
        The collection of domains associated with this tenant. Not nullable.
      value:
        - capabilities: "{{ capabilities }}"
          isDefault: {{ isDefault }}
          isInitial: {{ isInitial }}
          name: "{{ name }}"
          type: "{{ type }}"
          @odata.type: "{{ @odata.type }}"
    - name: branding
      value: "{{ branding }}"
      description: |
        Branding for the organization. Nullable.
    - name: certificateBasedAuthConfiguration
      description: |
        Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          certificateAuthorities: "{{ certificateAuthorities }}"
    - name: extensions
      description: |
        The collection of open extensions defined for the organization. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
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

Update the properties of the currently authenticated organization. In this case, organization is defined as a collection of exactly one record, and so its ID must be specified in the request.  The ID is also known as the tenantId of the organization.

```sql
UPDATE entraid.organization.organization
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
assignedPlans = '{{ assignedPlans }}',
businessPhones = '{{ businessPhones }}',
city = '{{ city }}',
country = '{{ country }}',
countryLetterCode = '{{ countryLetterCode }}',
createdDateTime = '{{ createdDateTime }}',
defaultUsageLocation = '{{ defaultUsageLocation }}',
displayName = '{{ displayName }}',
marketingNotificationEmails = '{{ marketingNotificationEmails }}',
mobileDeviceManagementAuthority = '{{ mobileDeviceManagementAuthority }}',
onPremisesLastSyncDateTime = '{{ onPremisesLastSyncDateTime }}',
onPremisesSyncEnabled = {{ onPremisesSyncEnabled }},
partnerTenantType = '{{ partnerTenantType }}',
postalCode = '{{ postalCode }}',
preferredLanguage = '{{ preferredLanguage }}',
privacyProfile = '{{ privacyProfile }}',
provisionedPlans = '{{ provisionedPlans }}',
securityComplianceNotificationMails = '{{ securityComplianceNotificationMails }}',
securityComplianceNotificationPhones = '{{ securityComplianceNotificationPhones }}',
state = '{{ state }}',
street = '{{ street }}',
technicalNotificationMails = '{{ technicalNotificationMails }}',
tenantType = '{{ tenantType }}',
verifiedDomains = '{{ verifiedDomains }}',
branding = '{{ branding }}',
certificateBasedAuthConfiguration = '{{ certificateBasedAuthConfiguration }}',
extensions = '{{ extensions }}'
WHERE 
organization-id = '{{ organization-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
assignedPlans,
branding,
businessPhones,
certificateBasedAuthConfiguration,
city,
country,
countryLetterCode,
createdDateTime,
defaultUsageLocation,
deletedDateTime,
displayName,
extensions,
marketingNotificationEmails,
mobileDeviceManagementAuthority,
onPremisesLastSyncDateTime,
onPremisesSyncEnabled,
partnerTenantType,
postalCode,
preferredLanguage,
privacyProfile,
provisionedPlans,
securityComplianceNotificationMails,
securityComplianceNotificationPhones,
state,
street,
technicalNotificationMails,
tenantType,
verifiedDomains;
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
DELETE FROM entraid.organization.organization
WHERE organization-id = '{{ organization-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_available_extension_properties"
    values={[
        { label: 'get_available_extension_properties', value: 'get_available_extension_properties' },
        { label: 'get_by_ids', value: 'get_by_ids' },
        { label: 'validate_properties', value: 'validate_properties' },
        { label: 'check_member_groups', value: 'check_member_groups' },
        { label: 'check_member_objects', value: 'check_member_objects' },
        { label: 'get_member_groups', value: 'get_member_groups' },
        { label: 'get_member_objects', value: 'get_member_objects' },
        { label: 'restore', value: 'restore' },
        { label: 'set_mobile_device_management_authority', value: 'set_mobile_device_management_authority' }
    ]}
>
<TabItem value="get_available_extension_properties">

Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:

```sql
EXEC entraid.organization.organization.get_available_extension_properties 
@@json=
'{
"isSyncedFromOnPremises": {{ isSyncedFromOnPremises }}
}'
;
```
</TabItem>
<TabItem value="get_by_ids">

Return the directory objects specified in a list of IDs. Only a subset of user properties are returned by default in v1.0. Some common uses for this function are to:

```sql
EXEC entraid.organization.organization.get_by_ids 
@@json=
'{
"ids": "{{ ids }}", 
"types": "{{ types }}"
}'
;
```
</TabItem>
<TabItem value="validate_properties">

Validate that a Microsoft 365 group's display name or mail nickname complies with naming policies. Clients can use this API to determine whether a display name or mail nickname is valid before trying to create a Microsoft 365 group. To validate the properties of an existing group, use the group: validateProperties function. The following policy validations are performed for the display name and mail nickname properties:<br />1. Validate the prefix and suffix naming policy<br />2. Validate the custom banned words policy<br />3. Validate that the mail nickname is unique This API only returns the first validation failure that is encountered. If the properties fail multiple validations, only the first validation failure is returned. However, you can validate both the mail nickname and the display name and receive a collection of validation errors if you're only validating the prefix and suffix naming policy. To learn more about configuring naming policies, see Configure naming policy.

```sql
EXEC entraid.organization.organization.validate_properties 
@@json=
'{
"entityType": "{{ entityType }}", 
"displayName": "{{ displayName }}", 
"mailNickname": "{{ mailNickname }}", 
"onBehalfOfUserId": "{{ onBehalfOfUserId }}"
}'
;
```
</TabItem>
<TabItem value="check_member_groups">

Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.

```sql
EXEC entraid.organization.organization.check_member_groups 
@organization-id='{{ organization-id }}' --required 
@@json=
'{
"groupIds": "{{ groupIds }}"
}'
;
```
</TabItem>
<TabItem value="check_member_objects">

Success

```sql
EXEC entraid.organization.organization.check_member_objects 
@organization-id='{{ organization-id }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="get_member_groups">

Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.

```sql
EXEC entraid.organization.organization.get_member_groups 
@organization-id='{{ organization-id }}' --required 
@@json=
'{
"securityEnabledOnly": {{ securityEnabledOnly }}
}'
;
```
</TabItem>
<TabItem value="get_member_objects">

Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.

```sql
EXEC entraid.organization.organization.get_member_objects 
@organization-id='{{ organization-id }}' --required 
@@json=
'{
"securityEnabledOnly": {{ securityEnabledOnly }}
}'
;
```
</TabItem>
<TabItem value="restore">

Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.

```sql
EXEC entraid.organization.organization.restore 
@organization-id='{{ organization-id }}' --required
;
```
</TabItem>
<TabItem value="set_mobile_device_management_authority">

Set mobile device management authority

```sql
EXEC entraid.organization.organization.set_mobile_device_management_authority 
@organization-id='{{ organization-id }}' --required
;
```
</TabItem>
</Tabs>
