# IamOAuthToken

The meta data for generating OAuth2 token of a user. It is created when user logged in via OAuth2 using Authorization Code grant and deleted upon logout, expiration timeout or manual deletion.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
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


