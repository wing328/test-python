# FabricEthNetworkControlPolicyAllOf

Definition of the list of properties defined in 'fabric.EthNetworkControlPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_enabled** | **bool** | Enables the CDP on an interface. | [optional] 
**forge_mac** | **str** | Determines if the MAC forging is allowed or denied on an interface. | [optional]  if omitted the server will use the default value of "allow"
**lldp_settings** | [**FabricLldpSettings**](FabricLldpSettings.md) |  | [optional] 
**mac_registration_mode** | **str** | Determines the MAC addresses that have to be registered with the switch. | [optional]  if omitted the server will use the default value of "nativeVlanOnly"
**uplink_fail_action** | **str** | Determines the state of the virtual interface (vethernet / vfc) on the switch when a suitable uplink is not pinned. | [optional]  if omitted the server will use the default value of "linkDown"
**network_policy** | [**[VnicEthNetworkPolicyRelationship], none_type**](VnicEthNetworkPolicyRelationship.md) | An array of relationships to vnicEthNetworkPolicy resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


