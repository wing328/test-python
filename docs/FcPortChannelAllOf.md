# FcPortChannelAllOf

Definition of the list of properties defined in 'fc.PortChannel', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_speed** | **str** | Administrator configured Speed applied on the port channel. | [optional] 
**admin_state** | **str** | Administratively configured state (enabled/disabled) for this portchannel. | [optional] [readonly] 
**mode** | **str** | Mode information N_proxy, F or E associated to the Fibre Channel portchannel. | [optional] 
**oper_speed** | **str** | Operational speed of this port-channel. | [optional] 
**oper_state** | **str** | Operational state of this port-channel. | [optional] 
**oper_state_qual** | **str** | Reason for this port-channel&#39;s Operational state. | [optional] 
**port_channel_id** | **int** | Unique identifier for this port-channel on the FI. | [optional] 
**role** | **str** | This port-channel&#39;s configured role (fcUplink, fcStorage, etc.). | [optional] 
**switch_id** | **str** | Switch Identifier that is local to a cluster. | [optional] 
**vsan** | **int** | Virtual San that is associated to the port-channel. | [optional] 
**equipment_switch_card** | [**EquipmentSwitchCardRelationship**](EquipmentSwitchCardRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


