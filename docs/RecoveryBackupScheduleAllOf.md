# RecoveryBackupScheduleAllOf

Definition of the list of properties defined in 'recovery.BackupSchedule', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_time** | **datetime** | The time at which the backup is to be run on a given day. This is used when the frequency unit is daily. | [optional] 
**frequency_unit** | **str** | The frequency at which the backup schedule must run. | [optional]  if omitted the server will use the default value of "Daily"
**hours** | **int** | The frequency, in hours, at which the backup schedule runs. | [optional]  if omitted the server will use the default value of 8

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


