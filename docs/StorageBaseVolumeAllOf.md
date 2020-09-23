# StorageBaseVolumeAllOf

Definition of the list of properties defined in 'storage.BaseVolume', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Short description about the volume. | [optional] [readonly] 
**naa_id** | **str** | NAA id of volume. It is a significant number to identify corresponding lun path in hypervisor. | [optional] [readonly] 
**name** | **str** | Named entity of the volume. | [optional] [readonly] 
**size** | **int** | User provisioned volume size. It is the size exposed to host. | [optional] [readonly] 
**storage_utilization** | [**StorageBaseCapacity**](StorageBaseCapacity.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


