# StorageFlexUtilPhysicalDrive

Storage Flex Util Physical Drive.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**block_size** | **str** | Block size of the FlexUtil Physical drive. | [optional] 
**capacity** | **str** | Capacity of the FlexUtil Physical drive. | [optional] 
**controller** | **str** | Type of the Physical Drive Controller. | [optional] 
**drives_enabled** | **str** | The number of drives enabled in the FlexUtil Physical Drive. | [optional] 
**health** | **str** | Health of the FlexUtil Physical drive. | [optional] 
**manufacturer_date** | **str** | Manufacturing date of the FlexUtil Physical Drive. | [optional] 
**manufacturer_id** | **str** | Manufacturer identity of the FlexUtil Physical Drive. | [optional] 
**oem_id** | **str** | The OEM Identifier of the FlexUtil physical drive. | [optional] 
**partition_count** | **str** | The number of partitions present on the FlexUtil Physical Drive. | [optional] 
**pd_status** | **str** | Status of the FlexUtil Physical Drive. | [optional] 
**physical_drive** | **str** | The type of physical drive. Example - microSD. | [optional] 
**product_name** | **str** | Product name of the FlexUtil Physical Drive. | [optional] 
**product_revision** | **str** | Product revision of the FlexUtil Physical Drive. | [optional] 
**read_error_count** | **str** | Read error count of the FlexUtil Physical Drive. | [optional] 
**read_error_threshold** | **str** | Read error threshold for FlexUtil Physical Drive. | [optional] 
**write_enabled** | **str** | Write access state of the FlexUtil Physical Drive. | [optional] 
**write_error_count** | **str** | Write error count of the FlexUtil Physical Drive. | [optional] 
**write_error_threshold** | **str** | Write error threshold for FlexUtil Physical Drive. | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_flex_util_controller** | [**StorageFlexUtilControllerRelationship**](StorageFlexUtilControllerRelationship.md) |  | [optional] 
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


