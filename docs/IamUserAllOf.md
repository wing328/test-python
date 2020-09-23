# IamUserAllOf

Definition of the list of properties defined in 'iam.User', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_ip_address** | **str** | IP address from which the user last logged in to Intersight. | [optional] [readonly] 
**email** | **str** | Email of the user. Users are added to Intersight using the email configured in the IdP. | [optional] 
**first_name** | **str** | First name of the user. This field is populated from the IdP attributes received after authentication. | [optional] [readonly] 
**last_login_time** | **datetime** | Last successful login time for user. | [optional] [readonly] 
**last_name** | **str** | Last name of the user. This field is populated from the IdP attributes received after authentication. | [optional] [readonly] 
**name** | **str** | Name as configured in the IdP. | [optional] [readonly] 
**user_id_or_email** | **str** | UserID or email as configured in the IdP. | [optional] 
**user_type** | **str** | Type of the User. If a user is added manually by specifying the email address, or has logged in using groups, based on the IdP attributes received during authentication. If added manually, the user type will be static, otherwise dynamic. | [optional] [readonly] 
**user_unique_identifier** | **str** | Unique id of the user used by the identity provider to store the user. | [optional] [readonly] 
**api_keys** | [**[IamApiKeyRelationship], none_type**](IamApiKeyRelationship.md) | An array of relationships to iamApiKey resources. | [optional] [readonly] 
**app_registrations** | [**[IamAppRegistrationRelationship], none_type**](IamAppRegistrationRelationship.md) | An array of relationships to iamAppRegistration resources. | [optional] [readonly] 
**idp** | [**IamIdpRelationship**](IamIdpRelationship.md) |  | [optional] 
**idpreference** | [**IamIdpReferenceRelationship**](IamIdpReferenceRelationship.md) |  | [optional] 
**local_user_password** | [**IamLocalUserPasswordRelationship**](IamLocalUserPasswordRelationship.md) |  | [optional] 
**oauth_tokens** | [**[IamOAuthTokenRelationship], none_type**](IamOAuthTokenRelationship.md) | An array of relationships to iamOAuthToken resources. | [optional] [readonly] 
**permissions** | [**[IamPermissionRelationship], none_type**](IamPermissionRelationship.md) | An array of relationships to iamPermission resources. | [optional] 
**sessions** | [**[IamSessionRelationship], none_type**](IamSessionRelationship.md) | An array of relationships to iamSession resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


