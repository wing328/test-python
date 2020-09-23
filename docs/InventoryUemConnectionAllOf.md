# InventoryUemConnectionAllOf

Definition of the list of properties defined in 'inventory.UemConnection', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | Connections status of Uem endpoint. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**ep_info** | [**InventoryEpInfo**](InventoryEpInfo.md) |  | [optional] 
**ep_type** | **str** | Type of Uem endpoint (BMC, CMC or VIC). | [optional] [readonly] 
**ip** | **str** | The IP address of the Uem endpoint. | [optional] [readonly] 
**member_identity** | **str** | The member identity of the UEM connection being inventoried. | [optional] [readonly] 
**model** | **str** | The model of the Uem endpoint. | [optional] [readonly] 
**serial** | **str** | The serial number of the Uem endpoint. | [optional] [readonly] 
**target_mo_id** | **str** | The MoId address of the Uem endpoint. | [optional] [readonly] 
**vendor** | **str** | The vendor of the Uem endpoint. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


