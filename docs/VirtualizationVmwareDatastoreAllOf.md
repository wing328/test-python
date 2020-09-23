# VirtualizationVmwareDatastoreAllOf

Definition of the list of properties defined in 'virtualization.VmwareDatastore', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessible** | **bool** | Shows if this datastore is accessible. | [optional] 
**maintenance_mode** | **bool** | Indicates if the datastore is in maintenance mode. Will be set to True, when in maintenance mode. | [optional] 
**multiple_host_access** | **bool** | Indicates if this datastore is connected to multiple hosts. | [optional] 
**status** | **str** | Datastore health status, as reported by the hypervisor platform. | [optional]  if omitted the server will use the default value of "Unknown"
**thin_provisioning_supported** | **bool** | Indicates if this datastore supports thin provisioning for files. | [optional] 
**un_committed** | **int** | Space uncommitted in this datastore in bytes. | [optional] 
**url** | **str** | The URL to access this datastore (example - &#39;ds:///vmfs/volumes/562a4e8a-0eeb5372-dd61-78baf9cb9afa/&#39;). | [optional] 
**cluster** | [**VirtualizationVmwareClusterRelationship**](VirtualizationVmwareClusterRelationship.md) |  | [optional] 
**datacenter** | [**VirtualizationVmwareDatacenterRelationship**](VirtualizationVmwareDatacenterRelationship.md) |  | [optional] 
**hosts** | [**[VirtualizationVmwareHostRelationship], none_type**](VirtualizationVmwareHostRelationship.md) | An array of relationships to virtualizationVmwareHost resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


