# ApplianceDataExportPolicyAllOf

Definition of the list of properties defined in 'appliance.DataExportPolicy', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Status of the data collection mode. If the value is &#39;true&#39;, then data collection is enabled. | [optional] 
**name** | **str** | Name of the Data Export Policy. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**parent_config** | [**ApplianceDataExportPolicyRelationship**](ApplianceDataExportPolicyRelationship.md) |  | [optional] 
**sub_configs** | [**[ApplianceDataExportPolicyRelationship], none_type**](ApplianceDataExportPolicyRelationship.md) | An array of relationships to applianceDataExportPolicy resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


