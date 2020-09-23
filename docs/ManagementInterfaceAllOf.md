# ManagementInterfaceAllOf

Definition of the list of properties defined in 'management.Interface', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway** | **str** | Default gateway for the interface. | [optional] [readonly] 
**host_name** | **str** | Hostname configured for the interface. | [optional] 
**ip_address** | **str** | IP address of the interface. | [optional] [readonly] 
**ipv4_address** | **str** | IPv4 address of the interface. | [optional] [readonly] 
**ipv4_gateway** | **str** | IPv4 default gateway for the interface. | [optional] [readonly] 
**ipv4_mask** | **str** | IPv4 Netmask for the interface. | [optional] [readonly] 
**ipv6_address** | **str** | IPv6 address of the interface. | [optional] 
**ipv6_gateway** | **str** | IPv6 default gateway for the interface. | [optional] 
**ipv6_prefix** | **int** | IPv6 prefix for the interface. | [optional] 
**mac_address** | **str** | MAC address configured for the interface. | [optional] [readonly] 
**mask** | **str** | Netmask for the interface. | [optional] [readonly] 
**switch_id** | **str** | Switch Id connected to the interface. | [optional] 
**uem_conn_status** | **str** | The event channel connection status for the interface. | [optional] 
**virtual_host_name** | **str** | Virtual hostname configured for the interface in case of clustered environment. | [optional] 
**inventory_device_info** | [**InventoryDeviceInfoRelationship**](InventoryDeviceInfoRelationship.md) |  | [optional] 
**management_controller** | [**ManagementControllerRelationship**](ManagementControllerRelationship.md) |  | [optional] 
**registered_device** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


