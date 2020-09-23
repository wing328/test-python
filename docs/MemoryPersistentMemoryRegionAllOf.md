# MemoryPersistentMemoryRegionAllOf

Definition of the list of properties defined in 'memory.PersistentMemoryRegion', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free_capacity** | **str** | Free capacity in GiB of the Persistent Memory Region. | [optional] [readonly] 
**health_state** | **str** | Health state of the Persistent Memory Region. | [optional] [readonly] 
**interleaved_set_id** | **str** | ID of the Interleaved Set formed for this Persistent Memory Region. | [optional] [readonly] 
**locater_ids** | **str** | Set of locator IDs that are included in the Persistent Memory Region. | [optional] [readonly] 
**persistent_memory_type** | **str** | Persistent Memory type of the Persistent Memory Region. | [optional] [readonly] 
**region_id** | **str** | ID of the Persistent Memory Region. | [optional] [readonly] 
**socket_id** | **str** | Socket ID of the Persistent Memory Region. | [optional] [readonly] 
**socket_memory_id** | **str** | Socket Memory ID of the Persistent Memory Region. | [optional] [readonly] 
**total_capacity** | **str** | Total capacity in GiB of the Persistent Memory Region. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**memory_persistent_memory_configuration** | [**MemoryPersistentMemoryConfigurationRelationship**](MemoryPersistentMemoryConfigurationRelationship.md) |  | [optional] 
**persistent_memory_namespaces** | [**[MemoryPersistentMemoryNamespaceRelationship], none_type**](MemoryPersistentMemoryNamespaceRelationship.md) | An array of relationships to memoryPersistentMemoryNamespace resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


