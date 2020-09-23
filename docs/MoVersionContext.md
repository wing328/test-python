# MoVersionContext

VersionContext contains the versioning info for an object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**interested_mos** | [**[MoMoRef]**](MoMoRef.md) |  | [optional] 
**ref_mo** | [**MoMoRef**](MoMoRef.md) |  | [optional] 
**timestamp** | **datetime** | The time this versioned Managed Object was created. | [optional] [readonly] 
**version** | **str** | The version of the Managed Object, e.g. an incrementing number or a hash id. | [optional] [readonly] 
**version_type** | **str** | Specifies type of version. Currently the only supported value is \&quot;Configured\&quot; that is used to keep track of snapshots of policies and profiles that are intended to be configured to target endpoints. | [optional] [readonly]  if omitted the server will use the default value of "Modified"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


