# HyperflexClusterProfileAllOf

Definition of the list of properties defined in 'hyperflex.ClusterProfile', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ip_address** | **str** | The storage data IP address for the HyperFlex cluster. | [optional] 
**hypervisor_type** | **str** | The hypervisor type for the HyperFlex cluster. | [optional]  if omitted the server will use the default value of "ESXi"
**mac_address_prefix** | **str** | The MAC address prefix in the form of 00:25:B5:XX. | [optional] 
**mgmt_ip_address** | **str** | The management IP address for the HyperFlex cluster. | [optional] 
**mgmt_platform** | **str** | The management platform for the HyperFlex cluster. | [optional]  if omitted the server will use the default value of "FI"
**replication** | **int** | The number of copies of each data block written. | [optional] 
**storage_data_vlan** | [**HyperflexNamedVlan**](HyperflexNamedVlan.md) |  | [optional] 
**wwxn_prefix** | **str** | The WWxN prefix in the form of 20:00:00:25:B5:XX. | [optional] 
**associated_cluster** | [**HyperflexClusterRelationship**](HyperflexClusterRelationship.md) |  | [optional] 
**auto_support** | [**HyperflexAutoSupportPolicyRelationship**](HyperflexAutoSupportPolicyRelationship.md) |  | [optional] 
**cluster_network** | [**HyperflexClusterNetworkPolicyRelationship**](HyperflexClusterNetworkPolicyRelationship.md) |  | [optional] 
**cluster_storage** | [**HyperflexClusterStoragePolicyRelationship**](HyperflexClusterStoragePolicyRelationship.md) |  | [optional] 
**config_result** | [**HyperflexConfigResultRelationship**](HyperflexConfigResultRelationship.md) |  | [optional] 
**ext_fc_storage** | [**HyperflexExtFcStoragePolicyRelationship**](HyperflexExtFcStoragePolicyRelationship.md) |  | [optional] 
**ext_iscsi_storage** | [**HyperflexExtIscsiStoragePolicyRelationship**](HyperflexExtIscsiStoragePolicyRelationship.md) |  | [optional] 
**local_credential** | [**HyperflexLocalCredentialPolicyRelationship**](HyperflexLocalCredentialPolicyRelationship.md) |  | [optional] 
**node_config** | [**HyperflexNodeConfigPolicyRelationship**](HyperflexNodeConfigPolicyRelationship.md) |  | [optional] 
**node_profile_config** | [**[HyperflexNodeProfileRelationship], none_type**](HyperflexNodeProfileRelationship.md) | An array of relationships to hyperflexNodeProfile resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**proxy_setting** | [**HyperflexProxySettingPolicyRelationship**](HyperflexProxySettingPolicyRelationship.md) |  | [optional] 
**running_workflows** | [**[WorkflowWorkflowInfoRelationship], none_type**](WorkflowWorkflowInfoRelationship.md) | An array of relationships to workflowWorkflowInfo resources. | [optional] [readonly] 
**software_version** | [**HyperflexSoftwareVersionPolicyRelationship**](HyperflexSoftwareVersionPolicyRelationship.md) |  | [optional] 
**sys_config** | [**HyperflexSysConfigPolicyRelationship**](HyperflexSysConfigPolicyRelationship.md) |  | [optional] 
**ucsm_config** | [**HyperflexUcsmConfigPolicyRelationship**](HyperflexUcsmConfigPolicyRelationship.md) |  | [optional] 
**vcenter_config** | [**HyperflexVcenterConfigPolicyRelationship**](HyperflexVcenterConfigPolicyRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


