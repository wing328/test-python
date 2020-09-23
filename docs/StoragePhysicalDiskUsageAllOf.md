# StoragePhysicalDiskUsageAllOf

Definition of the list of properties defined in 'storage.PhysicalDiskUsage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_blocks** | **str** | The number of blocks that are a part of the virtual drive. | [optional] [readonly] 
**physical_drive** | **str** | The physical disk for which the usage is reported. | [optional] [readonly] 
**span** | **str** | The span of the physical disk. | [optional] [readonly] 
**starting_block** | **str** | The starting block id of the virtual drive within the physical drive. | [optional] [readonly] 
**state** | **str** | The current state of the physical disk usage. | [optional] [readonly] 
**virtual_drive** | **str** | The virtual drive corresponding to the physical disk. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


