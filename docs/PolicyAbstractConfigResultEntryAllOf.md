# PolicyAbstractConfigResultEntryAllOf

Definition of the list of properties defined in 'policy.AbstractConfigResultEntry', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_time** | **str** | The completed time of the task in installer. | [optional] 
**context** | [**PolicyConfigResultContext**](PolicyConfigResultContext.md) |  | [optional] 
**message** | **str** | Localized message based on the locale setting of the user&#39;s context. | [optional] 
**owner_id** | **str** | The identifier of the object that owns the result message. The owner ID is used to correlate a given result entry to a task or entity. For example, a config result entry that describes the result of a workflow task may have the task&#39;s instance ID as the owner. | [optional] 
**state** | **str** | Values  -- Ok, Ok-with-warning, Errored. | [optional] 
**type** | **str** | Indicates if the result is reported during the logical model validation/resource allocation phase. or the configuration applying phase. Values -- validation, config. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


