# ComputeBoardAllOf

Definition of the list of properties defined in 'compute.Board', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_id** | **int** | The identity of the motherboard. | [optional] [readonly] 
**cpu_type_controller** | **str** | The type of central processing unit on the mother board. | [optional] [readonly] 
**oper_power_state** | **str** | Current power state of the mother board of the server. | [optional] [readonly] 
**presence** | **str** | Identifies the presence of the mother board of the server. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**equipment_tpms** | [**[EquipmentTpmRelationship], none_type**](EquipmentTpmRelationship.md) | An array of relationships to equipmentTpm resources. | [optional] [readonly] 
**graphics_cards** | [**[GraphicsCardRelationship], none_type**](GraphicsCardRelationship.md) | An array of relationships to graphicsCard resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**memory_arrays** | [**[MemoryArrayRelationship], none_type**](MemoryArrayRelationship.md) | An array of relationships to memoryArray resources. | [optional] [readonly] 
**pci_coprocessor_cards** | [**[PciCoprocessorCardRelationship], none_type**](PciCoprocessorCardRelationship.md) | An array of relationships to pciCoprocessorCard resources. | [optional] [readonly] 
**pci_switch** | [**[PciSwitchRelationship], none_type**](PciSwitchRelationship.md) | An array of relationships to pciSwitch resources. | [optional] [readonly] 
**persistent_memory_configuration** | [**MemoryPersistentMemoryConfigurationRelationship**](MemoryPersistentMemoryConfigurationRelationship.md) |  | [optional] 
**processors** | [**[ProcessorUnitRelationship], none_type**](ProcessorUnitRelationship.md) | An array of relationships to processorUnit resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**security_units** | [**[SecurityUnitRelationship], none_type**](SecurityUnitRelationship.md) | An array of relationships to securityUnit resources. | [optional] [readonly] 
**storage_controllers** | [**[StorageControllerRelationship], none_type**](StorageControllerRelationship.md) | An array of relationships to storageController resources. | [optional] [readonly] 
**storage_flex_flash_controllers** | [**[StorageFlexFlashControllerRelationship], none_type**](StorageFlexFlashControllerRelationship.md) | An array of relationships to storageFlexFlashController resources. | [optional] [readonly] 
**storage_flex_util_controllers** | [**[StorageFlexUtilControllerRelationship], none_type**](StorageFlexUtilControllerRelationship.md) | An array of relationships to storageFlexUtilController resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


