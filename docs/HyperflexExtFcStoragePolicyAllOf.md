# HyperflexExtFcStoragePolicyAllOf

Definition of the list of properties defined in 'hyperflex.ExtFcStoragePolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_state** | **bool** | Enables or disables external FC storage configuration. | [optional] 
**exta_traffic** | [**HyperflexNamedVsan**](HyperflexNamedVsan.md) |  | [optional] 
**extb_traffic** | [**HyperflexNamedVsan**](HyperflexNamedVsan.md) |  | [optional] 
**wwxn_prefix_range** | [**HyperflexWwxnPrefixRange**](HyperflexWwxnPrefixRange.md) |  | [optional] 
**cluster_profiles** | [**[HyperflexClusterProfileRelationship], none_type**](HyperflexClusterProfileRelationship.md) | An array of relationships to hyperflexClusterProfile resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


