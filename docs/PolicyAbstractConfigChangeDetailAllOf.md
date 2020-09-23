# PolicyAbstractConfigChangeDetailAllOf

Definition of the list of properties defined in 'policy.AbstractConfigChangeDetail', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | **[str]** |  | [optional] 
**config_change_context** | [**PolicyConfigResultContext**](PolicyConfigResultContext.md) |  | [optional] 
**config_change_flag** | **str** | Config change flag to differentiate Pending-changes and Config-drift. | [optional]  if omitted the server will use the default value of "Pending-changes"
**disruptions** | **[str]** |  | [optional] 
**message** | **bool, date, datetime, dict, float, int, list, str, none_type** | Detailed description of the config change.} type: string | [optional] 
**mod_status** | **str** | Modification status of the mo in this config change. | [optional]  if omitted the server will use the default value of "None"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


