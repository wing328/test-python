# EquipmentChassisRelationship

A relationship to the 'equipment.Chassis' resource, or the expanded 'equipment.Chassis' resource, or the 'null' value.
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
**chassis_id** | **int** | The assigned identifier for a chassis. | [optional] [readonly] 
**connection_path** | **str** | This field identifies the connectivity path for the chassis enclosure. | [optional] [readonly] 
**connection_status** | **str** | This field identifies the connectivity status for the chassis enclosure. | [optional] [readonly] 
**description** | **str** | This field is to provide description for chassis model. | [optional] [readonly] 
**fault_summary** | **int** | This field summarizes the faults on the chassis enclosure. | [optional] 
**management_mode** | **str** | The management mode of the blade server chassis. | [optional] [readonly]  if omitted the server will use the default value of "IntersightStandalone"
**name** | **str** | This field identifies the name for the chassis enclosure. | [optional] [readonly] 
**oper_state** | **str** | This field identifies the Chassis Operational State. | [optional] [readonly] 
**part_number** | **str** | Part Number identifier for the chassis enclosure. | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the chassis enclosure. | [optional] [readonly] 
**platform_type** | **str** | The platform type that the chassis is a part of. | [optional] 
**product_name** | **str** | This field identifies the Product Name for the chassis enclosure. | [optional] [readonly] 
**sku** | **str** | This field identifies the Stock Keeping Unit for the chassis enclosure. | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for the chassis enclosure. | [optional] [readonly] 
**blades** | [**[ComputeBladeRelationship], none_type**](ComputeBladeRelationship.md) | An array of relationships to computeBlade resources. | [optional] [readonly] 
**fanmodules** | [**[EquipmentFanModuleRelationship], none_type**](EquipmentFanModuleRelationship.md) | An array of relationships to equipmentFanModule resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**ioms** | [**[EquipmentIoCardRelationship], none_type**](EquipmentIoCardRelationship.md) | An array of relationships to equipmentIoCard resources. | [optional] [readonly] 
**locator_led** | [**EquipmentLocatorLedRelationship**](EquipmentLocatorLedRelationship.md) |  | [optional] 
**psu_control** | [**EquipmentPsuControlRelationship**](EquipmentPsuControlRelationship.md) |  | [optional] 
**psus** | [**[EquipmentPsuRelationship], none_type**](EquipmentPsuRelationship.md) | An array of relationships to equipmentPsu resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**sasexpanders** | [**[StorageSasExpanderRelationship], none_type**](StorageSasExpanderRelationship.md) | An array of relationships to storageSasExpander resources. | [optional] [readonly] 
**siocs** | [**[EquipmentSystemIoControllerRelationship], none_type**](EquipmentSystemIoControllerRelationship.md) | An array of relationships to equipmentSystemIoController resources. | [optional] [readonly] 
**storage_enclosures** | [**[StorageEnclosureRelationship], none_type**](StorageEnclosureRelationship.md) | An array of relationships to storageEnclosure resources. | [optional] [readonly] 
**selector** | **str** | An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of &#39;moid&#39; by clients. 1. If &#39;moid&#39; is set this field is ignored. 1. If &#39;selector&#39; is set and &#39;moid&#39; is empty/absent from the request, Intersight determines the Moid of the resource matching the filter expression and populates it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq &#39;3AA8B7T11&#39;. | [optional] [readonly] 
**link** | **str** | A URL to an instance of the &#39;mo.MoRef&#39; class. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


