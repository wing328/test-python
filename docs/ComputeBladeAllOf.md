# ComputeBladeAllOf

Definition of the list of properties defined in 'compute.Blade', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **str** | The id of the chassis that the blade is located in. | [optional] [readonly] 
**scaled_mode** | **str** | The mode of the server that determines it is scaled. | [optional] [readonly] 
**slot_id** | **int** | The slot number in the chassis that the blade is located in. | [optional] [readonly] 
**adapters** | [**[AdapterUnitRelationship], none_type**](AdapterUnitRelationship.md) | An array of relationships to adapterUnit resources. | [optional] [readonly] 
**bios_units** | [**[BiosUnitRelationship], none_type**](BiosUnitRelationship.md) | An array of relationships to biosUnit resources. | [optional] [readonly] 
**bmc** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**equipment_chassis** | [**EquipmentChassisRelationship**](EquipmentChassisRelationship.md) |  | [optional] 
**equipment_io_expanders** | [**[EquipmentIoExpanderRelationship], none_type**](EquipmentIoExpanderRelationship.md) | An array of relationships to equipmentIoExpander resources. | [optional] [readonly] 
**generic_inventory_holders** | [**[InventoryGenericInventoryHolderRelationship], none_type**](InventoryGenericInventoryHolderRelationship.md) | An array of relationships to inventoryGenericInventoryHolder resources. | [optional] [readonly] 
**graphics_cards** | [**[GraphicsCardRelationship], none_type**](GraphicsCardRelationship.md) | An array of relationships to graphicsCard resources. | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**locator_led** | [**EquipmentLocatorLedRelationship**](EquipmentLocatorLedRelationship.md) |  | [optional] 
**memory_arrays** | [**[MemoryArrayRelationship], none_type**](MemoryArrayRelationship.md) | An array of relationships to memoryArray resources. | [optional] 
**pci_devices** | [**[PciDeviceRelationship], none_type**](PciDeviceRelationship.md) | An array of relationships to pciDevice resources. | [optional] [readonly] 
**processors** | [**[ProcessorUnitRelationship], none_type**](ProcessorUnitRelationship.md) | An array of relationships to processorUnit resources. | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_controllers** | [**[StorageControllerRelationship], none_type**](StorageControllerRelationship.md) | An array of relationships to storageController resources. | [optional] 
**storage_enclosures** | [**[StorageEnclosureRelationship], none_type**](StorageEnclosureRelationship.md) | An array of relationships to storageEnclosure resources. | [optional] [readonly] 
**top_system** | [**TopSystemRelationship**](TopSystemRelationship.md) |  | [optional] 
**uem_connection** | [**InventoryUemConnectionRelationship**](InventoryUemConnectionRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


