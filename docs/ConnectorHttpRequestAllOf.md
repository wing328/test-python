# ConnectorHttpRequestAllOf

Definition of the list of properties defined in 'connector.HttpRequest', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Contents of the request body to send for PUT/PATCH/POST requests. | [optional] 
**dial_timeout** | **int** | The timeout for establishing the TCP connection to the target host. If not set the request timeout value is used. | [optional] 
**header** | **bool, date, datetime, dict, float, int, list, str, none_type** | Collection of key value pairs to set in the request header. | [optional] 
**internal** | **bool** | The request is for an internal platform API that requires authentication to be inserted by the platform implementation. | [optional] 
**method** | **str** | Method specifies the HTTP method (GET, POST, PUT, etc.). For client requests an empty string means GET. | [optional] 
**timeout** | **int** | The timeout for the HTTP request to complete, from connection establishment to response body read complete. If not set a default timeout of five minutes is used. | [optional] 
**url** | [**ConnectorUrl**](ConnectorUrl.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


