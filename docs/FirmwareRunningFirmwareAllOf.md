# FirmwareRunningFirmwareAllOf

Definition of the list of properties defined in 'firmware.RunningFirmware', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Kind of the firmware - boot-booloader/system/kernel. | [optional] [readonly] 
**package_version** | **str** | Package version which the firmware belongs to. | [optional] [readonly] 
**type** | **str** | The type of the firmware. | [optional] [readonly] 
**version** | **str** | The version of the firmware. | [optional] [readonly] 
**bios_unit** | [**BiosUnitRelationship**](BiosUnitRelationship.md) |  | [optional] 
**graphics_card** | [**GraphicsCardRelationship**](GraphicsCardRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**management_controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**network_elements** | [**[NetworkElementRelationship], none_type**](NetworkElementRelationship.md) | An array of relationships to networkElement resources. | [optional] 
**pci_switch** | [**PciSwitchRelationship**](PciSwitchRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_controller** | [**StorageControllerRelationship**](StorageControllerRelationship.md) |  | [optional] 
**storage_flex_flash_controller** | [**StorageFlexFlashControllerRelationship**](StorageFlexFlashControllerRelationship.md) |  | [optional] 
**storage_physical_disk** | [**StoragePhysicalDiskRelationship**](StoragePhysicalDiskRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


