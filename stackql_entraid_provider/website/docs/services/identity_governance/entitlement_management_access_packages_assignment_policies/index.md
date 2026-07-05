--- 
title: entitlement_management_access_packages_assignment_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_access_packages_assignment_policies
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_access_packages_assignment_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_access_packages_assignment_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_access_packages_assignment_policies" /></td></tr>
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
    <td><CopyableCode code="accessPackage" /></td>
    <td><code></code></td>
    <td>Access package containing this policy. Read-only. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedTargetScope" /></td>
    <td><code></code></td>
    <td>Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, allDirectoryAgentIdentities, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticRequestSettings" /></td>
    <td><code></code></td>
    <td>This property is only present for an auto assignment policy; if absent, this is a request-based policy.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog" /></td>
    <td><code></code></td>
    <td>Catalog of the access package containing this policy. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customExtensionStageSettings" /></td>
    <td><code>array</code></td>
    <td>The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code></code></td>
    <td>The expiration date for assignments created in this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSettings" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="questions" /></td>
    <td><code>array</code></td>
    <td>Questions that are posed to the  requestor.</td>
</tr>
<tr>
    <td><CopyableCode code="requestApprovalSettings" /></td>
    <td><code></code></td>
    <td>Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.</td>
</tr>
<tr>
    <td><CopyableCode code="requestorSettings" /></td>
    <td><code></code></td>
    <td>Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewSettings" /></td>
    <td><code></code></td>
    <td>Settings for access reviews of assignments through this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="specificAllowedTargets" /></td>
    <td><code>array</code></td>
    <td>The principals that can be assigned access from an access package through this policy.</td>
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
    <td><CopyableCode code="accessPackage" /></td>
    <td><code></code></td>
    <td>Access package containing this policy. Read-only. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedTargetScope" /></td>
    <td><code></code></td>
    <td>Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, allDirectoryAgentIdentities, unknownFutureValue.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticRequestSettings" /></td>
    <td><code></code></td>
    <td>This property is only present for an auto assignment policy; if absent, this is a request-based policy.</td>
</tr>
<tr>
    <td><CopyableCode code="catalog" /></td>
    <td><code></code></td>
    <td>Catalog of the access package containing this policy. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="customExtensionStageSettings" /></td>
    <td><code>array</code></td>
    <td>The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="expiration" /></td>
    <td><code></code></td>
    <td>The expiration date for assignments created in this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="notificationSettings" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="questions" /></td>
    <td><code>array</code></td>
    <td>Questions that are posed to the  requestor.</td>
</tr>
<tr>
    <td><CopyableCode code="requestApprovalSettings" /></td>
    <td><code></code></td>
    <td>Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.</td>
</tr>
<tr>
    <td><CopyableCode code="requestorSettings" /></td>
    <td><code></code></td>
    <td>Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.</td>
</tr>
<tr>
    <td><CopyableCode code="reviewSettings" /></td>
    <td><code></code></td>
    <td>Settings for access reviews of assignments through this policy.</td>
</tr>
<tr>
    <td><CopyableCode code="specificAllowedTargets" /></td>
    <td><code>array</code></td>
    <td>The principals that can be assigned access from an access package through this policy.</td>
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
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a>, <a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a></td>
    <td></td>
    <td>Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a></td>
    <td></td>
    <td>Read-only. Nullable. Supports $expand.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a>, <a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a>, <a href="#parameter-access_package_assignment_policy_id"><code>access_package_assignment_policy_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
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
<tr id="parameter-access_package_assignment_policy_id">
    <td><CopyableCode code="access_package_assignment_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackageAssignmentPolicy</td>
</tr>
<tr id="parameter-access_package_id">
    <td><CopyableCode code="access_package_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackage</td>
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

Read-only. Nullable. Supports $expand.

```sql
SELECT
id,
accessPackage,
allowedTargetScope,
automaticRequestSettings,
catalog,
createdDateTime,
customExtensionStageSettings,
description,
displayName,
expiration,
modifiedDateTime,
notificationSettings,
questions,
requestApprovalSettings,
requestorSettings,
reviewSettings,
specificAllowedTargets
FROM entra_id.identity_governance.entitlement_management_access_packages_assignment_policies
WHERE access_package_id = '{{ access_package_id }}' -- required
AND access_package_assignment_policy_id = '{{ access_package_assignment_policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Read-only. Nullable. Supports $expand.

```sql
SELECT
id,
accessPackage,
allowedTargetScope,
automaticRequestSettings,
catalog,
createdDateTime,
customExtensionStageSettings,
description,
displayName,
expiration,
modifiedDateTime,
notificationSettings,
questions,
requestApprovalSettings,
requestorSettings,
reviewSettings,
specificAllowedTargets
FROM entra_id.identity_governance.entitlement_management_access_packages_assignment_policies
WHERE access_package_id = '{{ access_package_id }}' -- required
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
INSERT INTO entra_id.identity_governance.entitlement_management_access_packages_assignment_policies (
id,
allowedTargetScope,
automaticRequestSettings,
createdDateTime,
description,
displayName,
expiration,
modifiedDateTime,
notificationSettings,
requestApprovalSettings,
requestorSettings,
reviewSettings,
specificAllowedTargets,
accessPackage,
catalog,
customExtensionStageSettings,
questions,
access_package_id
)
SELECT 
'{{ id }}',
'{{ allowedTargetScope }}',
'{{ automaticRequestSettings }}',
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ expiration }}',
'{{ modifiedDateTime }}',
'{{ notificationSettings }}',
'{{ requestApprovalSettings }}',
'{{ requestorSettings }}',
'{{ reviewSettings }}',
'{{ specificAllowedTargets }}',
'{{ accessPackage }}',
'{{ catalog }}',
'{{ customExtensionStageSettings }}',
'{{ questions }}',
'{{ access_package_id }}'
RETURNING
id,
accessPackage,
allowedTargetScope,
automaticRequestSettings,
catalog,
createdDateTime,
customExtensionStageSettings,
description,
displayName,
expiration,
modifiedDateTime,
notificationSettings,
questions,
requestApprovalSettings,
requestorSettings,
reviewSettings,
specificAllowedTargets
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_access_packages_assignment_policies
  props:
    - name: access_package_id
      value: "{{ access_package_id }}"
      description: Required parameter for the entitlement_management_access_packages_assignment_policies resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: allowedTargetScope
      value: "{{ allowedTargetScope }}"
      description: |
        Principals that can be assigned the access package through this policy. The possible values are: notSpecified, specificDirectoryUsers, specificConnectedOrganizationUsers, specificDirectoryServicePrincipals, allMemberUsers, allDirectoryUsers, allDirectoryServicePrincipals, allConfiguredConnectedOrganizationUsers, allExternalUsers, allDirectoryAgentIdentities, unknownFutureValue.
    - name: automaticRequestSettings
      value: "{{ automaticRequestSettings }}"
      description: |
        This property is only present for an auto assignment policy; if absent, this is a request-based policy.
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: description
      value: "{{ description }}"
      description: |
        The description of the policy.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name of the policy.
    - name: expiration
      value: "{{ expiration }}"
      description: |
        The expiration date for assignments created in this policy.
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    - name: notificationSettings
      value: "{{ notificationSettings }}"
    - name: requestApprovalSettings
      value: "{{ requestApprovalSettings }}"
      description: |
        Specifies the settings for approval of requests for an access package assignment through this policy. For example, if approval is required for new requests.
    - name: requestorSettings
      value: "{{ requestorSettings }}"
      description: |
        Provides additional settings to select who can create a request for an access package assignment through this policy, and what they can include in their request.
    - name: reviewSettings
      value: "{{ reviewSettings }}"
      description: |
        Settings for access reviews of assignments through this policy.
    - name: specificAllowedTargets
      description: |
        The principals that can be assigned access from an access package through this policy.
      value:
    - name: accessPackage
      value: "{{ accessPackage }}"
      description: |
        Access package containing this policy. Read-only. Supports $expand.
    - name: catalog
      value: "{{ catalog }}"
      description: |
        Catalog of the access package containing this policy. Read-only.
    - name: customExtensionStageSettings
      description: |
        The collection of stages when to execute one or more custom access package workflow extensions. Supports $expand.
      value:
        - id: "{{ id }}"
          stage: "{{ stage }}"
          customExtension: "{{ customExtension }}"
    - name: questions
      description: |
        Questions that are posed to the  requestor.
      value:
        - id: "{{ id }}"
          isAnswerEditable: {{ isAnswerEditable }}
          isRequired: {{ isRequired }}
          localizations: "{{ localizations }}"
          sequence: {{ sequence }}
          text: "{{ text }}"
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

No description available.

```sql
UPDATE entra_id.identity_governance.entitlement_management_access_packages_assignment_policies
SET 
id = '{{ id }}',
allowedTargetScope = '{{ allowedTargetScope }}',
automaticRequestSettings = '{{ automaticRequestSettings }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
expiration = '{{ expiration }}',
modifiedDateTime = '{{ modifiedDateTime }}',
notificationSettings = '{{ notificationSettings }}',
requestApprovalSettings = '{{ requestApprovalSettings }}',
requestorSettings = '{{ requestorSettings }}',
reviewSettings = '{{ reviewSettings }}',
specificAllowedTargets = '{{ specificAllowedTargets }}',
accessPackage = '{{ accessPackage }}',
catalog = '{{ catalog }}',
customExtensionStageSettings = '{{ customExtensionStageSettings }}',
questions = '{{ questions }}'
WHERE 
access_package_id = '{{ access_package_id }}' --required
AND access_package_assignment_policy_id = '{{ access_package_assignment_policy_id }}' --required
RETURNING
id,
accessPackage,
allowedTargetScope,
automaticRequestSettings,
catalog,
createdDateTime,
customExtensionStageSettings,
description,
displayName,
expiration,
modifiedDateTime,
notificationSettings,
questions,
requestApprovalSettings,
requestorSettings,
reviewSettings,
specificAllowedTargets;
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
DELETE FROM entra_id.identity_governance.entitlement_management_access_packages_assignment_policies
WHERE access_package_id = '{{ access_package_id }}' --required
AND access_package_assignment_policy_id = '{{ access_package_assignment_policy_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
