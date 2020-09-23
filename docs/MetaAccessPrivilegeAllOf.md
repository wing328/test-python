# MetaAccessPrivilegeAllOf

Definition of the list of properties defined in 'meta.AccessPrivilege', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The type of CRUD operation (create, read, update, delete) for which an access privilege is required. | [optional] [readonly]  if omitted the server will use the default value of "Update"
**privilege** | **str** | The name of the privilege which is required to invoke the specified CRUD method. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


