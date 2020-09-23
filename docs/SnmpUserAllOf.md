# SnmpUserAllOf

Definition of the list of properties defined in 'snmp.User', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_password** | **str** | Authorization password for the user. | [optional] 
**auth_type** | **str** | Authorization protocol for authenticating the user. | [optional]  if omitted the server will use the default value of "NA"
**is_auth_password_set** | **bool** | Indicates whether the value of the &#39;authPassword&#39; property has been set. | [optional] [readonly] 
**is_privacy_password_set** | **bool** | Indicates whether the value of the &#39;privacyPassword&#39; property has been set. | [optional] [readonly] 
**name** | **str** | SNMP username. Must have a minimum of 1 and and a maximum of 31 characters. | [optional] 
**privacy_password** | **str** | Privacy password for the user. | [optional] 
**privacy_type** | **str** | Privacy protocol for the user. | [optional]  if omitted the server will use the default value of "NA"
**security_level** | **str** | Security mechanism used for communication between agent and manager. | [optional]  if omitted the server will use the default value of "AuthPriv"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


