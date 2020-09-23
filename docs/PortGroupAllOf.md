# PortGroupAllOf

Definition of the list of properties defined in 'port.Group', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport** | **str** | Type of port group. Values are Eth or Fc. | [optional] [readonly] 
**equipment_shared_io_module** | [**EquipmentSharedIoModuleRelationship**](EquipmentSharedIoModuleRelationship.md) |  | [optional] 
**equipment_switch_card** | [**EquipmentSwitchCardRelationship**](EquipmentSwitchCardRelationship.md) |  | [optional] 
**ethernet_ports** | [**[EtherPhysicalPortRelationship], none_type**](EtherPhysicalPortRelationship.md) | An array of relationships to etherPhysicalPort resources. | [optional] [readonly] 
**fc_ports** | [**[FcPhysicalPortRelationship], none_type**](FcPhysicalPortRelationship.md) | An array of relationships to fcPhysicalPort resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**sub_groups** | [**[PortSubGroupRelationship], none_type**](PortSubGroupRelationship.md) | An array of relationships to portSubGroup resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


