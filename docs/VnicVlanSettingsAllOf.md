# VnicVlanSettingsAllOf

Definition of the list of properties defined in 'vnic.VlanSettings', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_vlans** | **str** | Allowed VLAN IDs of the virtual interface. | [optional] 
**default_vlan** | **int** | Native VLAN ID of the virtual interface or the corresponding vethernet on the peer Fabric Interconnect to which the virtual interface is connected. Setting the ID to 0 will not associate any native VLAN to the traffic on the virtual interface. | [optional] 
**mode** | **str** | Option to determine if the port can carry single VLAN (Access) or multiple VLANs (Trunk) traffic. | [optional]  if omitted the server will use the default value of "ACCESS"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


