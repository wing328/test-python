# ConnectorHttpRequest

A HTTP request sent by a cloud service to be proxied through a device connector.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**body** | **str** | Contents of the request body to send for PUT/PATCH/POST requests. | [optional] 
**dial_timeout** | **int** | The timeout for establishing the TCP connection to the target host. If not set the request timeout value is used. | [optional] 
**header** | **bool, date, datetime, dict, float, int, list, str, none_type** | Collection of key value pairs to set in the request header. | [optional] 
**internal** | **bool** | The request is for an internal platform API that requires authentication to be inserted by the platform implementation. | [optional] 
**method** | **str** | Method specifies the HTTP method (GET, POST, PUT, etc.). For client requests an empty string means GET. | [optional] 
**timeout** | **int** | The timeout for the HTTP request to complete, from connection establishment to response body read complete. If not set a default timeout of five minutes is used. | [optional] 
**url** | [**ConnectorUrl**](ConnectorUrl.md) |  | [optional] 
**encrypted_aes_key** | **str** | The secure properties that have large text content as value can be encrypted using AES key. In these cases, the AES key needs to be encrypted using the device connector public key and passed as the value for this property. The secure properties that are encrypted using the AES key are mapped against the property name with prefix &#39;AES&#39; in SecureProperties dictionary. | [optional] 
**encryption_key** | **str** | The public key that was used to encrypt the values present in SecureProperties dictionary. If the given public key is not same as device connector&#39;s public key, an error reponse with appropriate error message is thrown back. | [optional] 
**secure_properties** | **bool, date, datetime, dict, float, int, list, str, none_type** | A dictionary of encrypted secure values mapped against the secure property name. The values that are encrypted using AES key must be mapped against the secure property name with a &#39;AES&#39; prefix Device connector expects the message body to be a golang template and the template can use the secure property names as placeholders. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


