--- 
title: group_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - group_settings
  - group_settings
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

Creates, updates, deletes, gets or lists a <code>group_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="group_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.group_settings.group_settings" /></td></tr>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of this group of settings, which comes from the associated template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the tenant-level groupSettingTemplates object that's been customized for this group-level settings object. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Collection of name-value pairs corresponding to the name and defaultValue properties in the referenced groupSettingTemplates object.</td>
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
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of this group of settings, which comes from the associated template.</td>
</tr>
<tr>
    <td><CopyableCode code="templateId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier for the tenant-level groupSettingTemplates object that's been customized for this group-level settings object. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="values" /></td>
    <td><code>array</code></td>
    <td>Collection of name-value pairs corresponding to the name and defaultValue properties in the referenced groupSettingTemplates object.</td>
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
    <td><a href="#parameter-group_setting_id"><code>group_setting_id</code></a></td>
    <td></td>
    <td>Retrieve the properties of a specific group setting object. The setting can be a tenant-level or group-specific setting.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Retrieve a list of tenant-level or group-specific group settings objects.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td></td>
    <td></td>
    <td>Create a new group setting based on the templates available in groupSettingTemplates. These settings can be at the tenant-level or at the group level. Group settings apply to only Microsoft 365 groups. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-group_setting_id"><code>group_setting_id</code></a></td>
    <td></td>
    <td>Update the properties of a groupSetting object for tenant-wide group settings or a specific group setting.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-group_setting_id"><code>group_setting_id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a tenant-level or group-specific groupSetting object.</td>
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
<tr id="parameter-group_setting_id">
    <td><CopyableCode code="group_setting_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of groupSetting</td>
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

Retrieve the properties of a specific group setting object. The setting can be a tenant-level or group-specific setting.

```sql
SELECT
id,
displayName,
templateId,
values
FROM entra_id.group_settings.group_settings
WHERE group_setting_id = '{{ group_setting_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve a list of tenant-level or group-specific group settings objects.

```sql
SELECT
id,
displayName,
templateId,
values
FROM entra_id.group_settings.group_settings
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

Create a new group setting based on the templates available in groupSettingTemplates. These settings can be at the tenant-level or at the group level. Group settings apply to only Microsoft 365 groups. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.

```sql
INSERT INTO entra_id.group_settings.group_settings (
id,
displayName,
templateId,
values
)
SELECT 
'{{ id }}',
'{{ displayName }}',
'{{ templateId }}',
'{{ values }}'
RETURNING
id,
displayName,
templateId,
values
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: group_settings
  props:
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        Display name of this group of settings, which comes from the associated template.
    - name: templateId
      value: "{{ templateId }}"
      description: |
        Unique identifier for the tenant-level groupSettingTemplates object that's been customized for this group-level settings object. Read-only.
    - name: values
      description: |
        Collection of name-value pairs corresponding to the name and defaultValue properties in the referenced groupSettingTemplates object.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
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

Update the properties of a groupSetting object for tenant-wide group settings or a specific group setting.

```sql
UPDATE entra_id.group_settings.group_settings
SET 
id = '{{ id }}',
displayName = '{{ displayName }}',
templateId = '{{ templateId }}',
values = '{{ values }}'
WHERE 
group_setting_id = '{{ group_setting_id }}' --required
RETURNING
id,
displayName,
templateId,
values;
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

Delete a tenant-level or group-specific groupSetting object.

```sql
DELETE FROM entra_id.group_settings.group_settings
WHERE group_setting_id = '{{ group_setting_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
