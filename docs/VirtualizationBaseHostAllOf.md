# VirtualizationBaseHostAllOf

Definition of the list of properties defined in 'virtualization.BaseHost', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_info** | [**VirtualizationCpuInfo**](VirtualizationCpuInfo.md) |  | [optional] 
**hardware_info** | [**InfraHardwareInfo**](InfraHardwareInfo.md) |  | [optional] 
**hypervisor_type** | **str** | Identifies the broad type of the underlying hypervisor. | [optional]  if omitted the server will use the default value of "Unknown"
**identity** | **str** | The internally generated identity of this host. This entity is not manipulated by users. It aids in uniquely identifying the datacenter object. For VMware, this is an MOR (managed object reference). | [optional] 
**maintenance_mode** | **bool** | Is this host in maintenance mode. Set to true or false. | [optional] 
**memory_capacity** | [**VirtualizationMemoryCapacity**](VirtualizationMemoryCapacity.md) |  | [optional] 
**model** | **str** | Commercial model information about this hardware. | [optional] 
**name** | **str** | Name of this host supplied by user. It is not the identity of the host. The name is subject to user manipulations. | [optional] 
**processor_capacity** | [**VirtualizationComputeCapacity**](VirtualizationComputeCapacity.md) |  | [optional] 
**product_info** | [**VirtualizationProductInfo**](VirtualizationProductInfo.md) |  | [optional] 
**serial** | **str** | Serial number of this host (internally generated). | [optional] 
**status** | **str** | Host health status, as reported by the hypervisor platform. | [optional]  if omitted the server will use the default value of "Unknown"
**up_time** | **str** | The uptime of the host, stored as Duration (from w3c). | [optional] 
**uuid** | **str** | Universally unique identity of this host (example b3d4483b-5560-9342-8309-b486c9236610). Internally generated. | [optional] 
**vendor** | **str** | Commercial vendor details of this hardware. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


