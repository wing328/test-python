# IamIdpReferenceAllOf

Definition of the list of properties defined in 'iam.IdpReference', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | The email domain name for this IdP of the user. When a user enters an email during login in the Intersight home page, the IdP is picked by matching this domain name with the email domain name for authentication. | [optional] [readonly] 
**idp_entity_id** | **str** | Entity ID of the IdP. In SAML, the entity ID uniquely identifies the IdP/Service Provider. | [optional] [readonly] 
**multi_factor_authentication** | **bool** | The flag represents if the second factor of authentication is required for Cisco IdP users. | [optional] 
**name** | **str** | Cisco IdP reference in an account. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**idp** | [**IamIdpRelationship**](IamIdpRelationship.md) |  | [optional] 
**user_preferences** | [**[IamUserPreferenceRelationship], none_type**](IamUserPreferenceRelationship.md) | An array of relationships to iamUserPreference resources. | [optional] [readonly] 
**usergroups** | [**[IamUserGroupRelationship], none_type**](IamUserGroupRelationship.md) | An array of relationships to iamUserGroup resources. | [optional] 
**users** | [**[IamUserRelationship], none_type**](IamUserRelationship.md) | An array of relationships to iamUser resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


