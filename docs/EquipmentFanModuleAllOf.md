# EquipmentFanModuleAllOf

Definition of the list of properties defined in 'equipment.FanModule', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | This field is to provide description for the fan module. | [optional] [readonly] 
**module_id** | **int** | This field acts as the identifier for this particular Module, within the Fabric Interconnect. | [optional] [readonly] 
**oper_state** | **str** | This field is used to indicate this fan module&#39;s operational state. | [optional] [readonly] 
**part_number** | **str** | This field identifies the Part Number for this Fan Module. | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the fan module. | [optional] [readonly] 
**presence** | **str** | This field is used to indicate this fan module&#39;s presence. | [optional] [readonly] 
**sku** | **str** | This field identifies the Stockkeeping Unit for this Fan Module. | [optional] [readonly] 
**tray_id** | **int** | Tray identifier for the fan module. | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for this Fan Module. | [optional] [readonly] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**equipment_chassis** | [**EquipmentChassisRelationship**](EquipmentChassisRelationship.md) |  | [optional] 
**equipment_rack_enclosure** | [**EquipmentRackEnclosureRelationship**](EquipmentRackEnclosureRelationship.md) |  | [optional] 
**fans** | [**[EquipmentFanRelationship], none_type**](EquipmentFanRelationship.md) | An array of relationships to equipmentFan resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**network_element** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


