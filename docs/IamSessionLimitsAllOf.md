# IamSessionLimitsAllOf

Definition of the list of properties defined in 'iam.SessionLimits', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idle_time_out** | **int** | The idle timeout interval for the web session in seconds. When a session is not refreshed for this duration, the session is marked as idle and removed. | [optional] 
**maximum_limit** | **int** | The maximum number of sessions allowed in an account. The default value is 128. | [optional] [readonly] 
**per_user_limit** | **int** | The maximum number of sessions allowed per user. Default value is 32. | [optional] [readonly] 
**session_time_out** | **int** | The session expiry duration in seconds. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**permission** | [**IamPermissionRelationship**](IamPermissionRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


