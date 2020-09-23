# IamEndPointRoleAllOf

Definition of the list of properties defined in 'iam.EndPointRole', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the end point role. | [optional] [readonly] 
**role_type** | **str** | User specified tags to roles like as ep-admin or ep-readonly. | [optional] [readonly] 
**type** | **str** | The type of the end point like Cisco UCS Fabric Interconnect or Cisco IMC. | [optional] [readonly]  if omitted the server will use the default value of ""
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**end_point_privileges** | [**[IamEndPointPrivilegeRelationship], none_type**](IamEndPointPrivilegeRelationship.md) | An array of relationships to iamEndPointPrivilege resources. | [optional] [readonly] 
**system** | [**IamSystemRelationship**](IamSystemRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


