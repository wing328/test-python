# MoVersionContextAllOf

Definition of the list of properties defined in 'mo.VersionContext', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interested_mos** | [**[MoMoRef]**](MoMoRef.md) |  | [optional] 
**ref_mo** | [**MoMoRef**](MoMoRef.md) |  | [optional] 
**timestamp** | **datetime** | The time this versioned Managed Object was created. | [optional] [readonly] 
**version** | **str** | The version of the Managed Object, e.g. an incrementing number or a hash id. | [optional] [readonly] 
**version_type** | **str** | Specifies type of version. Currently the only supported value is \&quot;Configured\&quot; that is used to keep track of snapshots of policies and profiles that are intended to be configured to target endpoints. | [optional] [readonly]  if omitted the server will use the default value of "Modified"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


