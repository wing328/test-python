# AssetManagedDeviceStatus

Maintains the Managed Device Status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**cloud_port** | **int** | Port used for the connection to the Cloud by the Device Connector for the Managed Device. | [optional] 
**connection_failure_reason** | **str** | Maintains the reason for the failure of connection to the Device in case of connection failure. | [optional] 
**connection_status** | **str** | Maintains the status of the connection to the Device. | [optional]  if omitted the server will use the default value of "Unknown"
**error_code** | **int** | Maintains code related to error from Device Connector, if any. | [optional] 
**error_reason** | **str** | Maintains the reason for the error from Device Connector, if any. | [optional] 
**process_id** | **int** | Maintains the process pid of the Device Connector for the Managed Device. | [optional] 
**server_port** | **int** | Port used for receiving requests from Intersight Assist by the Device Connector for the Managed Device. | [optional] 
**state** | **str** | Maintains the state of the Managed Device, such as Start Success, Start Failure, etc. See ManagedDeviceState for device connection states. | [optional]  if omitted the server will use the default value of "New"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


