# HyperflexNodeAllOf

Definition of the list of properties defined in 'hyperflex.Node', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_number** | **str** |  | [optional] [readonly] 
**display_version** | **str** |  | [optional] [readonly] 
**host_name** | **str** |  | [optional] [readonly] 
**hypervisor** | **str** |  | [optional] [readonly] 
**identity** | [**HyperflexHxUuIdDt**](HyperflexHxUuIdDt.md) |  | [optional] 
**ip** | [**HyperflexHxNetworkAddressDt**](HyperflexHxNetworkAddressDt.md) |  | [optional] 
**lockdown** | **bool** |  | [optional] [readonly] 
**model_number** | **str** |  | [optional] [readonly] 
**role** | **str** |  | [optional] [readonly]  if omitted the server will use the default value of "UNKNOWN"
**serial_number** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly]  if omitted the server will use the default value of "UNKNOWN"
**version** | **str** |  | [optional] [readonly] 
**cluster** | [**HyperflexClusterRelationship**](HyperflexClusterRelationship.md) |  | [optional] 
**cluster_member** | [**AssetClusterMemberRelationship**](AssetClusterMemberRelationship.md) |  | [optional] 
**physical_server** | [**ComputePhysicalRelationship**](ComputePhysicalRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


