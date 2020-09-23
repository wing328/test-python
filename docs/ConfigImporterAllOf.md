# ConfigImporterAllOf

Definition of the list of properties defined in 'config.Importer', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**import_path** | **str** | The path to the archive in Intersight storage that has all the MOs to be imported. | [optional] 
**import_source** | **str** | The source of the archive in Intersight storage that has all the MOs to be imported. | [optional]  if omitted the server will use the default value of "ImageRepo"
**name** | **str** | An identifier for the importer instance. | [optional] 
**skip_integrity_checks** | **bool** | Specifies whether integrity checks must be skipped. | [optional] 
**status** | **str** | Status of the import operation. | [optional] [readonly]  if omitted the server will use the default value of ""
**status_message** | **str** | Status message associated with failures or progress indication. | [optional] [readonly] 
**imported_items** | [**[ConfigImportedItemRelationship], none_type**](ConfigImportedItemRelationship.md) | An array of relationships to configImportedItem resources. | [optional] [readonly] 
**organization** | [**OrganizationOrganizationRelationship**](OrganizationOrganizationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


