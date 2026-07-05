--- 
title: risk_prevention_web_application_firewall_verifications
hide_title: false
hide_table_of_contents: false
keywords:
  - risk_prevention_web_application_firewall_verifications
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

Creates, updates, deletes, gets or lists a <code>risk_prevention_web_application_firewall_verifications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="risk_prevention_web_application_firewall_verifications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.risk_prevention_web_application_firewall_verifications" /></td></tr>
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
    <td><CopyableCode code="provider" /></td>
    <td><code></code></td>
    <td>Reference to a provider resource associated with this verification model. Represents a WAF provider that can be used to verify or manage the host.</td>
</tr>
<tr>
    <td><CopyableCode code="providerType" /></td>
    <td><code>string</code></td>
    <td> (akamai, cloudflare, unknownFutureValue) (title: webApplicationFirewallProviderType)</td>
</tr>
<tr>
    <td><CopyableCode code="verificationResult" /></td>
    <td><code></code></td>
    <td>An object describing the outcome of the verification operation, including status, errors or warnings</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedDetails" /></td>
    <td><code></code></td>
    <td>Details of DNS configuration</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedHost" /></td>
    <td><code>string</code></td>
    <td>The host (domain or subdomain) that was verified as part of this verification operation.</td>
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
    <td><CopyableCode code="provider" /></td>
    <td><code></code></td>
    <td>Reference to a provider resource associated with this verification model. Represents a WAF provider that can be used to verify or manage the host.</td>
</tr>
<tr>
    <td><CopyableCode code="providerType" /></td>
    <td><code>string</code></td>
    <td> (akamai, cloudflare, unknownFutureValue) (title: webApplicationFirewallProviderType)</td>
</tr>
<tr>
    <td><CopyableCode code="verificationResult" /></td>
    <td><code></code></td>
    <td>An object describing the outcome of the verification operation, including status, errors or warnings</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedDetails" /></td>
    <td><code></code></td>
    <td>Details of DNS configuration</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedHost" /></td>
    <td><code>string</code></td>
    <td>The host (domain or subdomain) that was verified as part of this verification operation.</td>
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
    <td><a href="#parameter-web_application_firewall_verification_model_id"><code>web_application_firewall_verification_model_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of webApplicationFirewallVerificationModel object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the webApplicationFirewallVerificationModel objects and their properties.</td>
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
    <td><a href="#parameter-web_application_firewall_verification_model_id"><code>web_application_firewall_verification_model_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-web_application_firewall_verification_model_id"><code>web_application_firewall_verification_model_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a webApplicationFirewallVerificationModel object.</td>
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
<tr id="parameter-web_application_firewall_verification_model_id">
    <td><CopyableCode code="web_application_firewall_verification_model_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of webApplicationFirewallVerificationModel</td>
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

Read the properties and relationships of webApplicationFirewallVerificationModel object.

```sql
SELECT
id,
provider,
providerType,
verificationResult,
verifiedDetails,
verifiedHost
FROM entra_id.identity.risk_prevention_web_application_firewall_verifications
WHERE web_application_firewall_verification_model_id = '{{ web_application_firewall_verification_model_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the webApplicationFirewallVerificationModel objects and their properties.

```sql
SELECT
id,
provider,
providerType,
verificationResult,
verifiedDetails,
verifiedHost
FROM entra_id.identity.risk_prevention_web_application_firewall_verifications
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
INSERT INTO entra_id.identity.risk_prevention_web_application_firewall_verifications (
id,
providerType,
verificationResult,
verifiedDetails,
verifiedHost,
provider
)
SELECT 
'{{ id }}',
'{{ providerType }}',
'{{ verificationResult }}',
'{{ verifiedDetails }}',
'{{ verifiedHost }}',
'{{ provider }}'
RETURNING
id,
provider,
providerType,
verificationResult,
verifiedDetails,
verifiedHost
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: risk_prevention_web_application_firewall_verifications
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: providerType
      value: "{{ providerType }}"
      valid_values: ['akamai', 'cloudflare', 'unknownFutureValue']
    - name: verificationResult
      value: "{{ verificationResult }}"
      description: |
        An object describing the outcome of the verification operation, including status, errors or warnings
    - name: verifiedDetails
      value: "{{ verifiedDetails }}"
      description: |
        Details of DNS configuration
    - name: verifiedHost
      value: "{{ verifiedHost }}"
      description: |
        The host (domain or subdomain) that was verified as part of this verification operation.
    - name: provider
      value: "{{ provider }}"
      description: |
        Reference to a provider resource associated with this verification model. Represents a WAF provider that can be used to verify or manage the host.
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
UPDATE entra_id.identity.risk_prevention_web_application_firewall_verifications
SET 
id = '{{ id }}',
providerType = '{{ providerType }}',
verificationResult = '{{ verificationResult }}',
verifiedDetails = '{{ verifiedDetails }}',
verifiedHost = '{{ verifiedHost }}',
provider = '{{ provider }}'
WHERE 
web_application_firewall_verification_model_id = '{{ web_application_firewall_verification_model_id }}' --required
RETURNING
id,
provider,
providerType,
verificationResult,
verifiedDetails,
verifiedHost;
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

Delete a webApplicationFirewallVerificationModel object.

```sql
DELETE FROM entra_id.identity.risk_prevention_web_application_firewall_verifications
WHERE web_application_firewall_verification_model_id = '{{ web_application_firewall_verification_model_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
