--- 
title: lifecycle_workflows_workflows_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - lifecycle_workflows_workflows_tasks
  - identity_governance
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

Creates, updates, deletes, gets or lists a <code>lifecycle_workflows_workflows_tasks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="lifecycle_workflows_workflows_tasks" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.identity_governance.lifecycle_workflows_workflows_tasks" /></td></tr>
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
    <td><CopyableCode code="arguments" /></td>
    <td><code>array</code></td>
    <td>Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td> (joiner, leaver, unknownFutureValue, mover) (title: lifecycleTaskCategory)</td>
</tr>
<tr>
    <td><CopyableCode code="continueOnError" /></td>
    <td><code>boolean</code></td>
    <td>A Boolean value that specifies whether, if this task fails, the workflow stops, and subsequent tasks aren't run. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A string that describes the purpose of the task for administrative use. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.</td>
</tr>
<tr>
    <td><CopyableCode code="executionSequence" /></td>
    <td><code>number (int32)</code></td>
    <td>An integer that states in what order the task runs in a workflow.Supports $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>A Boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.</td>
</tr>
<tr>
    <td><CopyableCode code="taskDefinitionId" /></td>
    <td><code>string</code></td>
    <td>A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.Supports $filter(eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="taskProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The result of processing the task.</td>
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
    <td><CopyableCode code="arguments" /></td>
    <td><code>array</code></td>
    <td>Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td> (joiner, leaver, unknownFutureValue, mover) (title: lifecycleTaskCategory)</td>
</tr>
<tr>
    <td><CopyableCode code="continueOnError" /></td>
    <td><code>boolean</code></td>
    <td>A Boolean value that specifies whether, if this task fails, the workflow stops, and subsequent tasks aren't run. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A string that describes the purpose of the task for administrative use. Optional.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.</td>
</tr>
<tr>
    <td><CopyableCode code="executionSequence" /></td>
    <td><code>number (int32)</code></td>
    <td>An integer that states in what order the task runs in a workflow.Supports $orderby.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>A Boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.</td>
</tr>
<tr>
    <td><CopyableCode code="taskDefinitionId" /></td>
    <td><code>string</code></td>
    <td>A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.Supports $filter(eq, ne).</td>
</tr>
<tr>
    <td><CopyableCode code="taskProcessingResults" /></td>
    <td><code>array</code></td>
    <td>The result of processing the task.</td>
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
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a></td>
    <td></td>
    <td>Get a specific task from a workflow or workflowVersion.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a></td>
    <td></td>
    <td>Retrieve the details of the built-in tasks in Lifecycle Workflows.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-workflow_id"><code>workflow_id</code></a>, <a href="#parameter-task_id"><code>task_id</code></a></td>
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
<tr id="parameter-task_id">
    <td><CopyableCode code="task_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of task</td>
</tr>
<tr id="parameter-workflow_id">
    <td><CopyableCode code="workflow_id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of workflow</td>
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

Get a specific task from a workflow or workflowVersion.

```sql
SELECT
id,
arguments,
category,
continueOnError,
description,
displayName,
executionSequence,
isEnabled,
taskDefinitionId,
taskProcessingResults
FROM entra_id.identity_governance.lifecycle_workflows_workflows_tasks
WHERE workflow_id = '{{ workflow_id }}' -- required
AND task_id = '{{ task_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Retrieve the details of the built-in tasks in Lifecycle Workflows.

```sql
SELECT
id,
arguments,
category,
continueOnError,
description,
displayName,
executionSequence,
isEnabled,
taskDefinitionId,
taskProcessingResults
FROM entra_id.identity_governance.lifecycle_workflows_workflows_tasks
WHERE workflow_id = '{{ workflow_id }}' -- required
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
INSERT INTO entra_id.identity_governance.lifecycle_workflows_workflows_tasks (
id,
arguments,
category,
continueOnError,
description,
displayName,
executionSequence,
isEnabled,
taskDefinitionId,
taskProcessingResults,
workflow_id
)
SELECT 
'{{ id }}',
'{{ arguments }}',
'{{ category }}',
{{ continueOnError }},
'{{ description }}',
'{{ displayName }}',
{{ executionSequence }},
{{ isEnabled }},
'{{ taskDefinitionId }}',
'{{ taskProcessingResults }}',
'{{ workflow_id }}'
RETURNING
id,
arguments,
category,
continueOnError,
description,
displayName,
executionSequence,
isEnabled,
taskDefinitionId,
taskProcessingResults
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: lifecycle_workflows_workflows_tasks
  props:
    - name: workflow_id
      value: "{{ workflow_id }}"
      description: Required parameter for the lifecycle_workflows_workflows_tasks resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: arguments
      description: |
        Arguments included within the task.  For guidance to configure this property, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
    - name: category
      value: "{{ category }}"
      valid_values: ['joiner', 'leaver', 'unknownFutureValue', 'mover']
    - name: continueOnError
      value: {{ continueOnError }}
      description: |
        A Boolean value that specifies whether, if this task fails, the workflow stops, and subsequent tasks aren't run. Optional.
    - name: description
      value: "{{ description }}"
      description: |
        A string that describes the purpose of the task for administrative use. Optional.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        A unique string that identifies the task. Required.Supports $filter(eq, ne) and orderBy.
    - name: executionSequence
      value: {{ executionSequence }}
      description: |
        An integer that states in what order the task runs in a workflow.Supports $orderby.
    - name: isEnabled
      value: {{ isEnabled }}
      description: |
        A Boolean value that denotes whether the task is set to run or not. Optional.Supports $filter(eq, ne) and orderBy.
    - name: taskDefinitionId
      value: "{{ taskDefinitionId }}"
      description: |
        A unique template identifier for the task. For more information about the tasks that Lifecycle Workflows currently supports and their unique identifiers, see Configure the arguments for built-in Lifecycle Workflow tasks. Required.Supports $filter(eq, ne).
    - name: taskProcessingResults
      description: |
        The result of processing the task.
      value:
        - id: "{{ id }}"
          completedDateTime: "{{ completedDateTime }}"
          createdDateTime: "{{ createdDateTime }}"
          failureReason: "{{ failureReason }}"
          processingInfo: "{{ processingInfo }}"
          processingStatus: "{{ processingStatus }}"
          startedDateTime: "{{ startedDateTime }}"
          subject:
            id: "{{ id }}"
            deletedDateTime: "{{ deletedDateTime }}"
            aboutMe: "{{ aboutMe }}"
            accountEnabled: {{ accountEnabled }}
            ageGroup: "{{ ageGroup }}"
            assignedLicenses:
              - disabledPlans: "{{ disabledPlans }}"
                skuId: "{{ skuId }}"
            assignedPlans:
              - assignedDateTime: "{{ assignedDateTime }}"
                capabilityStatus: "{{ capabilityStatus }}"
                service: "{{ service }}"
                servicePlanId: "{{ servicePlanId }}"
            authorizationInfo: "{{ authorizationInfo }}"
            birthday: "{{ birthday }}"
            businessPhones:
              - "{{ businessPhones }}"
            city: "{{ city }}"
            companyName: "{{ companyName }}"
            consentProvidedForMinor: "{{ consentProvidedForMinor }}"
            country: "{{ country }}"
            createdDateTime: "{{ createdDateTime }}"
            creationType: "{{ creationType }}"
            customSecurityAttributes: "{{ customSecurityAttributes }}"
            department: "{{ department }}"
            deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
            displayName: "{{ displayName }}"
            employeeHireDate: "{{ employeeHireDate }}"
            employeeId: "{{ employeeId }}"
            employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
            employeeOrgData: "{{ employeeOrgData }}"
            employeeType: "{{ employeeType }}"
            externalUserState: "{{ externalUserState }}"
            externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
            faxNumber: "{{ faxNumber }}"
            givenName: "{{ givenName }}"
            hireDate: "{{ hireDate }}"
            identities:
              - issuer: "{{ issuer }}"
                issuerAssignedId: "{{ issuerAssignedId }}"
                signInType: "{{ signInType }}"
            identityParentId: "{{ identityParentId }}"
            imAddresses:
              - "{{ imAddresses }}"
            interests:
              - "{{ interests }}"
            isManagementRestricted: {{ isManagementRestricted }}
            isResourceAccount: {{ isResourceAccount }}
            jobTitle: "{{ jobTitle }}"
            lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
            legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
            licenseAssignmentStates:
              - assignedByGroup: "{{ assignedByGroup }}"
                disabledPlans: "{{ disabledPlans }}"
                error: "{{ error }}"
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                skuId: "{{ skuId }}"
                state: "{{ state }}"
            mail: "{{ mail }}"
            mailboxSettings: "{{ mailboxSettings }}"
            mailNickname: "{{ mailNickname }}"
            mobilePhone: "{{ mobilePhone }}"
            mySite: "{{ mySite }}"
            officeLocation: "{{ officeLocation }}"
            onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
            onPremisesDomainName: "{{ onPremisesDomainName }}"
            onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
            onPremisesImmutableId: "{{ onPremisesImmutableId }}"
            onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
            onPremisesProvisioningErrors:
              - category: "{{ category }}"
                occurredDateTime: "{{ occurredDateTime }}"
                propertyCausingError: "{{ propertyCausingError }}"
                value: "{{ value }}"
            onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
            onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
            onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
            onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
            otherMails:
              - "{{ otherMails }}"
            passwordPolicies: "{{ passwordPolicies }}"
            passwordProfile: "{{ passwordProfile }}"
            pastProjects:
              - "{{ pastProjects }}"
            postalCode: "{{ postalCode }}"
            preferredDataLocation: "{{ preferredDataLocation }}"
            preferredLanguage: "{{ preferredLanguage }}"
            preferredName: "{{ preferredName }}"
            print: "{{ print }}"
            provisionedPlans:
              - capabilityStatus: "{{ capabilityStatus }}"
                provisioningStatus: "{{ provisioningStatus }}"
                service: "{{ service }}"
            proxyAddresses:
              - "{{ proxyAddresses }}"
            responsibilities:
              - "{{ responsibilities }}"
            schools:
              - "{{ schools }}"
            securityIdentifier: "{{ securityIdentifier }}"
            serviceProvisioningErrors:
              - createdDateTime: "{{ createdDateTime }}"
                isResolved: {{ isResolved }}
                serviceInstance: "{{ serviceInstance }}"
            showInAddressList: {{ showInAddressList }}
            signInActivity: "{{ signInActivity }}"
            signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
            skills:
              - "{{ skills }}"
            state: "{{ state }}"
            streetAddress: "{{ streetAddress }}"
            surname: "{{ surname }}"
            usageLocation: "{{ usageLocation }}"
            userPrincipalName: "{{ userPrincipalName }}"
            userType: "{{ userType }}"
            activities:
              - id: "{{ id }}"
                activationUrl: "{{ activationUrl }}"
                activitySourceHost: "{{ activitySourceHost }}"
                appActivityId: "{{ appActivityId }}"
                appDisplayName: "{{ appDisplayName }}"
                contentInfo: "{{ contentInfo }}"
                contentUrl: "{{ contentUrl }}"
                createdDateTime: "{{ createdDateTime }}"
                expirationDateTime: "{{ expirationDateTime }}"
                fallbackUrl: "{{ fallbackUrl }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                status: "{{ status }}"
                userTimezone: "{{ userTimezone }}"
                visualElements:
                  attribution:
                    addImageQuery: {{ addImageQuery }}
                    alternateText: "{{ alternateText }}"
                    alternativeText: "{{ alternativeText }}"
                    iconUrl: "{{ iconUrl }}"
                  backgroundColor: "{{ backgroundColor }}"
                  content: "{{ content }}"
                  description: "{{ description }}"
                  displayText: "{{ displayText }}"
                historyItems: "{{ historyItems }}"
            adhocCalls:
              - id: "{{ id }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            agreementAcceptances:
              - id: "{{ id }}"
                agreementFileId: "{{ agreementFileId }}"
                agreementId: "{{ agreementId }}"
                deviceDisplayName: "{{ deviceDisplayName }}"
                deviceId: "{{ deviceId }}"
                deviceOSType: "{{ deviceOSType }}"
                deviceOSVersion: "{{ deviceOSVersion }}"
                expirationDateTime: "{{ expirationDateTime }}"
                recordedDateTime: "{{ recordedDateTime }}"
                state: "{{ state }}"
                userDisplayName: "{{ userDisplayName }}"
                userEmail: "{{ userEmail }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
            appRoleAssignments:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
                appRoleId: "{{ appRoleId }}"
                createdDateTime: "{{ createdDateTime }}"
                principalDisplayName: "{{ principalDisplayName }}"
                principalId: "{{ principalId }}"
                principalType: "{{ principalType }}"
                resourceDisplayName: "{{ resourceDisplayName }}"
                resourceId: "{{ resourceId }}"
            authentication: "{{ authentication }}"
            calendar: "{{ calendar }}"
            calendarGroups:
              - id: "{{ id }}"
                changeKey: "{{ changeKey }}"
                classId: "{{ classId }}"
                name: "{{ name }}"
                calendars: "{{ calendars }}"
            calendars:
              - id: "{{ id }}"
                allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
                canEdit: {{ canEdit }}
                canShare: {{ canShare }}
                canViewPrivateItems: {{ canViewPrivateItems }}
                changeKey: "{{ changeKey }}"
                color: "{{ color }}"
                defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
                hexColor: "{{ hexColor }}"
                isDefaultCalendar: {{ isDefaultCalendar }}
                isRemovable: {{ isRemovable }}
                isTallyingResponses: {{ isTallyingResponses }}
                name: "{{ name }}"
                owner: "{{ owner }}"
                calendarPermissions: "{{ calendarPermissions }}"
                calendarView: "{{ calendarView }}"
                events: "{{ events }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            calendarView:
              - id: "{{ id }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            chats:
              - id: "{{ id }}"
                chatType: "{{ chatType }}"
                createdDateTime: "{{ createdDateTime }}"
                isHiddenForAllMembers: {{ isHiddenForAllMembers }}
                lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                migrationMode: "{{ migrationMode }}"
                onlineMeetingInfo: "{{ onlineMeetingInfo }}"
                originalCreatedDateTime: "{{ originalCreatedDateTime }}"
                tenantId: "{{ tenantId }}"
                topic: "{{ topic }}"
                viewpoint: "{{ viewpoint }}"
                webUrl: "{{ webUrl }}"
                installedApps: "{{ installedApps }}"
                lastMessagePreview: "{{ lastMessagePreview }}"
                members: "{{ members }}"
                messages: "{{ messages }}"
                permissionGrants: "{{ permissionGrants }}"
                pinnedMessages: "{{ pinnedMessages }}"
                tabs: "{{ tabs }}"
            cloudClipboard: "{{ cloudClipboard }}"
            cloudPCs:
              - id: "{{ id }}"
                aadDeviceId: "{{ aadDeviceId }}"
                displayName: "{{ displayName }}"
                gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
                imageDisplayName: "{{ imageDisplayName }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                managedDeviceId: "{{ managedDeviceId }}"
                managedDeviceName: "{{ managedDeviceName }}"
                onPremisesConnectionName: "{{ onPremisesConnectionName }}"
                provisioningPolicyId: "{{ provisioningPolicyId }}"
                provisioningPolicyName: "{{ provisioningPolicyName }}"
                provisioningType: "{{ provisioningType }}"
                servicePlanId: "{{ servicePlanId }}"
                servicePlanName: "{{ servicePlanName }}"
                userPrincipalName: "{{ userPrincipalName }}"
            contactFolders:
              - id: "{{ id }}"
                displayName: "{{ displayName }}"
                parentFolderId: "{{ parentFolderId }}"
                childFolders: "{{ childFolders }}"
                contacts: "{{ contacts }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            contacts:
              - id: "{{ id }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                assistantName: "{{ assistantName }}"
                birthday: "{{ birthday }}"
                businessAddress: "{{ businessAddress }}"
                businessHomePage: "{{ businessHomePage }}"
                businessPhones: "{{ businessPhones }}"
                children: "{{ children }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                emailAddresses: "{{ emailAddresses }}"
                fileAs: "{{ fileAs }}"
                generation: "{{ generation }}"
                givenName: "{{ givenName }}"
                homeAddress: "{{ homeAddress }}"
                homePhones: "{{ homePhones }}"
                imAddresses: "{{ imAddresses }}"
                initials: "{{ initials }}"
                jobTitle: "{{ jobTitle }}"
                manager: "{{ manager }}"
                middleName: "{{ middleName }}"
                mobilePhone: "{{ mobilePhone }}"
                nickName: "{{ nickName }}"
                officeLocation: "{{ officeLocation }}"
                otherAddress: "{{ otherAddress }}"
                parentFolderId: "{{ parentFolderId }}"
                personalNotes: "{{ personalNotes }}"
                primaryEmailAddress: "{{ primaryEmailAddress }}"
                profession: "{{ profession }}"
                secondaryEmailAddress: "{{ secondaryEmailAddress }}"
                spouseName: "{{ spouseName }}"
                surname: "{{ surname }}"
                tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
                title: "{{ title }}"
                yomiCompanyName: "{{ yomiCompanyName }}"
                yomiGivenName: "{{ yomiGivenName }}"
                yomiSurname: "{{ yomiSurname }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                photo: "{{ photo }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            createdObjects:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
            dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
            deviceManagementTroubleshootingEvents:
              - id: "{{ id }}"
                correlationId: "{{ correlationId }}"
                eventDateTime: "{{ eventDateTime }}"
            directReports:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
            drive: "{{ drive }}"
            drives:
              - id: "{{ id }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                driveType: "{{ driveType }}"
                owner: "{{ owner }}"
                quota: "{{ quota }}"
                sharePointIds: "{{ sharePointIds }}"
                system: "{{ system }}"
                bundles: "{{ bundles }}"
                following: "{{ following }}"
                items: "{{ items }}"
                list: "{{ list }}"
                root: "{{ root }}"
                special: "{{ special }}"
            employeeExperience: "{{ employeeExperience }}"
            events:
              - id: "{{ id }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                allowNewTimeProposals: {{ allowNewTimeProposals }}
                attendees: "{{ attendees }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                cancelledOccurrences: "{{ cancelledOccurrences }}"
                end: "{{ end }}"
                hasAttachments: {{ hasAttachments }}
                hideAttendees: {{ hideAttendees }}
                iCalUId: "{{ iCalUId }}"
                importance: "{{ importance }}"
                isAllDay: {{ isAllDay }}
                isCancelled: {{ isCancelled }}
                isDraft: {{ isDraft }}
                isOnlineMeeting: {{ isOnlineMeeting }}
                isOrganizer: {{ isOrganizer }}
                isReminderOn: {{ isReminderOn }}
                location: "{{ location }}"
                locations: "{{ locations }}"
                onlineMeeting: "{{ onlineMeeting }}"
                onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                organizer: "{{ organizer }}"
                originalEndTimeZone: "{{ originalEndTimeZone }}"
                originalStart: "{{ originalStart }}"
                originalStartTimeZone: "{{ originalStartTimeZone }}"
                recurrence: "{{ recurrence }}"
                reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                responseRequested: {{ responseRequested }}
                responseStatus: "{{ responseStatus }}"
                sensitivity: "{{ sensitivity }}"
                seriesMasterId: "{{ seriesMasterId }}"
                showAs: "{{ showAs }}"
                start: "{{ start }}"
                subject: "{{ subject }}"
                transactionId: "{{ transactionId }}"
                type: "{{ type }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                calendar: "{{ calendar }}"
                exceptionOccurrences: "{{ exceptionOccurrences }}"
                extensions: "{{ extensions }}"
                instances: "{{ instances }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            extensions:
              - id: "{{ id }}"
            followedSites:
              - id: "{{ id }}"
                createdBy: "{{ createdBy }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                eTag: "{{ eTag }}"
                lastModifiedBy: "{{ lastModifiedBy }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                name: "{{ name }}"
                parentReference: "{{ parentReference }}"
                webUrl: "{{ webUrl }}"
                createdByUser: "{{ createdByUser }}"
                lastModifiedByUser: "{{ lastModifiedByUser }}"
                displayName: "{{ displayName }}"
                error: "{{ error }}"
                isPersonalSite: {{ isPersonalSite }}
                root: "{{ root }}"
                sharepointIds: "{{ sharepointIds }}"
                siteCollection: "{{ siteCollection }}"
                analytics: "{{ analytics }}"
                columns: "{{ columns }}"
                contentTypes: "{{ contentTypes }}"
                drive: "{{ drive }}"
                drives: "{{ drives }}"
                externalColumns: "{{ externalColumns }}"
                items: "{{ items }}"
                lists: "{{ lists }}"
                onenote: "{{ onenote }}"
                operations: "{{ operations }}"
                pages: "{{ pages }}"
                permissions: "{{ permissions }}"
                sites: "{{ sites }}"
                termStore: "{{ termStore }}"
                termStores: "{{ termStores }}"
            inferenceClassification: "{{ inferenceClassification }}"
            insights: "{{ insights }}"
            joinedTeams:
              - id: "{{ id }}"
                classification: "{{ classification }}"
                createdDateTime: "{{ createdDateTime }}"
                description: "{{ description }}"
                displayName: "{{ displayName }}"
                firstChannelName: "{{ firstChannelName }}"
                funSettings: "{{ funSettings }}"
                guestSettings: "{{ guestSettings }}"
                internalId: "{{ internalId }}"
                isArchived: {{ isArchived }}
                memberSettings: "{{ memberSettings }}"
                messagingSettings: "{{ messagingSettings }}"
                specialization: "{{ specialization }}"
                summary: "{{ summary }}"
                tenantId: "{{ tenantId }}"
                visibility: "{{ visibility }}"
                webUrl: "{{ webUrl }}"
                allChannels: "{{ allChannels }}"
                channels: "{{ channels }}"
                group: "{{ group }}"
                incomingChannels: "{{ incomingChannels }}"
                installedApps: "{{ installedApps }}"
                members: "{{ members }}"
                operations: "{{ operations }}"
                permissionGrants: "{{ permissionGrants }}"
                photo: "{{ photo }}"
                primaryChannel: "{{ primaryChannel }}"
                schedule: "{{ schedule }}"
                tags: "{{ tags }}"
                template: "{{ template }}"
            licenseDetails:
              - id: "{{ id }}"
                servicePlans: "{{ servicePlans }}"
                skuId: "{{ skuId }}"
                skuPartNumber: "{{ skuPartNumber }}"
            mailFolders:
              - id: "{{ id }}"
                childFolderCount: {{ childFolderCount }}
                displayName: "{{ displayName }}"
                isHidden: {{ isHidden }}
                parentFolderId: "{{ parentFolderId }}"
                totalItemCount: {{ totalItemCount }}
                unreadItemCount: {{ unreadItemCount }}
                childFolders: "{{ childFolders }}"
                messageRules: "{{ messageRules }}"
                messages: "{{ messages }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            managedAppRegistrations:
              - id: "{{ id }}"
                appIdentifier: "{{ appIdentifier }}"
                applicationVersion: "{{ applicationVersion }}"
                createdDateTime: "{{ createdDateTime }}"
                deviceName: "{{ deviceName }}"
                deviceTag: "{{ deviceTag }}"
                deviceType: "{{ deviceType }}"
                flaggedReasons: "{{ flaggedReasons }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managementSdkVersion: "{{ managementSdkVersion }}"
                platformVersion: "{{ platformVersion }}"
                userId: "{{ userId }}"
                version: "{{ version }}"
                appliedPolicies: "{{ appliedPolicies }}"
                intendedPolicies: "{{ intendedPolicies }}"
                operations: "{{ operations }}"
            managedDevices:
              - id: "{{ id }}"
                activationLockBypassCode: "{{ activationLockBypassCode }}"
                androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
                azureADDeviceId: "{{ azureADDeviceId }}"
                azureADRegistered: {{ azureADRegistered }}
                complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
                complianceState: "{{ complianceState }}"
                configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
                deviceActionResults: "{{ deviceActionResults }}"
                deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
                deviceEnrollmentType: "{{ deviceEnrollmentType }}"
                deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
                deviceName: "{{ deviceName }}"
                deviceRegistrationState: "{{ deviceRegistrationState }}"
                easActivated: {{ easActivated }}
                easActivationDateTime: "{{ easActivationDateTime }}"
                easDeviceId: "{{ easDeviceId }}"
                emailAddress: "{{ emailAddress }}"
                enrolledDateTime: "{{ enrolledDateTime }}"
                enrollmentProfileName: "{{ enrollmentProfileName }}"
                ethernetMacAddress: "{{ ethernetMacAddress }}"
                exchangeAccessState: "{{ exchangeAccessState }}"
                exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
                exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
                freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
                iccid: "{{ iccid }}"
                imei: "{{ imei }}"
                isEncrypted: {{ isEncrypted }}
                isSupervised: {{ isSupervised }}
                jailBroken: "{{ jailBroken }}"
                lastSyncDateTime: "{{ lastSyncDateTime }}"
                managedDeviceName: "{{ managedDeviceName }}"
                managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
                managementAgent: "{{ managementAgent }}"
                managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
                managementState: "{{ managementState }}"
                manufacturer: "{{ manufacturer }}"
                meid: "{{ meid }}"
                model: "{{ model }}"
                notes: "{{ notes }}"
                operatingSystem: "{{ operatingSystem }}"
                osVersion: "{{ osVersion }}"
                partnerReportedThreatState: "{{ partnerReportedThreatState }}"
                phoneNumber: "{{ phoneNumber }}"
                physicalMemoryInBytes: {{ physicalMemoryInBytes }}
                remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
                remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
                requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
                serialNumber: "{{ serialNumber }}"
                subscriberCarrier: "{{ subscriberCarrier }}"
                totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
                udid: "{{ udid }}"
                userDisplayName: "{{ userDisplayName }}"
                userId: "{{ userId }}"
                userPrincipalName: "{{ userPrincipalName }}"
                wiFiMacAddress: "{{ wiFiMacAddress }}"
                deviceCategory: "{{ deviceCategory }}"
                deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
                deviceConfigurationStates: "{{ deviceConfigurationStates }}"
                logCollectionRequests: "{{ logCollectionRequests }}"
                users: "{{ users }}"
                windowsProtectionState: "{{ windowsProtectionState }}"
            manager: "{{ manager }}"
            memberOf:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
            messages:
              - id: "{{ id }}"
                categories: "{{ categories }}"
                changeKey: "{{ changeKey }}"
                createdDateTime: "{{ createdDateTime }}"
                lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                bccRecipients: "{{ bccRecipients }}"
                body: "{{ body }}"
                bodyPreview: "{{ bodyPreview }}"
                ccRecipients: "{{ ccRecipients }}"
                conversationId: "{{ conversationId }}"
                conversationIndex: "{{ conversationIndex }}"
                flag: "{{ flag }}"
                from: "{{ from }}"
                hasAttachments: {{ hasAttachments }}
                importance: "{{ importance }}"
                inferenceClassification: "{{ inferenceClassification }}"
                internetMessageHeaders: "{{ internetMessageHeaders }}"
                internetMessageId: "{{ internetMessageId }}"
                isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
                isDraft: {{ isDraft }}
                isRead: {{ isRead }}
                isReadReceiptRequested: {{ isReadReceiptRequested }}
                parentFolderId: "{{ parentFolderId }}"
                receivedDateTime: "{{ receivedDateTime }}"
                replyTo: "{{ replyTo }}"
                sender: "{{ sender }}"
                sentDateTime: "{{ sentDateTime }}"
                subject: "{{ subject }}"
                toRecipients: "{{ toRecipients }}"
                uniqueBody: "{{ uniqueBody }}"
                webLink: "{{ webLink }}"
                attachments: "{{ attachments }}"
                extensions: "{{ extensions }}"
                multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
            oauth2PermissionGrants:
              - id: "{{ id }}"
                clientId: "{{ clientId }}"
                consentType: "{{ consentType }}"
                principalId: "{{ principalId }}"
                resourceId: "{{ resourceId }}"
                scope: "{{ scope }}"
            onenote: "{{ onenote }}"
            onlineMeetings:
              - id: "{{ id }}"
                allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
                allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
                allowBreakoutRooms: {{ allowBreakoutRooms }}
                allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
                allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
                allowedPresenters: "{{ allowedPresenters }}"
                allowLiveShare: "{{ allowLiveShare }}"
                allowMeetingChat: "{{ allowMeetingChat }}"
                allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
                allowPowerPointSharing: {{ allowPowerPointSharing }}
                allowRecording: {{ allowRecording }}
                allowTeamworkReactions: {{ allowTeamworkReactions }}
                allowTranscription: {{ allowTranscription }}
                allowWhiteboard: {{ allowWhiteboard }}
                audioConferencing: "{{ audioConferencing }}"
                chatInfo: "{{ chatInfo }}"
                chatRestrictions: "{{ chatRestrictions }}"
                expiryDateTime: "{{ expiryDateTime }}"
                isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
                isEntryExitAnnounced: {{ isEntryExitAnnounced }}
                joinInformation: "{{ joinInformation }}"
                joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
                joinWebUrl: "{{ joinWebUrl }}"
                lobbyBypassSettings: "{{ lobbyBypassSettings }}"
                meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
                meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
                recordAutomatically: {{ recordAutomatically }}
                sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
                shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
                subject: "{{ subject }}"
                videoTeleconferenceId: "{{ videoTeleconferenceId }}"
                watermarkProtection: "{{ watermarkProtection }}"
                attendanceReports: "{{ attendanceReports }}"
                attendeeReport: "{{ attendeeReport }}"
                broadcastSettings: "{{ broadcastSettings }}"
                creationDateTime: "{{ creationDateTime }}"
                endDateTime: "{{ endDateTime }}"
                externalId: "{{ externalId }}"
                isBroadcast: {{ isBroadcast }}
                meetingTemplateId: "{{ meetingTemplateId }}"
                participants: "{{ participants }}"
                startDateTime: "{{ startDateTime }}"
                recordings: "{{ recordings }}"
                transcripts: "{{ transcripts }}"
            onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
            outlook: "{{ outlook }}"
            ownedDevices:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
            ownedObjects:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
            people:
              - id: "{{ id }}"
                birthday: "{{ birthday }}"
                companyName: "{{ companyName }}"
                department: "{{ department }}"
                displayName: "{{ displayName }}"
                givenName: "{{ givenName }}"
                imAddress: "{{ imAddress }}"
                isFavorite: {{ isFavorite }}
                jobTitle: "{{ jobTitle }}"
                officeLocation: "{{ officeLocation }}"
                personNotes: "{{ personNotes }}"
                personType: "{{ personType }}"
                phones: "{{ phones }}"
                postalAddresses: "{{ postalAddresses }}"
                profession: "{{ profession }}"
                scoredEmailAddresses: "{{ scoredEmailAddresses }}"
                surname: "{{ surname }}"
                userPrincipalName: "{{ userPrincipalName }}"
                websites: "{{ websites }}"
                yomiCompany: "{{ yomiCompany }}"
            permissionGrants:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
                clientAppId: "{{ clientAppId }}"
                clientId: "{{ clientId }}"
                permission: "{{ permission }}"
                permissionType: "{{ permissionType }}"
                resourceAppId: "{{ resourceAppId }}"
            photo: "{{ photo }}"
            photos:
              - id: "{{ id }}"
                height: {{ height }}
                width: {{ width }}
            planner: "{{ planner }}"
            presence: "{{ presence }}"
            registeredDevices:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
            scopedRoleMemberOf:
              - id: "{{ id }}"
                administrativeUnitId: "{{ administrativeUnitId }}"
                roleId: "{{ roleId }}"
                roleMemberInfo:
                  displayName: "{{ displayName }}"
                  id: "{{ id }}"
            settings: "{{ settings }}"
            solutions: "{{ solutions }}"
            sponsors:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
            teamwork: "{{ teamwork }}"
            todo: "{{ todo }}"
            transitiveMemberOf:
              - id: "{{ id }}"
                deletedDateTime: "{{ deletedDateTime }}"
          task:
            id: "{{ id }}"
            arguments:
              - name: "{{ name }}"
                value: "{{ value }}"
            category: "{{ category }}"
            continueOnError: {{ continueOnError }}
            description: "{{ description }}"
            displayName: "{{ displayName }}"
            executionSequence: {{ executionSequence }}
            isEnabled: {{ isEnabled }}
            taskDefinitionId: "{{ taskDefinitionId }}"
            taskProcessingResults:
              - id: "{{ id }}"
                completedDateTime: "{{ completedDateTime }}"
                createdDateTime: "{{ createdDateTime }}"
                failureReason: "{{ failureReason }}"
                processingInfo: "{{ processingInfo }}"
                processingStatus: "{{ processingStatus }}"
                startedDateTime: "{{ startedDateTime }}"
                subject:
                  id: "{{ id }}"
                  deletedDateTime: "{{ deletedDateTime }}"
                  aboutMe: "{{ aboutMe }}"
                  accountEnabled: {{ accountEnabled }}
                  ageGroup: "{{ ageGroup }}"
                  assignedLicenses:
                    - disabledPlans: "{{ disabledPlans }}"
                      skuId: "{{ skuId }}"
                  assignedPlans:
                    - assignedDateTime: "{{ assignedDateTime }}"
                      capabilityStatus: "{{ capabilityStatus }}"
                      service: "{{ service }}"
                      servicePlanId: "{{ servicePlanId }}"
                  authorizationInfo: "{{ authorizationInfo }}"
                  birthday: "{{ birthday }}"
                  businessPhones:
                    - "{{ businessPhones }}"
                  city: "{{ city }}"
                  companyName: "{{ companyName }}"
                  consentProvidedForMinor: "{{ consentProvidedForMinor }}"
                  country: "{{ country }}"
                  createdDateTime: "{{ createdDateTime }}"
                  creationType: "{{ creationType }}"
                  customSecurityAttributes: "{{ customSecurityAttributes }}"
                  department: "{{ department }}"
                  deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
                  displayName: "{{ displayName }}"
                  employeeHireDate: "{{ employeeHireDate }}"
                  employeeId: "{{ employeeId }}"
                  employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
                  employeeOrgData: "{{ employeeOrgData }}"
                  employeeType: "{{ employeeType }}"
                  externalUserState: "{{ externalUserState }}"
                  externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
                  faxNumber: "{{ faxNumber }}"
                  givenName: "{{ givenName }}"
                  hireDate: "{{ hireDate }}"
                  identities:
                    - issuer: "{{ issuer }}"
                      issuerAssignedId: "{{ issuerAssignedId }}"
                      signInType: "{{ signInType }}"
                  identityParentId: "{{ identityParentId }}"
                  imAddresses:
                    - "{{ imAddresses }}"
                  interests:
                    - "{{ interests }}"
                  isManagementRestricted: {{ isManagementRestricted }}
                  isResourceAccount: {{ isResourceAccount }}
                  jobTitle: "{{ jobTitle }}"
                  lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
                  legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
                  licenseAssignmentStates:
                    - assignedByGroup: "{{ assignedByGroup }}"
                      disabledPlans: "{{ disabledPlans }}"
                      error: "{{ error }}"
                      lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                      skuId: "{{ skuId }}"
                      state: "{{ state }}"
                  mail: "{{ mail }}"
                  mailboxSettings: "{{ mailboxSettings }}"
                  mailNickname: "{{ mailNickname }}"
                  mobilePhone: "{{ mobilePhone }}"
                  mySite: "{{ mySite }}"
                  officeLocation: "{{ officeLocation }}"
                  onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
                  onPremisesDomainName: "{{ onPremisesDomainName }}"
                  onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
                  onPremisesImmutableId: "{{ onPremisesImmutableId }}"
                  onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
                  onPremisesProvisioningErrors:
                    - category: "{{ category }}"
                      occurredDateTime: "{{ occurredDateTime }}"
                      propertyCausingError: "{{ propertyCausingError }}"
                      value: "{{ value }}"
                  onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
                  onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
                  onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
                  onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
                  otherMails:
                    - "{{ otherMails }}"
                  passwordPolicies: "{{ passwordPolicies }}"
                  passwordProfile: "{{ passwordProfile }}"
                  pastProjects:
                    - "{{ pastProjects }}"
                  postalCode: "{{ postalCode }}"
                  preferredDataLocation: "{{ preferredDataLocation }}"
                  preferredLanguage: "{{ preferredLanguage }}"
                  preferredName: "{{ preferredName }}"
                  print: "{{ print }}"
                  provisionedPlans:
                    - capabilityStatus: "{{ capabilityStatus }}"
                      provisioningStatus: "{{ provisioningStatus }}"
                      service: "{{ service }}"
                  proxyAddresses:
                    - "{{ proxyAddresses }}"
                  responsibilities:
                    - "{{ responsibilities }}"
                  schools:
                    - "{{ schools }}"
                  securityIdentifier: "{{ securityIdentifier }}"
                  serviceProvisioningErrors:
                    - createdDateTime: "{{ createdDateTime }}"
                      isResolved: {{ isResolved }}
                      serviceInstance: "{{ serviceInstance }}"
                  showInAddressList: {{ showInAddressList }}
                  signInActivity: "{{ signInActivity }}"
                  signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
                  skills:
                    - "{{ skills }}"
                  state: "{{ state }}"
                  streetAddress: "{{ streetAddress }}"
                  surname: "{{ surname }}"
                  usageLocation: "{{ usageLocation }}"
                  userPrincipalName: "{{ userPrincipalName }}"
                  userType: "{{ userType }}"
                  activities:
                    - id: "{{ id }}"
                      activationUrl: "{{ activationUrl }}"
                      activitySourceHost: "{{ activitySourceHost }}"
                      appActivityId: "{{ appActivityId }}"
                      appDisplayName: "{{ appDisplayName }}"
                      contentInfo: "{{ contentInfo }}"
                      contentUrl: "{{ contentUrl }}"
                      createdDateTime: "{{ createdDateTime }}"
                      expirationDateTime: "{{ expirationDateTime }}"
                      fallbackUrl: "{{ fallbackUrl }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      status: "{{ status }}"
                      userTimezone: "{{ userTimezone }}"
                      visualElements:
                        attribution: "{{ attribution }}"
                        backgroundColor: "{{ backgroundColor }}"
                        content: "{{ content }}"
                        description: "{{ description }}"
                        displayText: "{{ displayText }}"
                      historyItems: "{{ historyItems }}"
                  adhocCalls:
                    - id: "{{ id }}"
                      recordings: "{{ recordings }}"
                      transcripts: "{{ transcripts }}"
                  agreementAcceptances:
                    - id: "{{ id }}"
                      agreementFileId: "{{ agreementFileId }}"
                      agreementId: "{{ agreementId }}"
                      deviceDisplayName: "{{ deviceDisplayName }}"
                      deviceId: "{{ deviceId }}"
                      deviceOSType: "{{ deviceOSType }}"
                      deviceOSVersion: "{{ deviceOSVersion }}"
                      expirationDateTime: "{{ expirationDateTime }}"
                      recordedDateTime: "{{ recordedDateTime }}"
                      state: "{{ state }}"
                      userDisplayName: "{{ userDisplayName }}"
                      userEmail: "{{ userEmail }}"
                      userId: "{{ userId }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                  appRoleAssignments:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                      appRoleId: "{{ appRoleId }}"
                      createdDateTime: "{{ createdDateTime }}"
                      principalDisplayName: "{{ principalDisplayName }}"
                      principalId: "{{ principalId }}"
                      principalType: "{{ principalType }}"
                      resourceDisplayName: "{{ resourceDisplayName }}"
                      resourceId: "{{ resourceId }}"
                  authentication: "{{ authentication }}"
                  calendar: "{{ calendar }}"
                  calendarGroups:
                    - id: "{{ id }}"
                      changeKey: "{{ changeKey }}"
                      classId: "{{ classId }}"
                      name: "{{ name }}"
                      calendars: "{{ calendars }}"
                  calendars:
                    - id: "{{ id }}"
                      allowedOnlineMeetingProviders: "{{ allowedOnlineMeetingProviders }}"
                      canEdit: {{ canEdit }}
                      canShare: {{ canShare }}
                      canViewPrivateItems: {{ canViewPrivateItems }}
                      changeKey: "{{ changeKey }}"
                      color: "{{ color }}"
                      defaultOnlineMeetingProvider: "{{ defaultOnlineMeetingProvider }}"
                      hexColor: "{{ hexColor }}"
                      isDefaultCalendar: {{ isDefaultCalendar }}
                      isRemovable: {{ isRemovable }}
                      isTallyingResponses: {{ isTallyingResponses }}
                      name: "{{ name }}"
                      owner: "{{ owner }}"
                      calendarPermissions: "{{ calendarPermissions }}"
                      calendarView: "{{ calendarView }}"
                      events: "{{ events }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  calendarView:
                    - id: "{{ id }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      allowNewTimeProposals: {{ allowNewTimeProposals }}
                      attendees: "{{ attendees }}"
                      body: "{{ body }}"
                      bodyPreview: "{{ bodyPreview }}"
                      cancelledOccurrences: "{{ cancelledOccurrences }}"
                      end: "{{ end }}"
                      hasAttachments: {{ hasAttachments }}
                      hideAttendees: {{ hideAttendees }}
                      iCalUId: "{{ iCalUId }}"
                      importance: "{{ importance }}"
                      isAllDay: {{ isAllDay }}
                      isCancelled: {{ isCancelled }}
                      isDraft: {{ isDraft }}
                      isOnlineMeeting: {{ isOnlineMeeting }}
                      isOrganizer: {{ isOrganizer }}
                      isReminderOn: {{ isReminderOn }}
                      location: "{{ location }}"
                      locations: "{{ locations }}"
                      onlineMeeting: "{{ onlineMeeting }}"
                      onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                      onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                      organizer: "{{ organizer }}"
                      originalEndTimeZone: "{{ originalEndTimeZone }}"
                      originalStart: "{{ originalStart }}"
                      originalStartTimeZone: "{{ originalStartTimeZone }}"
                      recurrence: "{{ recurrence }}"
                      reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                      responseRequested: {{ responseRequested }}
                      responseStatus: "{{ responseStatus }}"
                      sensitivity: "{{ sensitivity }}"
                      seriesMasterId: "{{ seriesMasterId }}"
                      showAs: "{{ showAs }}"
                      start: "{{ start }}"
                      subject: "{{ subject }}"
                      transactionId: "{{ transactionId }}"
                      type: "{{ type }}"
                      webLink: "{{ webLink }}"
                      attachments: "{{ attachments }}"
                      calendar: "{{ calendar }}"
                      exceptionOccurrences: "{{ exceptionOccurrences }}"
                      extensions: "{{ extensions }}"
                      instances: "{{ instances }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  chats:
                    - id: "{{ id }}"
                      chatType: "{{ chatType }}"
                      createdDateTime: "{{ createdDateTime }}"
                      isHiddenForAllMembers: {{ isHiddenForAllMembers }}
                      lastUpdatedDateTime: "{{ lastUpdatedDateTime }}"
                      migrationMode: "{{ migrationMode }}"
                      onlineMeetingInfo: "{{ onlineMeetingInfo }}"
                      originalCreatedDateTime: "{{ originalCreatedDateTime }}"
                      tenantId: "{{ tenantId }}"
                      topic: "{{ topic }}"
                      viewpoint: "{{ viewpoint }}"
                      webUrl: "{{ webUrl }}"
                      installedApps: "{{ installedApps }}"
                      lastMessagePreview: "{{ lastMessagePreview }}"
                      members: "{{ members }}"
                      messages: "{{ messages }}"
                      permissionGrants: "{{ permissionGrants }}"
                      pinnedMessages: "{{ pinnedMessages }}"
                      tabs: "{{ tabs }}"
                  cloudClipboard: "{{ cloudClipboard }}"
                  cloudPCs:
                    - id: "{{ id }}"
                      aadDeviceId: "{{ aadDeviceId }}"
                      displayName: "{{ displayName }}"
                      gracePeriodEndDateTime: "{{ gracePeriodEndDateTime }}"
                      imageDisplayName: "{{ imageDisplayName }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      managedDeviceId: "{{ managedDeviceId }}"
                      managedDeviceName: "{{ managedDeviceName }}"
                      onPremisesConnectionName: "{{ onPremisesConnectionName }}"
                      provisioningPolicyId: "{{ provisioningPolicyId }}"
                      provisioningPolicyName: "{{ provisioningPolicyName }}"
                      provisioningType: "{{ provisioningType }}"
                      servicePlanId: "{{ servicePlanId }}"
                      servicePlanName: "{{ servicePlanName }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                  contactFolders:
                    - id: "{{ id }}"
                      displayName: "{{ displayName }}"
                      parentFolderId: "{{ parentFolderId }}"
                      childFolders: "{{ childFolders }}"
                      contacts: "{{ contacts }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  contacts:
                    - id: "{{ id }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      assistantName: "{{ assistantName }}"
                      birthday: "{{ birthday }}"
                      businessAddress: "{{ businessAddress }}"
                      businessHomePage: "{{ businessHomePage }}"
                      businessPhones: "{{ businessPhones }}"
                      children: "{{ children }}"
                      companyName: "{{ companyName }}"
                      department: "{{ department }}"
                      displayName: "{{ displayName }}"
                      emailAddresses: "{{ emailAddresses }}"
                      fileAs: "{{ fileAs }}"
                      generation: "{{ generation }}"
                      givenName: "{{ givenName }}"
                      homeAddress: "{{ homeAddress }}"
                      homePhones: "{{ homePhones }}"
                      imAddresses: "{{ imAddresses }}"
                      initials: "{{ initials }}"
                      jobTitle: "{{ jobTitle }}"
                      manager: "{{ manager }}"
                      middleName: "{{ middleName }}"
                      mobilePhone: "{{ mobilePhone }}"
                      nickName: "{{ nickName }}"
                      officeLocation: "{{ officeLocation }}"
                      otherAddress: "{{ otherAddress }}"
                      parentFolderId: "{{ parentFolderId }}"
                      personalNotes: "{{ personalNotes }}"
                      primaryEmailAddress: "{{ primaryEmailAddress }}"
                      profession: "{{ profession }}"
                      secondaryEmailAddress: "{{ secondaryEmailAddress }}"
                      spouseName: "{{ spouseName }}"
                      surname: "{{ surname }}"
                      tertiaryEmailAddress: "{{ tertiaryEmailAddress }}"
                      title: "{{ title }}"
                      yomiCompanyName: "{{ yomiCompanyName }}"
                      yomiGivenName: "{{ yomiGivenName }}"
                      yomiSurname: "{{ yomiSurname }}"
                      extensions: "{{ extensions }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      photo: "{{ photo }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  createdObjects:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
                  deviceManagementTroubleshootingEvents:
                    - id: "{{ id }}"
                      correlationId: "{{ correlationId }}"
                      eventDateTime: "{{ eventDateTime }}"
                  directReports:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  drive: "{{ drive }}"
                  drives:
                    - id: "{{ id }}"
                      createdBy: "{{ createdBy }}"
                      createdDateTime: "{{ createdDateTime }}"
                      description: "{{ description }}"
                      eTag: "{{ eTag }}"
                      lastModifiedBy: "{{ lastModifiedBy }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      name: "{{ name }}"
                      parentReference: "{{ parentReference }}"
                      webUrl: "{{ webUrl }}"
                      createdByUser: "{{ createdByUser }}"
                      lastModifiedByUser: "{{ lastModifiedByUser }}"
                      driveType: "{{ driveType }}"
                      owner: "{{ owner }}"
                      quota: "{{ quota }}"
                      sharePointIds: "{{ sharePointIds }}"
                      system: "{{ system }}"
                      bundles: "{{ bundles }}"
                      following: "{{ following }}"
                      items: "{{ items }}"
                      list: "{{ list }}"
                      root: "{{ root }}"
                      special: "{{ special }}"
                  employeeExperience: "{{ employeeExperience }}"
                  events:
                    - id: "{{ id }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      allowNewTimeProposals: {{ allowNewTimeProposals }}
                      attendees: "{{ attendees }}"
                      body: "{{ body }}"
                      bodyPreview: "{{ bodyPreview }}"
                      cancelledOccurrences: "{{ cancelledOccurrences }}"
                      end: "{{ end }}"
                      hasAttachments: {{ hasAttachments }}
                      hideAttendees: {{ hideAttendees }}
                      iCalUId: "{{ iCalUId }}"
                      importance: "{{ importance }}"
                      isAllDay: {{ isAllDay }}
                      isCancelled: {{ isCancelled }}
                      isDraft: {{ isDraft }}
                      isOnlineMeeting: {{ isOnlineMeeting }}
                      isOrganizer: {{ isOrganizer }}
                      isReminderOn: {{ isReminderOn }}
                      location: "{{ location }}"
                      locations: "{{ locations }}"
                      onlineMeeting: "{{ onlineMeeting }}"
                      onlineMeetingProvider: "{{ onlineMeetingProvider }}"
                      onlineMeetingUrl: "{{ onlineMeetingUrl }}"
                      organizer: "{{ organizer }}"
                      originalEndTimeZone: "{{ originalEndTimeZone }}"
                      originalStart: "{{ originalStart }}"
                      originalStartTimeZone: "{{ originalStartTimeZone }}"
                      recurrence: "{{ recurrence }}"
                      reminderMinutesBeforeStart: {{ reminderMinutesBeforeStart }}
                      responseRequested: {{ responseRequested }}
                      responseStatus: "{{ responseStatus }}"
                      sensitivity: "{{ sensitivity }}"
                      seriesMasterId: "{{ seriesMasterId }}"
                      showAs: "{{ showAs }}"
                      start: "{{ start }}"
                      subject: "{{ subject }}"
                      transactionId: "{{ transactionId }}"
                      type: "{{ type }}"
                      webLink: "{{ webLink }}"
                      attachments: "{{ attachments }}"
                      calendar: "{{ calendar }}"
                      exceptionOccurrences: "{{ exceptionOccurrences }}"
                      extensions: "{{ extensions }}"
                      instances: "{{ instances }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  extensions:
                    - id: "{{ id }}"
                  followedSites:
                    - id: "{{ id }}"
                      createdBy: "{{ createdBy }}"
                      createdDateTime: "{{ createdDateTime }}"
                      description: "{{ description }}"
                      eTag: "{{ eTag }}"
                      lastModifiedBy: "{{ lastModifiedBy }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      name: "{{ name }}"
                      parentReference: "{{ parentReference }}"
                      webUrl: "{{ webUrl }}"
                      createdByUser: "{{ createdByUser }}"
                      lastModifiedByUser: "{{ lastModifiedByUser }}"
                      displayName: "{{ displayName }}"
                      error: "{{ error }}"
                      isPersonalSite: {{ isPersonalSite }}
                      root: "{{ root }}"
                      sharepointIds: "{{ sharepointIds }}"
                      siteCollection: "{{ siteCollection }}"
                      analytics: "{{ analytics }}"
                      columns: "{{ columns }}"
                      contentTypes: "{{ contentTypes }}"
                      drive: "{{ drive }}"
                      drives: "{{ drives }}"
                      externalColumns: "{{ externalColumns }}"
                      items: "{{ items }}"
                      lists: "{{ lists }}"
                      onenote: "{{ onenote }}"
                      operations: "{{ operations }}"
                      pages: "{{ pages }}"
                      permissions: "{{ permissions }}"
                      sites: "{{ sites }}"
                      termStore: "{{ termStore }}"
                      termStores: "{{ termStores }}"
                  inferenceClassification: "{{ inferenceClassification }}"
                  insights: "{{ insights }}"
                  joinedTeams:
                    - id: "{{ id }}"
                      classification: "{{ classification }}"
                      createdDateTime: "{{ createdDateTime }}"
                      description: "{{ description }}"
                      displayName: "{{ displayName }}"
                      firstChannelName: "{{ firstChannelName }}"
                      funSettings: "{{ funSettings }}"
                      guestSettings: "{{ guestSettings }}"
                      internalId: "{{ internalId }}"
                      isArchived: {{ isArchived }}
                      memberSettings: "{{ memberSettings }}"
                      messagingSettings: "{{ messagingSettings }}"
                      specialization: "{{ specialization }}"
                      summary: "{{ summary }}"
                      tenantId: "{{ tenantId }}"
                      visibility: "{{ visibility }}"
                      webUrl: "{{ webUrl }}"
                      allChannels: "{{ allChannels }}"
                      channels: "{{ channels }}"
                      group: "{{ group }}"
                      incomingChannels: "{{ incomingChannels }}"
                      installedApps: "{{ installedApps }}"
                      members: "{{ members }}"
                      operations: "{{ operations }}"
                      permissionGrants: "{{ permissionGrants }}"
                      photo: "{{ photo }}"
                      primaryChannel: "{{ primaryChannel }}"
                      schedule: "{{ schedule }}"
                      tags: "{{ tags }}"
                      template: "{{ template }}"
                  licenseDetails:
                    - id: "{{ id }}"
                      servicePlans: "{{ servicePlans }}"
                      skuId: "{{ skuId }}"
                      skuPartNumber: "{{ skuPartNumber }}"
                  mailFolders:
                    - id: "{{ id }}"
                      childFolderCount: {{ childFolderCount }}
                      displayName: "{{ displayName }}"
                      isHidden: {{ isHidden }}
                      parentFolderId: "{{ parentFolderId }}"
                      totalItemCount: {{ totalItemCount }}
                      unreadItemCount: {{ unreadItemCount }}
                      childFolders: "{{ childFolders }}"
                      messageRules: "{{ messageRules }}"
                      messages: "{{ messages }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  managedAppRegistrations:
                    - id: "{{ id }}"
                      appIdentifier: "{{ appIdentifier }}"
                      applicationVersion: "{{ applicationVersion }}"
                      createdDateTime: "{{ createdDateTime }}"
                      deviceName: "{{ deviceName }}"
                      deviceTag: "{{ deviceTag }}"
                      deviceType: "{{ deviceType }}"
                      flaggedReasons: "{{ flaggedReasons }}"
                      lastSyncDateTime: "{{ lastSyncDateTime }}"
                      managementSdkVersion: "{{ managementSdkVersion }}"
                      platformVersion: "{{ platformVersion }}"
                      userId: "{{ userId }}"
                      version: "{{ version }}"
                      appliedPolicies: "{{ appliedPolicies }}"
                      intendedPolicies: "{{ intendedPolicies }}"
                      operations: "{{ operations }}"
                  managedDevices:
                    - id: "{{ id }}"
                      activationLockBypassCode: "{{ activationLockBypassCode }}"
                      androidSecurityPatchLevel: "{{ androidSecurityPatchLevel }}"
                      azureADDeviceId: "{{ azureADDeviceId }}"
                      azureADRegistered: {{ azureADRegistered }}
                      complianceGracePeriodExpirationDateTime: "{{ complianceGracePeriodExpirationDateTime }}"
                      complianceState: "{{ complianceState }}"
                      configurationManagerClientEnabledFeatures: "{{ configurationManagerClientEnabledFeatures }}"
                      deviceActionResults: "{{ deviceActionResults }}"
                      deviceCategoryDisplayName: "{{ deviceCategoryDisplayName }}"
                      deviceEnrollmentType: "{{ deviceEnrollmentType }}"
                      deviceHealthAttestationState: "{{ deviceHealthAttestationState }}"
                      deviceName: "{{ deviceName }}"
                      deviceRegistrationState: "{{ deviceRegistrationState }}"
                      easActivated: {{ easActivated }}
                      easActivationDateTime: "{{ easActivationDateTime }}"
                      easDeviceId: "{{ easDeviceId }}"
                      emailAddress: "{{ emailAddress }}"
                      enrolledDateTime: "{{ enrolledDateTime }}"
                      enrollmentProfileName: "{{ enrollmentProfileName }}"
                      ethernetMacAddress: "{{ ethernetMacAddress }}"
                      exchangeAccessState: "{{ exchangeAccessState }}"
                      exchangeAccessStateReason: "{{ exchangeAccessStateReason }}"
                      exchangeLastSuccessfulSyncDateTime: "{{ exchangeLastSuccessfulSyncDateTime }}"
                      freeStorageSpaceInBytes: {{ freeStorageSpaceInBytes }}
                      iccid: "{{ iccid }}"
                      imei: "{{ imei }}"
                      isEncrypted: {{ isEncrypted }}
                      isSupervised: {{ isSupervised }}
                      jailBroken: "{{ jailBroken }}"
                      lastSyncDateTime: "{{ lastSyncDateTime }}"
                      managedDeviceName: "{{ managedDeviceName }}"
                      managedDeviceOwnerType: "{{ managedDeviceOwnerType }}"
                      managementAgent: "{{ managementAgent }}"
                      managementCertificateExpirationDate: "{{ managementCertificateExpirationDate }}"
                      managementState: "{{ managementState }}"
                      manufacturer: "{{ manufacturer }}"
                      meid: "{{ meid }}"
                      model: "{{ model }}"
                      notes: "{{ notes }}"
                      operatingSystem: "{{ operatingSystem }}"
                      osVersion: "{{ osVersion }}"
                      partnerReportedThreatState: "{{ partnerReportedThreatState }}"
                      phoneNumber: "{{ phoneNumber }}"
                      physicalMemoryInBytes: {{ physicalMemoryInBytes }}
                      remoteAssistanceSessionErrorDetails: "{{ remoteAssistanceSessionErrorDetails }}"
                      remoteAssistanceSessionUrl: "{{ remoteAssistanceSessionUrl }}"
                      requireUserEnrollmentApproval: {{ requireUserEnrollmentApproval }}
                      serialNumber: "{{ serialNumber }}"
                      subscriberCarrier: "{{ subscriberCarrier }}"
                      totalStorageSpaceInBytes: {{ totalStorageSpaceInBytes }}
                      udid: "{{ udid }}"
                      userDisplayName: "{{ userDisplayName }}"
                      userId: "{{ userId }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                      wiFiMacAddress: "{{ wiFiMacAddress }}"
                      deviceCategory: "{{ deviceCategory }}"
                      deviceCompliancePolicyStates: "{{ deviceCompliancePolicyStates }}"
                      deviceConfigurationStates: "{{ deviceConfigurationStates }}"
                      logCollectionRequests: "{{ logCollectionRequests }}"
                      users: "{{ users }}"
                      windowsProtectionState: "{{ windowsProtectionState }}"
                  manager: "{{ manager }}"
                  memberOf:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  messages:
                    - id: "{{ id }}"
                      categories: "{{ categories }}"
                      changeKey: "{{ changeKey }}"
                      createdDateTime: "{{ createdDateTime }}"
                      lastModifiedDateTime: "{{ lastModifiedDateTime }}"
                      bccRecipients: "{{ bccRecipients }}"
                      body: "{{ body }}"
                      bodyPreview: "{{ bodyPreview }}"
                      ccRecipients: "{{ ccRecipients }}"
                      conversationId: "{{ conversationId }}"
                      conversationIndex: "{{ conversationIndex }}"
                      flag: "{{ flag }}"
                      from: "{{ from }}"
                      hasAttachments: {{ hasAttachments }}
                      importance: "{{ importance }}"
                      inferenceClassification: "{{ inferenceClassification }}"
                      internetMessageHeaders: "{{ internetMessageHeaders }}"
                      internetMessageId: "{{ internetMessageId }}"
                      isDeliveryReceiptRequested: {{ isDeliveryReceiptRequested }}
                      isDraft: {{ isDraft }}
                      isRead: {{ isRead }}
                      isReadReceiptRequested: {{ isReadReceiptRequested }}
                      parentFolderId: "{{ parentFolderId }}"
                      receivedDateTime: "{{ receivedDateTime }}"
                      replyTo: "{{ replyTo }}"
                      sender: "{{ sender }}"
                      sentDateTime: "{{ sentDateTime }}"
                      subject: "{{ subject }}"
                      toRecipients: "{{ toRecipients }}"
                      uniqueBody: "{{ uniqueBody }}"
                      webLink: "{{ webLink }}"
                      attachments: "{{ attachments }}"
                      extensions: "{{ extensions }}"
                      multiValueExtendedProperties: "{{ multiValueExtendedProperties }}"
                      singleValueExtendedProperties: "{{ singleValueExtendedProperties }}"
                  oauth2PermissionGrants:
                    - id: "{{ id }}"
                      clientId: "{{ clientId }}"
                      consentType: "{{ consentType }}"
                      principalId: "{{ principalId }}"
                      resourceId: "{{ resourceId }}"
                      scope: "{{ scope }}"
                  onenote: "{{ onenote }}"
                  onlineMeetings:
                    - id: "{{ id }}"
                      allowAttendeeToEnableCamera: {{ allowAttendeeToEnableCamera }}
                      allowAttendeeToEnableMic: {{ allowAttendeeToEnableMic }}
                      allowBreakoutRooms: {{ allowBreakoutRooms }}
                      allowCopyingAndSharingMeetingContent: {{ allowCopyingAndSharingMeetingContent }}
                      allowedLobbyAdmitters: "{{ allowedLobbyAdmitters }}"
                      allowedPresenters: "{{ allowedPresenters }}"
                      allowLiveShare: "{{ allowLiveShare }}"
                      allowMeetingChat: "{{ allowMeetingChat }}"
                      allowParticipantsToChangeName: {{ allowParticipantsToChangeName }}
                      allowPowerPointSharing: {{ allowPowerPointSharing }}
                      allowRecording: {{ allowRecording }}
                      allowTeamworkReactions: {{ allowTeamworkReactions }}
                      allowTranscription: {{ allowTranscription }}
                      allowWhiteboard: {{ allowWhiteboard }}
                      audioConferencing: "{{ audioConferencing }}"
                      chatInfo: "{{ chatInfo }}"
                      chatRestrictions: "{{ chatRestrictions }}"
                      expiryDateTime: "{{ expiryDateTime }}"
                      isEndToEndEncryptionEnabled: {{ isEndToEndEncryptionEnabled }}
                      isEntryExitAnnounced: {{ isEntryExitAnnounced }}
                      joinInformation: "{{ joinInformation }}"
                      joinMeetingIdSettings: "{{ joinMeetingIdSettings }}"
                      joinWebUrl: "{{ joinWebUrl }}"
                      lobbyBypassSettings: "{{ lobbyBypassSettings }}"
                      meetingOptionsWebUrl: "{{ meetingOptionsWebUrl }}"
                      meetingSpokenLanguageTag: "{{ meetingSpokenLanguageTag }}"
                      recordAutomatically: {{ recordAutomatically }}
                      sensitivityLabelAssignment: "{{ sensitivityLabelAssignment }}"
                      shareMeetingChatHistoryDefault: "{{ shareMeetingChatHistoryDefault }}"
                      subject: "{{ subject }}"
                      videoTeleconferenceId: "{{ videoTeleconferenceId }}"
                      watermarkProtection: "{{ watermarkProtection }}"
                      attendanceReports: "{{ attendanceReports }}"
                      attendeeReport: "{{ attendeeReport }}"
                      broadcastSettings: "{{ broadcastSettings }}"
                      creationDateTime: "{{ creationDateTime }}"
                      endDateTime: "{{ endDateTime }}"
                      externalId: "{{ externalId }}"
                      isBroadcast: {{ isBroadcast }}
                      meetingTemplateId: "{{ meetingTemplateId }}"
                      participants: "{{ participants }}"
                      startDateTime: "{{ startDateTime }}"
                      recordings: "{{ recordings }}"
                      transcripts: "{{ transcripts }}"
                  onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
                  outlook: "{{ outlook }}"
                  ownedDevices:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  ownedObjects:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  people:
                    - id: "{{ id }}"
                      birthday: "{{ birthday }}"
                      companyName: "{{ companyName }}"
                      department: "{{ department }}"
                      displayName: "{{ displayName }}"
                      givenName: "{{ givenName }}"
                      imAddress: "{{ imAddress }}"
                      isFavorite: {{ isFavorite }}
                      jobTitle: "{{ jobTitle }}"
                      officeLocation: "{{ officeLocation }}"
                      personNotes: "{{ personNotes }}"
                      personType: "{{ personType }}"
                      phones: "{{ phones }}"
                      postalAddresses: "{{ postalAddresses }}"
                      profession: "{{ profession }}"
                      scoredEmailAddresses: "{{ scoredEmailAddresses }}"
                      surname: "{{ surname }}"
                      userPrincipalName: "{{ userPrincipalName }}"
                      websites: "{{ websites }}"
                      yomiCompany: "{{ yomiCompany }}"
                  permissionGrants:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                      clientAppId: "{{ clientAppId }}"
                      clientId: "{{ clientId }}"
                      permission: "{{ permission }}"
                      permissionType: "{{ permissionType }}"
                      resourceAppId: "{{ resourceAppId }}"
                  photo: "{{ photo }}"
                  photos:
                    - id: "{{ id }}"
                      height: {{ height }}
                      width: {{ width }}
                  planner: "{{ planner }}"
                  presence: "{{ presence }}"
                  registeredDevices:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  scopedRoleMemberOf:
                    - id: "{{ id }}"
                      administrativeUnitId: "{{ administrativeUnitId }}"
                      roleId: "{{ roleId }}"
                      roleMemberInfo:
                        displayName: "{{ displayName }}"
                        id: "{{ id }}"
                  settings: "{{ settings }}"
                  solutions: "{{ solutions }}"
                  sponsors:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                  teamwork: "{{ teamwork }}"
                  todo: "{{ todo }}"
                  transitiveMemberOf:
                    - id: "{{ id }}"
                      deletedDateTime: "{{ deletedDateTime }}"
                task:
                  id: "{{ id }}"
                  arguments:
                    - name: "{{ name }}"
                      value: "{{ value }}"
                  category: "{{ category }}"
                  continueOnError: {{ continueOnError }}
                  description: "{{ description }}"
                  displayName: "{{ displayName }}"
                  executionSequence: {{ executionSequence }}
                  isEnabled: {{ isEnabled }}
                  taskDefinitionId: "{{ taskDefinitionId }}"
                  taskProcessingResults:
                    - id: "{{ id }}"
                      completedDateTime: "{{ completedDateTime }}"
                      createdDateTime: "{{ createdDateTime }}"
                      failureReason: "{{ failureReason }}"
                      processingInfo: "{{ processingInfo }}"
                      processingStatus: "{{ processingStatus }}"
                      startedDateTime: "{{ startedDateTime }}"
                      subject:
                        id: "{{ id }}"
                        deletedDateTime: "{{ deletedDateTime }}"
                        aboutMe: "{{ aboutMe }}"
                        accountEnabled: {{ accountEnabled }}
                        ageGroup: "{{ ageGroup }}"
                        assignedLicenses: "{{ assignedLicenses }}"
                        assignedPlans: "{{ assignedPlans }}"
                        authorizationInfo: "{{ authorizationInfo }}"
                        birthday: "{{ birthday }}"
                        businessPhones: "{{ businessPhones }}"
                        city: "{{ city }}"
                        companyName: "{{ companyName }}"
                        consentProvidedForMinor: "{{ consentProvidedForMinor }}"
                        country: "{{ country }}"
                        createdDateTime: "{{ createdDateTime }}"
                        creationType: "{{ creationType }}"
                        customSecurityAttributes: "{{ customSecurityAttributes }}"
                        department: "{{ department }}"
                        deviceEnrollmentLimit: {{ deviceEnrollmentLimit }}
                        displayName: "{{ displayName }}"
                        employeeHireDate: "{{ employeeHireDate }}"
                        employeeId: "{{ employeeId }}"
                        employeeLeaveDateTime: "{{ employeeLeaveDateTime }}"
                        employeeOrgData: "{{ employeeOrgData }}"
                        employeeType: "{{ employeeType }}"
                        externalUserState: "{{ externalUserState }}"
                        externalUserStateChangeDateTime: "{{ externalUserStateChangeDateTime }}"
                        faxNumber: "{{ faxNumber }}"
                        givenName: "{{ givenName }}"
                        hireDate: "{{ hireDate }}"
                        identities: "{{ identities }}"
                        identityParentId: "{{ identityParentId }}"
                        imAddresses: "{{ imAddresses }}"
                        interests: "{{ interests }}"
                        isManagementRestricted: {{ isManagementRestricted }}
                        isResourceAccount: {{ isResourceAccount }}
                        jobTitle: "{{ jobTitle }}"
                        lastPasswordChangeDateTime: "{{ lastPasswordChangeDateTime }}"
                        legalAgeGroupClassification: "{{ legalAgeGroupClassification }}"
                        licenseAssignmentStates: "{{ licenseAssignmentStates }}"
                        mail: "{{ mail }}"
                        mailboxSettings: "{{ mailboxSettings }}"
                        mailNickname: "{{ mailNickname }}"
                        mobilePhone: "{{ mobilePhone }}"
                        mySite: "{{ mySite }}"
                        officeLocation: "{{ officeLocation }}"
                        onPremisesDistinguishedName: "{{ onPremisesDistinguishedName }}"
                        onPremisesDomainName: "{{ onPremisesDomainName }}"
                        onPremisesExtensionAttributes: "{{ onPremisesExtensionAttributes }}"
                        onPremisesImmutableId: "{{ onPremisesImmutableId }}"
                        onPremisesLastSyncDateTime: "{{ onPremisesLastSyncDateTime }}"
                        onPremisesProvisioningErrors: "{{ onPremisesProvisioningErrors }}"
                        onPremisesSamAccountName: "{{ onPremisesSamAccountName }}"
                        onPremisesSecurityIdentifier: "{{ onPremisesSecurityIdentifier }}"
                        onPremisesSyncEnabled: {{ onPremisesSyncEnabled }}
                        onPremisesUserPrincipalName: "{{ onPremisesUserPrincipalName }}"
                        otherMails: "{{ otherMails }}"
                        passwordPolicies: "{{ passwordPolicies }}"
                        passwordProfile: "{{ passwordProfile }}"
                        pastProjects: "{{ pastProjects }}"
                        postalCode: "{{ postalCode }}"
                        preferredDataLocation: "{{ preferredDataLocation }}"
                        preferredLanguage: "{{ preferredLanguage }}"
                        preferredName: "{{ preferredName }}"
                        print: "{{ print }}"
                        provisionedPlans: "{{ provisionedPlans }}"
                        proxyAddresses: "{{ proxyAddresses }}"
                        responsibilities: "{{ responsibilities }}"
                        schools: "{{ schools }}"
                        securityIdentifier: "{{ securityIdentifier }}"
                        serviceProvisioningErrors: "{{ serviceProvisioningErrors }}"
                        showInAddressList: {{ showInAddressList }}
                        signInActivity: "{{ signInActivity }}"
                        signInSessionsValidFromDateTime: "{{ signInSessionsValidFromDateTime }}"
                        skills: "{{ skills }}"
                        state: "{{ state }}"
                        streetAddress: "{{ streetAddress }}"
                        surname: "{{ surname }}"
                        usageLocation: "{{ usageLocation }}"
                        userPrincipalName: "{{ userPrincipalName }}"
                        userType: "{{ userType }}"
                        activities: "{{ activities }}"
                        adhocCalls: "{{ adhocCalls }}"
                        agreementAcceptances: "{{ agreementAcceptances }}"
                        appRoleAssignments: "{{ appRoleAssignments }}"
                        authentication: "{{ authentication }}"
                        calendar: "{{ calendar }}"
                        calendarGroups: "{{ calendarGroups }}"
                        calendars: "{{ calendars }}"
                        calendarView: "{{ calendarView }}"
                        chats: "{{ chats }}"
                        cloudClipboard: "{{ cloudClipboard }}"
                        cloudPCs: "{{ cloudPCs }}"
                        contactFolders: "{{ contactFolders }}"
                        contacts: "{{ contacts }}"
                        createdObjects: "{{ createdObjects }}"
                        dataSecurityAndGovernance: "{{ dataSecurityAndGovernance }}"
                        deviceManagementTroubleshootingEvents: "{{ deviceManagementTroubleshootingEvents }}"
                        directReports: "{{ directReports }}"
                        drive: "{{ drive }}"
                        drives: "{{ drives }}"
                        employeeExperience: "{{ employeeExperience }}"
                        events: "{{ events }}"
                        extensions: "{{ extensions }}"
                        followedSites: "{{ followedSites }}"
                        inferenceClassification: "{{ inferenceClassification }}"
                        insights: "{{ insights }}"
                        joinedTeams: "{{ joinedTeams }}"
                        licenseDetails: "{{ licenseDetails }}"
                        mailFolders: "{{ mailFolders }}"
                        managedAppRegistrations: "{{ managedAppRegistrations }}"
                        managedDevices: "{{ managedDevices }}"
                        manager: "{{ manager }}"
                        memberOf: "{{ memberOf }}"
                        messages: "{{ messages }}"
                        oauth2PermissionGrants: "{{ oauth2PermissionGrants }}"
                        onenote: "{{ onenote }}"
                        onlineMeetings: "{{ onlineMeetings }}"
                        onPremisesSyncBehavior: "{{ onPremisesSyncBehavior }}"
                        outlook: "{{ outlook }}"
                        ownedDevices: "{{ ownedDevices }}"
                        ownedObjects: "{{ ownedObjects }}"
                        people: "{{ people }}"
                        permissionGrants: "{{ permissionGrants }}"
                        photo: "{{ photo }}"
                        photos: "{{ photos }}"
                        planner: "{{ planner }}"
                        presence: "{{ presence }}"
                        registeredDevices: "{{ registeredDevices }}"
                        scopedRoleMemberOf: "{{ scopedRoleMemberOf }}"
                        settings: "{{ settings }}"
                        solutions: "{{ solutions }}"
                        sponsors: "{{ sponsors }}"
                        teamwork: "{{ teamwork }}"
                        todo: "{{ todo }}"
                        transitiveMemberOf: "{{ transitiveMemberOf }}"
                      task:
                        id: "{{ id }}"
                        arguments: "{{ arguments }}"
                        category: "{{ category }}"
                        continueOnError: {{ continueOnError }}
                        description: "{{ description }}"
                        displayName: "{{ displayName }}"
                        executionSequence: {{ executionSequence }}
                        isEnabled: {{ isEnabled }}
                        taskDefinitionId: "{{ taskDefinitionId }}"
                        taskProcessingResults: "{{ taskProcessingResults }}"
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
UPDATE entra_id.identity_governance.lifecycle_workflows_workflows_tasks
SET 
id = '{{ id }}',
arguments = '{{ arguments }}',
category = '{{ category }}',
continueOnError = {{ continueOnError }},
description = '{{ description }}',
displayName = '{{ displayName }}',
executionSequence = {{ executionSequence }},
isEnabled = {{ isEnabled }},
taskDefinitionId = '{{ taskDefinitionId }}',
taskProcessingResults = '{{ taskProcessingResults }}'
WHERE 
workflow_id = '{{ workflow_id }}' --required
AND task_id = '{{ task_id }}' --required
RETURNING
id,
arguments,
category,
continueOnError,
description,
displayName,
executionSequence,
isEnabled,
taskDefinitionId,
taskProcessingResults;
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
DELETE FROM entra_id.identity_governance.lifecycle_workflows_workflows_tasks
WHERE workflow_id = '{{ workflow_id }}' --required
AND task_id = '{{ task_id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
