# WorkflowPropertiesAllOf

Definition of the list of properties defined in 'workflow.Properties', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_meta** | **bool** | When set to false the task definition can only be used by internal system workflows. When set to true then the task can be included in user defined workflows. | [optional] 
**input_definition** | [**[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**output_definition** | [**[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**retry_count** | **int** | The number of times a task should be tried before marking as failed. | [optional] 
**retry_delay** | **int** | The delay in seconds after which the the task is re-tried. | [optional] 
**retry_policy** | **str** | The retry policy for the task. | [optional]  if omitted the server will use the default value of "Fixed"
**support_status** | **str** | Supported status of the definition. | [optional]  if omitted the server will use the default value of "Supported"
**timeout** | **int** | The timeout value in seconds after which task will be marked as timed out. Max allowed value is 7 days. | [optional] 
**timeout_policy** | **str** | The timeout policy for the task. | [optional]  if omitted the server will use the default value of "Timeout"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


