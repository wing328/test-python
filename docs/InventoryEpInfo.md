# InventoryEpInfo

The runtime information about a UEM (Unified Event Mechanism) supported endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**connection_status** | **str** | Connections status of UEM endpoint. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**ep_type** | **str** | Type of UEM endpoint (BMC, CMC or VIC). | [optional] [readonly] 
**ip** | **str** | The IP address of the UEM endpoint. | [optional] [readonly] 
**mac_address** | **str** | The MAC address of the UEM endpoint. | [optional] [readonly] 
**member_identity** | **str** | The member identity of the UEM connection being inventoried. | [optional] [readonly] 
**model** | **str** | The model of the UEM endpoint. | [optional] [readonly] 
**serial** | **str** | The serial number of the UEM endpoint. | [optional] [readonly] 
**server_registration_id** | **str** | The device id of the server which this EP is a part of. | [optional] [readonly] 
**vendor** | **str** | The vendor of the UEM endpoint. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


