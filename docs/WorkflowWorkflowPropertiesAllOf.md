# WorkflowWorkflowPropertiesAllOf

Definition of the list of properties defined in 'workflow.WorkflowProperties', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_meta** | **bool** | When set to false the workflow is owned by the system and used for internal services. Such workflows cannot be directly used by external entities. | [optional] 
**retryable** | **bool** | When true, this workflow can be retried if has not been modified for more than a period of 2 weeks. | [optional] 
**support_status** | **str** | Supported status of the definition. | [optional]  if omitted the server will use the default value of "Supported"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


