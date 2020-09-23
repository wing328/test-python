# ApplianceUpgradeAllOf

Definition of the list of properties defined in 'appliance.Upgrade', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if the software upgrade is active or not. | [optional] [readonly] 
**auto_created** | **bool** | Indicates that the request was automatically created by the system. | [optional] [readonly] 
**completed_phases** | [**[OnpremUpgradePhase]**](OnpremUpgradePhase.md) |  | [optional] 
**current_phase** | [**OnpremUpgradePhase**](OnpremUpgradePhase.md) |  | [optional] 
**description** | **str** | Description of the software upgrade. | [optional] [readonly] 
**elapsed_time** | **int** | Elapsed time in seconds during the software upgrade. | [optional] [readonly] 
**end_time** | **datetime** | End date of the software upgrade. | [optional] [readonly] 
**error_code** | **int** | Error code for Intersight Appliance&#39;s software upgrade. In case of failure - this code will help decide if software upgrade can be retried. | [optional] [readonly] 
**fingerprint** | **str** | Software upgrade manifest&#39;s fingerprint. | [optional] [readonly] 
**is_rolling_back** | **bool** | Track if software upgrade is upgrading or rolling back. | [optional] [readonly] 
**messages** | **[str]** |  | [optional] 
**rollback_needed** | **bool** | Track if rollback is needed. | [optional] 
**rollback_phases** | [**[OnpremUpgradePhase]**](OnpremUpgradePhase.md) |  | [optional] 
**rollback_status** | **str** | Status of the Intersight Appliance&#39;s software rollback status. | [optional] [readonly] 
**services** | **[str]** |  | [optional] 
**start_time** | **datetime** | Start date of the software upgrade. UI can modify startTime to re-schedule an upgrade. | [optional] 
**status** | **str** | Status of the Intersight Appliance&#39;s software upgrade. | [optional] [readonly] 
**total_phases** | **int** | TotalPhase represents the total number of the upgradePhases for one upgrade. | [optional] [readonly] 
**ui_packages** | **[str]** |  | [optional] 
**version** | **str** | Software upgrade manifest&#39;s version. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**image_bundle** | [**ApplianceImageBundleRelationship**](ApplianceImageBundleRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


