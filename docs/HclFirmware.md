# HclFirmware

Model which holds the details of firmware version and driver version.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**driver_name** | **str** | Protocol for which the driver is provided. E.g.  enic, fnic, lsi_mr3. | [optional] 
**driver_version** | **str** | Version of the Driver supported. | [optional] 
**error_code** | **str** | Error code for the support status. | [optional] [readonly]  if omitted the server will use the default value of "Success"
**firmware_version** | **str** | Firmware version of the product/adapter supported. | [optional] 
**id** | **str** | Identifier of the firmware. | [optional] 
**latest_driver** | **bool** | True if the driver is latest recommended driver. | [optional] [readonly] 
**latest_firmware** | **bool** | True if the firmware is latest recommended firmware. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


