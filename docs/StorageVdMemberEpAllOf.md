# StorageVdMemberEpAllOf

Definition of the list of properties defined in 'storage.VdMemberEp', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oper_qualifier_reason** | **str** | For certain states, indicates the reason why the operState is in that state. | [optional] [readonly] 
**presence** | **str** | The presence state of the local disk. | [optional] [readonly] 
**role** | **str** | Role of the disk normal or hot-spare, used by virtual-drive. | [optional] [readonly] 
**span_id** | **str** | The span id number of the virtual drive. | [optional] [readonly] 
**vd_member_ep_id** | **int** | The local disk slot number as id. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**storage_virtual_drive** | [**StorageVirtualDriveRelationship**](StorageVirtualDriveRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


