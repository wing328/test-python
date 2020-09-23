# ConnectorCommandControlMessageAllOf

Definition of the list of properties defined in 'connector.CommandControlMessage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | The working directory of the command. If empty command is executed in the same directory the device connector process was called. | [optional] 
**msg_type** | **str** | Message carrying the operation to perform. | [optional] 
**stream** | **str** | The command to execute. Commands must be whitelisted by platform implementation, if a command does not match any whitelisted command patterns an error will be returned to the requesting service on command start. | [optional] 
**terminal** | **bool** | Indicates that a pseudo terminal should be attached to the command. Used for interactive commands. e.g A cross launch cli. | [optional] 
**timeout** | **int** | The timeout for the command to complete and exit after starting or receiving input. If timeout is not set a default of 10 minutes will be used. If there is input to the command stream the timeout is extended. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


