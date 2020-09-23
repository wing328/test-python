# WorkflowWorkflowInfoRelationship

A relationship to the 'workflow.WorkflowInfo' resource, or the expanded 'workflow.WorkflowInfo' resource, or the 'null' value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] defaults to nulltype.Null
**account_moid** | **str** | The Account ID for this managed object. | [optional] [readonly] 
**create_time** | **datetime** | The time when this managed object was created. | [optional] [readonly] 
**domain_group_moid** | **str** | The DomainGroup ID for this managed object. | [optional] [readonly] 
**mod_time** | **datetime** | The time when this managed object was last modified. | [optional] [readonly] 
**moid** | **str** | The unique identifier of this Managed Object instance. | [optional] 
**owners** | **[str]** |  | [optional] 
**shared_scope** | **str** | Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs. | [optional] [readonly] 
**tags** | [**[MoTag]**](MoTag.md) |  | [optional] 
**version_context** | [**MoVersionContext**](MoVersionContext.md) |  | [optional] 
**ancestors** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**parent** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**permission_resources** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**display_names** | [**DisplayNames**](DisplayNames.md) |  | [optional] 
**action** | **str** | The action of the workflow such as start, cancel, retry, pause. | [optional]  if omitted the server will use the default value of "None"
**cleanup_time** | **datetime** | The time when the workflow info will be removed from database. | [optional] [readonly] 
**end_time** | **datetime** | The time when the workflow reached a final state. | [optional] [readonly] 
**failed_workflow_cleanup_duration** | **int** | The duration in hours after which the workflow info for failed, terminated or timed out workflow will be removed from database. | [optional] 
**input** | **bool, date, datetime, dict, float, int, list, str, none_type** | All the given inputs for the workflow. | [optional] 
**inst_id** | **str** | A workflow instance Id which is the unique identified for the workflow execution. | [optional] [readonly] 
**internal** | **bool** | Denotes if this workflow is internal and should be hidden from user view of running workflows. | [optional] 
**last_action** | **str** | The last action that was issued on the workflow is saved in this field. | [optional] [readonly]  if omitted the server will use the default value of "None"
**message** | [**[WorkflowMessage]**](WorkflowMessage.md) |  | [optional] 
**meta_version** | **int** | Version of the workflow metadata for which this workflow execution was started. | [optional] 
**name** | **str** | A name of the workflow execution instance. | [optional] 
**output** | **bool, date, datetime, dict, float, int, list, str, none_type** | All the generated outputs for the workflow. | [optional] [readonly] 
**pause_reason** | **str** | Denotes the reason workflow is in paused status. | [optional]  if omitted the server will use the default value of "None"
**progress** | **float** | This field indicates percentage of workflow task execution. | [optional] [readonly] 
**properties** | [**WorkflowWorkflowInfoProperties**](WorkflowWorkflowInfoProperties.md) |  | [optional] 
**retry_from_task_name** | **str** | This field is applicable when Retry action is issued for a workflow which is in a final state. When this field is not specified then the workflow will retry from the start of the workflow. When this field is specified then the workflow will be retried from the specified task. The field should carry the task name which is the unique name of the task within the workflow. The task name must be one of the tasks that completed or failed in the previous run, you cannot retry a workflow from a task which wasn&#39;t run in the previous iteration. | [optional] 
**src** | **str** | The source microservice name which is the owner for this workflow. | [optional] [readonly] 
**start_time** | **datetime** | The time when the workflow was started for execution. | [optional] [readonly] 
**status** | **str** | A status of the workflow (RUNNING, WAITING, COMPLETED, TIME_OUT, FAILED). | [optional] [readonly] 
**success_workflow_cleanup_duration** | **int** | The duration in hours after which the workflow info for successful workflow will be removed from database. | [optional] 
**trace_id** | **str** | The trace id to keep track of workflow execution. | [optional] [readonly] 
**type** | **str** | A type of the workflow (serverconfig, ansible_monitoring). | [optional] [readonly] 
**user_id** | **str** | The user identifier which indicates the user that started this workflow. | [optional] [readonly] 
**wait_reason** | **str** | Denotes the reason workflow is in waiting status. | [optional]  if omitted the server will use the default value of "None"
**workflow_ctx** | **bool, date, datetime, dict, float, int, list, str, none_type** | The workflow context which contains initiator and target information. | [optional] 
**workflow_meta_type** | **str** | The type of workflow meta. Derived from the workflow meta that is used to launch this workflow instance. | [optional]  if omitted the server will use the default value of "SystemDefined"
**workflow_task_count** | **int** | Total number of workflow tasks in this workflow. | [optional] [readonly] 
**_0_switch_profile** | [**FabricSwitchProfileRelationship**](FabricSwitchProfileRelationship.md) |  | [optional] 
**_1_cluster_profile** | [**HyperflexClusterProfileRelationship**](HyperflexClusterProfileRelationship.md) |  | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**associated_object** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**parent_task_info** | [**WorkflowTaskInfoRelationship**](WorkflowTaskInfoRelationship.md) |  | [optional] 
**pending_dynamic_workflow_info** | [**WorkflowPendingDynamicWorkflowInfoRelationship**](WorkflowPendingDynamicWorkflowInfoRelationship.md) |  | [optional] 
**permission** | [**IamPermissionRelationship**](IamPermissionRelationship.md) |  | [optional] 
**task_infos** | [**[WorkflowTaskInfoRelationship], none_type**](WorkflowTaskInfoRelationship.md) | An array of relationships to workflowTaskInfo resources. | [optional] [readonly] 
**workflow_definition** | [**WorkflowWorkflowDefinitionRelationship**](WorkflowWorkflowDefinitionRelationship.md) |  | [optional] 
**selector** | **str** | An OData $filter expression which describes the REST resource to be referenced. This field may be set instead of &#39;moid&#39; by clients. 1. If &#39;moid&#39; is set this field is ignored. 1. If &#39;selector&#39; is set and &#39;moid&#39; is empty/absent from the request, Intersight determines the Moid of the resource matching the filter expression and populates it in the MoRef that is part of the object instance being inserted/updated to fulfill the REST request. An error is returned if the filter matches zero or more than one REST resource. An example filter string is: Serial eq &#39;3AA8B7T11&#39;. | [optional] [readonly] 
**link** | **str** | A URL to an instance of the &#39;mo.MoRef&#39; class. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


