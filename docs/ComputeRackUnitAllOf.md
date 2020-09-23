# ComputeRackUnitAllOf

Definition of the list of properties defined in 'compute.RackUnit', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | Connectivity Status of RackUnit to Switch - A or B or AB. | [optional] [readonly] 
**server_id** | **int** | RackUnit ID that uniquely identifies the server. | [optional] [readonly] 
**topology_scan_status** | **str** | To maintain the Topology workflow run status. | [optional] 
**adapters** | [**[AdapterUnitRelationship], none_type**](AdapterUnitRelationship.md) | An array of relationships to adapterUnit resources. | [optional] [readonly] 
**bios_bootmode** | [**BiosBootModeRelationship**](BiosBootModeRelationship.md) |  | [optional] 
**biosunits** | [**[BiosUnitRelationship], none_type**](BiosUnitRelationship.md) | An array of relationships to biosUnit resources. | [optional] [readonly] 
**bmc** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**boot_device_bootmode** | [**BootDeviceBootModeRelationship**](BootDeviceBootModeRelationship.md) |  | [optional] 
**fanmodules** | [**[EquipmentFanModuleRelationship], none_type**](EquipmentFanModuleRelationship.md) | An array of relationships to equipmentFanModule resources. | [optional] [readonly] 
**generic_inventory_holders** | [**[InventoryGenericInventoryHolderRelationship], none_type**](InventoryGenericInventoryHolderRelationship.md) | An array of relationships to inventoryGenericInventoryHolder resources. | [optional] [readonly] 
**graphics_cards** | [**[GraphicsCardRelationship], none_type**](GraphicsCardRelationship.md) | An array of relationships to graphicsCard resources. | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**locator_led** | [**EquipmentLocatorLedRelationship**](EquipmentLocatorLedRelationship.md) |  | [optional] 
**memory_arrays** | [**[MemoryArrayRelationship], none_type**](MemoryArrayRelationship.md) | An array of relationships to memoryArray resources. | [optional] 
**pci_devices** | [**[PciDeviceRelationship], none_type**](PciDeviceRelationship.md) | An array of relationships to pciDevice resources. | [optional] [readonly] 
**processors** | [**[ProcessorUnitRelationship], none_type**](ProcessorUnitRelationship.md) | An array of relationships to processorUnit resources. | [optional] 
**psus** | [**[EquipmentPsuRelationship], none_type**](EquipmentPsuRelationship.md) | An array of relationships to equipmentPsu resources. | [optional] [readonly] 
**rack_enclosure_slot** | [**EquipmentRackEnclosureSlotRelationship**](EquipmentRackEnclosureSlotRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**sas_expanders** | [**[StorageSasExpanderRelationship], none_type**](StorageSasExpanderRelationship.md) | An array of relationships to storageSasExpander resources. | [optional] 
**storage_controllers** | [**[StorageControllerRelationship], none_type**](StorageControllerRelationship.md) | An array of relationships to storageController resources. | [optional] 
**storage_enclosures** | [**[StorageEnclosureRelationship], none_type**](StorageEnclosureRelationship.md) | An array of relationships to storageEnclosure resources. | [optional] [readonly] 
**top_system** | [**TopSystemRelationship**](TopSystemRelationship.md) |  | [optional] 
**uem_connection** | [**InventoryUemConnectionRelationship**](InventoryUemConnectionRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


