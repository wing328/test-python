# SdwanRouterPolicyAllOf

Definition of the list of properties defined in 'sdwan.RouterPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_size** | **str** | Scale of the SD-WAN router virtual machine deployment. | [optional]  if omitted the server will use the default value of "Typical"
**wan_count** | **int** | Number of WAN connections across the SD-WAN site. | [optional] 
**wan_termination_type** | **str** | Defines if the WAN networks are singly or dually terminated. Dually terminated WANs are configured on all the SD-WAN routers. Singly terminated WANs are configured only on one of the SD-WAN routers. | [optional]  if omitted the server will use the default value of "Single"
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[SdwanProfileRelationship], none_type**](SdwanProfileRelationship.md) | An array of relationships to sdwanProfile resources. | [optional] 
**solution_image** | [**SoftwareSolutionDistributableRelationship**](SoftwareSolutionDistributableRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


