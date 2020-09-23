# SoftwarerepositoryCategoryMapperAllOf

Definition of the list of properties defined in 'softwarerepository.CategoryMapper', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category of the model series. | [optional] 
**file_type** | **str** | The type of distributable image, example huu, scu, driver, os. | [optional]  if omitted the server will use the default value of "Distributable"
**mdf_id** | **str** | Cisco software repository image category identifier. | [optional] 
**regex_pattern** | **str** | The regex that all images of this category follow. | [optional] 
**source** | **str** | The image can be downloaded from cisco.com or external cloud store. | [optional]  if omitted the server will use the default value of "Cisco"
**supported_models** | **[str]** |  | [optional] 
**sw_id** | **str** | The software type id provided by cisco.com. | [optional] 
**tag_types** | **[str]** |  | [optional] 
**version** | **str** | The version from which user can download images from amazon store, if source is external cloud store. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


