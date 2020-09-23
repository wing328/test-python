# StorageBaseCapacityAllOf

Definition of the list of properties defined in 'storage.BaseCapacity', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** | Total consumable storage capacity represented in bytes. System may reserve some space for internal purposes which is excluded from total capacity. | [optional] [readonly] 
**free** | **int** | Unused space available for applications to consume, represented in bytes. | [optional] [readonly] 
**total** | **int** | Total storage capacity, represented in bytes. It is set by the component manufacturer. | [optional] [readonly] 
**used** | **int** | Used or consumed storage capacity, represented in bytes. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


