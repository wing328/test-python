# IamOAuthTokenAllOf

Definition of the list of properties defined in 'iam.OAuthToken', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_expiration_time** | **datetime** | Expiration time for the JWT token to which it can be used for api calls. | [optional] [readonly] 
**client_id** | **str** | The identifier of the registered application to which the token belongs. | [optional] 
**client_ip_address** | **str** | The user agent IP address from which the auth token is launched. | [optional] [readonly] 
**client_name** | **str** | The name of the registered application to which the token belongs. | [optional] 
**expiration_time** | **datetime** | Expiration time for the JWT token to which it can be refreshed. | [optional] [readonly] 
**last_login_client** | **str** | The client address from which last login is initiated. | [optional] [readonly] 
**last_login_time** | **datetime** | The last login time for user. | [optional] [readonly] 
**token_id** | **str** | Token identifier. Not the Access Token itself. | [optional] [readonly] 
**user_meta** | [**IamClientMeta**](IamClientMeta.md) |  | [optional] 
**app_registration** | [**IamAppRegistrationRelationship**](IamAppRegistrationRelationship.md) |  | [optional] 
**permission** | [**IamPermissionRelationship**](IamPermissionRelationship.md) |  | [optional] 
**user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

