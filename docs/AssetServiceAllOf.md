# AssetServiceAllOf

Definition of the list of properties defined in 'asset.Service', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**AssetServiceOptions**](AssetServiceOptions.md) |  | [optional] 
**status** | **str** | Status indicates if the respective Service can establish a connection and authenticate with the managed target. Status does not include information about the functional health of the target. | [optional]  if omitted the server will use the default value of ""
**status_error_reason** | **str** | When &#39;Status&#39; is not Connected, statusErrorReason provides further details about why the device is not connected with Intersight. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


