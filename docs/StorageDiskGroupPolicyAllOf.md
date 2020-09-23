# StorageDiskGroupPolicyAllOf

Definition of the list of properties defined in 'storage.DiskGroupPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dedicated_hot_spares** | [**[StorageLocalDisk]**](StorageLocalDisk.md) |  | [optional] 
**raid_level** | **str** | The supported RAID level for the disk group. | [optional]  if omitted the server will use the default value of "Raid0"
**span_groups** | [**[StorageSpanGroup]**](StorageSpanGroup.md) |  | [optional] 
**use_jbods** | **bool** | Selected disks in the disk group in JBOD state will be set to Unconfigured Good state before they are used in virtual drive creation. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**storage_policies** | [**[StorageStoragePolicyRelationship], none_type**](StorageStoragePolicyRelationship.md) | An array of relationships to storageStoragePolicy resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


