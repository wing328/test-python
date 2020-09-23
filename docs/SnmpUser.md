# SnmpUser

Complex type for a User based security model, for communication between an agent and manager. Applicable only for SNMPv3.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**auth_password** | **str** | Authorization password for the user. | [optional] 
**auth_type** | **str** | Authorization protocol for authenticating the user. | [optional]  if omitted the server will use the default value of "NA"
**is_auth_password_set** | **bool** | Indicates whether the value of the &#39;authPassword&#39; property has been set. | [optional] [readonly] 
**is_privacy_password_set** | **bool** | Indicates whether the value of the &#39;privacyPassword&#39; property has been set. | [optional] [readonly] 
**name** | **str** | SNMP username. Must have a minimum of 1 and and a maximum of 31 characters. | [optional] 
**privacy_password** | **str** | Privacy password for the user. | [optional] 
**privacy_type** | **str** | Privacy protocol for the user. | [optional]  if omitted the server will use the default value of "NA"
**security_level** | **str** | Security mechanism used for communication between agent and manager. | [optional]  if omitted the server will use the default value of "AuthPriv"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


