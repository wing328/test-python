# AdapterDceInterfaceSettingsAllOf

Definition of the list of properties defined in 'adapter.DceInterfaceSettings', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fec_mode** | **str** | Forward Error Correction (FEC) mode setting for the DCE interfaces of the adapter. FEC mode setting is supported only for Cisco VIC 14xx adapters. FEC mode &#39;cl74&#39; is unsupported for Cisco VIC 1495/1497. This setting will be ignored for unsupported adapters and for unavailable DCE interfaces. | [optional]  if omitted the server will use the default value of "Auto"
**interface_id** | **int** | DCE interface id on which settings needs to be configured. Supported values are (0-3). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


