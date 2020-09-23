# ConnectorFileMessageAllOf

Definition of the list of properties defined in 'connector.FileMessage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**msg_type** | **str** | Message type carrying the file operation to perform. | [optional]  if omitted the server will use the default value of "OpenFile"
**path** | **str** | The absolute path of the file to open on the platforms file system. Must be a sub-directory of a directory defined within the platform configurations WriteableDirectories. The file system device to write to must also have sufficient free space to write to (&lt;75% full). Must be set for each message that is sent. | [optional] 
**stream** | **str** | The stream of bytes to write to file. Only applicable for FileContent message. Ignored for OpenFile and CloseFile messages. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


