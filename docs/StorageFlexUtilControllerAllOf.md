# StorageFlexUtilControllerAllOf

Definition of the list of properties defined in 'storage.FlexUtilController', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_name** | **str** | Name of the Flex Util Controller. | [optional] 
**controller_status** | **str** | The current status of the controller. | [optional] 
**ff_controller_id** | **str** | Identifier for the Storage Flex Util Controller. | [optional] 
**internal_state** | **str** | The internal state of the controller. | [optional] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**flex_util_physical_drives** | [**[StorageFlexUtilPhysicalDriveRelationship], none_type**](StorageFlexUtilPhysicalDriveRelationship.md) | An array of relationships to storageFlexUtilPhysicalDrive resources. | [optional] [readonly] 
**flex_util_virtual_drives** | [**[StorageFlexUtilVirtualDriveRelationship], none_type**](StorageFlexUtilVirtualDriveRelationship.md) | An array of relationships to storageFlexUtilVirtualDrive resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


