# NtpPolicyAllOf

Definition of the list of properties defined in 'ntp.Policy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | State of NTP service on the endpoint. | [optional] 
**ntp_servers** | **[str]** |  | [optional] 
**timezone** | **str** | Timezone of services on the endpoint. | [optional]  if omitted the server will use the default value of "Pacific/Niue"
**appliance_account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


