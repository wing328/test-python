# ComputePhysicalRelationship

A relationship to the 'compute.Physical' resource, or the expanded 'compute.Physical' resource, or the 'null' value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] defaults to nulltype.Null
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
**device_mo_id** | **str** | The database identifier of the registered device of an object. | [optional] [readonly] 
**dn** | **str** | The Distinguished Name unambiguously identifies an object in the system. | [optional] [readonly] 
**rn** | **str** | The Relative Name uniquely identifies an object within a given context. | [optional] [readonly] 
**model** | **str** | This field identifies the model of the given component. | [optional] [readonly] 
**revision** | **str** | This field identifies the revision of the given component. | [optional] [readonly] 
**serial** | **str** | This field identifies the serial of the given component. | [optional] [readonly] 
**vendor** | **str** | This field identifies the vendor of the given component. | [optional] [readonly] 
**admin_power_state** | **str** | The desired power state of the server. | [optional] [readonly] 
**asset_tag** | **str** | The user defined asset tag assigned to the server. | [optional] [readonly] 
**available_memory** | **int** | The amount of memory available on the server. | [optional] [readonly] 
**bios_post_complete** | **bool** | The BIOS POST completion status of the server. | [optional] 
**fault_summary** | **int** | The fault summary for the server. | [optional] 
**kvm_ip_addresses** | [**[ComputeIpAddress]**](ComputeIpAddress.md) |  | [optional] 
**management_mode** | **str** | The management mode of the server. | [optional]  if omitted the server will use the default value of "IntersightStandalone"
**memory_speed** | **str** | The maximum memory speed in MHz available on the server. | [optional] [readonly] 
**mgmt_ip_address** | **str** | Management address of the server. | [optional] 
**num_adaptors** | **int** | The total number of network adapters present on the server. | [optional] [readonly] 
**num_cpu_cores** | **int** | The total number of CPU cores present on the server. | [optional] [readonly] 
**num_cpu_cores_enabled** | **int** | The total number of CPU cores enabled on the server. | [optional] [readonly] 
**num_cpus** | **int** | The total number of CPUs present on the server. | [optional] [readonly] 
**num_eth_host_interfaces** | **int** | The total number of vNICs which are visible to a host on the server. | [optional] [readonly] 
**num_fc_host_interfaces** | **int** | The total number of vHBAs which are visible to a host on the server. | [optional] [readonly] 
**num_threads** | **int** | The total number of threads the server is capable of handling. | [optional] [readonly] 
**oper_power_state** | **str** | The actual power state of the server. | [optional] [readonly] 
**oper_state** | **str** | The operational state of the server. | [optional] [readonly] 
**operability** | **str** | The operability of the server. | [optional] [readonly] 
**platform_type** | **str** | The platform type of the registered device - whether managed by UCSM or operating in standalone mode. | [optional] 
**presence** | **str** | Indicates if a server is present in a slot and is applicable for blade servers. | [optional] [readonly] 
**service_profile** | **str** | The distinguished name of the service profile to which the server is associated to. It is applicable only for servers which are managed via UCSM. | [optional] [readonly] 
**total_memory** | **int** | The total memory available on the server. | [optional] [readonly] 
**user_label** | **str** | The user defined label assigned to the server. | [optional] [readonly] 
**uuid** | **str** | The universally unique identity of the server. | [optional] [readonly] 
**mgmt_identity** | [**EquipmentPhysicalIdentityRelationship**](EquipmentPhysicalIdentityRelationship.md) |  | [optional] 
**selector** | **str** | An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of &#39;moid&#39; by clients. 1. If &#39;moid&#39; is set this field is ignored. 1. If &#39;selector&#39; is set and &#39;moid&#39; is empty/absent from the request, Intersight determines the Moid of the resource matching the filter expression and populates it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq &#39;3AA8B7T11&#39;. | [optional] [readonly] 
**link** | **str** | A URL to an instance of the &#39;mo.MoRef&#39; class. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


