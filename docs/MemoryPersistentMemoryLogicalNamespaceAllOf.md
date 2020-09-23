# MemoryPersistentMemoryLogicalNamespaceAllOf

Definition of the list of properties defined in 'memory.PersistentMemoryLogicalNamespace', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** | Capacity of this Namespace that is created or modified. | [optional] 
**mode** | **str** | Mode of this Namespace that is created or modified. | [optional]  if omitted the server will use the default value of "raw"
**name** | **str** | Name of this Namespace to be created on the server. | [optional] 
**socket_id** | **int** | Socket ID of the region on which this Namespace has to be created or modified. | [optional]  if omitted the server will use the default value of 1
**socket_memory_id** | **str** | Socket Memory ID of the region on which this Namespace has to be created or modified. | [optional]  if omitted the server will use the default value of "Not Applicable"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


