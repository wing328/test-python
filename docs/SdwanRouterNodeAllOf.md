# SdwanRouterNodeAllOf

Definition of the list of properties defined in 'sdwan.RouterNode', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_template** | **str** | Name of the Cisco vManage device template that the current device should be attached to. A device template consists of many feature templates that contain SD-WAN vEdge router configuration. | [optional] 
**name** | **str** | Name of the router node object. | [optional] 
**network_configuration** | [**[SdwanNetworkConfigurationType]**](SdwanNetworkConfigurationType.md) |  | [optional] 
**template_inputs** | [**[SdwanTemplateInputsType]**](SdwanTemplateInputsType.md) |  | [optional] 
**uuid** | **str** | Uniquely identifies the router by its chassis number. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profile** | [**SdwanProfileRelationship**](SdwanProfileRelationship.md) |  | [optional] 
**server_node** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


