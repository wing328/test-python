# OnpremImagePackage

ImagePackage encapsulates a software image package. ImagePackage can be a docker image, a UI web image, an endpoint (e.g. UCSM) image, a device connector image or an ansible scripts package.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**file_path** | **str** | Optional file path of the image package. | [optional] [readonly] 
**file_sha** | **str** | Image file&#39;s fingerprint. Fingerprint is calculated using SHA256 algorithm. | [optional] [readonly] 
**file_size** | **int** | Image file size in bytes. | [optional] [readonly] 
**file_time** | **datetime** | Image file&#39;s last modified date and time. | [optional] [readonly] 
**filename** | **str** | Filename of the image package. | [optional] [readonly] 
**name** | **str** | Name of the software image package. | [optional] [readonly] 
**package_type** | **str** | Image package type (e.g. service, system etc.). | [optional] [readonly] 
**version** | **str** | Image package version string. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


