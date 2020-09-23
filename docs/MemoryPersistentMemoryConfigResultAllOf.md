# MemoryPersistentMemoryConfigResultAllOf

Definition of the list of properties defined in 'memory.PersistentMemoryConfigResult', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_error_desc** | **str** | Error in the result of a previously applied Persistent Memory configuration on a server. | [optional] [readonly] 
**config_result** | **str** | Result of a previously applied Persistent Memory configuration on a server. | [optional] [readonly] 
**config_sequence_no** | **int** | Sequence number of a previously applied Persistent Memory configuration on a server. | [optional] [readonly] 
**config_state** | **str** | State of a previously applied Persistent Memory configuration on a server. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**memory_persistent_memory_configuration** | [**MemoryPersistentMemoryConfigurationRelationship**](MemoryPersistentMemoryConfigurationRelationship.md) |  | [optional] 
**persistent_memory_namespace_config_results** | [**[MemoryPersistentMemoryNamespaceConfigResultRelationship], none_type**](MemoryPersistentMemoryNamespaceConfigResultRelationship.md) | An array of relationships to memoryPersistentMemoryNamespaceConfigResult resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


