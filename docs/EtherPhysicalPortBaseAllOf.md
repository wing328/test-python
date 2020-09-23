# EtherPhysicalPortBaseAllOf

Definition of the list of properties defined in 'ether.PhysicalPortBase', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | Mac Address of a port in the Fabric Interconnect. | [optional] [readonly] 
**mode** | **str** | Operating mode of this port. | [optional] [readonly] 
**oper_speed** | **str** | Current Operational speed for this port. | [optional] [readonly] 
**peer_dn** | **str** | PeerDn for ethernet physical port. | [optional] [readonly] 
**port_channel_id** | **int** | Port channel id for port channel created on FI switch. | [optional] [readonly] 
**port_type** | **str** | Defines the transport type for this port (ethernet OR fc). | [optional] [readonly] 
**transceiver_type** | **str** | Transceiver model attached to a port in the Fabric Interconnect. | [optional] [readonly] 
**acknowledged_peer_interface** | [**PortInterfaceBaseRelationship**](PortInterfaceBaseRelationship.md) |  | [optional] 
**peer_interface** | [**PortInterfaceBaseRelationship**](PortInterfaceBaseRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


