# FirmwareComponentMeta

Contains the details for each component in the HSU bundle catalog.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**component_label** | **str** | The name of the component in the compressed HSU bundle. | [optional] 
**component_type** | **str** | The type of component image within the distributable. | [optional]  if omitted the server will use the default value of "ALL"
**description** | **str** | This shows the description of component image within the distributable. | [optional] 
**disruption** | **str** | The type of disruption on each component. For example, host reboot, automatic power cycle, and manual power cycle. | [optional]  if omitted the server will use the default value of "None"
**is_oob_supported** | **bool** | If set, the component can be updated through out-of-band management, else, is updated through the booting host service utility. | [optional] 
**model** | **str** | The model of the component image in the distributable. | [optional] 
**oob_manageability** | **[str]** |  | [optional] 
**packed_version** | **str** | The packaged version of component image within the distributable. | [optional] 
**redfish_url** | **str** | The redfish target for each component. | [optional] 
**vendor** | **str** | The version of the component image in the distributable. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


