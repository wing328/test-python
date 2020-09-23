# InventoryEpInfoAllOf

Definition of the list of properties defined in 'inventory.EpInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | Connections status of UEM endpoint. | [optional] [readonly]  if omitted the server will use the default value of "Unknown"
**ep_type** | **str** | Type of UEM endpoint (BMC, CMC or VIC). | [optional] [readonly] 
**ip** | **str** | The IP address of the UEM endpoint. | [optional] [readonly] 
**mac_address** | **str** | The MAC address of the UEM endpoint. | [optional] [readonly] 
**member_identity** | **str** | The member identity of the UEM connection being inventoried. | [optional] [readonly] 
**model** | **str** | The model of the UEM endpoint. | [optional] [readonly] 
**serial** | **str** | The serial number of the UEM endpoint. | [optional] [readonly] 
**server_registration_id** | **str** | The device id of the server which this EP is a part of. | [optional] [readonly] 
**vendor** | **str** | The vendor of the UEM endpoint. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


