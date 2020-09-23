# VirtualizationVmwareVirtualMachineAllOf

Definition of the list of properties defined in 'virtualization.VmwareVirtualMachine', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotation** | **str** | List of annotations provided to this VM by user. Can be long. | [optional] 
**boot_time** | **datetime** | Time when this VM booted up. | [optional] 
**config_name** | **str** | The configuration name for this VM. This maybe the same as the guest hostname. | [optional] 
**connection_state** | **str** | Shows if virtual machine is connected to vCenter. Values are Connected, Disconnected, Orphaned, Inaccessible, and Invalid. | [optional] 
**cpu_hot_add_enabled** | **bool** | Indicates if the capability to add CPUs to a running VM is enabled. | [optional] 
**cpu_shares** | [**VirtualizationVmwareVmCpuShareInfo**](VirtualizationVmwareVmCpuShareInfo.md) |  | [optional] 
**cpu_socket_info** | [**VirtualizationVmwareVmCpuSocketInfo**](VirtualizationVmwareVmCpuSocketInfo.md) |  | [optional] 
**custom_attributes** | **[str]** |  | [optional] 
**default_power_off_type** | **str** | Indicates how the VM will be powered off (soft, hard etc.). | [optional] 
**dhcp_enabled** | **bool** | Shows if DHCP is used for IP/DNS on this VM. | [optional] 
**disk_commit_info** | [**VirtualizationVmwareVmDiskCommitInfo**](VirtualizationVmwareVmDiskCommitInfo.md) |  | [optional] 
**dns_server_list** | **[str]** |  | [optional] 
**dns_suffix_list** | **[str]** |  | [optional] 
**folder** | **str** | The folder name associated with this VM. | [optional] 
**guest_state** | **str** | The state of the guest OS running on this VM. Could be running, not running etc. | [optional]  if omitted the server will use the default value of "Unknown"
**instance_uuid** | **str** | UUID assigned by vCenter to every VM. | [optional] 
**is_template** | **bool** | If true, indicates that the entity refers to a template of a virtual machine and not a real virtual machine. | [optional] 
**mac_address** | **[str]** |  | [optional] 
**mem_shares** | [**VirtualizationVmwareVmMemoryShareInfo**](VirtualizationVmwareVmMemoryShareInfo.md) |  | [optional] 
**memory_hot_add_enabled** | **bool** | Adding memory to a running VM. | [optional] 
**network_count** | **int** | Indicates how many networks are used by this VM. | [optional] 
**port_groups** | **[str]** |  | [optional] 
**protected_vm** | **bool** | Shows if this is a protected VM. VMs can be in protection groups. | [optional] 
**remote_display_info** | [**VirtualizationVmwareRemoteDisplayInfo**](VirtualizationVmwareRemoteDisplayInfo.md) |  | [optional] 
**remote_display_vnc_enabled** | **bool** | Shows if support for a remote VNC access is enabled. | [optional] 
**resource_pool** | **str** | Name of the resource pool to which this VM belongs (optional). | [optional] 
**resource_pool_owner** | **str** | Who owns the resource pool. | [optional] 
**resource_pool_parent** | **str** | The parent of the current resource pool to which this VM belongs. | [optional] 
**tool_running_status** | **str** | Indicates if guest tools are running on this VM. Could be set to guestToolNotRunning or guestToolsRunning. | [optional] 
**tools_version** | **str** | The version of the guest tools, usually not specified. | [optional] 
**vm_disk_count** | **int** | Shows the number of disks assigned to this VM. | [optional] 
**vm_overall_status** | **str** | The operational state of the VM. Could be Available, Provisioned, Maintenance mode, Deleting, etc. | [optional] 
**vm_path** | **str** | Example - [datastore3] VCSA-134/VCSA-134.vmx. | [optional] 
**vm_version** | **str** | Information about the version of this VM (vmx-09, vmx-11 etc.). | [optional] 
**vm_vnic_count** | **int** | How many vnics are present. | [optional] 
**vnic_device_config_id** | **str** | Information related to the guest info&#39;s VNIC virtual device. It is a comma-separated list. | [optional] 
**cluster** | [**VirtualizationVmwareClusterRelationship**](VirtualizationVmwareClusterRelationship.md) |  | [optional] 
**datacenter** | [**VirtualizationVmwareDatacenterRelationship**](VirtualizationVmwareDatacenterRelationship.md) |  | [optional] 
**datastores** | [**[VirtualizationVmwareDatastoreRelationship], none_type**](VirtualizationVmwareDatastoreRelationship.md) | An array of relationships to virtualizationVmwareDatastore resources. | [optional] [readonly] 
**host** | [**VirtualizationVmwareHostRelationship**](VirtualizationVmwareHostRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


