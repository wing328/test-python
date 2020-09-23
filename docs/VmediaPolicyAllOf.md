# VmediaPolicyAllOf

Definition of the list of properties defined in 'vmedia.Policy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | State of the Virtual Media service on the endpoint. | [optional] 
**encryption** | **bool** | If enabled, allows encryption of all Virtual Media communications. | [optional] 
**low_power_usb** | **bool** | If enabled, the virtual drives appear on the boot selection menu after mapping the image and rebooting the host. | [optional] 
**mappings** | [**[VmediaMapping]**](VmediaMapping.md) |  | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[PolicyAbstractConfigProfileRelationship], none_type**](PolicyAbstractConfigProfileRelationship.md) | An array of relationships to policyAbstractConfigProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


