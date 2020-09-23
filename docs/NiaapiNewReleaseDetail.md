# NiaapiNewReleaseDetail

The detail content of of this post.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**description** | **str** | Description of this new verison release post. | [optional] 
**link** | **str** | Link of downloading the release file. | [optional] 
**release_note_link** | **str** | The link used to provide a gateway for customer to review the release note. | [optional] 
**release_note_link_title** | **str** | The link title used to provide a gateway for customer to review the release note. | [optional] 
**software_download_link** | **str** | The link used to provide a gateway for customer to download the release. | [optional] 
**software_download_link_title** | **str** | The link title used to provide a gateway for customer to download the release. | [optional] 
**title** | **str** | Title of the new verison release post. | [optional] 
**version** | **str** | Version number Associate with this Post. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


