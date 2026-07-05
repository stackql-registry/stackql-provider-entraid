--- 
title: service_configuration_records
hide_title: false
hide_table_of_contents: false
keywords:
  - service_configuration_records
  - domains
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

Creates, updates, deletes, gets or lists a <code>service_configuration_records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_configuration_records" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.domains.service_configuration_records" /></td></tr>
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
    <td><CopyableCode code="isOptional" /></td>
    <td><code>boolean</code></td>
    <td>If false, the customer must configure this record at the DNS host for Microsoft Online Services to operate correctly with the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>Value used when configuring the name of the DNS record at the DNS host.</td>
</tr>
<tr>
    <td><CopyableCode code="recordType" /></td>
    <td><code>string</code></td>
    <td>Indicates what type of DNS record this entity represents. The value can be CName, Mx, Srv, or Txt.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedService" /></td>
    <td><code>string</code></td>
    <td>Microsoft Online Service or feature that has a dependency on this DNS record. Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>number (int32)</code></td>
    <td>Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.</td>
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
    <td><CopyableCode code="isOptional" /></td>
    <td><code>boolean</code></td>
    <td>If false, the customer must configure this record at the DNS host for Microsoft Online Services to operate correctly with the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>Value used when configuring the name of the DNS record at the DNS host.</td>
</tr>
<tr>
    <td><CopyableCode code="recordType" /></td>
    <td><code>string</code></td>
    <td>Indicates what type of DNS record this entity represents. The value can be CName, Mx, Srv, or Txt.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedService" /></td>
    <td><code>string</code></td>
    <td>Microsoft Online Service or feature that has a dependency on this DNS record. Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.</td>
</tr>
<tr>
    <td><CopyableCode code="ttl" /></td>
    <td><code>number (int32)</code></td>
    <td>Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.</td>
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
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-domain_dns_record_id"><code>domain_dns_record_id</code></a></td>
    <td></td>
    <td>DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Doesn't support $expand.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a></td>
    <td></td>
    <td>Retrieves a list of domainDnsRecord objects needed to enable services for the domain. Use the returned list to add records to the zone file of the domain. This can be done through the domain registrar or DNS server configuration.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-domain_dns_record_id"><code>domain_dns_record_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-domain_id"><code>domain_id</code></a>, <a href="#parameter-domain_dns_record_id"><code>domain_dns_record_id</code></a></td>
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
<tr id="parameter-domain_dns_record_id">
    <td><CopyableCode code="domain_dns_record_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of domainDnsRecord</td>
</tr>
<tr id="parameter-domain_id">
    <td><CopyableCode code="domain_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of domain</td>
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

DNS records the customer adds to the DNS zone file of the domain before the domain can be used by Microsoft Online services. Read-only, Nullable. Doesn't support $expand.

```sql
SELECT
id,
isOptional,
label,
recordType,
supportedService,
ttl
FROM entra_id.domains.service_configuration_records
WHERE domain_id = '{{ domain_id }}' -- required
AND domain_dns_record_id = '{{ domain_dns_record_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieves a list of domainDnsRecord objects needed to enable services for the domain. Use the returned list to add records to the zone file of the domain. This can be done through the domain registrar or DNS server configuration.

```sql
SELECT
id,
isOptional,
label,
recordType,
supportedService,
ttl
FROM entra_id.domains.service_configuration_records
WHERE domain_id = '{{ domain_id }}' -- required
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
INSERT INTO entra_id.domains.service_configuration_records (
id,
isOptional,
label,
recordType,
supportedService,
ttl,
domain_id
)
SELECT 
'{{ id }}',
{{ isOptional }},
'{{ label }}',
'{{ recordType }}',
'{{ supportedService }}',
{{ ttl }},
'{{ domain_id }}'
RETURNING
id,
isOptional,
label,
recordType,
supportedService,
ttl
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: service_configuration_records
  props:
    - name: domain_id
      value: "{{ domain_id }}"
      description: Required parameter for the service_configuration_records resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: isOptional
      value: {{ isOptional }}
      description: |
        If false, the customer must configure this record at the DNS host for Microsoft Online Services to operate correctly with the domain.
    - name: label
      value: "{{ label }}"
      description: |
        Value used when configuring the name of the DNS record at the DNS host.
    - name: recordType
      value: "{{ recordType }}"
      description: |
        Indicates what type of DNS record this entity represents. The value can be CName, Mx, Srv, or Txt.
    - name: supportedService
      value: "{{ supportedService }}"
      description: |
        Microsoft Online Service or feature that has a dependency on this DNS record. Can be one of the following values: null, Email, Sharepoint, EmailInternalRelayOnly, OfficeCommunicationsOnline, SharePointDefaultDomain, FullRedelegation, SharePointPublic, OrgIdAuthentication, Yammer, Intune.
    - name: ttl
      value: {{ ttl }}
      description: |
        Value to use when configuring the time-to-live (ttl) property of the DNS record at the DNS host. Not nullable.
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
UPDATE entra_id.domains.service_configuration_records
SET 
id = '{{ id }}',
isOptional = {{ isOptional }},
label = '{{ label }}',
recordType = '{{ recordType }}',
supportedService = '{{ supportedService }}',
ttl = {{ ttl }}
WHERE 
domain_id = '{{ domain_id }}' --required
AND domain_dns_record_id = '{{ domain_dns_record_id }}' --required
RETURNING
id,
isOptional,
label,
recordType,
supportedService,
ttl;
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
DELETE FROM entra_id.domains.service_configuration_records
WHERE domain_id = '{{ domain_id }}' --required
AND domain_dns_record_id = '{{ domain_dns_record_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
