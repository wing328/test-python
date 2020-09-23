# WorkflowSshSessionAllOf

Definition of the list of properties defined in 'workflow.SshSession', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_transfer_to_remote** | [**WorkflowFileTransfer**](WorkflowFileTransfer.md) |  | [optional] 
**message_type** | **str** | The type of SSH message to send to the remote server. | [optional]  if omitted the server will use the default value of "ExecuteCommand"
**ssh_command** | [**WorkflowSshCmd**](WorkflowSshCmd.md) |  | [optional] 
**ssh_configuration** | [**WorkflowSshConfig**](WorkflowSshConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


