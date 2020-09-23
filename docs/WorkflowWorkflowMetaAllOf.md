# WorkflowWorkflowMetaAllOf

Definition of the list of properties defined in 'workflow.WorkflowMeta', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description for the workflow. | [optional] 
**input_parameters** | **[str]** |  | [optional] 
**name** | **str** | The name given to the workflow. | [optional] 
**output_parameters** | **bool, date, datetime, dict, float, int, list, str, none_type** | The workflow output parameters. | [optional] 
**retryable** | **bool** | When true, this workflow can be retried for 2 weeks since the last modification of the workflow. | [optional] 
**schema_version** | **int** | The Conductor schema version that decides what attribute can be supported. | [optional] 
**src** | **str** | The src is workflow owner service. | [optional] 
**tasks** | **bool, date, datetime, dict, float, int, list, str, none_type** | The tasks contained inside of the workflow. | [optional] 
**type** | **str** | The type of workflow definition. | [optional]  if omitted the server will use the default value of "SystemDefined"
**version** | **int** | The version for the workflow so we can support multiple versions for the same workflow name. | [optional] 
**wait_on_duplicate** | **bool** | Parameter decides if workflows will wait for a duplicate to finish before starting a new one. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


