# HyperflexProxySettingPolicyAllOf

Definition of the list of properties defined in 'hyperflex.ProxySettingPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | HTTP Proxy server FQDN or IP. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**password** | **str** | The password for the HTTP Proxy. | [optional] 
**port** | **int** | The HTTP Proxy port number. The port number of the HTTP proxy must be between 1 and 65535, inclusive. | [optional] 
**username** | **str** | The username for the HTTP Proxy. | [optional] 
**cluster_profiles** | [**[HyperflexClusterProfileRelationship], none_type**](HyperflexClusterProfileRelationship.md) | An array of relationships to hyperflexClusterProfile resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


