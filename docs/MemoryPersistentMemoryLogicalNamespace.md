# MemoryPersistentMemoryLogicalNamespace

Persistent Memory Namespace specification that needs to be applied to the associated servers through this policy. This would result in the creation, modification, or deletion of a Namespace on the servers.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**capacity** | **int** | Capacity of this Namespace that is created or modified. | [optional] 
**mode** | **str** | Mode of this Namespace that is created or modified. | [optional]  if omitted the server will use the default value of "raw"
**name** | **str** | Name of this Namespace to be created on the server. | [optional] 
**socket_id** | **int** | Socket ID of the region on which this Namespace has to be created or modified. | [optional]  if omitted the server will use the default value of 1
**socket_memory_id** | **str** | Socket Memory ID of the region on which this Namespace has to be created or modified. | [optional]  if omitted the server will use the default value of "Not Applicable"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


