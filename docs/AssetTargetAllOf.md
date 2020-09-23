# AssetTargetAllOf

Definition of the list of properties defined in 'asset.Target', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**[AssetConnection]**](AssetConnection.md) |  | [optional] 
**services** | [**[AssetService]**](AssetService.md) |  | [optional] 
**status** | **str** | Status indicates if Intersight can establish a connection and authenticate with the managed target. Status does not include information about the functional health of the target. | [optional] [readonly]  if omitted the server will use the default value of ""
**status_error_reason** | **str** | StatusErrorReason provides additional context for the Status. | [optional] [readonly] 
**target_type** | **str** | The type of the managed target. For example a UCS Server or Vmware Vcenter target. | [optional]  if omitted the server will use the default value of ""
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 
**assist** | [**AssetDeviceRegistrationRelationship**](AssetDeviceRegistrationRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


