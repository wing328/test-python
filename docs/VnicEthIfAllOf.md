# VnicEthIfAllOf

Definition of the list of properties defined in 'vnic.EthIf', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdn** | [**VnicCdn**](VnicCdn.md) |  | [optional] 
**failover_enabled** | **bool** | Setting this to true esnures that the traffic failsover from one uplink to another auotmatically in case of an uplink failure. It is applicable for Cisco VIC adapters only which are connected to Fabric Interconnect cluster. The uplink if specified determines the primary uplink in case of a failover. | [optional] 
**mac_address** | **str** | The MAC address that is assigned to the vnic based on the MAC pool that has been assigned to the LAN Connectivity Policy. | [optional] [readonly] 
**name** | **str** | Name of the virtual ethernet interface. | [optional] 
**order** | **int** | The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two. | [optional] 
**placement** | [**VnicPlacementSettings**](VnicPlacementSettings.md) |  | [optional] 
**standby_vif_id** | **int** | The Standby VIF Id is applicable for failover enabled vNICS. It should be the same as the channel number of the standby vethernet created on switch in order to set up the standby data path. | [optional] [readonly] 
**usnic_settings** | [**VnicUsnicSettings**](VnicUsnicSettings.md) |  | [optional] 
**vif_id** | **int** | The Vif Id should be same as the channel number of the vethernet created on switch in order to set up the data path. The property is applicable only for FI attached servers where a vethernet is created on the switch for every vNIC. | [optional] [readonly] 
**vmq_settings** | [**VnicVmqSettings**](VnicVmqSettings.md) |  | [optional] 
**eth_adapter_policy** | [**VnicEthAdapterPolicyRelationship**](VnicEthAdapterPolicyRelationship.md) |  | [optional] 
**eth_network_policy** | [**VnicEthNetworkPolicyRelationship**](VnicEthNetworkPolicyRelationship.md) |  | [optional] 
**eth_qos_policy** | [**VnicEthQosPolicyRelationship**](VnicEthQosPolicyRelationship.md) |  | [optional] 
**lan_connectivity_policy** | [**VnicLanConnectivityPolicyRelationship**](VnicLanConnectivityPolicyRelationship.md) |  | [optional] 
**lcp_vnic** | [**VnicEthIfRelationship**](VnicEthIfRelationship.md) |  | [optional] 
**mac_lease** | [**MacpoolLeaseRelationship**](MacpoolLeaseRelationship.md) |  | [optional] 
**mac_pool** | [**MacpoolPoolRelationship**](MacpoolPoolRelationship.md) |  | [optional] 
**profile** | [**PolicyAbstractConfigProfileRelationship**](PolicyAbstractConfigProfileRelationship.md) |  | [optional] 
**sp_vnics** | [**[VnicEthIfRelationship], none_type**](VnicEthIfRelationship.md) | An array of relationships to vnicEthIf resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


