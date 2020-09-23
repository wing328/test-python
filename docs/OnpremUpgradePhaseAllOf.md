# OnpremUpgradePhaseAllOf

Definition of the list of properties defined in 'onprem.UpgradePhase', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed_time** | **int** | Elapsed time in seconds to complete the current upgrade phase. | [optional] [readonly] 
**end_time** | **datetime** | End date of the software upgrade phase. | [optional] [readonly] 
**failed** | **bool** | Indicates if the upgrade phase has failed or not. | [optional] [readonly] 
**message** | **str** | Status message set during the upgrade phase. | [optional] [readonly] 
**name** | **str** | Name of the upgrade phase. | [optional] [readonly]  if omitted the server will use the default value of "init"
**start_time** | **datetime** | Start date of the software upgrade phase. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


