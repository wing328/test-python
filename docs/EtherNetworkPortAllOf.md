# EtherNetworkPortAllOf

Definition of the list of properties defined in 'ether.NetworkPort', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_id** | **int** | Febric extender identifier for this port. | [optional] 
**peer_dn** | **str** | Peer DN for network host port of fabric extender. | [optional] 
**port_id** | **int** | Switch physical port identifier. | [optional] 
**slot_id** | **int** | Switch expansion slot module identifier. | [optional] 
**speed** | **str** | Network Port Speed of IO card or fabric extender. | [optional] [readonly] 
**switch_id** | **str** | Switch Identifier that is local to a cluster. | [optional] 
**equipment_io_card_base** | [**EquipmentIoCardBaseRelationship**](EquipmentIoCardBaseRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


