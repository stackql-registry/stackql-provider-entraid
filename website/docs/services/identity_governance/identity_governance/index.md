--- 
title: identity_governance
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_governance
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

Creates, updates, deletes, gets or lists an <code>identity_governance</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="identity_governance" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.identity_governance.identity_governance" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="accessReviews" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.accessReviewSet, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="appConsent" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.appConsentApprovalRoute, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="entitlementManagement" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.entitlementManagement, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="lifecycleWorkflows" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.identityGovernance.lifecycleWorkflowsContainer, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="privilegedAccess" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.privilegedAccessRoot, title: entity)</td>
</tr>
<tr>
    <td><CopyableCode code="termsOfUse" /></td>
    <td><code>object</code></td>
    <td>(opaque JSON object) (x-ms-discriminator-value: #microsoft.graph.termsOfUseContainer, title: entity)</td>
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
@odata.type,
accessReviews,
appConsent,
entitlementManagement,
lifecycleWorkflows,
privilegedAccess,
termsOfUse
FROM entraid.identity_governance.identity_governance
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
UPDATE entraid.identity_governance.identity_governance
SET 
accessReviews = '{{ accessReviews }}',
appConsent = '{{ appConsent }}',
entitlementManagement = '{{ entitlementManagement }}',
lifecycleWorkflows = '{{ lifecycleWorkflows }}',
privilegedAccess = '{{ privilegedAccess }}',
termsOfUse = '{{ termsOfUse }}',
@odata.type = '{{ @odata.type }}'
WHERE 
@odata.type = '{{ @odata.type }}' --required
RETURNING
@odata.type,
accessReviews,
appConsent,
entitlementManagement,
lifecycleWorkflows,
privilegedAccess,
termsOfUse;
```
</TabItem>
</Tabs>
