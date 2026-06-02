--- 
title: entitlement_management_access_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_access_packages
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_access_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_access_packages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.entitlement_management_access_packages" /></td></tr>
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
    <td><CopyableCode code="accessPackagesIncompatibleWith" /></td>
    <td><code>array</code></td>
    <td>The access packages that are incompatible with this package. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentPolicies" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog" /></td>
    <td><code></code></td>
    <td>Required when creating the access package. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the access package.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Required. The display name of the access package. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="incompatibleAccessPackages" /></td>
    <td><code>array</code></td>
    <td>The access packages whose assigned users are ineligible to be assigned this access package.</td>
</tr>
<tr>
    <td><CopyableCode code="incompatibleGroups" /></td>
    <td><code>array</code></td>
    <td>The groups whose members are ineligible to be assigned this access package.</td>
</tr>
<tr>
    <td><CopyableCode code="isHidden" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the access package is hidden from the requestor.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRoleScopes" /></td>
    <td><code>array</code></td>
    <td>The resource roles and scopes in this access package.</td>
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
    <td><CopyableCode code="accessPackagesIncompatibleWith" /></td>
    <td><code>array</code></td>
    <td>The access packages that are incompatible with this package. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentPolicies" /></td>
    <td><code>array</code></td>
    <td>Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog" /></td>
    <td><code></code></td>
    <td>Required when creating the access package. Read-only. Nullable.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the access package.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Required. The display name of the access package. Supports $filter (eq, contains).</td>
</tr>
<tr>
    <td><CopyableCode code="incompatibleAccessPackages" /></td>
    <td><code>array</code></td>
    <td>The access packages whose assigned users are ineligible to be assigned this access package.</td>
</tr>
<tr>
    <td><CopyableCode code="incompatibleGroups" /></td>
    <td><code>array</code></td>
    <td>The groups whose members are ineligible to be assigned this access package.</td>
</tr>
<tr>
    <td><CopyableCode code="isHidden" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the access package is hidden from the requestor.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRoleScopes" /></td>
    <td><code>array</code></td>
    <td>The resource roles and scopes in this access package.</td>
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
    <td><a href="#parameter-accessPackage-id"><code>accessPackage-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the properties and relationships of an accessPackage object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve a list of accessPackage objects.  The resulting list includes all the access packages that the caller has access to read, across all catalogs.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new accessPackage object. The access package will be added to an existing accessPackageCatalog.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-accessPackage-id"><code>accessPackage-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update an existing accessPackage object to change one or more of its properties, such as the display name or description.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-accessPackage-id"><code>accessPackage-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete an accessPackage object. You cannot delete an access package if it has any accessPackageAssignment.</td>
</tr>
<tr>
    <td><a href="#get_applicable_policy_requirements"><CopyableCode code="get_applicable_policy_requirements" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-accessPackage-id"><code>accessPackage-id</code></a></td>
    <td></td>
    <td>In Microsoft Entra entitlement management, this action retrieves a list of accessPackageAssignmentRequestRequirements objects that the currently signed-in user can use to create an accessPackageAssignmentRequest.  Each requirement object corresponds to an access package assignment policy that the currently signed-in user is allowed to request an assignment for.</td>
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
<tr id="parameter-accessPackage-id">
    <td><CopyableCode code="accessPackage-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackage</td>
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

Retrieve the properties and relationships of an accessPackage object.

```sql
SELECT
id,
@odata.type,
accessPackagesIncompatibleWith,
assignmentPolicies,
catalog,
createdDateTime,
description,
displayName,
incompatibleAccessPackages,
incompatibleGroups,
isHidden,
modifiedDateTime,
resourceRoleScopes
FROM entraid.identity_governance.entitlement_management_access_packages
WHERE accessPackage-id = '{{ accessPackage-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of accessPackage objects.  The resulting list includes all the access packages that the caller has access to read, across all catalogs.

```sql
SELECT
id,
@odata.type,
accessPackagesIncompatibleWith,
assignmentPolicies,
catalog,
createdDateTime,
description,
displayName,
incompatibleAccessPackages,
incompatibleGroups,
isHidden,
modifiedDateTime,
resourceRoleScopes
FROM entraid.identity_governance.entitlement_management_access_packages
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

Create a new accessPackage object. The access package will be added to an existing accessPackageCatalog.

```sql
INSERT INTO entraid.identity_governance.entitlement_management_access_packages (
id,
@odata.type,
createdDateTime,
description,
displayName,
isHidden,
modifiedDateTime,
accessPackagesIncompatibleWith,
assignmentPolicies,
catalog,
incompatibleAccessPackages,
incompatibleGroups,
resourceRoleScopes
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
{{ isHidden }},
'{{ modifiedDateTime }}',
'{{ accessPackagesIncompatibleWith }}',
'{{ assignmentPolicies }}',
'{{ catalog }}',
'{{ incompatibleAccessPackages }}',
'{{ incompatibleGroups }}',
'{{ resourceRoleScopes }}'
RETURNING
id,
@odata.type,
accessPackagesIncompatibleWith,
assignmentPolicies,
catalog,
createdDateTime,
description,
displayName,
incompatibleAccessPackages,
incompatibleGroups,
isHidden,
modifiedDateTime,
resourceRoleScopes
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_access_packages
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the access package.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Required. The display name of the access package. Supports $filter (eq, contains).
    - name: isHidden
      value: {{ isHidden }}
      description: |
        Indicates whether the access package is hidden from the requestor.
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    - name: accessPackagesIncompatibleWith
      description: |
        The access packages that are incompatible with this package. Read-only.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          isHidden: {{ isHidden }}
          modifiedDateTime: "{{ modifiedDateTime }}"
          accessPackagesIncompatibleWith: "{{ accessPackagesIncompatibleWith }}"
          assignmentPolicies: "{{ assignmentPolicies }}"
          catalog: "{{ catalog }}"
          incompatibleAccessPackages: "{{ incompatibleAccessPackages }}"
          incompatibleGroups: "{{ incompatibleGroups }}"
          resourceRoleScopes: "{{ resourceRoleScopes }}"
    - name: assignmentPolicies
      description: |
        Read-only. Nullable. Supports $expand.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          allowedTargetScope: "{{ allowedTargetScope }}"
          automaticRequestSettings: "{{ automaticRequestSettings }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          expiration: "{{ expiration }}"
          modifiedDateTime: "{{ modifiedDateTime }}"
          notificationSettings: "{{ notificationSettings }}"
          requestApprovalSettings: "{{ requestApprovalSettings }}"
          requestorSettings: "{{ requestorSettings }}"
          reviewSettings: "{{ reviewSettings }}"
          specificAllowedTargets: "{{ specificAllowedTargets }}"
          accessPackage: "{{ accessPackage }}"
          catalog: "{{ catalog }}"
          customExtensionStageSettings: "{{ customExtensionStageSettings }}"
          questions: "{{ questions }}"
    - name: catalog
      value: "{{ catalog }}"
      description: |
        Required when creating the access package. Read-only. Nullable.
    - name: incompatibleAccessPackages
      description: |
        The access packages whose assigned users are ineligible to be assigned this access package.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          isHidden: {{ isHidden }}
          modifiedDateTime: "{{ modifiedDateTime }}"
          accessPackagesIncompatibleWith: "{{ accessPackagesIncompatibleWith }}"
          assignmentPolicies: "{{ assignmentPolicies }}"
          catalog: "{{ catalog }}"
          incompatibleAccessPackages: "{{ incompatibleAccessPackages }}"
          incompatibleGroups: "{{ incompatibleGroups }}"
          resourceRoleScopes: "{{ resourceRoleScopes }}"
    - name: incompatibleGroups
      description: |
        The groups whose members are ineligible to be assigned this access package.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          deletedDateTime: "{{ deletedDateTime }}"
          allowExternalSenders: {{ allowExternalSenders }}
          assignedLabels: "{{ assignedLabels }}"
          assignedLicenses: "{{ assignedLicenses }}"
          autoSubscribeNewMembers: {{ autoSubscribeNewMembers }}
          classification: "{{ classification }}"
          createdDateTime: "{{ createdDateTime }}"
          description: "{{ description }}"
          displayName: "{{ displayName }}"
          expirationDateTime: "{{ expirationDateTime }}"
          groupTypes: "{{ groupTypes }}"
          hasMembersWithLicenseErrors: {{ hasMembersWithLicenseErrors }}
          hideFromAddressLists: {{ hideFromAddressLists }}
          hideFromOutlookClients: {{ hideFromOutlookClients }}
          infoCatalogs: "{{ infoCatalogs }}"
          isArchived: {{ isArchived }}
          isAssignableToRole: {{ isAssignableToRole }}
          isManagementRestricted: {{ isManagementRestricted }}
          isSubscribedByMail: {{ isSubscribedByMail }}
          licenseProcessingState: "{{ licenseProcessingState }}"
          mail: "{{ mail }}"
          mailEnabled: {{ mailEnabled }}
          mailNickname: "{{ mailNickname }}"
          membershipRule: "{{ membershipRule }}"
          membershipRuleProcessingState: "{{ membershipRuleProcessingState }}"
          onPremisesDomainName: "{{ onPremisesDomainName }}"
          onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
          onPremisesNetBiosName: "{{ onPremisesNetBiosName }}"
          onPremisesProvisioningErrors: "{{ onPremisesProvisioningErrors }}"
          onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
          onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
          onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
          preferredDataLocation: "{{ preferredDataLocation }}"
          preferredLanguage: "{{ preferredLanguage }}"
          proxyAddresses: "{{ proxyAddresses }}"
          renewedDateTime: "{{ renewedDateTime }}"
          resourceBehaviorOptions: "{{ resourceBehaviorOptions }}"
          resourceProvisioningOptions: "{{ resourceProvisioningOptions }}"
          securityEnabled: {{ securityEnabled }}
          securityIdentifier: "{{ securityIdentifier }}"
          serviceProvisioningErrors: "{{ serviceProvisioningErrors }}"
          theme: "{{ theme }}"
          uniqueName: "{{ uniqueName }}"
          unseenCount: {{ unseenCount }}
          visibility: "{{ visibility }}"
          welcomeMessageEnabled: {{ welcomeMessageEnabled }}
          acceptedSenders: "{{ acceptedSenders }}"
          appRoleAssignments: "{{ appRoleAssignments }}"
          calendar: "{{ calendar }}"
          calendarView: "{{ calendarView }}"
          conversations: "{{ conversations }}"
          createdOnBehalfOf: "{{ createdOnBehalfOf }}"
          drive: "{{ drive }}"
          drives: "{{ drives }}"
          events: "{{ events }}"
          extensions: "{{ extensions }}"
          groupLifecyclePolicies: "{{ groupLifecyclePolicies }}"
          memberOf: "{{ memberOf }}"
          members: "{{ members }}"
          membersWithLicenseErrors: "{{ membersWithLicenseErrors }}"
          onenote: "{{ onenote }}"
          onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
          owners: "{{ owners }}"
          permissionGrants: "{{ permissionGrants }}"
          photo: "{{ photo }}"
          photos: "{{ photos }}"
          planner: "{{ planner }}"
          rejectedSenders: "{{ rejectedSenders }}"
          settings: "{{ settings }}"
          sites: "{{ sites }}"
          team: "{{ team }}"
          threads: "{{ threads }}"
          transitiveMemberOf: "{{ transitiveMemberOf }}"
          transitiveMembers: "{{ transitiveMembers }}"
    - name: resourceRoleScopes
      description: |
        The resource roles and scopes in this access package.
      value:
        - id: "{{ id }}"
          @odata.type: "{{ @odata.type }}"
          createdDateTime: "{{ createdDateTime }}"
          role: "{{ role }}"
          scope: "{{ scope }}"
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

Update an existing accessPackage object to change one or more of its properties, such as the display name or description.

```sql
UPDATE entraid.identity_governance.entitlement_management_access_packages
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
isHidden = {{ isHidden }},
modifiedDateTime = '{{ modifiedDateTime }}',
accessPackagesIncompatibleWith = '{{ accessPackagesIncompatibleWith }}',
assignmentPolicies = '{{ assignmentPolicies }}',
catalog = '{{ catalog }}',
incompatibleAccessPackages = '{{ incompatibleAccessPackages }}',
incompatibleGroups = '{{ incompatibleGroups }}',
resourceRoleScopes = '{{ resourceRoleScopes }}'
WHERE 
accessPackage-id = '{{ accessPackage-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
accessPackagesIncompatibleWith,
assignmentPolicies,
catalog,
createdDateTime,
description,
displayName,
incompatibleAccessPackages,
incompatibleGroups,
isHidden,
modifiedDateTime,
resourceRoleScopes;
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

Delete an accessPackage object. You cannot delete an access package if it has any accessPackageAssignment.

```sql
DELETE FROM entraid.identity_governance.entitlement_management_access_packages
WHERE accessPackage-id = '{{ accessPackage-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_applicable_policy_requirements"
    values={[
        { label: 'get_applicable_policy_requirements', value: 'get_applicable_policy_requirements' }
    ]}
>
<TabItem value="get_applicable_policy_requirements">

In Microsoft Entra entitlement management, this action retrieves a list of accessPackageAssignmentRequestRequirements objects that the currently signed-in user can use to create an accessPackageAssignmentRequest.  Each requirement object corresponds to an access package assignment policy that the currently signed-in user is allowed to request an assignment for.

```sql
EXEC entraid.identity_governance.entitlement_management_access_packages.get_applicable_policy_requirements 
@accessPackage-id='{{ accessPackage-id }}' --required
;
```
</TabItem>
</Tabs>
