# VirtualizationBaseClusterAllOf

Definition of the list of properties defined in 'virtualization.BaseCluster', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hypervisor_type** | **str** | Identifies the broad type of the underlying hypervisor. | [optional]  if omitted the server will use the default value of "Unknown"
**identity** | **str** | The internally generated identity of this cluster. This entity is not manipulated by users. It aids in uniquely identifying the cluster object. In case of VMware, this is a MOR (managed object reference). | [optional] [readonly] 
**memory_capacity** | [**VirtualizationMemoryCapacity**](VirtualizationMemoryCapacity.md) |  | [optional] 
**name** | **str** | The user-provided name for this cluster to facilitate identification. | [optional] [readonly] 
**processor_capacity** | [**VirtualizationComputeCapacity**](VirtualizationComputeCapacity.md) |  | [optional] 
**status** | **str** | Cluster health status as reported by the hypervisor platform. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**total_cores** | **int** | Total number of CPU cores in this cluster. It is a cumulative number across all hosts in the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


