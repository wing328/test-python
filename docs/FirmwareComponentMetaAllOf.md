# FirmwareComponentMetaAllOf

Definition of the list of properties defined in 'firmware.ComponentMeta', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_label** | **str** | The name of the component in the compressed HSU bundle. | [optional] 
**component_type** | **str** | The type of component image within the distributable. | [optional]  if omitted the server will use the default value of "ALL"
**description** | **str** | This shows the description of component image within the distributable. | [optional] 
**disruption** | **str** | The type of disruption on each component. For example, host reboot, automatic power cycle, and manual power cycle. | [optional]  if omitted the server will use the default value of "None"
**is_oob_supported** | **bool** | If set, the component can be updated through out-of-band management, else, is updated through the booting host service utility. | [optional] 
**model** | **str** | The model of the component image in the distributable. | [optional] 
**oob_manageability** | **[str]** |  | [optional] 
**packed_version** | **str** | The packaged version of component image within the distributable. | [optional] 
**redfish_url** | **str** | The redfish target for each component. | [optional] 
**vendor** | **str** | The version of the component image in the distributable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


