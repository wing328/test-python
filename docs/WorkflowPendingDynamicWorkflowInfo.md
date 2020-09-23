# WorkflowPendingDynamicWorkflowInfo

Information for a pending Dynamic Workflow Instance before it is run.  Validation needs to be done on the dynamic workflow tasks before starting.  After it begins, it will be tracked with regular WorkflowInstance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
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
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

