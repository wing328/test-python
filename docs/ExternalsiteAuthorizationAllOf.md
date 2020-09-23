# ExternalsiteAuthorizationAllOf

Definition of the list of properties defined in 'externalsite.Authorization', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**is_user_id_set** | **bool** | Indicates whether the value of the &#39;userId&#39; property has been set. | [optional] [readonly] 
**password** | **str** | The password of the given username to download the image from external repository like cisco.com. | [optional] 
**repository_type** | **str** | The repository type to which this authorization will be requested. Cisco is the only available repository today. | [optional]  if omitted the server will use the default value of "cisco"
**user_id** | **str** | The username that has permission to download the image from external repository like cisco.com. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


