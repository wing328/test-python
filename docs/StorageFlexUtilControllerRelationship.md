# StorageFlexUtilControllerRelationship

A relationship to the 'storage.FlexUtilController' resource, or the expanded 'storage.FlexUtilController' resource, or the 'null' value.
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
**controller_name** | **str** | Name of the Flex Util Controller. | [optional] 
**controller_status** | **str** | The current status of the controller. | [optional] 
**ff_controller_id** | **str** | Identifier for the Storage Flex Util Controller. | [optional] 
**internal_state** | **str** | The internal state of the controller. | [optional] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**flex_util_physical_drives** | [**[StorageFlexUtilPhysicalDriveRelationship], none_type**](StorageFlexUtilPhysicalDriveRelationship.md) | An array of relationships to storageFlexUtilPhysicalDrive resources. | [optional] [readonly] 
**flex_util_virtual_drives** | [**[StorageFlexUtilVirtualDriveRelationship], none_type**](StorageFlexUtilVirtualDriveRelationship.md) | An array of relationships to storageFlexUtilVirtualDrive resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**selector** | **str** | An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of &#39;moid&#39; by clients. 1. If &#39;moid&#39; is set this field is ignored. 1. If &#39;selector&#39; is set and &#39;moid&#39; is empty/absent from the request, Intersight determines the Moid of the resource matching the filter expression and populates it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq &#39;3AA8B7T11&#39;. | [optional] [readonly] 
**link** | **str** | A URL to an instance of the &#39;mo.MoRef&#39; class. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

