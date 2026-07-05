--- 
title: device_local_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - device_local_credentials
  - directory
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

Creates, updates, deletes, gets or lists a <code>device_local_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="device_local_credentials" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.directory.device_local_credentials" /></td></tr>
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
    <td><CopyableCode code="credentials" /></td>
    <td><code>array</code></td>
    <td>The credentials of the device's local administrator account backed up to Azure Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceName" /></td>
    <td><code>string</code></td>
    <td>Display name of the device that the local credentials are associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBackupDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the local administrator account credential was backed up to Azure Active Directory. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the local administrator account credential will be refreshed and backed up to Azure Active Directory. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><CopyableCode code="credentials" /></td>
    <td><code>array</code></td>
    <td>The credentials of the device's local administrator account backed up to Azure Active Directory.</td>
</tr>
<tr>
    <td><CopyableCode code="deviceName" /></td>
    <td><code>string</code></td>
    <td>Display name of the device that the local credentials are associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="lastBackupDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the local administrator account credential was backed up to Azure Active Directory. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="refreshDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the local administrator account credential will be refreshed and backed up to Azure Active Directory. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
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
    <td><a href="#parameter-device_local_credential_info_id"><code>device_local_credential_info_id</code></a></td>
    <td></td>
    <td>Retrieve the properties of a deviceLocalCredentialInfo for a specified device object. </td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the deviceLocalCredentialInfo objects and their properties, excluding the credentials property. </td>
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
    <td><a href="#parameter-device_local_credential_info_id"><code>device_local_credential_info_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-device_local_credential_info_id"><code>device_local_credential_info_id</code></a></td>
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
<tr id="parameter-device_local_credential_info_id">
    <td><CopyableCode code="device_local_credential_info_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of deviceLocalCredentialInfo</td>
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

Retrieve the properties of a deviceLocalCredentialInfo for a specified device object. 

```sql
SELECT
id,
credentials,
deviceName,
lastBackupDateTime,
refreshDateTime
FROM entra_id.directory.device_local_credentials
WHERE device_local_credential_info_id = '{{ device_local_credential_info_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the deviceLocalCredentialInfo objects and their properties, excluding the credentials property. 

```sql
SELECT
id,
credentials,
deviceName,
lastBackupDateTime,
refreshDateTime
FROM entra_id.directory.device_local_credentials
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
INSERT INTO entra_id.directory.device_local_credentials (
id,
credentials,
deviceName,
lastBackupDateTime,
refreshDateTime
)
SELECT 
'{{ id }}',
'{{ credentials }}',
'{{ deviceName }}',
'{{ lastBackupDateTime }}',
'{{ refreshDateTime }}'
RETURNING
id,
credentials,
deviceName,
lastBackupDateTime,
refreshDateTime
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: device_local_credentials
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: credentials
      description: |
        The credentials of the device's local administrator account backed up to Azure Active Directory.
      value:
        - id: "{{ id }}"
          accountName: "{{ accountName }}"
          accountSid: "{{ accountSid }}"
          backupDateTime: "{{ backupDateTime }}"
          passwordBase64: "{{ passwordBase64 }}"
    - name: deviceName
      value: "{{ deviceName }}"
      description: |
        Display name of the device that the local credentials are associated with.
    - name: lastBackupDateTime
      value: "{{ lastBackupDateTime }}"
      description: |
        When the local administrator account credential was backed up to Azure Active Directory.
    - name: refreshDateTime
      value: "{{ refreshDateTime }}"
      description: |
        When the local administrator account credential will be refreshed and backed up to Azure Active Directory.
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
UPDATE entra_id.directory.device_local_credentials
SET 
id = '{{ id }}',
credentials = '{{ credentials }}',
deviceName = '{{ deviceName }}',
lastBackupDateTime = '{{ lastBackupDateTime }}',
refreshDateTime = '{{ refreshDateTime }}'
WHERE 
device_local_credential_info_id = '{{ device_local_credential_info_id }}' --required
RETURNING
id,
credentials,
deviceName,
lastBackupDateTime,
refreshDateTime;
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
DELETE FROM entra_id.directory.device_local_credentials
WHERE device_local_credential_info_id = '{{ device_local_credential_info_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
