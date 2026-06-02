--- 
title: b2x_user_flows_api_connector_configuration_post_federation_signup
hide_title: false
hide_table_of_contents: false
keywords:
  - b2x_user_flows_api_connector_configuration_post_federation_signup
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

Creates, updates, deletes, gets or lists a <code>b2x_user_flows_api_connector_configuration_post_federation_signup</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="b2x_user_flows_api_connector_configuration_post_federation_signup" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.b2x_user_flows_api_connector_configuration_post_federation_signup" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#add_ref"><CopyableCode code="add_ref" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#remove_ref"><CopyableCode code="remove_ref" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td></td>
</tr>
<tr>
    <td><a href="#upload_client_certificate"><CopyableCode code="upload_client_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-b2xIdentityUserFlow-id"><code>b2xIdentityUserFlow-id</code></a></td>
    <td></td>
    <td>Upload a PKCS 12 format key (.pfx) to an API connector's authentication configuration. The input is a base-64 encoded value of the PKCS 12 certificate contents. This method returns an apiConnector.</td>
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
<tr id="parameter-b2xIdentityUserFlow-id">
    <td><CopyableCode code="b2xIdentityUserFlow-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of b2xIdentityUserFlow</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="add_ref"
    values={[
        { label: 'add_ref', value: 'add_ref' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="add_ref">

No description available.

```sql
INSERT INTO entra_id.identity.b2x_user_flows_api_connector_configuration_post_federation_signup (
@odata.id,
@odata.type,
b2xIdentityUserFlow-id
)
SELECT 
'{{ @odata.id }}',
'{{ @odata.type }}',
'{{ b2xIdentityUserFlow-id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: b2x_user_flows_api_connector_configuration_post_federation_signup
  props:
    - name: b2xIdentityUserFlow-id
      value: "{{ b2xIdentityUserFlow-id }}"
      description: Required parameter for the b2x_user_flows_api_connector_configuration_post_federation_signup resource.
    - name: @odata.id
      value: "{{ @odata.id }}"
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

No description available.

```sql
UPDATE entra_id.identity.b2x_user_flows_api_connector_configuration_post_federation_signup
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
authenticationConfiguration = '{{ authenticationConfiguration }}',
displayName = '{{ displayName }}',
targetUrl = '{{ targetUrl }}'
WHERE 
b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
authenticationConfiguration,
displayName,
targetUrl;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' },
        { label: 'remove_ref', value: 'remove_ref' }
    ]}
>
<TabItem value="delete">

No description available.

```sql
DELETE FROM entra_id.identity.b2x_user_flows_api_connector_configuration_post_federation_signup
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
<TabItem value="remove_ref">

No description available.

```sql
DELETE FROM entra_id.identity.b2x_user_flows_api_connector_configuration_post_federation_signup
WHERE b2xIdentityUserFlow-id = '{{ b2xIdentityUserFlow-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="upload_client_certificate"
    values={[
        { label: 'upload_client_certificate', value: 'upload_client_certificate' }
    ]}
>
<TabItem value="upload_client_certificate">

Upload a PKCS 12 format key (.pfx) to an API connector's authentication configuration. The input is a base-64 encoded value of the PKCS 12 certificate contents. This method returns an apiConnector.

```sql
EXEC entra_id.identity.b2x_user_flows_api_connector_configuration_post_federation_signup.upload_client_certificate 
@b2xIdentityUserFlow-id='{{ b2xIdentityUserFlow-id }}' --required 
@@json=
'{
"pkcs12Value": "{{ pkcs12Value }}", 
"password": "{{ password }}"
}'
;
```
</TabItem>
</Tabs>
