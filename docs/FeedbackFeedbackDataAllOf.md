# FeedbackFeedbackDataAllOf

Definition of the list of properties defined in 'feedback.FeedbackData', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Account name of the feedback sender. Copied in order to be persisted in case of account removal. | [optional] 
**alternative_follow_up_emails** | **[str]** |  | [optional] 
**comment** | **str** | Text of the feedback as provided by the user, if it is a bug or a comment. | [optional] 
**email** | **str** | User&#39;s email address details. | [optional] 
**evaluation** | **str** | Evalation rating as provided by the user to capture user sentiment regarding the issue. | [optional]  if omitted the server will use the default value of "Excellent"
**follow_up** | **bool** | If a user is open for follow-up or not. | [optional] 
**trace_ids** | **bool, date, datetime, dict, float, int, list, str, none_type** | Bunch of last traceId for reproducing user last activity. | [optional] 
**type** | **str** | Type of the feedback from user. | [optional]  if omitted the server will use the default value of "Evaluation"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


