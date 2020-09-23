# StorageFlexFlashControllerAllOf

Definition of the list of properties defined in 'storage.FlexFlashController', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_state** | **str** | State of the Flex Flash Storage Controller. | [optional] [readonly] 
**ff_controller_id** | **str** | Identifier for the Flex Flash Storage Controller. | [optional] [readonly] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**flex_flash_controller_props** | [**[StorageFlexFlashControllerPropsRelationship], none_type**](StorageFlexFlashControllerPropsRelationship.md) | An array of relationships to storageFlexFlashControllerProps resources. | [optional] [readonly] 
**flex_flash_physical_drives** | [**[StorageFlexFlashPhysicalDriveRelationship], none_type**](StorageFlexFlashPhysicalDriveRelationship.md) | An array of relationships to storageFlexFlashPhysicalDrive resources. | [optional] [readonly] 
**flex_flash_virtual_drives** | [**[StorageFlexFlashVirtualDriveRelationship], none_type**](StorageFlexFlashVirtualDriveRelationship.md) | An array of relationships to storageFlexFlashVirtualDrive resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**running_firmware** | [**[FirmwareRunningFirmwareRelationship], none_type**](FirmwareRunningFirmwareRelationship.md) | An array of relationships to firmwareRunningFirmware resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


