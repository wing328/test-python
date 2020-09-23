# AaaAuditRecordAllOf

Definition of the list of properties defined in 'aaa.AuditRecord', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email of the associated user that made the change.  In case the user is later deleted, we still have some reference to the information. | [optional] 
**inst_id** | **str** | The instance id of AuditRecordLocal, which is used to identify if the comming AuditRecordLocal was already processed before. | [optional] 
**source_ip** | **str** | The source IP of the client. | [optional] 
**timestamp** | **datetime** | The creation time of AuditRecordLocal, which is the time when the affected MO was created/modified/deleted. | [optional] [readonly] 
**user_id_or_email** | **str** | The userId or the email of the associated user that made the change. In case that user is later deleted, we still have some reference to the information. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**sessions** | [**IamSessionRelationship**](IamSessionRelationship.md) |  | [optional] 
**user** | [**IamUserRelationship**](IamUserRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


