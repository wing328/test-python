# IamPrivilegeSetAllOf

Definition of the list of properties defined in 'iam.PrivilegeSet', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the privilege set. | [optional] [readonly] 
**name** | **str** | Name of the privilege set. | [optional] 
**privilege_names** | **[str]** |  | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**associated_privilege_sets** | [**[IamPrivilegeSetRelationship], none_type**](IamPrivilegeSetRelationship.md) | An array of relationships to iamPrivilegeSet resources. | [optional] 
**privileges** | [**[IamPrivilegeRelationship], none_type**](IamPrivilegeRelationship.md) | An array of relationships to iamPrivilege resources. | [optional] [readonly] 
**system** | [**IamSystemRelationship**](IamSystemRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


