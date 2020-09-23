# CapabilitySectionAllOf

Definition of the list of properties defined in 'capability.Section', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Administrative action to initialize/load the catalog section from a particular source. | [optional] [readonly]  if omitted the server will use the default value of "None"
**catalog_name** | **str** | The catalog name reference. | [optional] 
**name** | **str** | A unique name for the section inside a catalog. | [optional] 
**source** | **str** | The configured source for this section of the catalog. | [optional] [readonly]  if omitted the server will use the default value of "Local"
**version** | **str** | Version of the section inside a catalog. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


