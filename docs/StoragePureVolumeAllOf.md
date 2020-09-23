# StoragePureVolumeAllOf

Definition of the list of properties defined in 'storage.PureVolume', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Creation time of the volume. | [optional] [readonly] 
**serial** | **str** | Serial number of the volume. | [optional] [readonly] 
**source** | **str** | Source from which the volume is created. Applicable only if the volume is cloned from other volume or snapshot. | [optional] [readonly] 
**array** | [**StoragePureArrayRelationship**](StoragePureArrayRelationship.md) |  | [optional] 
**protection_group** | [**StoragePureProtectionGroupRelationship**](StoragePureProtectionGroupRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


