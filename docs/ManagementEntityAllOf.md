# ManagementEntityAllOf

Definition of the list of properties defined in 'management.Entity', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_link_state** | **str** | Cluster link state between the Fabric Interconnects. | [optional] [readonly] 
**cluster_readiness** | **str** | Cluster readiness of the Fabric Interconnect. | [optional] [readonly] 
**cluster_state** | **str** | Cluster state of the Fabric Interconnect. | [optional] [readonly] 
**entity_id** | **str** | Identity of the Fabric Interconnect - A/B. | [optional] [readonly] 
**leadership** | **str** | Role (Primary / Subordinate) of the Fabric Interconnect. | [optional] [readonly] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**network_element** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


