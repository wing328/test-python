# SoftwareSolutionDistributableAllOf

Definition of the list of properties defined in 'software.SolutionDistributable', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** | The path of the file in S3/minio bucket. | [optional] [readonly] 
**solution_name** | **str** | The name of the solution in which the image belongs. | [optional] 
**sub_type** | **str** | The type of the file like OS image, Script etc. | [optional]  if omitted the server will use the default value of "osimage"
**catalog** | [**SoftwarerepositoryCatalogRelationship**](SoftwarerepositoryCatalogRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


