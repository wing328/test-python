# IamRoleAllOf

Definition of the list of properties defined in 'iam.Role', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Informative description about each role. | [optional] [readonly] 
**name** | **str** | The name of the role which has to be granted to user. | [optional] 
**privilege_names** | **[str]** |  | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**privilege_sets** | [**[IamPrivilegeSetRelationship], none_type**](IamPrivilegeSetRelationship.md) | An array of relationships to iamPrivilegeSet resources. | [optional] [readonly] 
**system** | [**IamSystemRelationship**](IamSystemRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


