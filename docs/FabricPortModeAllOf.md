# FabricPortModeAllOf

Definition of the list of properties defined in 'fabric.PortMode', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_mode** | **str** | Custom Port Mode specified for the port range. | [optional]  if omitted the server will use the default value of "FibreChannel"
**port_id_end** | **int** | Ending range of the Port Identifier. | [optional] 
**port_id_start** | **int** | Starting range of the Port Identifier. | [optional] 
**slot_id** | **int** | Slot Identifier of the switch. | [optional] 
**port_policy** | [**FabricPortPolicyRelationship**](FabricPortPolicyRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


