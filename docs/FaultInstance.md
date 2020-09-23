# FaultInstance

An endpoint anomaly is represented by this object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**acknowledged** | **str** | The user acknowledgement state of the fault. | [optional] [readonly] 
**affected_dn** | **str** | The Distinguished Name of the Managed object which was affected. | [optional] [readonly] 
**affected_mo_id** | **str** | Managed object Id which was affected. | [optional] [readonly] 
**affected_mo_type** | **str** | Managed object type which was affected. | [optional] [readonly] 
**ancestor_mo_id** | **str** | Object Id of the parent of the Managed object which was affected. | [optional] [readonly] 
**ancestor_mo_type** | **str** | Object type of the parent of the Managed object which was affected. | [optional] [readonly] 
**code** | **str** | Numerical fault code of the fault found. | [optional] [readonly] 
**creation_time** | **str** | The time of creation of the fault instance. | [optional] [readonly] 
**description** | **str** | Detailed message of the fault. | [optional] [readonly] 
**last_transition_time** | **str** | Last transition time of the fault. | [optional] [readonly] 
**num_occurrences** | **int** | The number of times this fault has occured. | [optional] [readonly] 
**original_severity** | **str** | Current Severity of the fault found. | [optional] [readonly] 
**previous_severity** | **str** | The Severity of the fault prior to user update. | [optional] [readonly] 
**rule** | **str** | The rule that is responsible for generation of the fault. | [optional] [readonly] 
**severity** | **str** | Severity of the fault found. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
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
**device_mo_id** | **str** | The database identifier of the registered device of an object. | [optional] [readonly] 
**dn** | **str** | The Distinguished Name unambiguously identifies an object in the system. | [optional] [readonly] 
**rn** | **str** | The Relative Name uniquely identifies an object within a given context. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


