# UcsdUcsdRestoreParameters

Restore Configuration Parameters for UCS Director restore workflow.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**location** | **str** | The complete location of the path on the server. The location should be specified in the following format- hostname-or-ipv4address&lt;:port&gt;/absolute-file-path. | [optional] 
**password** | **str** | The password of the target backup server. Only required if the target server is accessed using SFTP or SCP protocol. | [optional] 
**protocol** | **str** | The protocol used to backup the UCS Director. | [optional] 
**restore_configuration_files** | **bool** | Decides whether UCS Director property files should also be restored. | [optional] 
**restore_license** | **bool** | Decides whether license should also be restored. | [optional] 
**username** | **str** | The username of the target backup server. Only required if the target server is accessed using SFTP or SCP protocol. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


