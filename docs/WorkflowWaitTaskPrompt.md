# WorkflowWaitTaskPrompt

WaitTaskPrompt is used to create a customized prompts for wait control task. Wait task can be used in workflow for variety of reason, the prompts will help workflow designer to provide a customized set of prompts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**description** | **str** | Description that give more details about what it means to pick this prompt option for the wait task. | [optional] 
**label** | **str** | User friendly label for the prompt. This label will be shown to the user as one of available options for the wait task. | [optional] 
**name** | **str** | Name for the wait prompt. | [optional] 
**task_status** | **str** | Task status for the wait task when this prompt option is selected. | [optional]  if omitted the server will use the default value of "Scheduled"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


