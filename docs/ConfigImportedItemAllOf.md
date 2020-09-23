# ConfigImportedItemAllOf

Definition of the list of properties defined in 'config.ImportedItem', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_shared** | **bool** | Specifies whether this item MO was in shared scope or user scope when exported. | [optional] [readonly] 
**is_updated** | **bool** | Specifies whether this item MO was updated or created while importing in desired service. | [optional] [readonly] 
**item** | [**ConfigMoRef**](ConfigMoRef.md) |  | [optional] 
**name** | **str** | MO item identity (the moref corresponding to item) expressed as a string. | [optional] [readonly] 
**new_moid** | **str** | Moid of the MO created/updated during import for the item. | [optional] [readonly] 
**service_version** | **str** | Version of the service that owned the item MO when the item was exported. | [optional] [readonly] 
**status** | **str** | Status of the item&#39;s import operation. | [optional] [readonly]  if omitted the server will use the default value of ""
**status_message** | **str** | Progress or error message for the MO&#39;s import operation. | [optional] [readonly] 
**importer** | [**ConfigImporterRelationship**](ConfigImporterRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


