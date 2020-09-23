# StorageControllerAllOf

Definition of the list of properties defined in 'storage.Controller', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_flags** | **str** | The flags for the storage controller. | [optional] [readonly] 
**controller_id** | **str** | The Id of the storage controller. | [optional] [readonly] 
**controller_status** | **str** | The current status of controller. | [optional] [readonly] 
**foreign_config_present** | **bool** | Storage controller has detected disks in foreign config. | [optional] 
**hw_revision** | **str** | The hardware revision of controller. | [optional] [readonly] 
**interface_type** | **str** | Interface types are Sas, Sata, PCH. | [optional] 
**max_volumes_supported** | **int** | Maximum virtual drives that can be created on this Storage Controller. | [optional] 
**oob_interface_supported** | **str** | The CIMC support for out-of-band configuration of controller. | [optional] [readonly] 
**oper_state** | **str** | The current operational state of controller. | [optional] [readonly] 
**operability** | **str** | Operability state of the storage controller. | [optional] [readonly] 
**pci_addr** | **str** | The current pci address of controller. | [optional] [readonly] 
**pci_slot** | **str** | The pci slot name for the controller. | [optional] [readonly] 
**presence** | **str** | Physical Presence State for the Storage Controller. | [optional] [readonly] 
**raid_support** | **str** | The RAID levels supported by controller. | [optional] [readonly] 
**rebuild_rate** | **str** | Logical volume or RAID rebuild rate of Storage Controller. | [optional] [readonly] 
**self_encrypt_enabled** | **str** | Storage controller disk self encryption state. | [optional] 
**type** | **str** | Controller types are Raid, FlexFlash. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**disk_group** | [**[StorageDiskGroupRelationship], none_type**](StorageDiskGroupRelationship.md) | An array of relationships to storageDiskGroup resources. | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**physical_disk_extensions** | [**[StoragePhysicalDiskExtensionRelationship], none_type**](StoragePhysicalDiskExtensionRelationship.md) | An array of relationships to storagePhysicalDiskExtension resources. | [optional] [readonly] 
**physical_disks** | [**[StoragePhysicalDiskRelationship], none_type**](StoragePhysicalDiskRelationship.md) | An array of relationships to storagePhysicalDisk resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**running_firmware** | [**[FirmwareRunningFirmwareRelationship], none_type**](FirmwareRunningFirmwareRelationship.md) | An array of relationships to firmwareRunningFirmware resources. | [optional] [readonly] 
**virtual_drive_extensions** | [**[StorageVirtualDriveExtensionRelationship], none_type**](StorageVirtualDriveExtensionRelationship.md) | An array of relationships to storageVirtualDriveExtension resources. | [optional] [readonly] 
**virtual_drives** | [**[StorageVirtualDriveRelationship], none_type**](StorageVirtualDriveRelationship.md) | An array of relationships to storageVirtualDrive resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


