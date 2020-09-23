# EquipmentSwitchCardAllOf

Definition of the list of properties defined in 'equipment.SwitchCard', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Detailed description of this switch hardware. | [optional] [readonly] 
**num_ports** | **int** | Number of ports present in this switch hardware. | [optional] [readonly] 
**out_of_band_ip_address** | **str** | Field specifies this Switch&#39;s Out-of-band IP address. | [optional] [readonly] 
**out_of_band_ip_gateway** | **str** | Field specifies this Switch&#39;s default gateway for the out-of-band management interface. | [optional] [readonly] 
**presence** | **str** | Presence for this switch hardware. | [optional] [readonly] 
**slot_id** | **int** | Slot identifier of the local Switch slot Interface. | [optional] [readonly] 
**state** | **str** | Operational state of the switch hardware. | [optional] [readonly] 
**switch_id** | **str** | Switch Identifier that is local to a cluster. | [optional] [readonly] 
**fc_port_channels** | [**[FcPortChannelRelationship], none_type**](FcPortChannelRelationship.md) | An array of relationships to fcPortChannel resources. | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**network_element** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 
**port_channels** | [**[EtherPortChannelRelationship], none_type**](EtherPortChannelRelationship.md) | An array of relationships to etherPortChannel resources. | [optional] 
**port_groups** | [**[PortGroupRelationship], none_type**](PortGroupRelationship.md) | An array of relationships to portGroup resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


