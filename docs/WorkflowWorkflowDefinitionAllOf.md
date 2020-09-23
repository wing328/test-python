# WorkflowWorkflowDefinitionAllOf

Definition of the list of properties defined in 'workflow.WorkflowDefinition', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_version** | **bool** | When true this will be the workflow version that is used when a specific workflow definition version is not specified. The default version is used when user executes a workflow without specifying a version or when workflow is included in another workflow without a specific version. The very first workflow definition created with a name will be set as the default version, after that user can explicitly set any version of the workflow definition as the default version. | [optional] 
**description** | **str** | The description for this workflow. | [optional] 
**input_definition** | [**[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**label** | **str** | A user friendly short name to identify the workflow. Name can only contain letters (a-z, A-Z), numbers (0-9), hyphen (-), period (.), colon (:), space ( ) or an underscore (_). | [optional] 
**license_entitlement** | **str** | License entitlement required to run this workflow. It is calculated based on the highest license requirement of all its tasks. | [optional] [readonly]  if omitted the server will use the default value of "Base"
**max_task_count** | **int** | The maximum number of tasks that can be executed on this workflow. | [optional] [readonly] 
**name** | **str** | The name for this workflow. You can have multiple versions of the workflow with the same name. Name can only contain letters (a-z, A-Z), numbers (0-9), hyphen (-), period (.) or an underscore (_). | [optional] 
**output_definition** | [**[WorkflowBaseDataType]**](WorkflowBaseDataType.md) |  | [optional] 
**output_parameters** | **bool, date, datetime, dict, float, int, list, str, none_type** | The output mappings for the workflow. The outputs for worflows will generally be task output variables that we want to export out at the end of the workflow. The format to specify the mapping is &#39;${Source.output.JsonPath}&#39;. &#39;Source&#39; is the name of the task within the workflow. You can map any task output to a workflow output as long as the types are compatible. Following this is JSON path expression to extract JSON fragment from source&#39;s output. | [optional] 
**properties** | [**WorkflowWorkflowProperties**](WorkflowWorkflowProperties.md) |  | [optional] 
**tasks** | [**[WorkflowWorkflowTask]**](WorkflowWorkflowTask.md) |  | [optional] 
**ui_rendering_data** | **bool, date, datetime, dict, float, int, list, str, none_type** | This will hold the data needed for workflow to be rendered in the user interface. | [optional] 
**validation_information** | [**WorkflowValidationInformation**](WorkflowValidationInformation.md) |  | [optional] 
**version** | **int** | The version of the workflow to support multiple versions. | [optional] 
**catalog** | [**WorkflowCatalogRelationship**](WorkflowCatalogRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


