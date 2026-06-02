--- 
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - groups
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

Creates, updates, deletes, gets or lists a <code>groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="groups" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.groups.groups" /></td></tr>
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
    <td><CopyableCode code="acceptedSenders" /></td>
    <td><code>array</code></td>
    <td>The list of users or groups allowed to create posts or calendar events in this group. If this list is nonempty, then only users or groups listed here are allowed to post.</td>
</tr>
<tr>
    <td><CopyableCode code="allowExternalSenders" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if people external to the organization can send messages to the group. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignments" /></td>
    <td><code>array</code></td>
    <td>Represents the app roles granted to a group for an application. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLabels" /></td>
    <td><code>array</code></td>
    <td>The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Requires $select to retrieve. This property can be updated only in delegated scenarios where the caller requires both the Microsoft Graph permission and a supported administrator role.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLicenses" /></td>
    <td><code>array</code></td>
    <td>The licenses that are assigned to the group. Requires $select to retrieve. Supports $filter (eq). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="autoSubscribeNewMembers" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if new members added to the group are autosubscribed to receive email notifications. You can set this property in a PATCH request for the group; don't set it in the initial POST request that creates the group. Default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="calendar" /></td>
    <td><code></code></td>
    <td>The group's calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarView" /></td>
    <td><code>array</code></td>
    <td>The calendar view for the calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="classification" /></td>
    <td><code>string</code></td>
    <td>Describes a classification for the group (such as low, medium, or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="conversations" /></td>
    <td><code>array</code></td>
    <td>The group's conversations.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group was created. The value can't be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOnBehalfOf" /></td>
    <td><code></code></td>
    <td>The user (or application) that created the group. NOTE: This property isn't set if the user is an administrator. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the group. This property is required when a group is created and can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="drive" /></td>
    <td><code></code></td>
    <td>The group's default drive. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="drives" /></td>
    <td><code>array</code></td>
    <td>The group's drives. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>The group's calendar events.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group is set to expire. It's null for security groups, but for Microsoft 365 groups, it represents when the group is set to expire as defined in the groupLifecyclePolicy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="groupLifecyclePolicies" /></td>
    <td><code>array</code></td>
    <td>The collection of lifecycle policies for this group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="groupTypes" /></td>
    <td><code>array</code></td>
    <td>Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or a distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).</td>
</tr>
<tr>
    <td><CopyableCode code="hasMembersWithLicenseErrors" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="hideFromAddressLists" /></td>
    <td><code>boolean</code></td>
    <td>True if the group isn't displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="hideFromOutlookClients" /></td>
    <td><code>boolean</code></td>
    <td>True if the group isn't displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="infoCatalogs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isArchived" /></td>
    <td><code>boolean</code></td>
    <td>When a group is associated with a team, this property determines whether the team is in read-only mode.To read this property, use the /group/&#123;groupId&#125;/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="isAssignableToRole" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this group can be assigned to a Microsoft Entra role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true, visibility must be Hidden, and the group can't be a dynamic group (that is, groupTypes can't contain DynamicMembership). Only callers with at least the Privileged Role Administrator role can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Microsoft Entra role assignmentsUsing this feature requires a Microsoft Entra ID P1 license. Returned by default. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementRestricted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the group is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a group member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isSubscribedByMail" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the signed-in user is subscribed to receive email conversations. The default value is true. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="licenseProcessingState" /></td>
    <td><code></code></td>
    <td>Indicates the status of the group license assignment to all group members. The default value is false. Read-only. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete.Requires $select to retrieve. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="mail" /></td>
    <td><code>string</code></td>
    <td>The SMTP address for the group, for example, 'serviceadmins@contoso.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="mailNickname" /></td>
    <td><code>string</code></td>
    <td>The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following characters: @ () / [] ' ; : &lt;&gt; , SPACE. Required. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>array</code></td>
    <td>The members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).</td>
</tr>
<tr>
    <td><CopyableCode code="membersWithLicenseErrors" /></td>
    <td><code>array</code></td>
    <td>A list of group members with license errors from this group-based license assignment. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="membershipRule" /></td>
    <td><code>string</code></td>
    <td>The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="membershipRuleProcessingState" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDomainName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last time at which the group was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesNetBiosName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSamAccountName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises security identifier (SID) for the group synchronized from on-premises to the cloud. Read-only. Returned by default. Supports $filter (eq including on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncBehavior" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onenote" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the group who can be users or service principals. Limited to 100 owners. Nullable. If this property isn't specified when creating a Microsoft 365 group the calling user (admin or non-admin) is automatically assigned as the group owner. A non-admin user can't explicitly add themselves to this collection when they're creating the group. For more information, see the related known issue. For security groups, the admin user isn't automatically added to this collection. For more information, see the related known issue. Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).</td>
</tr>
<tr>
    <td><CopyableCode code="permissionGrants" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="photo" /></td>
    <td><code></code></td>
    <td>The group's profile photo</td>
</tr>
<tr>
    <td><CopyableCode code="photos" /></td>
    <td><code>array</code></td>
    <td>The profile photos owned by the group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="planner" /></td>
    <td><code></code></td>
    <td>Entry-point to Planner resource that might exist for a Unified Group.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredDataLocation" /></td>
    <td><code>string</code></td>
    <td>The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling app must be granted the Directory.ReadWrite.All permission and the user be assigned at least one of the following Microsoft Entra roles: User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example, en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAddresses" /></td>
    <td><code>array</code></td>
    <td>Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="rejectedSenders" /></td>
    <td><code>array</code></td>
    <td>The list of users or groups not allowed to create posts or calendar events in this group. Nullable</td>
</tr>
<tr>
    <td><CopyableCode code="renewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group was last renewed. This value can't be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceBehaviorOptions" /></td>
    <td><code>array</code></td>
    <td>Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This property can be set only as part of creation (POST). For the list of possible values, see Microsoft 365 group behaviors and provisioning options.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProvisioningOptions" /></td>
    <td><code>array</code></td>
    <td>Specifies the group resources that are associated with the Microsoft 365 group. The possible value is Team. For more information, see Microsoft 365 group behaviors and provisioning options. Returned by default. Supports $filter (eq, not, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="securityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the group is a security group. Required. Returned by default. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="securityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Security identifier of the group, used in Windows scenarios. Read-only. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a group object.  Supports $filter (eq, not, for isResolved and serviceInstance).</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>array</code></td>
    <td>Settings that can govern this group's behavior, like whether members can invite guests to the group. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="sites" /></td>
    <td><code>array</code></td>
    <td>The list of SharePoint sites in this group. Access the default site with /sites/root.</td>
</tr>
<tr>
    <td><CopyableCode code="team" /></td>
    <td><code></code></td>
    <td>The team associated with this group.</td>
</tr>
<tr>
    <td><CopyableCode code="theme" /></td>
    <td><code>string</code></td>
    <td>Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange, or Red. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="threads" /></td>
    <td><code>array</code></td>
    <td>The group's conversation threads. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td>The groups that a group is a member of, either directly or through nested membership. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMembers" /></td>
    <td><code>array</code></td>
    <td>The direct and transitive members of a group. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>The unique identifier that can be assigned to a group and used as an alternate key. Immutable. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="unseenCount" /></td>
    <td><code>number (int32)</code></td>
    <td>Count of conversations that received new posts since the signed-in user last visited the group. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="visibility" /></td>
    <td><code>string</code></td>
    <td>Specifies the group join policy and group content visibility for groups. The possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value isn't specified during group creation on Microsoft Graph, a security group is created as Private by default, and the Microsoft 365 group is Public. Groups assignable to roles are always Private. To learn more, see group visibility options. Returned by default. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="welcomeMessageEnabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
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
    <td><CopyableCode code="acceptedSenders" /></td>
    <td><code>array</code></td>
    <td>The list of users or groups allowed to create posts or calendar events in this group. If this list is nonempty, then only users or groups listed here are allowed to post.</td>
</tr>
<tr>
    <td><CopyableCode code="allowExternalSenders" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if people external to the organization can send messages to the group. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignments" /></td>
    <td><code>array</code></td>
    <td>Represents the app roles granted to a group for an application. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLabels" /></td>
    <td><code>array</code></td>
    <td>The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Requires $select to retrieve. This property can be updated only in delegated scenarios where the caller requires both the Microsoft Graph permission and a supported administrator role.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLicenses" /></td>
    <td><code>array</code></td>
    <td>The licenses that are assigned to the group. Requires $select to retrieve. Supports $filter (eq). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="autoSubscribeNewMembers" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if new members added to the group are autosubscribed to receive email notifications. You can set this property in a PATCH request for the group; don't set it in the initial POST request that creates the group. Default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="calendar" /></td>
    <td><code></code></td>
    <td>The group's calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarView" /></td>
    <td><code>array</code></td>
    <td>The calendar view for the calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="classification" /></td>
    <td><code>string</code></td>
    <td>Describes a classification for the group (such as low, medium, or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="conversations" /></td>
    <td><code>array</code></td>
    <td>The group's conversations.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group was created. The value can't be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOnBehalfOf" /></td>
    <td><code></code></td>
    <td>The user (or application) that created the group. NOTE: This property isn't set if the user is an administrator. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the group. This property is required when a group is created and can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="drive" /></td>
    <td><code></code></td>
    <td>The group's default drive. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="drives" /></td>
    <td><code>array</code></td>
    <td>The group's drives. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>The group's calendar events.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group is set to expire. It's null for security groups, but for Microsoft 365 groups, it represents when the group is set to expire as defined in the groupLifecyclePolicy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="groupLifecyclePolicies" /></td>
    <td><code>array</code></td>
    <td>The collection of lifecycle policies for this group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="groupTypes" /></td>
    <td><code>array</code></td>
    <td>Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or a distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).</td>
</tr>
<tr>
    <td><CopyableCode code="hasMembersWithLicenseErrors" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="hideFromAddressLists" /></td>
    <td><code>boolean</code></td>
    <td>True if the group isn't displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="hideFromOutlookClients" /></td>
    <td><code>boolean</code></td>
    <td>True if the group isn't displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="infoCatalogs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isArchived" /></td>
    <td><code>boolean</code></td>
    <td>When a group is associated with a team, this property determines whether the team is in read-only mode.To read this property, use the /group/&#123;groupId&#125;/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="isAssignableToRole" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this group can be assigned to a Microsoft Entra role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true, visibility must be Hidden, and the group can't be a dynamic group (that is, groupTypes can't contain DynamicMembership). Only callers with at least the Privileged Role Administrator role can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Microsoft Entra role assignmentsUsing this feature requires a Microsoft Entra ID P1 license. Returned by default. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementRestricted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the group is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a group member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isSubscribedByMail" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the signed-in user is subscribed to receive email conversations. The default value is true. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="licenseProcessingState" /></td>
    <td><code></code></td>
    <td>Indicates the status of the group license assignment to all group members. The default value is false. Read-only. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete.Requires $select to retrieve. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="mail" /></td>
    <td><code>string</code></td>
    <td>The SMTP address for the group, for example, 'serviceadmins@contoso.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="mailNickname" /></td>
    <td><code>string</code></td>
    <td>The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following characters: @ () / [] ' ; : &lt;&gt; , SPACE. Required. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>array</code></td>
    <td>The members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).</td>
</tr>
<tr>
    <td><CopyableCode code="membersWithLicenseErrors" /></td>
    <td><code>array</code></td>
    <td>A list of group members with license errors from this group-based license assignment. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="membershipRule" /></td>
    <td><code>string</code></td>
    <td>The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="membershipRuleProcessingState" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDomainName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last time at which the group was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesNetBiosName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSamAccountName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises security identifier (SID) for the group synchronized from on-premises to the cloud. Read-only. Returned by default. Supports $filter (eq including on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncBehavior" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onenote" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the group who can be users or service principals. Limited to 100 owners. Nullable. If this property isn't specified when creating a Microsoft 365 group the calling user (admin or non-admin) is automatically assigned as the group owner. A non-admin user can't explicitly add themselves to this collection when they're creating the group. For more information, see the related known issue. For security groups, the admin user isn't automatically added to this collection. For more information, see the related known issue. Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).</td>
</tr>
<tr>
    <td><CopyableCode code="permissionGrants" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="photo" /></td>
    <td><code></code></td>
    <td>The group's profile photo</td>
</tr>
<tr>
    <td><CopyableCode code="photos" /></td>
    <td><code>array</code></td>
    <td>The profile photos owned by the group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="planner" /></td>
    <td><code></code></td>
    <td>Entry-point to Planner resource that might exist for a Unified Group.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredDataLocation" /></td>
    <td><code>string</code></td>
    <td>The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling app must be granted the Directory.ReadWrite.All permission and the user be assigned at least one of the following Microsoft Entra roles: User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example, en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAddresses" /></td>
    <td><code>array</code></td>
    <td>Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="rejectedSenders" /></td>
    <td><code>array</code></td>
    <td>The list of users or groups not allowed to create posts or calendar events in this group. Nullable</td>
</tr>
<tr>
    <td><CopyableCode code="renewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group was last renewed. This value can't be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceBehaviorOptions" /></td>
    <td><code>array</code></td>
    <td>Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This property can be set only as part of creation (POST). For the list of possible values, see Microsoft 365 group behaviors and provisioning options.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProvisioningOptions" /></td>
    <td><code>array</code></td>
    <td>Specifies the group resources that are associated with the Microsoft 365 group. The possible value is Team. For more information, see Microsoft 365 group behaviors and provisioning options. Returned by default. Supports $filter (eq, not, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="securityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the group is a security group. Required. Returned by default. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="securityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Security identifier of the group, used in Windows scenarios. Read-only. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a group object.  Supports $filter (eq, not, for isResolved and serviceInstance).</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>array</code></td>
    <td>Settings that can govern this group's behavior, like whether members can invite guests to the group. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="sites" /></td>
    <td><code>array</code></td>
    <td>The list of SharePoint sites in this group. Access the default site with /sites/root.</td>
</tr>
<tr>
    <td><CopyableCode code="team" /></td>
    <td><code></code></td>
    <td>The team associated with this group.</td>
</tr>
<tr>
    <td><CopyableCode code="theme" /></td>
    <td><code>string</code></td>
    <td>Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange, or Red. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="threads" /></td>
    <td><code>array</code></td>
    <td>The group's conversation threads. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td>The groups that a group is a member of, either directly or through nested membership. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMembers" /></td>
    <td><code>array</code></td>
    <td>The direct and transitive members of a group. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>The unique identifier that can be assigned to a group and used as an alternate key. Immutable. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="unseenCount" /></td>
    <td><code>number (int32)</code></td>
    <td>Count of conversations that received new posts since the signed-in user last visited the group. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="visibility" /></td>
    <td><code>string</code></td>
    <td>Specifies the group join policy and group content visibility for groups. The possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value isn't specified during group creation on Microsoft Graph, a security group is created as Private by default, and the Microsoft 365 group is Public. Groups assignable to roles are always Private. To learn more, see group visibility options. Returned by default. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="welcomeMessageEnabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
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
    <td><CopyableCode code="acceptedSenders" /></td>
    <td><code>array</code></td>
    <td>The list of users or groups allowed to create posts or calendar events in this group. If this list is nonempty, then only users or groups listed here are allowed to post.</td>
</tr>
<tr>
    <td><CopyableCode code="allowExternalSenders" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if people external to the organization can send messages to the group. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="appRoleAssignments" /></td>
    <td><code>array</code></td>
    <td>Represents the app roles granted to a group for an application. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLabels" /></td>
    <td><code>array</code></td>
    <td>The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Requires $select to retrieve. This property can be updated only in delegated scenarios where the caller requires both the Microsoft Graph permission and a supported administrator role.</td>
</tr>
<tr>
    <td><CopyableCode code="assignedLicenses" /></td>
    <td><code>array</code></td>
    <td>The licenses that are assigned to the group. Requires $select to retrieve. Supports $filter (eq). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="autoSubscribeNewMembers" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if new members added to the group are autosubscribed to receive email notifications. You can set this property in a PATCH request for the group; don't set it in the initial POST request that creates the group. Default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="calendar" /></td>
    <td><code></code></td>
    <td>The group's calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="calendarView" /></td>
    <td><code>array</code></td>
    <td>The calendar view for the calendar. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="classification" /></td>
    <td><code>string</code></td>
    <td>Describes a classification for the group (such as low, medium, or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="conversations" /></td>
    <td><code>array</code></td>
    <td>The group's conversations.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group was created. The value can't be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="createdOnBehalfOf" /></td>
    <td><code></code></td>
    <td>The user (or application) that created the group. NOTE: This property isn't set if the user is an administrator. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when this object was deleted. Always null when the object hasn't been deleted. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the group. This property is required when a group is created and can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="drive" /></td>
    <td><code></code></td>
    <td>The group's default drive. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="drives" /></td>
    <td><code>array</code></td>
    <td>The group's drives. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>The group's calendar events.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group is set to expire. It's null for security groups, but for Microsoft 365 groups, it represents when the group is set to expire as defined in the groupLifecyclePolicy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>The collection of open extensions defined for the group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="groupLifecyclePolicies" /></td>
    <td><code>array</code></td>
    <td>The collection of lifecycle policies for this group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="groupTypes" /></td>
    <td><code>array</code></td>
    <td>Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or a distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).</td>
</tr>
<tr>
    <td><CopyableCode code="hasMembersWithLicenseErrors" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example. Supports $filter (eq).</td>
</tr>
<tr>
    <td><CopyableCode code="hideFromAddressLists" /></td>
    <td><code>boolean</code></td>
    <td>True if the group isn't displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="hideFromOutlookClients" /></td>
    <td><code>boolean</code></td>
    <td>True if the group isn't displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="infoCatalogs" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="isArchived" /></td>
    <td><code>boolean</code></td>
    <td>When a group is associated with a team, this property determines whether the team is in read-only mode.To read this property, use the /group/&#123;groupId&#125;/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.</td>
</tr>
<tr>
    <td><CopyableCode code="isAssignableToRole" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether this group can be assigned to a Microsoft Entra role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true, visibility must be Hidden, and the group can't be a dynamic group (that is, groupTypes can't contain DynamicMembership). Only callers with at least the Privileged Role Administrator role can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Microsoft Entra role assignmentsUsing this feature requires a Microsoft Entra ID P1 license. Returned by default. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="isManagementRestricted" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the group is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a group member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.</td>
</tr>
<tr>
    <td><CopyableCode code="isSubscribedByMail" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the signed-in user is subscribed to receive email conversations. The default value is true. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="licenseProcessingState" /></td>
    <td><code></code></td>
    <td>Indicates the status of the group license assignment to all group members. The default value is false. Read-only. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete.Requires $select to retrieve. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="mail" /></td>
    <td><code>string</code></td>
    <td>The SMTP address for the group, for example, 'serviceadmins@contoso.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="mailEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not).</td>
</tr>
<tr>
    <td><CopyableCode code="mailNickname" /></td>
    <td><code>string</code></td>
    <td>The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following characters: @ () / [] ' ; : &lt;&gt; , SPACE. Required. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="memberOf" /></td>
    <td><code>array</code></td>
    <td>Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="members" /></td>
    <td><code>array</code></td>
    <td>The members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).</td>
</tr>
<tr>
    <td><CopyableCode code="membersWithLicenseErrors" /></td>
    <td><code>array</code></td>
    <td>A list of group members with license errors from this group-based license assignment. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="membershipRule" /></td>
    <td><code>string</code></td>
    <td>The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="membershipRuleProcessingState" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesDomainName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesLastSyncDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Indicates the last time at which the group was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in). (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesNetBiosName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSamAccountName" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSecurityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Contains the on-premises security identifier (SID) for the group synchronized from on-premises to the cloud. Read-only. Returned by default. Supports $filter (eq including on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncBehavior" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="onPremisesSyncEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="onenote" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="owners" /></td>
    <td><code>array</code></td>
    <td>The owners of the group who can be users or service principals. Limited to 100 owners. Nullable. If this property isn't specified when creating a Microsoft 365 group the calling user (admin or non-admin) is automatically assigned as the group owner. A non-admin user can't explicitly add themselves to this collection when they're creating the group. For more information, see the related known issue. For security groups, the admin user isn't automatically added to this collection. For more information, see the related known issue. Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).</td>
</tr>
<tr>
    <td><CopyableCode code="permissionGrants" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="photo" /></td>
    <td><code></code></td>
    <td>The group's profile photo</td>
</tr>
<tr>
    <td><CopyableCode code="photos" /></td>
    <td><code>array</code></td>
    <td>The profile photos owned by the group. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="planner" /></td>
    <td><code></code></td>
    <td>Entry-point to Planner resource that might exist for a Unified Group.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredDataLocation" /></td>
    <td><code>string</code></td>
    <td>The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling app must be granted the Directory.ReadWrite.All permission and the user be assigned at least one of the following Microsoft Entra roles: User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredLanguage" /></td>
    <td><code>string</code></td>
    <td>The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example, en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).</td>
</tr>
<tr>
    <td><CopyableCode code="proxyAddresses" /></td>
    <td><code>array</code></td>
    <td>Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).</td>
</tr>
<tr>
    <td><CopyableCode code="rejectedSenders" /></td>
    <td><code>array</code></td>
    <td>The list of users or groups not allowed to create posts or calendar events in this group. Nullable</td>
</tr>
<tr>
    <td><CopyableCode code="renewedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of when the group was last renewed. This value can't be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceBehaviorOptions" /></td>
    <td><code>array</code></td>
    <td>Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This property can be set only as part of creation (POST). For the list of possible values, see Microsoft 365 group behaviors and provisioning options.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceProvisioningOptions" /></td>
    <td><code>array</code></td>
    <td>Specifies the group resources that are associated with the Microsoft 365 group. The possible value is Team. For more information, see Microsoft 365 group behaviors and provisioning options. Returned by default. Supports $filter (eq, not, startsWith).</td>
</tr>
<tr>
    <td><CopyableCode code="securityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Specifies whether the group is a security group. Required. Returned by default. Supports $filter (eq, ne, not, in).</td>
</tr>
<tr>
    <td><CopyableCode code="securityIdentifier" /></td>
    <td><code>string</code></td>
    <td>Security identifier of the group, used in Windows scenarios. Read-only. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceProvisioningErrors" /></td>
    <td><code>array</code></td>
    <td>Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a group object.  Supports $filter (eq, not, for isResolved and serviceInstance).</td>
</tr>
<tr>
    <td><CopyableCode code="settings" /></td>
    <td><code>array</code></td>
    <td>Settings that can govern this group's behavior, like whether members can invite guests to the group. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="sites" /></td>
    <td><code>array</code></td>
    <td>The list of SharePoint sites in this group. Access the default site with /sites/root.</td>
</tr>
<tr>
    <td><CopyableCode code="team" /></td>
    <td><code></code></td>
    <td>The team associated with this group.</td>
</tr>
<tr>
    <td><CopyableCode code="theme" /></td>
    <td><code>string</code></td>
    <td>Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange, or Red. Returned by default.</td>
</tr>
<tr>
    <td><CopyableCode code="threads" /></td>
    <td><code>array</code></td>
    <td>The group's conversation threads. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMemberOf" /></td>
    <td><code>array</code></td>
    <td>The groups that a group is a member of, either directly or through nested membership. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="transitiveMembers" /></td>
    <td><code>array</code></td>
    <td>The direct and transitive members of a group. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>The unique identifier that can be assigned to a group and used as an alternate key. Immutable. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="unseenCount" /></td>
    <td><code>number (int32)</code></td>
    <td>Count of conversations that received new posts since the signed-in user last visited the group. Requires $select to retrieve. Supported only on the Get group API (GET /groups/&#123;ID&#125;).</td>
</tr>
<tr>
    <td><CopyableCode code="visibility" /></td>
    <td><code>string</code></td>
    <td>Specifies the group join policy and group content visibility for groups. The possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value isn't specified during group creation on Microsoft Graph, a security group is created as Private by default, and the Microsoft 365 group is Public. Groups assignable to roles are always Private. To learn more, see group visibility options. Returned by default. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="welcomeMessageEnabled" /></td>
    <td><code>boolean</code></td>
    <td></td>
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
    <td><a href="#parameter-uniqueName"><code>uniqueName</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that aren't_ returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and aren't returned in the $select query.</td>
</tr>
<tr>
    <td><a href="#get_2"><CopyableCode code="get_2" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that aren't_ returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and aren't returned in the $select query.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-ConsistencyLevel"><code>ConsistencyLevel</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>List all the groups available in an organization, excluding dynamic distribution groups. To retrieve dynamic distribution groups, use the Exchange admin center. This operation returns by default only a subset of the properties for each group. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the group and specify the properties in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and are not returned in the $select query.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new group as specified in the request body. You can create the following types of groups: This operation returns by default only a subset of the properties for each group. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-uniqueName"><code>uniqueName</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new group object if it doesn't exist, or update the properties of an existing group object.<br />You can create or update the following types of group: By default, this operation returns only a subset of the properties for each group. For a list of properties that are returned by default, see the Properties section of the group resource. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option.</td>
</tr>
<tr>
    <td><a href="#update_2"><CopyableCode code="update_2" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new group object if it doesn't exist, or update the properties of an existing group object.<br />You can create or update the following types of group: By default, this operation returns only a subset of the properties for each group. For a list of properties that are returned by default, see the Properties section of the group resource. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-uniqueName"><code>uniqueName</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a group. When deleted, both Microsoft 365 and security groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This doesn't apply to Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.</td>
</tr>
<tr>
    <td><a href="#delete_2"><CopyableCode code="delete_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a group. When deleted, both Microsoft 365 and security groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This doesn't apply to Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.</td>
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
    <td><a href="#add_favorite"><CopyableCode code="add_favorite" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Add the group to the list of the current user's favorite groups.  The group shows up in Outlook and Teams favorites. Supported for Microsoft 365 groups only.</td>
</tr>
<tr>
    <td><a href="#assign_license"><CopyableCode code="assign_license" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Add or remove licenses on a group. Licenses assigned to the group will be assigned to all users in the group. Group-based licensing is an alternative to direct user licensing. To learn more about group-based licensing, see What is group-based licensing in Microsoft Entra ID. To get the subscriptions available in the directory, perform a GET subscribedSkus request.</td>
</tr>
<tr>
    <td><a href="#check_granted_permissions_for_app"><CopyableCode code="check_granted_permissions_for_app" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#check_member_groups"><CopyableCode code="check_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.</td>
</tr>
<tr>
    <td><a href="#check_member_objects"><CopyableCode code="check_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_member_groups"><CopyableCode code="get_member_groups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Return all the group IDs for the groups that the specified user, group, service principal, organizational contact, device, or directory object is a member of. This function is transitive. This API returns up to 11,000 group IDs. If more than 11,000 results are available, it returns a 400 Bad Request error with the DirectoryResultSizeLimitExceeded error code. If you get the DirectoryResultSizeLimitExceeded error code, use the List group transitive memberOf API instead.</td>
</tr>
<tr>
    <td><a href="#get_member_objects"><CopyableCode code="get_member_objects" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Return all IDs for the groups, administrative units, and directory roles that an object of one of the following types is a member of:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. Only users and role-enabled groups can be members of directory roles.</td>
</tr>
<tr>
    <td><a href="#remove_favorite"><CopyableCode code="remove_favorite" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Remove the group from the list of the current user's favorite groups. Supported for Microsoft 365 groups only.</td>
</tr>
<tr>
    <td><a href="#renew"><CopyableCode code="renew" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Renew a group's expiration. When a group is renewed, the group expiration is extended by the number of days defined in the policy.</td>
</tr>
<tr>
    <td><a href="#reset_unseen_count"><CopyableCode code="reset_unseen_count" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Reset the unseenCount of all the posts that the current user hasn't seen since their last visit. Supported for Microsoft 365 groups only.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.</td>
</tr>
<tr>
    <td><a href="#retry_service_provisioning"><CopyableCode code="retry_service_provisioning" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Retry the group service provisioning.</td>
</tr>
<tr>
    <td><a href="#validate_properties_2"><CopyableCode code="validate_properties_2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-group-id"><code>group-id</code></a></td>
    <td></td>
    <td>Validate that a Microsoft 365 group's display name or mail nickname complies with naming policies. Clients can use this API to determine whether a display name or mail nickname is valid before trying to update a Microsoft 365 group. To validate the properties before creating a group, use the directoryobject:validateProperties function. The following policy validations are performed for the display name and mail nickname properties: This API only returns the first validation failure that is encountered. If the properties fail multiple validations, only the first validation failure is returned. However, you can validate both the mail nickname and the display name and receive a collection of validation errors if you are only validating the prefix and suffix naming policy. To learn more about configuring naming policies, see Configure naming policy.</td>
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
<tr id="parameter-group-id">
    <td><CopyableCode code="group-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of group</td>
</tr>
<tr id="parameter-uniqueName">
    <td><CopyableCode code="uniqueName" /></td>
    <td><code>string</code></td>
    <td>Alternate key of group</td>
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

Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that aren't_ returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and aren't returned in the $select query.

```sql
SELECT
id,
@odata.type,
acceptedSenders,
allowExternalSenders,
appRoleAssignments,
assignedLabels,
assignedLicenses,
autoSubscribeNewMembers,
calendar,
calendarView,
classification,
conversations,
createdDateTime,
createdOnBehalfOf,
deletedDateTime,
description,
displayName,
drive,
drives,
events,
expirationDateTime,
extensions,
groupLifecyclePolicies,
groupTypes,
hasMembersWithLicenseErrors,
hideFromAddressLists,
hideFromOutlookClients,
infoCatalogs,
isArchived,
isAssignableToRole,
isManagementRestricted,
isSubscribedByMail,
licenseProcessingState,
mail,
mailEnabled,
mailNickname,
memberOf,
members,
membersWithLicenseErrors,
membershipRule,
membershipRuleProcessingState,
onPremisesDomainName,
onPremisesLastSyncDateTime,
onPremisesNetBiosName,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onenote,
owners,
permissionGrants,
photo,
photos,
planner,
preferredDataLocation,
preferredLanguage,
proxyAddresses,
rejectedSenders,
renewedDateTime,
resourceBehaviorOptions,
resourceProvisioningOptions,
securityEnabled,
securityIdentifier,
serviceProvisioningErrors,
settings,
sites,
team,
theme,
threads,
transitiveMemberOf,
transitiveMembers,
uniqueName,
unseenCount,
visibility,
welcomeMessageEnabled
FROM entraid.groups.groups
WHERE uniqueName = '{{ uniqueName }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get_2">

Get the properties and relationships of a group object. This operation returns by default only a subset of all the available properties, as noted in the Properties section. To get properties that aren't_ returned by default, specify them in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and aren't returned in the $select query.

```sql
SELECT
id,
@odata.type,
acceptedSenders,
allowExternalSenders,
appRoleAssignments,
assignedLabels,
assignedLicenses,
autoSubscribeNewMembers,
calendar,
calendarView,
classification,
conversations,
createdDateTime,
createdOnBehalfOf,
deletedDateTime,
description,
displayName,
drive,
drives,
events,
expirationDateTime,
extensions,
groupLifecyclePolicies,
groupTypes,
hasMembersWithLicenseErrors,
hideFromAddressLists,
hideFromOutlookClients,
infoCatalogs,
isArchived,
isAssignableToRole,
isManagementRestricted,
isSubscribedByMail,
licenseProcessingState,
mail,
mailEnabled,
mailNickname,
memberOf,
members,
membersWithLicenseErrors,
membershipRule,
membershipRuleProcessingState,
onPremisesDomainName,
onPremisesLastSyncDateTime,
onPremisesNetBiosName,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onenote,
owners,
permissionGrants,
photo,
photos,
planner,
preferredDataLocation,
preferredLanguage,
proxyAddresses,
rejectedSenders,
renewedDateTime,
resourceBehaviorOptions,
resourceProvisioningOptions,
securityEnabled,
securityIdentifier,
serviceProvisioningErrors,
settings,
sites,
team,
theme,
threads,
transitiveMemberOf,
transitiveMembers,
uniqueName,
unseenCount,
visibility,
welcomeMessageEnabled
FROM entraid.groups.groups
WHERE group-id = '{{ group-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List all the groups available in an organization, excluding dynamic distribution groups. To retrieve dynamic distribution groups, use the Exchange admin center. This operation returns by default only a subset of the properties for each group. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the group and specify the properties in a $select OData query option. The hasMembersWithLicenseErrors and isArchived properties are an exception and are not returned in the $select query.

```sql
SELECT
id,
@odata.type,
acceptedSenders,
allowExternalSenders,
appRoleAssignments,
assignedLabels,
assignedLicenses,
autoSubscribeNewMembers,
calendar,
calendarView,
classification,
conversations,
createdDateTime,
createdOnBehalfOf,
deletedDateTime,
description,
displayName,
drive,
drives,
events,
expirationDateTime,
extensions,
groupLifecyclePolicies,
groupTypes,
hasMembersWithLicenseErrors,
hideFromAddressLists,
hideFromOutlookClients,
infoCatalogs,
isArchived,
isAssignableToRole,
isManagementRestricted,
isSubscribedByMail,
licenseProcessingState,
mail,
mailEnabled,
mailNickname,
memberOf,
members,
membersWithLicenseErrors,
membershipRule,
membershipRuleProcessingState,
onPremisesDomainName,
onPremisesLastSyncDateTime,
onPremisesNetBiosName,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onenote,
owners,
permissionGrants,
photo,
photos,
planner,
preferredDataLocation,
preferredLanguage,
proxyAddresses,
rejectedSenders,
renewedDateTime,
resourceBehaviorOptions,
resourceProvisioningOptions,
securityEnabled,
securityIdentifier,
serviceProvisioningErrors,
settings,
sites,
team,
theme,
threads,
transitiveMemberOf,
transitiveMembers,
uniqueName,
unseenCount,
visibility,
welcomeMessageEnabled
FROM entraid.groups.groups
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

Create a new group as specified in the request body. You can create the following types of groups: This operation returns by default only a subset of the properties for each group. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option.

```sql
INSERT INTO entraid.groups.groups (
id,
@odata.type,
deletedDateTime,
allowExternalSenders,
assignedLabels,
assignedLicenses,
autoSubscribeNewMembers,
classification,
createdDateTime,
description,
displayName,
expirationDateTime,
groupTypes,
hasMembersWithLicenseErrors,
hideFromAddressLists,
hideFromOutlookClients,
infoCatalogs,
isArchived,
isAssignableToRole,
isManagementRestricted,
isSubscribedByMail,
licenseProcessingState,
mail,
mailEnabled,
mailNickname,
membershipRule,
membershipRuleProcessingState,
onPremisesDomainName,
onPremisesLastSyncDateTime,
onPremisesNetBiosName,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncEnabled,
preferredDataLocation,
preferredLanguage,
proxyAddresses,
renewedDateTime,
resourceBehaviorOptions,
resourceProvisioningOptions,
securityEnabled,
securityIdentifier,
serviceProvisioningErrors,
theme,
uniqueName,
unseenCount,
visibility,
welcomeMessageEnabled,
acceptedSenders,
appRoleAssignments,
calendar,
calendarView,
conversations,
createdOnBehalfOf,
drive,
drives,
events,
extensions,
groupLifecyclePolicies,
memberOf,
members,
membersWithLicenseErrors,
onenote,
onPremisesSyncBehavior,
owners,
permissionGrants,
photo,
photos,
planner,
rejectedSenders,
settings,
sites,
team,
threads,
transitiveMemberOf,
transitiveMembers
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ deletedDateTime }}',
{{ allowExternalSenders }},
'{{ assignedLabels }}',
'{{ assignedLicenses }}',
{{ autoSubscribeNewMembers }},
'{{ classification }}',
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ expirationDateTime }}',
'{{ groupTypes }}',
{{ hasMembersWithLicenseErrors }},
{{ hideFromAddressLists }},
{{ hideFromOutlookClients }},
'{{ infoCatalogs }}',
{{ isArchived }},
{{ isAssignableToRole }},
{{ isManagementRestricted }},
{{ isSubscribedByMail }},
'{{ licenseProcessingState }}',
'{{ mail }}',
{{ mailEnabled }},
'{{ mailNickname }}',
'{{ membershipRule }}',
'{{ membershipRuleProcessingState }}',
'{{ onPremisesDomainName }}',
'{{ onPremisesLastSyncDateTime }}',
'{{ onPremisesNetBiosName }}',
'{{ onPremisesProvisioningErrors }}',
'{{ onPremisesSamAccountName }}',
'{{ onPremisesSecurityIdentifier }}',
{{ onPremisesSyncEnabled }},
'{{ preferredDataLocation }}',
'{{ preferredLanguage }}',
'{{ proxyAddresses }}',
'{{ renewedDateTime }}',
'{{ resourceBehaviorOptions }}',
'{{ resourceProvisioningOptions }}',
{{ securityEnabled }},
'{{ securityIdentifier }}',
'{{ serviceProvisioningErrors }}',
'{{ theme }}',
'{{ uniqueName }}',
{{ unseenCount }},
'{{ visibility }}',
{{ welcomeMessageEnabled }},
'{{ acceptedSenders }}',
'{{ appRoleAssignments }}',
'{{ calendar }}',
'{{ calendarView }}',
'{{ conversations }}',
'{{ createdOnBehalfOf }}',
'{{ drive }}',
'{{ drives }}',
'{{ events }}',
'{{ extensions }}',
'{{ groupLifecyclePolicies }}',
'{{ memberOf }}',
'{{ members }}',
'{{ membersWithLicenseErrors }}',
'{{ onenote }}',
'{{ onPremisesSyncBehavior }}',
'{{ owners }}',
'{{ permissionGrants }}',
'{{ photo }}',
'{{ photos }}',
'{{ planner }}',
'{{ rejectedSenders }}',
'{{ settings }}',
'{{ sites }}',
'{{ team }}',
'{{ threads }}',
'{{ transitiveMemberOf }}',
'{{ transitiveMembers }}'
RETURNING
id,
@odata.type,
acceptedSenders,
allowExternalSenders,
appRoleAssignments,
assignedLabels,
assignedLicenses,
autoSubscribeNewMembers,
calendar,
calendarView,
classification,
conversations,
createdDateTime,
createdOnBehalfOf,
deletedDateTime,
description,
displayName,
drive,
drives,
events,
expirationDateTime,
extensions,
groupLifecyclePolicies,
groupTypes,
hasMembersWithLicenseErrors,
hideFromAddressLists,
hideFromOutlookClients,
infoCatalogs,
isArchived,
isAssignableToRole,
isManagementRestricted,
isSubscribedByMail,
licenseProcessingState,
mail,
mailEnabled,
mailNickname,
memberOf,
members,
membersWithLicenseErrors,
membershipRule,
membershipRuleProcessingState,
onPremisesDomainName,
onPremisesLastSyncDateTime,
onPremisesNetBiosName,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onenote,
owners,
permissionGrants,
photo,
photos,
planner,
preferredDataLocation,
preferredLanguage,
proxyAddresses,
rejectedSenders,
renewedDateTime,
resourceBehaviorOptions,
resourceProvisioningOptions,
securityEnabled,
securityIdentifier,
serviceProvisioningErrors,
settings,
sites,
team,
theme,
threads,
transitiveMemberOf,
transitiveMembers,
uniqueName,
unseenCount,
visibility,
welcomeMessageEnabled
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: groups
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
    - name: allowExternalSenders
      value: {{ allowExternalSenders }}
      description: |
        Indicates if people external to the organization can send messages to the group. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/{ID}).
    - name: assignedLabels
      description: |
        The list of sensitivity label pairs (label ID, label name) associated with a Microsoft 365 group. Requires $select to retrieve. This property can be updated only in delegated scenarios where the caller requires both the Microsoft Graph permission and a supported administrator role.
      value:
        - displayName: "{{ displayName }}"
          labelId: "{{ labelId }}"
          @odata.type: "{{ @odata.type }}"
    - name: assignedLicenses
      description: |
        The licenses that are assigned to the group. Requires $select to retrieve. Supports $filter (eq). Read-only.
      value:
        - disabledPlans: "{{ disabledPlans }}"
          skuId: "{{ skuId }}"
          @odata.type: "{{ @odata.type }}"
    - name: autoSubscribeNewMembers
      value: {{ autoSubscribeNewMembers }}
      description: |
        Indicates if new members added to the group are autosubscribed to receive email notifications. You can set this property in a PATCH request for the group; don't set it in the initial POST request that creates the group. Default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/{ID}).
    - name: classification
      value: "{{ classification }}"
      description: |
        Describes a classification for the group (such as low, medium, or high business impact). Valid values for this property are defined by creating a ClassificationList setting value, based on the template definition.Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        Timestamp of when the group was created. The value can't be modified and is automatically populated when the group is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        An optional description for the group. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith) and $search.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the group. This property is required when a group is created and can't be cleared during updates. Maximum length is 256 characters. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values), $search, and $orderby.
    - name: expirationDateTime
      value: "{{ expirationDateTime }}"
      description: |
        Timestamp of when the group is set to expire. It's null for security groups, but for Microsoft 365 groups, it represents when the group is set to expire as defined in the groupLifecyclePolicy. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
    - name: groupTypes
      value:
        - "{{ groupTypes }}"
      description: |
        Specifies the group type and its membership. If the collection contains Unified, the group is a Microsoft 365 group; otherwise, it's either a security group or a distribution group. For details, see groups overview.If the collection includes DynamicMembership, the group has dynamic membership; otherwise, membership is static. Returned by default. Supports $filter (eq, not).
    - name: hasMembersWithLicenseErrors
      value: {{ hasMembersWithLicenseErrors }}
      description: |
        Indicates whether there are members in this group that have license errors from its group-based license assignment. This property is never returned on a GET operation. You can use it as a $filter argument to get groups that have members with license errors (that is, filter for this property being true). See an example. Supports $filter (eq).
    - name: hideFromAddressLists
      value: {{ hideFromAddressLists }}
      description: |
        True if the group isn't displayed in certain parts of the Outlook UI: the Address Book, address lists for selecting message recipients, and the Browse Groups dialog for searching groups; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/{ID}).
    - name: hideFromOutlookClients
      value: {{ hideFromOutlookClients }}
      description: |
        True if the group isn't displayed in Outlook clients, such as Outlook for Windows and Outlook on the web; otherwise, false. The default value is false. Requires $select to retrieve. Supported only on the Get group API (GET /groups/{ID}).
    - name: infoCatalogs
      value:
        - "{{ infoCatalogs }}"
    - name: isArchived
      value: {{ isArchived }}
      description: |
        When a group is associated with a team, this property determines whether the team is in read-only mode.To read this property, use the /group/{groupId}/team endpoint or the Get team API. To update this property, use the archiveTeam and unarchiveTeam APIs.
    - name: isAssignableToRole
      value: {{ isAssignableToRole }}
      description: |
        Indicates whether this group can be assigned to a Microsoft Entra role. Optional. This property can only be set while creating the group and is immutable. If set to true, the securityEnabled property must also be set to true, visibility must be Hidden, and the group can't be a dynamic group (that is, groupTypes can't contain DynamicMembership). Only callers with at least the Privileged Role Administrator role can set this property. The caller must also be assigned the RoleManagement.ReadWrite.Directory permission to set this property or update the membership of such groups. For more, see Using a group to manage Microsoft Entra role assignmentsUsing this feature requires a Microsoft Entra ID P1 license. Returned by default. Supports $filter (eq, ne, not).
    - name: isManagementRestricted
      value: {{ isManagementRestricted }}
      description: |
        Indicates whether the group is a member of a restricted management administrative unit. If not set, the default value is null and the default behavior is false. Read-only.  To manage a group member of a restricted management administrative unit, the administrator or calling app must be assigned a Microsoft Entra role at the scope of the restricted management administrative unit. Requires $select to retrieve.
    - name: isSubscribedByMail
      value: {{ isSubscribedByMail }}
      description: |
        Indicates whether the signed-in user is subscribed to receive email conversations. The default value is true. Requires $select to retrieve. Supported only on the Get group API (GET /groups/{ID}).
    - name: licenseProcessingState
      value: "{{ licenseProcessingState }}"
      description: |
        Indicates the status of the group license assignment to all group members. The default value is false. Read-only. Possible values: QueuedForProcessing, ProcessingInProgress, and ProcessingComplete.Requires $select to retrieve. Read-only.
    - name: mail
      value: "{{ mail }}"
      description: |
        The SMTP address for the group, for example, 'serviceadmins@contoso.com'. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: mailEnabled
      value: {{ mailEnabled }}
      description: |
        Specifies whether the group is mail-enabled. Required. Returned by default. Supports $filter (eq, ne, not).
    - name: mailNickname
      value: "{{ mailNickname }}"
      description: |
        The mail alias for the group, unique for Microsoft 365 groups in the organization. Maximum length is 64 characters. This property can contain only characters in the ASCII character set 0 - 127 except the following characters: @ () / [] ' ; : <> , SPACE. Required. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: membershipRule
      value: "{{ membershipRule }}"
      description: |
        The rule that determines members for this group if the group is a dynamic group (groupTypes contains DynamicMembership). For more information about the syntax of the membership rule, see Membership Rules syntax. Returned by default. Supports $filter (eq, ne, not, ge, le, startsWith).
    - name: membershipRuleProcessingState
      value: "{{ membershipRuleProcessingState }}"
      description: |
        Indicates whether the dynamic membership processing is on or paused. Possible values are On or Paused. Returned by default. Supports $filter (eq, ne, not, in).
    - name: onPremisesDomainName
      value: "{{ onPremisesDomainName }}"
      description: |
        Contains the on-premises domain FQDN, also called dnsDomainName synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.
    - name: onPremisesLastSyncDateTime
      value: "{{ onPremisesLastSyncDateTime }}"
      description: |
        Indicates the last time at which the group was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Read-only. Supports $filter (eq, ne, not, ge, le, in).
    - name: onPremisesNetBiosName
      value: "{{ onPremisesNetBiosName }}"
      description: |
        Contains the on-premises netBios name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Read-only.
    - name: onPremisesProvisioningErrors
      description: |
        Errors when using Microsoft synchronization product during provisioning. Returned by default. Supports $filter (eq, not).
      value:
        - category: "{{ category }}"
          occurredDateTime: "{{ occurredDateTime }}"
          propertyCausingError: "{{ propertyCausingError }}"
          value: "{{ value }}"
          @odata.type: "{{ @odata.type }}"
    - name: onPremisesSamAccountName
      value: "{{ onPremisesSamAccountName }}"
      description: |
        Contains the on-premises SAM account name synchronized from the on-premises directory. The property is only populated for customers synchronizing their on-premises directory to Microsoft Entra ID via Microsoft Entra Connect.Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith). Read-only.
    - name: onPremisesSecurityIdentifier
      value: "{{ onPremisesSecurityIdentifier }}"
      description: |
        Contains the on-premises security identifier (SID) for the group synchronized from on-premises to the cloud. Read-only. Returned by default. Supports $filter (eq including on null values).
    - name: onPremisesSyncEnabled
      value: {{ onPremisesSyncEnabled }}
      description: |
        true if this group is synced from an on-premises directory; false if this group was originally synced from an on-premises directory but is no longer synced; null if this object has never synced from an on-premises directory (default). Returned by default. Read-only. Supports $filter (eq, ne, not, in, and eq on null values).
    - name: preferredDataLocation
      value: "{{ preferredDataLocation }}"
      description: |
        The preferred data location for the Microsoft 365 group. By default, the group inherits the group creator's preferred data location. To set this property, the calling app must be granted the Directory.ReadWrite.All permission and the user be assigned at least one of the following Microsoft Entra roles: User Account Administrator Directory Writer  Exchange Administrator  SharePoint Administrator  For more information about this property, see OneDrive Online Multi-Geo. Nullable. Returned by default.
    - name: preferredLanguage
      value: "{{ preferredLanguage }}"
      description: |
        The preferred language for a Microsoft 365 group. Should follow ISO 639-1 Code; for example, en-US. Returned by default. Supports $filter (eq, ne, not, ge, le, in, startsWith, and eq on null values).
    - name: proxyAddresses
      value:
        - "{{ proxyAddresses }}"
      description: |
        Email addresses for the group that direct to the same group mailbox. For example: ['SMTP: bob@contoso.com', 'smtp: bob@sales.contoso.com']. The any operator is required to filter expressions on multi-valued properties. Returned by default. Read-only. Not nullable. Supports $filter (eq, not, ge, le, startsWith, endsWith, /$count eq 0, /$count ne 0).
    - name: renewedDateTime
      value: "{{ renewedDateTime }}"
      description: |
        Timestamp of when the group was last renewed. This value can't be modified directly and is only updated via the renew service action. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z. Returned by default. Supports $filter (eq, ne, not, ge, le, in). Read-only.
    - name: resourceBehaviorOptions
      value:
        - "{{ resourceBehaviorOptions }}"
      description: |
        Specifies the group behaviors that can be set for a Microsoft 365 group during creation. This property can be set only as part of creation (POST). For the list of possible values, see Microsoft 365 group behaviors and provisioning options.
    - name: resourceProvisioningOptions
      value:
        - "{{ resourceProvisioningOptions }}"
      description: |
        Specifies the group resources that are associated with the Microsoft 365 group. The possible value is Team. For more information, see Microsoft 365 group behaviors and provisioning options. Returned by default. Supports $filter (eq, not, startsWith).
    - name: securityEnabled
      value: {{ securityEnabled }}
      description: |
        Specifies whether the group is a security group. Required. Returned by default. Supports $filter (eq, ne, not, in).
    - name: securityIdentifier
      value: "{{ securityIdentifier }}"
      description: |
        Security identifier of the group, used in Windows scenarios. Read-only. Returned by default.
    - name: serviceProvisioningErrors
      description: |
        Errors published by a federated service describing a nontransient, service-specific error regarding the properties or link from a group object.  Supports $filter (eq, not, for isResolved and serviceInstance).
      value:
        - createdDateTime: "{{ createdDateTime }}"
          isResolved: {{ isResolved }}
          serviceInstance: "{{ serviceInstance }}"
          @odata.type: "{{ @odata.type }}"
    - name: theme
      value: "{{ theme }}"
      description: |
        Specifies a Microsoft 365 group's color theme. Possible values are Teal, Purple, Green, Blue, Pink, Orange, or Red. Returned by default.
    - name: uniqueName
      value: "{{ uniqueName }}"
      description: |
        The unique identifier that can be assigned to a group and used as an alternate key. Immutable. Read-only.
    - name: unseenCount
      value: {{ unseenCount }}
      description: |
        Count of conversations that received new posts since the signed-in user last visited the group. Requires $select to retrieve. Supported only on the Get group API (GET /groups/{ID}).
    - name: visibility
      value: "{{ visibility }}"
      description: |
        Specifies the group join policy and group content visibility for groups. The possible values are: Private, Public, or HiddenMembership. HiddenMembership can be set only for Microsoft 365 groups when the groups are created. It can't be updated later. Other values of visibility can be updated after group creation. If visibility value isn't specified during group creation on Microsoft Graph, a security group is created as Private by default, and the Microsoft 365 group is Public. Groups assignable to roles are always Private. To learn more, see group visibility options. Returned by default. Nullable.
    - name: welcomeMessageEnabled
      value: {{ welcomeMessageEnabled }}
    - name: acceptedSenders
      description: |
        The list of users or groups allowed to create posts or calendar events in this group. If this list is nonempty, then only users or groups listed here are allowed to post.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: appRoleAssignments
      description: |
        Represents the app roles granted to a group for an application. Supports $expand.
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
    - name: calendar
      value: "{{ calendar }}"
      description: |
        The group's calendar. Read-only.
    - name: calendarView
      description: |
        The calendar view for the calendar. Read-only.
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
    - name: conversations
      description: |
        The group's conversations.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          hasAttachments: {{ hasAttachments }}
          lastDeliveredDateTime: "{{ lastDeliveredDateTime }}"
          preview: "{{ preview }}"
          topic: "{{ topic }}"
          uniqueSenders: "{{ uniqueSenders }}"
          threads: "{{ threads }}"
    - name: createdOnBehalfOf
      value: "{{ createdOnBehalfOf }}"
      description: |
        The user (or application) that created the group. NOTE: This property isn't set if the user is an administrator. Read-only.
    - name: drive
      value: "{{ drive }}"
      description: |
        The group's default drive. Read-only.
    - name: drives
      description: |
        The group's drives. Read-only.
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
    - name: events
      description: |
        The group's calendar events.
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
        The collection of open extensions defined for the group. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
    - name: groupLifecyclePolicies
      description: |
        The collection of lifecycle policies for this group. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          alternateNotificationEmails: "{{ alternateNotificationEmails }}"
          groupLifetimeInDays: {{ groupLifetimeInDays }}
          managedGroupTypes: "{{ managedGroupTypes }}"
    - name: memberOf
      description: |
        Groups that this group is a member of. HTTP Methods: GET (supported for all groups). Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: members
      description: |
        The members of this group, who can be users, devices, other groups, or service principals. Supports the List members, Add member, and Remove member operations. Nullable. Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=members($select=id,userPrincipalName,displayName).
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: membersWithLicenseErrors
      description: |
        A list of group members with license errors from this group-based license assignment. Read-only.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: onenote
      value: "{{ onenote }}"
    - name: onPremisesSyncBehavior
      value: "{{ onPremisesSyncBehavior }}"
    - name: owners
      description: |
        The owners of the group who can be users or service principals. Limited to 100 owners. Nullable. If this property isn't specified when creating a Microsoft 365 group the calling user (admin or non-admin) is automatically assigned as the group owner. A non-admin user can't explicitly add themselves to this collection when they're creating the group. For more information, see the related known issue. For security groups, the admin user isn't automatically added to this collection. For more information, see the related known issue. Supports $filter (/$count eq 0, /$count ne 0, /$count eq 1, /$count ne 1); Supports $expand including nested $select. For example, /groups?$filter=startsWith(displayName,'Role')&$select=id,displayName&$expand=owners($select=id,userPrincipalName,displayName).
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: permissionGrants
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
        The group's profile photo
    - name: photos
      description: |
        The profile photos owned by the group. Read-only. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          height: {{ height }}
          width: {{ width }}
    - name: planner
      value: "{{ planner }}"
      description: |
        Entry-point to Planner resource that might exist for a Unified Group.
    - name: rejectedSenders
      description: |
        The list of users or groups not allowed to create posts or calendar events in this group. Nullable
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: settings
      description: |
        Settings that can govern this group's behavior, like whether members can invite guests to the group. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          displayName: "{{ displayName }}"
          templateId: "{{ templateId }}"
          values: "{{ values }}"
    - name: sites
      description: |
        The list of SharePoint sites in this group. Access the default site with /sites/root.
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
    - name: team
      value: "{{ team }}"
      description: |
        The team associated with this group.
    - name: threads
      description: |
        The group's conversation threads. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          ccRecipients: "{{ ccRecipients }}"
          hasAttachments: {{ hasAttachments }}
          isLocked: {{ isLocked }}
          lastDeliveredDateTime: "{{ lastDeliveredDateTime }}"
          preview: "{{ preview }}"
          topic: "{{ topic }}"
          toRecipients: "{{ toRecipients }}"
          uniqueSenders: "{{ uniqueSenders }}"
          posts: "{{ posts }}"
    - name: transitiveMemberOf
      description: |
        The groups that a group is a member of, either directly or through nested membership. Nullable.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
    - name: transitiveMembers
      description: |
        The direct and transitive members of a group. Nullable.
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

Create a new group object if it doesn't exist, or update the properties of an existing group object.<br />You can create or update the following types of group: By default, this operation returns only a subset of the properties for each group. For a list of properties that are returned by default, see the Properties section of the group resource. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option.

```sql
UPDATE entraid.groups.groups
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
allowExternalSenders = {{ allowExternalSenders }},
assignedLabels = '{{ assignedLabels }}',
assignedLicenses = '{{ assignedLicenses }}',
autoSubscribeNewMembers = {{ autoSubscribeNewMembers }},
classification = '{{ classification }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
expirationDateTime = '{{ expirationDateTime }}',
groupTypes = '{{ groupTypes }}',
hasMembersWithLicenseErrors = {{ hasMembersWithLicenseErrors }},
hideFromAddressLists = {{ hideFromAddressLists }},
hideFromOutlookClients = {{ hideFromOutlookClients }},
infoCatalogs = '{{ infoCatalogs }}',
isArchived = {{ isArchived }},
isAssignableToRole = {{ isAssignableToRole }},
isManagementRestricted = {{ isManagementRestricted }},
isSubscribedByMail = {{ isSubscribedByMail }},
licenseProcessingState = '{{ licenseProcessingState }}',
mail = '{{ mail }}',
mailEnabled = {{ mailEnabled }},
mailNickname = '{{ mailNickname }}',
membershipRule = '{{ membershipRule }}',
membershipRuleProcessingState = '{{ membershipRuleProcessingState }}',
onPremisesDomainName = '{{ onPremisesDomainName }}',
onPremisesLastSyncDateTime = '{{ onPremisesLastSyncDateTime }}',
onPremisesNetBiosName = '{{ onPremisesNetBiosName }}',
onPremisesProvisioningErrors = '{{ onPremisesProvisioningErrors }}',
onPremisesSamAccountName = '{{ onPremisesSamAccountName }}',
onPremisesSecurityIdentifier = '{{ onPremisesSecurityIdentifier }}',
onPremisesSyncEnabled = {{ onPremisesSyncEnabled }},
preferredDataLocation = '{{ preferredDataLocation }}',
preferredLanguage = '{{ preferredLanguage }}',
proxyAddresses = '{{ proxyAddresses }}',
renewedDateTime = '{{ renewedDateTime }}',
resourceBehaviorOptions = '{{ resourceBehaviorOptions }}',
resourceProvisioningOptions = '{{ resourceProvisioningOptions }}',
securityEnabled = {{ securityEnabled }},
securityIdentifier = '{{ securityIdentifier }}',
serviceProvisioningErrors = '{{ serviceProvisioningErrors }}',
theme = '{{ theme }}',
uniqueName = '{{ uniqueName }}',
unseenCount = {{ unseenCount }},
visibility = '{{ visibility }}',
welcomeMessageEnabled = {{ welcomeMessageEnabled }},
acceptedSenders = '{{ acceptedSenders }}',
appRoleAssignments = '{{ appRoleAssignments }}',
calendar = '{{ calendar }}',
calendarView = '{{ calendarView }}',
conversations = '{{ conversations }}',
createdOnBehalfOf = '{{ createdOnBehalfOf }}',
drive = '{{ drive }}',
drives = '{{ drives }}',
events = '{{ events }}',
extensions = '{{ extensions }}',
groupLifecyclePolicies = '{{ groupLifecyclePolicies }}',
memberOf = '{{ memberOf }}',
members = '{{ members }}',
membersWithLicenseErrors = '{{ membersWithLicenseErrors }}',
onenote = '{{ onenote }}',
onPremisesSyncBehavior = '{{ onPremisesSyncBehavior }}',
owners = '{{ owners }}',
permissionGrants = '{{ permissionGrants }}',
photo = '{{ photo }}',
photos = '{{ photos }}',
planner = '{{ planner }}',
rejectedSenders = '{{ rejectedSenders }}',
settings = '{{ settings }}',
sites = '{{ sites }}',
team = '{{ team }}',
threads = '{{ threads }}',
transitiveMemberOf = '{{ transitiveMemberOf }}',
transitiveMembers = '{{ transitiveMembers }}'
WHERE 
uniqueName = '{{ uniqueName }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
acceptedSenders,
allowExternalSenders,
appRoleAssignments,
assignedLabels,
assignedLicenses,
autoSubscribeNewMembers,
calendar,
calendarView,
classification,
conversations,
createdDateTime,
createdOnBehalfOf,
deletedDateTime,
description,
displayName,
drive,
drives,
events,
expirationDateTime,
extensions,
groupLifecyclePolicies,
groupTypes,
hasMembersWithLicenseErrors,
hideFromAddressLists,
hideFromOutlookClients,
infoCatalogs,
isArchived,
isAssignableToRole,
isManagementRestricted,
isSubscribedByMail,
licenseProcessingState,
mail,
mailEnabled,
mailNickname,
memberOf,
members,
membersWithLicenseErrors,
membershipRule,
membershipRuleProcessingState,
onPremisesDomainName,
onPremisesLastSyncDateTime,
onPremisesNetBiosName,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onenote,
owners,
permissionGrants,
photo,
photos,
planner,
preferredDataLocation,
preferredLanguage,
proxyAddresses,
rejectedSenders,
renewedDateTime,
resourceBehaviorOptions,
resourceProvisioningOptions,
securityEnabled,
securityIdentifier,
serviceProvisioningErrors,
settings,
sites,
team,
theme,
threads,
transitiveMemberOf,
transitiveMembers,
uniqueName,
unseenCount,
visibility,
welcomeMessageEnabled;
```
</TabItem>
<TabItem value="update_2">

Create a new group object if it doesn't exist, or update the properties of an existing group object.<br />You can create or update the following types of group: By default, this operation returns only a subset of the properties for each group. For a list of properties that are returned by default, see the Properties section of the group resource. To get properties that are not returned by default, do a GET operation and specify the properties in a $select OData query option.

```sql
UPDATE entraid.groups.groups
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
deletedDateTime = '{{ deletedDateTime }}',
allowExternalSenders = {{ allowExternalSenders }},
assignedLabels = '{{ assignedLabels }}',
assignedLicenses = '{{ assignedLicenses }}',
autoSubscribeNewMembers = {{ autoSubscribeNewMembers }},
classification = '{{ classification }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
expirationDateTime = '{{ expirationDateTime }}',
groupTypes = '{{ groupTypes }}',
hasMembersWithLicenseErrors = {{ hasMembersWithLicenseErrors }},
hideFromAddressLists = {{ hideFromAddressLists }},
hideFromOutlookClients = {{ hideFromOutlookClients }},
infoCatalogs = '{{ infoCatalogs }}',
isArchived = {{ isArchived }},
isAssignableToRole = {{ isAssignableToRole }},
isManagementRestricted = {{ isManagementRestricted }},
isSubscribedByMail = {{ isSubscribedByMail }},
licenseProcessingState = '{{ licenseProcessingState }}',
mail = '{{ mail }}',
mailEnabled = {{ mailEnabled }},
mailNickname = '{{ mailNickname }}',
membershipRule = '{{ membershipRule }}',
membershipRuleProcessingState = '{{ membershipRuleProcessingState }}',
onPremisesDomainName = '{{ onPremisesDomainName }}',
onPremisesLastSyncDateTime = '{{ onPremisesLastSyncDateTime }}',
onPremisesNetBiosName = '{{ onPremisesNetBiosName }}',
onPremisesProvisioningErrors = '{{ onPremisesProvisioningErrors }}',
onPremisesSamAccountName = '{{ onPremisesSamAccountName }}',
onPremisesSecurityIdentifier = '{{ onPremisesSecurityIdentifier }}',
onPremisesSyncEnabled = {{ onPremisesSyncEnabled }},
preferredDataLocation = '{{ preferredDataLocation }}',
preferredLanguage = '{{ preferredLanguage }}',
proxyAddresses = '{{ proxyAddresses }}',
renewedDateTime = '{{ renewedDateTime }}',
resourceBehaviorOptions = '{{ resourceBehaviorOptions }}',
resourceProvisioningOptions = '{{ resourceProvisioningOptions }}',
securityEnabled = {{ securityEnabled }},
securityIdentifier = '{{ securityIdentifier }}',
serviceProvisioningErrors = '{{ serviceProvisioningErrors }}',
theme = '{{ theme }}',
uniqueName = '{{ uniqueName }}',
unseenCount = {{ unseenCount }},
visibility = '{{ visibility }}',
welcomeMessageEnabled = {{ welcomeMessageEnabled }},
acceptedSenders = '{{ acceptedSenders }}',
appRoleAssignments = '{{ appRoleAssignments }}',
calendar = '{{ calendar }}',
calendarView = '{{ calendarView }}',
conversations = '{{ conversations }}',
createdOnBehalfOf = '{{ createdOnBehalfOf }}',
drive = '{{ drive }}',
drives = '{{ drives }}',
events = '{{ events }}',
extensions = '{{ extensions }}',
groupLifecyclePolicies = '{{ groupLifecyclePolicies }}',
memberOf = '{{ memberOf }}',
members = '{{ members }}',
membersWithLicenseErrors = '{{ membersWithLicenseErrors }}',
onenote = '{{ onenote }}',
onPremisesSyncBehavior = '{{ onPremisesSyncBehavior }}',
owners = '{{ owners }}',
permissionGrants = '{{ permissionGrants }}',
photo = '{{ photo }}',
photos = '{{ photos }}',
planner = '{{ planner }}',
rejectedSenders = '{{ rejectedSenders }}',
settings = '{{ settings }}',
sites = '{{ sites }}',
team = '{{ team }}',
threads = '{{ threads }}',
transitiveMemberOf = '{{ transitiveMemberOf }}',
transitiveMembers = '{{ transitiveMembers }}'
WHERE 
group-id = '{{ group-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
acceptedSenders,
allowExternalSenders,
appRoleAssignments,
assignedLabels,
assignedLicenses,
autoSubscribeNewMembers,
calendar,
calendarView,
classification,
conversations,
createdDateTime,
createdOnBehalfOf,
deletedDateTime,
description,
displayName,
drive,
drives,
events,
expirationDateTime,
extensions,
groupLifecyclePolicies,
groupTypes,
hasMembersWithLicenseErrors,
hideFromAddressLists,
hideFromOutlookClients,
infoCatalogs,
isArchived,
isAssignableToRole,
isManagementRestricted,
isSubscribedByMail,
licenseProcessingState,
mail,
mailEnabled,
mailNickname,
memberOf,
members,
membersWithLicenseErrors,
membershipRule,
membershipRuleProcessingState,
onPremisesDomainName,
onPremisesLastSyncDateTime,
onPremisesNetBiosName,
onPremisesProvisioningErrors,
onPremisesSamAccountName,
onPremisesSecurityIdentifier,
onPremisesSyncBehavior,
onPremisesSyncEnabled,
onenote,
owners,
permissionGrants,
photo,
photos,
planner,
preferredDataLocation,
preferredLanguage,
proxyAddresses,
rejectedSenders,
renewedDateTime,
resourceBehaviorOptions,
resourceProvisioningOptions,
securityEnabled,
securityIdentifier,
serviceProvisioningErrors,
settings,
sites,
team,
theme,
threads,
transitiveMemberOf,
transitiveMembers,
uniqueName,
unseenCount,
visibility,
welcomeMessageEnabled;
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

Delete a group. When deleted, both Microsoft 365 and security groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This doesn't apply to Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.

```sql
DELETE FROM entraid.groups.groups
WHERE uniqueName = '{{ uniqueName }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="delete_2">

Delete a group. When deleted, both Microsoft 365 and security groups are moved to a temporary container and can be restored within 30 days. After that time, they're permanently deleted. This doesn't apply to Distribution groups which are permanently deleted immediately. To learn more, see deletedItems.

```sql
DELETE FROM entraid.groups.groups
WHERE group-id = '{{ group-id }}' --required
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
        { label: 'add_favorite', value: 'add_favorite' },
        { label: 'assign_license', value: 'assign_license' },
        { label: 'check_granted_permissions_for_app', value: 'check_granted_permissions_for_app' },
        { label: 'check_member_groups', value: 'check_member_groups' },
        { label: 'check_member_objects', value: 'check_member_objects' },
        { label: 'get_member_groups', value: 'get_member_groups' },
        { label: 'get_member_objects', value: 'get_member_objects' },
        { label: 'remove_favorite', value: 'remove_favorite' },
        { label: 'renew', value: 'renew' },
        { label: 'reset_unseen_count', value: 'reset_unseen_count' },
        { label: 'restore', value: 'restore' },
        { label: 'retry_service_provisioning', value: 'retry_service_provisioning' },
        { label: 'validate_properties_2', value: 'validate_properties_2' }
    ]}
>
<TabItem value="get_available_extension_properties">

Return all directory extension definitions that are registered in a directory, including through multitenant apps. The following entities support extension properties:

```sql
EXEC entraid.groups.groups.get_available_extension_properties 
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
EXEC entraid.groups.groups.get_by_ids 
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
EXEC entraid.groups.groups.validate_properties 
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
<TabItem value="add_favorite">

Add the group to the list of the current user's favorite groups.  The group shows up in Outlook and Teams favorites. Supported for Microsoft 365 groups only.

```sql
EXEC entraid.groups.groups.add_favorite 
@group-id='{{ group-id }}' --required
;
```
</TabItem>
<TabItem value="assign_license">

Add or remove licenses on a group. Licenses assigned to the group will be assigned to all users in the group. Group-based licensing is an alternative to direct user licensing. To learn more about group-based licensing, see What is group-based licensing in Microsoft Entra ID. To get the subscriptions available in the directory, perform a GET subscribedSkus request.

```sql
EXEC entraid.groups.groups.assign_license 
@group-id='{{ group-id }}' --required 
@@json=
'{
"addLicenses": "{{ addLicenses }}", 
"removeLicenses": "{{ removeLicenses }}"
}'
;
```
</TabItem>
<TabItem value="check_granted_permissions_for_app">

Success

```sql
EXEC entraid.groups.groups.check_granted_permissions_for_app 
@group-id='{{ group-id }}' --required
;
```
</TabItem>
<TabItem value="check_member_groups">

Check for membership in a specified list of group IDs, and return from that list the IDs of groups where a specified object is a member. The specified object can be of one of the following types:<br />- user<br />- group<br />- service principal<br />- organizational contact<br />- device<br />- directory object This function is transitive. You can check up to a maximum of 20 groups per request. This function supports all groups provisioned in Microsoft Entra ID. Because Microsoft 365 groups cannot contain other groups, membership in a Microsoft 365 group is always direct.

```sql
EXEC entraid.groups.groups.check_member_groups 
@group-id='{{ group-id }}' --required 
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
EXEC entraid.groups.groups.check_member_objects 
@group-id='{{ group-id }}' --required 
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
EXEC entraid.groups.groups.get_member_groups 
@group-id='{{ group-id }}' --required 
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
EXEC entraid.groups.groups.get_member_objects 
@group-id='{{ group-id }}' --required 
@@json=
'{
"securityEnabledOnly": {{ securityEnabledOnly }}
}'
;
```
</TabItem>
<TabItem value="remove_favorite">

Remove the group from the list of the current user's favorite groups. Supported for Microsoft 365 groups only.

```sql
EXEC entraid.groups.groups.remove_favorite 
@group-id='{{ group-id }}' --required
;
```
</TabItem>
<TabItem value="renew">

Renew a group's expiration. When a group is renewed, the group expiration is extended by the number of days defined in the policy.

```sql
EXEC entraid.groups.groups.renew 
@group-id='{{ group-id }}' --required
;
```
</TabItem>
<TabItem value="reset_unseen_count">

Reset the unseenCount of all the posts that the current user hasn't seen since their last visit. Supported for Microsoft 365 groups only.

```sql
EXEC entraid.groups.groups.reset_unseen_count 
@group-id='{{ group-id }}' --required
;
```
</TabItem>
<TabItem value="restore">

Restore a recently deleted directory object from deleted items. The following types are supported:<br />- administrativeUnit<br />- application<br />- agentIdentityBlueprint<br />- agentIdentity<br />- agentIdentityBlueprintPrincipal<br />- agentUser<br />- certificateBasedAuthPki<br />- certificateAuthorityDetail<br />- group<br />- servicePrincipal<br />- user If an item is accidentally deleted, you can fully restore the item. Additionally, restoring an application doesn't automatically restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.

```sql
EXEC entraid.groups.groups.restore 
@group-id='{{ group-id }}' --required
;
```
</TabItem>
<TabItem value="retry_service_provisioning">

Retry the group service provisioning.

```sql
EXEC entraid.groups.groups.retry_service_provisioning 
@group-id='{{ group-id }}' --required
;
```
</TabItem>
<TabItem value="validate_properties_2">

Validate that a Microsoft 365 group's display name or mail nickname complies with naming policies. Clients can use this API to determine whether a display name or mail nickname is valid before trying to update a Microsoft 365 group. To validate the properties before creating a group, use the directoryobject:validateProperties function. The following policy validations are performed for the display name and mail nickname properties: This API only returns the first validation failure that is encountered. If the properties fail multiple validations, only the first validation failure is returned. However, you can validate both the mail nickname and the display name and receive a collection of validation errors if you are only validating the prefix and suffix naming policy. To learn more about configuring naming policies, see Configure naming policy.

```sql
EXEC entraid.groups.groups.validate_properties_2 
@group-id='{{ group-id }}' --required 
@@json=
'{
"displayName": "{{ displayName }}", 
"mailNickname": "{{ mailNickname }}", 
"onBehalfOfUserId": "{{ onBehalfOfUserId }}"
}'
;
```
</TabItem>
</Tabs>
