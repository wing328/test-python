# FirmwareUpgradeStatusAllOf

Definition of the list of properties defined in 'firmware.UpgradeStatus', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_error** | **str** | The error message from the endpoint during the download. | [optional] 
**download_message** | **bool, date, datetime, dict, float, int, list, str, none_type** | The message from the endpoint during the download.} type: string | [optional] 
**download_percentage** | **int** | The percentage of the image downloaded in the endpoint. | [optional] 
**download_progress** | **int** | The download progress of the file represented as a percentage between 0% and 100%. If progress reporting is not possible a value of -1 is sent. | [optional] 
**download_retries** | **int** | The number of retries the plugin attempted before succeeding or failing the download. | [optional] 
**download_stage** | **str** | The image download stages. Example:downloading, flashing. | [optional] 
**ep_power_status** | **str** | The server power status after the upgrade request is submitted in the endpoint. | [optional]  if omitted the server will use the default value of "none"
**overall_error** | **str** | The reason for the operation failure. | [optional] 
**overall_percentage** | **int** | The overall percentage of the operation. | [optional] 
**overallstatus** | **str** | The overall status of the operation. | [optional]  if omitted the server will use the default value of "none"
**pending_type** | **str** | Pending reason for the upgrade waiting. | [optional]  if omitted the server will use the default value of "none"
**sha256checksum** | **str** | The sha256checksum of the downloaded file as calculated by the download plugin after successfully downloading a file. | [optional] 
**upgrade** | [**FirmwareUpgradeBaseRelationship**](FirmwareUpgradeBaseRelationship.md) |  | [optional] 
**workflow** | [**WorkflowWorkflowInfoRelationship**](WorkflowWorkflowInfoRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


