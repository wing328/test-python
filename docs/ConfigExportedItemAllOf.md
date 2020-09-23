# ConfigExportedItemAllOf

Definition of the list of properties defined in 'config.ExportedItem', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Name of the file corresponding to item MO. | [optional] [readonly] 
**item** | [**ConfigMoRef**](ConfigMoRef.md) |  | [optional] 
**name** | **str** | MO item identity (the moref corresponding to item) expressed as a string. | [optional] [readonly] 
**service_version** | **str** | Version of the service that owns the item MO. | [optional] [readonly] 
**status** | **str** | Status of the item&#39;s export operation. | [optional] [readonly]  if omitted the server will use the default value of ""
**status_message** | **str** | Progress or error message for the MO&#39;s export operation. | [optional] [readonly] 
**exporter** | [**ConfigExporterRelationship**](ConfigExporterRelationship.md) |  | [optional] 
**parent_item** | [**ConfigExportedItemRelationship**](ConfigExportedItemRelationship.md) |  | [optional] 
**related_items** | [**[ConfigExportedItemRelationship], none_type**](ConfigExportedItemRelationship.md) | An array of relationships to configExportedItem resources. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


