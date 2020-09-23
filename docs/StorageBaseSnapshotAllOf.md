# StorageBaseSnapshotAllOf

Definition of the list of properties defined in 'storage.BaseSnapshot', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **datetime** | Exact date and time at which snapshot was created. | [optional] [readonly] 
**name** | **str** | Name of the snapshot which represents point-in-time copy of volume. | [optional] [readonly] 
**protection_group_name** | **str** | Name of the protection group to which the snapshot belongs. Value is empty, if the snapshot is created directly on volume. | [optional] [readonly] 
**size** | **int** | Snapshot size represented in bytes. | [optional] [readonly] 
**source** | **str** | Source object on which the snapshot is created. It is the name of the originating volume. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


