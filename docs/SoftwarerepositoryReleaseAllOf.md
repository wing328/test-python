# SoftwarerepositoryReleaseAllOf

Definition of the list of properties defined in 'softwarerepository.Release', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_date** | **datetime** | The date when the file was released or distributed by its vendor. | [optional] 
**release_notes_url** | **str** | The URL for the release notes of this image. | [optional] 
**supported_models** | **[str]** |  | [optional] 
**type** | **str** | The platform release type for which the images are released. This can be a fabric switch or compute server hardware. | [optional]  if omitted the server will use the default value of "FabricSwitch"
**version** | **str** | Cisco provided release version. | [optional] 
**catalog** | [**SoftwarerepositoryCatalogRelationship**](SoftwarerepositoryCatalogRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


