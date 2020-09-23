# VnicFcIfAllOf

Definition of the list of properties defined in 'vnic.FcIf', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the virtual fibre channel interface. | [optional] 
**order** | **int** | The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two. | [optional] 
**persistent_bindings** | **bool** | Enables retention of LUN ID associations in memory until they are manually cleared. | [optional] 
**placement** | [**VnicPlacementSettings**](VnicPlacementSettings.md) |  | [optional] 
**type** | **str** | VHBA Type configuration for SAN Connectivity Policy. This configuration is supported only on Cisco VIC 14XX series and higher series of adapters. | [optional]  if omitted the server will use the default value of "fc-initiator"
**vif_id** | **int** | This should be the same as the channel number of the vfc created on switch in order to set up the data path. The property is applicable only for FI attached servers where a vfc is created on the switch for every vHBA. | [optional] [readonly] 
**wwpn** | **str** | The WWPN address that is assigned to the vhba based on the wwn pool that has been assigned to the SAN Connectivity Policy. | [optional] [readonly] 
**fc_adapter_policy** | [**VnicFcAdapterPolicyRelationship**](VnicFcAdapterPolicyRelationship.md) |  | [optional] 
**fc_network_policy** | [**VnicFcNetworkPolicyRelationship**](VnicFcNetworkPolicyRelationship.md) |  | [optional] 
**fc_qos_policy** | [**VnicFcQosPolicyRelationship**](VnicFcQosPolicyRelationship.md) |  | [optional] 
**profile** | [**PolicyAbstractConfigProfileRelationship**](PolicyAbstractConfigProfileRelationship.md) |  | [optional] 
**san_connectivity_policy** | [**VnicSanConnectivityPolicyRelationship**](VnicSanConnectivityPolicyRelationship.md) |  | [optional] 
**scp_vhba** | [**VnicFcIfRelationship**](VnicFcIfRelationship.md) |  | [optional] 
**sp_vhbas** | [**[VnicFcIfRelationship], none_type**](VnicFcIfRelationship.md) | An array of relationships to vnicFcIf resources. | [optional] 
**wwpn_lease** | [**FcpoolLeaseRelationship**](FcpoolLeaseRelationship.md) |  | [optional] 
**wwpn_pool** | [**FcpoolPoolRelationship**](FcpoolPoolRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


