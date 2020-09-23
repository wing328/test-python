# ConfigExporterAllOf

Definition of the list of properties defined in 'config.Exporter', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_path** | **str** | Pre-signed URL to download the exported package, if the export operation has completed successfully. Regenerated during a GET request, if the existing pre-signed URL has expired. | [optional] [readonly] 
**items** | [**[ConfigMoRef]**](ConfigMoRef.md) |  | [optional] 
**name** | **str** | An identifier for the exporter instance. | [optional] 
**status** | **str** | Status of the export operation. | [optional] [readonly]  if omitted the server will use the default value of ""
**status_message** | **str** | Status message associated with failures or progress indication. | [optional] [readonly] 
**exported_items** | [**[ConfigExportedItemRelationship], none_type**](ConfigExportedItemRelationship.md) | An array of relationships to configExportedItem resources. | [optional] [readonly] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


