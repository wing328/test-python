# WorkflowTaskInfoAllOf

Definition of the list of properties defined in 'workflow.TaskInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The task description and this is the description that was added when the task was included into the workflow. | [optional] [readonly] 
**end_time** | **datetime** | The time stamp when the task reached a final state. | [optional] [readonly] 
**failure_reason** | **str** | Description of the reason why the task failed. | [optional] [readonly] 
**input** | **bool, date, datetime, dict, float, int, list, str, none_type** | The input data that was sent to the task at the start of execution. | [optional] [readonly] 
**inst_id** | **str** | The instance ID of the task running in the workflow engine. | [optional] [readonly] 
**internal** | **bool** | Denotes whether or not this is an internal task.  Internal tasks will be hidden from the UI within a workflow. | [optional] [readonly] 
**label** | **str** | User friendly short label to describe this task instance in the workflow. | [optional] [readonly] 
**message** | [**[WorkflowMessage]**](WorkflowMessage.md) |  | [optional] 
**name** | **str** | Task definition name which specifies the task type. | [optional] [readonly] 
**output** | **bool, date, datetime, dict, float, int, list, str, none_type** | The output data that was generated by this task. | [optional] [readonly] 
**ref_name** | **str** | The task reference name to ensure its unique inside a workflow. | [optional] [readonly] 
**retry_count** | **int** | A counter for number of retries. | [optional] [readonly] 
**running_inst_id** | **str** | The instance ID of the task that is currently being executed. When retrying a workflow with failed tasks, the task in workflow engine will have a new instance ID, but the task may still be in-progress. In this case, the task instId reflects the instance ID in the workflow engine, while runningInstId reflects the instance ID of the instance that is currently being executed. | [optional] [readonly] 
**start_time** | **datetime** | The time stamp when the task started execution. | [optional] [readonly] 
**status** | **str** | The status of the task and this will specify if the task is running or has reached a final state. | [optional] 
**task_inst_id_list** | [**[WorkflowTaskRetryInfo]**](WorkflowTaskRetryInfo.md) |  | [optional] 
**sub_workflow_info** | [**WorkflowWorkflowInfoRelationship**](WorkflowWorkflowInfoRelationship.md) |  | [optional] 
**task_definition** | [**WorkflowTaskDefinitionRelationship**](WorkflowTaskDefinitionRelationship.md) |  | [optional] 
**workflow_info** | [**WorkflowWorkflowInfoRelationship**](WorkflowWorkflowInfoRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

