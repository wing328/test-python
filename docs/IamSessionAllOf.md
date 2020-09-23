# IamSessionAllOf

Definition of the list of properties defined in 'iam.Session', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_permissions** | [**[IamAccountPermissions]**](IamAccountPermissions.md) |  | [optional] 
**client_ip_address** | **str** | The user agent IP address from which the session is launched. | [optional] [readonly] 
**expiration** | **datetime** | Expiration time for the session. | [optional] [readonly] 
**idle_time_expiration** | **datetime** | Idle time expiration for the session. | [optional] [readonly] 
**last_login_client** | **str** | The client address from which last login is initiated. | [optional] [readonly] 
**last_login_time** | **datetime** | The last login time for user. | [optional] [readonly] 
**permission** | [**IamPermissionRelationship**](IamPermissionRelationship.md) |  | [optional] 
**user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


