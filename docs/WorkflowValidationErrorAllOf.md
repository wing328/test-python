# WorkflowValidationErrorAllOf

Definition of the list of properties defined in 'workflow.ValidationError', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_log** | **bool, date, datetime, dict, float, int, list, str, none_type** | Description of the error.} type: string | [optional] [readonly] 
**field** | **str** | When populated this refers to the input or output field within the workflow or task. | [optional] [readonly] 
**task_name** | **str** | The task name on which the error is found, when empty the error applies to the top level workflow. | [optional] [readonly] 
**transition_name** | **str** | When populated this refers to the transition connection that has a problem. When this field has value OnSuccess it means the transition connection OnSuccess for the task has an issue. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


