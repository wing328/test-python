# IppoolShadowPoolAllOf

Definition of the list of properties defined in 'ippool.ShadowPool', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_v4_blocks** | [**[IppoolIpBlock]**](IppoolIpBlock.md) |  | [optional] 
**ip_v4_config** | [**IppoolIpV4Config**](IppoolIpV4Config.md) |  | [optional] 
**v4_assigned** | **int** | Number of IPv4 addresses currently in use. | [optional] [readonly] 
**v4_size** | **int** | Number of IPv4 addresses in this pool. | [optional] [readonly] 
**v6_assigned** | **int** | Number of IPv6 addresses currently in use. | [optional] [readonly] 
**v6_size** | **int** | Number of IPv6 addresses in this pool. | [optional] [readonly] 
**pool** | [**IppoolPoolRelationship**](IppoolPoolRelationship.md) |  | [optional] 
**v4_block_heads** | [**[IppoolShadowBlockRelationship], none_type**](IppoolShadowBlockRelationship.md) | An array of relationships to ippoolShadowBlock resources. | [optional] [readonly] 
**vrf** | [**VrfVrfRelationship**](VrfVrfRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


