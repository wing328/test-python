# IppoolPoolAllOf

Definition of the list of properties defined in 'ippool.Pool', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_v4_blocks** | [**[IppoolIpBlock]**](IppoolIpBlock.md) |  | [optional] 
**ip_v4_config** | [**IppoolIpV4Config**](IppoolIpV4Config.md) |  | [optional] 
**v4_assigned** | **int** | Number of IPv4 addresses currently in use. | [optional] [readonly] 
**v4_size** | **int** | Number of IPv4 addresses in this pool. | [optional] [readonly] 
**v6_assigned** | **int** | Number of IPv6 addresses currently in use. | [optional] [readonly] 
**v6_size** | **int** | Number of IPv6 addresses in this pool. | [optional] [readonly] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**shadow_pools** | [**[IppoolShadowPoolRelationship], none_type**](IppoolShadowPoolRelationship.md) | An array of relationships to ippoolShadowPool resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


