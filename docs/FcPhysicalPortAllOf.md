# FcPhysicalPortAllOf

Definition of the list of properties defined in 'fc.PhysicalPort', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_speed** | **str** | Administrator configured Speed applied on the port. | [optional] [readonly] 
**admin_state** | **str** | Administratively configured state (enabled/disabled) for this port. | [optional] [readonly] 
**b2b_credit** | **int** | Buffer to Buffer credits of FC port. | [optional] [readonly] 
**max_speed** | **str** | Maximum Speed with which the port operates. | [optional] [readonly] 
**mode** | **str** | Mode information N_proxy, F or E associated to the Fibre Channel port. | [optional] [readonly] 
**oper_speed** | **str** | Operational Speed with which the port operates. | [optional] [readonly] 
**peer_dn** | **str** | PeerDn for fibre channel physical port. | [optional] [readonly] 
**port_channel_id** | **int** | Port channel id of FC port channel created on FI switch. | [optional] [readonly] 
**transceiver_type** | **str** | Transceiver type of a Fibre Channel port. | [optional] [readonly] 
**vsan** | **int** | Virtual San that is associated to the port. | [optional] [readonly] 
**wwn** | **str** | World Wide Name of a Fibre Channel port. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**port_group** | [**PortGroupRelationship**](PortGroupRelationship.md) |  | [optional] 
**port_sub_group** | [**PortSubGroupRelationship**](PortSubGroupRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


