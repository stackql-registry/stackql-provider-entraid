--- 
title: cross_tenant_access_policy_partners
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_tenant_access_policy_partners
  - policies
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

Creates, updates, deletes, gets or lists a <code>cross_tenant_access_policy_partners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cross_tenant_access_policy_partners" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entraid.policies.cross_tenant_access_policy_partners" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="appServiceConnectInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for inbound app service connect settings that control which applications can connect across tenant boundaries with the partner organization. (title: crossTenantAccessPolicyAppServiceConnectSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="automaticUserConsentSettings" /></td>
    <td><code>object</code></td>
    <td>Determines the partner-specific configuration for automatic user consent settings. Unless specifically configured, the inboundAllowed and outboundAllowed properties are null and inherit from the default settings, which is always false. (title: inboundOutboundPolicyConfiguration)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users from other organizations accessing your resources via Microsoft Entra B2B collaboration. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationOutbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B collaboration. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectOutbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B direct connect. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="identitySynchronization" /></td>
    <td><code>object</code></td>
    <td>Defines the cross-tenant policy for the synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multitenant organization by automating the creation, update, and deletion of users from one tenant to another. (title: crossTenantIdentitySyncPolicyPartner)</td>
</tr>
<tr>
    <td><CopyableCode code="inboundTrust" /></td>
    <td><code>object</code></td>
    <td>Determines the partner-specific configuration for trusting other Conditional Access claims from external Microsoft Entra organizations. (title: crossTenantAccessPolicyInboundTrust)</td>
</tr>
<tr>
    <td><CopyableCode code="isInMultiTenantOrganization" /></td>
    <td><code>boolean</code></td>
    <td>Identifies whether a tenant is a member of a multitenant organization.</td>
</tr>
<tr>
    <td><CopyableCode code="isServiceProvider" /></td>
    <td><code>boolean</code></td>
    <td>Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.</td>
</tr>
<tr>
    <td><CopyableCode code="m365CollaborationInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for inbound Microsoft 365 collaboration settings that determine which users from the partner organization can collaborate with your organization using Microsoft 365 apps. (title: crossTenantAccessPolicyM365CollaborationInboundSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="m365CollaborationOutbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for outbound Microsoft 365 collaboration settings that determine which users in your organization can collaborate with the partner organization using Microsoft 365 apps. (title: crossTenantAccessPolicyM365CollaborationOutboundSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant identifier for the partner Microsoft Entra organization. Read-only. Key.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantRestrictions" /></td>
    <td><code>object</code></td>
    <td>Defines the partner-specific tenant restrictions configuration for users in your organization who access a partner organization using partner supplied identities on your network or devices. (x-ms-discriminator-value: #microsoft.graph.crossTenantAccessPolicyTenantRestrictions, title: crossTenantAccessPolicyB2BSetting)</td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="appServiceConnectInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for inbound app service connect settings that control which applications can connect across tenant boundaries with the partner organization. (title: crossTenantAccessPolicyAppServiceConnectSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="automaticUserConsentSettings" /></td>
    <td><code>object</code></td>
    <td>Determines the partner-specific configuration for automatic user consent settings. Unless specifically configured, the inboundAllowed and outboundAllowed properties are null and inherit from the default settings, which is always false. (title: inboundOutboundPolicyConfiguration)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users from other organizations accessing your resources via Microsoft Entra B2B collaboration. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bCollaborationOutbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B collaboration. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="b2bDirectConnectOutbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B direct connect. (title: crossTenantAccessPolicyB2BSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="identitySynchronization" /></td>
    <td><code>object</code></td>
    <td>Defines the cross-tenant policy for the synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multitenant organization by automating the creation, update, and deletion of users from one tenant to another. (title: crossTenantIdentitySyncPolicyPartner)</td>
</tr>
<tr>
    <td><CopyableCode code="inboundTrust" /></td>
    <td><code>object</code></td>
    <td>Determines the partner-specific configuration for trusting other Conditional Access claims from external Microsoft Entra organizations. (title: crossTenantAccessPolicyInboundTrust)</td>
</tr>
<tr>
    <td><CopyableCode code="isInMultiTenantOrganization" /></td>
    <td><code>boolean</code></td>
    <td>Identifies whether a tenant is a member of a multitenant organization.</td>
</tr>
<tr>
    <td><CopyableCode code="isServiceProvider" /></td>
    <td><code>boolean</code></td>
    <td>Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.</td>
</tr>
<tr>
    <td><CopyableCode code="m365CollaborationInbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for inbound Microsoft 365 collaboration settings that determine which users from the partner organization can collaborate with your organization using Microsoft 365 apps. (title: crossTenantAccessPolicyM365CollaborationInboundSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="m365CollaborationOutbound" /></td>
    <td><code>object</code></td>
    <td>Defines your partner-specific configuration for outbound Microsoft 365 collaboration settings that determine which users in your organization can collaborate with the partner organization using Microsoft 365 apps. (title: crossTenantAccessPolicyM365CollaborationOutboundSetting)</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant identifier for the partner Microsoft Entra organization. Read-only. Key.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantRestrictions" /></td>
    <td><code>object</code></td>
    <td>Defines the partner-specific tenant restrictions configuration for users in your organization who access a partner organization using partner supplied identities on your network or devices. (x-ms-discriminator-value: #microsoft.graph.crossTenantAccessPolicyTenantRestrictions, title: crossTenantAccessPolicyB2BSetting)</td>
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
    <td><a href="#parameter-crossTenantAccessPolicyConfigurationPartner-tenantId"><code>crossTenantAccessPolicyConfigurationPartner-tenantId</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of a partner-specific configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a list of all partner configurations within a cross-tenant access policy. You can also use the $expand parameter to list the user synchronization policy for all partner configurations.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new partner configuration in a cross-tenant access policy.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-crossTenantAccessPolicyConfigurationPartner-tenantId"><code>crossTenantAccessPolicyConfigurationPartner-tenantId</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of a partner-specific configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-crossTenantAccessPolicyConfigurationPartner-tenantId"><code>crossTenantAccessPolicyConfigurationPartner-tenantId</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a partner-specific configuration in a cross-tenant access policy. If a configuration includes a user synchronization policy, you must first delete the user synchronization policy before you can delete the partner-specific configuration.</td>
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
<tr id="parameter-crossTenantAccessPolicyConfigurationPartner-tenantId">
    <td><CopyableCode code="crossTenantAccessPolicyConfigurationPartner-tenantId" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of crossTenantAccessPolicyConfigurationPartner</td>
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

Read the properties and relationships of a partner-specific configuration.

```sql
SELECT
@odata.type,
appServiceConnectInbound,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
identitySynchronization,
inboundTrust,
isInMultiTenantOrganization,
isServiceProvider,
m365CollaborationInbound,
m365CollaborationOutbound,
tenantId,
tenantRestrictions
FROM entraid.policies.cross_tenant_access_policy_partners
WHERE crossTenantAccessPolicyConfigurationPartner-tenantId = '{{ crossTenantAccessPolicyConfigurationPartner-tenantId }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get a list of all partner configurations within a cross-tenant access policy. You can also use the $expand parameter to list the user synchronization policy for all partner configurations.

```sql
SELECT
@odata.type,
appServiceConnectInbound,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
identitySynchronization,
inboundTrust,
isInMultiTenantOrganization,
isServiceProvider,
m365CollaborationInbound,
m365CollaborationOutbound,
tenantId,
tenantRestrictions
FROM entraid.policies.cross_tenant_access_policy_partners
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

Create a new partner configuration in a cross-tenant access policy.

```sql
INSERT INTO entraid.policies.cross_tenant_access_policy_partners (
appServiceConnectInbound,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
inboundTrust,
isInMultiTenantOrganization,
isServiceProvider,
m365CollaborationInbound,
m365CollaborationOutbound,
tenantId,
tenantRestrictions,
identitySynchronization,
@odata.type
)
SELECT 
'{{ appServiceConnectInbound }}',
'{{ automaticUserConsentSettings }}',
'{{ b2bCollaborationInbound }}',
'{{ b2bCollaborationOutbound }}',
'{{ b2bDirectConnectInbound }}',
'{{ b2bDirectConnectOutbound }}',
'{{ inboundTrust }}',
{{ isInMultiTenantOrganization }},
{{ isServiceProvider }},
'{{ m365CollaborationInbound }}',
'{{ m365CollaborationOutbound }}',
'{{ tenantId }}',
'{{ tenantRestrictions }}',
'{{ identitySynchronization }}',
'{{ @odata.type }}' /* required */
RETURNING
@odata.type,
appServiceConnectInbound,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
identitySynchronization,
inboundTrust,
isInMultiTenantOrganization,
isServiceProvider,
m365CollaborationInbound,
m365CollaborationOutbound,
tenantId,
tenantRestrictions
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: cross_tenant_access_policy_partners
  props:
    - name: appServiceConnectInbound
      description: |
        Defines your partner-specific configuration for inbound app service connect settings that control which applications can connect across tenant boundaries with the partner organization.
      value:
        applications:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: automaticUserConsentSettings
      description: |
        Determines the partner-specific configuration for automatic user consent settings. Unless specifically configured, the inboundAllowed and outboundAllowed properties are null and inherit from the default settings, which is always false.
      value:
        inboundAllowed: {{ inboundAllowed }}
        outboundAllowed: {{ outboundAllowed }}
        @odata.type: "{{ @odata.type }}"
    - name: b2bCollaborationInbound
      description: |
        Defines your partner-specific configuration for users from other organizations accessing your resources via Microsoft Entra B2B collaboration.
      value:
        applications:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        usersAndGroups:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: b2bCollaborationOutbound
      description: |
        Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B collaboration.
      value:
        applications:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        usersAndGroups:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: b2bDirectConnectInbound
      description: |
        Defines your partner-specific configuration for users from other organizations accessing your resources via Azure B2B direct connect.
      value:
        applications:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        usersAndGroups:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: b2bDirectConnectOutbound
      description: |
        Defines your partner-specific configuration for users in your organization going outbound to access resources in another organization via Microsoft Entra B2B direct connect.
      value:
        applications:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        usersAndGroups:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: inboundTrust
      description: |
        Determines the partner-specific configuration for trusting other Conditional Access claims from external Microsoft Entra organizations.
      value:
        isCompliantDeviceAccepted: {{ isCompliantDeviceAccepted }}
        isHybridAzureADJoinedDeviceAccepted: {{ isHybridAzureADJoinedDeviceAccepted }}
        isMfaAccepted: {{ isMfaAccepted }}
        @odata.type: "{{ @odata.type }}"
    - name: isInMultiTenantOrganization
      value: {{ isInMultiTenantOrganization }}
      description: |
        Identifies whether a tenant is a member of a multitenant organization.
    - name: isServiceProvider
      value: {{ isServiceProvider }}
      description: |
        Identifies whether the partner-specific configuration is a Cloud Service Provider for your organization.
    - name: m365CollaborationInbound
      description: |
        Defines your partner-specific configuration for inbound Microsoft 365 collaboration settings that determine which users from the partner organization can collaborate with your organization using Microsoft 365 apps.
      value:
        users:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: m365CollaborationOutbound
      description: |
        Defines your partner-specific configuration for outbound Microsoft 365 collaboration settings that determine which users in your organization can collaborate with the partner organization using Microsoft 365 apps.
      value:
        usersAndGroups:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: tenantId
      value: "{{ tenantId }}"
      description: |
        The tenant identifier for the partner Microsoft Entra organization. Read-only. Key.
    - name: tenantRestrictions
      description: |
        Defines the partner-specific tenant restrictions configuration for users in your organization who access a partner organization using partner supplied identities on your network or devices.
      value:
        applications:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        usersAndGroups:
          accessType: "{{ accessType }}"
          targets:
            - target: "{{ target }}"
              targetType: "{{ targetType }}"
              @odata.type: "{{ @odata.type }}"
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
        devices: "{{ devices }}"
    - name: identitySynchronization
      description: |
        Defines the cross-tenant policy for the synchronization of users from a partner tenant. Use this user synchronization policy to streamline collaboration between users in a multitenant organization by automating the creation, update, and deletion of users from one tenant to another.
      value:
        displayName: "{{ displayName }}"
        tenantId: "{{ tenantId }}"
        userSyncInbound:
          isSyncAllowed: {{ isSyncAllowed }}
          @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: @odata.type
      value: "{{ @odata.type }}"
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

Update the properties of a partner-specific configuration.

```sql
UPDATE entraid.policies.cross_tenant_access_policy_partners
SET 
appServiceConnectInbound = '{{ appServiceConnectInbound }}',
automaticUserConsentSettings = '{{ automaticUserConsentSettings }}',
b2bCollaborationInbound = '{{ b2bCollaborationInbound }}',
b2bCollaborationOutbound = '{{ b2bCollaborationOutbound }}',
b2bDirectConnectInbound = '{{ b2bDirectConnectInbound }}',
b2bDirectConnectOutbound = '{{ b2bDirectConnectOutbound }}',
inboundTrust = '{{ inboundTrust }}',
isInMultiTenantOrganization = {{ isInMultiTenantOrganization }},
isServiceProvider = {{ isServiceProvider }},
m365CollaborationInbound = '{{ m365CollaborationInbound }}',
m365CollaborationOutbound = '{{ m365CollaborationOutbound }}',
tenantId = '{{ tenantId }}',
tenantRestrictions = '{{ tenantRestrictions }}',
identitySynchronization = '{{ identitySynchronization }}',
@odata.type = '{{ @odata.type }}'
WHERE 
crossTenantAccessPolicyConfigurationPartner-tenantId = '{{ crossTenantAccessPolicyConfigurationPartner-tenantId }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
@odata.type,
appServiceConnectInbound,
automaticUserConsentSettings,
b2bCollaborationInbound,
b2bCollaborationOutbound,
b2bDirectConnectInbound,
b2bDirectConnectOutbound,
identitySynchronization,
inboundTrust,
isInMultiTenantOrganization,
isServiceProvider,
m365CollaborationInbound,
m365CollaborationOutbound,
tenantId,
tenantRestrictions;
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

Delete a partner-specific configuration in a cross-tenant access policy. If a configuration includes a user synchronization policy, you must first delete the user synchronization policy before you can delete the partner-specific configuration.

```sql
DELETE FROM entraid.policies.cross_tenant_access_policy_partners
WHERE crossTenantAccessPolicyConfigurationPartner-tenantId = '{{ crossTenantAccessPolicyConfigurationPartner-tenantId }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
