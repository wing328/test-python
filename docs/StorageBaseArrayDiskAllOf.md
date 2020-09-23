# StorageBaseArrayDiskAllOf

Definition of the list of properties defined in 'storage.BaseArrayDisk', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Disk name available in storage array. | [optional] [readonly] 
**part_number** | **str** | Storage disk part number. | [optional] [readonly] 
**protocol** | **str** | Storage protocol used in disk for communication. Possible values are SAS, SATA and NVMe. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**speed** | **int** | Disk speed for read or write operation measured in rpm. | [optional] [readonly] 
**status** | **str** | Storage disk health status. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**storage_utilization** | [**StorageBaseCapacity**](StorageBaseCapacity.md) |  | [optional] 
**type** | **str** | Storage disk type - it can be SSD, HDD, NVRAM. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**version** | **str** | Storage disk version number. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


