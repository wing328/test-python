# VirtualizationBaseHost

Common attributes of any host associated to a hypervisor manager. Serves as a base class for all concrete host types A Host belongs to a datacenter and optionally to a cluster, and runs virtual machines on it. A host is basically a hardware platform that runs the VMs. Depending on the capacity of the host, it can support 100s of virtual machines.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**cpu_info** | [**VirtualizationCpuInfo**](VirtualizationCpuInfo.md) |  | [optional] 
**hardware_info** | [**InfraHardwareInfo**](InfraHardwareInfo.md) |  | [optional] 
**hypervisor_type** | **str** | Identifies the broad type of the underlying hypervisor. | [optional]  if omitted the server will use the default value of "Unknown"
**identity** | **str** | The internally generated identity of this host. This entity is not manipulated by users. It aids in uniquely identifying the datacenter object. For VMware, this is an MOR (managed object reference). | [optional] 
**maintenance_mode** | **bool** | Is this host in maintenance mode. Set to true or false. | [optional] 
**memory_capacity** | [**VirtualizationMemoryCapacity**](VirtualizationMemoryCapacity.md) |  | [optional] 
**model** | **str** | Commercial model information about this hardware. | [optional] 
**name** | **str** | Name of this host supplied by user. It is not the identity of the host. The name is subject to user manipulations. | [optional] 
**processor_capacity** | [**VirtualizationComputeCapacity**](VirtualizationComputeCapacity.md) |  | [optional] 
**product_info** | [**VirtualizationProductInfo**](VirtualizationProductInfo.md) |  | [optional] 
**serial** | **str** | Serial number of this host (internally generated). | [optional] 
**status** | **str** | Host health status, as reported by the hypervisor platform. | [optional]  if omitted the server will use the default value of "Unknown"
**up_time** | **str** | The uptime of the host, stored as Duration (from w3c). | [optional] 
**uuid** | **str** | Universally unique identity of this host (example b3d4483b-5560-9342-8309-b486c9236610). Internally generated. | [optional] 
**vendor** | **str** | Commercial vendor details of this hardware. | [optional] 
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
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


