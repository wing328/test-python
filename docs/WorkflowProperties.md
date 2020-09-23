# WorkflowProperties

Properties for the task definition like the inputs, outputs, timeout and retry policies. Tasks are the building blocks for workflows.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**external_meta** | **bool** | When set to false the task definition can only be used by internal system workflows. When set to true then the task can be included in user defined workflows. | [optional] 
**input_definition** | [**[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**output_definition** | [**[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**retry_count** | **int** | The number of times a task should be tried before marking as failed. | [optional] 
**retry_delay** | **int** | The delay in seconds after which the the task is re-tried. | [optional] 
**retry_policy** | **str** | The retry policy for the task. | [optional]  if omitted the server will use the default value of "Fixed"
**support_status** | **str** | Supported status of the definition. | [optional]  if omitted the server will use the default value of "Supported"
**timeout** | **int** | The timeout value in seconds after which task will be marked as timed out. Max allowed value is 7 days. | [optional] 
**timeout_policy** | **str** | The timeout policy for the task. | [optional]  if omitted the server will use the default value of "Timeout"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


