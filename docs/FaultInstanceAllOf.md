# FaultInstanceAllOf

Definition of the list of properties defined in 'fault.Instance', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


