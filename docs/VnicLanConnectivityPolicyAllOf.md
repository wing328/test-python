# VnicLanConnectivityPolicyAllOf

Definition of the list of properties defined in 'vnic.LanConnectivityPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_mode** | **str** | The mode used for placement of vnics on network adapters. It can either be Auto or Custom. | [optional]  if omitted the server will use the default value of "custom"
**target_platform** | **str** | The platform for which the server profile is applicable. It can either be a server that is operating in standalone mode or which is attached to a Fabric Interconnect managed by Intersight. | [optional]  if omitted the server will use the default value of "Standalone"
**eth_ifs** | [**[VnicEthIfRelationship], none_type**](VnicEthIfRelationship.md) | An array of relationships to vnicEthIf resources. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


