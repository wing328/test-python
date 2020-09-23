# FirmwareServerUpgradeImpact

Impact of the server endpoint during the upgrade operation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**impact_detail** | [**[FirmwareComponentImpact]**](FirmwareComponentImpact.md) |  | [optional] 
**name** | **str** | Name of the server impacted by the upgrade. | [optional] 
**user_label** | **str** | Details about the server which will be impacted by the upgrade. | [optional] 
**computation_error** | **str** | Details for the error that occurred during the reboot validation analysis. | [optional] 
**computation_status_detail** | **str** | The computation status of the estimate operation for a component. | [optional]  if omitted the server will use the default value of "Inprogress"
**domain_name** | **str** | The endpoint type or name. | [optional] 
**end_point** | **str** | A reference to a REST resource, uniquely identified by object type and MOID. | [optional] 
**firmware_version** | **str** | The current firmware version of the component. | [optional] 
**impact_type** | **str** | The impact type of the endpoint, whether a reboot is required or not. | [optional]  if omitted the server will use the default value of "NoReboot"
**model** | **str** | The model details of the component. | [optional] 
**target_firmware_version** | **str** | The target firmware version of the component. | [optional] 
**version_impact** | **str** | The change of version impact for the endpoint. | [optional]  if omitted the server will use the default value of "None"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


