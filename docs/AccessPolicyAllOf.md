# AccessPolicyAllOf

Definition of the list of properties defined in 'access.Policy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inband_vlan** | **int** | VLAN to be used for server access over Inband network. | [optional] 
**inband_ip_pool** | [**IppoolPoolRelationship**](IppoolPoolRelationship.md) |  | [optional] 
**inband_vrf** | [**VrfVrfRelationship**](VrfVrfRelationship.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


