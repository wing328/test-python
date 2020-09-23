# VirtualizationVmwareHostRelationship

A relationship to the 'virtualization.VmwareHost' resource, or the expanded 'virtualization.VmwareHost' resource, or the 'null' value.
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
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
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
**boot_time** | **datetime** | The time when this host booted up. | [optional] 
**connection_state** | **str** | Indicates if the host is connected to the vCenter. Values are connected, not connected. | [optional] 
**hw_power_state** | **str** | Is the host Powered-up or Powered-down. | [optional]  if omitted the server will use the default value of "Unknown"
**network_adapter_count** | **int** | The count of all network adapters attached to this host. | [optional] 
**resource_consumed** | [**VirtualizationVmwareResourceConsumption**](VirtualizationVmwareResourceConsumption.md) |  | [optional] 
**storage_adapter_count** | **int** | The count of all storage adapters attached to this host. | [optional] 
**vcenter_host_id** | **str** | The identity of this host within vCenter (optional). | [optional] 
**cluster** | [**VirtualizationVmwareClusterRelationship**](VirtualizationVmwareClusterRelationship.md) |  | [optional] 
**datacenter** | [**VirtualizationVmwareDatacenterRelationship**](VirtualizationVmwareDatacenterRelationship.md) |  | [optional] 
**datastores** | [**[VirtualizationVmwareDatastoreRelationship], none_type**](VirtualizationVmwareDatastoreRelationship.md) | An array of relationships to virtualizationVmwareDatastore resources. | [optional] [readonly] 
**selector** | **str** | An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of &#39;moid&#39; by clients. 1. If &#39;moid&#39; is set this field is ignored. 1. If &#39;selector&#39; is set and &#39;moid&#39; is empty/absent from the request, Intersight determines the Moid of the resource matching the filter expression and populates it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq &#39;3AA8B7T11&#39;. | [optional] [readonly] 
**link** | **str** | A URL to an instance of the &#39;mo.MoRef&#39; class. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


