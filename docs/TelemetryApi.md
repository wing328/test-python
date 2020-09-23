# openapi_client.TelemetryApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_telemetry_time_series**](TelemetryApi.md#query_telemetry_time_series) | **POST** /api/v1/telemetry/TimeSeries | Perform a Druid time series aggregation request.


# **query_telemetry_time_series**
> [TelemetryDruidIntervalResult] query_telemetry_time_series(telemetry_druid_aggregate_request)

Perform a Druid time series aggregation request.

Endpoint that exposes Druid requests for time series data. This endpoint exposes multiple requests, including Time series, Top N, GroupBy, Scan, Time Boundary, Segment meta-data and datasource meta-data.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import telemetry_api
from openapi_client.model.telemetry_druid_aggregate_request import TelemetryDruidAggregateRequest
from openapi_client.model.telemetry_druid_interval_result import TelemetryDruidIntervalResult
from pprint import pprint
# Defining the host is optional and defaults to https://intersight.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://intersight.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure HTTP message signature: http_signature
# The HTTP Signature Header mechanism that can be used by a client to
# authenticate the sender of a message and ensure that particular headers
# have not been modified in transit.
#
# You can specify the signing key-id, private key path, signing scheme,
# signing algorithm, list of signed headers and signature max validity.
# The 'key_id' parameter is an opaque string that the API server can use
# to lookup the client and validate the signature.
# The 'private_key_path' parameter should be the path to a file that
# contains a DER or base-64 encoded private key.
# The 'private_key_passphrase' parameter is optional. Set the passphrase
# if the private key is encrypted.
# The 'signed_headers' parameter is used to specify the list of
# HTTP headers included when generating the signature for the message.
# You can specify HTTP headers that you want to protect with a cryptographic
# signature. Note that proxies may add, modify or remove HTTP headers
# for legitimate reasons, so you should only add headers that you know
# will not be modified. For example, if you want to protect the HTTP request
# body, you can specify the Digest header. In that case, the client calculates
# the digest of the HTTP request body and includes the digest in the message
# signature.
# The 'signature_max_validity' parameter is optional. It is configured as a
# duration to express when the signature ceases to be valid. The client calculates
# the expiration date every time it generates the cryptographic signature
# of an HTTP request. The API server may have its own security policy
# that controls the maximum validity of the signature. The client max validity
# must be lower than the server max validity.
# The time on the client and server must be synchronized, otherwise the
# server may reject the client signature.
#
# The client must use a combination of private key, signing scheme,
# signing algorithm and hash algorithm that matches the security policy of
# the API server.
#
# See openapi_client.signing for a list of all supported parameters.
configuration = openapi_client.Configuration(
    host = "https://intersight.com",
    signing_info = openapi_client.signing.HttpSigningConfiguration(
        key_id = 'my-key-id',
        private_key_path = 'private_key.pem',
        private_key_passphrase = 'YOUR_PASSPHRASE',
        signing_scheme = openapi_client.signing.SCHEME_HS2019,
        signing_algorithm = openapi_client.signing.ALGORITHM_ECDSA_MODE_FIPS_186_3,
        hash_algorithm = openapi_client.signing.SCHEME_RSA_SHA256,
        signed_headers = [
                            openapi_client.signing.HEADER_REQUEST_TARGET,
                            openapi_client.signing.HEADER_CREATED,
                            openapi_client.signing.HEADER_EXPIRES,
                            openapi_client.signing.HEADER_HOST,
                            openapi_client.signing.HEADER_DATE,
                            openapi_client.signing.HEADER_DIGEST,
                            'Content-Type',
                            'Content-Length',
                            'User-Agent'
                         ],
        signature_max_validity = datetime.timedelta(minutes=5)
    )
)

# Configure OAuth2 access token for authorization: oAuth2
configuration = openapi_client.Configuration(
    host = "https://intersight.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = telemetry_api.TelemetryApi(api_client)
    telemetry_druid_aggregate_request = TelemetryDruidAggregateRequest() # TelemetryDruidAggregateRequest | The Druid request schema for time series queries.

    # example passing only required values which don't have defaults set
    try:
        # Perform a Druid time series aggregation request.
        api_response = api_instance.query_telemetry_time_series(telemetry_druid_aggregate_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TelemetryApi->query_telemetry_time_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **telemetry_druid_aggregate_request** | [**TelemetryDruidAggregateRequest**](TelemetryDruidAggregateRequest.md)| The Druid request schema for time series queries. |

### Return type

[**[TelemetryDruidIntervalResult]**](TelemetryDruidIntervalResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the Druid request has been fullfilled. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
