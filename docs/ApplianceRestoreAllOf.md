# ApplianceRestoreAllOf

Definition of the list of properties defined in 'appliance.Restore', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed_time** | **int** | Elapsed time in seconds since the restore process has started. | [optional] [readonly] 
**end_time** | **datetime** | End date and time of the restore process. | [optional] [readonly] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**messages** | **[str]** |  | [optional] 
**password** | **str** | Password for authenticating with the file server. | [optional] 
**start_time** | **datetime** | Start date and time of the restore process. | [optional] [readonly] 
**status** | **str** | Status of the restore managed object. | [optional] [readonly]  if omitted the server will use the default value of "Started"
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


