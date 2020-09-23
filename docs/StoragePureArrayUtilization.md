# StoragePureArrayUtilization

Storage space consumption of Pure FlashArray.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**data_reduction** | **float** | Ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5.0 means that for every 5 MB the host writes to the array, 1 MB is stored on the array&#39;s flash modules. | [optional] [readonly] 
**parity** | **float** | Percentage of data that is fully protected. The percentage value will drop below 100% if the data is not fully protected. | [optional] [readonly] 
**provisioned** | **int** | Total provisioned storage capacity in Pure FlashArray, represented in bytes. | [optional] [readonly] 
**shared** | **int** | Physical space occupied by deduplicated data, represented in bytes. The space is shared with other volumes and snapshots as a result of data deduplication. | [optional] [readonly] 
**snapshot** | **int** | Physical space occupied by the snapshots, represented in bytes. | [optional] [readonly] 
**system** | **int** | Physical space occupied by internal array metadata, represented in bytes. | [optional] [readonly] 
**thin_provisioned** | **float** | Percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed. | [optional] [readonly] 
**total_reduction** | **float** | Ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10.0 means that for every 10 MB of provisioned space, 1 MB is stored on the array&#39;s flash modules. | [optional] [readonly] 
**volume** | **int** | Physical space occupied by volume data, excluding shared, array metadata and snapshots. Size is represented in bytes. | [optional] [readonly] 
**available** | **int** | Total consumable storage capacity represented in bytes. System may reserve some space for internal purposes which is excluded from total capacity. | [optional] [readonly] 
**free** | **int** | Unused space available for applications to consume, represented in bytes. | [optional] [readonly] 
**total** | **int** | Total storage capacity, represented in bytes. It is set by the component manufacturer. | [optional] [readonly] 
**used** | **int** | Used or consumed storage capacity, represented in bytes. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


