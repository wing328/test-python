# ResourceGroupAllOf

Definition of the list of properties defined in 'resource.Group', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this resource group. | [optional] 
**per_type_combined_selector** | [**[ResourcePerTypeCombinedSelector]**](ResourcePerTypeCombinedSelector.md) |  | [optional] 
**qualifier** | **str** | Qualifier shall be used to specify if we want to organize resources using multiple resource group or single For an account, resource groups can be of only one of the above types. (Both the types are mutually exclusive for an account.). | [optional]  if omitted the server will use the default value of "Allow-Selectors"
**selectors** | [**[ResourceSelector]**](ResourceSelector.md) |  | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**organizations** | [**[OrganizationOrganizationRelationship], none_type**](OrganizationOrganizationRelationship.md) | An array of relationships to organizationOrganization resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


