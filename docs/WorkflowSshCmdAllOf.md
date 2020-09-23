# WorkflowSshCmdAllOf

Definition of the list of properties defined in 'workflow.SshCmd', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | SSH command to execute on the remote server. | [optional] 
**command_type** | **str** | SSH command type to execute on the remote server. | [optional]  if omitted the server will use the default value of "NonInteractiveCmd"
**expect_prompts** | [**[ConnectorExpectPrompt]**](ConnectorExpectPrompt.md) |  | [optional] 
**shell_prompt** | **str** | Regex of the remote server&#39;s shell prompt. | [optional] 
**shell_prompt_timeout** | **int** | Expect timeout value in seconds for the shell prompt. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


