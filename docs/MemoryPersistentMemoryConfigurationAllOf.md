# MemoryPersistentMemoryConfigurationAllOf

Definition of the list of properties defined in 'memory.PersistentMemoryConfiguration', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_capacity** | **str** | Memory capacity in GiB of a Persistent Memory configuration on a server. | [optional] [readonly] 
**num_of_modules** | **str** | Number of Persistent Memory Modules on a server. | [optional] [readonly] 
**num_of_regions** | **str** | Number of Persistent Memory Regions on a server. | [optional] [readonly] 
**persistent_memory_capacity** | **str** | Persistent memory capacity in GiB of a Persistent Memory configuration on a server. | [optional] [readonly] 
**reserved_capacity** | **str** | Reserved capacity in GiB of a Persistent Memory configuration on a server. | [optional] [readonly] 
**security_state** | **str** | Collective security state of all Persistent Memory modules on a server. | [optional] [readonly] 
**total_capacity** | **str** | Total capacity in GiB of a Persistent Memory configuration on a server. | [optional] [readonly] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**persistent_memory_config_result** | [**MemoryPersistentMemoryConfigResultRelationship**](MemoryPersistentMemoryConfigResultRelationship.md) |  | [optional] 
**persistent_memory_regions** | [**[MemoryPersistentMemoryRegionRelationship], none_type**](MemoryPersistentMemoryRegionRelationship.md) | An array of relationships to memoryPersistentMemoryRegion resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


