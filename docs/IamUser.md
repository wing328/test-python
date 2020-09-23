# IamUser

The Intersight account user.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path. | [readonly] 
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


