# TamAdvisoryInfoAllOf

Definition of the list of properties defined in 'tam.AdvisoryInfo', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Current state of the advisory for the owner. Indicates if the user is interested in getting updates for the advisory. | [optional]  if omitted the server will use the default value of "active"
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**advisory** | [**TamBaseAdvisoryRelationship**](TamBaseAdvisoryRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


