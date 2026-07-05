--- 
title: synchronization_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_jobs
  - applications
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
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.applications.synchronization_jobs" /></td></tr>
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
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td>Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#get_bulk_upload"><CopyableCode code="get_bulk_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>The bulk upload operation for the job.</td>
</tr>
<tr>
    <td><a href="#update_bulk_upload"><CopyableCode code="update_bulk_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete_bulk_upload"><CopyableCode code="delete_bulk_upload" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#pause"><CopyableCode code="pause" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Temporarily stop a running synchronization job. All the progress, including job state, is persisted, and the job will continue from where it left off when a start call is made.</td>
</tr>
<tr>
    <td><a href="#provision_on_demand"><CopyableCode code="provision_on_demand" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Select a user and provision the account on-demand. The rate limit for this API is 5 requests per 10 seconds.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Restart a stopped synchronization job, forcing it to reprocess all the objects in the directory. Optionally clears existing the synchronization state and previous errors.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Start an existing synchronization job. If the job is in a paused state, it continues processing changes from the point where it was paused. If the job is in quarantine, the quarantine status is cleared. Don't create scripts to call the start job continuously while it's running because that can cause the service to stop running. Use the start job only when the job is currently paused or in quarantine. </td>
</tr>
<tr>
    <td><a href="#validate_credentials"><CopyableCode code="validate_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Validate that the credentials are valid in the tenant.</td>
</tr>
<tr>
    <td><a href="#schema_directories_discover"><CopyableCode code="schema_directories_discover" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a>, <a href="#parameter-directory_definition_id"><code>directory_definition_id</code></a></td>
    <td></td>
    <td>Discover the latest schema definition for provisioning to an application. </td>
</tr>
<tr>
    <td><a href="#schema_parse_expression"><CopyableCode code="schema_parse_expression" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-synchronization_job_id"><code>synchronization_job_id</code></a></td>
    <td></td>
    <td>Parse a given string expression into an attributeMappingSource object. For more information about expressions, see Writing Expressions for Attribute Mappings in Microsoft Entra ID.</td>
</tr>
<tr>
    <td><a href="#validate_credentials_2"><CopyableCode code="validate_credentials_2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a></td>
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
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of application</td>
</tr>
<tr id="parameter-directory_definition_id">
    <td><CopyableCode code="directory_definition_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of directoryDefinition</td>
</tr>
<tr id="parameter-synchronization_job_id">
    <td><CopyableCode code="synchronization_job_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of synchronizationJob</td>
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

Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.

```sql
SELECT
id,
bulkUpload,
schedule,
schema,
status,
synchronizationJobSettings,
templateId
FROM entra_id.applications.synchronization_jobs
WHERE application_id = '{{ application_id }}' -- required
AND synchronization_job_id = '{{ synchronization_job_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.

```sql
SELECT
id,
bulkUpload,
schedule,
schema,
status,
synchronizationJobSettings,
templateId
FROM entra_id.applications.synchronization_jobs
WHERE application_id = '{{ application_id }}' -- required
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
INSERT INTO entra_id.applications.synchronization_jobs (
id,
schedule,
status,
synchronizationJobSettings,
templateId,
bulkUpload,
schema,
application_id
)
SELECT 
'{{ id }}',
'{{ schedule }}',
'{{ status }}',
'{{ synchronizationJobSettings }}',
'{{ templateId }}',
'{{ bulkUpload }}',
'{{ schema }}',
'{{ application_id }}'
RETURNING
id,
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
    - name: application_id
      value: "{{ application_id }}"
      description: Required parameter for the synchronization_jobs resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
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
UPDATE entra_id.applications.synchronization_jobs
SET 
id = '{{ id }}',
schedule = '{{ schedule }}',
status = '{{ status }}',
synchronizationJobSettings = '{{ synchronizationJobSettings }}',
templateId = '{{ templateId }}',
bulkUpload = '{{ bulkUpload }}',
schema = '{{ schema }}'
WHERE 
application_id = '{{ application_id }}' --required
AND synchronization_job_id = '{{ synchronization_job_id }}' --required
RETURNING
id,
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

No description available.

```sql
DELETE FROM entra_id.applications.synchronization_jobs
WHERE application_id = '{{ application_id }}' --required
AND synchronization_job_id = '{{ synchronization_job_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_bulk_upload"
    values={[
        { label: 'get_bulk_upload', value: 'get_bulk_upload' },
        { label: 'update_bulk_upload', value: 'update_bulk_upload' },
        { label: 'delete_bulk_upload', value: 'delete_bulk_upload' },
        { label: 'pause', value: 'pause' },
        { label: 'provision_on_demand', value: 'provision_on_demand' },
        { label: 'restart', value: 'restart' },
        { label: 'start', value: 'start' },
        { label: 'validate_credentials', value: 'validate_credentials' },
        { label: 'schema_directories_discover', value: 'schema_directories_discover' },
        { label: 'schema_parse_expression', value: 'schema_parse_expression' },
        { label: 'validate_credentials_2', value: 'validate_credentials_2' }
    ]}
>
<TabItem value="get_bulk_upload">

The bulk upload operation for the job.

```sql
EXEC entra_id.applications.synchronization_jobs.get_bulk_upload 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required, 
@$select='{{ $select }}', 
@$expand='{{ $expand }}'
;
```
</TabItem>
<TabItem value="update_bulk_upload">

Success

```sql
EXEC entra_id.applications.synchronization_jobs.update_bulk_upload 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required 
@@json=
'{
"id": "{{ id }}", 
}'
;
```
</TabItem>
<TabItem value="delete_bulk_upload">

Success

```sql
EXEC entra_id.applications.synchronization_jobs.delete_bulk_upload 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required, 
@If-Match='{{ If-Match }}'
;
```
</TabItem>
<TabItem value="pause">

Temporarily stop a running synchronization job. All the progress, including job state, is persisted, and the job will continue from where it left off when a start call is made.

```sql
EXEC entra_id.applications.synchronization_jobs.pause 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required
;
```
</TabItem>
<TabItem value="provision_on_demand">

Select a user and provision the account on-demand. The rate limit for this API is 5 requests per 10 seconds.

```sql
EXEC entra_id.applications.synchronization_jobs.provision_on_demand 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required 
@@json=
'{
"parameters": "{{ parameters }}"
}'
;
```
</TabItem>
<TabItem value="restart">

Restart a stopped synchronization job, forcing it to reprocess all the objects in the directory. Optionally clears existing the synchronization state and previous errors.

```sql
EXEC entra_id.applications.synchronization_jobs.restart 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required 
@@json=
'{
"criteria": "{{ criteria }}"
}'
;
```
</TabItem>
<TabItem value="start">

Start an existing synchronization job. If the job is in a paused state, it continues processing changes from the point where it was paused. If the job is in quarantine, the quarantine status is cleared. Don't create scripts to call the start job continuously while it's running because that can cause the service to stop running. Use the start job only when the job is currently paused or in quarantine. 

```sql
EXEC entra_id.applications.synchronization_jobs.start 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required
;
```
</TabItem>
<TabItem value="validate_credentials">

Validate that the credentials are valid in the tenant.

```sql
EXEC entra_id.applications.synchronization_jobs.validate_credentials 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required 
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
<TabItem value="schema_directories_discover">

Discover the latest schema definition for provisioning to an application. 

```sql
EXEC entra_id.applications.synchronization_jobs.schema_directories_discover 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required, 
@directory_definition_id='{{ directory_definition_id }}' --required
;
```
</TabItem>
<TabItem value="schema_parse_expression">

Parse a given string expression into an attributeMappingSource object. For more information about expressions, see Writing Expressions for Attribute Mappings in Microsoft Entra ID.

```sql
EXEC entra_id.applications.synchronization_jobs.schema_parse_expression 
@application_id='{{ application_id }}' --required, 
@synchronization_job_id='{{ synchronization_job_id }}' --required 
@@json=
'{
"expression": "{{ expression }}", 
"testInputObject": "{{ testInputObject }}", 
"targetAttributeDefinition": "{{ targetAttributeDefinition }}"
}'
;
```
</TabItem>
<TabItem value="validate_credentials_2">

Success

```sql
EXEC entra_id.applications.synchronization_jobs.validate_credentials_2 
@application_id='{{ application_id }}' --required 
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
