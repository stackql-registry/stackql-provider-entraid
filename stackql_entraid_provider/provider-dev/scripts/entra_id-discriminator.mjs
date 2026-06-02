// Service discriminator for deriving the `entra_id` (Microsoft Entra ID) provider
// from the monolithic Microsoft Graph OpenAPI document.
//
// Microsoft Graph tags every operation as `<workload>.<entityType>[.Actions|.Functions]`
// (e.g. `users.user`, `groups.calendar`, `servicePrincipals.appRoleAssignment`).
// The first segment is the Graph "workload". Entra ID is the identity & directory
// surface of Graph, so we keep the identity/directory workloads and drop the
// productivity ones (Exchange mail/calendar, OneDrive/SharePoint files, Teams,
// Intune device management, Planner, Search, Security, etc.).
//
// Returns a snake_case service name, or `null` to drop the operation.

// Map each in-scope Graph workload (first tag segment) -> stackql service name.
const WORKLOAD_TO_SERVICE = {
  applications: 'applications',
  applicationTemplates: 'application_templates',
  servicePrincipals: 'service_principals',
  directory: 'directory',
  directoryObjects: 'directory_objects',
  directoryRoles: 'directory_roles',
  directoryRoleTemplates: 'directory_role_templates',
  domains: 'domains',
  domainDnsRecords: 'domain_dns_records',
  groups: 'groups',
  groupSettings: 'group_settings',
  groupSettingTemplates: 'group_setting_templates',
  groupLifecyclePolicies: 'group_lifecycle_policies',
  organization: 'organization',
  contacts: 'org_contacts',
  contracts: 'contracts',
  devices: 'devices',
  oauth2PermissionGrants: 'oauth2_permission_grants',
  permissionGrants: 'permission_grants',
  roleManagement: 'role_management',
  scopedRoleMemberships: 'scoped_role_memberships',
  subscribedSkus: 'subscribed_skus',
  identity: 'identity',
  identityGovernance: 'identity_governance',
  identityProtection: 'identity_protection',
  identityProviders: 'identity_providers',
  policies: 'policies',
  authenticationMethodConfigurations: 'authentication_method_configurations',
  authenticationMethodsPolicy: 'authentication_methods_policy',
  certificateBasedAuthConfiguration: 'certificate_based_auth_configuration',
  invitations: 'invitations',
  agreements: 'agreements',
  agreementAcceptances: 'agreement_acceptances',
  auditLogs: 'audit_logs',
  dataPolicyOperations: 'data_policy_operations',
  tenantRelationships: 'tenant_relationships',
  schemaExtensions: 'schema_extensions',
  users: 'users',
  // Provisioning attribute-mapping helper endpoints (/filterOperators, /functions)
  filterOperators: 'synchronization',
  functions: 'synchronization',
};

// Within the `users` workload, keep only identity/directory entity types.
// Everything else (mail, calendar, drive, chat, teamwork, onenote, todo, etc.)
// is M365 productivity, not Entra ID.
const USERS_KEEP_ENTITY = new Set([
  'user',
  'appRoleAssignment',
  'licenseDetails',
  'oAuth2PermissionGrant',
  'directoryObject',
  'scopedRoleMembership',
  'authentication',
  'extension',
  'onPremisesSyncBehavior',
  'serviceProvisioningError',
]);

// Within the `groups` workload, keep only the directory-relevant entity types.
const GROUPS_KEEP_ENTITY = new Set([
  'group',
  'directoryObject',
  'appRoleAssignment',
  'groupLifecyclePolicy',
  'groupSetting',
  'extension',
  'onPremisesSyncBehavior',
  'serviceProvisioningError',
  'resourceSpecificPermissionGrant',
]);

export default function entra_idDiscriminator(path, operationId, tags /*, ctx */) {
  if (!Array.isArray(tags) || tags.length === 0) {
    return null;
  }
  const tag = tags[0];
  const parts = String(tag).split('.');
  const workload = parts[0];
  const entity = parts[1];

  const service = WORKLOAD_TO_SERVICE[workload];
  if (!service) {
    return null; // workload not part of Entra ID
  }

  // Surgically scope the two big mixed workloads to their directory resources.
  if (workload === 'users' && !USERS_KEEP_ENTITY.has(entity)) {
    return null;
  }
  if (workload === 'groups' && !GROUPS_KEEP_ENTITY.has(entity)) {
    return null;
  }

  return service;
}
