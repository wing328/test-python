# WorkflowDecisionTask

A DecisionTask is a control task that executes a sequence of WorkflowTasks based off decision provided and evaluated by this task.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**condition** | **str** | The condition to evaluate for this decision task. The condition can be a workflow or task variable or an expression based on the input parameters. Example value for condition if its Workflow/task variable is -  \&quot;${task1.output.var1} or ${workflow.input.var2}\&quot; which evaluates to a value matching any of the decision case values. Example value for condition if its an expression is - \&quot;if ( $.element ! &#x3D; null &amp;&amp; $.element &gt; 0 ) &#39;true&#39;; else &#39;false&#39;; \&quot; which evaluates to &#39;true&#39; or &#39;false&#39; and will match one of the decision case values. Here \&quot;element\&quot; is a variable in decisiontask&#39;s inputParameters JSON formatted map. You can also use javascript like functions indexOf, toUpperCase in the expression which will be evaluated by the expression evaluator. | [optional] 
**decision_cases** | [**[WorkflowDecisionCase]**](WorkflowDecisionCase.md) |  | [optional] 
**default_task** | **str** | The default next Task to execute if the decision cannot be evaluated to any of the DecisionCases. | [optional] 
**input_parameters** | **bool, date, datetime, dict, float, int, list, str, none_type** | JSON formatted map that defines the input given to the decision task. The inputs are used as variables in the condition property of decision task. The input variables can be static values like \&quot;hello\&quot; , \&quot;24\&quot;, \&quot;true\&quot; OR previous task outputs/workflow inputs like \&quot;${task2.output.var1}}\&quot;. The input variables are referrenced as $.inputVariableName in the condition property. | [optional] 
**description** | **str** | The description of this task instance in the workflow. | [optional] 
**label** | **str** | A user defined label identifier of the workflow task used for UI display. | [optional] 
**name** | **str** | The name of the task within the workflow and it must be unique among all WorkflowTasks within a workflow definition. This name serves as the internal unique identifier for the task and is used to pick input and output parameters to feed into other tasks. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


