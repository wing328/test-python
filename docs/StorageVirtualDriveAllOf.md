# StorageVirtualDriveAllOf

Definition of the list of properties defined in 'storage.VirtualDrive', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_policy** | **str** | The access policy of the virtual drive. | [optional] [readonly] 
**actual_write_cache_policy** | **str** | The current write cache policy of the virtual drive. | [optional] [readonly] 
**available_size** | **str** | Available storage capacity of the virtual drive. | [optional] [readonly] 
**block_size** | **str** | Block size of the virtual drive. | [optional] [readonly] 
**bootable** | **str** | The virtual drive bootable state. | [optional] [readonly] 
**config_state** | **str** | The configuration state of the virtual drive. | [optional] [readonly] 
**configured_write_cache_policy** | **str** | The requested write cache policy of the virtual drive. | [optional] [readonly] 
**connection_protocol** | **str** | The connection protocol of the virtual drive. | [optional] [readonly] 
**drive_cache** | **str** | The state of the drive cache of the virtual drive. | [optional] [readonly] 
**drive_security** | **str** | The driveSecurity state of the Virtual drive. | [optional] [readonly] 
**drive_state** | **str** | The state of the Virtual drive. | [optional] [readonly] 
**io_policy** | **str** | The Input/Output Policy defined on the Virtual drive. | [optional] [readonly] 
**name** | **str** | The name of the Virtual drive. | [optional] [readonly] 
**num_blocks** | **str** | Number of Blocks on the Physical Disk. | [optional] [readonly] 
**oper_state** | **str** | The current operational state of Virtual drive. | [optional] [readonly] 
**operability** | **str** | The current operability state of Virtual drive. | [optional] [readonly] 
**physical_block_size** | **str** | The block size of the the virtual drive. | [optional] [readonly] 
**presence** | **str** | The presence status of the virtual drive. | [optional] [readonly] 
**read_policy** | **str** | The read-ahead cache mode of the virtual drive. | [optional] [readonly] 
**security_flags** | **str** | The security flags set for this virtual drive. | [optional] [readonly] 
**size** | **str** | The size of the virtual drive in MB. | [optional] [readonly] 
**strip_size** | **str** | The strip size is the portion of a stripe that resides on a single drive in the drive group, this is measured in KB. | [optional] [readonly] 
**type** | **str** | The raid type of the virtual drive. | [optional] [readonly] 
**uuid** | **str** | The uuid of the virtual drive. | [optional] [readonly] 
**vendor_uuid** | **str** | The UUID value of the vendor. | [optional] [readonly] 
**virtual_drive_id** | **str** | The identifier for this Virtual drive. | [optional] [readonly] 
**disk_group** | [**StorageDiskGroupRelationship**](StorageDiskGroupRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**physical_disk_usages** | [**[StoragePhysicalDiskUsageRelationship], none_type**](StoragePhysicalDiskUsageRelationship.md) | An array of relationships to storagePhysicalDiskUsage resources. | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_controller** | [**StorageControllerRelationship**](StorageControllerRelationship.md) |  | [optional] 
**vd_member_eps** | [**[StorageVdMemberEpRelationship], none_type**](StorageVdMemberEpRelationship.md) | An array of relationships to storageVdMemberEp resources. | [optional] [readonly] 
**virtual_drive_extension** | [**StorageVirtualDriveExtensionRelationship**](StorageVirtualDriveExtensionRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


