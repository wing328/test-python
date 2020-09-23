# SoftwarerepositoryCachedImageAllOf

Definition of the list of properties defined in 'softwarerepository.CachedImage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be performed on the imported file. If &#39;PreCache&#39; is set, the image will be cached in endpoint. If &#39;Evict&#39; is set, the cached file will be removed. Applicable in Intersight appliance deployment. If &#39;Cancel&#39; is set, the ImportState is marked as &#39;Failed&#39;. Applicable for local machine source. | [optional]  if omitted the server will use the default value of "None"
**cache_state** | **str** | The state  of this file in the endpoint The importState is updated during the cache operation and as part of the cache monitoring process. | [optional] [readonly]  if omitted the server will use the default value of "ReadyForImport"
**cached_time** | **datetime** | The time when the image or file was cached into the FI storage. | [optional] [readonly] 
**last_access_time** | **datetime** | Used by the cache monitoring process to determine the files that are to be evicted from the cache. | [optional] [readonly] 
**md5sum** | **str** | The MD5 sum of the firmware image that will be used by the endpoint to validate the integrity of the image. | [optional] [readonly] 
**original_sha512sum** | **str** | The actual sha512sum of the cached image. | [optional] [readonly] 
**path** | **str** | The absolute path of the imported file in the endpoint. | [optional] [readonly] 
**registered_workflows** | **[str]** |  | [optional] 
**used_count** | **int** | The number of times this file has been used to copy or upgrade or install actions. Used by the cache monitoring process to determine the files to be evicted from the cache. | [optional] [readonly] 
**file** | [**SoftwarerepositoryFileRelationship**](SoftwarerepositoryFileRelationship.md) |  | [optional] 
**network_element** | [**NetworkElementRelationship**](NetworkElementRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


