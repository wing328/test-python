# IamIdpAllOf

Definition of the list of properties defined in 'iam.Idp', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Email domain name of the user for this IdP. When a user enters an email during login in the Intersight home page, the IdP is picked by matching this domain name with the email domain name for authentication. | [optional] 
**idp_entity_id** | **str** | The Entity ID of the IdP. In SAML, the entity ID uniquely identifies the IdP or Service Provider. | [optional] [readonly] 
**metadata** | **str** | SAML metadata of the IdP. | [optional] 
**name** | **str** | The name of the Identity Provider, for example Cisco, Okta, or OneID. | [optional] 
**type** | **str** | Authentication protocol used by the IdP. | [optional]  if omitted the server will use the default value of "saml"
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**ldap_policy** | [**IamLdapPolicyRelationship**](IamLdapPolicyRelationship.md) |  | [optional] 
**system** | [**IamSystemRelationship**](IamSystemRelationship.md) |  | [optional] 
**user_preferences** | [**[IamUserPreferenceRelationship], none_type**](IamUserPreferenceRelationship.md) | An array of relationships to iamUserPreference resources. | [optional] [readonly] 
**usergroups** | [**[IamUserGroupRelationship], none_type**](IamUserGroupRelationship.md) | An array of relationships to iamUserGroup resources. | [optional] 
**users** | [**[IamUserRelationship], none_type**](IamUserRelationship.md) | An array of relationships to iamUser resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


