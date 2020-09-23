# HyperflexCluster

A HyperFlex cluster. Contains inventory information concerning the health, software versions, storage, and nodes of the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**capacity_runway** | **int** | The number of days remaining before the cluster&#39;s storage utilization reaches the recommended capacity limit of 76%. Default value is math.MaxInt32 to indicate that the capacity runway is \&quot;Unknown\&quot; for a cluster that is not connected or with not sufficient data. | [optional] [readonly] 
**cluster_name** | **str** | The name of this HyperFlex cluster. | [optional] [readonly] 
**cluster_type** | **int** | The storage type of this cluster (All Flash or Hybrid). | [optional] [readonly] 
**cluster_uuid** | **str** | The unique identifier for this HyperFlex cluster. | [optional] [readonly] 
**compute_node_count** | **int** | The number of compute nodes that belong to this cluster. | [optional] [readonly] 
**converged_node_count** | **int** | The number of converged nodes that belong to this cluster. | [optional] [readonly] 
**deployment_type** | **str** | The deployment type of the HyperFlex cluster. The cluster can have one of the following configurations: 1. Datacenter: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes on a single site. 2. Stretched Cluster: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes distributed across multiple sites. 3. Edge: The HyperFlex cluster consists of 2-4 standalone nodes. If the cluster is running a HyperFlex Data Platform version less than 4.0 or if the deployment type cannot be determined, the deployment type is set as &#39;NA&#39; (not available). | [optional] [readonly]  if omitted the server will use the default value of "NA"
**device_id** | **str** | The unique identifier of the device registration that represents this HyperFlex cluster&#39;s connection to Intersight. | [optional] [readonly] 
**flt_aggr** | **int** | The number of yellow (warning) and red (critical) alarms stored as an aggregate. The first 16 bits indicate the number of red alarms, and the last 16 bits contain the number of yellow alarms. | [optional] [readonly] 
**hx_version** | **str** | The HyperFlex Data Platform version of this cluster. | [optional] [readonly] 
**hxdp_build_version** | **str** | The version and build number of the HyperFlex Data Platform for this cluster. After a cluster upgrade, this version string will be updated on the next inventory cycle to reflect the newly installed version. | [optional] [readonly] 
**hypervisor_type** | **str** | The type of hypervisor running on this cluster. | [optional] [readonly]  if omitted the server will use the default value of "ESXi"
**hypervisor_version** | **str** | The version of hypervisor running on this cluster. | [optional] [readonly] 
**summary** | [**HyperflexSummary**](HyperflexSummary.md) |  | [optional] 
**utilization_percentage** | **float** | The storage utilization percentage is computed based on total capacity and current capacity utilization. | [optional] [readonly] 
**utilization_trend_percentage** | **float** | The storage utilization trend percentage represents the trend in percentage computed using the first and last point from historical data. | [optional] [readonly] 
**vm_count** | **int** | The number of virtual machines present on this cluster. | [optional] [readonly] 
**alarm** | [**[HyperflexAlarmRelationship], none_type**](HyperflexAlarmRelationship.md) | An array of relationships to hyperflexAlarm resources. | [optional] [readonly] 
**health** | [**HyperflexHealthRelationship**](HyperflexHealthRelationship.md) |  | [optional] 
**nodes** | [**[HyperflexNodeRelationship], none_type**](HyperflexNodeRelationship.md) | An array of relationships to hyperflexNode resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**account_moid** | **str** | The Account ID for this managed object. | [optional] [readonly] 
**create_time** | **datetime** | The time when this managed object was created. | [optional] [readonly] 
**domain_group_moid** | **str** | The DomainGroup ID for this managed object. | [optional] [readonly] 
**mod_time** | **datetime** | The time when this managed object was last modified. | [optional] [readonly] 
**moid** | **str** | The unique identifier of this Managed Object instance. | [optional] 
**owners** | **[str]** |  | [optional] 
**shared_scope** | **str** | Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs. | [optional] [readonly] 
**tags** | [**[MoTag]**](MoTag.md) |  | [optional] 
**version_context** | [**MoVersionContext**](MoVersionContext.md) |  | [optional] 
**ancestors** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**parent** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**permission_resources** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**display_names** | [**DisplayNames**](DisplayNames.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


