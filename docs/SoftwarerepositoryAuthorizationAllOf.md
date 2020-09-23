# SoftwarerepositoryAuthorizationAllOf

Definition of the list of properties defined in 'softwarerepository.Authorization', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**is_user_id_set** | **bool** | Indicates whether the value of the &#39;userId&#39; property has been set. | [optional] [readonly] 
**password** | **str** | The password that will be used by Intersight to create OAuth2 tokens for interacting with the external repository, on the user account&#39;s behalf. | [optional] 
**repository_type** | **str** | The external repository for which this authorization has been provided. The only supported repository today is cisco.com. | [optional]  if omitted the server will use the default value of "Cisco"
**user_id** | **str** | The username that will be used by Intersight to create OAuth2 tokens for interacting with the external repository, on the user account&#39;s behalf. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


