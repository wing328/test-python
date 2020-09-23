# SyslogRemoteLoggingClient

Remote logging client for the endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**enabled** | **bool** | Enables/disables remote logging for the endpoint If enabled, log messages will be sent to the syslog server mentioned in the Hostname/IP Address field. | [optional] 
**hostname** | **str** | Hostname or IP Address of the syslog server where log should be stored. | [optional] 
**min_severity** | **str** | Lowest level of messages to be included in the remote log. | [optional]  if omitted the server will use the default value of "warning"
**port** | **int** | Port number used for logging on syslog server. | [optional] 
**protocol** | **str** | Transport layer protocol for transmission of log messages to syslog server. | [optional]  if omitted the server will use the default value of "udp"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


