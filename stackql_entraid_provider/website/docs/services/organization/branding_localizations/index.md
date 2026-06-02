--- 
title: branding_localizations
hide_title: false
hide_table_of_contents: false
keywords:
  - branding_localizations
  - organization
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

Creates, updates, deletes, gets or lists a <code>branding_localizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="branding_localizations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="entra_id.organization.branding_localizations" /></td></tr>
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
    <td><CopyableCode code="@odata.type" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="backgroundColor" /></td>
    <td><code>string</code></td>
    <td>Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.</td>
</tr>
<tr>
    <td><CopyableCode code="backgroundImage" /></td>
    <td><code>string (base64url)</code></td>
    <td>Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image reduces bandwidth requirements and make the page load faster.</td>
</tr>
<tr>
    <td><CopyableCode code="backgroundImageRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="bannerLogo" /></td>
    <td><code>string (base64url)</code></td>
    <td>A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="bannerLogoRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnList" /></td>
    <td><code>array</code></td>
    <td>A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="contentCustomization" /></td>
    <td><code></code></td>
    <td>Represents the content options to be customized throughout the authentication flow for a tenant. NOTE: Supported by Microsoft Entra External ID in external tenants only.</td>
</tr>
<tr>
    <td><CopyableCode code="customAccountResetCredentialsUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL for resetting account credentials. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customCSS" /></td>
    <td><code>string (base64url)</code></td>
    <td>CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25 KB.</td>
</tr>
<tr>
    <td><CopyableCode code="customCSSRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="customCannotAccessYourAccountText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'Can't access your account?' self-service password reset (SSPR) hyperlink text on the sign-in page. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customCannotAccessYourAccountUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL to replace the default URL of the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in page. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters. DO NOT USE. Use customAccountResetCredentialsUrl instead.</td>
</tr>
<tr>
    <td><CopyableCode code="customForgotMyPasswordText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'Forgot my password' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customPrivacyAndCookiesText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'Privacy and Cookies' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customPrivacyAndCookiesUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL to replace the default URL of the 'Privacy and Cookies' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customResetItNowText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'reset it now' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters. DO NOT USE: Customization of the 'reset it now' hyperlink text is currently not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="customTermsOfUseText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the the default 'Terms of Use' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customTermsOfUseUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL to replace the default URL of the 'Terms of Use' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128characters.</td>
</tr>
<tr>
    <td><CopyableCode code="favicon" /></td>
    <td><code>string (base64url)</code></td>
    <td>A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="faviconRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative url for the favicon above that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="headerBackgroundColor" /></td>
    <td><code>string</code></td>
    <td>The RGB color to apply to customize the color of the header.</td>
</tr>
<tr>
    <td><CopyableCode code="headerLogo" /></td>
    <td><code>string (base64url)</code></td>
    <td>A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="headerLogoRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="loginPageLayoutConfiguration" /></td>
    <td><code></code></td>
    <td>Represents the layout configuration to be displayed on the login page for a tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="loginPageTextVisibilitySettings" /></td>
    <td><code></code></td>
    <td>Represents the various texts that can be hidden on the login page for a tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="signInPageText" /></td>
    <td><code>string</code></td>
    <td>Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogo" /></td>
    <td><code>string (base64url)</code></td>
    <td>A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogoDark" /></td>
    <td><code>string (base64url)</code></td>
    <td>A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogoDarkRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogoRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="usernameHintText" /></td>
    <td><code>string</code></td>
    <td>A string that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.</td>
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
    <td><CopyableCode code="backgroundColor" /></td>
    <td><code>string</code></td>
    <td>Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.</td>
</tr>
<tr>
    <td><CopyableCode code="backgroundImage" /></td>
    <td><code>string (base64url)</code></td>
    <td>Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image reduces bandwidth requirements and make the page load faster.</td>
</tr>
<tr>
    <td><CopyableCode code="backgroundImageRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="bannerLogo" /></td>
    <td><code>string (base64url)</code></td>
    <td>A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="bannerLogoRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="cdnList" /></td>
    <td><code>array</code></td>
    <td>A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="contentCustomization" /></td>
    <td><code></code></td>
    <td>Represents the content options to be customized throughout the authentication flow for a tenant. NOTE: Supported by Microsoft Entra External ID in external tenants only.</td>
</tr>
<tr>
    <td><CopyableCode code="customAccountResetCredentialsUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL for resetting account credentials. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customCSS" /></td>
    <td><code>string (base64url)</code></td>
    <td>CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25 KB.</td>
</tr>
<tr>
    <td><CopyableCode code="customCSSRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="customCannotAccessYourAccountText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'Can't access your account?' self-service password reset (SSPR) hyperlink text on the sign-in page. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customCannotAccessYourAccountUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL to replace the default URL of the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in page. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters. DO NOT USE. Use customAccountResetCredentialsUrl instead.</td>
</tr>
<tr>
    <td><CopyableCode code="customForgotMyPasswordText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'Forgot my password' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customPrivacyAndCookiesText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'Privacy and Cookies' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customPrivacyAndCookiesUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL to replace the default URL of the 'Privacy and Cookies' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customResetItNowText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the default 'reset it now' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters. DO NOT USE: Customization of the 'reset it now' hyperlink text is currently not supported.</td>
</tr>
<tr>
    <td><CopyableCode code="customTermsOfUseText" /></td>
    <td><code>string</code></td>
    <td>A string to replace the the default 'Terms of Use' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="customTermsOfUseUrl" /></td>
    <td><code>string</code></td>
    <td>A custom URL to replace the default URL of the 'Terms of Use' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128characters.</td>
</tr>
<tr>
    <td><CopyableCode code="favicon" /></td>
    <td><code>string (base64url)</code></td>
    <td>A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="faviconRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative url for the favicon above that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="headerBackgroundColor" /></td>
    <td><code>string</code></td>
    <td>The RGB color to apply to customize the color of the header.</td>
</tr>
<tr>
    <td><CopyableCode code="headerLogo" /></td>
    <td><code>string (base64url)</code></td>
    <td>A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="headerLogoRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="loginPageLayoutConfiguration" /></td>
    <td><code></code></td>
    <td>Represents the layout configuration to be displayed on the login page for a tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="loginPageTextVisibilitySettings" /></td>
    <td><code></code></td>
    <td>Represents the various texts that can be hidden on the login page for a tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="signInPageText" /></td>
    <td><code>string</code></td>
    <td>Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogo" /></td>
    <td><code>string (base64url)</code></td>
    <td>A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogoDark" /></td>
    <td><code>string (base64url)</code></td>
    <td>A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogoDarkRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="squareLogoRelativeUrl" /></td>
    <td><code>string</code></td>
    <td>A relative URL for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="usernameHintText" /></td>
    <td><code>string</code></td>
    <td>A string that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.</td>
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
    <td><a href="#parameter-organization-id"><code>organization-id</code></a>, <a href="#parameter-organizationalBrandingLocalization-id"><code>organizationalBrandingLocalization-id</code></a></td>
    <td><a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a>, <a href="#parameter-$search"><code>$search</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$count"><code>$count</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Retrieve all localization branding objects, including the default branding.</td>
</tr>
<tr>
    <td><a href="#insert"><CopyableCode code="insert" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Create a new organizationalBrandingLocalization object. This creates a localized branding and at the same time, the default branding if it doesn't exist. The default branding is created only once. It's loaded when a localized branding isn't configured for the user's browser language. To retrieve the default branding, see Get branding.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a>, <a href="#parameter-organizationalBrandingLocalization-id"><code>organizationalBrandingLocalization-id</code></a>, <a href="#parameter-@odata.type"><code>@odata.type</code></a></td>
    <td></td>
    <td>Update the properties of an organizationalBrandingLocalization object for a specific localization.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-organization-id"><code>organization-id</code></a>, <a href="#parameter-organizationalBrandingLocalization-id"><code>organizationalBrandingLocalization-id</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Delete a localized branding object. To delete the organizationalBrandingLocalization object, all images (Stream types) must first be removed from the object.</td>
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
<tr id="parameter-organization-id">
    <td><CopyableCode code="organization-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of organization</td>
</tr>
<tr id="parameter-organizationalBrandingLocalization-id">
    <td><CopyableCode code="organizationalBrandingLocalization-id" /></td>
    <td><code>string</code></td>
    <td>The unique identifier of organizationalBrandingLocalization</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.

```sql
SELECT
id,
@odata.type,
backgroundColor,
backgroundImage,
backgroundImageRelativeUrl,
bannerLogo,
bannerLogoRelativeUrl,
cdnList,
contentCustomization,
customAccountResetCredentialsUrl,
customCSS,
customCSSRelativeUrl,
customCannotAccessYourAccountText,
customCannotAccessYourAccountUrl,
customForgotMyPasswordText,
customPrivacyAndCookiesText,
customPrivacyAndCookiesUrl,
customResetItNowText,
customTermsOfUseText,
customTermsOfUseUrl,
favicon,
faviconRelativeUrl,
headerBackgroundColor,
headerLogo,
headerLogoRelativeUrl,
loginPageLayoutConfiguration,
loginPageTextVisibilitySettings,
signInPageText,
squareLogo,
squareLogoDark,
squareLogoDarkRelativeUrl,
squareLogoRelativeUrl,
usernameHintText
FROM entra_id.organization.branding_localizations
WHERE organization-id = '{{ organization-id }}' -- required
AND organizationalBrandingLocalization-id = '{{ organizationalBrandingLocalization-id }}' -- required
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Retrieve all localization branding objects, including the default branding.

```sql
SELECT
id,
@odata.type,
backgroundColor,
backgroundImage,
backgroundImageRelativeUrl,
bannerLogo,
bannerLogoRelativeUrl,
cdnList,
contentCustomization,
customAccountResetCredentialsUrl,
customCSS,
customCSSRelativeUrl,
customCannotAccessYourAccountText,
customCannotAccessYourAccountUrl,
customForgotMyPasswordText,
customPrivacyAndCookiesText,
customPrivacyAndCookiesUrl,
customResetItNowText,
customTermsOfUseText,
customTermsOfUseUrl,
favicon,
faviconRelativeUrl,
headerBackgroundColor,
headerLogo,
headerLogoRelativeUrl,
loginPageLayoutConfiguration,
loginPageTextVisibilitySettings,
signInPageText,
squareLogo,
squareLogoDark,
squareLogoDarkRelativeUrl,
squareLogoRelativeUrl,
usernameHintText
FROM entra_id.organization.branding_localizations
WHERE organization-id = '{{ organization-id }}' -- required
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

Create a new organizationalBrandingLocalization object. This creates a localized branding and at the same time, the default branding if it doesn't exist. The default branding is created only once. It's loaded when a localized branding isn't configured for the user's browser language. To retrieve the default branding, see Get branding.

```sql
INSERT INTO entra_id.organization.branding_localizations (
id,
@odata.type,
backgroundColor,
backgroundImage,
backgroundImageRelativeUrl,
bannerLogo,
bannerLogoRelativeUrl,
cdnList,
contentCustomization,
customAccountResetCredentialsUrl,
customCannotAccessYourAccountText,
customCannotAccessYourAccountUrl,
customCSS,
customCSSRelativeUrl,
customForgotMyPasswordText,
customPrivacyAndCookiesText,
customPrivacyAndCookiesUrl,
customResetItNowText,
customTermsOfUseText,
customTermsOfUseUrl,
favicon,
faviconRelativeUrl,
headerBackgroundColor,
headerLogo,
headerLogoRelativeUrl,
loginPageLayoutConfiguration,
loginPageTextVisibilitySettings,
signInPageText,
squareLogo,
squareLogoDark,
squareLogoDarkRelativeUrl,
squareLogoRelativeUrl,
usernameHintText,
organization-id
)
SELECT 
'{{ id }}',
'{{ @odata.type }}' /* required */,
'{{ backgroundColor }}',
'{{ backgroundImage }}',
'{{ backgroundImageRelativeUrl }}',
'{{ bannerLogo }}',
'{{ bannerLogoRelativeUrl }}',
'{{ cdnList }}',
'{{ contentCustomization }}',
'{{ customAccountResetCredentialsUrl }}',
'{{ customCannotAccessYourAccountText }}',
'{{ customCannotAccessYourAccountUrl }}',
'{{ customCSS }}',
'{{ customCSSRelativeUrl }}',
'{{ customForgotMyPasswordText }}',
'{{ customPrivacyAndCookiesText }}',
'{{ customPrivacyAndCookiesUrl }}',
'{{ customResetItNowText }}',
'{{ customTermsOfUseText }}',
'{{ customTermsOfUseUrl }}',
'{{ favicon }}',
'{{ faviconRelativeUrl }}',
'{{ headerBackgroundColor }}',
'{{ headerLogo }}',
'{{ headerLogoRelativeUrl }}',
'{{ loginPageLayoutConfiguration }}',
'{{ loginPageTextVisibilitySettings }}',
'{{ signInPageText }}',
'{{ squareLogo }}',
'{{ squareLogoDark }}',
'{{ squareLogoDarkRelativeUrl }}',
'{{ squareLogoRelativeUrl }}',
'{{ usernameHintText }}',
'{{ organization-id }}'
RETURNING
id,
@odata.type,
backgroundColor,
backgroundImage,
backgroundImageRelativeUrl,
bannerLogo,
bannerLogoRelativeUrl,
cdnList,
contentCustomization,
customAccountResetCredentialsUrl,
customCSS,
customCSSRelativeUrl,
customCannotAccessYourAccountText,
customCannotAccessYourAccountUrl,
customForgotMyPasswordText,
customPrivacyAndCookiesText,
customPrivacyAndCookiesUrl,
customResetItNowText,
customTermsOfUseText,
customTermsOfUseUrl,
favicon,
faviconRelativeUrl,
headerBackgroundColor,
headerLogo,
headerLogoRelativeUrl,
loginPageLayoutConfiguration,
loginPageTextVisibilitySettings,
signInPageText,
squareLogo,
squareLogoDark,
squareLogoDarkRelativeUrl,
squareLogoRelativeUrl,
usernameHintText
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: branding_localizations
  props:
    - name: organization-id
      value: "{{ organization-id }}"
      description: Required parameter for the branding_localizations resource.
    - name: id
      value: "{{ id }}"
      description: |
        The unique identifier for an entity. Read-only.
    - name: @odata.type
      value: "{{ @odata.type }}"
    - name: backgroundColor
      value: "{{ backgroundColor }}"
      description: |
        Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
    - name: backgroundImage
      value: "{{ backgroundImage }}"
      description: |
        Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image reduces bandwidth requirements and make the page load faster.
    - name: backgroundImageRelativeUrl
      value: "{{ backgroundImageRelativeUrl }}"
      description: |
        A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    - name: bannerLogo
      value: "{{ bannerLogo }}"
      description: |
        A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
    - name: bannerLogoRelativeUrl
      value: "{{ bannerLogoRelativeUrl }}"
      description: |
        A relative URL for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
    - name: cdnList
      value:
        - "{{ cdnList }}"
      description: |
        A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
    - name: contentCustomization
      value: "{{ contentCustomization }}"
      description: |
        Represents the content options to be customized throughout the authentication flow for a tenant. NOTE: Supported by Microsoft Entra External ID in external tenants only.
    - name: customAccountResetCredentialsUrl
      value: "{{ customAccountResetCredentialsUrl }}"
      description: |
        A custom URL for resetting account credentials. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
    - name: customCannotAccessYourAccountText
      value: "{{ customCannotAccessYourAccountText }}"
      description: |
        A string to replace the default 'Can't access your account?' self-service password reset (SSPR) hyperlink text on the sign-in page. This text must be in Unicode format and not exceed 256 characters.
    - name: customCannotAccessYourAccountUrl
      value: "{{ customCannotAccessYourAccountUrl }}"
      description: |
        A custom URL to replace the default URL of the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in page. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters. DO NOT USE. Use customAccountResetCredentialsUrl instead.
    - name: customCSS
      value: "{{ customCSS }}"
      description: |
        CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25 KB.
    - name: customCSSRelativeUrl
      value: "{{ customCSSRelativeUrl }}"
      description: |
        A relative URL for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    - name: customForgotMyPasswordText
      value: "{{ customForgotMyPasswordText }}"
      description: |
        A string to replace the default 'Forgot my password' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters.
    - name: customPrivacyAndCookiesText
      value: "{{ customPrivacyAndCookiesText }}"
      description: |
        A string to replace the default 'Privacy and Cookies' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
    - name: customPrivacyAndCookiesUrl
      value: "{{ customPrivacyAndCookiesUrl }}"
      description: |
        A custom URL to replace the default URL of the 'Privacy and Cookies' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
    - name: customResetItNowText
      value: "{{ customResetItNowText }}"
      description: |
        A string to replace the default 'reset it now' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters. DO NOT USE: Customization of the 'reset it now' hyperlink text is currently not supported.
    - name: customTermsOfUseText
      value: "{{ customTermsOfUseText }}"
      description: |
        A string to replace the the default 'Terms of Use' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
    - name: customTermsOfUseUrl
      value: "{{ customTermsOfUseUrl }}"
      description: |
        A custom URL to replace the default URL of the 'Terms of Use' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128characters.
    - name: favicon
      value: "{{ favicon }}"
      description: |
        A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.
    - name: faviconRelativeUrl
      value: "{{ faviconRelativeUrl }}"
      description: |
        A relative url for the favicon above that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    - name: headerBackgroundColor
      value: "{{ headerBackgroundColor }}"
      description: |
        The RGB color to apply to customize the color of the header.
    - name: headerLogo
      value: "{{ headerLogo }}"
      description: |
        A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
    - name: headerLogoRelativeUrl
      value: "{{ headerLogoRelativeUrl }}"
      description: |
        A relative URL for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
    - name: loginPageLayoutConfiguration
      value: "{{ loginPageLayoutConfiguration }}"
      description: |
        Represents the layout configuration to be displayed on the login page for a tenant.
    - name: loginPageTextVisibilitySettings
      value: "{{ loginPageTextVisibilitySettings }}"
      description: |
        Represents the various texts that can be hidden on the login page for a tenant.
    - name: signInPageText
      value: "{{ signInPageText }}"
      description: |
        Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters.
    - name: squareLogo
      value: "{{ squareLogo }}"
      description: |
        A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
    - name: squareLogoDark
      value: "{{ squareLogoDark }}"
      description: |
        A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
    - name: squareLogoDarkRelativeUrl
      value: "{{ squareLogoDarkRelativeUrl }}"
      description: |
        A relative URL for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    - name: squareLogoRelativeUrl
      value: "{{ squareLogoRelativeUrl }}"
      description: |
        A relative URL for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    - name: usernameHintText
      value: "{{ usernameHintText }}"
      description: |
        A string that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
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

Update the properties of an organizationalBrandingLocalization object for a specific localization.

```sql
UPDATE entra_id.organization.branding_localizations
SET 
id = '{{ id }}',
@odata.type = '{{ @odata.type }}',
backgroundColor = '{{ backgroundColor }}',
backgroundImage = '{{ backgroundImage }}',
backgroundImageRelativeUrl = '{{ backgroundImageRelativeUrl }}',
bannerLogo = '{{ bannerLogo }}',
bannerLogoRelativeUrl = '{{ bannerLogoRelativeUrl }}',
cdnList = '{{ cdnList }}',
contentCustomization = '{{ contentCustomization }}',
customAccountResetCredentialsUrl = '{{ customAccountResetCredentialsUrl }}',
customCannotAccessYourAccountText = '{{ customCannotAccessYourAccountText }}',
customCannotAccessYourAccountUrl = '{{ customCannotAccessYourAccountUrl }}',
customCSS = '{{ customCSS }}',
customCSSRelativeUrl = '{{ customCSSRelativeUrl }}',
customForgotMyPasswordText = '{{ customForgotMyPasswordText }}',
customPrivacyAndCookiesText = '{{ customPrivacyAndCookiesText }}',
customPrivacyAndCookiesUrl = '{{ customPrivacyAndCookiesUrl }}',
customResetItNowText = '{{ customResetItNowText }}',
customTermsOfUseText = '{{ customTermsOfUseText }}',
customTermsOfUseUrl = '{{ customTermsOfUseUrl }}',
favicon = '{{ favicon }}',
faviconRelativeUrl = '{{ faviconRelativeUrl }}',
headerBackgroundColor = '{{ headerBackgroundColor }}',
headerLogo = '{{ headerLogo }}',
headerLogoRelativeUrl = '{{ headerLogoRelativeUrl }}',
loginPageLayoutConfiguration = '{{ loginPageLayoutConfiguration }}',
loginPageTextVisibilitySettings = '{{ loginPageTextVisibilitySettings }}',
signInPageText = '{{ signInPageText }}',
squareLogo = '{{ squareLogo }}',
squareLogoDark = '{{ squareLogoDark }}',
squareLogoDarkRelativeUrl = '{{ squareLogoDarkRelativeUrl }}',
squareLogoRelativeUrl = '{{ squareLogoRelativeUrl }}',
usernameHintText = '{{ usernameHintText }}'
WHERE 
organization-id = '{{ organization-id }}' --required
AND organizationalBrandingLocalization-id = '{{ organizationalBrandingLocalization-id }}' --required
AND @odata.type = '{{ @odata.type }}' --required
RETURNING
id,
@odata.type,
backgroundColor,
backgroundImage,
backgroundImageRelativeUrl,
bannerLogo,
bannerLogoRelativeUrl,
cdnList,
contentCustomization,
customAccountResetCredentialsUrl,
customCSS,
customCSSRelativeUrl,
customCannotAccessYourAccountText,
customCannotAccessYourAccountUrl,
customForgotMyPasswordText,
customPrivacyAndCookiesText,
customPrivacyAndCookiesUrl,
customResetItNowText,
customTermsOfUseText,
customTermsOfUseUrl,
favicon,
faviconRelativeUrl,
headerBackgroundColor,
headerLogo,
headerLogoRelativeUrl,
loginPageLayoutConfiguration,
loginPageTextVisibilitySettings,
signInPageText,
squareLogo,
squareLogoDark,
squareLogoDarkRelativeUrl,
squareLogoRelativeUrl,
usernameHintText;
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

Delete a localized branding object. To delete the organizationalBrandingLocalization object, all images (Stream types) must first be removed from the object.

```sql
DELETE FROM entra_id.organization.branding_localizations
WHERE organization-id = '{{ organization-id }}' --required
AND organizationalBrandingLocalization-id = '{{ organizationalBrandingLocalization-id }}' --required
AND If-Match = '{{ If-Match }}'
;
```
</TabItem>
</Tabs>
