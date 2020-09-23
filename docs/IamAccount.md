# IamAccount

The Intersight Account used to access Intersight.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**name** | **str** | Name of the Intersight account. By default, name is same as the MoID of the account. | [optional] 
**status** | **str** | Status of the account. To activate the Intersight account, claim a device to the account. | [optional] [readonly] 
**_1_license_reservation_op** | [**LicenseLicenseReservationOpRelationship**](LicenseLicenseReservationOpRelationship.md) |  | [optional] 
**app_registrations** | [**[IamAppRegistrationRelationship], none_type**](IamAppRegistrationRelationship.md) | An array of relationships to iamAppRegistration resources. | [optional] [readonly] 
**domain_groups** | [**[IamDomainGroupRelationship], none_type**](IamDomainGroupRelationship.md) | An array of relationships to iamDomainGroup resources. | [optional] [readonly] 
**end_point_roles** | [**[IamEndPointRoleRelationship], none_type**](IamEndPointRoleRelationship.md) | An array of relationships to iamEndPointRole resources. | [optional] [readonly] 
**idpreferences** | [**[IamIdpReferenceRelationship], none_type**](IamIdpReferenceRelationship.md) | An array of relationships to iamIdpReference resources. | [optional] [readonly] 
**idps** | [**[IamIdpRelationship], none_type**](IamIdpRelationship.md) | An array of relationships to iamIdp resources. | [optional] [readonly] 
**permissions** | [**[IamPermissionRelationship], none_type**](IamPermissionRelationship.md) | An array of relationships to iamPermission resources. | [optional] [readonly] 
**privilege_sets** | [**[IamPrivilegeSetRelationship], none_type**](IamPrivilegeSetRelationship.md) | An array of relationships to iamPrivilegeSet resources. | [optional] [readonly] 
**privileges** | [**[IamPrivilegeRelationship], none_type**](IamPrivilegeRelationship.md) | An array of relationships to iamPrivilege resources. | [optional] [readonly] 
**resource_limits** | [**IamResourceLimitsRelationship**](IamResourceLimitsRelationship.md) |  | [optional] 
**roles** | [**[IamRoleRelationship], none_type**](IamRoleRelationship.md) | An array of relationships to iamRole resources. | [optional] [readonly] 
**security_holder** | [**IamSecurityHolderRelationship**](IamSecurityHolderRelationship.md) |  | [optional] 
**session_limits** | [**IamSessionLimitsRelationship**](IamSessionLimitsRelationship.md) |  | [optional] 
**account_moid** | **str** | The Account ID for this managed object. | [optional] [readonly] 
**create_time** | **datetime** | The time when this managed object was created. | [optional] [readonly] 
**domain_group_moid** | **str** | The DomainGroup ID for this managed object. | [optional] [readonly] 
**mod_time** | **datetime** | The time when this managed object was last modified. | [optional] [readonly] 
**moid** | **str** | The unique identifier of this Managed Object instance. | [optional] 
**owners** | **[str]** |  | [optional] 
**shared_scope** | **str** | Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs. | [optional] [readonly] 
**tags** | [**[MoTag]**](MoTag.md) |  | [optional] 
**version_context** | [**MoVersionContext**](MoVersionContext.md) |  | [optional] 
**ancestors** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**parent** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**permission_resources** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**display_names** | [**DisplayNames**](DisplayNames.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


