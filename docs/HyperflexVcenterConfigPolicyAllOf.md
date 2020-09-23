# HyperflexVcenterConfigPolicyAllOf

Definition of the list of properties defined in 'hyperflex.VcenterConfigPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_center** | **str** | The vCenter datacenter name. | [optional] 
**hostname** | **str** | The vCenter server FQDN or IP. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**password** | **str** | The password for authenticating with vCenter. Follow the corresponding password policy governed by vCenter. | [optional] 
**sso_url** | **str** | Overrides the default vCenter Single Sign-On URL. Do not specify unless instructed by Cisco TAC. | [optional] 
**username** | **str** | The vCenter username (e.g. administrator@vsphere.local). | [optional] 
**cluster_profiles** | [**[HyperflexClusterProfileRelationship], none_type**](HyperflexClusterProfileRelationship.md) | An array of relationships to hyperflexClusterProfile resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


