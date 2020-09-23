# VnicEthNetworkPolicyAllOf

Definition of the list of properties defined in 'vnic.EthNetworkPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_platform** | **str** | The platform for which the server profile is applicable. It can either be a server that is operating in standalone mode or which is attached to a Fabric Interconnect managed by Intersight. | [optional]  if omitted the server will use the default value of "Standalone"
**vlan_settings** | [**VnicVlanSettings**](VnicVlanSettings.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


