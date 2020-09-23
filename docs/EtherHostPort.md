# EtherHostPort

Model object contains the details of host port available on IO card or fabric extender.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
**module_id** | **int** | Fabric extender identifier for this port. | [optional] 
**speed** | **str** | Host Port Speed of IO card or fabric extender. | [optional] [readonly] 
**equipment_io_card_base** | [**EquipmentIoCardBaseRelationship**](EquipmentIoCardBaseRelationship.md) |  | [optional] 
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
**oper_state** | **str** | Operational state of this port (enabled/disabled). | [optional] [readonly] 
**oper_state_qual** | **str** | Reason for this port&#39;s Operational state. | [optional] [readonly] 
**port_id** | **int** | Switch physical port identifier. | [optional] [readonly] 
**role** | **str** | The role assigned to this port. | [optional] [readonly] 
**slot_id** | **int** | Switch expansion slot module identifier. | [optional] [readonly] 
**switch_id** | **str** | Switch Identifier that is local to a cluster. | [optional] [readonly] 
**mac_address** | **str** | Mac Address of a port in the Fabric Interconnect. | [optional] [readonly] 
**mode** | **str** | Operating mode of this port. | [optional] [readonly] 
**oper_speed** | **str** | Current Operational speed for this port. | [optional] [readonly] 
**peer_dn** | **str** | PeerDn for ethernet physical port. | [optional] [readonly] 
**port_channel_id** | **int** | Port channel id for port channel created on FI switch. | [optional] [readonly] 
**port_type** | **str** | Defines the transport type for this port (ethernet OR fc). | [optional] [readonly] 
**transceiver_type** | **str** | Transceiver model attached to a port in the Fabric Interconnect. | [optional] [readonly] 
**acknowledged_peer_interface** | [**PortInterfaceBaseRelationship**](PortInterfaceBaseRelationship.md) |  | [optional] 
**peer_interface** | [**PortInterfaceBaseRelationship**](PortInterfaceBaseRelationship.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


