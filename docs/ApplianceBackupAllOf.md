# ApplianceBackupAllOf

Definition of the list of properties defined in 'appliance.Backup', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed_time** | **int** | Elapsed time in seconds since the backup process has started. | [optional] [readonly] 
**end_time** | **datetime** | End date and time of the backup process. | [optional] [readonly] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**messages** | **[str]** |  | [optional] 
**password** | **str** | Password to authenticate the fileserver. | [optional] 
**start_time** | **datetime** | Start date and time of the backup process. | [optional] [readonly] 
**status** | **str** | Status of the backup managed object. | [optional] [readonly]  if omitted the server will use the default value of "Started"
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


