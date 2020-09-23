# FabricVsanAllOf

Definition of the list of properties defined in 'fabric.Vsan', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_zoning** | **str** | Enables or Disables the default zoning state. | [optional]  if omitted the server will use the default value of "Enabled"
**fc_zone_sharing_mode** | **str** | Logical grouping mode for fc ports. | [optional] 
**fcoe_vlan** | **int** | FCOE Vlan associated to the VSAN configuration. | [optional] 
**name** | **str** | User given name for the VSAN configuration. | [optional] 
**vsan_id** | **int** | Virtual San Identifier in the switch. | [optional] 
**fc_network_policy** | [**FabricFcNetworkPolicyRelationship**](FabricFcNetworkPolicyRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


