--- 
title: conditional_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - conditional_access_policies
  - policies
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

Creates, updates, deletes, gets or lists a <code>conditional_access_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="conditional_access_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.conditional_access_policies" /></td></tr>
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
    <td><CopyableCode code="conditions" /></td>
    <td><code>object</code></td>
    <td> (title: conditionalAccessConditionSet)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td> (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><CopyableCode code="conditions" /></td>
    <td><code>object</code></td>
    <td> (title: conditionalAccessConditionSet)</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="deletedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td> (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Readonly. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-conditional_access_policy_id"><code>conditional_access_policy_id</code></a></td>
    <td></td>
    <td>The custom rules that define an access scenario.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>The custom rules that define an access scenario.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-conditional_access_policy_id"><code>conditional_access_policy_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-conditional_access_policy_id"><code>conditional_access_policy_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-conditional_access_policy_id"><code>conditional_access_policy_id</code></a></td>
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
<tr id="parameter-conditional_access_policy_id">
    <td><CopyableCode code="conditional_access_policy_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of conditionalAccessPolicy</td>
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

The custom rules that define an access scenario.

```sql
SELECT
id,
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
FROM entra_id.policies.conditional_access_policies
WHERE conditional_access_policy_id = '{{ conditional_access_policy_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

The custom rules that define an access scenario.

```sql
SELECT
id,
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
FROM entra_id.policies.conditional_access_policies
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
INSERT INTO entra_id.policies.conditional_access_policies (
deletedDateTime,
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
- name: conditional_access_policies
  props:
    - name: deletedDateTime
      value: "{{ deletedDateTime }}"
    - name: conditions
      value:
        applications:
          applicationFilter:
            mode: "{{ mode }}"
            rule: "{{ rule }}"
          excludeApplications:
            - "{{ excludeApplications }}"
          includeApplications:
            - "{{ includeApplications }}"
          includeAuthenticationContextClassReferences:
            - "{{ includeAuthenticationContextClassReferences }}"
          includeUserActions:
            - "{{ includeUserActions }}"
        authenticationFlows:
          transferMethods: "{{ transferMethods }}"
        clientApplications:
          excludeServicePrincipals:
            - "{{ excludeServicePrincipals }}"
          includeServicePrincipals:
            - "{{ includeServicePrincipals }}"
          servicePrincipalFilter:
            mode: "{{ mode }}"
            rule: "{{ rule }}"
        clientAppTypes:
          - "{{ clientAppTypes }}"
        devices:
          deviceFilter:
            mode: "{{ mode }}"
            rule: "{{ rule }}"
        insiderRiskLevels: "{{ insiderRiskLevels }}"
        locations:
          excludeLocations:
            - "{{ excludeLocations }}"
          includeLocations:
            - "{{ includeLocations }}"
        platforms:
          excludePlatforms:
            - "{{ excludePlatforms }}"
          includePlatforms:
            - "{{ includePlatforms }}"
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
            guestOrExternalUserTypes: "{{ guestOrExternalUserTypes }}"
          excludeRoles:
            - "{{ excludeRoles }}"
          excludeUsers:
            - "{{ excludeUsers }}"
          includeGroups:
            - "{{ includeGroups }}"
          includeGuestsOrExternalUsers:
            externalTenants:
              membershipKind: "{{ membershipKind }}"
            guestOrExternalUserTypes: "{{ guestOrExternalUserTypes }}"
          includeRoles:
            - "{{ includeRoles }}"
          includeUsers:
            - "{{ includeUsers }}"
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
UPDATE entra_id.policies.conditional_access_policies
SET 
deletedDateTime = '{{ deletedDateTime }}',
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
conditional_access_policy_id = '{{ conditional_access_policy_id }}' --required
RETURNING
id,
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
DELETE FROM entra_id.policies.conditional_access_policies
WHERE conditional_access_policy_id = '{{ conditional_access_policy_id }}' --required
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
EXEC entra_id.policies.conditional_access_policies.restore 
@conditional_access_policy_id='{{ conditional_access_policy_id }}' --required
;
```
</TabItem>
</Tabs>
