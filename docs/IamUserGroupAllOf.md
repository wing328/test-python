# IamUserGroupAllOf

Definition of the list of properties defined in 'iam.UserGroup', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the user group which the dynamic user belongs to. | [optional] 
**idp** | [**IamIdpRelationship**](IamIdpRelationship.md) |  | [optional] 
**idpreference** | [**IamIdpReferenceRelationship**](IamIdpReferenceRelationship.md) |  | [optional] 
**permissions** | [**[IamPermissionRelationship], none_type**](IamPermissionRelationship.md) | An array of relationships to iamPermission resources. | [optional] 
**qualifier** | [**IamQualifierRelationship**](IamQualifierRelationship.md) |  | [optional] 
**users** | [**[IamUserRelationship], none_type**](IamUserRelationship.md) | An array of relationships to iamUser resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


