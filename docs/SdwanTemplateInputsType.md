# SdwanTemplateInputsType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**editable** | **bool** | Defines if the input is editable. | [optional] 
**key** | **str** | Name of the dynamic input key specified in the vManage template. | [optional] 
**required** | **bool** | Defines if the input is optional or required. | [optional] 
**template** | **str** | Refers to the name of the vManage template that this inputs belongs to. | [optional] [readonly] 
**title** | **str** | Label for the property being saved in the current instance of template Input. | [optional] 
**type** | **str** | Defines the object type for the input. | [optional] 
**value** | **str** | Value of the dynamic input key specfied in the vManage template. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


