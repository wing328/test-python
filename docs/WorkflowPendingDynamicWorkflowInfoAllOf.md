# WorkflowPendingDynamicWorkflowInfoAllOf

Definition of the list of properties defined in 'workflow.PendingDynamicWorkflowInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **bool, date, datetime, dict, float, int, list, str, none_type** | The inputs of the workflow. | [optional] 
**name** | **str** | A name for the pending dynamic workflow. | [optional] 
**pending_services** | **[str]** |  | [optional] 
**src** | **str** | The src is workflow owner service. | [optional] 
**status** | **str** | The current status of the PendingDynamicWorkflowInfo. | [optional]  if omitted the server will use the default value of "GatheringTasks"
**wait_on_duplicate** | **bool** | When set to true workflow engine will wait for a duplicate to finish before starting a new one. | [optional] 
**workflow_action_task_lists** | [**[WorkflowDynamicWorkflowActionTaskList]**](WorkflowDynamicWorkflowActionTaskList.md) |  | [optional] 
**workflow_ctx** | **bool, date, datetime, dict, float, int, list, str, none_type** | The workflow&#39;s workflow context which contains initiator and target information. | [optional] 
**workflow_key** | **str** | This key contains workflow, initiator and target name. Workflow engine uses the key to do workflow dedup. | [optional] 
**workflow_meta** | **bool, date, datetime, dict, float, int, list, str, none_type** | The metadata of the workflow. | [optional] 
**workflow_info** | [**WorkflowWorkflowInfoRelationship**](WorkflowWorkflowInfoRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


