# ConnectorStartStreamFromDeviceAllOf

Definition of the list of properties defined in 'connector.StartStreamFromDevice', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** | The asset.ClusterMember member identity that is opening this stream. | [optional] 
**stream_config** | **bool, date, datetime, dict, float, int, list, str, none_type** | Any extra configuration needed to open/identify a stream. | [optional] 
**stream_type** | **str** | Identifies the type of stream to open to the device. The Intersight service will validate that the device should open a stream of this type and if so build a stream configuration and send it down to the device. The streamType should identify a unique stream to open to a device, that is if the device sends a stream open message and a stream of that type is already open in the cloud the existing stream should be re-used. | [optional] 
**topic** | **str** | The topic the device should send the stream open message to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


