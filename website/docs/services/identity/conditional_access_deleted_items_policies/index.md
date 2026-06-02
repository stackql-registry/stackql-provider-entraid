--- 
title: conditional_access_deleted_items_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - conditional_access_deleted_items_policies
  - identity
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

Creates, updates, deletes, gets or lists a <code>conditional_access_deleted_items_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="conditional_access_deleted_items_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.conditional_access_deleted_items_policies" /></td></tr>
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
    <td>Specifies the identifier of a conditionalAccessPolicy object. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="conditions" /></td>
    <td><code>object</code></td>
    <td> (title: conditionalAccessConditionSet)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td> (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Specifies a display name for the conditionalAccessPolicy object.</td>
</tr>
<tr>
    <td><CopyableCode code="grantControls" /></td>
    <td><code></code></td>
    <td>Specifies the grant controls that must be fulfilled to pass the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionControls" /></td>
    <td><code></code></td>
    <td>Specifies the session controls that are enforced after sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td> (enabled, disabled, enabledForReportingButNotEnforced) (title: conditionalAccessPolicyState)</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Specifies the unique identifier of a Conditional Access template. Inherited from entity.</td>
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
    <td>Specifies the identifier of a conditionalAccessPolicy object. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="conditions" /></td>
    <td><code>object</code></td>
    <td> (title: conditionalAccessConditionSet)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td> (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Specifies a display name for the conditionalAccessPolicy object.</td>
</tr>
<tr>
    <td><CopyableCode code="grantControls" /></td>
    <td><code></code></td>
    <td>Specifies the grant controls that must be fulfilled to pass the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionControls" /></td>
    <td><code></code></td>
    <td>Specifies the session controls that are enforced after sign-in.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td> (enabled, disabled, enabledForReportingButNotEnforced) (title: conditionalAccessPolicyState)</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Specifies the unique identifier of a Conditional Access template. Inherited from entity.</td>
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
    <td><a href="#parameter-conditionalAccessPolicy-id"><code>conditionalAccessPolicy-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td></td>
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
    <td><a href="#parameter-conditionalAccessPolicy-id"><code>conditionalAccessPolicy-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-conditionalAccessPolicy-id"><code>conditionalAccessPolicy-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-conditionalAccessPolicy-id"><code>conditionalAccessPolicy-id</code></a></td>
    <td></td>
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
<tr id="parameter-conditionalAccessPolicy-id">
    <td><CopyableCode code="conditionalAccessPolicy-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of conditionalAccessPolicy</td>
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

Retrieved navigation property

```sql
SELECT
id,
@odata.type,
conditions,
createdDateTime,
deletedDateTime,
description,
displayName,
grantControls,
modifiedDateTime,
sessionControls,
state,
templateId
FROM entra_id.identity.conditional_access_deleted_items_policies
WHERE conditionalAccessPolicy-id = '{{ conditionalAccessPolicy-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieved collection

```sql
SELECT
id,
@odata.type,
conditions,
createdDateTime,
deletedDateTime,
description,
displayName,
grantControls,
modifiedDateTime,
sessionControls,
state,
templateId
FROM entra_id.identity.conditional_access_deleted_items_policies
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
INSERT INTO entra_id.identity.conditional_access_deleted_items_policies (
deletedDateTime,
@odata.type,
conditions,
createdDateTime,
description,
displayName,
grantControls,
id,
modifiedDateTime,
sessionControls,
state,
templateId
)
SELECT 
'{{ deletedDateTime }}',
'{{ @odata.type }}' /* required */,
'{{ conditions }}',
'{{ createdDateTime }}',
'{{ description }}',
'{{ displayName }}',
'{{ grantControls }}',
'{{ id }}',
'{{ modifiedDateTime }}',
'{{ sessionControls }}',
'{{ state }}',
'{{ templateId }}'
RETURNING
id,
@odata.type,
conditions,
createdDateTime,
deletedDateTime,
description,
displayName,
grantControls,
modifiedDateTime,
sessionControls,
state,
templateId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: conditional_access_deleted_items_policies
  props:
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: conditions
      value:
        applications:
          applicationFilter:
            mode: "{{ mode }}"
            rule: "{{ rule }}"
            @odata.type: "{{ @odata.type }}"
          excludeApplications:
            - "{{ excludeApplications }}"
          includeApplications:
            - "{{ includeApplications }}"
          includeAuthenticationContextClassReferences:
            - "{{ includeAuthenticationContextClassReferences }}"
          includeUserActions:
            - "{{ includeUserActions }}"
          @odata.type: "{{ @odata.type }}"
        authenticationFlows:
          transferMethods: "{{ transferMethods }}"
          @odata.type: "{{ @odata.type }}"
        clientApplications:
          excludeServicePrincipals:
            - "{{ excludeServicePrincipals }}"
          includeServicePrincipals:
            - "{{ includeServicePrincipals }}"
          servicePrincipalFilter:
            mode: "{{ mode }}"
            rule: "{{ rule }}"
            @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        clientAppTypes:
          - "{{ clientAppTypes }}"
        devices:
          deviceFilter:
            mode: "{{ mode }}"
            rule: "{{ rule }}"
            @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        insiderRiskLevels: "{{ insiderRiskLevels }}"
        locations:
          excludeLocations:
            - "{{ excludeLocations }}"
          includeLocations:
            - "{{ includeLocations }}"
          @odata.type: "{{ @odata.type }}"
        platforms:
          excludePlatforms:
            - "{{ excludePlatforms }}"
          includePlatforms:
            - "{{ includePlatforms }}"
          @odata.type: "{{ @odata.type }}"
        servicePrincipalRiskLevels:
          - "{{ servicePrincipalRiskLevels }}"
        signInRiskLevels:
          - "{{ signInRiskLevels }}"
        userRiskLevels:
          - "{{ userRiskLevels }}"
        users:
          excludeGroups:
            - "{{ excludeGroups }}"
          excludeGuestsOrExternalUsers:
            externalTenants:
              membershipKind: "{{ membershipKind }}"
              @odata.type: "{{ @odata.type }}"
            guestOrExternalUserTypes: "{{ guestOrExternalUserTypes }}"
            @odata.type: "{{ @odata.type }}"
          excludeRoles:
            - "{{ excludeRoles }}"
          excludeUsers:
            - "{{ excludeUsers }}"
          includeGroups:
            - "{{ includeGroups }}"
          includeGuestsOrExternalUsers:
            externalTenants:
              membershipKind: "{{ membershipKind }}"
              @odata.type: "{{ @odata.type }}"
            guestOrExternalUserTypes: "{{ guestOrExternalUserTypes }}"
            @odata.type: "{{ @odata.type }}"
          includeRoles:
            - "{{ includeRoles }}"
          includeUsers:
            - "{{ includeUsers }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: createdDateTime
      value: "{{ createdDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
    - name: description
      value: "{{ description }}"
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Specifies a display name for the conditionalAccessPolicy object.
    - name: grantControls
      value: "{{ grantControls }}"
      description: |
        Specifies the grant controls that must be fulfilled to pass the policy.
    - name: id
      value: "{{ id }}"
      description: |
        Specifies the identifier of a conditionalAccessPolicy object. Read-only.
    - name: modifiedDateTime
      value: "{{ modifiedDateTime }}"
      description: |
        The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly.
    - name: sessionControls
      value: "{{ sessionControls }}"
      description: |
        Specifies the session controls that are enforced after sign-in.
    - name: state
      value: "{{ state }}"
      valid_values: ['enabled', 'disabled', 'enabledForReportingButNotEnforced']
    - name: templateId
      value: "{{ templateId }}"
      description: |
        Specifies the unique identifier of a Conditional Access template. Inherited from entity.
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
UPDATE entra_id.identity.conditional_access_deleted_items_policies
SET 
deletedDateTime = '{{ deletedDateTime }}',
@odata.type = '{{ @odata.type }}',
conditions = '{{ conditions }}',
createdDateTime = '{{ createdDateTime }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
grantControls = '{{ grantControls }}',
id = '{{ id }}',
modifiedDateTime = '{{ modifiedDateTime }}',
sessionControls = '{{ sessionControls }}',
state = '{{ state }}',
templateId = '{{ templateId }}'
WHERE 
conditionalAccessPolicy-id = '{{ conditionalAccessPolicy-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
conditions,
createdDateTime,
deletedDateTime,
description,
displayName,
grantControls,
modifiedDateTime,
sessionControls,
state,
templateId;
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
DELETE FROM entra_id.identity.conditional_access_deleted_items_policies
WHERE conditionalAccessPolicy-id = '{{ conditionalAccessPolicy-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="restore"
    values={[
        { label: 'restore', value: 'restore' }
    ]}
>
<TabItem value="restore">

Success

```sql
EXEC entra_id.identity.conditional_access_deleted_items_policies.restore 
@conditionalAccessPolicy-id='{{ conditionalAccessPolicy-id }}' --required
;
```
</TabItem>
</Tabs>
