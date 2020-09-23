# FirmwareFirmwareInventory

Firmware inventory for server component.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**category** | **str** | Component category. For example, MRAID is under storage controller, CIMC is under management controller. | [optional] 
**label** | **str** | The name of the component to reflect on UI. | [optional] 
**model** | **str** | Model deatils of component. | [optional] 
**update_uri** | **str** | The redfish URI to get the firmware inventory of server components. | [optional] 
**vendor** | **str** | The vendor of the component. | [optional] 
**version** | **str** | The firmware running version on the component. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


