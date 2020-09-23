# ApplianceNodeInfoAllOf

Definition of the list of properties defined in 'appliance.NodeInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Cluster node&#39;s FQDN or IP address. | [optional] [readonly] 
**node_id** | **int** | System assigned unique ID of the Intersight Appliance node. The system incrementally assigns identifiers to each node in the Intersight Appliance cluster starting with a value of 1. | [optional] [readonly] 
**node_ip_v4_config** | [**CommIpV4Interface**](CommIpV4Interface.md) |  | [optional] 
**operational_status** | **str** | Operational status of the Intersight Appliance node. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

