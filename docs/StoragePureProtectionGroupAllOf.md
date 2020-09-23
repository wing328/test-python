# StoragePureProtectionGroupAllOf

Definition of the list of properties defined in 'storage.PureProtectionGroup', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Overall size of all snapshots in the protection group, represented in bytes. | [optional] 
**source** | **str** | Name of PureStorage array name on which the protection group is created. | [optional] [readonly] 
**targets** | **[str]** |  | [optional] 
**array** | [**StoragePureArrayRelationship**](StoragePureArrayRelationship.md) |  | [optional] 
**host_groups** | [**[StoragePureHostGroupRelationship], none_type**](StoragePureHostGroupRelationship.md) | An array of relationships to storagePureHostGroup resources. | [optional] [readonly] 
**hosts** | [**[StoragePureHostRelationship], none_type**](StoragePureHostRelationship.md) | An array of relationships to storagePureHost resources. | [optional] [readonly] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**volumes** | [**[StoragePureVolumeRelationship], none_type**](StoragePureVolumeRelationship.md) | An array of relationships to storagePureVolume resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


