# IamPermissionAllOf

Definition of the list of properties defined in 'iam.Permission', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The informative description about each permission. | [optional] 
**name** | **str** | The name of the permission which has to be granted to user. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**end_point_roles** | [**[IamEndPointRoleRelationship], none_type**](IamEndPointRoleRelationship.md) | An array of relationships to iamEndPointRole resources. | [optional] [readonly] 
**resource_roles** | [**[IamResourceRolesRelationship], none_type**](IamResourceRolesRelationship.md) | An array of relationships to iamResourceRoles resources. | [optional] 
**roles** | [**[IamRoleRelationship], none_type**](IamRoleRelationship.md) | An array of relationships to iamRole resources. | [optional] 
**session_limits** | [**IamSessionLimitsRelationship**](IamSessionLimitsRelationship.md) |  | [optional] 
**user_groups** | [**[IamUserGroupRelationship], none_type**](IamUserGroupRelationship.md) | An array of relationships to iamUserGroup resources. | [optional] 
**users** | [**[IamUserRelationship], none_type**](IamUserRelationship.md) | An array of relationships to iamUser resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


