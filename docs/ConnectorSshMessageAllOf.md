# ConnectorSshMessageAllOf

Definition of the list of properties defined in 'connector.SshMessage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expect_prompts** | [**[ConnectorExpectPrompt]**](ConnectorExpectPrompt.md) |  | [optional] 
**msg_type** | **int** | The operation to execute on a new or existing session. | [optional] 
**session_id** | **str** | Unique id of session to route messages to. | [optional] 
**shell_prompt** | **str** | The regex of the secure shell prompt. | [optional] 
**stream** | **str** | Input to the SSH operation to be executed. e.g. file contents to write. | [optional] 
**timeout** | **int** | The timeout for the ssh command to complete and exit after starting or receiving input. If timeout is not set a default of 10 minutes will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


