# MemoryPersistentMemoryGoalAllOf

Definition of the list of properties defined in 'memory.PersistentMemoryGoal', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_mode_percentage** | **int** | Volatile memory percentage. | [optional] 
**persistent_memory_type** | **str** | Type of the Persistent Memory configuration where the Persistent Memory Modules are combined in an interleaved set or not. | [optional]  if omitted the server will use the default value of "app-direct"
**socket_id** | **str** | CPU Socket ID to which this goal will be applied. | [optional]  if omitted the server will use the default value of "All Sockets"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


