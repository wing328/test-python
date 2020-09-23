# EtherPortChannelAllOf

Definition of the list of properties defined in 'ether.PortChannel', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_vlan** | **str** | Access VLANs for this port-channel, on this FI. | [optional] 
**admin_state** | **str** | Administratively configured state (enabled/disabled) for this port-channel. | [optional] 
**allowed_vlans** | **str** | Allowed VLANs on this port-channel, on this FI. | [optional] 
**mode** | **str** | Operating mode of this port-channel. | [optional] 
**native_vlan** | **str** | Native VLAN for this port-channel, on this FI. | [optional] 
**oper_speed** | **str** | Operational speed of this port-channel. | [optional] 
**oper_state** | **str** | Operational state of this port-channel. | [optional] 
**oper_state_qual** | **str** | Reason for this port-channel&#39;s Operational state. | [optional] 
**port_channel_id** | **int** | Unique identifier for this port-channel on the FI. | [optional] 
**role** | **str** | This port-channel&#39;s configured role (uplink, server, etc.). | [optional] 
**switch_id** | **str** | Switch Identifier that is local to a cluster. | [optional] 
**equipment_switch_card** | [**EquipmentSwitchCardRelationship**](EquipmentSwitchCardRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


