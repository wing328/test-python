# ProcessorUnitAllOf

Definition of the list of properties defined in 'processor.Unit', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | The architecture of the installed processor. | [optional] [readonly] 
**num_cores** | **int** | The number of cores present in a given processor. | [optional] [readonly] 
**num_cores_enabled** | **str** | The number of enabled cores in the installed processor. | [optional] [readonly] 
**num_threads** | **str** | The maximum number of threads available in the installed processor. | [optional] [readonly] 
**oper_power_state** | **str** | The power state of the processor. | [optional] [readonly] 
**oper_state** | **str** | The health indicator of the processor, &#39;OK&#39; indicates the processor is operatinal. | [optional] [readonly] 
**operability** | **str** | Operability state of the central processing unit. | [optional] [readonly] 
**presence** | **str** | The valid values are &#39;equipped&#39; and &#39;absent&#39;. | [optional] [readonly] 
**processor_id** | **int** | The ID number of a given processor. | [optional] [readonly] 
**socket_designation** | **str** | The socket ID of the installed processor. | [optional] [readonly] 
**speed** | **float** | The maximum speed of the installed processor in GHz. | [optional] [readonly] 
**stepping** | **str** | The CPU stepping of the installed processor. | [optional] [readonly] 
**thermal** | **str** | The temperature of the processor in centigrade. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_board** | [**ComputeBoardRelationship**](ComputeBoardRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


