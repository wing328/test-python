# StoragePhysicalDiskExtensionAllOf

Definition of the list of properties defined in 'storage.PhysicalDiskExtension', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootable** | **str** | The whether disk is bootable or not. | [optional] [readonly] 
**disk_dn** | **str** | The distinguished name of the Physical drive. | [optional] [readonly] 
**disk_id** | **int** | The storage Enclosure slotId. | [optional] [readonly] 
**disk_state** | **str** | The current drive state of disk. | [optional] [readonly] 
**health** | **str** | The current drive state of disk. | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**physical_disk** | [**StoragePhysicalDiskRelationship**](StoragePhysicalDiskRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_controller** | [**StorageControllerRelationship**](StorageControllerRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


