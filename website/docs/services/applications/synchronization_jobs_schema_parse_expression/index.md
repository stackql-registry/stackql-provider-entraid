--- 
title: synchronization_jobs_schema_parse_expression
hide_title: false
hide_table_of_contents: false
keywords:
  - synchronization_jobs_schema_parse_expression
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

Creates, updates, deletes, gets or lists a <code>synchronization_jobs_schema_parse_expression</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="synchronization_jobs_schema_parse_expression" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.applications.synchronization_jobs_schema_parse_expression" /></td></tr>
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
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application-id"><code>application-id</code></a>, <a href="#parameter-synchronizationJob-id"><code>synchronizationJob-id</code></a></td>
    <td></td>
    <td>Parse a given string expression into an attributeMappingSource object. For more information about expressions, see Writing Expressions for Attribute Mappings in Microsoft Entra ID.</td>
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
<tr id="parameter-application-id">
    <td><CopyableCode code="application-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of application</td>
</tr>
<tr id="parameter-synchronizationJob-id">
    <td><CopyableCode code="synchronizationJob-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of synchronizationJob</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="insert"
    values={[
        { label: 'insert', value: 'insert' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="insert">

Parse a given string expression into an attributeMappingSource object. For more information about expressions, see Writing Expressions for Attribute Mappings in Microsoft Entra ID.

```sql
INSERT INTO entra_id.applications.synchronization_jobs_schema_parse_expression (
expression,
testInputObject,
targetAttributeDefinition,
application-id,
synchronizationJob-id
)
SELECT 
'{{ expression }}',
'{{ testInputObject }}',
'{{ targetAttributeDefinition }}',
'{{ application-id }}',
'{{ synchronizationJob-id }}'
RETURNING
@odata.type,
error,
evaluationResult,
evaluationSucceeded,
parsedExpression,
parsingSucceeded
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: synchronization_jobs_schema_parse_expression
  props:
    - name: application-id
      value: "{{ application-id }}"
      description: Required parameter for the synchronization_jobs_schema_parse_expression resource.
    - name: synchronizationJob-id
      value: "{{ synchronizationJob-id }}"
      description: Required parameter for the synchronization_jobs_schema_parse_expression resource.
    - name: expression
      value: "{{ expression }}"
    - name: testInputObject
      description: |
        (opaque JSON object)
      value:
        definition:
          attributes:
            - anchor: {{ anchor }}
              apiExpressions: "{{ apiExpressions }}"
              caseExact: {{ caseExact }}
              defaultValue: "{{ defaultValue }}"
              flowNullValues: {{ flowNullValues }}
              metadata: "{{ metadata }}"
              multivalued: {{ multivalued }}
              mutability: "{{ mutability }}"
              name: "{{ name }}"
              referencedObjects: "{{ referencedObjects }}"
              required: {{ required }}
              type: "{{ type }}"
              @odata.type: "{{ @odata.type }}"
          metadata:
            - key: "{{ key }}"
              value: "{{ value }}"
              @odata.type: "{{ @odata.type }}"
          name: "{{ name }}"
          supportedApis:
            - "{{ supportedApis }}"
          @odata.type: "{{ @odata.type }}"
        properties:
          - key: "{{ key }}"
            @odata.type: "{{ @odata.type }}"
        @odata.type: "{{ @odata.type }}"
    - name: targetAttributeDefinition
      description: |
        (opaque JSON object)
      value:
        anchor: {{ anchor }}
        apiExpressions:
          - key: "{{ key }}"
            value: "{{ value }}"
            @odata.type: "{{ @odata.type }}"
        caseExact: {{ caseExact }}
        defaultValue: "{{ defaultValue }}"
        flowNullValues: {{ flowNullValues }}
        metadata:
          - key: "{{ key }}"
            value: "{{ value }}"
            @odata.type: "{{ @odata.type }}"
        multivalued: {{ multivalued }}
        mutability: "{{ mutability }}"
        name: "{{ name }}"
        referencedObjects:
          - referencedObjectName: "{{ referencedObjectName }}"
            referencedProperty: "{{ referencedProperty }}"
            @odata.type: "{{ @odata.type }}"
        required: {{ required }}
        type: "{{ type }}"
        @odata.type: "{{ @odata.type }}"
`}</CodeBlock>

</TabItem>
</Tabs>
