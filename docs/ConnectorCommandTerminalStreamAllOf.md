# ConnectorCommandTerminalStreamAllOf

Definition of the list of properties defined in 'connector.CommandTerminalStream', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_type** | **str** | The type of data this message contains. | [optional] 
**sequence** | **int** | Sequence of the message within a session to handle out-of-order delivery. | [optional] 
**stream** | **str** | The input/output payload to/from the pseudo terminal session. When sent from the cloud service if the msgType is CommandInput stream is piped to stdin of the command or a resize message if msgType is CommandResize. From the device connector value is always the combined output of stdout &amp; stderr. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


