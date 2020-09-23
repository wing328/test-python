# ComputePersistentMemoryOperationAllOf

Definition of the list of properties defined in 'compute.PersistentMemoryOperation', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_action** | **str** | Administrative actions that can be performed on the Persistent Memory Modules. | [optional]  if omitted the server will use the default value of "None"
**is_secure_passphrase_set** | **bool** | Indicates whether the value of the &#39;securePassphrase&#39; property has been set. | [optional] [readonly] 
**modules** | [**[ComputePersistentMemoryModule]**](ComputePersistentMemoryModule.md) |  | [optional] 
**secure_passphrase** | **str** | Secure passphrase of the Persistent Memory Modules of the server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


