--- 
title: entitlement_management_access_packages_incompatible_access_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - entitlement_management_access_packages_incompatible_access_packages
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

Creates, updates, deletes, gets or lists an <code>entitlement_management_access_packages_incompatible_access_packages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="entitlement_management_access_packages_incompatible_access_packages" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.entitlement_management_access_packages_incompatible_access_packages" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td>The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a></td>
    <td></td>
    <td>Retrieve a list of the accessPackage objects that have been marked as incompatible on an accessPackage.  </td>
</tr>
<tr>
    <td><a href="#add_ref"><CopyableCode code="add_ref" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a></td>
    <td></td>
    <td>Add an accessPackage to the list of access packages that have been marked as incompatible on an accessPackage.  </td>
</tr>
<tr>
    <td><a href="#remove_ref"><CopyableCode code="remove_ref" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a>, <a href="#parameter-access_package_id1"><code>access_package_id1</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove an access package from the list of access packages that have been marked as incompatible on an accessPackage.  </td>
</tr>
<tr>
    <td><a href="#remove_ref_2"><CopyableCode code="remove_ref_2" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-access_package_id"><code>access_package_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Remove an access package from the list of access packages that have been marked as incompatible on an accessPackage.  </td>
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
<tr id="parameter-access_package_id">
    <td><CopyableCode code="access_package_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of accessPackage</td>
</tr>
<tr id="parameter-access_package_id1">
    <td><CopyableCode code="access_package_id1" /></td>
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
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Retrieve a list of the accessPackage objects that have been marked as incompatible on an accessPackage.  

```sql
SELECT
id,
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
FROM entra_id.identity_governance.entitlement_management_access_packages_incompatible_access_packages
WHERE access_package_id = '{{ access_package_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="add_ref"
    values={[
        { label: 'add_ref', value: 'add_ref' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="add_ref">

Add an accessPackage to the list of access packages that have been marked as incompatible on an accessPackage.  

```sql
INSERT INTO entra_id.identity_governance.entitlement_management_access_packages_incompatible_access_packages (
directoryObjectId,
access_package_id
)
SELECT 
'{{ directoryObjectId }}',
'{{ access_package_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: entitlement_management_access_packages_incompatible_access_packages
  props:
    - name: access_package_id
      value: "{{ access_package_id }}"
      description: Required parameter for the entitlement_management_access_packages_incompatible_access_packages resource.
    - name: directoryObjectId
      value: "{{ directoryObjectId }}"
      description: |
        The id of the directory object to reference (a user, group, service principal, device, ...). Sent on the wire as '@odata.id': 'https://graph.microsoft.com/v1.0/directoryObjects/{id}'.
`}</CodeBlock>

</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="remove_ref"
    values={[
        { label: 'remove_ref', value: 'remove_ref' },
        { label: 'remove_ref_2', value: 'remove_ref_2' }
    ]}
>
<TabItem value="remove_ref">

Remove an access package from the list of access packages that have been marked as incompatible on an accessPackage.  

```sql
DELETE FROM entra_id.identity_governance.entitlement_management_access_packages_incompatible_access_packages
WHERE access_package_id = '{{ access_package_id }}' --required
AND access_package_id1 = '{{ access_package_id1 }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="remove_ref_2">

Remove an access package from the list of access packages that have been marked as incompatible on an accessPackage.  

```sql
DELETE FROM entra_id.identity_governance.entitlement_management_access_packages_incompatible_access_packages
AND access_package_id = '{{ access_package_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
