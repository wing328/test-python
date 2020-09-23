# HyperflexClusterStoragePolicyAllOf

Definition of the list of properties defined in 'hyperflex.ClusterStoragePolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_partition_cleanup** | **bool** | If enabled, formats existing disk partitions (destroys all user data). | [optional] 
**logical_avalability_zone_config** | [**HyperflexLogicalAvailabilityZone**](HyperflexLogicalAvailabilityZone.md) |  | [optional] 
**vdi_optimization** | **bool** | Enable or disable VDI optimization (hybrid HyperFlex systems only). | [optional] 
**cluster_profiles** | [**[HyperflexClusterProfileRelationship], none_type**](HyperflexClusterProfileRelationship.md) | An array of relationships to hyperflexClusterProfile resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


