# EquipmentRackEnclosureAllOf

Definition of the list of properties defined in 'equipment.RackEnclosure', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enclosure_id** | **int** | This represents the Enclosure Identifier for Rack servers. | [optional] [readonly] 
**fanmodules** | [**[EquipmentFanModuleRelationship], none_type**](EquipmentFanModuleRelationship.md) | An array of relationships to equipmentFanModule resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**psus** | [**[EquipmentPsuRelationship], none_type**](EquipmentPsuRelationship.md) | An array of relationships to equipmentPsu resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**slots** | [**[EquipmentRackEnclosureSlotRelationship], none_type**](EquipmentRackEnclosureSlotRelationship.md) | An array of relationships to equipmentRackEnclosureSlot resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


