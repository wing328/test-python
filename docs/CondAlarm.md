# CondAlarm

A state-full entity representing a found problem. Alarms can be reported by the managed system itself or can be determined by Intersight.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**affected_mo_id** | **str** | MoId of the affected object from the managed system&#39;s point of view. | [optional] 
**affected_mo_type** | **str** | Managed system affected object type. For example Adaptor, FI, CIMC. | [optional] 
**affected_object** | **str** | A unique key for an alarm instance, consists of a combination of a unique system name and msAffectedObject. | [optional] 
**ancestor_mo_id** | **str** | Parent MoId of the fault from managed system. For example, Blade moid for adaptor fault. | [optional] 
**ancestor_mo_type** | **str** | Parent MO type of the fault from managed system. For example, Blade for adaptor fault. | [optional] 
**code** | **str** | A unique alarm code. For alarms mapped from UCS faults, this will be the same as the UCS fault code. | [optional] 
**creation_time** | **datetime** | The time the alarm was created. | [optional] 
**description** | **str** | A longer description of the alarm than the name. The description contains details of the component reporting the issue. | [optional] 
**last_transition_time** | **datetime** | The time the alarm last had a change in severity. | [optional] 
**ms_affected_object** | **str** | A unique key for the alarm from the managed system&#39;s point of view. For example, in the case of UCS, this is the fault&#39;s dn. | [optional] 
**name** | **str** | Uniquely identifies the type of alarm. For alarms originating from Intersight, this will be a descriptive name. For alarms that are mapped from faults, the name will be derived from fault properties. For example, alarms mapped from UCS faults will use a prefix of UCS and appended with the fault code. | [optional] 
**orig_severity** | **str** | The original severity when the alarm was first created. | [optional]  if omitted the server will use the default value of "None"
**severity** | **str** | The severity of the alarm. Valid values are Critical, Warning, Info, and Cleared. | [optional]  if omitted the server will use the default value of "None"
**affected_mo** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
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


