--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.users.users" /></td></tr>
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
    <td><CopyableCode code="aboutMe" /></td>
    <td><code>string</code></td>
    <td>A freeform text entry field for the user to describe themselves. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="accountEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the account is enabled; otherwise, false. This property is required when a user is created. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="activities" /></td>
    <td><code>array</code></td>
    <td>The user's activities across devices. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="adhocCalls" /></td>
    <td><code>array</code></td>
    <td>Ad hoc calls associated with the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="ageGroup" /></td>
    <td><code>string</code></td>
    <td>Sets the age group of the user. Allowed values: null, Minor, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="agreementAcceptances" /></td>
    <td><code>array</code></td>
    <td>The user's terms of use acceptance statuses. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignments" /></td>
    <td><code>array</code></td>
    <td>Represents the app roles a user is granted for an application. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLicenses" /></td>
    <td><code>array</code></td>
    <td>The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate between directly assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly assigned and inherited licenses. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="assignedPlans" /></td>
    <td><code>array</code></td>
    <td>The plans that are assigned to the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq and not).</td>
</tr>
<tr>
    <td><CopyableCode code="authentication" /></td>
    <td><code></code></td>
    <td>The authentication methods that are supported for the user.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationInfo" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="birthday" /></td>
    <td><code>string (date-time)</code></td>
    <td>The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="businessPhones" /></td>
    <td><code>array</code></td>
    <td>The telephone numbers for the user. NOTE: Although it's a string collection, only one number can be set for this property. Read-only for users synced from the on-premises directory. Returned by default. Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="calendar" /></td>
    <td><code></code></td>
    <td>The user's primary calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarGroups" /></td>
    <td><code>array</code></td>
    <td>The user's calendar groups. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarView" /></td>
    <td><code>array</code></td>
    <td>The calendar view for the calendar. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="calendars" /></td>
    <td><code>array</code></td>
    <td>The user's calendars. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="chats" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>The city where the user is located. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="cloudClipboard" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloudPCs" /></td>
    <td><code>array</code></td>
    <td>The user's Cloud PCs. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="companyName" /></td>
    <td><code>string</code></td>
    <td>The name of the company that the user is associated with. This property can be useful for describing the company that a guest comes from. The maximum length is 64 characters.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="consentProvidedForMinor" /></td>
    <td><code>string</code></td>
    <td>Sets whether consent was obtained for minors. Allowed values: null, Granted, Denied, and NotRequired. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="contactFolders" /></td>
    <td><code>array</code></td>
    <td>The user's contacts folders. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="contacts" /></td>
    <td><code>array</code></td>
    <td>The user's contacts. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country or region where the user is located; for example, US or UK. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the user was created, in ISO 8601 format and UTC. The value can't be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Microsoft Entra ID. Property is null for some users created before June 2018 and on-premises users that were synced to Microsoft Entra ID before June 2018. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects that the user created. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="creationType" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by a guest signing up through a link that is part of a user flow (SelfServiceSignUp). Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="customSecurityAttributes" /></td>
    <td><code></code></td>
    <td>An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, startsWith). The filter value is case-sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSecurityAndGovernance" /></td>
    <td><code></code></td>
    <td>The data security and governance settings for the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="department" /></td>
    <td><code>string</code></td>
    <td>The name of the department in which the user works. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceEnrollmentLimit" /></td>
    <td><code>number (int32)</code></td>
    <td>The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceManagementTroubleshootingEvents" /></td>
    <td><code>array</code></td>
    <td>The list of troubleshooting events for this user.</td>
</tr>
<tr>
    <td><CopyableCode code="directReports" /></td>
    <td><code>array</code></td>
    <td>The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and family name. This property is required when a user is created and it can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderby, and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="drive" /></td>
    <td><code></code></td>
    <td>The user's OneDrive. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="drives" /></td>
    <td><code>array</code></td>
    <td>A collection of drives available for this user. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="employeeExperience" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="employeeHireDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the user was hired or will start work in a future hire. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="employeeId" /></td>
    <td><code>string</code></td>
    <td>The employee identifier assigned to the user by the organization. The maximum length is 16 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="employeeLeaveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs at least one of the following Microsoft Entra roles: Lifecycle Workflows Administrator (least privilege), Global Reader. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="employeeOrgData" /></td>
    <td><code></code></td>
    <td>Represents organization data (for example, division and costCenter) associated with a user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in).</td>
</tr>
<tr>
    <td><CopyableCode code="employeeType" /></td>
    <td><code>string</code></td>
    <td>Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the user. Read-only. Supports $expand. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="externalUserState" /></td>
    <td><code>string</code></td>
    <td>For a guest invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Requires $select to retrieve. Supports $filter (eq, ne, not , in).</td>
</tr>
<tr>
    <td><CopyableCode code="externalUserStateChangeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shows the timestamp for the latest change to the externalUserState property. Requires $select to retrieve. Supports $filter (eq, ne, not , in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="faxNumber" /></td>
    <td><code>string</code></td>
    <td>The fax number of the user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="followedSites" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="givenName" /></td>
    <td><code>string</code></td>
    <td>The given name (first name) of the user. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="hireDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve.  Note: This property is specific to SharePoint in Microsoft 365. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="identities" /></td>
    <td><code>array</code></td>
    <td>Represents the identities that can be used to sign in to this user account. Microsoft (also known as a local account), organizations, or social identity providers such as Facebook, Google, and Microsoft can provide identity and tie it to a user account. It might contain multiple items with the same signInType value. Requires $select to retrieve.  Supports $filter (eq) with limitations.</td>
</tr>
<tr>
    <td><CopyableCode code="identityParentId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="imAddresses" /></td>
    <td><code>array</code></td>
    <td>The instant message voice-over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="inferenceClassification" /></td>
    <td><code></code></td>
    <td>Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code></code></td>
    <td>Represents relationships between a user and items such as OneDrive for work or school documents, calculated using advanced analytics and machine learning techniques. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="interests" /></td>
    <td><code>array</code></td>
    <td>A list for the user to describe their interests. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementRestricted" /></td>
    <td><code>boolean</code></td>
    <td>true if the user is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a user who is a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isResourceAccount" /></td>
    <td><code>boolean</code></td>
    <td>Don't use – reserved for future use.</td>
</tr>
<tr>
    <td><CopyableCode code="jobTitle" /></td>
    <td><code>string</code></td>
    <td>The user's job title. Maximum length is 128 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="joinedTeams" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lastPasswordChangeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when this Microsoft Entra user last changed their password or when their password was created, whichever date the latest action was performed. The date and time information uses ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="legalAgeGroupClassification" /></td>
    <td><code>string</code></td>
    <td>Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, Undefined,  MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseAssignmentStates" /></td>
    <td><code>array</code></td>
    <td>State of license assignments for this user. Also indicates licenses that are directly assigned or the user inherited through group memberships. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseDetails" /></td>
    <td><code>array</code></td>
    <td>A collection of this user's license details. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="mail" /></td>
    <td><code>string</code></td>
    <td>The SMTP address for the user, for example, jeff@contoso.com. Changes to this property update the user's proxyAddresses collection to include the value as an SMTP address. This property can't contain accent characters.  NOTE: We don't recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailFolders" /></td>
    <td><code>array</code></td>
    <td>The user's mail folders. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mailNickname" /></td>
    <td><code>string</code></td>
    <td>The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailboxSettings" /></td>
    <td><code></code></td>
    <td>Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="managedAppRegistrations" /></td>
    <td><code>array</code></td>
    <td>Zero or more managed app registrations that belong to the user.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDevices" /></td>
    <td><code>array</code></td>
    <td>The managed devices associated with the user.</td>
</tr>
<tr>
    <td><CopyableCode code="manager" /></td>
    <td><code></code></td>
    <td>The user or contact that is this user's manager. Read-only. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>The groups and directory roles that the user is a member of. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td>The messages in a mailbox or folder. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mobilePhone" /></td>
    <td><code>string</code></td>
    <td>The primary cellular telephone number for the user. Read-only for users synced from the on-premises directory. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="mySite" /></td>
    <td><code>string</code></td>
    <td>The URL for the user's site. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2PermissionGrants" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="officeLocation" /></td>
    <td><code>string</code></td>
    <td>The office location in the user's place of business. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDistinguishedName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDomainName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesExtensionAttributes" /></td>
    <td><code></code></td>
    <td>Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. Each attribute can store up to 1024 characters. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during the creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Requires $select to retrieve. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesImmutableId" /></td>
    <td><code>string</code></td>
    <td>This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object. This property must be specified when creating a new user account in the Graph if you're using a federated domain for the user's userPrincipalName (UPN) property. NOTE: The $ and _ characters can't be used when specifying this property. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last time at which the object was synced with the on-premises directory; for example: 2013-02-16T03:04:54Z. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors when using Microsoft synchronization product during provisioning. Requires $select to retrieve. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSamAccountName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Requires $select to retrieve. Supports $filter (eq including on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncBehavior" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Microsoft Entra ID. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesUserPrincipalName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="onenote" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onlineMeetings" /></td>
    <td><code>array</code></td>
    <td>Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.</td>
</tr>
<tr>
    <td><CopyableCode code="otherMails" /></td>
    <td><code>array</code></td>
    <td>A list of other email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. Can store up to 250 values, each with a limit of 250 characters. NOTE: This property can't contain accent characters. Requires $select to retrieve. Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="outlook" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ownedDevices" /></td>
    <td><code>array</code></td>
    <td>Devices the user owns. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).</td>
</tr>
<tr>
    <td><CopyableCode code="ownedObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects the user owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).</td>
</tr>
<tr>
    <td><CopyableCode code="passwordPolicies" /></td>
    <td><code>string</code></td>
    <td>Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two might be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. Requires $select to retrieve. For more information on the default password policies, see Microsoft Entra password policies. Supports $filter (ne, not, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="passwordProfile" /></td>
    <td><code></code></td>
    <td>Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). To update this property:  User-PasswordProfile.ReadWrite.All is the least privileged permission to update this property.  In delegated scenarios, the User Administrator Microsoft Entra role is the least privileged admin role supported to update this property for nonadmin users. Privileged Authentication Administrator is the least privileged role that's allowed to update this property for all administrators in the tenant. In general, the signed-in user must have a higher privileged administrator role as indicated in Who can reset passwords.  In app-only scenarios, the calling app must be assigned a supported permission and at least the User Administrator Microsoft Entra role.</td>
</tr>
<tr>
    <td><CopyableCode code="pastProjects" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their past projects. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="people" /></td>
    <td><code>array</code></td>
    <td>People that are relevant to the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionGrants" /></td>
    <td><code>array</code></td>
    <td>List all resource-specific permission grants of a user.</td>
</tr>
<tr>
    <td><CopyableCode code="photo" /></td>
    <td><code></code></td>
    <td>The user's profile photo. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="photos" /></td>
    <td><code>array</code></td>
    <td>The collection of the user's profile photos in different sizes. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="planner" /></td>
    <td><code></code></td>
    <td>Entry-point to the Planner resource that might exist for a user. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>The postal code for the user's postal address. The postal code is specific to the user's country or region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="preferredDataLocation" /></td>
    <td><code>string</code></td>
    <td>The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for the user. The preferred language format is based on RFC 4646. The name is a combination of an ISO 639 two-letter lowercase culture code associated with the language, and an ISO 3166 two-letter uppercase subculture code associated with the country or region. Example: 'en-US', or 'es-ES'. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values)</td>
</tr>
<tr>
    <td><CopyableCode code="preferredName" /></td>
    <td><code>string</code></td>
    <td>The preferred name for the user. Not Supported. This attribute returns an empty string.Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="presence" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="print" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provisionedPlans" /></td>
    <td><code>array</code></td>
    <td>The plans that are provisioned for the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAddresses" /></td>
    <td><code>array</code></td>
    <td>For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address, while those addresses prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of 10 unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="registeredDevices" /></td>
    <td><code>array</code></td>
    <td>Devices that are registered for the user. Read-only. Nullable. Supports $expand and returns up to 100 objects.</td>
</tr>
<tr>
    <td><CopyableCode code="responsibilities" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their responsibilities. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="schools" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate the schools they attended. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="scopedRoleMemberOf" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="securityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a user object.  Supports $filter (eq, not, for isResolved and serviceInstance).</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="showInAddressList" /></td>
    <td><code>boolean</code></td>
    <td>Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.</td>
</tr>
<tr>
    <td><CopyableCode code="signInActivity" /></td>
    <td><code></code></td>
    <td>Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note: Details for this property require a Microsoft Entra ID P1 or P2 license and the AuditLog.Read.All permission.This property isn't returned for a user who never signed in or last signed in before April 2020.</td>
</tr>
<tr>
    <td><CopyableCode code="signInSessionsValidFromDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Any refresh tokens or session tokens (session cookies) issued before this time are invalid. Applications get an error when using an invalid refresh or session token to acquire a delegated access token (to access APIs such as Microsoft Graph). If this happens, the application needs to acquire a new refresh token by requesting the authorized endpoint. Read-only. Use revokeSignInSessions to reset. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="skills" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their skills. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="solutions" /></td>
    <td><code></code></td>
    <td>The identifier that relates the user to the working time schedule triggers. Read-Only. Nullable</td>
</tr>
<tr>
    <td><CopyableCode code="sponsors" /></td>
    <td><code>array</code></td>
    <td>The users and groups responsible for this guest's privileges in the tenant and keeping the guest's information and access updated. (HTTP Methods: GET, POST, DELETE.). Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state or province in the user's address. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="streetAddress" /></td>
    <td><code>string</code></td>
    <td>The street address of the user's place of business. Maximum length is 1,024 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="surname" /></td>
    <td><code>string</code></td>
    <td>The user's surname (family name or last name). Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="teamwork" /></td>
    <td><code></code></td>
    <td>A container for Microsoft Teams features available for the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="todo" /></td>
    <td><code></code></td>
    <td>Represents the To Do services available to a user.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td>The groups, including nested groups, and directory roles that a user is a member of. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="usageLocation" /></td>
    <td><code>string</code></td>
    <td>A two-letter country code (ISO standard 3166). Required for users that are assigned licenses due to legal requirements to check for availability of services in countries/regions. Examples include: US, JP, and GB. Not nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name for the user based on the Internet standard RFC 822. By convention, this value should map to the user's email name. The general format is alias@domain, where the domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property can't contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="userType" /></td>
    <td><code>string</code></td>
    <td>A string value that can be used to classify user types in your directory. The possible values are Member and Guest. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for members and guests, see What are the default user permissions in Microsoft Entra ID?</td>
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
    <td><CopyableCode code="aboutMe" /></td>
    <td><code>string</code></td>
    <td>A freeform text entry field for the user to describe themselves. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="accountEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the account is enabled; otherwise, false. This property is required when a user is created. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="activities" /></td>
    <td><code>array</code></td>
    <td>The user's activities across devices. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="adhocCalls" /></td>
    <td><code>array</code></td>
    <td>Ad hoc calls associated with the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="ageGroup" /></td>
    <td><code>string</code></td>
    <td>Sets the age group of the user. Allowed values: null, Minor, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="agreementAcceptances" /></td>
    <td><code>array</code></td>
    <td>The user's terms of use acceptance statuses. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignments" /></td>
    <td><code>array</code></td>
    <td>Represents the app roles a user is granted for an application. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLicenses" /></td>
    <td><code>array</code></td>
    <td>The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate between directly assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly assigned and inherited licenses. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="assignedPlans" /></td>
    <td><code>array</code></td>
    <td>The plans that are assigned to the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq and not).</td>
</tr>
<tr>
    <td><CopyableCode code="authentication" /></td>
    <td><code></code></td>
    <td>The authentication methods that are supported for the user.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationInfo" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="birthday" /></td>
    <td><code>string (date-time)</code></td>
    <td>The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="businessPhones" /></td>
    <td><code>array</code></td>
    <td>The telephone numbers for the user. NOTE: Although it's a string collection, only one number can be set for this property. Read-only for users synced from the on-premises directory. Returned by default. Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="calendar" /></td>
    <td><code></code></td>
    <td>The user's primary calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarGroups" /></td>
    <td><code>array</code></td>
    <td>The user's calendar groups. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarView" /></td>
    <td><code>array</code></td>
    <td>The calendar view for the calendar. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="calendars" /></td>
    <td><code>array</code></td>
    <td>The user's calendars. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="chats" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>The city where the user is located. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="cloudClipboard" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloudPCs" /></td>
    <td><code>array</code></td>
    <td>The user's Cloud PCs. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="companyName" /></td>
    <td><code>string</code></td>
    <td>The name of the company that the user is associated with. This property can be useful for describing the company that a guest comes from. The maximum length is 64 characters.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="consentProvidedForMinor" /></td>
    <td><code>string</code></td>
    <td>Sets whether consent was obtained for minors. Allowed values: null, Granted, Denied, and NotRequired. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="contactFolders" /></td>
    <td><code>array</code></td>
    <td>The user's contacts folders. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="contacts" /></td>
    <td><code>array</code></td>
    <td>The user's contacts. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country or region where the user is located; for example, US or UK. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the user was created, in ISO 8601 format and UTC. The value can't be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Microsoft Entra ID. Property is null for some users created before June 2018 and on-premises users that were synced to Microsoft Entra ID before June 2018. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects that the user created. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="creationType" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by a guest signing up through a link that is part of a user flow (SelfServiceSignUp). Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="customSecurityAttributes" /></td>
    <td><code></code></td>
    <td>An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, startsWith). The filter value is case-sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSecurityAndGovernance" /></td>
    <td><code></code></td>
    <td>The data security and governance settings for the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="department" /></td>
    <td><code>string</code></td>
    <td>The name of the department in which the user works. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceEnrollmentLimit" /></td>
    <td><code>number (int32)</code></td>
    <td>The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceManagementTroubleshootingEvents" /></td>
    <td><code>array</code></td>
    <td>The list of troubleshooting events for this user.</td>
</tr>
<tr>
    <td><CopyableCode code="directReports" /></td>
    <td><code>array</code></td>
    <td>The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and family name. This property is required when a user is created and it can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderby, and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="drive" /></td>
    <td><code></code></td>
    <td>The user's OneDrive. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="drives" /></td>
    <td><code>array</code></td>
    <td>A collection of drives available for this user. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="employeeExperience" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="employeeHireDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the user was hired or will start work in a future hire. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="employeeId" /></td>
    <td><code>string</code></td>
    <td>The employee identifier assigned to the user by the organization. The maximum length is 16 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="employeeLeaveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs at least one of the following Microsoft Entra roles: Lifecycle Workflows Administrator (least privilege), Global Reader. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="employeeOrgData" /></td>
    <td><code></code></td>
    <td>Represents organization data (for example, division and costCenter) associated with a user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in).</td>
</tr>
<tr>
    <td><CopyableCode code="employeeType" /></td>
    <td><code>string</code></td>
    <td>Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the user. Read-only. Supports $expand. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="externalUserState" /></td>
    <td><code>string</code></td>
    <td>For a guest invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Requires $select to retrieve. Supports $filter (eq, ne, not , in).</td>
</tr>
<tr>
    <td><CopyableCode code="externalUserStateChangeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shows the timestamp for the latest change to the externalUserState property. Requires $select to retrieve. Supports $filter (eq, ne, not , in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="faxNumber" /></td>
    <td><code>string</code></td>
    <td>The fax number of the user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="followedSites" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="givenName" /></td>
    <td><code>string</code></td>
    <td>The given name (first name) of the user. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="hireDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve.  Note: This property is specific to SharePoint in Microsoft 365. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="identities" /></td>
    <td><code>array</code></td>
    <td>Represents the identities that can be used to sign in to this user account. Microsoft (also known as a local account), organizations, or social identity providers such as Facebook, Google, and Microsoft can provide identity and tie it to a user account. It might contain multiple items with the same signInType value. Requires $select to retrieve.  Supports $filter (eq) with limitations.</td>
</tr>
<tr>
    <td><CopyableCode code="identityParentId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="imAddresses" /></td>
    <td><code>array</code></td>
    <td>The instant message voice-over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="inferenceClassification" /></td>
    <td><code></code></td>
    <td>Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code></code></td>
    <td>Represents relationships between a user and items such as OneDrive for work or school documents, calculated using advanced analytics and machine learning techniques. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="interests" /></td>
    <td><code>array</code></td>
    <td>A list for the user to describe their interests. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementRestricted" /></td>
    <td><code>boolean</code></td>
    <td>true if the user is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a user who is a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isResourceAccount" /></td>
    <td><code>boolean</code></td>
    <td>Don't use – reserved for future use.</td>
</tr>
<tr>
    <td><CopyableCode code="jobTitle" /></td>
    <td><code>string</code></td>
    <td>The user's job title. Maximum length is 128 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="joinedTeams" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lastPasswordChangeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when this Microsoft Entra user last changed their password or when their password was created, whichever date the latest action was performed. The date and time information uses ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="legalAgeGroupClassification" /></td>
    <td><code>string</code></td>
    <td>Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, Undefined,  MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseAssignmentStates" /></td>
    <td><code>array</code></td>
    <td>State of license assignments for this user. Also indicates licenses that are directly assigned or the user inherited through group memberships. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseDetails" /></td>
    <td><code>array</code></td>
    <td>A collection of this user's license details. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="mail" /></td>
    <td><code>string</code></td>
    <td>The SMTP address for the user, for example, jeff@contoso.com. Changes to this property update the user's proxyAddresses collection to include the value as an SMTP address. This property can't contain accent characters.  NOTE: We don't recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailFolders" /></td>
    <td><code>array</code></td>
    <td>The user's mail folders. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mailNickname" /></td>
    <td><code>string</code></td>
    <td>The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailboxSettings" /></td>
    <td><code></code></td>
    <td>Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="managedAppRegistrations" /></td>
    <td><code>array</code></td>
    <td>Zero or more managed app registrations that belong to the user.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDevices" /></td>
    <td><code>array</code></td>
    <td>The managed devices associated with the user.</td>
</tr>
<tr>
    <td><CopyableCode code="manager" /></td>
    <td><code></code></td>
    <td>The user or contact that is this user's manager. Read-only. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>The groups and directory roles that the user is a member of. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td>The messages in a mailbox or folder. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mobilePhone" /></td>
    <td><code>string</code></td>
    <td>The primary cellular telephone number for the user. Read-only for users synced from the on-premises directory. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="mySite" /></td>
    <td><code>string</code></td>
    <td>The URL for the user's site. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2PermissionGrants" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="officeLocation" /></td>
    <td><code>string</code></td>
    <td>The office location in the user's place of business. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDistinguishedName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDomainName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesExtensionAttributes" /></td>
    <td><code></code></td>
    <td>Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. Each attribute can store up to 1024 characters. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during the creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Requires $select to retrieve. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesImmutableId" /></td>
    <td><code>string</code></td>
    <td>This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object. This property must be specified when creating a new user account in the Graph if you're using a federated domain for the user's userPrincipalName (UPN) property. NOTE: The $ and _ characters can't be used when specifying this property. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last time at which the object was synced with the on-premises directory; for example: 2013-02-16T03:04:54Z. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors when using Microsoft synchronization product during provisioning. Requires $select to retrieve. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSamAccountName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Requires $select to retrieve. Supports $filter (eq including on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncBehavior" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Microsoft Entra ID. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesUserPrincipalName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="onenote" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onlineMeetings" /></td>
    <td><code>array</code></td>
    <td>Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.</td>
</tr>
<tr>
    <td><CopyableCode code="otherMails" /></td>
    <td><code>array</code></td>
    <td>A list of other email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. Can store up to 250 values, each with a limit of 250 characters. NOTE: This property can't contain accent characters. Requires $select to retrieve. Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="outlook" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ownedDevices" /></td>
    <td><code>array</code></td>
    <td>Devices the user owns. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).</td>
</tr>
<tr>
    <td><CopyableCode code="ownedObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects the user owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).</td>
</tr>
<tr>
    <td><CopyableCode code="passwordPolicies" /></td>
    <td><code>string</code></td>
    <td>Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two might be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. Requires $select to retrieve. For more information on the default password policies, see Microsoft Entra password policies. Supports $filter (ne, not, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="passwordProfile" /></td>
    <td><code></code></td>
    <td>Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). To update this property:  User-PasswordProfile.ReadWrite.All is the least privileged permission to update this property.  In delegated scenarios, the User Administrator Microsoft Entra role is the least privileged admin role supported to update this property for nonadmin users. Privileged Authentication Administrator is the least privileged role that's allowed to update this property for all administrators in the tenant. In general, the signed-in user must have a higher privileged administrator role as indicated in Who can reset passwords.  In app-only scenarios, the calling app must be assigned a supported permission and at least the User Administrator Microsoft Entra role.</td>
</tr>
<tr>
    <td><CopyableCode code="pastProjects" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their past projects. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="people" /></td>
    <td><code>array</code></td>
    <td>People that are relevant to the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionGrants" /></td>
    <td><code>array</code></td>
    <td>List all resource-specific permission grants of a user.</td>
</tr>
<tr>
    <td><CopyableCode code="photo" /></td>
    <td><code></code></td>
    <td>The user's profile photo. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="photos" /></td>
    <td><code>array</code></td>
    <td>The collection of the user's profile photos in different sizes. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="planner" /></td>
    <td><code></code></td>
    <td>Entry-point to the Planner resource that might exist for a user. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>The postal code for the user's postal address. The postal code is specific to the user's country or region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="preferredDataLocation" /></td>
    <td><code>string</code></td>
    <td>The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for the user. The preferred language format is based on RFC 4646. The name is a combination of an ISO 639 two-letter lowercase culture code associated with the language, and an ISO 3166 two-letter uppercase subculture code associated with the country or region. Example: 'en-US', or 'es-ES'. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values)</td>
</tr>
<tr>
    <td><CopyableCode code="preferredName" /></td>
    <td><code>string</code></td>
    <td>The preferred name for the user. Not Supported. This attribute returns an empty string.Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="presence" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="print" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provisionedPlans" /></td>
    <td><code>array</code></td>
    <td>The plans that are provisioned for the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAddresses" /></td>
    <td><code>array</code></td>
    <td>For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address, while those addresses prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of 10 unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="registeredDevices" /></td>
    <td><code>array</code></td>
    <td>Devices that are registered for the user. Read-only. Nullable. Supports $expand and returns up to 100 objects.</td>
</tr>
<tr>
    <td><CopyableCode code="responsibilities" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their responsibilities. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="schools" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate the schools they attended. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="scopedRoleMemberOf" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="securityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a user object.  Supports $filter (eq, not, for isResolved and serviceInstance).</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="showInAddressList" /></td>
    <td><code>boolean</code></td>
    <td>Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.</td>
</tr>
<tr>
    <td><CopyableCode code="signInActivity" /></td>
    <td><code></code></td>
    <td>Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note: Details for this property require a Microsoft Entra ID P1 or P2 license and the AuditLog.Read.All permission.This property isn't returned for a user who never signed in or last signed in before April 2020.</td>
</tr>
<tr>
    <td><CopyableCode code="signInSessionsValidFromDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Any refresh tokens or session tokens (session cookies) issued before this time are invalid. Applications get an error when using an invalid refresh or session token to acquire a delegated access token (to access APIs such as Microsoft Graph). If this happens, the application needs to acquire a new refresh token by requesting the authorized endpoint. Read-only. Use revokeSignInSessions to reset. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="skills" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their skills. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="solutions" /></td>
    <td><code></code></td>
    <td>The identifier that relates the user to the working time schedule triggers. Read-Only. Nullable</td>
</tr>
<tr>
    <td><CopyableCode code="sponsors" /></td>
    <td><code>array</code></td>
    <td>The users and groups responsible for this guest's privileges in the tenant and keeping the guest's information and access updated. (HTTP Methods: GET, POST, DELETE.). Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state or province in the user's address. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="streetAddress" /></td>
    <td><code>string</code></td>
    <td>The street address of the user's place of business. Maximum length is 1,024 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="surname" /></td>
    <td><code>string</code></td>
    <td>The user's surname (family name or last name). Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="teamwork" /></td>
    <td><code></code></td>
    <td>A container for Microsoft Teams features available for the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="todo" /></td>
    <td><code></code></td>
    <td>Represents the To Do services available to a user.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td>The groups, including nested groups, and directory roles that a user is a member of. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="usageLocation" /></td>
    <td><code>string</code></td>
    <td>A two-letter country code (ISO standard 3166). Required for users that are assigned licenses due to legal requirements to check for availability of services in countries/regions. Examples include: US, JP, and GB. Not nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name for the user based on the Internet standard RFC 822. By convention, this value should map to the user's email name. The general format is alias@domain, where the domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property can't contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="userType" /></td>
    <td><code>string</code></td>
    <td>A string value that can be used to classify user types in your directory. The possible values are Member and Guest. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for members and guests, see What are the default user permissions in Microsoft Entra ID?</td>
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
    <td><CopyableCode code="aboutMe" /></td>
    <td><code>string</code></td>
    <td>A freeform text entry field for the user to describe themselves. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="accountEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the account is enabled; otherwise, false. This property is required when a user is created. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="activities" /></td>
    <td><code>array</code></td>
    <td>The user's activities across devices. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="adhocCalls" /></td>
    <td><code>array</code></td>
    <td>Ad hoc calls associated with the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="ageGroup" /></td>
    <td><code>string</code></td>
    <td>Sets the age group of the user. Allowed values: null, Minor, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="agreementAcceptances" /></td>
    <td><code>array</code></td>
    <td>The user's terms of use acceptance statuses. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignments" /></td>
    <td><code>array</code></td>
    <td>Represents the app roles a user is granted for an application. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLicenses" /></td>
    <td><code>array</code></td>
    <td>The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate between directly assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly assigned and inherited licenses. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="assignedPlans" /></td>
    <td><code>array</code></td>
    <td>The plans that are assigned to the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq and not).</td>
</tr>
<tr>
    <td><CopyableCode code="authentication" /></td>
    <td><code></code></td>
    <td>The authentication methods that are supported for the user.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationInfo" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="birthday" /></td>
    <td><code>string (date-time)</code></td>
    <td>The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="businessPhones" /></td>
    <td><code>array</code></td>
    <td>The telephone numbers for the user. NOTE: Although it's a string collection, only one number can be set for this property. Read-only for users synced from the on-premises directory. Returned by default. Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="calendar" /></td>
    <td><code></code></td>
    <td>The user's primary calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarGroups" /></td>
    <td><code>array</code></td>
    <td>The user's calendar groups. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarView" /></td>
    <td><code>array</code></td>
    <td>The calendar view for the calendar. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="calendars" /></td>
    <td><code>array</code></td>
    <td>The user's calendars. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="chats" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="city" /></td>
    <td><code>string</code></td>
    <td>The city where the user is located. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="cloudClipboard" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="cloudPCs" /></td>
    <td><code>array</code></td>
    <td>The user's Cloud PCs. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="companyName" /></td>
    <td><code>string</code></td>
    <td>The name of the company that the user is associated with. This property can be useful for describing the company that a guest comes from. The maximum length is 64 characters.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="consentProvidedForMinor" /></td>
    <td><code>string</code></td>
    <td>Sets whether consent was obtained for minors. Allowed values: null, Granted, Denied, and NotRequired. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).</td>
</tr>
<tr>
    <td><CopyableCode code="contactFolders" /></td>
    <td><code>array</code></td>
    <td>The user's contacts folders. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="contacts" /></td>
    <td><code>array</code></td>
    <td>The user's contacts. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>The country or region where the user is located; for example, US or UK. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time the user was created, in ISO 8601 format and UTC. The value can't be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Microsoft Entra ID. Property is null for some users created before June 2018 and on-premises users that were synced to Microsoft Entra ID before June 2018. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects that the user created. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="creationType" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by a guest signing up through a link that is part of a user flow (SelfServiceSignUp). Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="customSecurityAttributes" /></td>
    <td><code></code></td>
    <td>An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, startsWith). The filter value is case-sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSecurityAndGovernance" /></td>
    <td><code></code></td>
    <td>The data security and governance settings for the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="department" /></td>
    <td><code>string</code></td>
    <td>The name of the department in which the user works. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="deviceEnrollmentLimit" /></td>
    <td><code>number (int32)</code></td>
    <td>The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceManagementTroubleshootingEvents" /></td>
    <td><code>array</code></td>
    <td>The list of troubleshooting events for this user.</td>
</tr>
<tr>
    <td><CopyableCode code="directReports" /></td>
    <td><code>array</code></td>
    <td>The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and family name. This property is required when a user is created and it can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderby, and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="drive" /></td>
    <td><code></code></td>
    <td>The user's OneDrive. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="drives" /></td>
    <td><code>array</code></td>
    <td>A collection of drives available for this user. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="employeeExperience" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="employeeHireDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the user was hired or will start work in a future hire. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="employeeId" /></td>
    <td><code>string</code></td>
    <td>The employee identifier assigned to the user by the organization. The maximum length is 16 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="employeeLeaveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs at least one of the following Microsoft Entra roles: Lifecycle Workflows Administrator (least privilege), Global Reader. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="employeeOrgData" /></td>
    <td><code></code></td>
    <td>Represents organization data (for example, division and costCenter) associated with a user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in).</td>
</tr>
<tr>
    <td><CopyableCode code="employeeType" /></td>
    <td><code>string</code></td>
    <td>Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the user. Read-only. Supports $expand. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="externalUserState" /></td>
    <td><code>string</code></td>
    <td>For a guest invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Requires $select to retrieve. Supports $filter (eq, ne, not , in).</td>
</tr>
<tr>
    <td><CopyableCode code="externalUserStateChangeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shows the timestamp for the latest change to the externalUserState property. Requires $select to retrieve. Supports $filter (eq, ne, not , in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="faxNumber" /></td>
    <td><code>string</code></td>
    <td>The fax number of the user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="followedSites" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="givenName" /></td>
    <td><code>string</code></td>
    <td>The given name (first name) of the user. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="hireDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve.  Note: This property is specific to SharePoint in Microsoft 365. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="identities" /></td>
    <td><code>array</code></td>
    <td>Represents the identities that can be used to sign in to this user account. Microsoft (also known as a local account), organizations, or social identity providers such as Facebook, Google, and Microsoft can provide identity and tie it to a user account. It might contain multiple items with the same signInType value. Requires $select to retrieve.  Supports $filter (eq) with limitations.</td>
</tr>
<tr>
    <td><CopyableCode code="identityParentId" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="imAddresses" /></td>
    <td><code>array</code></td>
    <td>The instant message voice-over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="inferenceClassification" /></td>
    <td><code></code></td>
    <td>Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code></code></td>
    <td>Represents relationships between a user and items such as OneDrive for work or school documents, calculated using advanced analytics and machine learning techniques. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="interests" /></td>
    <td><code>array</code></td>
    <td>A list for the user to describe their interests. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementRestricted" /></td>
    <td><code>boolean</code></td>
    <td>true if the user is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a user who is a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isResourceAccount" /></td>
    <td><code>boolean</code></td>
    <td>Don't use – reserved for future use.</td>
</tr>
<tr>
    <td><CopyableCode code="jobTitle" /></td>
    <td><code>string</code></td>
    <td>The user's job title. Maximum length is 128 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="joinedTeams" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="lastPasswordChangeDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when this Microsoft Entra user last changed their password or when their password was created, whichever date the latest action was performed. The date and time information uses ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="legalAgeGroupClassification" /></td>
    <td><code>string</code></td>
    <td>Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, Undefined,  MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseAssignmentStates" /></td>
    <td><code>array</code></td>
    <td>State of license assignments for this user. Also indicates licenses that are directly assigned or the user inherited through group memberships. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="licenseDetails" /></td>
    <td><code>array</code></td>
    <td>A collection of this user's license details. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="mail" /></td>
    <td><code>string</code></td>
    <td>The SMTP address for the user, for example, jeff@contoso.com. Changes to this property update the user's proxyAddresses collection to include the value as an SMTP address. This property can't contain accent characters.  NOTE: We don't recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailFolders" /></td>
    <td><code>array</code></td>
    <td>The user's mail folders. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mailNickname" /></td>
    <td><code>string</code></td>
    <td>The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailboxSettings" /></td>
    <td><code></code></td>
    <td>Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="managedAppRegistrations" /></td>
    <td><code>array</code></td>
    <td>Zero or more managed app registrations that belong to the user.</td>
</tr>
<tr>
    <td><CopyableCode code="managedDevices" /></td>
    <td><code>array</code></td>
    <td>The managed devices associated with the user.</td>
</tr>
<tr>
    <td><CopyableCode code="manager" /></td>
    <td><code></code></td>
    <td>The user or contact that is this user's manager. Read-only. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>The groups and directory roles that the user is a member of. Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="messages" /></td>
    <td><code>array</code></td>
    <td>The messages in a mailbox or folder. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="mobilePhone" /></td>
    <td><code>string</code></td>
    <td>The primary cellular telephone number for the user. Read-only for users synced from the on-premises directory. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="mySite" /></td>
    <td><code>string</code></td>
    <td>The URL for the user's site. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="oauth2PermissionGrants" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="officeLocation" /></td>
    <td><code>string</code></td>
    <td>The office location in the user's place of business. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDistinguishedName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDomainName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesExtensionAttributes" /></td>
    <td><code></code></td>
    <td>Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. Each attribute can store up to 1024 characters. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during the creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Requires $select to retrieve. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesImmutableId" /></td>
    <td><code>string</code></td>
    <td>This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object. This property must be specified when creating a new user account in the Graph if you're using a federated domain for the user's userPrincipalName (UPN) property. NOTE: The $ and _ characters can't be used when specifying this property. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last time at which the object was synced with the on-premises directory; for example: 2013-02-16T03:04:54Z. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors when using Microsoft synchronization product during provisioning. Requires $select to retrieve. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSamAccountName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Requires $select to retrieve. Supports $filter (eq including on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncBehavior" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Microsoft Entra ID. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesUserPrincipalName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="onenote" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onlineMeetings" /></td>
    <td><code>array</code></td>
    <td>Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.</td>
</tr>
<tr>
    <td><CopyableCode code="otherMails" /></td>
    <td><code>array</code></td>
    <td>A list of other email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. Can store up to 250 values, each with a limit of 250 characters. NOTE: This property can't contain accent characters. Requires $select to retrieve. Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="outlook" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ownedDevices" /></td>
    <td><code>array</code></td>
    <td>Devices the user owns. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).</td>
</tr>
<tr>
    <td><CopyableCode code="ownedObjects" /></td>
    <td><code>array</code></td>
    <td>Directory objects the user owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).</td>
</tr>
<tr>
    <td><CopyableCode code="passwordPolicies" /></td>
    <td><code>string</code></td>
    <td>Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two might be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. Requires $select to retrieve. For more information on the default password policies, see Microsoft Entra password policies. Supports $filter (ne, not, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="passwordProfile" /></td>
    <td><code></code></td>
    <td>Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). To update this property:  User-PasswordProfile.ReadWrite.All is the least privileged permission to update this property.  In delegated scenarios, the User Administrator Microsoft Entra role is the least privileged admin role supported to update this property for nonadmin users. Privileged Authentication Administrator is the least privileged role that's allowed to update this property for all administrators in the tenant. In general, the signed-in user must have a higher privileged administrator role as indicated in Who can reset passwords.  In app-only scenarios, the calling app must be assigned a supported permission and at least the User Administrator Microsoft Entra role.</td>
</tr>
<tr>
    <td><CopyableCode code="pastProjects" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their past projects. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="people" /></td>
    <td><code>array</code></td>
    <td>People that are relevant to the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionGrants" /></td>
    <td><code>array</code></td>
    <td>List all resource-specific permission grants of a user.</td>
</tr>
<tr>
    <td><CopyableCode code="photo" /></td>
    <td><code></code></td>
    <td>The user's profile photo. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="photos" /></td>
    <td><code>array</code></td>
    <td>The collection of the user's profile photos in different sizes. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="planner" /></td>
    <td><code></code></td>
    <td>Entry-point to the Planner resource that might exist for a user. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="postalCode" /></td>
    <td><code>string</code></td>
    <td>The postal code for the user's postal address. The postal code is specific to the user's country or region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="preferredDataLocation" /></td>
    <td><code>string</code></td>
    <td>The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for the user. The preferred language format is based on RFC 4646. The name is a combination of an ISO 639 two-letter lowercase culture code associated with the language, and an ISO 3166 two-letter uppercase subculture code associated with the country or region. Example: 'en-US', or 'es-ES'. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values)</td>
</tr>
<tr>
    <td><CopyableCode code="preferredName" /></td>
    <td><code>string</code></td>
    <td>The preferred name for the user. Not Supported. This attribute returns an empty string.Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="presence" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="print" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="provisionedPlans" /></td>
    <td><code>array</code></td>
    <td>The plans that are provisioned for the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le).</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAddresses" /></td>
    <td><code>array</code></td>
    <td>For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address, while those addresses prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of 10 unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="registeredDevices" /></td>
    <td><code>array</code></td>
    <td>Devices that are registered for the user. Read-only. Nullable. Supports $expand and returns up to 100 objects.</td>
</tr>
<tr>
    <td><CopyableCode code="responsibilities" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their responsibilities. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="schools" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate the schools they attended. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="scopedRoleMemberOf" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="securityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a user object.  Supports $filter (eq, not, for isResolved and serviceInstance).</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="showInAddressList" /></td>
    <td><code>boolean</code></td>
    <td>Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.</td>
</tr>
<tr>
    <td><CopyableCode code="signInActivity" /></td>
    <td><code></code></td>
    <td>Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note: Details for this property require a Microsoft Entra ID P1 or P2 license and the AuditLog.Read.All permission.This property isn't returned for a user who never signed in or last signed in before April 2020.</td>
</tr>
<tr>
    <td><CopyableCode code="signInSessionsValidFromDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Any refresh tokens or session tokens (session cookies) issued before this time are invalid. Applications get an error when using an invalid refresh or session token to acquire a delegated access token (to access APIs such as Microsoft Graph). If this happens, the application needs to acquire a new refresh token by requesting the authorized endpoint. Read-only. Use revokeSignInSessions to reset. Requires $select to retrieve. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="skills" /></td>
    <td><code>array</code></td>
    <td>A list for the user to enumerate their skills. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="solutions" /></td>
    <td><code></code></td>
    <td>The identifier that relates the user to the working time schedule triggers. Read-Only. Nullable</td>
</tr>
<tr>
    <td><CopyableCode code="sponsors" /></td>
    <td><code>array</code></td>
    <td>The users and groups responsible for this guest's privileges in the tenant and keeping the guest's information and access updated. (HTTP Methods: GET, POST, DELETE.). Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state or province in the user's address. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="streetAddress" /></td>
    <td><code>string</code></td>
    <td>The street address of the user's place of business. Maximum length is 1,024 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="surname" /></td>
    <td><code>string</code></td>
    <td>The user's surname (family name or last name). Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="teamwork" /></td>
    <td><code></code></td>
    <td>A container for Microsoft Teams features available for the user. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="todo" /></td>
    <td><code></code></td>
    <td>Represents the To Do services available to a user.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td>The groups, including nested groups, and directory roles that a user is a member of. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="usageLocation" /></td>
    <td><code>string</code></td>
    <td>A two-letter country code (ISO standard 3166). Required for users that are assigned licenses due to legal requirements to check for availability of services in countries/regions. Examples include: US, JP, and GB. Not nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name for the user based on the Internet standard RFC 822. By convention, this value should map to the user's email name. The general format is alias@domain, where the domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property can't contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="userType" /></td>
    <td><code>string</code></td>
    <td>A string value that can be used to classify user types in your directory. The possible values are Member and Guest. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for members and guests, see What are the default user permissions in Microsoft Entra ID?</td>
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
    <td><a href="#parameter-userPrincipalName"><code>userPrincipalName</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of user objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new user.<br />The request body contains the user to create. At a minimum, you must specify the required properties for the user. You can optionally specify any other writable properties.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-userPrincipalName"><code>userPrincipalName</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a user object.</td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a user object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-userPrincipalName"><code>userPrincipalName</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a user object.   When deleted, user resources, including their mailbox and license assignments, are moved to a temporary container and if the user is restored within 30 days, these objects are restored to them. The user is also restored to any groups they were a member of. After 30 days and if not restored, the user object is permanently deleted and their assigned resources freed. To manage the deleted user object, see deletedItems.</td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a user object.   When deleted, user resources, including their mailbox and license assignments, are moved to a temporary container and if the user is restored within 30 days, these objects are restored to them. The user is also restored to any groups they were a member of. After 30 days and if not restored, the user object is permanently deleted and their assigned resources freed. To manage the deleted user object, see deletedItems.</td>
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
    <td><a href="#assign_license"><CopyableCode code="assign_license" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Add or remove licenses for the user to enable or disable their use of Microsoft cloud offerings that the company has licenses to. For example, an organization can have a Microsoft 365 Enterprise E3 subscription with 100 licenses, and this request assigns one of those licenses to a specific user. You can also enable and disable specific plans associated with a subscription. Direct user licensing method is an alternative to group-based licensing.</td>
</tr>
<tr>
    <td><a href="#check_member_groups"><CopyableCode code="check_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.</td>
</tr>
<tr>
    <td><a href="#check_member_objects"><CopyableCode code="check_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#export_personal_data"><CopyableCode code="export_personal_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Submit a data policy operation request from a company administrator or an application to export an organizational user's data. This data includes the user's data stored in OneDrive and their activity reports. For more information about exporting data while complying with regulations, see Data Subject Requests and the GDPR and CCPA.</td>
</tr>
<tr>
    <td><a href="#find_meeting_times"><CopyableCode code="find_meeting_times" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Suggest meeting times and locations based on organizer and attendee availability, and time or location constraints specified as parameters. If findMeetingTimes cannot return any meeting suggestions, the response would indicate a reason in the emptySuggestionsReason property.<br />Based on this value, you can better adjust the parameters and call findMeetingTimes again. The algorithm used to suggest meeting times and locations undergoes fine-tuning from time to time. In scenarios like test environments where the input parameters and calendar data remain static, expect that the suggested results may differ over time.</td>
</tr>
<tr>
    <td><a href="#get_mail_tips"><CopyableCode code="get_mail_tips" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Get the MailTips of one or more recipients as available to the signed-in user. Note that by making a POST call to the getMailTips action, you can request specific types of MailTips to<br />be returned for more than one recipient at one time. The requested MailTips are returned in a mailTips collection.</td>
</tr>
<tr>
    <td><a href="#get_member_groups"><CopyableCode code="get_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.</td>
</tr>
<tr>
    <td><a href="#get_member_objects"><CopyableCode code="get_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.</td>
</tr>
<tr>
    <td><a href="#remove_all_devices_from_management"><CopyableCode code="remove_all_devices_from_management" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Retire all devices from management for this user</td>
</tr>
<tr>
    <td><a href="#reprocess_license_assignment"><CopyableCode code="reprocess_license_assignment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Reprocess all group-based license assignments for the user. To learn more about group-based licensing, see What is group-based licensing in Microsoft Entra ID. Also see Identify and resolve license assignment problems for a group in Microsoft Entra ID for more details.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.</td>
</tr>
<tr>
    <td><a href="#retry_service_provisioning"><CopyableCode code="retry_service_provisioning" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Retry the provisioning of a user object in Microsoft Entra ID.</td>
</tr>
<tr>
    <td><a href="#revoke_sign_in_sessions"><CopyableCode code="revoke_sign_in_sessions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Invalidates all the refresh tokens issued to applications for a user (and session cookies in a user's browser), by resetting the signInSessionsValidFromDateTime user property to the current date-time. Typically, this operation is performed (by the user or an administrator) if the user has a lost or stolen device. This operation prevents access to the organization's data through applications on the device by requiring the user to sign in again to all applications that they consented to previously, independent of device.</td>
</tr>
<tr>
    <td><a href="#send_mail"><CopyableCode code="send_mail" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Send the message specified in the request body using either JSON or MIME format. When using JSON format, you can include a file attachment in the same sendMail action call. When using MIME format: This method saves the message in the Sent Items folder. Alternatively, create a draft message to send later. To learn more about the steps involved in the backend before a mail is delivered to recipients, see here.</td>
</tr>
<tr>
    <td><a href="#wipe_managed_app_registrations_by_device_tag"><CopyableCode code="wipe_managed_app_registrations_by_device_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-user-id"><code>user-id</code></a></td>
    <td></td>
    <td>Issues a wipe operation on an app registration with specified device tag.</td>
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
<tr id="parameter-user-id">
    <td><CopyableCode code="user-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of user</td>
</tr>
<tr id="parameter-userPrincipalName">
    <td><CopyableCode code="userPrincipalName" /></td>
    <td><code>string</code></td>
    <td>Alternate key of user</td>
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

Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.

```sql
SELECT
id,
@odata.type,
aboutMe,
accountEnabled,
activities,
adhocCalls,
ageGroup,
agreementAcceptances,
appRoleAssignments,
assignedLicenses,
assignedPlans,
authentication,
authorizationInfo,
birthday,
businessPhones,
calendar,
calendarGroups,
calendarView,
calendars,
chats,
city,
cloudClipboard,
cloudPCs,
companyName,
consentProvidedForMinor,
contactFolders,
contacts,
country,
createdDateTime,
createdObjects,
creationType,
customSecurityAttributes,
dataSecurityAndGovernance,
deletedDateTime,
department,
deviceEnrollmentLimit,
deviceManagementTroubleshootingEvents,
directReports,
displayName,
drive,
drives,
employeeExperience,
employeeHireDate,
employeeId,
employeeLeaveDateTime,
employeeOrgData,
employeeType,
events,
extensions,
externalUserState,
externalUserStateChangeDateTime,
faxNumber,
followedSites,
givenName,
hireDate,
identities,
identityParentId,
imAddresses,
inferenceClassification,
insights,
interests,
isManagementRestricted,
isResourceAccount,
jobTitle,
joinedTeams,
lastPasswordChangeDateTime,
legalAgeGroupClassification,
licenseAssignmentStates,
licenseDetails,
mail,
mailFolders,
mailNickname,
mailboxSettings,
managedAppRegistrations,
managedDevices,
manager,
memberOf,
messages,
mobilePhone,
mySite,
oauth2PermissionGrants,
officeLocation,
onPremisesDistinguishedName,
onPremisesDomainName,
onPremisesExtensionAttributes,
onPremisesImmutableId,
onPremisesLastSyncDateTime,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onPremisesUserPrincipalName,
onenote,
onlineMeetings,
otherMails,
outlook,
ownedDevices,
ownedObjects,
passwordPolicies,
passwordProfile,
pastProjects,
people,
permissionGrants,
photo,
photos,
planner,
postalCode,
preferredDataLocation,
preferredLanguage,
preferredName,
presence,
print,
provisionedPlans,
proxyAddresses,
registeredDevices,
responsibilities,
schools,
scopedRoleMemberOf,
securityIdentifier,
serviceProvisioningErrors,
settings,
showInAddressList,
signInActivity,
signInSessionsValidFromDateTime,
skills,
solutions,
sponsors,
state,
streetAddress,
surname,
teamwork,
todo,
transitiveMemberOf,
usageLocation,
userPrincipalName,
userType
FROM entra_id.users.users
WHERE userPrincipalName = '{{ userPrincipalName }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_2">

Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.

```sql
SELECT
id,
@odata.type,
aboutMe,
accountEnabled,
activities,
adhocCalls,
ageGroup,
agreementAcceptances,
appRoleAssignments,
assignedLicenses,
assignedPlans,
authentication,
authorizationInfo,
birthday,
businessPhones,
calendar,
calendarGroups,
calendarView,
calendars,
chats,
city,
cloudClipboard,
cloudPCs,
companyName,
consentProvidedForMinor,
contactFolders,
contacts,
country,
createdDateTime,
createdObjects,
creationType,
customSecurityAttributes,
dataSecurityAndGovernance,
deletedDateTime,
department,
deviceEnrollmentLimit,
deviceManagementTroubleshootingEvents,
directReports,
displayName,
drive,
drives,
employeeExperience,
employeeHireDate,
employeeId,
employeeLeaveDateTime,
employeeOrgData,
employeeType,
events,
extensions,
externalUserState,
externalUserStateChangeDateTime,
faxNumber,
followedSites,
givenName,
hireDate,
identities,
identityParentId,
imAddresses,
inferenceClassification,
insights,
interests,
isManagementRestricted,
isResourceAccount,
jobTitle,
joinedTeams,
lastPasswordChangeDateTime,
legalAgeGroupClassification,
licenseAssignmentStates,
licenseDetails,
mail,
mailFolders,
mailNickname,
mailboxSettings,
managedAppRegistrations,
managedDevices,
manager,
memberOf,
messages,
mobilePhone,
mySite,
oauth2PermissionGrants,
officeLocation,
onPremisesDistinguishedName,
onPremisesDomainName,
onPremisesExtensionAttributes,
onPremisesImmutableId,
onPremisesLastSyncDateTime,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onPremisesUserPrincipalName,
onenote,
onlineMeetings,
otherMails,
outlook,
ownedDevices,
ownedObjects,
passwordPolicies,
passwordProfile,
pastProjects,
people,
permissionGrants,
photo,
photos,
planner,
postalCode,
preferredDataLocation,
preferredLanguage,
preferredName,
presence,
print,
provisionedPlans,
proxyAddresses,
registeredDevices,
responsibilities,
schools,
scopedRoleMemberOf,
securityIdentifier,
serviceProvisioningErrors,
settings,
showInAddressList,
signInActivity,
signInSessionsValidFromDateTime,
skills,
solutions,
sponsors,
state,
streetAddress,
surname,
teamwork,
todo,
transitiveMemberOf,
usageLocation,
userPrincipalName,
userType
FROM entra_id.users.users
WHERE user-id = '{{ user-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of user objects.

```sql
SELECT
id,
@odata.type,
aboutMe,
accountEnabled,
activities,
adhocCalls,
ageGroup,
agreementAcceptances,
appRoleAssignments,
assignedLicenses,
assignedPlans,
authentication,
authorizationInfo,
birthday,
businessPhones,
calendar,
calendarGroups,
calendarView,
calendars,
chats,
city,
cloudClipboard,
cloudPCs,
companyName,
consentProvidedForMinor,
contactFolders,
contacts,
country,
createdDateTime,
createdObjects,
creationType,
customSecurityAttributes,
dataSecurityAndGovernance,
deletedDateTime,
department,
deviceEnrollmentLimit,
deviceManagementTroubleshootingEvents,
directReports,
displayName,
drive,
drives,
employeeExperience,
employeeHireDate,
employeeId,
employeeLeaveDateTime,
employeeOrgData,
employeeType,
events,
extensions,
externalUserState,
externalUserStateChangeDateTime,
faxNumber,
followedSites,
givenName,
hireDate,
identities,
identityParentId,
imAddresses,
inferenceClassification,
insights,
interests,
isManagementRestricted,
isResourceAccount,
jobTitle,
joinedTeams,
lastPasswordChangeDateTime,
legalAgeGroupClassification,
licenseAssignmentStates,
licenseDetails,
mail,
mailFolders,
mailNickname,
mailboxSettings,
managedAppRegistrations,
managedDevices,
manager,
memberOf,
messages,
mobilePhone,
mySite,
oauth2PermissionGrants,
officeLocation,
onPremisesDistinguishedName,
onPremisesDomainName,
onPremisesExtensionAttributes,
onPremisesImmutableId,
onPremisesLastSyncDateTime,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onPremisesUserPrincipalName,
onenote,
onlineMeetings,
otherMails,
outlook,
ownedDevices,
ownedObjects,
passwordPolicies,
passwordProfile,
pastProjects,
people,
permissionGrants,
photo,
photos,
planner,
postalCode,
preferredDataLocation,
preferredLanguage,
preferredName,
presence,
print,
provisionedPlans,
proxyAddresses,
registeredDevices,
responsibilities,
schools,
scopedRoleMemberOf,
securityIdentifier,
serviceProvisioningErrors,
settings,
showInAddressList,
signInActivity,
signInSessionsValidFromDateTime,
skills,
solutions,
sponsors,
state,
streetAddress,
surname,
teamwork,
todo,
transitiveMemberOf,
usageLocation,
userPrincipalName,
userType
FROM entra_id.users.users
WHERE ConsistencyLevel = '{{ ConsistencyLevel }}'
AND $top = '{{ $top }}'
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

Create a new user.<br />The request body contains the user to create. At a minimum, you must specify the required properties for the user. You can optionally specify any other writable properties.

```sql
INSERT INTO entra_id.users.users (
id,
@odata.type,
deletedDateTime,
aboutMe,
accountEnabled,
ageGroup,
assignedLicenses,
assignedPlans,
authorizationInfo,
birthday,
businessPhones,
city,
companyName,
consentProvidedForMinor,
country,
createdDateTime,
creationType,
customSecurityAttributes,
department,
deviceEnrollmentLimit,
displayName,
employeeHireDate,
employeeId,
employeeLeaveDateTime,
employeeOrgData,
employeeType,
externalUserState,
externalUserStateChangeDateTime,
faxNumber,
givenName,
hireDate,
identities,
identityParentId,
imAddresses,
interests,
isManagementRestricted,
isResourceAccount,
jobTitle,
lastPasswordChangeDateTime,
legalAgeGroupClassification,
licenseAssignmentStates,
mail,
mailboxSettings,
mailNickname,
mobilePhone,
mySite,
officeLocation,
onPremisesDistinguishedName,
onPremisesDomainName,
onPremisesExtensionAttributes,
onPremisesImmutableId,
onPremisesLastSyncDateTime,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncEnabled,
onPremisesUserPrincipalName,
otherMails,
passwordPolicies,
passwordProfile,
pastProjects,
postalCode,
preferredDataLocation,
preferredLanguage,
preferredName,
print,
provisionedPlans,
proxyAddresses,
responsibilities,
schools,
securityIdentifier,
serviceProvisioningErrors,
showInAddressList,
signInActivity,
signInSessionsValidFromDateTime,
skills,
state,
streetAddress,
surname,
usageLocation,
userPrincipalName,
userType,
activities,
adhocCalls,
agreementAcceptances,
appRoleAssignments,
authentication,
calendar,
calendarGroups,
calendars,
calendarView,
chats,
cloudClipboard,
cloudPCs,
contactFolders,
contacts,
createdObjects,
dataSecurityAndGovernance,
deviceManagementTroubleshootingEvents,
directReports,
drive,
drives,
employeeExperience,
events,
extensions,
followedSites,
inferenceClassification,
insights,
joinedTeams,
licenseDetails,
mailFolders,
managedAppRegistrations,
managedDevices,
manager,
memberOf,
messages,
oauth2PermissionGrants,
onenote,
onlineMeetings,
onPremisesSyncBehavior,
outlook,
ownedDevices,
ownedObjects,
people,
permissionGrants,
photo,
photos,
planner,
presence,
registeredDevices,
scopedRoleMemberOf,
settings,
solutions,
sponsors,
teamwork,
todo,
transitiveMemberOf
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
'{{ aboutMe }}',
{{ accountEnabled }},
'{{ ageGroup }}',
'{{ assignedLicenses }}',
'{{ assignedPlans }}',
'{{ authorizationInfo }}',
'{{ birthday }}',
'{{ businessPhones }}',
'{{ city }}',
'{{ companyName }}',
'{{ consentProvidedForMinor }}',
'{{ country }}',
'{{ createdDateTime }}',
'{{ creationType }}',
'{{ customSecurityAttributes }}',
'{{ department }}',
{{ deviceEnrollmentLimit }},
'{{ displayName }}',
'{{ employeeHireDate }}',
'{{ employeeId }}',
'{{ employeeLeaveDateTime }}',
'{{ employeeOrgData }}',
'{{ employeeType }}',
'{{ externalUserState }}',
'{{ externalUserStateChangeDateTime }}',
'{{ faxNumber }}',
'{{ givenName }}',
'{{ hireDate }}',
'{{ identities }}',
'{{ identityParentId }}',
'{{ imAddresses }}',
'{{ interests }}',
{{ isManagementRestricted }},
{{ isResourceAccount }},
'{{ jobTitle }}',
'{{ lastPasswordChangeDateTime }}',
'{{ legalAgeGroupClassification }}',
'{{ licenseAssignmentStates }}',
'{{ mail }}',
'{{ mailboxSettings }}',
'{{ mailNickname }}',
'{{ mobilePhone }}',
'{{ mySite }}',
'{{ officeLocation }}',
'{{ onPremisesDistinguishedName }}',
'{{ onPremisesDomainName }}',
'{{ onPremisesExtensionAttributes }}',
'{{ onPremisesImmutableId }}',
'{{ onPremisesLastSyncDateTime }}',
'{{ onPremisesProvisioningErrors }}',
'{{ onPremisesSamAccountName }}',
'{{ onPremisesSecurityIdentifier }}',
{{ onPremisesSyncEnabled }},
'{{ onPremisesUserPrincipalName }}',
'{{ otherMails }}',
'{{ passwordPolicies }}',
'{{ passwordProfile }}',
'{{ pastProjects }}',
'{{ postalCode }}',
'{{ preferredDataLocation }}',
'{{ preferredLanguage }}',
'{{ preferredName }}',
'{{ print }}',
'{{ provisionedPlans }}',
'{{ proxyAddresses }}',
'{{ responsibilities }}',
'{{ schools }}',
'{{ securityIdentifier }}',
'{{ serviceProvisioningErrors }}',
{{ showInAddressList }},
'{{ signInActivity }}',
'{{ signInSessionsValidFromDateTime }}',
'{{ skills }}',
'{{ state }}',
'{{ streetAddress }}',
'{{ surname }}',
'{{ usageLocation }}',
'{{ userPrincipalName }}',
'{{ userType }}',
'{{ activities }}',
'{{ adhocCalls }}',
'{{ agreementAcceptances }}',
'{{ appRoleAssignments }}',
'{{ authentication }}',
'{{ calendar }}',
'{{ calendarGroups }}',
'{{ calendars }}',
'{{ calendarView }}',
'{{ chats }}',
'{{ cloudClipboard }}',
'{{ cloudPCs }}',
'{{ contactFolders }}',
'{{ contacts }}',
'{{ createdObjects }}',
'{{ dataSecurityAndGovernance }}',
'{{ deviceManagementTroubleshootingEvents }}',
'{{ directReports }}',
'{{ drive }}',
'{{ drives }}',
'{{ employeeExperience }}',
'{{ events }}',
'{{ extensions }}',
'{{ followedSites }}',
'{{ inferenceClassification }}',
'{{ insights }}',
'{{ joinedTeams }}',
'{{ licenseDetails }}',
'{{ mailFolders }}',
'{{ managedAppRegistrations }}',
'{{ managedDevices }}',
'{{ manager }}',
'{{ memberOf }}',
'{{ messages }}',
'{{ oauth2PermissionGrants }}',
'{{ onenote }}',
'{{ onlineMeetings }}',
'{{ onPremisesSyncBehavior }}',
'{{ outlook }}',
'{{ ownedDevices }}',
'{{ ownedObjects }}',
'{{ people }}',
'{{ permissionGrants }}',
'{{ photo }}',
'{{ photos }}',
'{{ planner }}',
'{{ presence }}',
'{{ registeredDevices }}',
'{{ scopedRoleMemberOf }}',
'{{ settings }}',
'{{ solutions }}',
'{{ sponsors }}',
'{{ teamwork }}',
'{{ todo }}',
'{{ transitiveMemberOf }}'
RETURNING
id,
@odata.type,
aboutMe,
accountEnabled,
activities,
adhocCalls,
ageGroup,
agreementAcceptances,
appRoleAssignments,
assignedLicenses,
assignedPlans,
authentication,
authorizationInfo,
birthday,
businessPhones,
calendar,
calendarGroups,
calendarView,
calendars,
chats,
city,
cloudClipboard,
cloudPCs,
companyName,
consentProvidedForMinor,
contactFolders,
contacts,
country,
createdDateTime,
createdObjects,
creationType,
customSecurityAttributes,
dataSecurityAndGovernance,
deletedDateTime,
department,
deviceEnrollmentLimit,
deviceManagementTroubleshootingEvents,
directReports,
displayName,
drive,
drives,
employeeExperience,
employeeHireDate,
employeeId,
employeeLeaveDateTime,
employeeOrgData,
employeeType,
events,
extensions,
externalUserState,
externalUserStateChangeDateTime,
faxNumber,
followedSites,
givenName,
hireDate,
identities,
identityParentId,
imAddresses,
inferenceClassification,
insights,
interests,
isManagementRestricted,
isResourceAccount,
jobTitle,
joinedTeams,
lastPasswordChangeDateTime,
legalAgeGroupClassification,
licenseAssignmentStates,
licenseDetails,
mail,
mailFolders,
mailNickname,
mailboxSettings,
managedAppRegistrations,
managedDevices,
manager,
memberOf,
messages,
mobilePhone,
mySite,
oauth2PermissionGrants,
officeLocation,
onPremisesDistinguishedName,
onPremisesDomainName,
onPremisesExtensionAttributes,
onPremisesImmutableId,
onPremisesLastSyncDateTime,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onPremisesUserPrincipalName,
onenote,
onlineMeetings,
otherMails,
outlook,
ownedDevices,
ownedObjects,
passwordPolicies,
passwordProfile,
pastProjects,
people,
permissionGrants,
photo,
photos,
planner,
postalCode,
preferredDataLocation,
preferredLanguage,
preferredName,
presence,
print,
provisionedPlans,
proxyAddresses,
registeredDevices,
responsibilities,
schools,
scopedRoleMemberOf,
securityIdentifier,
serviceProvisioningErrors,
settings,
showInAddressList,
signInActivity,
signInSessionsValidFromDateTime,
skills,
solutions,
sponsors,
state,
streetAddress,
surname,
teamwork,
todo,
transitiveMemberOf,
usageLocation,
userPrincipalName,
userType
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: users
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
    - name: aboutMe
      value: "{{ aboutMe }}"
      description: |
        A freeform text entry field for the user to describe themselves. Requires $select to retrieve.
    - name: accountEnabled
      value: {{ accountEnabled }}
      description: |
        true if the account is enabled; otherwise, false. This property is required when a user is created. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).
    - name: ageGroup
      value: "{{ ageGroup }}"
      description: |
        Sets the age group of the user. Allowed values: null, Minor, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).
    - name: assignedLicenses
      description: |
        The licenses that are assigned to the user, including inherited (group-based) licenses. This property doesn't differentiate between directly assigned and inherited licenses. Use the licenseAssignmentStates property to identify the directly assigned and inherited licenses. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, /$count eq 0, /$count ne 0).
      value:
        - disabledPlans: "{{ disabledPlans }}"
          skuId: "{{ skuId }}"
          @odata.type: "{{ @odata.type }}"
    - name: assignedPlans
      description: |
        The plans that are assigned to the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq and not).
      value:
        - assignedDateTime: "{{ assignedDateTime }}"
          capabilityStatus: "{{ capabilityStatus }}"
          service: "{{ service }}"
          servicePlanId: "{{ servicePlanId }}"
          @odata.type: "{{ @odata.type }}"
    - name: authorizationInfo
      value: "{{ authorizationInfo }}"
    - name: birthday
      value: "{{ birthday }}"
      description: |
        The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve.
    - name: businessPhones
      value:
        - "{{ businessPhones }}"
      description: |
        The telephone numbers for the user. NOTE: Although it's a string collection, only one number can be set for this property. Read-only for users synced from the on-premises directory. Returned by default. Supports $filter (eq, not, ge, le, startsWith).
    - name: city
      value: "{{ city }}"
      description: |
        The city where the user is located. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: companyName
      value: "{{ companyName }}"
      description: |
        The name of the company that the user is associated with. This property can be useful for describing the company that a guest comes from. The maximum length is 64 characters.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: consentProvidedForMinor
      value: "{{ consentProvidedForMinor }}"
      description: |
        Sets whether consent was obtained for minors. Allowed values: null, Granted, Denied, and NotRequired. For more information, see legal age group property definitions. Requires $select to retrieve. Supports $filter (eq, ne, not, and in).
    - name: country
      value: "{{ country }}"
      description: |
        The country or region where the user is located; for example, US or UK. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The date and time the user was created, in ISO 8601 format and UTC. The value can't be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Microsoft Entra ID. Property is null for some users created before June 2018 and on-premises users that were synced to Microsoft Entra ID before June 2018. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in).
    - name: creationType
      value: "{{ creationType }}"
      description: |
        Indicates whether the user account was created through one of the following methods:  As a regular school or work account (null). As an external account (Invitation). As a local account for an Azure Active Directory B2C tenant (LocalAccount). Through self-service sign-up by an internal user using email verification (EmailVerified). Through self-service sign-up by a guest signing up through a link that is part of a user flow (SelfServiceSignUp). Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, in).
    - name: customSecurityAttributes
      value: "{{ customSecurityAttributes }}"
      description: |
        An open complex type that holds the value of a custom security attribute that is assigned to a directory object. Nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, startsWith). The filter value is case-sensitive. To read this property, the calling app must be assigned the CustomSecAttributeAssignment.Read.All permission. To write this property, the calling app must be assigned the CustomSecAttributeAssignment.ReadWrite.All permissions. To read or write this property in delegated scenarios, the admin must be assigned the Attribute Assignment Administrator role.
    - name: department
      value: "{{ department }}"
      description: |
        The name of the department in which the user works. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, and eq on null values).
    - name: deviceEnrollmentLimit
      value: {{ deviceEnrollmentLimit }}
      description: |
        The limit on the maximum number of devices that the user is permitted to enroll. Allowed values are 5 or 1000.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The name displayed in the address book for the user. This value is usually the combination of the user's first name, middle initial, and family name. This property is required when a user is created and it can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values), $orderby, and $search.
    - name: employeeHireDate
      value: "{{ employeeHireDate }}"
      description: |
        The date and time when the user was hired or will start work in a future hire. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in).
    - name: employeeId
      value: "{{ employeeId }}"
      description: |
        The employee identifier assigned to the user by the organization. The maximum length is 16 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    - name: employeeLeaveDateTime
      value: "{{ employeeLeaveDateTime }}"
      description: |
        The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs at least one of the following Microsoft Entra roles: Lifecycle Workflows Administrator (least privilege), Global Reader. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user.
    - name: employeeOrgData
      value: "{{ employeeOrgData }}"
      description: |
        Represents organization data (for example, division and costCenter) associated with a user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in).
    - name: employeeType
      value: "{{ employeeType }}"
      description: |
        Captures enterprise worker type. For example, Employee, Contractor, Consultant, or Vendor. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith).
    - name: externalUserState
      value: "{{ externalUserState }}"
      description: |
        For a guest invited to the tenant using the invitation API, this property represents the invited user's invitation status. For invited users, the state can be PendingAcceptance or Accepted, or null for all other users. Requires $select to retrieve. Supports $filter (eq, ne, not , in).
    - name: externalUserStateChangeDateTime
      value: "{{ externalUserStateChangeDateTime }}"
      description: |
        Shows the timestamp for the latest change to the externalUserState property. Requires $select to retrieve. Supports $filter (eq, ne, not , in).
    - name: faxNumber
      value: "{{ faxNumber }}"
      description: |
        The fax number of the user. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    - name: givenName
      value: "{{ givenName }}"
      description: |
        The given name (first name) of the user. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    - name: hireDate
      value: "{{ hireDate }}"
      description: |
        The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve.  Note: This property is specific to SharePoint in Microsoft 365. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs.
    - name: identities
      description: |
        Represents the identities that can be used to sign in to this user account. Microsoft (also known as a local account), organizations, or social identity providers such as Facebook, Google, and Microsoft can provide identity and tie it to a user account. It might contain multiple items with the same signInType value. Requires $select to retrieve.  Supports $filter (eq) with limitations.
      value:
        - issuer: "{{ issuer }}"
          issuerAssignedId: "{{ issuerAssignedId }}"
          signInType: "{{ signInType }}"
          @odata.type: "{{ @odata.type }}"
    - name: identityParentId
      value: "{{ identityParentId }}"
    - name: imAddresses
      value:
        - "{{ imAddresses }}"
      description: |
        The instant message voice-over IP (VOIP) session initiation protocol (SIP) addresses for the user. Read-only. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith).
    - name: interests
      value:
        - "{{ interests }}"
      description: |
        A list for the user to describe their interests. Requires $select to retrieve.
    - name: isManagementRestricted
      value: {{ isManagementRestricted }}
      description: |
        true if the user is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a user who is a member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.
    - name: isResourceAccount
      value: {{ isResourceAccount }}
      description: |
        Don't use – reserved for future use.
    - name: jobTitle
      value: "{{ jobTitle }}"
      description: |
        The user's job title. Maximum length is 128 characters. Returned by default. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).
    - name: lastPasswordChangeDateTime
      value: "{{ lastPasswordChangeDateTime }}"
      description: |
        The time when this Microsoft Entra user last changed their password or when their password was created, whichever date the latest action was performed. The date and time information uses ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Requires $select to retrieve.
    - name: legalAgeGroupClassification
      value: "{{ legalAgeGroupClassification }}"
      description: |
        Used by enterprise applications to determine the legal age group of the user. This property is read-only and calculated based on ageGroup and consentProvidedForMinor properties. Allowed values: null, Undefined,  MinorWithOutParentalConsent, MinorWithParentalConsent, MinorNoParentalConsentRequired, NotAdult, and Adult. For more information, see legal age group property definitions. Requires $select to retrieve.
    - name: licenseAssignmentStates
      description: |
        State of license assignments for this user. Also indicates licenses that are directly assigned or the user inherited through group memberships. Read-only. Requires $select to retrieve.
      value:
        - assignedByGroup: "{{ assignedByGroup }}"
          disabledPlans: "{{ disabledPlans }}"
          error: "{{ error }}"
          lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
          skuId: "{{ skuId }}"
          state: "{{ state }}"
          @odata.type: "{{ @odata.type }}"
    - name: mail
      value: "{{ mail }}"
      description: |
        The SMTP address for the user, for example, jeff@contoso.com. Changes to this property update the user's proxyAddresses collection to include the value as an SMTP address. This property can't contain accent characters.  NOTE: We don't recommend updating this property for Azure AD B2C user profiles. Use the otherMails property instead. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith, and eq on null values).
    - name: mailboxSettings
      value: "{{ mailboxSettings }}"
      description: |
        Settings for the primary mailbox of the signed-in user. You can get or update settings for sending automatic replies to incoming messages, locale, and time zone. Requires $select to retrieve.
    - name: mailNickname
      value: "{{ mailNickname }}"
      description: |
        The mail alias for the user. This property must be specified when a user is created. Maximum length is 64 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: mobilePhone
      value: "{{ mobilePhone }}"
      description: |
        The primary cellular telephone number for the user. Read-only for users synced from the on-premises directory. Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values) and $search.
    - name: mySite
      value: "{{ mySite }}"
      description: |
        The URL for the user's site. Requires $select to retrieve.
    - name: officeLocation
      value: "{{ officeLocation }}"
      description: |
        The office location in the user's place of business. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: onPremisesDistinguishedName
      value: "{{ onPremisesDistinguishedName }}"
      description: |
        Contains the on-premises Active Directory distinguished name or DN. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.
    - name: onPremisesDomainName
      value: "{{ onPremisesDomainName }}"
      description: |
        Contains the on-premises domainFQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve.
    - name: onPremisesExtensionAttributes
      value: "{{ onPremisesExtensionAttributes }}"
      description: |
        Contains extensionAttributes1-15 for the user. These extension attributes are also known as Exchange custom attributes 1-15. Each attribute can store up to 1024 characters. For an onPremisesSyncEnabled user, the source of authority for this set of properties is the on-premises and is read-only. For a cloud-only user (where onPremisesSyncEnabled is false), these properties can be set during the creation or update of a user object.  For a cloud-only user previously synced from on-premises Active Directory, these properties are read-only in Microsoft Graph but can be fully managed through the Exchange Admin Center or the Exchange Online V2 module in PowerShell. Requires $select to retrieve. Supports $filter (eq, ne, not, in).
    - name: onPremisesImmutableId
      value: "{{ onPremisesImmutableId }}"
      description: |
        This property is used to associate an on-premises Active Directory user account to their Microsoft Entra user object. This property must be specified when creating a new user account in the Graph if you're using a federated domain for the user's userPrincipalName (UPN) property. NOTE: The $ and _ characters can't be used when specifying this property. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in).
    - name: onPremisesLastSyncDateTime
      value: "{{ onPremisesLastSyncDateTime }}"
      description: |
        Indicates the last time at which the object was synced with the on-premises directory; for example: 2013-02-16T03:04:54Z. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in).
    - name: onPremisesProvisioningErrors
      description: |
        Errors when using Microsoft synchronization product during provisioning. Requires $select to retrieve. Supports $filter (eq, not, ge, le).
      value:
        - category: "{{ category }}"
          occurredDateTime: "{{ occurredDateTime }}"
          propertyCausingError: "{{ propertyCausingError }}"
          value: "{{ value }}"
          @odata.type: "{{ @odata.type }}"
    - name: onPremisesSamAccountName
      value: "{{ onPremisesSamAccountName }}"
      description: |
        Contains the on-premises samAccountName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).
    - name: onPremisesSecurityIdentifier
      value: "{{ onPremisesSecurityIdentifier }}"
      description: |
        Contains the on-premises security identifier (SID) for the user that was synchronized from on-premises to the cloud. Read-only. Requires $select to retrieve. Supports $filter (eq including on null values).
    - name: onPremisesSyncEnabled
      value: {{ onPremisesSyncEnabled }}
      description: |
        true if this user object is currently being synced from an on-premises Active Directory (AD); otherwise the user isn't being synced and can be managed in Microsoft Entra ID. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values).
    - name: onPremisesUserPrincipalName
      value: "{{ onPremisesUserPrincipalName }}"
      description: |
        Contains the on-premises userPrincipalName synchronized from the on-premises directory. The property is only populated for customers who are synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith).
    - name: otherMails
      value:
        - "{{ otherMails }}"
      description: |
        A list of other email addresses for the user; for example: ['bob@contoso.com', 'Robert@fabrikam.com']. Can store up to 250 values, each with a limit of 250 characters. NOTE: This property can't contain accent characters. Requires $select to retrieve. Supports $filter (eq, not, ge, le, in, startsWith, endsWith, /$count eq 0, /$count ne 0).
    - name: passwordPolicies
      value: "{{ passwordPolicies }}"
      description: |
        Specifies password policies for the user. This value is an enumeration with one possible value being DisableStrongPassword, which allows weaker passwords than the default policy to be specified. DisablePasswordExpiration can also be specified. The two might be specified together; for example: DisablePasswordExpiration, DisableStrongPassword. Requires $select to retrieve. For more information on the default password policies, see Microsoft Entra password policies. Supports $filter (ne, not, and eq on null values).
    - name: passwordProfile
      value: "{{ passwordProfile }}"
      description: |
        Specifies the password profile for the user. The profile contains the user's password. This property is required when a user is created. The password in the profile must satisfy minimum requirements as specified by the passwordPolicies property. By default, a strong password is required. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). To update this property:  User-PasswordProfile.ReadWrite.All is the least privileged permission to update this property.  In delegated scenarios, the User Administrator Microsoft Entra role is the least privileged admin role supported to update this property for nonadmin users. Privileged Authentication Administrator is the least privileged role that's allowed to update this property for all administrators in the tenant. In general, the signed-in user must have a higher privileged administrator role as indicated in Who can reset passwords.  In app-only scenarios, the calling app must be assigned a supported permission and at least the User Administrator Microsoft Entra role.
    - name: pastProjects
      value:
        - "{{ pastProjects }}"
      description: |
        A list for the user to enumerate their past projects. Requires $select to retrieve.
    - name: postalCode
      value: "{{ postalCode }}"
      description: |
        The postal code for the user's postal address. The postal code is specific to the user's country or region. In the United States of America, this attribute contains the ZIP code. Maximum length is 40 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: preferredDataLocation
      value: "{{ preferredDataLocation }}"
      description: |
        The preferred data location for the user. For more information, see OneDrive Online Multi-Geo.
    - name: preferredLanguage
      value: "{{ preferredLanguage }}"
      description: |
        The preferred language for the user. The preferred language format is based on RFC 4646. The name is a combination of an ISO 639 two-letter lowercase culture code associated with the language, and an ISO 3166 two-letter uppercase subculture code associated with the country or region. Example: 'en-US', or 'es-ES'. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values)
    - name: preferredName
      value: "{{ preferredName }}"
      description: |
        The preferred name for the user. Not Supported. This attribute returns an empty string.Requires $select to retrieve.
    - name: print
      value: "{{ print }}"
    - name: provisionedPlans
      description: |
        The plans that are provisioned for the user. Read-only. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le).
      value:
        - capabilityStatus: "{{ capabilityStatus }}"
          provisioningStatus: "{{ provisioningStatus }}"
          service: "{{ service }}"
          @odata.type: "{{ @odata.type }}"
    - name: proxyAddresses
      value:
        - "{{ proxyAddresses }}"
      description: |
        For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. Changes to the mail property update this collection to include the value as an SMTP address. For more information, see mail and proxyAddresses properties. The proxy address prefixed with SMTP (capitalized) is the primary proxy address, while those addresses prefixed with smtp are the secondary proxy addresses. For Azure AD B2C accounts, this property has a limit of 10 unique addresses. Read-only in Microsoft Graph; you can update this property only through the Microsoft 365 admin center. Not nullable. Requires $select to retrieve. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
    - name: responsibilities
      value:
        - "{{ responsibilities }}"
      description: |
        A list for the user to enumerate their responsibilities. Requires $select to retrieve.
    - name: schools
      value:
        - "{{ schools }}"
      description: |
        A list for the user to enumerate the schools they attended. Requires $select to retrieve.
    - name: securityIdentifier
      value: "{{ securityIdentifier }}"
      description: |
        Security identifier (SID) of the user, used in Windows scenarios. Read-only. Returned by default. Supports $select and $filter (eq, not, ge, le, startsWith).
    - name: serviceProvisioningErrors
      description: |
        Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a user object.  Supports $filter (eq, not, for isResolved and serviceInstance).
      value:
        - createdDateTime: "{{ createdDateTime }}"
          isResolved: {{ isResolved }}
          serviceInstance: "{{ serviceInstance }}"
          @odata.type: "{{ @odata.type }}"
    - name: showInAddressList
      value: {{ showInAddressList }}
      description: |
        Do not use in Microsoft Graph. Manage this property through the Microsoft 365 admin center instead. Represents whether the user should be included in the Outlook global address list. See Known issue.
    - name: signInActivity
      value: "{{ signInActivity }}"
      description: |
        Get the last signed-in date and request ID of the sign-in for a given user. Read-only.Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le) but not with any other filterable properties. Note: Details for this property require a Microsoft Entra ID P1 or P2 license and the AuditLog.Read.All permission.This property isn't returned for a user who never signed in or last signed in before April 2020.
    - name: signInSessionsValidFromDateTime
      value: "{{ signInSessionsValidFromDateTime }}"
      description: |
        Any refresh tokens or session tokens (session cookies) issued before this time are invalid. Applications get an error when using an invalid refresh or session token to acquire a delegated access token (to access APIs such as Microsoft Graph). If this happens, the application needs to acquire a new refresh token by requesting the authorized endpoint. Read-only. Use revokeSignInSessions to reset. Requires $select to retrieve.
    - name: skills
      value:
        - "{{ skills }}"
      description: |
        A list for the user to enumerate their skills. Requires $select to retrieve.
    - name: state
      value: "{{ state }}"
      description: |
        The state or province in the user's address. Maximum length is 128 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: streetAddress
      value: "{{ streetAddress }}"
      description: |
        The street address of the user's place of business. Maximum length is 1,024 characters. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: surname
      value: "{{ surname }}"
      description: |
        The user's surname (family name or last name). Maximum length is 64 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: usageLocation
      value: "{{ usageLocation }}"
      description: |
        A two-letter country code (ISO standard 3166). Required for users that are assigned licenses due to legal requirements to check for availability of services in countries/regions. Examples include: US, JP, and GB. Not nullable. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: userPrincipalName
      value: "{{ userPrincipalName }}"
      description: |
        The user principal name (UPN) of the user. The UPN is an Internet-style sign-in name for the user based on the Internet standard RFC 822. By convention, this value should map to the user's email name. The general format is alias@domain, where the domain must be present in the tenant's collection of verified domains. This property is required when a user is created. The verified domains for the tenant can be accessed from the verifiedDomains property of organization.NOTE: This property can't contain accent characters. Only the following characters are allowed A - Z, a - z, 0 - 9, ' . - _ ! # ^ ~. For the complete list of allowed characters, see username policies. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, endsWith) and $orderby.
    - name: userType
      value: "{{ userType }}"
      description: |
        A string value that can be used to classify user types in your directory. The possible values are Member and Guest. Requires $select to retrieve. Supports $filter (eq, ne, not, in, and eq on null values). NOTE: For more information about the permissions for members and guests, see What are the default user permissions in Microsoft Entra ID?
    - name: activities
      description: |
        The user's activities across devices. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          activationUrl: "{{ activationUrl }}"
          activitySourceHost: "{{ activitySourceHost }}"
          appActivityId: "{{ appActivityId }}"
          appDisplayName: "{{ appDisplayName }}"
          contentInfo: "{{ contentInfo }}"
          contentUrl: "{{ contentUrl }}"
          createdDateTime: "{{ createdDateTime }}"
          expirationDateTime: "{{ expirationDateTime }}"
          fallbackUrl: "{{ fallbackUrl }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          status: "{{ status }}"
          userTimezone: "{{ userTimezone }}"
          visualElements:
            attribution:
              addImageQuery: {{ addImageQuery }}
              alternateText: "{{ alternateText }}"
              alternativeText: "{{ alternativeText }}"
              iconUrl: "{{ iconUrl }}"
              @odata.type: "{{ @odata.type }}"
            backgroundColor: "{{ backgroundColor }}"
            content: "{{ content }}"
            description: "{{ description }}"
            displayText: "{{ displayText }}"
            @odata.type: "{{ @odata.type }}"
          historyItems: "{{ historyItems }}"
    - name: adhocCalls
      description: |
        Ad hoc calls associated with the user. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          recordings: "{{ recordings }}"
          transcripts: "{{ transcripts }}"
    - name: agreementAcceptances
      description: |
        The user's terms of use acceptance statuses. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          agreementFileId: "{{ agreementFileId }}"
          agreementId: "{{ agreementId }}"
          deviceDisplayName: "{{ deviceDisplayName }}"
          deviceId: "{{ deviceId }}"
          deviceOSType: "{{ deviceOSType }}"
          deviceOSVersion: "{{ deviceOSVersion }}"
          expirationDateTime: "{{ expirationDateTime }}"
          recordedDateTime: "{{ recordedDateTime }}"
          state: "{{ state }}"
          userDisplayName: "{{ userDisplayName }}"
          userEmail: "{{ userEmail }}"
          userId: "{{ userId }}"
          userPrincipalName: "{{ userPrincipalName }}"
    - name: appRoleAssignments
      description: |
        Represents the app roles a user is granted for an application. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          appRoleId: "{{ appRoleId }}"
          createdDateTime: "{{ createdDateTime }}"
          principalDisplayName: "{{ principalDisplayName }}"
          principalId: "{{ principalId }}"
          principalType: "{{ principalType }}"
          resourceDisplayName: "{{ resourceDisplayName }}"
          resourceId: "{{ resourceId }}"
    - name: authentication
      value: "{{ authentication }}"
      description: |
        The authentication methods that are supported for the user.
    - name: calendar
      value: "{{ calendar }}"
      description: |
        The user's primary calendar. Read-only.
    - name: calendarGroups
      description: |
        The user's calendar groups. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          changeKey: "{{ changeKey }}"
          classId: "{{ classId }}"
          name: "{{ name }}"
          calendars: "{{ calendars }}"
    - name: calendars
      description: |
        The user's calendars. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
          canEdit: {{ canEdit }}
          canShare: {{ canShare }}
          canViewPrivateItems: {{ canViewPrivateItems }}
          changeKey: "{{ changeKey }}"
          color: "{{ color }}"
          defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
          hexColor: "{{ hexColor }}"
          isDefaultCalendar: {{ isDefaultCalendar }}
          isRemovable: {{ isRemovable }}
          isTallyingResponses: {{ isTallyingResponses }}
          name: "{{ name }}"
          owner: "{{ owner }}"
          calendarPermissions: "{{ calendarPermissions }}"
          calendarView: "{{ calendarView }}"
          events: "{{ events }}"
          multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
          singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
    - name: calendarView
      description: |
        The calendar view for the calendar. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          categories: "{{ categories }}"
          changeKey: "{{ changeKey }}"
          createdDateTime: "{{ createdDateTime }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          allowNewTimeProposals: {{ allowNewTimeProposals }}
          attendees: "{{ attendees }}"
          body: "{{ body }}"
          bodyPreview: "{{ bodyPreview }}"
          cancelledOccurrences: "{{ cancelledOccurrences }}"
          end: "{{ end }}"
          hasAttachments: {{ hasAttachments }}
          hideAttendees: {{ hideAttendees }}
          iCalUId: "{{ iCalUId }}"
          importance: "{{ importance }}"
          isAllDay: {{ isAllDay }}
          isCancelled: {{ isCancelled }}
          isDraft: {{ isDraft }}
          isOnlineMeeting: {{ isOnlineMeeting }}
          isOrganizer: {{ isOrganizer }}
          isReminderOn: {{ isReminderOn }}
          location: "{{ location }}"
          locations: "{{ locations }}"
          onlineMeeting: "{{ onlineMeeting }}"
          onlineMeetingProvider: "{{ onlineMeetingProvider }}"
          onlineMeetingUrl: "{{ onlineMeetingUrl }}"
          organizer: "{{ organizer }}"
          originalEndTimeZone: "{{ originalEndTimeZone }}"
          originalStart: "{{ originalStart }}"
          originalStartTimeZone: "{{ originalStartTimeZone }}"
          recurrence: "{{ recurrence }}"
          reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
          responseRequested: {{ responseRequested }}
          responseStatus: "{{ responseStatus }}"
          sensitivity: "{{ sensitivity }}"
          seriesMasterId: "{{ seriesMasterId }}"
          showAs: "{{ showAs }}"
          start: "{{ start }}"
          subject: "{{ subject }}"
          transactionId: "{{ transactionId }}"
          type: "{{ type }}"
          webLink: "{{ webLink }}"
          attachments: "{{ attachments }}"
          calendar: "{{ calendar }}"
          exceptionOccurrences: "{{ exceptionOccurrences }}"
          extensions: "{{ extensions }}"
          instances: "{{ instances }}"
          multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
          singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
    - name: chats
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          chatType: "{{ chatType }}"
          createdDateTime: "{{ createdDateTime }}"
          isHiddenForAllMembers: {{ isHiddenForAllMembers }}
          lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
          migrationMode: "{{ migrationMode }}"
          onlineMeetingInfo: "{{ onlineMeetingInfo }}"
          originalCreatedDateTime: "{{ originalCreatedDateTime }}"
          tenantId: "{{ tenantId }}"
          topic: "{{ topic }}"
          viewpoint: "{{ viewpoint }}"
          webUrl: "{{ webUrl }}"
          installedApps: "{{ installedApps }}"
          lastMessagePreview: "{{ lastMessagePreview }}"
          members: "{{ members }}"
          messages: "{{ messages }}"
          permissionGrants: "{{ permissionGrants }}"
          pinnedMessages: "{{ pinnedMessages }}"
          tabs: "{{ tabs }}"
    - name: cloudClipboard
      value: "{{ cloudClipboard }}"
    - name: cloudPCs
      description: |
        The user's Cloud PCs. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          aadDeviceId: "{{ aadDeviceId }}"
          displayName: "{{ displayName }}"
          gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
          imageDisplayName: "{{ imageDisplayName }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          managedDeviceId: "{{ managedDeviceId }}"
          managedDeviceName: "{{ managedDeviceName }}"
          onPremisesConnectionName: "{{ onPremisesConnectionName }}"
          provisioningPolicyId: "{{ provisioningPolicyId }}"
          provisioningPolicyName: "{{ provisioningPolicyName }}"
          provisioningType: "{{ provisioningType }}"
          servicePlanId: "{{ servicePlanId }}"
          servicePlanName: "{{ servicePlanName }}"
          userPrincipalName: "{{ userPrincipalName }}"
    - name: contactFolders
      description: |
        The user's contacts folders. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          displayName: "{{ displayName }}"
          parentFolderId: "{{ parentFolderId }}"
          childFolders: "{{ childFolders }}"
          contacts: "{{ contacts }}"
          multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
          singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
    - name: contacts
      description: |
        The user's contacts. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          categories: "{{ categories }}"
          changeKey: "{{ changeKey }}"
          createdDateTime: "{{ createdDateTime }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          assistantName: "{{ assistantName }}"
          birthday: "{{ birthday }}"
          businessAddress: "{{ businessAddress }}"
          businessHomePage: "{{ businessHomePage }}"
          businessPhones: "{{ businessPhones }}"
          children: "{{ children }}"
          companyName: "{{ companyName }}"
          department: "{{ department }}"
          displayName: "{{ displayName }}"
          emailAddresses: "{{ emailAddresses }}"
          fileAs: "{{ fileAs }}"
          generation: "{{ generation }}"
          givenName: "{{ givenName }}"
          homeAddress: "{{ homeAddress }}"
          homePhones: "{{ homePhones }}"
          imAddresses: "{{ imAddresses }}"
          initials: "{{ initials }}"
          jobTitle: "{{ jobTitle }}"
          manager: "{{ manager }}"
          middleName: "{{ middleName }}"
          mobilePhone: "{{ mobilePhone }}"
          nickName: "{{ nickName }}"
          officeLocation: "{{ officeLocation }}"
          otherAddress: "{{ otherAddress }}"
          parentFolderId: "{{ parentFolderId }}"
          personalNotes: "{{ personalNotes }}"
          primaryEmailAddress: "{{ primaryEmailAddress }}"
          profession: "{{ profession }}"
          secondaryEmailAddress: "{{ secondaryEmailAddress }}"
          spouseName: "{{ spouseName }}"
          surname: "{{ surname }}"
          tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
          title: "{{ title }}"
          yomiCompanyName: "{{ yomiCompanyName }}"
          yomiGivenName: "{{ yomiGivenName }}"
          yomiSurname: "{{ yomiSurname }}"
          extensions: "{{ extensions }}"
          multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
          photo: "{{ photo }}"
          singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
    - name: createdObjects
      description: |
        Directory objects that the user created. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: dataSecurityAndGovernance
      value: "{{ dataSecurityAndGovernance }}"
      description: |
        The data security and governance settings for the user. Read-only. Nullable.
    - name: deviceManagementTroubleshootingEvents
      description: |
        The list of troubleshooting events for this user.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          correlationId: "{{ correlationId }}"
          eventDateTime: "{{ eventDateTime }}"
    - name: directReports
      description: |
        The users and contacts that report to the user. (The users and contacts that have their manager property set to this user.) Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: drive
      value: "{{ drive }}"
      description: |
        The user's OneDrive. Read-only.
    - name: drives
      description: |
        A collection of drives available for this user. Read-only.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdBy: "{{ createdBy }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          eTag: "{{ eTag }}"
          lastModifiedBy: "{{ lastModifiedBy }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          name: "{{ name }}"
          parentReference: "{{ parentReference }}"
          webUrl: "{{ webUrl }}"
          createdByUser: "{{ createdByUser }}"
          lastModifiedByUser: "{{ lastModifiedByUser }}"
          driveType: "{{ driveType }}"
          owner: "{{ owner }}"
          quota: "{{ quota }}"
          sharePointIds: "{{ sharePointIds }}"
          system: "{{ system }}"
          bundles: "{{ bundles }}"
          following: "{{ following }}"
          items: "{{ items }}"
          list: "{{ list }}"
          root: "{{ root }}"
          special: "{{ special }}"
    - name: employeeExperience
      value: "{{ employeeExperience }}"
    - name: events
      description: |
        The user's events. Default is to show Events under the Default Calendar. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          categories: "{{ categories }}"
          changeKey: "{{ changeKey }}"
          createdDateTime: "{{ createdDateTime }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          allowNewTimeProposals: {{ allowNewTimeProposals }}
          attendees: "{{ attendees }}"
          body: "{{ body }}"
          bodyPreview: "{{ bodyPreview }}"
          cancelledOccurrences: "{{ cancelledOccurrences }}"
          end: "{{ end }}"
          hasAttachments: {{ hasAttachments }}
          hideAttendees: {{ hideAttendees }}
          iCalUId: "{{ iCalUId }}"
          importance: "{{ importance }}"
          isAllDay: {{ isAllDay }}
          isCancelled: {{ isCancelled }}
          isDraft: {{ isDraft }}
          isOnlineMeeting: {{ isOnlineMeeting }}
          isOrganizer: {{ isOrganizer }}
          isReminderOn: {{ isReminderOn }}
          location: "{{ location }}"
          locations: "{{ locations }}"
          onlineMeeting: "{{ onlineMeeting }}"
          onlineMeetingProvider: "{{ onlineMeetingProvider }}"
          onlineMeetingUrl: "{{ onlineMeetingUrl }}"
          organizer: "{{ organizer }}"
          originalEndTimeZone: "{{ originalEndTimeZone }}"
          originalStart: "{{ originalStart }}"
          originalStartTimeZone: "{{ originalStartTimeZone }}"
          recurrence: "{{ recurrence }}"
          reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
          responseRequested: {{ responseRequested }}
          responseStatus: "{{ responseStatus }}"
          sensitivity: "{{ sensitivity }}"
          seriesMasterId: "{{ seriesMasterId }}"
          showAs: "{{ showAs }}"
          start: "{{ start }}"
          subject: "{{ subject }}"
          transactionId: "{{ transactionId }}"
          type: "{{ type }}"
          webLink: "{{ webLink }}"
          attachments: "{{ attachments }}"
          calendar: "{{ calendar }}"
          exceptionOccurrences: "{{ exceptionOccurrences }}"
          extensions: "{{ extensions }}"
          instances: "{{ instances }}"
          multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
          singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
    - name: extensions
      description: |
        The collection of open extensions defined for the user. Read-only. Supports $expand. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
    - name: followedSites
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdBy: "{{ createdBy }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          eTag: "{{ eTag }}"
          lastModifiedBy: "{{ lastModifiedBy }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          name: "{{ name }}"
          parentReference: "{{ parentReference }}"
          webUrl: "{{ webUrl }}"
          createdByUser: "{{ createdByUser }}"
          lastModifiedByUser: "{{ lastModifiedByUser }}"
          displayName: "{{ displayName }}"
          error: "{{ error }}"
          isPersonalSite: {{ isPersonalSite }}
          root: "{{ root }}"
          sharepointIds: "{{ sharepointIds }}"
          siteCollection: "{{ siteCollection }}"
          analytics: "{{ analytics }}"
          columns: "{{ columns }}"
          contentTypes: "{{ contentTypes }}"
          drive: "{{ drive }}"
          drives: "{{ drives }}"
          externalColumns: "{{ externalColumns }}"
          items: "{{ items }}"
          lists: "{{ lists }}"
          onenote: "{{ onenote }}"
          operations: "{{ operations }}"
          pages: "{{ pages }}"
          permissions: "{{ permissions }}"
          sites: "{{ sites }}"
          termStore: "{{ termStore }}"
          termStores: "{{ termStores }}"
    - name: inferenceClassification
      value: "{{ inferenceClassification }}"
      description: |
        Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
    - name: insights
      value: "{{ insights }}"
      description: |
        Represents relationships between a user and items such as OneDrive for work or school documents, calculated using advanced analytics and machine learning techniques. Read-only. Nullable.
    - name: joinedTeams
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          classification: "{{ classification }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          firstChannelName: "{{ firstChannelName }}"
          funSettings: "{{ funSettings }}"
          guestSettings: "{{ guestSettings }}"
          internalId: "{{ internalId }}"
          isArchived: {{ isArchived }}
          memberSettings: "{{ memberSettings }}"
          messagingSettings: "{{ messagingSettings }}"
          specialization: "{{ specialization }}"
          summary: "{{ summary }}"
          tenantId: "{{ tenantId }}"
          visibility: "{{ visibility }}"
          webUrl: "{{ webUrl }}"
          allChannels: "{{ allChannels }}"
          channels: "{{ channels }}"
          group: "{{ group }}"
          incomingChannels: "{{ incomingChannels }}"
          installedApps: "{{ installedApps }}"
          members: "{{ members }}"
          operations: "{{ operations }}"
          permissionGrants: "{{ permissionGrants }}"
          photo: "{{ photo }}"
          primaryChannel: "{{ primaryChannel }}"
          schedule: "{{ schedule }}"
          tags: "{{ tags }}"
          template: "{{ template }}"
    - name: licenseDetails
      description: |
        A collection of this user's license details. Read-only.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          servicePlans: "{{ servicePlans }}"
          skuId: "{{ skuId }}"
          skuPartNumber: "{{ skuPartNumber }}"
    - name: mailFolders
      description: |
        The user's mail folders. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          childFolderCount: {{ childFolderCount }}
          displayName: "{{ displayName }}"
          isHidden: {{ isHidden }}
          parentFolderId: "{{ parentFolderId }}"
          totalItemCount: {{ totalItemCount }}
          unreadItemCount: {{ unreadItemCount }}
          childFolders: "{{ childFolders }}"
          messageRules: "{{ messageRules }}"
          messages: "{{ messages }}"
          multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
          singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
    - name: managedAppRegistrations
      description: |
        Zero or more managed app registrations that belong to the user.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          appIdentifier: "{{ appIdentifier }}"
          applicationVersion: "{{ applicationVersion }}"
          createdDateTime: "{{ createdDateTime }}"
          deviceName: "{{ deviceName }}"
          deviceTag: "{{ deviceTag }}"
          deviceType: "{{ deviceType }}"
          flaggedReasons: "{{ flaggedReasons }}"
          lastSyncDateTime: "{{ lastSyncDateTime }}"
          managementSdkVersion: "{{ managementSdkVersion }}"
          platformVersion: "{{ platformVersion }}"
          userId: "{{ userId }}"
          version: "{{ version }}"
          appliedPolicies: "{{ appliedPolicies }}"
          intendedPolicies: "{{ intendedPolicies }}"
          operations: "{{ operations }}"
    - name: managedDevices
      description: |
        The managed devices associated with the user.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          activationLockBypassCode: "{{ activationLockBypassCode }}"
          androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
          azureADDeviceId: "{{ azureADDeviceId }}"
          azureADRegistered: {{ azureADRegistered }}
          complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
          complianceState: "{{ complianceState }}"
          configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
          deviceActionResults: "{{ deviceActionResults }}"
          deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
          deviceEnrollmentType: "{{ deviceEnrollmentType }}"
          deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
          deviceName: "{{ deviceName }}"
          deviceRegistrationState: "{{ deviceRegistrationState }}"
          easActivated: {{ easActivated }}
          easActivationDateTime: "{{ easActivationDateTime }}"
          easDeviceId: "{{ easDeviceId }}"
          emailAddress: "{{ emailAddress }}"
          enrolledDateTime: "{{ enrolledDateTime }}"
          enrollmentProfileName: "{{ enrollmentProfileName }}"
          ethernetMacAddress: "{{ ethernetMacAddress }}"
          exchangeAccessState: "{{ exchangeAccessState }}"
          exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
          exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
          freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
          iccid: "{{ iccid }}"
          imei: "{{ imei }}"
          isEncrypted: {{ isEncrypted }}
          isSupervised: {{ isSupervised }}
          jailBroken: "{{ jailBroken }}"
          lastSyncDateTime: "{{ lastSyncDateTime }}"
          managedDeviceName: "{{ managedDeviceName }}"
          managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
          managementAgent: "{{ managementAgent }}"
          managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
          managementState: "{{ managementState }}"
          manufacturer: "{{ manufacturer }}"
          meid: "{{ meid }}"
          model: "{{ model }}"
          notes: "{{ notes }}"
          operatingSystem: "{{ operatingSystem }}"
          osVersion: "{{ osVersion }}"
          partnerReportedThreatState: "{{ partnerReportedThreatState }}"
          phoneNumber: "{{ phoneNumber }}"
          physicalMemoryInBytes: {{ physicalMemoryInBytes }}
          remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
          remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
          requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
          serialNumber: "{{ serialNumber }}"
          subscriberCarrier: "{{ subscriberCarrier }}"
          totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
          udid: "{{ udid }}"
          userDisplayName: "{{ userDisplayName }}"
          userId: "{{ userId }}"
          userPrincipalName: "{{ userPrincipalName }}"
          wiFiMacAddress: "{{ wiFiMacAddress }}"
          deviceCategory: "{{ deviceCategory }}"
          deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
          deviceConfigurationStates: "{{ deviceConfigurationStates }}"
          logCollectionRequests: "{{ logCollectionRequests }}"
          users: "{{ users }}"
          windowsProtectionState: "{{ windowsProtectionState }}"
    - name: manager
      value: "{{ manager }}"
      description: |
        The user or contact that is this user's manager. Read-only. Supports $expand.
    - name: memberOf
      description: |
        The groups and directory roles that the user is a member of. Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: messages
      description: |
        The messages in a mailbox or folder. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          categories: "{{ categories }}"
          changeKey: "{{ changeKey }}"
          createdDateTime: "{{ createdDateTime }}"
          lastModifiedDateTime: "{{ lastModifiedDateTime }}"
          bccRecipients: "{{ bccRecipients }}"
          body: "{{ body }}"
          bodyPreview: "{{ bodyPreview }}"
          ccRecipients: "{{ ccRecipients }}"
          conversationId: "{{ conversationId }}"
          conversationIndex: "{{ conversationIndex }}"
          flag: "{{ flag }}"
          from: "{{ from }}"
          hasAttachments: {{ hasAttachments }}
          importance: "{{ importance }}"
          inferenceClassification: "{{ inferenceClassification }}"
          internetMessageHeaders: "{{ internetMessageHeaders }}"
          internetMessageId: "{{ internetMessageId }}"
          isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
          isDraft: {{ isDraft }}
          isRead: {{ isRead }}
          isReadReceiptRequested: {{ isReadReceiptRequested }}
          parentFolderId: "{{ parentFolderId }}"
          receivedDateTime: "{{ receivedDateTime }}"
          replyTo: "{{ replyTo }}"
          sender: "{{ sender }}"
          sentDateTime: "{{ sentDateTime }}"
          subject: "{{ subject }}"
          toRecipients: "{{ toRecipients }}"
          uniqueBody: "{{ uniqueBody }}"
          webLink: "{{ webLink }}"
          attachments: "{{ attachments }}"
          extensions: "{{ extensions }}"
          multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
          singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
    - name: oauth2PermissionGrants
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          clientId: "{{ clientId }}"
          consentType: "{{ consentType }}"
          principalId: "{{ principalId }}"
          resourceId: "{{ resourceId }}"
          scope: "{{ scope }}"
    - name: onenote
      value: "{{ onenote }}"
    - name: onlineMeetings
      description: |
        Information about a meeting, including the URL used to join a meeting, the attendees list, and the description.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
          allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
          allowBreakoutRooms: {{ allowBreakoutRooms }}
          allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
          allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
          allowedPresenters: "{{ allowedPresenters }}"
          allowLiveShare: "{{ allowLiveShare }}"
          allowMeetingChat: "{{ allowMeetingChat }}"
          allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
          allowPowerPointSharing: {{ allowPowerPointSharing }}
          allowRecording: {{ allowRecording }}
          allowTeamworkReactions: {{ allowTeamworkReactions }}
          allowTranscription: {{ allowTranscription }}
          allowWhiteboard: {{ allowWhiteboard }}
          audioConferencing: "{{ audioConferencing }}"
          chatInfo: "{{ chatInfo }}"
          chatRestrictions: "{{ chatRestrictions }}"
          expiryDateTime: "{{ expiryDateTime }}"
          isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
          isEntryExitAnnounced: {{ isEntryExitAnnounced }}
          joinInformation: "{{ joinInformation }}"
          joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
          joinWebUrl: "{{ joinWebUrl }}"
          lobbyBypassSettings: "{{ lobbyBypassSettings }}"
          meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
          meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
          recordAutomatically: {{ recordAutomatically }}
          sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
          shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
          subject: "{{ subject }}"
          videoTeleconferenceId: "{{ videoTeleconferenceId }}"
          watermarkProtection: "{{ watermarkProtection }}"
          attendanceReports: "{{ attendanceReports }}"
          attendeeReport: "{{ attendeeReport }}"
          broadcastSettings: "{{ broadcastSettings }}"
          creationDateTime: "{{ creationDateTime }}"
          endDateTime: "{{ endDateTime }}"
          externalId: "{{ externalId }}"
          isBroadcast: {{ isBroadcast }}
          meetingTemplateId: "{{ meetingTemplateId }}"
          participants: "{{ participants }}"
          startDateTime: "{{ startDateTime }}"
          recordings: "{{ recordings }}"
          transcripts: "{{ transcripts }}"
    - name: onPremisesSyncBehavior
      value: "{{ onPremisesSyncBehavior }}"
    - name: outlook
      value: "{{ outlook }}"
    - name: ownedDevices
      description: |
        Devices the user owns. Read-only. Nullable. Supports $expand and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: ownedObjects
      description: |
        Directory objects the user owns. Read-only. Nullable. Supports $expand, $select nested in $expand, and $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1).
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: people
      description: |
        People that are relevant to the user. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          birthday: "{{ birthday }}"
          companyName: "{{ companyName }}"
          department: "{{ department }}"
          displayName: "{{ displayName }}"
          givenName: "{{ givenName }}"
          imAddress: "{{ imAddress }}"
          isFavorite: {{ isFavorite }}
          jobTitle: "{{ jobTitle }}"
          officeLocation: "{{ officeLocation }}"
          personNotes: "{{ personNotes }}"
          personType: "{{ personType }}"
          phones: "{{ phones }}"
          postalAddresses: "{{ postalAddresses }}"
          profession: "{{ profession }}"
          scoredEmailAddresses: "{{ scoredEmailAddresses }}"
          surname: "{{ surname }}"
          userPrincipalName: "{{ userPrincipalName }}"
          websites: "{{ websites }}"
          yomiCompany: "{{ yomiCompany }}"
    - name: permissionGrants
      description: |
        List all resource-specific permission grants of a user.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          clientAppId: "{{ clientAppId }}"
          clientId: "{{ clientId }}"
          permission: "{{ permission }}"
          permissionType: "{{ permissionType }}"
          resourceAppId: "{{ resourceAppId }}"
    - name: photo
      value: "{{ photo }}"
      description: |
        The user's profile photo. Read-only.
    - name: photos
      description: |
        The collection of the user's profile photos in different sizes. Read-only.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          height: {{ height }}
          width: {{ width }}
    - name: planner
      value: "{{ planner }}"
      description: |
        Entry-point to the Planner resource that might exist for a user. Read-only.
    - name: presence
      value: "{{ presence }}"
    - name: registeredDevices
      description: |
        Devices that are registered for the user. Read-only. Nullable. Supports $expand and returns up to 100 objects.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: scopedRoleMemberOf
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          administrativeUnitId: "{{ administrativeUnitId }}"
          roleId: "{{ roleId }}"
          roleMemberInfo:
            displayName: "{{ displayName }}"
            id: "{{ id }}"
            @odata.type: "{{ @odata.type }}"
    - name: settings
      value: "{{ settings }}"
    - name: solutions
      value: "{{ solutions }}"
      description: |
        The identifier that relates the user to the working time schedule triggers. Read-Only. Nullable
    - name: sponsors
      description: |
        The users and groups responsible for this guest's privileges in the tenant and keeping the guest's information and access updated. (HTTP Methods: GET, POST, DELETE.). Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: teamwork
      value: "{{ teamwork }}"
      description: |
        A container for Microsoft Teams features available for the user. Read-only. Nullable.
    - name: todo
      value: "{{ todo }}"
      description: |
        Represents the To Do services available to a user.
    - name: transitiveMemberOf
      description: |
        The groups, including nested groups, and directory roles that a user is a member of. Nullable.
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

Update the properties of a user object.

```sql
UPDATE entra_id.users.users
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
aboutMe = '{{ aboutMe }}',
accountEnabled = {{ accountEnabled }},
ageGroup = '{{ ageGroup }}',
assignedLicenses = '{{ assignedLicenses }}',
assignedPlans = '{{ assignedPlans }}',
authorizationInfo = '{{ authorizationInfo }}',
birthday = '{{ birthday }}',
businessPhones = '{{ businessPhones }}',
city = '{{ city }}',
companyName = '{{ companyName }}',
consentProvidedForMinor = '{{ consentProvidedForMinor }}',
country = '{{ country }}',
createdDateTime = '{{ createdDateTime }}',
creationType = '{{ creationType }}',
customSecurityAttributes = '{{ customSecurityAttributes }}',
department = '{{ department }}',
deviceEnrollmentLimit = {{ deviceEnrollmentLimit }},
displayName = '{{ displayName }}',
employeeHireDate = '{{ employeeHireDate }}',
employeeId = '{{ employeeId }}',
employeeLeaveDateTime = '{{ employeeLeaveDateTime }}',
employeeOrgData = '{{ employeeOrgData }}',
employeeType = '{{ employeeType }}',
externalUserState = '{{ externalUserState }}',
externalUserStateChangeDateTime = '{{ externalUserStateChangeDateTime }}',
faxNumber = '{{ faxNumber }}',
givenName = '{{ givenName }}',
hireDate = '{{ hireDate }}',
identities = '{{ identities }}',
identityParentId = '{{ identityParentId }}',
imAddresses = '{{ imAddresses }}',
interests = '{{ interests }}',
isManagementRestricted = {{ isManagementRestricted }},
isResourceAccount = {{ isResourceAccount }},
jobTitle = '{{ jobTitle }}',
lastPasswordChangeDateTime = '{{ lastPasswordChangeDateTime }}',
legalAgeGroupClassification = '{{ legalAgeGroupClassification }}',
licenseAssignmentStates = '{{ licenseAssignmentStates }}',
mail = '{{ mail }}',
mailboxSettings = '{{ mailboxSettings }}',
mailNickname = '{{ mailNickname }}',
mobilePhone = '{{ mobilePhone }}',
mySite = '{{ mySite }}',
officeLocation = '{{ officeLocation }}',
onPremisesDistinguishedName = '{{ onPremisesDistinguishedName }}',
onPremisesDomainName = '{{ onPremisesDomainName }}',
onPremisesExtensionAttributes = '{{ onPremisesExtensionAttributes }}',
onPremisesImmutableId = '{{ onPremisesImmutableId }}',
onPremisesLastSyncDateTime = '{{ onPremisesLastSyncDateTime }}',
onPremisesProvisioningErrors = '{{ onPremisesProvisioningErrors }}',
onPremisesSamAccountName = '{{ onPremisesSamAccountName }}',
onPremisesSecurityIdentifier = '{{ onPremisesSecurityIdentifier }}',
onPremisesSyncEnabled = {{ onPremisesSyncEnabled }},
onPremisesUserPrincipalName = '{{ onPremisesUserPrincipalName }}',
otherMails = '{{ otherMails }}',
passwordPolicies = '{{ passwordPolicies }}',
passwordProfile = '{{ passwordProfile }}',
pastProjects = '{{ pastProjects }}',
postalCode = '{{ postalCode }}',
preferredDataLocation = '{{ preferredDataLocation }}',
preferredLanguage = '{{ preferredLanguage }}',
preferredName = '{{ preferredName }}',
print = '{{ print }}',
provisionedPlans = '{{ provisionedPlans }}',
proxyAddresses = '{{ proxyAddresses }}',
responsibilities = '{{ responsibilities }}',
schools = '{{ schools }}',
securityIdentifier = '{{ securityIdentifier }}',
serviceProvisioningErrors = '{{ serviceProvisioningErrors }}',
showInAddressList = {{ showInAddressList }},
signInActivity = '{{ signInActivity }}',
signInSessionsValidFromDateTime = '{{ signInSessionsValidFromDateTime }}',
skills = '{{ skills }}',
state = '{{ state }}',
streetAddress = '{{ streetAddress }}',
surname = '{{ surname }}',
usageLocation = '{{ usageLocation }}',
userPrincipalName = '{{ userPrincipalName }}',
userType = '{{ userType }}',
activities = '{{ activities }}',
adhocCalls = '{{ adhocCalls }}',
agreementAcceptances = '{{ agreementAcceptances }}',
appRoleAssignments = '{{ appRoleAssignments }}',
authentication = '{{ authentication }}',
calendar = '{{ calendar }}',
calendarGroups = '{{ calendarGroups }}',
calendars = '{{ calendars }}',
calendarView = '{{ calendarView }}',
chats = '{{ chats }}',
cloudClipboard = '{{ cloudClipboard }}',
cloudPCs = '{{ cloudPCs }}',
contactFolders = '{{ contactFolders }}',
contacts = '{{ contacts }}',
createdObjects = '{{ createdObjects }}',
dataSecurityAndGovernance = '{{ dataSecurityAndGovernance }}',
deviceManagementTroubleshootingEvents = '{{ deviceManagementTroubleshootingEvents }}',
directReports = '{{ directReports }}',
drive = '{{ drive }}',
drives = '{{ drives }}',
employeeExperience = '{{ employeeExperience }}',
events = '{{ events }}',
extensions = '{{ extensions }}',
followedSites = '{{ followedSites }}',
inferenceClassification = '{{ inferenceClassification }}',
insights = '{{ insights }}',
joinedTeams = '{{ joinedTeams }}',
licenseDetails = '{{ licenseDetails }}',
mailFolders = '{{ mailFolders }}',
managedAppRegistrations = '{{ managedAppRegistrations }}',
managedDevices = '{{ managedDevices }}',
manager = '{{ manager }}',
memberOf = '{{ memberOf }}',
messages = '{{ messages }}',
oauth2PermissionGrants = '{{ oauth2PermissionGrants }}',
onenote = '{{ onenote }}',
onlineMeetings = '{{ onlineMeetings }}',
onPremisesSyncBehavior = '{{ onPremisesSyncBehavior }}',
outlook = '{{ outlook }}',
ownedDevices = '{{ ownedDevices }}',
ownedObjects = '{{ ownedObjects }}',
people = '{{ people }}',
permissionGrants = '{{ permissionGrants }}',
photo = '{{ photo }}',
photos = '{{ photos }}',
planner = '{{ planner }}',
presence = '{{ presence }}',
registeredDevices = '{{ registeredDevices }}',
scopedRoleMemberOf = '{{ scopedRoleMemberOf }}',
settings = '{{ settings }}',
solutions = '{{ solutions }}',
sponsors = '{{ sponsors }}',
teamwork = '{{ teamwork }}',
todo = '{{ todo }}',
transitiveMemberOf = '{{ transitiveMemberOf }}'
WHERE 
userPrincipalName = '{{ userPrincipalName }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
aboutMe,
accountEnabled,
activities,
adhocCalls,
ageGroup,
agreementAcceptances,
appRoleAssignments,
assignedLicenses,
assignedPlans,
authentication,
authorizationInfo,
birthday,
businessPhones,
calendar,
calendarGroups,
calendarView,
calendars,
chats,
city,
cloudClipboard,
cloudPCs,
companyName,
consentProvidedForMinor,
contactFolders,
contacts,
country,
createdDateTime,
createdObjects,
creationType,
customSecurityAttributes,
dataSecurityAndGovernance,
deletedDateTime,
department,
deviceEnrollmentLimit,
deviceManagementTroubleshootingEvents,
directReports,
displayName,
drive,
drives,
employeeExperience,
employeeHireDate,
employeeId,
employeeLeaveDateTime,
employeeOrgData,
employeeType,
events,
extensions,
externalUserState,
externalUserStateChangeDateTime,
faxNumber,
followedSites,
givenName,
hireDate,
identities,
identityParentId,
imAddresses,
inferenceClassification,
insights,
interests,
isManagementRestricted,
isResourceAccount,
jobTitle,
joinedTeams,
lastPasswordChangeDateTime,
legalAgeGroupClassification,
licenseAssignmentStates,
licenseDetails,
mail,
mailFolders,
mailNickname,
mailboxSettings,
managedAppRegistrations,
managedDevices,
manager,
memberOf,
messages,
mobilePhone,
mySite,
oauth2PermissionGrants,
officeLocation,
onPremisesDistinguishedName,
onPremisesDomainName,
onPremisesExtensionAttributes,
onPremisesImmutableId,
onPremisesLastSyncDateTime,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onPremisesUserPrincipalName,
onenote,
onlineMeetings,
otherMails,
outlook,
ownedDevices,
ownedObjects,
passwordPolicies,
passwordProfile,
pastProjects,
people,
permissionGrants,
photo,
photos,
planner,
postalCode,
preferredDataLocation,
preferredLanguage,
preferredName,
presence,
print,
provisionedPlans,
proxyAddresses,
registeredDevices,
responsibilities,
schools,
scopedRoleMemberOf,
securityIdentifier,
serviceProvisioningErrors,
settings,
showInAddressList,
signInActivity,
signInSessionsValidFromDateTime,
skills,
solutions,
sponsors,
state,
streetAddress,
surname,
teamwork,
todo,
transitiveMemberOf,
usageLocation,
userPrincipalName,
userType;
```
</TabItem>
<TabItem value="update_2">

Update the properties of a user object.

```sql
UPDATE entra_id.users.users
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
aboutMe = '{{ aboutMe }}',
accountEnabled = {{ accountEnabled }},
ageGroup = '{{ ageGroup }}',
assignedLicenses = '{{ assignedLicenses }}',
assignedPlans = '{{ assignedPlans }}',
authorizationInfo = '{{ authorizationInfo }}',
birthday = '{{ birthday }}',
businessPhones = '{{ businessPhones }}',
city = '{{ city }}',
companyName = '{{ companyName }}',
consentProvidedForMinor = '{{ consentProvidedForMinor }}',
country = '{{ country }}',
createdDateTime = '{{ createdDateTime }}',
creationType = '{{ creationType }}',
customSecurityAttributes = '{{ customSecurityAttributes }}',
department = '{{ department }}',
deviceEnrollmentLimit = {{ deviceEnrollmentLimit }},
displayName = '{{ displayName }}',
employeeHireDate = '{{ employeeHireDate }}',
employeeId = '{{ employeeId }}',
employeeLeaveDateTime = '{{ employeeLeaveDateTime }}',
employeeOrgData = '{{ employeeOrgData }}',
employeeType = '{{ employeeType }}',
externalUserState = '{{ externalUserState }}',
externalUserStateChangeDateTime = '{{ externalUserStateChangeDateTime }}',
faxNumber = '{{ faxNumber }}',
givenName = '{{ givenName }}',
hireDate = '{{ hireDate }}',
identities = '{{ identities }}',
identityParentId = '{{ identityParentId }}',
imAddresses = '{{ imAddresses }}',
interests = '{{ interests }}',
isManagementRestricted = {{ isManagementRestricted }},
isResourceAccount = {{ isResourceAccount }},
jobTitle = '{{ jobTitle }}',
lastPasswordChangeDateTime = '{{ lastPasswordChangeDateTime }}',
legalAgeGroupClassification = '{{ legalAgeGroupClassification }}',
licenseAssignmentStates = '{{ licenseAssignmentStates }}',
mail = '{{ mail }}',
mailboxSettings = '{{ mailboxSettings }}',
mailNickname = '{{ mailNickname }}',
mobilePhone = '{{ mobilePhone }}',
mySite = '{{ mySite }}',
officeLocation = '{{ officeLocation }}',
onPremisesDistinguishedName = '{{ onPremisesDistinguishedName }}',
onPremisesDomainName = '{{ onPremisesDomainName }}',
onPremisesExtensionAttributes = '{{ onPremisesExtensionAttributes }}',
onPremisesImmutableId = '{{ onPremisesImmutableId }}',
onPremisesLastSyncDateTime = '{{ onPremisesLastSyncDateTime }}',
onPremisesProvisioningErrors = '{{ onPremisesProvisioningErrors }}',
onPremisesSamAccountName = '{{ onPremisesSamAccountName }}',
onPremisesSecurityIdentifier = '{{ onPremisesSecurityIdentifier }}',
onPremisesSyncEnabled = {{ onPremisesSyncEnabled }},
onPremisesUserPrincipalName = '{{ onPremisesUserPrincipalName }}',
otherMails = '{{ otherMails }}',
passwordPolicies = '{{ passwordPolicies }}',
passwordProfile = '{{ passwordProfile }}',
pastProjects = '{{ pastProjects }}',
postalCode = '{{ postalCode }}',
preferredDataLocation = '{{ preferredDataLocation }}',
preferredLanguage = '{{ preferredLanguage }}',
preferredName = '{{ preferredName }}',
print = '{{ print }}',
provisionedPlans = '{{ provisionedPlans }}',
proxyAddresses = '{{ proxyAddresses }}',
responsibilities = '{{ responsibilities }}',
schools = '{{ schools }}',
securityIdentifier = '{{ securityIdentifier }}',
serviceProvisioningErrors = '{{ serviceProvisioningErrors }}',
showInAddressList = {{ showInAddressList }},
signInActivity = '{{ signInActivity }}',
signInSessionsValidFromDateTime = '{{ signInSessionsValidFromDateTime }}',
skills = '{{ skills }}',
state = '{{ state }}',
streetAddress = '{{ streetAddress }}',
surname = '{{ surname }}',
usageLocation = '{{ usageLocation }}',
userPrincipalName = '{{ userPrincipalName }}',
userType = '{{ userType }}',
activities = '{{ activities }}',
adhocCalls = '{{ adhocCalls }}',
agreementAcceptances = '{{ agreementAcceptances }}',
appRoleAssignments = '{{ appRoleAssignments }}',
authentication = '{{ authentication }}',
calendar = '{{ calendar }}',
calendarGroups = '{{ calendarGroups }}',
calendars = '{{ calendars }}',
calendarView = '{{ calendarView }}',
chats = '{{ chats }}',
cloudClipboard = '{{ cloudClipboard }}',
cloudPCs = '{{ cloudPCs }}',
contactFolders = '{{ contactFolders }}',
contacts = '{{ contacts }}',
createdObjects = '{{ createdObjects }}',
dataSecurityAndGovernance = '{{ dataSecurityAndGovernance }}',
deviceManagementTroubleshootingEvents = '{{ deviceManagementTroubleshootingEvents }}',
directReports = '{{ directReports }}',
drive = '{{ drive }}',
drives = '{{ drives }}',
employeeExperience = '{{ employeeExperience }}',
events = '{{ events }}',
extensions = '{{ extensions }}',
followedSites = '{{ followedSites }}',
inferenceClassification = '{{ inferenceClassification }}',
insights = '{{ insights }}',
joinedTeams = '{{ joinedTeams }}',
licenseDetails = '{{ licenseDetails }}',
mailFolders = '{{ mailFolders }}',
managedAppRegistrations = '{{ managedAppRegistrations }}',
managedDevices = '{{ managedDevices }}',
manager = '{{ manager }}',
memberOf = '{{ memberOf }}',
messages = '{{ messages }}',
oauth2PermissionGrants = '{{ oauth2PermissionGrants }}',
onenote = '{{ onenote }}',
onlineMeetings = '{{ onlineMeetings }}',
onPremisesSyncBehavior = '{{ onPremisesSyncBehavior }}',
outlook = '{{ outlook }}',
ownedDevices = '{{ ownedDevices }}',
ownedObjects = '{{ ownedObjects }}',
people = '{{ people }}',
permissionGrants = '{{ permissionGrants }}',
photo = '{{ photo }}',
photos = '{{ photos }}',
planner = '{{ planner }}',
presence = '{{ presence }}',
registeredDevices = '{{ registeredDevices }}',
scopedRoleMemberOf = '{{ scopedRoleMemberOf }}',
settings = '{{ settings }}',
solutions = '{{ solutions }}',
sponsors = '{{ sponsors }}',
teamwork = '{{ teamwork }}',
todo = '{{ todo }}',
transitiveMemberOf = '{{ transitiveMemberOf }}'
WHERE 
user-id = '{{ user-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
aboutMe,
accountEnabled,
activities,
adhocCalls,
ageGroup,
agreementAcceptances,
appRoleAssignments,
assignedLicenses,
assignedPlans,
authentication,
authorizationInfo,
birthday,
businessPhones,
calendar,
calendarGroups,
calendarView,
calendars,
chats,
city,
cloudClipboard,
cloudPCs,
companyName,
consentProvidedForMinor,
contactFolders,
contacts,
country,
createdDateTime,
createdObjects,
creationType,
customSecurityAttributes,
dataSecurityAndGovernance,
deletedDateTime,
department,
deviceEnrollmentLimit,
deviceManagementTroubleshootingEvents,
directReports,
displayName,
drive,
drives,
employeeExperience,
employeeHireDate,
employeeId,
employeeLeaveDateTime,
employeeOrgData,
employeeType,
events,
extensions,
externalUserState,
externalUserStateChangeDateTime,
faxNumber,
followedSites,
givenName,
hireDate,
identities,
identityParentId,
imAddresses,
inferenceClassification,
insights,
interests,
isManagementRestricted,
isResourceAccount,
jobTitle,
joinedTeams,
lastPasswordChangeDateTime,
legalAgeGroupClassification,
licenseAssignmentStates,
licenseDetails,
mail,
mailFolders,
mailNickname,
mailboxSettings,
managedAppRegistrations,
managedDevices,
manager,
memberOf,
messages,
mobilePhone,
mySite,
oauth2PermissionGrants,
officeLocation,
onPremisesDistinguishedName,
onPremisesDomainName,
onPremisesExtensionAttributes,
onPremisesImmutableId,
onPremisesLastSyncDateTime,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onPremisesUserPrincipalName,
onenote,
onlineMeetings,
otherMails,
outlook,
ownedDevices,
ownedObjects,
passwordPolicies,
passwordProfile,
pastProjects,
people,
permissionGrants,
photo,
photos,
planner,
postalCode,
preferredDataLocation,
preferredLanguage,
preferredName,
presence,
print,
provisionedPlans,
proxyAddresses,
registeredDevices,
responsibilities,
schools,
scopedRoleMemberOf,
securityIdentifier,
serviceProvisioningErrors,
settings,
showInAddressList,
signInActivity,
signInSessionsValidFromDateTime,
skills,
solutions,
sponsors,
state,
streetAddress,
surname,
teamwork,
todo,
transitiveMemberOf,
usageLocation,
userPrincipalName,
userType;
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

Delete a user object.   When deleted, user resources, including their mailbox and license assignments, are moved to a temporary container and if the user is restored within 30 days, these objects are restored to them. The user is also restored to any groups they were a member of. After 30 days and if not restored, the user object is permanently deleted and their assigned resources freed. To manage the deleted user object, see deletedItems.

```sql
DELETE FROM entra_id.users.users
WHERE userPrincipalName = '{{ userPrincipalName }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

Delete a user object.   When deleted, user resources, including their mailbox and license assignments, are moved to a temporary container and if the user is restored within 30 days, these objects are restored to them. The user is also restored to any groups they were a member of. After 30 days and if not restored, the user object is permanently deleted and their assigned resources freed. To manage the deleted user object, see deletedItems.

```sql
DELETE FROM entra_id.users.users
WHERE user-id = '{{ user-id }}' --required
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
        { label: 'assign_license', value: 'assign_license' },
        { label: 'check_member_groups', value: 'check_member_groups' },
        { label: 'check_member_objects', value: 'check_member_objects' },
        { label: 'export_personal_data', value: 'export_personal_data' },
        { label: 'find_meeting_times', value: 'find_meeting_times' },
        { label: 'get_mail_tips', value: 'get_mail_tips' },
        { label: 'get_member_groups', value: 'get_member_groups' },
        { label: 'get_member_objects', value: 'get_member_objects' },
        { label: 'remove_all_devices_from_management', value: 'remove_all_devices_from_management' },
        { label: 'reprocess_license_assignment', value: 'reprocess_license_assignment' },
        { label: 'restore', value: 'restore' },
        { label: 'retry_service_provisioning', value: 'retry_service_provisioning' },
        { label: 'revoke_sign_in_sessions', value: 'revoke_sign_in_sessions' },
        { label: 'send_mail', value: 'send_mail' },
        { label: 'wipe_managed_app_registrations_by_device_tag', value: 'wipe_managed_app_registrations_by_device_tag' }
    ]}
>
<TabItem value="get_available_extension_properties">

Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:

```sql
EXEC entra_id.users.users.get_available_extension_properties 
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
EXEC entra_id.users.users.get_by_ids 
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
EXEC entra_id.users.users.validate_properties 
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
<TabItem value="assign_license">

Add or remove licenses for the user to enable or disable their use of Microsoft cloud offerings that the company has licenses to. For example, an organization can have a Microsoft 365 Enterprise E3 subscription with 100 licenses, and this request assigns one of those licenses to a specific user. You can also enable and disable specific plans associated with a subscription. Direct user licensing method is an alternative to group-based licensing.

```sql
EXEC entra_id.users.users.assign_license 
@user-id='{{ user-id }}' --required 
@@json=
'{
"addLicenses": "{{ addLicenses }}", 
"removeLicenses": "{{ removeLicenses }}"
}'
;
```
</TabItem>
<TabItem value="check_member_groups">

Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.

```sql
EXEC entra_id.users.users.check_member_groups 
@user-id='{{ user-id }}' --required 
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
EXEC entra_id.users.users.check_member_objects 
@user-id='{{ user-id }}' --required 
@@json=
'{
"ids": "{{ ids }}"
}'
;
```
</TabItem>
<TabItem value="export_personal_data">

Submit a data policy operation request from a company administrator or an application to export an organizational user's data. This data includes the user's data stored in OneDrive and their activity reports. For more information about exporting data while complying with regulations, see Data Subject Requests and the GDPR and CCPA.

```sql
EXEC entra_id.users.users.export_personal_data 
@user-id='{{ user-id }}' --required 
@@json=
'{
"storageLocation": "{{ storageLocation }}"
}'
;
```
</TabItem>
<TabItem value="find_meeting_times">

Suggest meeting times and locations based on organizer and attendee availability, and time or location constraints specified as parameters. If findMeetingTimes cannot return any meeting suggestions, the response would indicate a reason in the emptySuggestionsReason property.<br />Based on this value, you can better adjust the parameters and call findMeetingTimes again. The algorithm used to suggest meeting times and locations undergoes fine-tuning from time to time. In scenarios like test environments where the input parameters and calendar data remain static, expect that the suggested results may differ over time.

```sql
EXEC entra_id.users.users.find_meeting_times 
@user-id='{{ user-id }}' --required 
@@json=
'{
"attendees": "{{ attendees }}", 
"locationConstraint": "{{ locationConstraint }}", 
"timeConstraint": "{{ timeConstraint }}", 
"meetingDuration": "{{ meetingDuration }}", 
"maxCandidates": {{ maxCandidates }}, 
"isOrganizerOptional": {{ isOrganizerOptional }}, 
"returnSuggestionReasons": {{ returnSuggestionReasons }}, 
"minimumAttendeePercentage": "{{ minimumAttendeePercentage }}"
}'
;
```
</TabItem>
<TabItem value="get_mail_tips">

Get the MailTips of one or more recipients as available to the signed-in user. Note that by making a POST call to the getMailTips action, you can request specific types of MailTips to<br />be returned for more than one recipient at one time. The requested MailTips are returned in a mailTips collection.

```sql
EXEC entra_id.users.users.get_mail_tips 
@user-id='{{ user-id }}' --required 
@@json=
'{
"EmailAddresses": "{{ EmailAddresses }}", 
"MailTipsOptions": "{{ MailTipsOptions }}"
}'
;
```
</TabItem>
<TabItem value="get_member_groups">

Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.

```sql
EXEC entra_id.users.users.get_member_groups 
@user-id='{{ user-id }}' --required 
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
EXEC entra_id.users.users.get_member_objects 
@user-id='{{ user-id }}' --required 
@@json=
'{
"securityEnabledOnly": {{ securityEnabledOnly }}
}'
;
```
</TabItem>
<TabItem value="remove_all_devices_from_management">

Retire all devices from management for this user

```sql
EXEC entra_id.users.users.remove_all_devices_from_management 
@user-id='{{ user-id }}' --required
;
```
</TabItem>
<TabItem value="reprocess_license_assignment">

Reprocess all group-based license assignments for the user. To learn more about group-based licensing, see What is group-based licensing in Microsoft Entra ID. Also see Identify and resolve license assignment problems for a group in Microsoft Entra ID for more details.

```sql
EXEC entra_id.users.users.reprocess_license_assignment 
@user-id='{{ user-id }}' --required
;
```
</TabItem>
<TabItem value="restore">

Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.

```sql
EXEC entra_id.users.users.restore 
@user-id='{{ user-id }}' --required
;
```
</TabItem>
<TabItem value="retry_service_provisioning">

Retry the provisioning of a user object in Microsoft Entra ID.

```sql
EXEC entra_id.users.users.retry_service_provisioning 
@user-id='{{ user-id }}' --required
;
```
</TabItem>
<TabItem value="revoke_sign_in_sessions">

Invalidates all the refresh tokens issued to applications for a user (and session cookies in a user's browser), by resetting the signInSessionsValidFromDateTime user property to the current date-time. Typically, this operation is performed (by the user or an administrator) if the user has a lost or stolen device. This operation prevents access to the organization's data through applications on the device by requiring the user to sign in again to all applications that they consented to previously, independent of device.

```sql
EXEC entra_id.users.users.revoke_sign_in_sessions 
@user-id='{{ user-id }}' --required
;
```
</TabItem>
<TabItem value="send_mail">

Send the message specified in the request body using either JSON or MIME format. When using JSON format, you can include a file attachment in the same sendMail action call. When using MIME format: This method saves the message in the Sent Items folder. Alternatively, create a draft message to send later. To learn more about the steps involved in the backend before a mail is delivered to recipients, see here.

```sql
EXEC entra_id.users.users.send_mail 
@user-id='{{ user-id }}' --required 
@@json=
'{
"Message": "{{ Message }}", 
"SaveToSentItems": {{ SaveToSentItems }}
}'
;
```
</TabItem>
<TabItem value="wipe_managed_app_registrations_by_device_tag">

Issues a wipe operation on an app registration with specified device tag.

```sql
EXEC entra_id.users.users.wipe_managed_app_registrations_by_device_tag 
@user-id='{{ user-id }}' --required 
@@json=
'{
"deviceTag": "{{ deviceTag }}"
}'
;
```
</TabItem>
</Tabs>
