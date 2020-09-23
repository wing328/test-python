# HclServiceStatusAllOf

Definition of the list of properties defined in 'hcl.ServiceStatus', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exemption_file_version** | **str** | Version of the last modified exemption file. | [optional] 
**identity** | **str** | A field to uniquely identify the document with the status. | [optional] 
**last_hcl_data_modified_time** | **datetime** | The timestamp of the last modified record in the HCL tool database. Used to query and get updated records. | [optional] 
**last_imported_data_checksum** | **str** | Checksum of the data dump used as the base for delta updates. | [optional] 
**status** | **str** | Status of the service indicatating if the service is up or under maintenance due to data update. | [optional]  if omitted the server will use the default value of "Unknown"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


