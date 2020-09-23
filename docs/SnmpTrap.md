# SnmpTrap

Complex type that models a trap message sent from an agent to the manager.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**destination** | **str** | Address to which the SNMP trap information is sent. | [optional] 
**enabled** | **bool** | Enables/disables the trap on the server If enabled, trap is active on the server. | [optional] 
**port** | **int** | Port used by the server to communicate with trap destination. Enter a value between 1-65535. | [optional] 
**type** | **str** | Type of trap which decides whether to receive a notification when a trap is received at the destination. | [optional]  if omitted the server will use the default value of "Trap"
**user** | **str** | SNMP user for the trap. Applicable only to SNMPv3. | [optional] 
**version** | **str** | SNMP version used for the trap. | [optional]  if omitted the server will use the default value of "V3"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


