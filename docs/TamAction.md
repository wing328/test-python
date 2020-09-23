# TamAction

An action is used to react when an object satifies the condition specified in alert query. For e.g. an action in case of an object matching a fieldNotice query would be to create an alert instance of type 'fieldNotice' for the affected object.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**affected_object_type** | **str** | Type of the managed object that should be marked with an instance of the Alert (when operation type is create) or that should have an alert instance removed (when operation type is remove). | [optional] 
**alert_type** | **str** | Alert type is used to denote the category of an Intersight alert (FieldNotice, equipment Fault etc.). | [optional]  if omitted the server will use the default value of "psirt"
**identifiers** | [**[TamIdentifiers]**](TamIdentifiers.md) |  | [optional] 
**name** | **str** | Uniquely identifies a given action among the set of actions corresponding to an advisory. Primarily used to store and compare results of subsequent iterations corresponding to the action queries. | [optional] 
**operation_type** | **str** | Operation type for the alert action. An action is used to carry out the process of \&quot;reacting\&quot; to an alert condition. For e.g.in case of a fieldNotice alert, the intention may be to create a new alert (if the condition matches and there is no existing alert) or to remove an existing alert when the alert condition has been remedied. | [optional]  if omitted the server will use the default value of "create"
**queries** | [**[TamQueryEntry]**](TamQueryEntry.md) |  | [optional] 
**type** | **str** | Type of Intersight alert. An alert in Intersight could be one of several kinds (FieldNotice, PSIRT etc.). Primarily used for filtering alerts based on the type. | [optional]  if omitted the server will use the default value of "restApi"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


