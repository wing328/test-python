# VirtualizationVmwareHostAllOf

Definition of the list of properties defined in 'virtualization.VmwareHost', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_time** | **datetime** | The time when this host booted up. | [optional] 
**connection_state** | **str** | Indicates if the host is connected to the vCenter. Values are connected, not connected. | [optional] 
**hw_power_state** | **str** | Is the host Powered-up or Powered-down. | [optional]  if omitted the server will use the default value of "Unknown"
**network_adapter_count** | **int** | The count of all network adapters attached to this host. | [optional] 
**resource_consumed** | [**VirtualizationVmwareResourceConsumption**](VirtualizationVmwareResourceConsumption.md) |  | [optional] 
**storage_adapter_count** | **int** | The count of all storage adapters attached to this host. | [optional] 
**vcenter_host_id** | **str** | The identity of this host within vCenter (optional). | [optional] 
**cluster** | [**VirtualizationVmwareClusterRelationship**](VirtualizationVmwareClusterRelationship.md) |  | [optional] 
**datacenter** | [**VirtualizationVmwareDatacenterRelationship**](VirtualizationVmwareDatacenterRelationship.md) |  | [optional] 
**datastores** | [**[VirtualizationVmwareDatastoreRelationship], none_type**](VirtualizationVmwareDatastoreRelationship.md) | An array of relationships to virtualizationVmwareDatastore resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


