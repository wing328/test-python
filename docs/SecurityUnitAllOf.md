# SecurityUnitAllOf

Definition of the list of properties defined in 'security.Unit', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oper_state** | **str** | Operational state of the security unit. | [optional] [readonly] 
**operability** | **str** | Operability state of the security unit. | [optional] [readonly] 
**part_number** | **str** | The part number of the security unit. | [optional] [readonly] 
**pci_slot** | **str** | PCIe slot of the security unit in the server. | [optional] [readonly] 
**power** | **str** | Power state of the security unit. | [optional] [readonly] 
**presence** | **str** | Security unit presence (equipped) or absence. | [optional] [readonly] 
**thermal** | **str** | Thermal state of the security unit. | [optional] [readonly] 
**unit_id** | **int** | The unique identifier assigned to the security unit within the server. | [optional] [readonly] 
**vid** | **str** | The vendor identifier of the security unit. | [optional] [readonly] 
**voltage** | **str** | The voltage state of the security unit. | [optional] [readonly] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


