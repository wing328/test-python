# CapabilityEquipmentSlotArray

Type to represent additional switch specific capabilities.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**first_index** | **float** | First Index information for a Switch/Fabric-Interconnect hardware. | [optional] 
**height** | **float** | Height information for a Switch/Fabric-Interconnect hardware. | [optional] 
**horizontal_start_offset** | **float** | Horizontal Start Offset information for a Switch/Fabric-Interconnect hardware. | [optional] 
**inline_group_separation** | **float** | Inline Group Separation information for a Switch/Fabric-Interconnect hardware. | [optional] 
**inline_group_size** | **float** | Inline Group Size information for a Switch/Fabric-Interconnect hardware. | [optional] 
**inline_offset** | **float** | Inline Offset information for a Switch/Fabric-Interconnect hardware. | [optional] 
**location** | **str** | Location information for a Switch/Fabric-Interconnect hardware. | [optional] 
**number_of_slots** | **int** | Number of Slots information for a Switch/Fabric-Interconnect hardware. | [optional] 
**orientation** | **str** | Orientation information for a Switch/Fabric-Interconnect hardware. | [optional] 
**selector** | **str** | Selector information for a Switch/Fabric-Interconnect hardware. | [optional] 
**slots_per_line** | **int** | Slots per line information for a Switch/Fabric-Interconnect hardware. | [optional] 
**transverse_group_separation** | **float** | Transverse Group Separation information for a Switch/Fabric-Interconnect hardware. | [optional] 
**transverse_group_size** | **float** | Transverse Group Size information for a Switch/Fabric-Interconnect hardware. | [optional] 
**transverse_offset** | **float** | Transverse Offset information for a Switch/Fabric-Interconnect hardware. | [optional] 
**vertical_start_offset** | **float** | Vertical Start Offset information for a Switch/Fabric-Interconnect hardware. | [optional] 
**width** | **float** | Width information for a Switch/Fabric-Interconnect hardware. | [optional] 
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
**name** | **str** | An unique identifer for a capability descriptor. | [optional] 
**section** | [**CapabilitySectionRelationship**](CapabilitySectionRelationship.md) |  | [optional] 
**pid** | **str** | Product Identifier for a Switch/Fabric-Interconnect. | [optional] 
**sku** | **str** | SKU information for Switch/Fabric-Interconnect. | [optional] 
**vid** | **str** | VID information for Switch/Fabric-Interconnect. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


