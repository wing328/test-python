# HyperflexSoftwareVersionPolicyAllOf

Definition of the list of properties defined in 'hyperflex.SoftwareVersionPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hxdp_version** | **str** | Desired HyperFlex Data Platform software version to apply on the HyperFlex cluster. | [optional] 
**hypervisor_version** | **str** | Desired  hypervisor version to apply for all the nodes on the HyperFlex cluster. | [optional] 
**server_firmware_version** | **str** | Desired server firmware version to apply on the HyperFlex Cluster. | [optional] 
**upgrade_types** | **[str]** |  | [optional] 
**cluster_profiles** | [**[HyperflexClusterProfileRelationship], none_type**](HyperflexClusterProfileRelationship.md) | An array of relationships to hyperflexClusterProfile resources. | [optional] 
**hxdp_version_info** | [**SoftwareHyperflexDistributableRelationship**](SoftwareHyperflexDistributableRelationship.md) |  | [optional] 
**hypervisor_version_info** | [**SoftwareHyperflexDistributableRelationship**](SoftwareHyperflexDistributableRelationship.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**server_firmware_version_info** | [**FirmwareDistributableRelationship**](FirmwareDistributableRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


