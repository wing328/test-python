# SdwanVmanageAccountPolicyAllOf

Definition of the list of properties defined in 'sdwan.VmanageAccountPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_address** | **str** | VManage server hostname (FQDN) that the acccount holds information for. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**password** | **str** | Local password for authenticating with the vManage server. | [optional] 
**port** | **int** | VManage Port number on which the application is running. | [optional] 
**username** | **str** | Local username for authenticating with the vManage server. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 
**profiles** | [**[SdwanProfileRelationship], none_type**](SdwanProfileRelationship.md) | An array of relationships to sdwanProfile resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


