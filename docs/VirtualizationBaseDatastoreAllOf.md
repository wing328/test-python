# VirtualizationBaseDatastoreAllOf

Definition of the list of properties defined in 'virtualization.BaseDatastore', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**VirtualizationStorageCapacity**](VirtualizationStorageCapacity.md) |  | [optional] 
**host_count** | **int** | Number of hosts attached to or supported-by this datastore. | [optional] 
**identity** | **str** | The internally generated identity of this datastore. This entity is not manipulated by users. It aids in uniquely identifying the datastore object. For VMware, this is a MOR (managed object reference). | [optional] 
**name** | **str** | Name of this datastore supplied by user. It is not the identity of the datastore. The name is subject to user manipulations. | [optional] 
**type** | **str** | A string indicating the type of the datastore (VMFS, NFS, etc). | [optional]  if omitted the server will use the default value of "Unknown"
**vm_count** | **int** | Number of virtual machines relying on (using) this datastore. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


