# StorageSasExpanderAllOf

Definition of the list of properties defined in 'storage.SasExpander', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expander_id** | **int** | Unique Identifier of the storage expander. | [optional] [readonly] 
**name** | **str** | The name  of the installed storage expander. | [optional] 
**oper_state** | **str** | The operational state of the storage expander. | [optional] [readonly] 
**operability** | **str** | The operability status of the storage expander. | [optional] [readonly] 
**presence** | **str** | The availability of the storage expander. | [optional] [readonly] 
**sas_address** | **str** | The SAS address of the SAS expander. | [optional] [readonly] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**equipment_chassis** | [**EquipmentChassisRelationship**](EquipmentChassisRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


