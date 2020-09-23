# FeedbackFeedbackData

Feedback data that collected on the UI from user.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**account_name** | **str** | Account name of the feedback sender. Copied in order to be persisted in case of account removal. | [optional] 
**alternative_follow_up_emails** | **[str]** |  | [optional] 
**comment** | **str** | Text of the feedback as provided by the user, if it is a bug or a comment. | [optional] 
**email** | **str** | User&#39;s email address details. | [optional] 
**evaluation** | **str** | Evalation rating as provided by the user to capture user sentiment regarding the issue. | [optional]  if omitted the server will use the default value of "Excellent"
**follow_up** | **bool** | If a user is open for follow-up or not. | [optional] 
**trace_ids** | **bool, date, datetime, dict, float, int, list, str, none_type** | Bunch of last traceId for reproducing user last activity. | [optional] 
**type** | **str** | Type of the feedback from user. | [optional]  if omitted the server will use the default value of "Evaluation"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


