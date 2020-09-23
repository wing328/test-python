# FirmwareBaseImpactAllOf

Definition of the list of properties defined in 'firmware.BaseImpact', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computation_error** | **str** | Details for the error that occurred during the reboot validation analysis. | [optional] 
**computation_status_detail** | **str** | The computation status of the estimate operation for a component. | [optional]  if omitted the server will use the default value of "Inprogress"
**domain_name** | **str** | The endpoint type or name. | [optional] 
**end_point** | **str** | A reference to a REST resource, uniquely identified by object type and MOID. | [optional] 
**firmware_version** | **str** | The current firmware version of the component. | [optional] 
**impact_type** | **str** | The impact type of the endpoint, whether a reboot is required or not. | [optional]  if omitted the server will use the default value of "NoReboot"
**model** | **str** | The model details of the component. | [optional] 
**target_firmware_version** | **str** | The target firmware version of the component. | [optional] 
**version_impact** | **str** | The change of version impact for the endpoint. | [optional]  if omitted the server will use the default value of "None"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


