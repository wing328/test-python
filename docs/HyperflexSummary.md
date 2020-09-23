# HyperflexSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**active_nodes** | **str** |  | [optional] [readonly] 
**address** | **str** |  | [optional] [readonly] 
**boottime** | **int** |  | [optional] [readonly] 
**cluster_access_policy** | **str** |  | [optional] [readonly] 
**compression_savings** | **float** |  | [optional] [readonly] 
**data_replication_compliance** | **str** |  | [optional] [readonly] 
**data_replication_factor** | **str** |  | [optional] [readonly] 
**deduplication_savings** | **float** |  | [optional] [readonly] 
**downtime** | **str** |  | [optional] [readonly] 
**free_capacity** | **int** |  | [optional] [readonly] 
**healing_info** | [**HyperflexStPlatformClusterHealingInfo**](HyperflexStPlatformClusterHealingInfo.md) |  | [optional] 
**name** | **str** |  | [optional] [readonly] 
**resiliency_details** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] [readonly] 
**resiliency_details_size** | **int** |  | [optional] [readonly] 
**resiliency_info** | [**HyperflexStPlatformClusterResiliencyInfo**](HyperflexStPlatformClusterResiliencyInfo.md) |  | [optional] 
**space_status** | **str** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 
**total_capacity** | **int** |  | [optional] [readonly] 
**total_savings** | **float** |  | [optional] [readonly] 
**uptime** | **str** |  | [optional] [readonly] 
**used_capacity** | **int** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


