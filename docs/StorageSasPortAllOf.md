# StorageSasPortAllOf

Definition of the list of properties defined in 'storage.SasPort', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The SAS Address assigned to storage port. | [optional] [readonly] 
**disk_id** | **int** | The unique disk identifier. | [optional] [readonly] 
**end_point_id** | **int** | The end-point Id assigned to storage port. | [optional] [readonly] 
**link_description** | **str** | The description for the link. | [optional] [readonly] 
**link_speed** | **str** | The link speed negotiated for communication. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_physical_disk** | [**StoragePhysicalDiskRelationship**](StoragePhysicalDiskRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


