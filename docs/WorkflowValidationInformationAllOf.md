# WorkflowValidationInformationAllOf

Definition of the list of properties defined in 'workflow.ValidationInformation', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The current validation state of this workflow. The possible states are Valid, Invalid, NotValidated (default). | [optional] [readonly]  if omitted the server will use the default value of "NotValidated"
**validation_error** | [**[WorkflowValidationError]**](WorkflowValidationError.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


