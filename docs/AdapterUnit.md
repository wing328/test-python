# AdapterUnit

The physical adapter present on a server.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**adapter_id** | **str** | Unique Identifier of an adapter Unit within a Rack Interface. | [optional] [readonly] 
**base_mac_address** | **str** | Original Base Mac address of an adapter unit. | [optional] [readonly] 
**connection_status** | **str** | Connectivity Status of adapter - A or B or AB. | [optional] [readonly] 
**integrated** | **str** | Cisco Integrated adapter or other type. | [optional] [readonly] 
**oper_state** | **str** | Operational state of an adapter unit. | [optional] [readonly] 
**operability** | **str** | Operability state of an adapter unit. | [optional] [readonly] 
**part_number** | **str** | Part number of an adapter unit. | [optional] [readonly] 
**pci_slot** | **str** | PCIe slot of the adapter in the server. | [optional] [readonly] 
**power** | **str** | Power state of an adapter unit. | [optional] [readonly] 
**presence** | **str** | Adapter Unit presence or absence. | [optional] [readonly] 
**thermal** | **str** | Thermal state of an adapter unit. | [optional] [readonly] 
**vid** | **str** | Virtual Id of the adapter in the server. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**ext_eth_ifs** | [**[AdapterExtEthInterfaceRelationship], none_type**](AdapterExtEthInterfaceRelationship.md) | An array of relationships to adapterExtEthInterface resources. | [optional] [readonly] 
**host_eth_ifs** | [**[AdapterHostEthInterfaceRelationship], none_type**](AdapterHostEthInterfaceRelationship.md) | An array of relationships to adapterHostEthInterface resources. | [optional] [readonly] 
**host_fc_ifs** | [**[AdapterHostFcInterfaceRelationship], none_type**](AdapterHostFcInterfaceRelationship.md) | An array of relationships to adapterHostFcInterface resources. | [optional] [readonly] 
**host_iscsi_ifs** | [**[AdapterHostIscsiInterfaceRelationship], none_type**](AdapterHostIscsiInterfaceRelationship.md) | An array of relationships to adapterHostIscsiInterface resources. | [optional] [readonly] 
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
**model** | **str** | This field identifies the model of the given component. | [optional] [readonly] 
**revision** | **str** | This field identifies the revision of the given component. | [optional] [readonly] 
**serial** | **str** | This field identifies the serial of the given component. | [optional] [readonly] 
**vendor** | **str** | This field identifies the vendor of the given component. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


