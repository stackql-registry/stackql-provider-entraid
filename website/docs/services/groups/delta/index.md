--- 
title: delta
hide_title: false
hide_table_of_contents: false
keywords:
  - delta
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

Creates, updates, deletes, gets or lists a <code>delta</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="delta" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.groups.delta" /></td></tr>
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
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get newly created, updated, or deleted groups, including group membership changes, without having to perform a full read of the entire group collection. For more information, see Use delta query to track changes in Microsoft Graph data for details.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get newly created, updated, or deleted groups, including group membership changes, without having to perform a full read of the entire group collection. For more information, see Use delta query to track changes in Microsoft Graph data for details.

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
FROM entraid.groups.delta
WHERE $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
AND $search = '{{ $search }}'
AND $filter = '{{ $filter }}'
AND $count = '{{ $count }}'
AND $select = '{{ $select }}'
AND $orderby = '{{ $orderby }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
