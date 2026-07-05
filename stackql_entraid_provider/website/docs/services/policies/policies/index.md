--- 
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.policies.policies" /></td></tr>
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
    <td><CopyableCode code="activityBasedTimeoutPolicies" /></td>
    <td><code>array</code></td>
    <td>The policy that controls the idle time out for web sessions for applications.</td>
</tr>
<tr>
    <td><CopyableCode code="adminConsentRequestPolicy" /></td>
    <td><code></code></td>
    <td>The policy by which consent requests are created and managed for the entire tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="appManagementPolicies" /></td>
    <td><code>array</code></td>
    <td>The policies that enforce app management restrictions for specific applications and service principals, overriding the defaultAppManagementPolicy.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationFlowsPolicy" /></td>
    <td><code></code></td>
    <td>The policy configuration of the self-service sign-up experience of external users.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationMethodsPolicy" /></td>
    <td><code></code></td>
    <td>The authentication methods and the users that are allowed to use them to sign in and perform multifactor authentication (MFA) in Microsoft Entra ID.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationStrengthPolicies" /></td>
    <td><code>array</code></td>
    <td>The authentication method combinations that are to be used in scenarios defined by Microsoft Entra Conditional Access.</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationPolicy" /></td>
    <td><code></code></td>
    <td>The policy that controls Microsoft Entra authorization settings.</td>
</tr>
<tr>
    <td><CopyableCode code="claimsMappingPolicies" /></td>
    <td><code>array</code></td>
    <td>The claim-mapping policies for WS-Fed, SAML, OAuth 2.0, and OpenID Connect protocols, for tokens issued to a specific application.</td>
</tr>
<tr>
    <td><CopyableCode code="conditionalAccessPolicies" /></td>
    <td><code>array</code></td>
    <td>The custom rules that define an access scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="crossTenantAccessPolicy" /></td>
    <td><code></code></td>
    <td>The custom rules that define an access scenario when interacting with external Microsoft Entra tenants.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultAppManagementPolicy" /></td>
    <td><code></code></td>
    <td>The tenant-wide policy that enforces app management restrictions for all applications and service principals.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceRegistrationPolicy" /></td>
    <td><code></code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="featureRolloutPolicies" /></td>
    <td><code>array</code></td>
    <td>The feature rollout policy associated with a directory object.</td>
</tr>
<tr>
    <td><CopyableCode code="homeRealmDiscoveryPolicies" /></td>
    <td><code>array</code></td>
    <td>The policy to control Microsoft Entra authentication behavior for federated users.</td>
</tr>
<tr>
    <td><CopyableCode code="identitySecurityDefaultsEnforcementPolicy" /></td>
    <td><code></code></td>
    <td>The policy that represents the security defaults that protect against common attacks.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerlessGroupPolicy" /></td>
    <td><code></code></td>
    <td>The policy configuration for managing groups that have lost their sole owner.</td>
</tr>
<tr>
    <td><CopyableCode code="permissionGrantPolicies" /></td>
    <td><code>array</code></td>
    <td>The policy that specifies the conditions under which consent can be granted.</td>
</tr>
<tr>
    <td><CopyableCode code="roleManagementPolicies" /></td>
    <td><code>array</code></td>
    <td>Specifies the various policies associated with scopes and roles.</td>
</tr>
<tr>
    <td><CopyableCode code="roleManagementPolicyAssignments" /></td>
    <td><code>array</code></td>
    <td>The assignment of a role management policy to a role definition object.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenIssuancePolicies" /></td>
    <td><code>array</code></td>
    <td>The policy that specifies the characteristics of SAML tokens issued by Microsoft Entra ID.</td>
</tr>
<tr>
    <td><CopyableCode code="tokenLifetimePolicies" /></td>
    <td><code>array</code></td>
    <td>The policy that controls the lifetime of a JWT access token, an ID token, or a SAML 1.1/2.0 token issued by Microsoft Entra ID.</td>
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
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
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
activityBasedTimeoutPolicies,
adminConsentRequestPolicy,
appManagementPolicies,
authenticationFlowsPolicy,
authenticationMethodsPolicy,
authenticationStrengthPolicies,
authorizationPolicy,
claimsMappingPolicies,
conditionalAccessPolicies,
crossTenantAccessPolicy,
defaultAppManagementPolicy,
deviceRegistrationPolicy,
featureRolloutPolicies,
homeRealmDiscoveryPolicies,
identitySecurityDefaultsEnforcementPolicy,
ownerlessGroupPolicy,
permissionGrantPolicies,
roleManagementPolicies,
roleManagementPolicyAssignments,
tokenIssuancePolicies,
tokenLifetimePolicies
FROM entra_id.policies.policies
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
UPDATE entra_id.policies.policies
SET 
id = '{{ id }}',
activityBasedTimeoutPolicies = '{{ activityBasedTimeoutPolicies }}',
adminConsentRequestPolicy = '{{ adminConsentRequestPolicy }}',
appManagementPolicies = '{{ appManagementPolicies }}',
authenticationFlowsPolicy = '{{ authenticationFlowsPolicy }}',
authenticationMethodsPolicy = '{{ authenticationMethodsPolicy }}',
authenticationStrengthPolicies = '{{ authenticationStrengthPolicies }}',
authorizationPolicy = '{{ authorizationPolicy }}',
claimsMappingPolicies = '{{ claimsMappingPolicies }}',
conditionalAccessPolicies = '{{ conditionalAccessPolicies }}',
crossTenantAccessPolicy = '{{ crossTenantAccessPolicy }}',
defaultAppManagementPolicy = '{{ defaultAppManagementPolicy }}',
deviceRegistrationPolicy = '{{ deviceRegistrationPolicy }}',
featureRolloutPolicies = '{{ featureRolloutPolicies }}',
homeRealmDiscoveryPolicies = '{{ homeRealmDiscoveryPolicies }}',
identitySecurityDefaultsEnforcementPolicy = '{{ identitySecurityDefaultsEnforcementPolicy }}',
ownerlessGroupPolicy = '{{ ownerlessGroupPolicy }}',
permissionGrantPolicies = '{{ permissionGrantPolicies }}',
roleManagementPolicies = '{{ roleManagementPolicies }}',
roleManagementPolicyAssignments = '{{ roleManagementPolicyAssignments }}',
tokenIssuancePolicies = '{{ tokenIssuancePolicies }}',
tokenLifetimePolicies = '{{ tokenLifetimePolicies }}'
RETURNING
id,
activityBasedTimeoutPolicies,
adminConsentRequestPolicy,
appManagementPolicies,
authenticationFlowsPolicy,
authenticationMethodsPolicy,
authenticationStrengthPolicies,
authorizationPolicy,
claimsMappingPolicies,
conditionalAccessPolicies,
crossTenantAccessPolicy,
defaultAppManagementPolicy,
deviceRegistrationPolicy,
featureRolloutPolicies,
homeRealmDiscoveryPolicies,
identitySecurityDefaultsEnforcementPolicy,
ownerlessGroupPolicy,
permissionGrantPolicies,
roleManagementPolicies,
roleManagementPolicyAssignments,
tokenIssuancePolicies,
tokenLifetimePolicies;
```
</TabItem>
</Tabs>
