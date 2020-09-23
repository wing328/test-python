# EquipmentIdentitySummary

Consolidated view of all equipment identities.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**adapter_serial** | **str** | Serial Identifier of an adapter participating in SWM. | [optional] [readonly] 
**admin_action** | **str** | Updated by UI/API to trigger specific chassis action type. | [optional] [readonly]  if omitted the server will use the default value of "None"
**admin_action_state** | **str** | The state of Maintenance Action performed. This will have three states. Applying - Action is in progress. Applied - Action is completed and applied. Failed - Action has failed. | [optional] [readonly]  if omitted the server will use the default value of "None"
**chassis_id** | **int** | Chassis Identifier of a blade server. | [optional] [readonly] 
**device_mo_id** | **str** | FI Device registration Mo ID. | [optional] [readonly] 
**identifier** | **int** | Numeric Identifier assigned by the management system to the equipment. | [optional] [readonly] 
**io_card_identity_list** | [**[EquipmentIoCardIdentity]**](EquipmentIoCardIdentity.md) |  | [optional] 
**lifecycle** | **str** | The equipment&#39;s lifecycle status. | [optional] [readonly]  if omitted the server will use the default value of "None"
**model** | **str** | The vendor provided model name for the equipment. | [optional] [readonly] 
**pending_discovery** | **str** | Indicates pending discovery flag. | [optional] [readonly] 
**serial** | **str** | The serial number of the equipment. | [optional] [readonly] 
**slot_id** | **int** | Chassis slot number of a blade server. | [optional] [readonly] 
**source_object_type** | **str** | The source object type of this view MO. | [optional] [readonly] 
**switch_id** | **int** | Switch ID to which Fabric Extender is connected, ID can be either 1 or 2, equalent to A or B. | [optional] [readonly] 
**vendor** | **str** | The manufacturer of the equipment. | [optional] [readonly] 
**device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
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


