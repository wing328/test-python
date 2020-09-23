# FirmwareUpgradeBaseAllOf

Definition of the list of properties defined in 'firmware.UpgradeBase', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_download** | [**FirmwareDirectDownload**](FirmwareDirectDownload.md) |  | [optional] 
**file_server** | [**SoftwarerepositoryFileServer**](SoftwarerepositoryFileServer.md) |  | [optional] 
**network_share** | [**FirmwareNetworkShare**](FirmwareNetworkShare.md) |  | [optional] 
**skip_estimate_impact** | **bool** | User has the option to skip the estimate impact calculation. | [optional] 
**status** | **str** | Status of the upgrade operation. | [optional]  if omitted the server will use the default value of "NONE"
**upgrade_type** | **str** | Desired upgrade mode to choose either direct download based upgrade or network share upgrade. | [optional]  if omitted the server will use the default value of "direct_upgrade"
**distributable** | [**FirmwareDistributableRelationship**](FirmwareDistributableRelationship.md) |  | [optional] 
**release** | [**SoftwarerepositoryReleaseRelationship**](SoftwarerepositoryReleaseRelationship.md) |  | [optional] 
**upgrade_impact** | [**FirmwareUpgradeImpactStatusRelationship**](FirmwareUpgradeImpactStatusRelationship.md) |  | [optional] 
**upgrade_status** | [**FirmwareUpgradeStatusRelationship**](FirmwareUpgradeStatusRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


