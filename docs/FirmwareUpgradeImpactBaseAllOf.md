# FirmwareUpgradeImpactBaseAllOf

Definition of the list of properties defined in 'firmware.UpgradeImpactBase', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**components** | **[str]** |  | [optional] 
**computation_state** | **str** | Captures the status of an upgrade impact calculation. Indicates whether the calculation is complete, in progress or the calculation is impossible due to the absence of the target image on the endpoint. | [optional]  if omitted the server will use the default value of "Inprogress"
**exclude_components** | **[str]** |  | [optional] 
**impacts** | [**[FirmwareBaseImpact]**](FirmwareBaseImpact.md) |  | [optional] 
**summary** | **str** | The summary on the component or components getting impacted by the upgrade. | [optional]  if omitted the server will use the default value of "Basic"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


