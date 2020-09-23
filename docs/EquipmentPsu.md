# EquipmentPsu

This represents power supply unit for chassis/server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**description** | **str** | This field is to provide description for the power supply unit. | [optional] [readonly] 
**oper_state** | **str** | This field identifies the psu operational state. | [optional] [readonly] 
**part_number** | **str** | This field identifies the Part Number for this Power Supply Unit. | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the Power Supply. | [optional] [readonly] 
**presence** | **str** | This field identifies the presence state of the psu. | [optional] [readonly] 
**psu_fw_version** | **str** | This field identifies the Firmware Version of the Power Supply. | [optional] [readonly] 
**psu_id** | **int** | This represents power supply unit identifier in chassis/server. | [optional] [readonly] 
**psu_input_src** | **str** | This field identifies the input source for the Power Supply. | [optional] [readonly] 
**psu_type** | **str** | This field identifies the type of the Power Supply. | [optional] [readonly] 
**psu_wattage** | **str** | This field identifies the Wattage of the Power Supply. | [optional] [readonly] 
**sku** | **str** | This field identifies the Stockkeeping Unit for this Power Supply. | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for this Power Supply Unit. | [optional] [readonly] 
**voltage** | **str** | This field is used to indicate the Voltage for this Power Supply. | [optional] [readonly] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**equipment_chassis** | [**EquipmentChassisRelationship**](EquipmentChassisRelationship.md) |  | [optional] 
**equipment_fex** | [**EquipmentFexRelationship**](EquipmentFexRelationship.md) |  | [optional] 
**equipment_rack_enclosure** | [**EquipmentRackEnclosureRelationship**](EquipmentRackEnclosureRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**network_element** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 
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
**model** | **str** | This field identifies the model of the given component. | [optional] [readonly] 
**revision** | **str** | This field identifies the revision of the given component. | [optional] [readonly] 
**serial** | **str** | This field identifies the serial of the given component. | [optional] [readonly] 
**vendor** | **str** | This field identifies the vendor of the given component. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


