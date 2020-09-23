# MemoryPersistentMemoryGoal

A Persistent Memory Goal that needs to be applied on the associated servers through the policy. This would result in the creation of regions and allocation of volatile memory on the server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**memory_mode_percentage** | **int** | Volatile memory percentage. | [optional] 
**persistent_memory_type** | **str** | Type of the Persistent Memory configuration where the Persistent Memory Modules are combined in an interleaved set or not. | [optional]  if omitted the server will use the default value of "app-direct"
**socket_id** | **str** | CPU Socket ID to which this goal will be applied. | [optional]  if omitted the server will use the default value of "All Sockets"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


