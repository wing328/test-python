# TamSecurityAdvisoryDetailsAllOf

Definition of the list of properties defined in 'tam.SecurityAdvisoryDetails', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **float** | CVSS version 3 base score for the security Advisory. | [optional] 
**cve_ids** | **[str]** |  | [optional] 
**environmental_score** | **float** | CVSS version 3 environmental score for the security Advisory. | [optional] 
**status** | **str** | Cisco assigned status of the published advisory. Depends on whether the investigation is complete or on-going. | [optional]  if omitted the server will use the default value of "interim"
**temporal_score** | **float** | CVSS version 3 temporal score for the security Advisory. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


