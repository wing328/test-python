# PortSubGroupAllOf

Definition of the list of properties defined in 'port.SubGroup', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport** | **str** | Type of port sub-group. Values are Eth or Fc. | [optional] [readonly] 
**ethernet_ports** | [**[EtherPhysicalPortRelationship], none_type**](EtherPhysicalPortRelationship.md) | An array of relationships to etherPhysicalPort resources. | [optional] [readonly] 
**fc_ports** | [**[FcPhysicalPortRelationship], none_type**](FcPhysicalPortRelationship.md) | An array of relationships to fcPhysicalPort resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**port_group** | [**PortGroupRelationship**](PortGroupRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


