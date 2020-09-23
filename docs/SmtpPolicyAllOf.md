# SmtpPolicyAllOf

Definition of the list of properties defined in 'smtp.Policy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If enabled, controls the state of the SMTP client service on the managed device. | [optional] 
**min_severity** | **str** | Minimum fault severity level to receive email notifications. Email notifications are sent for all faults whose severity is equal to or greater than the chosen level. | [optional]  if omitted the server will use the default value of "critical"
**sender_email** | **str** | The email address entered here will be displayed as the from address (mail received from address) of all the SMTP mail alerts that are received. If not configured, the hostname of the server is used in the from address field. | [optional] 
**smtp_port** | **int** | Port number used by the SMTP server for outgoing SMTP communication. | [optional] 
**smtp_recipients** | **[str]** |  | [optional] 
**smtp_server** | **str** | IP address or hostname of the SMTP server. The SMTP server is used by the managed device to send email notifications. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


