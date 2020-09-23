# HyperflexHealthAllOf

Definition of the list of properties defined in 'hyperflex.Health', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arbitration_service_state** | **str** |  | [optional] [readonly]  if omitted the server will use the default value of "NOT_AVAILABLE"
**data_replication_compliance** | **str** |  | [optional] [readonly]  if omitted the server will use the default value of "UNKNOWN"
**resiliency_details** | [**HyperflexHxResiliencyInfoDt**](HyperflexHxResiliencyInfoDt.md) |  | [optional] 
**state** | **str** |  | [optional] [readonly]  if omitted the server will use the default value of "UNKNOWN"
**uuid** | **str** |  | [optional] [readonly] 
**zk_health** | **str** |  | [optional] [readonly]  if omitted the server will use the default value of "NOT_AVAILABLE"
**zone_resiliency_list** | [**[HyperflexHxZoneResiliencyInfoDt]**](HyperflexHxZoneResiliencyInfoDt.md) |  | [optional] 
**cluster** | [**HyperflexClusterRelationship**](HyperflexClusterRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


