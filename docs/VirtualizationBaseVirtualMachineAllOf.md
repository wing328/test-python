# VirtualizationBaseVirtualMachineAllOf

Definition of the list of properties defined in 'virtualization.BaseVirtualMachine', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | [**InfraHardwareInfo**](InfraHardwareInfo.md) |  | [optional] 
**guest_info** | [**VirtualizationGuestInfo**](VirtualizationGuestInfo.md) |  | [optional] 
**hypervisor_type** | **str** | Type of hypervisor where the virtual machine is hosted for example ESXi. | [optional]  if omitted the server will use the default value of "Unknown"
**identity** | **str** | The internally generated identity of this VM. This entity is not manipulated by users. It aids in uniquely identifying the virtual machine object. For VMware, this is MOR (managed object reference). | [optional] 
**ip_address** | **[str]** |  | [optional] 
**memory_capacity** | [**VirtualizationMemoryCapacity**](VirtualizationMemoryCapacity.md) |  | [optional] 
**name** | **str** | User-provided name to identify the virtual machine. | [optional] 
**power_state** | **str** | Power state of the virtual machine. | [optional]  if omitted the server will use the default value of "Unknown"
**processor_capacity** | [**VirtualizationComputeCapacity**](VirtualizationComputeCapacity.md) |  | [optional] 
**uuid** | **str** | The uuid of this virtual machine. The uuid is internally generated and not user specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


