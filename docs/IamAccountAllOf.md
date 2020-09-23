# IamAccountAllOf

Definition of the list of properties defined in 'iam.Account', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


