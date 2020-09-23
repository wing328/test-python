# WorkflowPrimitiveDataPropertyAllOf

Definition of the list of properties defined in 'workflow.PrimitiveDataProperty', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | [**WorkflowConstraints**](WorkflowConstraints.md) |  | [optional] 
**inventory_selector** | [**[WorkflowMoReferenceProperty]**](WorkflowMoReferenceProperty.md) |  | [optional] 
**secure** | **bool** | Intersight supports secure properties as task input/output. The values of these properties are encrypted and stored in Intersight. This flag marks the property to be secure when it is set to true. | [optional] 
**type** | **str** | Specify the enum type for primitive data type. | [optional]  if omitted the server will use the default value of "string"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


