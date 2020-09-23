# StorageDiskGroupAllOf

Definition of the list of properties defined in 'storage.DiskGroup', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name to identity this disk group in the controller. | [optional] 
**raid_type** | **str** | Raid level of the virtual drives in this diskgroup. | [optional] 
**dedicated_hot_spares** | [**[StoragePhysicalDiskRelationship], none_type**](StoragePhysicalDiskRelationship.md) | An array of relationships to storagePhysicalDisk resources. | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**spans** | [**[StorageSpanRelationship], none_type**](StorageSpanRelationship.md) | An array of relationships to storageSpan resources. | [optional] 
**storage_controller** | [**StorageControllerRelationship**](StorageControllerRelationship.md) |  | [optional] 
**virtual_drives** | [**[StorageVirtualDriveRelationship], none_type**](StorageVirtualDriveRelationship.md) | An array of relationships to storageVirtualDrive resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


