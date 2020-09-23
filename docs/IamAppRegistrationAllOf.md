# IamAppRegistrationAllOf

Definition of the list of properties defined in 'iam.AppRegistration', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | A unique identifier for the OAuth2 client application. The client ID is auto-generated when the AppRegistration object is created. | [optional] [readonly] 
**client_name** | **str** | App Registration name specified by user. | [optional] 
**client_secret** | **str** | The OAuth2 client secret. The value of this property is generated when grantType includes &#39;client-credentials&#39;. Otherwise, no client-secret is generated. | [optional] 
**client_type** | **str** | The type of the OAuth2 client (public or confidential), as specified in https://tools.ietf.org/html/rfc6749#section-2.1. | [optional]  if omitted the server will use the default value of "public"
**description** | **str** | Description of the application. | [optional] 
**grant_types** | **[str]** |  | [optional] 
**redirect_uris** | **[str]** |  | [optional] 
**renew_client_secret** | **bool** | Set value to true to renew the client-secret. Applicable to client_credentials grant type. | [optional] 
**response_types** | **[str]** |  | [optional] 
**revocation_timestamp** | **datetime** | Used to perform revocation for tokens of AppRegistration. Updated only internally is case Revoke property come from UI with value true. On each request with OAuth2 access token the CreationTime of the OAuth2 token will be compared to RevokationTimestamp of the corresponding App Registration. | [optional] [readonly] 
**revoke** | **bool** | Used to trigger update the revocationTimestamp value. If UI sent updating request with the Revoke value is true, then update RevocationTimestamp. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**oauth_tokens** | [**[IamOAuthTokenRelationship], none_type**](IamOAuthTokenRelationship.md) | An array of relationships to iamOAuthToken resources. | [optional] [readonly] 
**permission** | [**IamPermissionRelationship**](IamPermissionRelationship.md) |  | [optional] 
**roles** | [**[IamRoleRelationship], none_type**](IamRoleRelationship.md) | An array of relationships to iamRole resources. | [optional] 
**user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


