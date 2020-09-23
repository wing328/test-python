# HyperflexSysConfigPolicyAllOf

Definition of the list of properties defined in 'hyperflex.SysConfigPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_domain_name** | **str** | The DNS Search Domain Name. This setting applies to HyperFlex Data Platform 3.0 or later only. | [optional] 
**dns_servers** | **[str]** |  | [optional] 
**ntp_servers** | **[str]** |  | [optional] 
**timezone** | **str** | The timezone of the HyperFlex cluster&#39;s system clock. | [optional]  if omitted the server will use the default value of "Pacific/Niue"
**cluster_profiles** | [**[HyperflexClusterProfileRelationship], none_type**](HyperflexClusterProfileRelationship.md) | An array of relationships to hyperflexClusterProfile resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


