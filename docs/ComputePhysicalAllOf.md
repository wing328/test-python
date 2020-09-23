# ComputePhysicalAllOf

Definition of the list of properties defined in 'compute.Physical', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_power_state** | **str** | The desired power state of the server. | [optional] [readonly] 
**asset_tag** | **str** | The user defined asset tag assigned to the server. | [optional] [readonly] 
**available_memory** | **int** | The amount of memory available on the server. | [optional] [readonly] 
**bios_post_complete** | **bool** | The BIOS POST completion status of the server. | [optional] 
**fault_summary** | **int** | The fault summary for the server. | [optional] 
**kvm_ip_addresses** | [**[ComputeIpAddress]**](ComputeIpAddress.md) |  | [optional] 
**management_mode** | **str** | The management mode of the server. | [optional]  if omitted the server will use the default value of "IntersightStandalone"
**memory_speed** | **str** | The maximum memory speed in MHz available on the server. | [optional] [readonly] 
**mgmt_ip_address** | **str** | Management address of the server. | [optional] 
**num_adaptors** | **int** | The total number of network adapters present on the server. | [optional] [readonly] 
**num_cpu_cores** | **int** | The total number of CPU cores present on the server. | [optional] [readonly] 
**num_cpu_cores_enabled** | **int** | The total number of CPU cores enabled on the server. | [optional] [readonly] 
**num_cpus** | **int** | The total number of CPUs present on the server. | [optional] [readonly] 
**num_eth_host_interfaces** | **int** | The total number of vNICs which are visible to a host on the server. | [optional] [readonly] 
**num_fc_host_interfaces** | **int** | The total number of vHBAs which are visible to a host on the server. | [optional] [readonly] 
**num_threads** | **int** | The total number of threads the server is capable of handling. | [optional] [readonly] 
**oper_power_state** | **str** | The actual power state of the server. | [optional] [readonly] 
**oper_state** | **str** | The operational state of the server. | [optional] [readonly] 
**operability** | **str** | The operability of the server. | [optional] [readonly] 
**platform_type** | **str** | The platform type of the registered device - whether managed by UCSM or operating in standalone mode. | [optional] 
**presence** | **str** | Indicates if a server is present in a slot and is applicable for blade servers. | [optional] [readonly] 
**service_profile** | **str** | The distinguished name of the service profile to which the server is associated to. It is applicable only for servers which are managed via UCSM. | [optional] [readonly] 
**total_memory** | **int** | The total memory available on the server. | [optional] [readonly] 
**user_label** | **str** | The user defined label assigned to the server. | [optional] [readonly] 
**uuid** | **str** | The universally unique identity of the server. | [optional] [readonly] 
**mgmt_identity** | [**EquipmentPhysicalIdentityRelationship**](EquipmentPhysicalIdentityRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


