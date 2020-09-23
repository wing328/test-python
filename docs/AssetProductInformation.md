# AssetProductInformation

Type for saving the product information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**bill_to** | [**AssetAddressInformation**](AssetAddressInformation.md) |  | [optional] 
**description** | **str** | Short description of the Cisco product that helps identify the product easily. example \&quot;DISTI:UCS 6248UP 1RU Fabric Int/No PSU/32 UP/ 12p LIC\&quot;. | [optional] [readonly] 
**family** | **str** | Family that the product belongs to. Example \&quot;UCSB\&quot;. | [optional] [readonly] 
**group** | **str** | Group that the product belongs to. It is one higher level categorization above family. example \&quot;Switch\&quot;. | [optional] [readonly] 
**number** | **str** | Product number that identifies the product. example PID. example \&quot;UCS-FI-6248UP-CH2\&quot;. | [optional] [readonly] 
**ship_to** | [**AssetAddressInformation**](AssetAddressInformation.md) |  | [optional] 
**sub_type** | **str** | Sub type of the product being specified. example \&quot;UCS 6200 SER\&quot;. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


