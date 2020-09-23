# IamEndPointUserRoleAllOf

Definition of the list of properties defined in 'iam.EndPointUserRole', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_password** | **bool** | Denotes whether password has changed. | [optional] [readonly] 
**enabled** | **bool** | Enables the user account on the endpoint. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**password** | **str** | Valid login password of the user. | [optional] 
**end_point_role** | [**[IamEndPointRoleRelationship], none_type**](IamEndPointRoleRelationship.md) | An array of relationships to iamEndPointRole resources. | [optional] 
**end_point_user** | [**IamEndPointUserRelationship**](IamEndPointUserRelationship.md) |  | [optional] 
**end_point_user_policy** | [**IamEndPointUserPolicyRelationship**](IamEndPointUserPolicyRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


