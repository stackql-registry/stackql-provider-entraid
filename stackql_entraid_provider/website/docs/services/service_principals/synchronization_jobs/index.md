--- 
title: synchronization_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_jobs
  - service_principals
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

Creates, updates, deletes, gets or lists a <code>synchronization_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_jobs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.service_principals.synchronization_jobs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'bulk_upload', value: 'bulk_upload' },
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="bulkUpload" /></td>
    <td><code></code></td>
    <td>The bulk upload operation for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code></code></td>
    <td>Schedule used to run the job. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code></code></td>
    <td>The synchronization schema configured for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>Status of the job, which includes when the job was last run, current job state, and errors.</td>
</tr>
<tr>
    <td><CopyableCode code="synchronizationJobSettings" /></td>
    <td><code>array</code></td>
    <td>Settings associated with the job. Some settings are inherited from the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the synchronization template this job is based on.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="bulk_upload">

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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="bulkUpload" /></td>
    <td><code></code></td>
    <td>The bulk upload operation for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code></code></td>
    <td>Schedule used to run the job. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="schema" /></td>
    <td><code></code></td>
    <td>The synchronization schema configured for the job.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code></code></td>
    <td>Status of the job, which includes when the job was last run, current job state, and errors.</td>
</tr>
<tr>
    <td><CopyableCode code="synchronizationJobSettings" /></td>
    <td><code>array</code></td>
    <td>Settings associated with the job. Some settings are inherited from the template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the synchronization template this job is based on.</td>
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
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve the existing synchronization job and its properties.</td>
</tr>
<tr>
    <td><a href="#bulk_upload"><CopyableCode code="bulk_upload" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The bulk upload operation for the job.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>List existing jobs for a given application instance (service principal).</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create new synchronization job with a default synchronization schema. The job is created in a disabled state. Call Start job to start synchronization.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Stop the synchronization job, and permanently delete all the state associated with it. Synchronized accounts are left as-is.</td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td></td>
    <td>Temporarily stop a running synchronization job. All the progress, including job state, is persisted, and the job will continue from where it left off when a start call is made.</td>
</tr>
<tr>
    <td><a href="#provision_on_demand"><CopyableCode code="provision_on_demand" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td></td>
    <td>Select a user and provision the account on-demand. The rate limit for this API is 5 requests per 10 seconds.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td></td>
    <td>Start an existing synchronization job. If the job is in a paused state, it continues processing changes from the point where it was paused. If the job is in quarantine, the quarantine status is cleared. Don't create scripts to call the start job continuously while it's running because that can cause the service to stop running. Use the start job only when the job is currently paused or in quarantine. </td>
</tr>
<tr>
    <td><a href="#validate_credentials"><CopyableCode code="validate_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td></td>
    <td>Validate that the credentials are valid in the tenant.</td>
</tr>
<tr>
    <td><a href="#validate_credentials_2"><CopyableCode code="validate_credentials_2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-servicePrincipal-id"><code>servicePrincipal-id</code></a></td>
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
<tr id="parameter-servicePrincipal-id">
    <td><CopyableCode code="servicePrincipal-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of servicePrincipal</td>
</tr>
<tr id="parameter-synchronizationJob-id">
    <td><CopyableCode code="synchronizationJob-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of synchronizationJob</td>
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
        { label: 'bulk_upload', value: 'bulk_upload' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieve the existing synchronization job and its properties.

```sql
SELECT
id,
@odata.type,
bulkUpload,
schedule,
schema,
status,
synchronizationJobSettings,
templateId
FROM entra_id.service_principals.synchronization_jobs
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
AND synchronizationJob-id = '{{ synchronizationJob-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="bulk_upload">

The bulk upload operation for the job.

```sql
SELECT
id,
@odata.type
FROM entra_id.service_principals.synchronization_jobs
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
AND synchronizationJob-id = '{{ synchronizationJob-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List existing jobs for a given application instance (service principal).

```sql
SELECT
id,
@odata.type,
bulkUpload,
schedule,
schema,
status,
synchronizationJobSettings,
templateId
FROM entra_id.service_principals.synchronization_jobs
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' -- required
AND $top = '{{ $top }}'
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

Create new synchronization job with a default synchronization schema. The job is created in a disabled state. Call Start job to start synchronization.

```sql
INSERT INTO entra_id.service_principals.synchronization_jobs (
id,
@odata.type,
schedule,
status,
synchronizationJobSettings,
templateId,
bulkUpload,
schema,
servicePrincipal-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ schedule }}',
'{{ status }}',
'{{ synchronizationJobSettings }}',
'{{ templateId }}',
'{{ bulkUpload }}',
'{{ schema }}',
'{{ servicePrincipal-id }}'
RETURNING
id,
@odata.type,
bulkUpload,
schedule,
schema,
status,
synchronizationJobSettings,
templateId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: synchronization_jobs
  props:
    - name: servicePrincipal-id
      value: "{{ servicePrincipal-id }}"
      description: Required parameter for the synchronization_jobs resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: schedule
      value: "{{ schedule }}"
      description: |
        Schedule used to run the job. Read-only.
    - name: status
      value: "{{ status }}"
      description: |
        Status of the job, which includes when the job was last run, current job state, and errors.
    - name: synchronizationJobSettings
      description: |
        Settings associated with the job. Some settings are inherited from the template.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
          @odata.type: "{{ @odata.type }}"
    - name: templateId
      value: "{{ templateId }}"
      description: |
        Identifier of the synchronization template this job is based on.
    - name: bulkUpload
      value: "{{ bulkUpload }}"
      description: |
        The bulk upload operation for the job.
    - name: schema
      value: "{{ schema }}"
      description: |
        The synchronization schema configured for the job.
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
UPDATE entra_id.service_principals.synchronization_jobs
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
schedule = '{{ schedule }}',
status = '{{ status }}',
synchronizationJobSettings = '{{ synchronizationJobSettings }}',
templateId = '{{ templateId }}',
bulkUpload = '{{ bulkUpload }}',
schema = '{{ schema }}'
WHERE 
servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND synchronizationJob-id = '{{ synchronizationJob-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
bulkUpload,
schedule,
schema,
status,
synchronizationJobSettings,
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

Stop the synchronization job, and permanently delete all the state associated with it. Synchronized accounts are left as-is.

```sql
DELETE FROM entra_id.service_principals.synchronization_jobs
WHERE servicePrincipal-id = '{{ servicePrincipal-id }}' --required
AND synchronizationJob-id = '{{ synchronizationJob-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="pause"
    values={[
        { label: 'pause', value: 'pause' },
        { label: 'provision_on_demand', value: 'provision_on_demand' },
        { label: 'start', value: 'start' },
        { label: 'validate_credentials', value: 'validate_credentials' },
        { label: 'validate_credentials_2', value: 'validate_credentials_2' }
    ]}
>
<TabItem value="pause">

Temporarily stop a running synchronization job. All the progress, including job state, is persisted, and the job will continue from where it left off when a start call is made.

```sql
EXEC entra_id.service_principals.synchronization_jobs.pause 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required, 
@synchronizationJob-id='{{ synchronizationJob-id }}' --required
;
```
</TabItem>
<TabItem value="provision_on_demand">

Select a user and provision the account on-demand. The rate limit for this API is 5 requests per 10 seconds.

```sql
EXEC entra_id.service_principals.synchronization_jobs.provision_on_demand 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required, 
@synchronizationJob-id='{{ synchronizationJob-id }}' --required 
@@json=
'{
"parameters": "{{ parameters }}"
}'
;
```
</TabItem>
<TabItem value="start">

Start an existing synchronization job. If the job is in a paused state, it continues processing changes from the point where it was paused. If the job is in quarantine, the quarantine status is cleared. Don't create scripts to call the start job continuously while it's running because that can cause the service to stop running. Use the start job only when the job is currently paused or in quarantine. 

```sql
EXEC entra_id.service_principals.synchronization_jobs.start 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required, 
@synchronizationJob-id='{{ synchronizationJob-id }}' --required
;
```
</TabItem>
<TabItem value="validate_credentials">

Validate that the credentials are valid in the tenant.

```sql
EXEC entra_id.service_principals.synchronization_jobs.validate_credentials 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required, 
@synchronizationJob-id='{{ synchronizationJob-id }}' --required 
@@json=
'{
"applicationIdentifier": "{{ applicationIdentifier }}", 
"templateId": "{{ templateId }}", 
"useSavedCredentials": {{ useSavedCredentials }}, 
"credentials": "{{ credentials }}"
}'
;
```
</TabItem>
<TabItem value="validate_credentials_2">

Success

```sql
EXEC entra_id.service_principals.synchronization_jobs.validate_credentials_2 
@servicePrincipal-id='{{ servicePrincipal-id }}' --required 
@@json=
'{
"applicationIdentifier": "{{ applicationIdentifier }}", 
"templateId": "{{ templateId }}", 
"useSavedCredentials": {{ useSavedCredentials }}, 
"credentials": "{{ credentials }}"
}'
;
```
</TabItem>
</Tabs>
