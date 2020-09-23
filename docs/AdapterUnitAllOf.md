# AdapterUnitAllOf

Definition of the list of properties defined in 'adapter.Unit', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adapter_id** | **str** | Unique Identifier of an adapter Unit within a Rack Interface. | [optional] [readonly] 
**base_mac_address** | **str** | Original Base Mac address of an adapter unit. | [optional] [readonly] 
**connection_status** | **str** | Connectivity Status of adapter - A or B or AB. | [optional] [readonly] 
**integrated** | **str** | Cisco Integrated adapter or other type. | [optional] [readonly] 
**oper_state** | **str** | Operational state of an adapter unit. | [optional] [readonly] 
**operability** | **str** | Operability state of an adapter unit. | [optional] [readonly] 
**part_number** | **str** | Part number of an adapter unit. | [optional] [readonly] 
**pci_slot** | **str** | PCIe slot of the adapter in the server. | [optional] [readonly] 
**power** | **str** | Power state of an adapter unit. | [optional] [readonly] 
**presence** | **str** | Adapter Unit presence or absence. | [optional] [readonly] 
**thermal** | **str** | Thermal state of an adapter unit. | [optional] [readonly] 
**vid** | **str** | Virtual Id of the adapter in the server. | [optional] [readonly] 
**compute_blade** | [**ComputeBladeRelationship**](ComputeBladeRelationship.md) |  | [optional] 
**compute_rack_unit** | [**ComputeRackUnitRelationship**](ComputeRackUnitRelationship.md) |  | [optional] 
**controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**ext_eth_ifs** | [**[AdapterExtEthInterfaceRelationship], none_type**](AdapterExtEthInterfaceRelationship.md) | An array of relationships to adapterExtEthInterface resources. | [optional] [readonly] 
**host_eth_ifs** | [**[AdapterHostEthInterfaceRelationship], none_type**](AdapterHostEthInterfaceRelationship.md) | An array of relationships to adapterHostEthInterface resources. | [optional] [readonly] 
**host_fc_ifs** | [**[AdapterHostFcInterfaceRelationship], none_type**](AdapterHostFcInterfaceRelationship.md) | An array of relationships to adapterHostFcInterface resources. | [optional] [readonly] 
**host_iscsi_ifs** | [**[AdapterHostIscsiInterfaceRelationship], none_type**](AdapterHostIscsiInterfaceRelationship.md) | An array of relationships to adapterHostIscsiInterface resources. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


