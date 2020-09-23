# VnicVmqSettingsAllOf

Definition of the list of properties defined in 'vnic.VmqSettings', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enables VMQ feature on the virtual interface. | [optional] 
**multi_queue_support** | **bool** | Enables Virtual Machine Multi-Queue feature on the virtual interface. VMMQ allows configuration of multiple I/O queues for a single VM and, thus, distributes traffic across multiple CPU cores in a VM. | [optional] 
**num_interrupts** | **int** | The number of interrupt resources to be allocated. Recommended value is the number of CPU threads or logical processors available in the server. | [optional] 
**num_sub_vnics** | **int** | The number of sub vnics to be created. | [optional] 
**num_vmqs** | **int** | The number of hardware Virtual Machine Queues to be allocated. The number of VMQs per adapter must be one more than the maximum number of VM NICs. | [optional] 
**vmmq_adapter_policy** | **str** | Ethernet Adapter policy to be associated with the subVnics. The Transmit Queue and Receive Queue resource value of VMMQ adapter policy should be greater than or equal to the configured number of sub vnics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


