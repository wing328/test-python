# IamLdapBaseProperties

Base settings of LDAP required while configuring LDAP policy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**attribute** | **str** | Role and locale information of the user. | [optional] 
**base_dn** | **str** | Base Distinguished Name (DN). Starting point from where server will search for users and groups. | [optional] 
**bind_dn** | **str** | Distinguished Name (DN) of the user, that is used to authenticate against LDAP servers. | [optional] 
**bind_method** | **str** | Authentication method to access LDAP servers. | [optional]  if omitted the server will use the default value of "LoginCredentials"
**domain** | **str** | The IPv4 domain that all users must be in. | [optional] 
**enable_encryption** | **bool** | If enabled, the endpoint encrypts all information it sends to the LDAP server. | [optional] 
**enable_group_authorization** | **bool** | If enabled, user authorization is also done at the group level for LDAP users not in the local user database. | [optional] 
**filter** | **str** | Criteria to identify entries in search requests. | [optional] 
**group_attribute** | **str** | Groups to which an LDAP entry belongs. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**nested_group_search_depth** | **int** | Search depth to look for a nested LDAP group in an LDAP group map. | [optional] 
**password** | **str** | Password of the user, that is used to authenticate. | [optional] 
**timeout** | **int** | LDAP authentication timeout duration, in seconds. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


