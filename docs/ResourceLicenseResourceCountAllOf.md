# ResourceLicenseResourceCountAllOf

Definition of the list of properties defined in 'resource.LicenseResourceCount', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_type** | **str** | Type of licensing defined for this resource group. Used for licensing group. | [optional] [readonly]  if omitted the server will use the default value of "Base"
**resource_count** | **int** | The number of resource belongs to this licensing tier. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**license_groups** | [**[ResourceGroupRelationship], none_type**](ResourceGroupRelationship.md) | An array of relationships to resourceGroup resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


