--- 
title: authentication_platform_credential_methods_device
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_platform_credential_methods_device
  - users
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

Creates, updates, deletes, gets or lists an <code>authentication_platform_credential_methods_device</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_platform_credential_methods_device" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.authentication_platform_credential_methods_device" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="accountEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the account is enabled; otherwise, false. Required. Default is true.  Supports $filter (eq, ne, not, in). Only callers with at least the Cloud Device Administrator role can set this property.</td>
</tr>
<tr>
    <td><CopyableCode code="alternativeSecurityIds" /></td>
    <td><code>array</code></td>
    <td>For internal use only. Not nullable. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="approximateLastSignInDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderby. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="complianceExpirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deviceCategory" /></td>
    <td><code>string</code></td>
    <td>User-defined property set by Intune to automatically add devices to groups and simplify managing devices.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier set by Azure Device Registration Service at the time of registration. This alternate key can be used to reference the device object. Supports $filter (eq, ne, not, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceMetadata" /></td>
    <td><code>string</code></td>
    <td>For internal use only. Set to null.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceOwnership" /></td>
    <td><code>string</code></td>
    <td>Ownership of the device. Intune sets this property. The possible values are: unknown, company, personal.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceVersion" /></td>
    <td><code>number (int32)</code></td>
    <td>For internal use only.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the device. Maximum length is 256 characters. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentProfileName" /></td>
    <td><code>string</code></td>
    <td>Enrollment profile applied to the device. For example, Apple Device Enrollment Profile, Device enrollment - Corporate device identifiers, or Windows Autopilot profile name. This property is set by Intune.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentType" /></td>
    <td><code>string</code></td>
    <td>Enrollment type of the device. Intune sets this property. The possible values are: unknown, userEnrollment, deviceEnrollmentManager, appleBulkWithUser, appleBulkWithoutUser, windowsAzureADJoin, windowsBulkUserless, windowsAutoEnrollment, windowsBulkAzureDomainJoin, windowsCoManagement, windowsAzureADJoinUsingDeviceAuth,appleUserEnrollment, appleUserEnrollmentWithServiceAccount. NOTE: This property might return other values apart from those listed.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the device. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="isCompliant" /></td>
    <td><code>boolean</code></td>
    <td>true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="isManaged" /></td>
    <td><code>boolean</code></td>
    <td>true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementRestricted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the device is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a device that's a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isRooted" /></td>
    <td><code>boolean</code></td>
    <td>true if the device is rooted or jail-broken. This property can only be updated by Intune.</td>
</tr>
<tr>
    <td><CopyableCode code="managementType" /></td>
    <td><code>string</code></td>
    <td>The management channel of the device. This property is set by Intune. The possible values are: eas, mdm, easMdm, intuneClient, easIntuneClient, configurationManagerClient, configurationManagerClientMdm, configurationManagerClientMdmEas, unknown, jamf, googleCloudDevicePolicyController.</td>
</tr>
<tr>
    <td><CopyableCode code="manufacturer" /></td>
    <td><code>string</code></td>
    <td>Manufacturer of the device. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="mdmAppId" /></td>
    <td><code>string</code></td>
    <td>Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="model" /></td>
    <td><code>string</code></td>
    <td>Model of the device. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>The on-premises security identifier (SID) for the user who was synchronized from on-premises to the cloud. Read-only. Requires $select to retrieve. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystem" /></td>
    <td><code>string</code></td>
    <td>The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystemVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="physicalIds" /></td>
    <td><code>array</code></td>
    <td>For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith,/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="profileType" /></td>
    <td><code>string</code></td>
    <td>The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.</td>
</tr>
<tr>
    <td><CopyableCode code="registeredOwners" /></td>
    <td><code>array</code></td>
    <td>The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="registeredUsers" /></td>
    <td><code>array</code></td>
    <td>Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="systemLabels" /></td>
    <td><code>array</code></td>
    <td>List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td>Groups and administrative units that the device is a member of. This operation is transitive. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="trustType" /></td>
    <td><code>string</code></td>
    <td>Type of trust for the joined device. Read-only. Possible values:  Workplace (indicates bring your own personal devices), AzureAd (Cloud-only joined devices), ServerAd (on-premises domain joined devices joined to Microsoft Entra ID). For more information, see Introduction to device management in Microsoft Entra ID. Supports $filter (eq, ne, not, in).</td>
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
    <td><a href="#parameter-user-id"><code>user-id</code></a>, <a href="#parameter-platformCredentialAuthenticationMethod-id"><code>platformCredentialAuthenticationMethod-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The registered device on which this Platform Credential resides. Supports $expand. When you get a user's Platform Credential registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/platformCredentialAuthenticationMethod/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.</td>
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
<tr id="parameter-platformCredentialAuthenticationMethod-id">
    <td><CopyableCode code="platformCredentialAuthenticationMethod-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of platformCredentialAuthenticationMethod</td>
</tr>
<tr id="parameter-user-id">
    <td><CopyableCode code="user-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of user</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>Expand related entities</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>Select properties to be returned</td>
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

The registered device on which this Platform Credential resides. Supports $expand. When you get a user's Platform Credential registration information, this property is returned only on a single GET and when you specify ?$expand. For example, GET /users/admin@contoso.com/authentication/platformCredentialAuthenticationMethod/_jpuR-TGZtk6aQCLF3BQjA2?$expand=device.

```sql
SELECT
id,
@odata.type,
accountEnabled,
alternativeSecurityIds,
approximateLastSignInDateTime,
complianceExpirationDateTime,
deletedDateTime,
deviceCategory,
deviceId,
deviceMetadata,
deviceOwnership,
deviceVersion,
displayName,
enrollmentProfileName,
enrollmentType,
extensions,
isCompliant,
isManaged,
isManagementRestricted,
isRooted,
managementType,
manufacturer,
mdmAppId,
memberOf,
model,
onPremisesLastSyncDateTime,
onPremisesSecurityIdentifier,
onPremisesSyncEnabled,
operatingSystem,
operatingSystemVersion,
physicalIds,
profileType,
registeredOwners,
registeredUsers,
registrationDateTime,
systemLabels,
transitiveMemberOf,
trustType
FROM entra_id.users.authentication_platform_credential_methods_device
WHERE user-id = '{{ user-id }}' -- required
AND platformCredentialAuthenticationMethod-id = '{{ platformCredentialAuthenticationMethod-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
