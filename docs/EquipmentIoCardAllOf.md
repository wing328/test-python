# EquipmentIoCardAllOf

Definition of the list of properties defined in 'equipment.IoCard', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_path** | **str** | Switch Id to which the IOM is connected to. The value can be A or B. | [optional] [readonly] 
**dc_supported** | **bool** | IOM device connector support. | [optional] [readonly] 
**side** | **str** | Location of IOM within a chassis. The value can be left or right. | [optional] [readonly] 
**equipment_chassis** | [**EquipmentChassisRelationship**](EquipmentChassisRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**physical_device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


