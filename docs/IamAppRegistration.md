# IamAppRegistration

AppRegistration encapsulates the meta-data values of a registered OAuth2 client application, as described in https://tools.ietf.org/html/rfc7591#section-2. Registered client applications have a set of metadata values associated with their client identifier at the Intersight authorization server, including the list of valid redirection URIs or a display name. The meta-data is used to specify how a client application can retrieve a OAuth2 Access Token and subsequently invoke Intersight API on behalf of this AppRegistration. To register an OAuth2 application, the following information must be provided. 1) Application name 2) An icon for the application 3) URL to the application's home page 4) A short description of the application 5) A list of redirect URLs When an AppRegistration is created, a unique OAuth2 clientId is generated and returned in the HTTP response.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
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
**account_moid** | **str** | The Account ID for this managed object. | [optional] [readonly] 
**create_time** | **datetime** | The time when this managed object was created. | [optional] [readonly] 
**domain_group_moid** | **str** | The DomainGroup ID for this managed object. | [optional] [readonly] 
**mod_time** | **datetime** | The time when this managed object was last modified. | [optional] [readonly] 
**moid** | **str** | The unique identifier of this Managed Object instance. | [optional] 
**owners** | **[str]** |  | [optional] 
**shared_scope** | **str** | Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a &#39;shared&#39; ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs. | [optional] [readonly] 
**tags** | [**[MoTag]**](MoTag.md) |  | [optional] 
**version_context** | [**MoVersionContext**](MoVersionContext.md) |  | [optional] 
**ancestors** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**parent** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**permission_resources** | [**[MoBaseMoRelationship], none_type**](MoBaseMoRelationship.md) | An array of relationships to moBaseMo resources. | [optional] [readonly] 
**display_names** | [**DisplayNames**](DisplayNames.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


