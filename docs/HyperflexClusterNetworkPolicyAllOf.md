# HyperflexClusterNetworkPolicyAllOf

Definition of the list of properties defined in 'hyperflex.ClusterNetworkPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jumbo_frame** | **bool** | Enable or disable jumbo frames. | [optional] 
**kvm_ip_range** | [**HyperflexIpAddrRange**](HyperflexIpAddrRange.md) |  | [optional] 
**mac_prefix_range** | [**HyperflexMacAddrPrefixRange**](HyperflexMacAddrPrefixRange.md) |  | [optional] 
**mgmt_vlan** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**uplink_speed** | **str** | Link speed of the server adapter port to the upstream switch. When the policy is attached to a cluster profile with EDGE management platform, the uplink speed can be &#39;1G&#39; or &#39;10G+&#39;. Use &#39;10G+&#39; for link speeds of 10G or above. When the policy is attached to a cluster profile with Fabric Interconnect management platform, the uplink speed can be &#39;default&#39; only. | [optional]  if omitted the server will use the default value of "default"
**vm_migration_vlan** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**vm_network_vlans** | [**[HyperflexNamedVlan]**](HyperflexNamedVlan.md) |  | [optional] 
**cluster_profiles** | [**[HyperflexClusterProfileRelationship], none_type**](HyperflexClusterProfileRelationship.md) | An array of relationships to hyperflexClusterProfile resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


