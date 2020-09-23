# MemoryArrayAllOf

Definition of the list of properties defined in 'memory.Array', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **int** | The instance number of the memory array. | [optional] [readonly] 
**cpu_id** | **int** | ID of the CPU that access this memory array. | [optional] [readonly] 
**current_capacity** | **str** | Current capacity of all the memory units on a server. | [optional] [readonly] 
**error_correction** | **str** | The primary hardware error detection or correction method supported by the memory array. | [optional] [readonly] 
**max_capacity** | **str** | Maximum capacity of all the memory units on a server. | [optional] [readonly] 
**max_devices** | **str** | The maximum number of slots or sockets available for memory devices in the memory array. | [optional] [readonly] 
**oper_power_state** | **str** | The power state indicator of the memory array. | [optional] [readonly] 
**presence** | **str** | The presence of atleast one memory device in the array. Valid values are &#39;equipped&#39; and &#39;absent&#39;. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**persistent_memory_units** | [**[MemoryPersistentMemoryUnitRelationship], none_type**](MemoryPersistentMemoryUnitRelationship.md) | An array of relationships to memoryPersistentMemoryUnit resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**units** | [**[MemoryUnitRelationship], none_type**](MemoryUnitRelationship.md) | An array of relationships to memoryUnit resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


