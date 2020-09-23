# StoragePhysicalDiskAllOf

Definition of the list of properties defined in 'storage.PhysicalDisk', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **str** | The block size of the physical disk in bytes. | [optional] [readonly] 
**bootable** | **str** | This field identifies the disk drive as bootable if set to true. | [optional] [readonly] 
**configuration_checkpoint** | **str** | The current configuration checkpoint of the physical disk. | [optional] [readonly] 
**configuration_state** | **str** | The current configuration state of the physical disk. | [optional] [readonly] 
**discovered_path** | **str** | The discovered path of the physical disk. | [optional] [readonly] 
**disk_id** | **str** | This field identifies the ID assigned to physical disks. | [optional] [readonly] 
**disk_state** | **str** | This field identifies the health of the disk. | [optional] [readonly] 
**drive_firmware** | **str** | This field identifies the disk firmware running in the disk. | [optional] 
**drive_state** | **str** | The drive state as reported by the controller. | [optional] [readonly] 
**fde_capable** | **str** | Full-Disk Encryption capability parameter of the physical disk. | [optional] 
**hot_spare_type** | **str** | Type of hotspare configured on the physical disk. | [optional] 
**link_speed** | **str** | The speed of the link between the drive and the controller. | [optional] [readonly] 
**link_state** | **str** | The current link state of the physical disk. | [optional] [readonly] 
**num_blocks** | **str** | The number of blocks present on the physical disk. | [optional] [readonly] 
**oper_power_state** | **str** | Operational power of the physical disk. | [optional] [readonly] 
**oper_qualifier_reason** | **str** | This reason for the operational status of the disk. | [optional] [readonly] 
**operability** | **str** | This field identifies the disk operability of the disk. | [optional] [readonly] 
**physical_block_size** | **str** | The block size of the installed physical disk. | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for physicalDisk. | [optional] [readonly] 
**presence** | **str** | The presence state of the physical disk. | [optional] [readonly] 
**protocol** | **str** | This field identifies the disk protocol used for communication. | [optional] [readonly] 
**raw_size** | **str** | The raw size of the physical disk in MB. | [optional] [readonly] 
**secured** | **str** | This field identifies whether the disk is encrypted. | [optional] 
**size** | **str** | The size of the physical disk in MB. | [optional] [readonly] 
**thermal** | **str** | Thermal state of the physical disk. | [optional] [readonly] 
**type** | **str** | This field identifies the type of the physical disk. | [optional] [readonly] 
**variant_type** | **str** | The variant type of the physical disk. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**locator_led** | [**EquipmentLocatorLedRelationship**](EquipmentLocatorLedRelationship.md) |  | [optional] 
**physical_disk_extensions** | [**[StoragePhysicalDiskExtensionRelationship], none_type**](StoragePhysicalDiskExtensionRelationship.md) | An array of relationships to storagePhysicalDiskExtension resources. | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**running_firmware** | [**[FirmwareRunningFirmwareRelationship], none_type**](FirmwareRunningFirmwareRelationship.md) | An array of relationships to firmwareRunningFirmware resources. | [optional] [readonly] 
**sas_ports** | [**[StorageSasPortRelationship], none_type**](StorageSasPortRelationship.md) | An array of relationships to storageSasPort resources. | [optional] [readonly] 
**storage_controller** | [**StorageControllerRelationship**](StorageControllerRelationship.md) |  | [optional] 
**storage_enclosure** | [**StorageEnclosureRelationship**](StorageEnclosureRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


