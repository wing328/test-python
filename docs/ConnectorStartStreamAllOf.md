# ConnectorStartStreamAllOf

Definition of the list of properties defined in 'connector.StartStream', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_size** | **int** | The number of outputs from a plugin to collect into a single message. Applicable only to streams that involve polling plugins and plugins which support emitting batchable data. Default value of zero indicates no batching. | [optional] 
**force_rebuild** | **bool** | Flag to force a rebuild of an existing stream. To be used if a stream is unable to recover itself in response to dropped messages. | [optional] 
**input** | **str** | Input to the plugin to start the start the stream or collect stream messages. | [optional] 
**keep_alive_interval** | **int** | Interval at which device should emit a keepalive message for this stream. Device will also expect a keepalive response from the cloud within the interval. If zero, no keepalive is required and stream should not timeout. | [optional] 
**plugin_name** | **str** | The plugin to run the stream on. | [optional] 
**poll_interval** | **int** | The desired interval to emit messages from this stream. The stream plugin will poll plugins at this interval to create a stream event. | [optional] 
**priority** | **int** | The priority level to apply to messages emitted by this stream. | [optional] 
**protocol_version** | **int** | The version of the device connector stream protocol. Used to change behavior of the device connector stream plugin based on the version of the Intersight service. Allows for multiple versions of Intersight services to interact with the stream plugin of devices. | [optional] 
**response_topic** | **str** | The topic for the device connector to publish messages to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


