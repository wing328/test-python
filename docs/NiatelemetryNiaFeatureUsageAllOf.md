# NiatelemetryNiaFeatureUsageAllOf

Definition of the list of properties defined in 'niatelemetry.NiaFeatureUsage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apic_count** | **int** | Number of APIC controllers. This determines the value of controllers for the fabric. | [optional] 
**app_center_count** | **int** | ACI APPs feature usage. This determines the total number of apps installed on the fabric. | [optional] 
**ave** | **str** | AVE feature usage. This determines if ACI virtual edge feature is enabled or disabled. | [optional] 
**bd_count** | **int** | Number of BDs. This determines the total number of Broadcast Domains across the fabric. | [optional] 
**consistency_checker_app** | **str** | Consistency checker application usage. This determines if the fabric has Consistency checker application installed. | [optional] 
**contract_count** | **int** | Number of contracts. This determines the total number of Contracts configured across the fabric. | [optional] 
**dns_count** | **int** | DNS feature usage. This determines the total number of DNS configurations across the fabric. | [optional] 
**eigrp_count** | **int** | Eigrp feature usage. This determines the total number of EIGRP sessions across the fabric. | [optional] 
**epg_count** | **int** | Number of EPGs. This determines the total number of End Point Groups across the fabric. | [optional] 
**hsrp_count** | **int** | Hsrp feature usage. This determines the total number of HSRP sessions across the fabric. | [optional] 
**ibgp_count** | **int** | Ibgp feature usage. This determines the total number of BGP sessions across the fabric. | [optional] 
**igmp_access_list_count** | **int** | IGMP Access List feature usage. This determines the total number of IGMP access lists configured across the fabric. | [optional] 
**igmp_snoop** | **str** | IGMP Snooping feature usage. This determines if this feature is enabled or disabled. | [optional] 
**ip_epg_count** | **int** | Number of IP based EPGs. This determines the total number of IP End Point Groups across the fabric. | [optional] 
**isis_count** | **int** | Isis feature usage. TThis determines the total number of ISIS sessions across the fabric. | [optional] 
**l2_multicast** | **str** | L2Multicast feature usage. This determines if this Layer 2 Multicast feature is being enabled / disabled on the fabric. | [optional] 
**leaf_count** | **int** | Number of Leafs. This determines the total number of Leaf switches in the fabric. | [optional] 
**maintenance_mode_count** | **int** | Maintenance Mode feature usage. This determines the number of switches that are currently in maintenance mode. | [optional] 
**management_over_v6_count** | **int** | Management over IPv6 feature usage. This determines the total number of IPv6 configurtaions in the fabric. | [optional] 
**nir** | **str** | NIR application usage. This determines if the fabric has NIR application installed. | [optional] 
**opflex_kubernetes_count** | **int** | Opflex for Kubernetes feature usage. This determines the total number of VMM sessions of type kubernetes. | [optional] 
**ospf_count** | **int** | Ospf feature usage. This determines the total number of OSPF sessions across the fabric. | [optional] 
**poe_count** | **int** | POE feature usage. This determines the total number of POE configurations across the fabric. | [optional] 
**qin_vni_tunnel_count** | **int** | QinVniTunnel feature usage. This determines if the qinVniTunnel feature is being used on the fabric and the scale of it. | [optional] 
**remote_leaf_count** | **int** | Number of remote Leafs. This determines if this feature is being enabled or disabled. | [optional] 
**scvmm_count** | **int** | SCVMM feature usage. This determines the total number of SCVMM configurations in the fabric. | [optional] 
**shared_l3_out_count** | **int** | SharedL3Out feature usage. This determines the total number of Shared L3 out configured across the fabric. | [optional] 
**smart_call_home** | **str** | Smart callhome feature usage. This determines if this feature is being enabled or disabled. | [optional] 
**snmp** | **str** | SNMP feature usage. This determines if this feature is enabled or disabled. | [optional] 
**spine_count** | **int** | Number of Spines. This determines the total number of spine switches in the fabric. | [optional] 
**ssh_over_v6_count** | **int** | Ssh over IPv6 feature usage. This determines the total number of IPv6 configurtaions in the fabric. | [optional] 
**syslog_over_v6_count** | **int** | Syslog over IPv6 feature usage. This determines the total number of IPv6 configurtaions in the fabric. | [optional] 
**tenant_count** | **int** | Number of tenants. This determines the total number of tenants configured across the fabric. | [optional] 
**tier_two_leaf_count** | **int** | Number of tier 2 Leafs. This determines the total number of tier 2 Leaf switches in the fabric. | [optional] 
**twamp** | **str** | TWAMP feature usage. This determines if this feature is enabled or disabled. | [optional] 
**useg** | **str** | VMM uSegmentation feature usage. This determines if microsegmentation feature is enabled or disabled. | [optional] 
**vpod_count** | **int** | Virtual pod feature usage. This determines the total number of virtual POD configurations in the fabrics. | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

