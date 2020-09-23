# IpmioverlanPolicyAllOf

Definition of the list of properties defined in 'ipmioverlan.Policy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | State of the IPMI Over LAN service on the endpoint. | [optional] 
**encryption_key** | **str** | The encryption key to use for IPMI communication. It should have an even number of hexadecimal characters and not exceed 40 characters. | [optional] 
**is_encryption_key_set** | **bool** | Indicates whether the value of the &#39;encryptionKey&#39; property has been set. | [optional] [readonly] 
**privilege** | **str** | The highest privilege level that can be assigned to an IPMI session on a server. | [optional]  if omitted the server will use the default value of "admin"
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


