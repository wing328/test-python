# WorkflowWebApiAllOf

Definition of the list of properties defined in 'workflow.WebApi', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_request_type** | **str** | If the target type is Endpoint, this property determines whether the request is to be handled as internal request or external request by the device connector. | [optional]  if omitted the server will use the default value of "Internal"
**headers** | **bool, date, datetime, dict, float, int, list, str, none_type** | Collection of key value pairs to set in the request header. | [optional] 
**method** | **str** | The HTTP method to be executed in the given URL (GET, POST, PUT, etc). If the value is not specified, GET will be used as default. | [optional] 
**mo_type** | **str** | The type of the intersight object for which API request is to be made. The property is valid in case of Intersight API calls and the base url is automatically prepended based on the value. | [optional] 
**protocol** | **str** | The accepted web protocol values are http and https. | [optional] 
**target_type** | **str** | If the web API is to be executed in a remote device connected to the Intersight through device connector, &#39;Endpoint&#39; is expected as the value whereas if the API is an Intersight API, &#39;Local&#39; is expected as the value. | [optional]  if omitted the server will use the default value of "Endpoint"
**url** | **str** | The URL of the resource in the target to which the API request is made. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


