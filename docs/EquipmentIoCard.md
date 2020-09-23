# EquipmentIoCard

I/O module on a chassis which multiplexes traffic from blade servers.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**connection_path** | **str** | Switch Id to which the IOM is connected to. The value can be A or B. | [optional] [readonly] 
**dc_supported** | **bool** | IOM device connector support. | [optional] [readonly] 
**side** | **str** | Location of IOM within a chassis. The value can be left or right. | [optional] [readonly] 
**equipment_chassis** | [**EquipmentChassisRelationship**](EquipmentChassisRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**physical_device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
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
**connection_status** | **str** | Connectivity Status of FEX/IOM to Switch - A or B or AB. | [optional] 
**description** | **str** | This field is to provide description for the iocard module model. | [optional] [readonly] 
**module_id** | **int** | Module Identifier for the IO module. | [optional] [readonly] 
**oper_state** | **str** | Operational state of IO card or fabric extender. | [optional] [readonly] 
**part_number** | **str** | Part Number identifier for the IO module. | [optional] [readonly] 
**pid** | **str** | This field identifies the Product ID for the IO module. | [optional] [readonly] 
**presence** | **str** | This field identifies the Presence state of the IO card module. | [optional] [readonly] 
**product_name** | **str** | This field identifies the Product Name for the iocard module model. | [optional] [readonly] 
**sku** | **str** | This field identifies the Stock Keeping Unit for the IO card module. | [optional] [readonly] 
**version** | **str** | This field identifies the version of the IO card module. | [optional] [readonly] 
**vid** | **str** | This field identifies the Vendor ID for the IO card module. | [optional] [readonly] 
**host_ports** | [**[EtherHostPortRelationship], none_type**](EtherHostPortRelationship.md) | An array of relationships to etherHostPort resources. | [optional] 
**mgmt_controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**network_ports** | [**[EtherNetworkPortRelationship], none_type**](EtherNetworkPortRelationship.md) | An array of relationships to etherNetworkPort resources. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


