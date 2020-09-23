# TerminalAuditLogAllOf

Definition of the list of properties defined in 'terminal.AuditLog', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **datetime** | The time the terminal was closed. If terminal has not closed, value is zero time. | [optional] [readonly] 
**start_time** | **datetime** | The time the terminal session was opened. | [optional] [readonly] 
**device_registration** | [**AssetDeviceConnectionRelationship**](AssetDeviceConnectionRelationship.md) |  | [optional] 
**user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


