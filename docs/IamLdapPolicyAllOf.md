# IamLdapPolicyAllOf

Definition of the list of properties defined in 'iam.LdapPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_properties** | [**IamLdapBaseProperties**](IamLdapBaseProperties.md) |  | [optional] 
**dns_parameters** | [**IamLdapDnsParameters**](IamLdapDnsParameters.md) |  | [optional] 
**enable_dns** | **bool** | Enables DNS to access LDAP servers. | [optional] 
**enabled** | **bool** | LDAP server performs authentication. | [optional] 
**user_search_precedence** | **str** | Search precedence between local user database and LDAP user database. | [optional]  if omitted the server will use the default value of "LocalUserDb"
**_0_idp** | [**IamIdpRelationship**](IamIdpRelationship.md) |  | [optional] 
**appliance_account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**groups** | [**[IamLdapGroupRelationship], none_type**](IamLdapGroupRelationship.md) | An array of relationships to iamLdapGroup resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 
**providers** | [**[IamLdapProviderRelationship], none_type**](IamLdapProviderRelationship.md) | An array of relationships to iamLdapProvider resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


