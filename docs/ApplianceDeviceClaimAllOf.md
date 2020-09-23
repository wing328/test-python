# ApplianceDeviceClaimAllOf

Definition of the list of properties defined in 'appliance.DeviceClaim', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Device identifier of the endpoint device. | [optional] [readonly] 
**hostname** | **str** | Hostname or IP address of the endpoint device the user wants to claim. | [optional] 
**is_password_set** | **bool** | Indicates whether the value of the &#39;password&#39; property has been set. | [optional] [readonly] 
**message** | **str** | Message set by the device claim process. | [optional] [readonly] 
**password** | **str** | Password to be used to login to the endpoint device. | [optional] 
**platform_type** | **str** | Platform type of the endpoint device. | [optional]  if omitted the server will use the default value of ""
**request_id** | **str** | User defined claim request identifier set by the UI. The RequestId field is not a mandatory. The Intersight Appliance will assign a unique value automatically if the field is not set. | [optional] 
**security_token** | **str** | Device security token of the endpoint device. | [optional] [readonly] 
**status** | **str** | Status of the device claim process. | [optional] [readonly]  if omitted the server will use the default value of "started"
**username** | **str** | Username to log in to the endpoint device. | [optional] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


