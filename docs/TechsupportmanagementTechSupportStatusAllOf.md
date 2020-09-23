# TechsupportmanagementTechSupportStatusAllOf

Definition of the list of properties defined in 'techsupportmanagement.TechSupportStatus', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The name of the Techsupport bundle file. | [optional] 
**reason** | **str** | Reason for techsupport failure, if any. | [optional] 
**relay_reason** | **str** | Reason for status relay failure, if any. | [optional] [readonly] 
**relay_status** | **str** | Status of techsupport status relay. Valid values are NoRelay, Pending, Completed, and Failed. | [optional] [readonly] 
**request_ts** | **datetime** | The time at which the techsupport request was initiated. | [optional] 
**status** | **str** | Status of techsupport collection. Valid values are Pending, CollectionInProgress, CollectionFailed, CollectionComplete, UploadPending, UploadInProgress, UploadPartsComplete, UploadFailed and Completed. The final status will be either CollectionFailed or UploadFailed if there is a failure and Completed if the request completed successfully and the file was uploaded to Intersight Storage Service. All the remaining status values indicates the progress of techsupport collection. | [optional] 
**techsupport_download_url** | **str** | The Url to download the techsupport file. | [optional] 
**cluster_member** | [**AssetClusterMemberRelationship**](AssetClusterMemberRelationship.md) |  | [optional] 
**device_registration** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 
**origin_resource** | [**MoBaseMoRelationship**](MoBaseMoRelationship.md) |  | [optional] 
**tech_support_request** | [**TechsupportmanagementTechSupportBundleRelationship**](TechsupportmanagementTechSupportBundleRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


