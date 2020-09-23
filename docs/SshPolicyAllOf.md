# SshPolicyAllOf

Definition of the list of properties defined in 'ssh.Policy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | State of SSH service on the endpoint. | [optional] 
**port** | **int** | Port used for secure shell access. | [optional] 
**timeout** | **int** | Number of seconds to wait before the system considers a SSH request to have timed out. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


