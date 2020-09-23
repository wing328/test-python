# StorageStoragePolicyAllOf

Definition of the list of properties defined in 'storage.StoragePolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_hot_spares** | [**[StorageLocalDisk]**](StorageLocalDisk.md) |  | [optional] 
**retain_policy_virtual_drives** | **bool** | Retains the virtual drives defined in policy if they exist already. If this flag is false, the existing virtual drives are removed and created again based on virtual drives in the policy. | [optional] 
**unused_disks_state** | **str** | Unused Disks State is used to specify the state, unconfigured good or jbod, in which the disks that are not used in this policy should be moved. | [optional]  if omitted the server will use the default value of "UnconfiguredGood"
**virtual_drives** | [**[StorageVirtualDriveConfig]**](StorageVirtualDriveConfig.md) |  | [optional] 
**disk_group_policies** | [**[StorageDiskGroupPolicyRelationship], none_type**](StorageDiskGroupPolicyRelationship.md) | An array of relationships to storageDiskGroupPolicy resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


