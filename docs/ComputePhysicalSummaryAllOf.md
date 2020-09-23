# ComputePhysicalSummaryAllOf

Definition of the list of properties defined in 'compute.PhysicalSummary', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_power_state** | **str** | The desired power state of the server. | [optional] [readonly] 
**asset_tag** | **str** | The user defined asset tag assigned to the server. | [optional] [readonly] 
**available_memory** | **int** | The amount of memory available on the server. | [optional] [readonly] 
**bios_post_complete** | **bool** | The BIOS POST completion status of the server. | [optional] [readonly] 
**chassis_id** | **str** | The id of the chassis that the blade is located in. | [optional] [readonly] 
**connection_status** | **str** | Connectivity Status of RackUnit to Switch - A or B or AB. | [optional] [readonly] 
**cpu_capacity** | **float** | CPU Capacity &#x3D; Number of CPU Sockets x Enabled Cores x Speed (GHz). | [optional] [readonly] 
**device_mo_id** | **str** | The database identifier of the registered device of an object. | [optional] [readonly] 
**dn** | **str** | The Distinguished Name unambiguously identifies an object in the system. | [optional] [readonly] 
**fault_summary** | **int** | The fault summary for the server. | [optional] [readonly] 
**firmware** | **str** | The firmware version of the Cisco Integrated Management Controller (CIMC) for this server. | [optional] [readonly] 
**ipv4_address** | **str** | The IPv4 address configured on the management interface of the Integrated Management Controller. | [optional] [readonly] 
**kvm_ip_addresses** | [**[ComputeIpAddress]**](ComputeIpAddress.md) |  | [optional] 
**management_mode** | **str** | The management mode of the server. | [optional] [readonly]  if omitted the server will use the default value of "IntersightStandalone"
**memory_speed** | **str** | The maximum memory speed in MHz available on the server. | [optional] [readonly] 
**mgmt_ip_address** | **str** | Management address of the server. | [optional] [readonly] 
**model** | **str** | This field identifies the model of the given component. | [optional] [readonly] 
**name** | **str** | The name of the UCS Fabric Interconnect cluster or Cisco Integrated Management Controller (CIMC). When this server is attached to a UCS Fabric Interconnect, the value of this property is the name of the UCS Fabric Interconnect. When this server configured in standalone mode, the value of this property is the name of the Cisco Integrated Management Controller. | [optional] [readonly] 
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
**platform_type** | **str** | The platform type of the registered device - whether managed by UCSM or operating in standalone mode. | [optional] [readonly] 
**presence** | **str** | Indicates if a server is present in a slot and is applicable for blade servers. | [optional] [readonly] 
**revision** | **str** | This field identifies the revision of the given component. | [optional] [readonly] 
**rn** | **str** | The Relative Name uniquely identifies an object within a given context. | [optional] [readonly] 
**scaled_mode** | **str** | The mode of the server that determines it is scaled. | [optional] [readonly] 
**serial** | **str** | This field identifies the serial of the given component. | [optional] [readonly] 
**server_id** | **int** | RackUnit ID that uniquely identifies the server. | [optional] [readonly] 
**service_profile** | **str** | The distinguished name of the service profile to which the server is associated to. It is applicable only for servers which are managed via UCSM. | [optional] [readonly] 
**slot_id** | **int** | The slot number in the chassis that the blade is located in. | [optional] [readonly] 
**source_object_type** | **str** | The source object type of this view MO. | [optional] [readonly] 
**topology_scan_status** | **str** | To maintain the Topology workflow run status. | [optional] [readonly] 
**total_memory** | **int** | The total memory available on the server. | [optional] [readonly] 
**user_label** | **str** | The user defined label assigned to the server. | [optional] [readonly] 
**uuid** | **str** | The universally unique identity of the server. | [optional] [readonly] 
**vendor** | **str** | This field identifies the vendor of the given component. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


