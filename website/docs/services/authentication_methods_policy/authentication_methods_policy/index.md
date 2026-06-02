--- 
title: authentication_methods_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - authentication_methods_policy
  - authentication_methods_policy
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

Creates, updates, deletes, gets or lists an <code>authentication_methods_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="authentication_methods_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.authentication_methods_policy.authentication_methods_policy" /></td></tr>
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
    <td><CopyableCode code="authenticationMethodConfigurations" /></td>
    <td><code>array</code></td>
    <td>Represents the settings for each authentication method. Automatically expanded on GET /policies/authenticationMethodsPolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the policy. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The name of the policy. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the last update to the policy. Read-only. (pattern: <code>^[0-9]&#123;4,&#125;-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]([.][0-9]&#123;1,12&#125;)?(Z|[+-][0-9][0-9]:[0-9][0-9])$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="policyMigrationState" /></td>
    <td><code></code></td>
    <td>The state of migration of the authentication methods policy from the legacy multifactor authentication and self-service password reset (SSPR) policies. The possible values are: premigration - means the authentication methods policy is used for authentication only, legacy policies are respected. migrationInProgress - means the authentication methods policy is used for both authentication and SSPR, legacy policies are respected. migrationComplete - means the authentication methods policy is used for authentication and SSPR, legacy policies are ignored. unknownFutureValue - Evolvable enumeration sentinel value. Do not use.</td>
</tr>
<tr>
    <td><CopyableCode code="policyVersion" /></td>
    <td><code>string</code></td>
    <td>The version of the policy in use. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="reconfirmationInDays" /></td>
    <td><code>number (int32)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="registrationEnforcement" /></td>
    <td><code></code></td>
    <td>Enforce registration at sign-in time. This property can be used to remind users to set up targeted authentication methods.</td>
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
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
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

Retrieved entity

```sql
SELECT
id,
@odata.type,
authenticationMethodConfigurations,
description,
displayName,
lastModifiedDateTime,
policyMigrationState,
policyVersion,
reconfirmationInDays,
registrationEnforcement
FROM entra_id.authentication_methods_policy.authentication_methods_policy
WHERE $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
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
UPDATE entra_id.authentication_methods_policy.authentication_methods_policy
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
description = '{{ description }}',
displayName = '{{ displayName }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
policyMigrationState = '{{ policyMigrationState }}',
policyVersion = '{{ policyVersion }}',
reconfirmationInDays = {{ reconfirmationInDays }},
registrationEnforcement = '{{ registrationEnforcement }}',
authenticationMethodConfigurations = '{{ authenticationMethodConfigurations }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
authenticationMethodConfigurations,
description,
displayName,
lastModifiedDateTime,
policyMigrationState,
policyVersion,
reconfirmationInDays,
registrationEnforcement;
```
</TabItem>
</Tabs>
