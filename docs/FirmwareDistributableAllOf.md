# FirmwareDistributableAllOf

Definition of the list of properties defined in 'firmware.Distributable', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_location** | **str** | The file location of the distributable. | [optional] 
**image_category** | **str** | The category into which the distributable falls into according to the supported platform series. For e.g.; C-Series/B-Series/Infrastructure. | [optional] 
**origin** | **str** | The source of the distributable. If it has been created by the user or system. | [optional]  if omitted the server will use the default value of "System"
**catalog** | [**SoftwarerepositoryCatalogRelationship**](SoftwarerepositoryCatalogRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


