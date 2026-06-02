--- 
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - devices
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

Creates, updates, deletes, gets or lists a <code>devices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="devices" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.devices.devices" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_2', value: 'get_2' },
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
<TabItem value="get_2">

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
    <td><a href="#parameter-deviceId"><code>deviceId</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the properties and relationships of a device object.</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-device-id"><code>device-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the properties and relationships of a device object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of device objects registered in the organization.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create and register a new device in the organization.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-deviceId"><code>deviceId</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a registered device. Only certain properties of a device can be updated through approved Mobile Device Managment (MDM) apps.</td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-device-id"><code>device-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a registered device. Only certain properties of a device can be updated through approved Mobile Device Managment (MDM) apps.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-deviceId"><code>deviceId</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a registered device.</td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device-id"><code>device-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a registered device.</td>
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
    <td><a href="#parameter-device-id"><code>device-id</code></a></td>
    <td></td>
    <td>Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.</td>
</tr>
<tr>
    <td><a href="#check_member_objects"><CopyableCode code="check_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device-id"><code>device-id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_member_groups"><CopyableCode code="get_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device-id"><code>device-id</code></a></td>
    <td></td>
    <td>Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.</td>
</tr>
<tr>
    <td><a href="#get_member_objects"><CopyableCode code="get_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device-id"><code>device-id</code></a></td>
    <td></td>
    <td>Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-device-id"><code>device-id</code></a></td>
    <td></td>
    <td>Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.</td>
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
<tr id="parameter-device-id">
    <td><CopyableCode code="device-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of device</td>
</tr>
<tr id="parameter-deviceId">
    <td><CopyableCode code="deviceId" /></td>
    <td><code>string</code></td>
    <td>Alternate key of device</td>
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
<tr id="parameter-ConsistencyLevel">
    <td><CopyableCode code="ConsistencyLevel" /></td>
    <td><code>string</code></td>
    <td>Indicates the requested consistency level. Documentation URL: https://docs.microsoft.com/graph/aad-advanced-queries</td>
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
        { label: 'get_2', value: 'get_2' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the properties and relationships of a device object.

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
FROM entraid.devices.devices
WHERE deviceId = '{{ deviceId }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_2">

Get the properties and relationships of a device object.

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
FROM entraid.devices.devices
WHERE device-id = '{{ device-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of device objects registered in the organization.

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
FROM entraid.devices.devices
WHERE ConsistencyLevel = '{{ ConsistencyLevel }}'
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

Create and register a new device in the organization.

```sql
INSERT INTO entraid.devices.devices (
id,
@odata.type,
deletedDateTime,
accountEnabled,
alternativeSecurityIds,
approximateLastSignInDateTime,
complianceExpirationDateTime,
deviceCategory,
deviceId,
deviceMetadata,
deviceOwnership,
deviceVersion,
displayName,
enrollmentProfileName,
enrollmentType,
isCompliant,
isManaged,
isManagementRestricted,
isRooted,
managementType,
manufacturer,
mdmAppId,
model,
onPremisesLastSyncDateTime,
onPremisesSecurityIdentifier,
onPremisesSyncEnabled,
operatingSystem,
operatingSystemVersion,
physicalIds,
profileType,
registrationDateTime,
systemLabels,
trustType,
extensions,
memberOf,
registeredOwners,
registeredUsers,
transitiveMemberOf
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
{{ accountEnabled }},
'{{ alternativeSecurityIds }}',
'{{ approximateLastSignInDateTime }}',
'{{ complianceExpirationDateTime }}',
'{{ deviceCategory }}',
'{{ deviceId }}',
'{{ deviceMetadata }}',
'{{ deviceOwnership }}',
{{ deviceVersion }},
'{{ displayName }}',
'{{ enrollmentProfileName }}',
'{{ enrollmentType }}',
{{ isCompliant }},
{{ isManaged }},
{{ isManagementRestricted }},
{{ isRooted }},
'{{ managementType }}',
'{{ manufacturer }}',
'{{ mdmAppId }}',
'{{ model }}',
'{{ onPremisesLastSyncDateTime }}',
'{{ onPremisesSecurityIdentifier }}',
{{ onPremisesSyncEnabled }},
'{{ operatingSystem }}',
'{{ operatingSystemVersion }}',
'{{ physicalIds }}',
'{{ profileType }}',
'{{ registrationDateTime }}',
'{{ systemLabels }}',
'{{ trustType }}',
'{{ extensions }}',
'{{ memberOf }}',
'{{ registeredOwners }}',
'{{ registeredUsers }}',
'{{ transitiveMemberOf }}'
RETURNING
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
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: devices
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
    - name: accountEnabled
      value: {{ accountEnabled }}
      description: |
        true if the account is enabled; otherwise, false. Required. Default is true.  Supports $filter (eq, ne, not, in). Only callers with at least the Cloud Device Administrator role can set this property.
    - name: alternativeSecurityIds
      description: |
        For internal use only. Not nullable. Supports $filter (eq, not, ge, le).
      value:
        - identityProvider: "{{ identityProvider }}"
          key: "{{ key }}"
          type: {{ type }}
          @odata.type: "{{ @odata.type }}"
    - name: approximateLastSignInDateTime
      value: "{{ approximateLastSignInDateTime }}"
      description: |
        The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Supports $filter (eq, ne, not, ge, le, and eq on null values) and $orderby.
    - name: complianceExpirationDateTime
      value: "{{ complianceExpirationDateTime }}"
      description: |
        The timestamp when the device is no longer deemed compliant. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: deviceCategory
      value: "{{ deviceCategory }}"
      description: |
        User-defined property set by Intune to automatically add devices to groups and simplify managing devices.
    - name: deviceId
      value: "{{ deviceId }}"
      description: |
        Unique identifier set by Azure Device Registration Service at the time of registration. This alternate key can be used to reference the device object. Supports $filter (eq, ne, not, startsWith).
    - name: deviceMetadata
      value: "{{ deviceMetadata }}"
      description: |
        For internal use only. Set to null.
    - name: deviceOwnership
      value: "{{ deviceOwnership }}"
      description: |
        Ownership of the device. Intune sets this property. The possible values are: unknown, company, personal.
    - name: deviceVersion
      value: {{ deviceVersion }}
      description: |
        For internal use only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the device. Maximum length is 256 characters. Required. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    - name: enrollmentProfileName
      value: "{{ enrollmentProfileName }}"
      description: |
        Enrollment profile applied to the device. For example, Apple Device Enrollment Profile, Device enrollment - Corporate device identifiers, or Windows Autopilot profile name. This property is set by Intune.
    - name: enrollmentType
      value: "{{ enrollmentType }}"
      description: |
        Enrollment type of the device. Intune sets this property. The possible values are: unknown, userEnrollment, deviceEnrollmentManager, appleBulkWithUser, appleBulkWithoutUser, windowsAzureADJoin, windowsBulkUserless, windowsAutoEnrollment, windowsBulkAzureDomainJoin, windowsCoManagement, windowsAzureADJoinUsingDeviceAuth,appleUserEnrollment, appleUserEnrollmentWithServiceAccount. NOTE: This property might return other values apart from those listed.
    - name: isCompliant
      value: {{ isCompliant }}
      description: |
        true if the device complies with Mobile Device Management (MDM) policies; otherwise, false. Read-only. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
    - name: isManaged
      value: {{ isManaged }}
      description: |
        true if the device is managed by a Mobile Device Management (MDM) app; otherwise, false. This can only be updated by Intune for any device OS type or by an approved MDM app for Windows OS devices. Supports $filter (eq, ne, not).
    - name: isManagementRestricted
      value: {{ isManagementRestricted }}
      description: |
        Indicates whether the device is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a device that's a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.
    - name: isRooted
      value: {{ isRooted }}
      description: |
        true if the device is rooted or jail-broken. This property can only be updated by Intune.
    - name: managementType
      value: "{{ managementType }}"
      description: |
        The management channel of the device. This property is set by Intune. The possible values are: eas, mdm, easMdm, intuneClient, easIntuneClient, configurationManagerClient, configurationManagerClientMdm, configurationManagerClientMdmEas, unknown, jamf, googleCloudDevicePolicyController.
    - name: manufacturer
      value: "{{ manufacturer }}"
      description: |
        Manufacturer of the device. Read-only.
    - name: mdmAppId
      value: "{{ mdmAppId }}"
      description: |
        Application identifier used to register device into MDM. Read-only. Supports $filter (eq, ne, not, startsWith).
    - name: model
      value: "{{ model }}"
      description: |
        Model of the device. Read-only.
    - name: onPremisesLastSyncDateTime
      value: "{{ onPremisesLastSyncDateTime }}"
      description: |
        The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z Read-only. Supports $filter (eq, ne, not, ge, le, in).
    - name: onPremisesSecurityIdentifier
      value: "{{ onPremisesSecurityIdentifier }}"
      description: |
        The on-premises security identifier (SID) for the user who was synchronized from on-premises to the cloud. Read-only. Requires $select to retrieve. Supports $filter (eq).
    - name: onPremisesSyncEnabled
      value: {{ onPremisesSyncEnabled }}
      description: |
        true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced; null if this object has never been synced from an on-premises directory (default). Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
    - name: operatingSystem
      value: "{{ operatingSystem }}"
      description: |
        The type of operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
    - name: operatingSystemVersion
      value: "{{ operatingSystemVersion }}"
      description: |
        The version of the operating system on the device. Required. Supports $filter (eq, ne, not, ge, le, startsWith, and eq on null values).
    - name: physicalIds
      value:
        - "{{ physicalIds }}"
      description: |
        For internal use only. Not nullable. Supports $filter (eq, not, ge, le, startsWith,/$count eq 0, /$count ne 0).
    - name: profileType
      value: "{{ profileType }}"
      description: |
        The profile type of the device. Possible values: RegisteredDevice (default), SecureVM, Printer, Shared, IoT.
    - name: registrationDateTime
      value: "{{ registrationDateTime }}"
      description: |
        Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: systemLabels
      value:
        - "{{ systemLabels }}"
      description: |
        List of labels applied to the device by the system. Supports $filter (/$count eq 0, /$count ne 0).
    - name: trustType
      value: "{{ trustType }}"
      description: |
        Type of trust for the joined device. Read-only. Possible values:  Workplace (indicates bring your own personal devices), AzureAd (Cloud-only joined devices), ServerAd (on-premises domain joined devices joined to Microsoft Entra ID). For more information, see Introduction to device management in Microsoft Entra ID. Supports $filter (eq, ne, not, in).
    - name: extensions
      description: |
        The collection of open extensions defined for the device. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
    - name: memberOf
      description: |
        Groups and administrative units that this device is a member of. Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: registeredOwners
      description: |
        The user that cloud joined the device or registered their personal device. The registered owner is set at the time of registration. Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: registeredUsers
      description: |
        Collection of registered users of the device. For cloud joined devices and registered personal devices, registered users are set to the same value as registered owners at the time of registration. Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: transitiveMemberOf
      description: |
        Groups and administrative units that the device is a member of. This operation is transitive. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' },
        { label: 'update_2', value: 'update_2' }
    ]}
>
<TabItem value="update">

Update the properties of a registered device. Only certain properties of a device can be updated through approved Mobile Device Managment (MDM) apps.

```sql
UPDATE entraid.devices.devices
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
accountEnabled = {{ accountEnabled }},
alternativeSecurityIds = '{{ alternativeSecurityIds }}',
approximateLastSignInDateTime = '{{ approximateLastSignInDateTime }}',
complianceExpirationDateTime = '{{ complianceExpirationDateTime }}',
deviceCategory = '{{ deviceCategory }}',
deviceId = '{{ deviceId }}',
deviceMetadata = '{{ deviceMetadata }}',
deviceOwnership = '{{ deviceOwnership }}',
deviceVersion = {{ deviceVersion }},
displayName = '{{ displayName }}',
enrollmentProfileName = '{{ enrollmentProfileName }}',
enrollmentType = '{{ enrollmentType }}',
isCompliant = {{ isCompliant }},
isManaged = {{ isManaged }},
isManagementRestricted = {{ isManagementRestricted }},
isRooted = {{ isRooted }},
managementType = '{{ managementType }}',
manufacturer = '{{ manufacturer }}',
mdmAppId = '{{ mdmAppId }}',
model = '{{ model }}',
onPremisesLastSyncDateTime = '{{ onPremisesLastSyncDateTime }}',
onPremisesSecurityIdentifier = '{{ onPremisesSecurityIdentifier }}',
onPremisesSyncEnabled = {{ onPremisesSyncEnabled }},
operatingSystem = '{{ operatingSystem }}',
operatingSystemVersion = '{{ operatingSystemVersion }}',
physicalIds = '{{ physicalIds }}',
profileType = '{{ profileType }}',
registrationDateTime = '{{ registrationDateTime }}',
systemLabels = '{{ systemLabels }}',
trustType = '{{ trustType }}',
extensions = '{{ extensions }}',
memberOf = '{{ memberOf }}',
registeredOwners = '{{ registeredOwners }}',
registeredUsers = '{{ registeredUsers }}',
transitiveMemberOf = '{{ transitiveMemberOf }}'
WHERE 
deviceId = '{{ deviceId }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
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
trustType;
```
</TabItem>
<TabItem value="update_2">

Update the properties of a registered device. Only certain properties of a device can be updated through approved Mobile Device Managment (MDM) apps.

```sql
UPDATE entraid.devices.devices
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
accountEnabled = {{ accountEnabled }},
alternativeSecurityIds = '{{ alternativeSecurityIds }}',
approximateLastSignInDateTime = '{{ approximateLastSignInDateTime }}',
complianceExpirationDateTime = '{{ complianceExpirationDateTime }}',
deviceCategory = '{{ deviceCategory }}',
deviceId = '{{ deviceId }}',
deviceMetadata = '{{ deviceMetadata }}',
deviceOwnership = '{{ deviceOwnership }}',
deviceVersion = {{ deviceVersion }},
displayName = '{{ displayName }}',
enrollmentProfileName = '{{ enrollmentProfileName }}',
enrollmentType = '{{ enrollmentType }}',
isCompliant = {{ isCompliant }},
isManaged = {{ isManaged }},
isManagementRestricted = {{ isManagementRestricted }},
isRooted = {{ isRooted }},
managementType = '{{ managementType }}',
manufacturer = '{{ manufacturer }}',
mdmAppId = '{{ mdmAppId }}',
model = '{{ model }}',
onPremisesLastSyncDateTime = '{{ onPremisesLastSyncDateTime }}',
onPremisesSecurityIdentifier = '{{ onPremisesSecurityIdentifier }}',
onPremisesSyncEnabled = {{ onPremisesSyncEnabled }},
operatingSystem = '{{ operatingSystem }}',
operatingSystemVersion = '{{ operatingSystemVersion }}',
physicalIds = '{{ physicalIds }}',
profileType = '{{ profileType }}',
registrationDateTime = '{{ registrationDateTime }}',
systemLabels = '{{ systemLabels }}',
trustType = '{{ trustType }}',
extensions = '{{ extensions }}',
memberOf = '{{ memberOf }}',
registeredOwners = '{{ registeredOwners }}',
registeredUsers = '{{ registeredUsers }}',
transitiveMemberOf = '{{ transitiveMemberOf }}'
WHERE 
device-id = '{{ device-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
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
trustType;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'delete_2', value: 'delete_2' }
    ]}
>
<TabItem value="delete">

Delete a registered device.

```sql
DELETE FROM entraid.devices.devices
WHERE deviceId = '{{ deviceId }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

Delete a registered device.

```sql
DELETE FROM entraid.devices.devices
WHERE device-id = '{{ device-id }}' --required
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
        { label: 'restore', value: 'restore' }
    ]}
>
<TabItem value="get_available_extension_properties">

Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:

```sql
EXEC entraid.devices.devices.get_available_extension_properties 
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
EXEC entraid.devices.devices.get_by_ids 
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
EXEC entraid.devices.devices.validate_properties 
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
EXEC entraid.devices.devices.check_member_groups 
@device-id='{{ device-id }}' --required 
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
EXEC entraid.devices.devices.check_member_objects 
@device-id='{{ device-id }}' --required 
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
EXEC entraid.devices.devices.get_member_groups 
@device-id='{{ device-id }}' --required 
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
EXEC entraid.devices.devices.get_member_objects 
@device-id='{{ device-id }}' --required 
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
EXEC entraid.devices.devices.restore 
@device-id='{{ device-id }}' --required
;
```
</TabItem>
</Tabs>
