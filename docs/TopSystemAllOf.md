# TopSystemAllOf

Definition of the list of properties defined in 'top.System', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_address** | **str** | The IPv4 address of system. | [optional] [readonly] 
**ipv6_address** | **str** | The IPv6 address of system. | [optional] [readonly] 
**mode** | **str** | The current mode of the system. | [optional] [readonly] 
**name** | **str** | The admin configured name of the system. | [optional] [readonly] 
**time_zone** | **str** | The operational timezone of the system, empty indicates no timezone has been set specifically. | [optional] 
**compute_blades** | [**[ComputeBladeRelationship], none_type**](ComputeBladeRelationship.md) | An array of relationships to computeBlade resources. | [optional] 
**compute_rack_units** | [**[ComputeRackUnitRelationship], none_type**](ComputeRackUnitRelationship.md) | An array of relationships to computeRackUnit resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**management_controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**network_elements** | [**[NetworkElementRelationship], none_type**](NetworkElementRelationship.md) | An array of relationships to networkElement resources. | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


