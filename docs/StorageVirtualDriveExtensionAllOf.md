# StorageVirtualDriveExtensionAllOf

Definition of the list of properties defined in 'storage.VirtualDriveExtension', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootable** | **str** | The ability to boot from the virtual drive. | [optional] [readonly] 
**container_id** | **int** | The container id of the virtual drive. | [optional] [readonly] 
**drive_state** | **str** | The state of the virtual drive. | [optional] [readonly] 
**name** | **str** | The name of the Virtual drive. | [optional] [readonly] 
**oper_device_id** | **str** | The operational device id of the virtual drive. | [optional] [readonly] 
**uuid** | **str** | The UUID assigned to the virtual drive. | [optional] [readonly] 
**vendor_uuid** | **str** | The UUID value of the vendor assigned to the virtual drive. | [optional] [readonly] 
**virtual_drive_dn** | **str** | The distinguished name of the virtual drive for which the extended data is provided. | [optional] [readonly] 
**virtual_drive_id** | **str** | The Id of the virtual drive. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_controller** | [**StorageControllerRelationship**](StorageControllerRelationship.md) |  | [optional] 
**virtual_drive** | [**StorageVirtualDriveRelationship**](StorageVirtualDriveRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


