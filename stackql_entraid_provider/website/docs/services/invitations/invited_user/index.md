--- 
title: invited_user
hide_title: false
hide_table_of_contents: false
keywords:
  - invited_user
  - invitations
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

Creates, updates, deletes, gets or lists an <code>invited_user</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="invited_user" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.invitations.invited_user" /></td></tr>
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
    <td>The birthday of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The date and time the user was created, in ISO 8601 format and UTC. The value can't be modified and is automatically populated when the entity is created. Nullable. For on-premises users, the value represents when they were first created in Microsoft Entra ID. Property is null for some users created before June 2018 and on-premises users that were synced to Microsoft Entra ID before June 2018. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The date and time when the user was hired or will start work in a future hire. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in). (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="employeeId" /></td>
    <td><code>string</code></td>
    <td>The employee identifier assigned to the user by the organization. The maximum length is 16 characters. Requires $select to retrieve. Supports $filter (eq, ne, not , ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="employeeLeaveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time when the user left or will leave the organization. To read this property, the calling app must be assigned the User-LifeCycleInfo.Read.All permission. To write this property, the calling app must be assigned the User.Read.All and User-LifeCycleInfo.ReadWrite.All permissions. To read this property in delegated scenarios, the admin needs at least one of the following Microsoft Entra roles: Lifecycle Workflows Administrator (least privilege), Global Reader. To write this property in delegated scenarios, the admin needs the Global Administrator role. Supports $filter (eq, ne, not , ge, le, in). For more information, see Configure the employeeLeaveDateTime property for a user. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>Shows the timestamp for the latest change to the externalUserState property. Requires $select to retrieve. Supports $filter (eq, ne, not , in). (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The hire date of the user. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z. Requires $select to retrieve.  Note: This property is specific to SharePoint in Microsoft 365. We recommend using the native employeeHireDate property to set and update hire date values using Microsoft Graph APIs. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The time when this Microsoft Entra user last changed their password or when their password was created, whichever date the latest action was performed. The date and time information uses ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Requires $select to retrieve. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>Indicates the last time at which the object was synced with the on-premises directory; for example: 2013-02-16T03:04:54Z. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. Requires $select to retrieve. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>Any refresh tokens or session tokens (session cookies) issued before this time are invalid. Applications get an error when using an invalid refresh or session token to acquire a delegated access token (to access APIs such as Microsoft Graph). If this happens, the application needs to acquire a new refresh token by requesting the authorized endpoint. Read-only. Use revokeSignInSessions to reset. Requires $select to retrieve. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The user created as part of the invitation creation. Read-only. The id property is required in the request body to reset a redemption status.</td>
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

The user created as part of the invitation creation. Read-only. The id property is required in the request body to reset a redemption status.

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
FROM entra_id.invitations.invited_user
WHERE $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
