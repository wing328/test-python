# HclHyperflexSoftwareCompatibilityInfoAllOf

Definition of the list of properties defined in 'hcl.HyperflexSoftwareCompatibilityInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**[HclConstraint]**](HclConstraint.md) |  | [optional] 
**hxdp_version** | **str** | HXDP component software version. | [optional] 
**hypervisor_type** | **str** | Type fo Hypervisor the HyperFlex components versions are compatible with. For example ESX, Hyperv or KVM. | [optional]  if omitted the server will use the default value of "ESXi"
**hypervisor_version** | **str** | Hypervisor component software version. | [optional] 
**server_fw_version** | **str** | UCS Server Firmware component software version. | [optional] 
**app_catalog** | [**HyperflexAppCatalogRelationship**](HyperflexAppCatalogRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


