# ContentGrammar

Content handler framework supports extraction of required values from API/device responses. These responses may be of various content types such as XML, JSON, etc. The values of importance are modeled as parameters in the content handler framework. The parameters can be of a scalar value type or a collection of values. A group of related parameters can be modeled as a single complex type parameter. These complex types will be very useful to extract a set of repeating group of related parameters. A grammar specification defines the set of parameters that need to be extracted from the content. The grammar specification allows complex type definitions to be defined for any complex parameters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**error_parameters** | [**[ContentBaseParameter]**](ContentBaseParameter.md) |  | [optional] 
**parameters** | [**[ContentBaseParameter]**](ContentBaseParameter.md) |  | [optional] 
**types** | [**[ContentComplexType]**](ContentComplexType.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


