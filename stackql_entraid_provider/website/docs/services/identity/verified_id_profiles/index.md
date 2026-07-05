--- 
title: verified_id_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_id_profiles
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

Creates, updates, deletes, gets or lists a <code>verified_id_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="verified_id_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity.verified_id_profiles" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Display name for the verified ID profile. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the verified ID profile. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="faceCheckConfiguration" /></td>
    <td><code>object</code></td>
    <td> (title: faceCheckConfiguration)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime the profile was last modified. Optional. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>number (int32)</code></td>
    <td>Defines profile processing priority if multiple profiles are configured. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td> (enabled, disabled, unknownFutureValue) (title: verifiedIdProfileState)</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedIdProfileConfiguration" /></td>
    <td><code>object</code></td>
    <td> (title: verifiedIdProfileConfiguration)</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedIdUsageConfigurations" /></td>
    <td><code>array</code></td>
    <td>Collection defining the usage purpose for the profile. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="verifierDid" /></td>
    <td><code>string</code></td>
    <td>Decentralized Identifier (DID) string that represents the verifier in the verifiable credential exchange. Required.</td>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Display name for the verified ID profile. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description for the verified ID profile. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="faceCheckConfiguration" /></td>
    <td><code>object</code></td>
    <td> (title: faceCheckConfiguration)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime the profile was last modified. Optional. (pattern: <code>^&#91;0-9&#93;&#123;4,&#125;-(0&#91;1-9&#93;|1&#91;012&#93;)-(0&#91;1-9&#93;|&#91;12&#93;&#91;0-9&#93;|3&#91;01&#93;)T(&#91;01&#93;&#91;0-9&#93;|2&#91;0-3&#93;):&#91;0-5&#93;&#91;0-9&#93;:&#91;0-5&#93;&#91;0-9&#93;(&#91;.&#93;&#91;0-9&#93;&#123;1,12&#125;)?(Z|&#91;+-&#93;&#91;0-9&#93;&#91;0-9&#93;:&#91;0-9&#93;&#91;0-9&#93;)$</code>)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>number (int32)</code></td>
    <td>Defines profile processing priority if multiple profiles are configured. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td> (enabled, disabled, unknownFutureValue) (title: verifiedIdProfileState)</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedIdProfileConfiguration" /></td>
    <td><code>object</code></td>
    <td> (title: verifiedIdProfileConfiguration)</td>
</tr>
<tr>
    <td><CopyableCode code="verifiedIdUsageConfigurations" /></td>
    <td><code>array</code></td>
    <td>Collection defining the usage purpose for the profile. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="verifierDid" /></td>
    <td><code>string</code></td>
    <td>Decentralized Identifier (DID) string that represents the verifier in the verifiable credential exchange. Required.</td>
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
    <td><a href="#parameter-verified_id_profile_id"><code>verified_id_profile_id</code></a></td>
    <td></td>
    <td>Read the properties and relationships of verifiedIdProfile object.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Get a list of the verifiedIdProfile objects and their properties.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new verifiedIdProfile object.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-verified_id_profile_id"><code>verified_id_profile_id</code></a></td>
    <td></td>
    <td>Update the properties of a verifiedIdProfile object.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-verified_id_profile_id"><code>verified_id_profile_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a verifiedIdProfile object.</td>
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
<tr id="parameter-verified_id_profile_id">
    <td><CopyableCode code="verified_id_profile_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of verifiedIdProfile</td>
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

Read the properties and relationships of verifiedIdProfile object.

```sql
SELECT
id,
name,
description,
faceCheckConfiguration,
lastModifiedDateTime,
priority,
state,
verifiedIdProfileConfiguration,
verifiedIdUsageConfigurations,
verifierDid
FROM entra_id.identity.verified_id_profiles
WHERE verified_id_profile_id = '{{ verified_id_profile_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of the verifiedIdProfile objects and their properties.

```sql
SELECT
id,
name,
description,
faceCheckConfiguration,
lastModifiedDateTime,
priority,
state,
verifiedIdProfileConfiguration,
verifiedIdUsageConfigurations,
verifierDid
FROM entra_id.identity.verified_id_profiles
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

Create a new verifiedIdProfile object.

```sql
INSERT INTO entra_id.identity.verified_id_profiles (
id,
description,
faceCheckConfiguration,
lastModifiedDateTime,
name,
priority,
state,
verifiedIdProfileConfiguration,
verifiedIdUsageConfigurations,
verifierDid
)
SELECT 
'{{ id }}',
'{{ description }}',
'{{ faceCheckConfiguration }}',
'{{ lastModifiedDateTime }}',
'{{ name }}',
{{ priority }},
'{{ state }}',
'{{ verifiedIdProfileConfiguration }}',
'{{ verifiedIdUsageConfigurations }}',
'{{ verifierDid }}'
RETURNING
id,
name,
description,
faceCheckConfiguration,
lastModifiedDateTime,
priority,
state,
verifiedIdProfileConfiguration,
verifiedIdUsageConfigurations,
verifierDid
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: verified_id_profiles
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: description
      value: "{{ description }}"
      description: |
        Description for the verified ID profile. Required.
    - name: faceCheckConfiguration
      value:
        isEnabled: {{ isEnabled }}
        sourcePhotoClaimName: "{{ sourcePhotoClaimName }}"
    - name: lastModifiedDateTime
      value: "{{ lastModifiedDateTime }}"
      description: |
        DateTime the profile was last modified. Optional.
    - name: name
      value: "{{ name }}"
      description: |
        Display name for the verified ID profile. Required.
    - name: priority
      value: {{ priority }}
      description: |
        Defines profile processing priority if multiple profiles are configured. Optional.
    - name: state
      value: "{{ state }}"
      valid_values: ['enabled', 'disabled', 'unknownFutureValue']
    - name: verifiedIdProfileConfiguration
      value:
        acceptedIssuer: "{{ acceptedIssuer }}"
        claimBindings:
          - matchConfidenceLevel: "{{ matchConfidenceLevel }}"
            sourceAttribute: "{{ sourceAttribute }}"
            verifiedIdClaim: "{{ verifiedIdClaim }}"
        claimBindingSource: "{{ claimBindingSource }}"
        claimValidation:
          customExtensionId: "{{ customExtensionId }}"
          isEnabled: {{ isEnabled }}
        type: "{{ type }}"
    - name: verifiedIdUsageConfigurations
      description: |
        Collection defining the usage purpose for the profile. Required.
      value:
        - isEnabledForTestOnly: {{ isEnabledForTestOnly }}
          purpose: "{{ purpose }}"
    - name: verifierDid
      value: "{{ verifierDid }}"
      description: |
        Decentralized Identifier (DID) string that represents the verifier in the verifiable credential exchange. Required.
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

Update the properties of a verifiedIdProfile object.

```sql
UPDATE entra_id.identity.verified_id_profiles
SET 
id = '{{ id }}',
description = '{{ description }}',
faceCheckConfiguration = '{{ faceCheckConfiguration }}',
lastModifiedDateTime = '{{ lastModifiedDateTime }}',
name = '{{ name }}',
priority = {{ priority }},
state = '{{ state }}',
verifiedIdProfileConfiguration = '{{ verifiedIdProfileConfiguration }}',
verifiedIdUsageConfigurations = '{{ verifiedIdUsageConfigurations }}',
verifierDid = '{{ verifierDid }}'
WHERE 
verified_id_profile_id = '{{ verified_id_profile_id }}' --required
RETURNING
id,
name,
description,
faceCheckConfiguration,
lastModifiedDateTime,
priority,
state,
verifiedIdProfileConfiguration,
verifiedIdUsageConfigurations,
verifierDid;
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

Delete a verifiedIdProfile object.

```sql
DELETE FROM entra_id.identity.verified_id_profiles
WHERE verified_id_profile_id = '{{ verified_id_profile_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
