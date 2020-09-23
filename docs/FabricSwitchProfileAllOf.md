# FabricSwitchProfileAllOf

Definition of the list of properties defined in 'fabric.SwitchProfile', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_changes** | [**PolicyConfigChange**](PolicyConfigChange.md) |  | [optional] 
**assigned_switch** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 
**associated_switch** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 
**config_change_details** | [**[FabricConfigChangeDetailRelationship], none_type**](FabricConfigChangeDetailRelationship.md) | An array of relationships to fabricConfigChangeDetail resources. | [optional] [readonly] 
**config_result** | [**FabricConfigResultRelationship**](FabricConfigResultRelationship.md) |  | [optional] 
**running_workflows** | [**[WorkflowWorkflowInfoRelationship], none_type**](WorkflowWorkflowInfoRelationship.md) | An array of relationships to workflowWorkflowInfo resources. | [optional] [readonly] 
**switch_cluster_profile** | [**FabricSwitchClusterProfileRelationship**](FabricSwitchClusterProfileRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


