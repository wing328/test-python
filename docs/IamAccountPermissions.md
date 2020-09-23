# IamAccountPermissions

Users can log in through the base URL (https://intersight.com) or account-specific URLs. When the Intersight user logs in through the base URL, Intersight identifies the accounts and permissions within each account which the user has access to. In case multiple permissions are identified, the user and session objects are created in the onboarding-user account, and the session object is updated with account and permission information. Intersight GUI uses this information to show available accounts and permissions for the user to select.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**account_identifier** | **str** | MOID of the account which a user can select after authentication. | [optional] [readonly] 
**account_name** | **str** | Name of the account which a user can select after authentication. | [optional] [readonly] 
**account_status** | **str** | Status of the account. Account remains inactive until a device is claimed to the account. | [optional] [readonly] 
**permissions** | [**[IamPermissionReference]**](IamPermissionReference.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


