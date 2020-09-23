# StorageBaseArrayDisk

Common attributes of a storage array disk.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**name** | **str** | Disk name available in storage array. | [optional] [readonly] 
**part_number** | **str** | Storage disk part number. | [optional] [readonly] 
**protocol** | **str** | Storage protocol used in disk for communication. Possible values are SAS, SATA and NVMe. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**speed** | **int** | Disk speed for read or write operation measured in rpm. | [optional] [readonly] 
**status** | **str** | Storage disk health status. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**storage_utilization** | [**StorageBaseCapacity**](StorageBaseCapacity.md) |  | [optional] 
**type** | **str** | Storage disk type - it can be SSD, HDD, NVRAM. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**version** | **str** | Storage disk version number. | [optional] [readonly] 
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
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


