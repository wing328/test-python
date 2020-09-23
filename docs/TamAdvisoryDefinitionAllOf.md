# TamAdvisoryDefinitionAllOf

Definition of the list of properties defined in 'tam.AdvisoryDefinition', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**[TamAction]**](TamAction.md) |  | [optional] 
**advisory_details** | [**TamBaseAdvisoryDetails**](TamBaseAdvisoryDetails.md) |  | [optional] 
**advisory_id** | **str** | Cisco generated identifier for the published security advisory. | [optional] 
**api_data_sources** | [**[TamApiDataSource]**](TamApiDataSource.md) |  | [optional] 
**date_published** | **datetime** | Date when the security advisory was first published by Cisco. | [optional] 
**date_updated** | **datetime** | Date when the security advisory was last updated by Cisco. | [optional] 
**external_url** | **str** | A link to an external URL describing security Advisory in more details. | [optional] 
**recommendation** | **str** | Recommended action to resolve the security advisory. | [optional] 
**type** | **str** | The type (field notice, security advisory etc.) of Intersight advisory. | [optional]  if omitted the server will use the default value of "securityAdvisory"
**version** | **str** | Cisco assigned advisory version after latest revision. | [optional] 
**workaround** | **str** | Workarounds available for the advisory. | [optional] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


