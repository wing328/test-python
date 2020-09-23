# AdapterAdapterConfig

Global adapter level settings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**dce_interface_settings** | [**[AdapterDceInterfaceSettings]**](AdapterDceInterfaceSettings.md) |  | [optional] 
**eth_settings** | [**AdapterEthSettings**](AdapterEthSettings.md) |  | [optional] 
**fc_settings** | [**AdapterFcSettings**](AdapterFcSettings.md) |  | [optional] 
**port_channel_settings** | [**AdapterPortChannelSettings**](AdapterPortChannelSettings.md) |  | [optional] 
**slot_id** | **str** | PCIe slot where the VIC adapter is installed. Supported values are (1-15) and MLOM. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


