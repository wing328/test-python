# StorageEnclosureAllOf

Definition of the list of properties defined in 'storage.Enclosure', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **int** | This represent the chassis-ID that houses the storage enclosure. | [optional] [readonly] 
**description** | **str** | This represnets the description for the storage enclosure. | [optional] [readonly] 
**enclosure_id** | **int** | This represnets the Identifier for the storage enclosure. | [optional] [readonly] 
**num_slots** | **int** | This represent the number of slots present in storage enclosure. | [optional] [readonly] 
**presence** | **str** | This represent the availability of storage enclosure. | [optional] [readonly] 
**server_id** | **int** | This represent the server-ID that houses the storage enclosure. | [optional] [readonly] 
**type** | **str** | This represent the type of storage enclosure. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**enclosure_disk_slots** | [**[StorageEnclosureDiskSlotEpRelationship], none_type**](StorageEnclosureDiskSlotEpRelationship.md) | An array of relationships to storageEnclosureDiskSlotEp resources. | [optional] [readonly] 
**enclosure_disks** | [**[StorageEnclosureDiskRelationship], none_type**](StorageEnclosureDiskRelationship.md) | An array of relationships to storageEnclosureDisk resources. | [optional] [readonly] 
**equipment_chassis** | [**EquipmentChassisRelationship**](EquipmentChassisRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**physical_disks** | [**[StoragePhysicalDiskRelationship], none_type**](StoragePhysicalDiskRelationship.md) | An array of relationships to storagePhysicalDisk resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


