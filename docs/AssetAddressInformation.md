# AssetAddressInformation

Type for saving the address information. It is used in asset.DeviceContractInformation object to save customer address.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**address1** | **str** | Address Line one of the address information. example \&quot;PO BOX 641570\&quot;. | [optional] [readonly] 
**address2** | **str** | Address Line two of the address information. example \&quot;Cisco Systems\&quot;. | [optional] [readonly] 
**city** | **str** | City in which the address resides. example \&quot;San Jose\&quot;. | [optional] [readonly] 
**country** | **str** | Country in which the address resides. example \&quot;US\&quot;. | [optional] [readonly] 
**location** | **str** | Location in which the address resides. example \&quot;14852\&quot;. | [optional] [readonly] 
**name** | **str** | Name of the user whose address is being populated. | [optional] [readonly] 
**postal_code** | **str** | Postal Code in which the address resides. example \&quot;95164-1570\&quot;. | [optional] [readonly] 
**state** | **str** | State in which the address resides. example \&quot;CA\&quot;. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


