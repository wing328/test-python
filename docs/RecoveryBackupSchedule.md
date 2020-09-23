# RecoveryBackupSchedule

Encapsulates the various backup settings available to the user for scheduling a backup on the endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**execution_time** | **datetime** | The time at which the backup is to be run on a given day. This is used when the frequency unit is daily. | [optional] 
**frequency_unit** | **str** | The frequency at which the backup schedule must run. | [optional]  if omitted the server will use the default value of "Daily"
**hours** | **int** | The frequency, in hours, at which the backup schedule runs. | [optional]  if omitted the server will use the default value of 8
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


