# HclHardwareCompatibilityProfile

Profile giving server hardware details, OS details and UCS Version details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**driver_iso_url** | **str** | Url for the ISO with the drivers supported for the server. | [optional] 
**error_code** | **str** | Error code indicating the compatibility status. | [optional] [readonly]  if omitted the server will use the default value of "Success"
**id** | **str** | Identifier of the hardware compatibility profile. | [optional] 
**os_vendor** | **str** | Vendor of the Operating System running on the server. | [optional] 
**os_version** | **str** | Version of the Operating System running on the server. | [optional] 
**processor_model** | **str** | Model of the processor present in the server. | [optional] 
**products** | [**[HclProduct]**](HclProduct.md) |  | [optional] 
**server_model** | **str** | Model of the server as returned by UCSM/CIMC XML API. | [optional] 
**server_revision** | **str** | Revision of the server model. | [optional] 
**ucs_version** | **str** | Version of the UCS software. | [optional] 
**version_type** | **str** | Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release. | [optional]  if omitted the server will use the default value of "UCSM"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


