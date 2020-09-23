# WorkflowBatchApiExecutorAllOf

Definition of the list of properties defined in 'workflow.BatchApiExecutor', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch** | [**[WorkflowApi]**](WorkflowApi.md) |  | [optional] 
**constraints** | [**WorkflowTaskConstraints**](WorkflowTaskConstraints.md) |  | [optional] 
**description** | **str** | A detailed description about the batch APIs. | [optional] 
**name** | **str** | Name for the batch API task. | [optional] 
**outcomes** | **bool, date, datetime, dict, float, int, list, str, none_type** | All the possible outcomes of this task are captured here. Outcomes property is a collection property of type workflow.Outcome objects. The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as &#39;true&#39;. This is an optional property and if not specified the task will be marked as success. | [optional] 
**output** | **bool, date, datetime, dict, float, int, list, str, none_type** | Intersight Orchestrator allows the extraction of required values from API responses using the API response grammar. These extracted values can be mapped to task output parameters defined in task definition. The mapping of API output parameters to the task output parameters is provided as JSON in this property. | [optional] 
**retry_from_failed_api** | **bool** | When an execution of a nth API in the Batch fails, Retry from falied API flag indicates if the execution should start from the nth API or the first API during task retry. By default the value is set to false. | [optional] 
**skip_on_condition** | **str** | The skip expression, if provided, allows the batch API executor to skip the task execution when the given expression evaluates to true. The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed. | [optional] 
**error_response_handler** | [**WorkflowErrorResponseHandlerRelationship**](WorkflowErrorResponseHandlerRelationship.md) |  | [optional] 
**task_definition** | [**WorkflowTaskDefinitionRelationship**](WorkflowTaskDefinitionRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


