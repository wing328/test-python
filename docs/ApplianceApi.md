# openapi_client.ApplianceApi

All URIs are relative to *https://intersight.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appliance_backup**](ApplianceApi.md#create_appliance_backup) | **POST** /api/v1/appliance/Backups | Create a &#39;appliance.Backup&#39; resource.
[**create_appliance_backup_policy**](ApplianceApi.md#create_appliance_backup_policy) | **POST** /api/v1/appliance/BackupPolicies | Create a &#39;appliance.BackupPolicy&#39; resource.
[**create_appliance_data_export_policy**](ApplianceApi.md#create_appliance_data_export_policy) | **POST** /api/v1/appliance/DataExportPolicies | Create a &#39;appliance.DataExportPolicy&#39; resource.
[**create_appliance_device_claim**](ApplianceApi.md#create_appliance_device_claim) | **POST** /api/v1/appliance/DeviceClaims | Create a &#39;appliance.DeviceClaim&#39; resource.
[**create_appliance_diag_setting**](ApplianceApi.md#create_appliance_diag_setting) | **POST** /api/v1/appliance/DiagSettings | Create a &#39;appliance.DiagSetting&#39; resource.
[**create_appliance_restore**](ApplianceApi.md#create_appliance_restore) | **POST** /api/v1/appliance/Restores | Create a &#39;appliance.Restore&#39; resource.
[**delete_appliance_backup**](ApplianceApi.md#delete_appliance_backup) | **DELETE** /api/v1/appliance/Backups/{Moid} | Delete a &#39;appliance.Backup&#39; resource.
[**delete_appliance_restore**](ApplianceApi.md#delete_appliance_restore) | **DELETE** /api/v1/appliance/Restores/{Moid} | Delete a &#39;appliance.Restore&#39; resource.
[**get_appliance_backup_by_moid**](ApplianceApi.md#get_appliance_backup_by_moid) | **GET** /api/v1/appliance/Backups/{Moid} | Read a &#39;appliance.Backup&#39; resource.
[**get_appliance_backup_list**](ApplianceApi.md#get_appliance_backup_list) | **GET** /api/v1/appliance/Backups | Read a &#39;appliance.Backup&#39; resource.
[**get_appliance_backup_policy_by_moid**](ApplianceApi.md#get_appliance_backup_policy_by_moid) | **GET** /api/v1/appliance/BackupPolicies/{Moid} | Read a &#39;appliance.BackupPolicy&#39; resource.
[**get_appliance_backup_policy_list**](ApplianceApi.md#get_appliance_backup_policy_list) | **GET** /api/v1/appliance/BackupPolicies | Read a &#39;appliance.BackupPolicy&#39; resource.
[**get_appliance_certificate_setting_by_moid**](ApplianceApi.md#get_appliance_certificate_setting_by_moid) | **GET** /api/v1/appliance/CertificateSettings/{Moid} | Read a &#39;appliance.CertificateSetting&#39; resource.
[**get_appliance_certificate_setting_list**](ApplianceApi.md#get_appliance_certificate_setting_list) | **GET** /api/v1/appliance/CertificateSettings | Read a &#39;appliance.CertificateSetting&#39; resource.
[**get_appliance_data_export_policy_by_moid**](ApplianceApi.md#get_appliance_data_export_policy_by_moid) | **GET** /api/v1/appliance/DataExportPolicies/{Moid} | Read a &#39;appliance.DataExportPolicy&#39; resource.
[**get_appliance_data_export_policy_list**](ApplianceApi.md#get_appliance_data_export_policy_list) | **GET** /api/v1/appliance/DataExportPolicies | Read a &#39;appliance.DataExportPolicy&#39; resource.
[**get_appliance_device_claim_by_moid**](ApplianceApi.md#get_appliance_device_claim_by_moid) | **GET** /api/v1/appliance/DeviceClaims/{Moid} | Read a &#39;appliance.DeviceClaim&#39; resource.
[**get_appliance_device_claim_list**](ApplianceApi.md#get_appliance_device_claim_list) | **GET** /api/v1/appliance/DeviceClaims | Read a &#39;appliance.DeviceClaim&#39; resource.
[**get_appliance_diag_setting_by_moid**](ApplianceApi.md#get_appliance_diag_setting_by_moid) | **GET** /api/v1/appliance/DiagSettings/{Moid} | Read a &#39;appliance.DiagSetting&#39; resource.
[**get_appliance_diag_setting_list**](ApplianceApi.md#get_appliance_diag_setting_list) | **GET** /api/v1/appliance/DiagSettings | Read a &#39;appliance.DiagSetting&#39; resource.
[**get_appliance_image_bundle_by_moid**](ApplianceApi.md#get_appliance_image_bundle_by_moid) | **GET** /api/v1/appliance/ImageBundles/{Moid} | Read a &#39;appliance.ImageBundle&#39; resource.
[**get_appliance_image_bundle_list**](ApplianceApi.md#get_appliance_image_bundle_list) | **GET** /api/v1/appliance/ImageBundles | Read a &#39;appliance.ImageBundle&#39; resource.
[**get_appliance_node_info_by_moid**](ApplianceApi.md#get_appliance_node_info_by_moid) | **GET** /api/v1/appliance/NodeInfos/{Moid} | Read a &#39;appliance.NodeInfo&#39; resource.
[**get_appliance_node_info_list**](ApplianceApi.md#get_appliance_node_info_list) | **GET** /api/v1/appliance/NodeInfos | Read a &#39;appliance.NodeInfo&#39; resource.
[**get_appliance_release_note_by_moid**](ApplianceApi.md#get_appliance_release_note_by_moid) | **GET** /api/v1/appliance/ReleaseNotes/{Moid} | Read a &#39;appliance.ReleaseNote&#39; resource.
[**get_appliance_release_note_list**](ApplianceApi.md#get_appliance_release_note_list) | **GET** /api/v1/appliance/ReleaseNotes | Read a &#39;appliance.ReleaseNote&#39; resource.
[**get_appliance_restore_by_moid**](ApplianceApi.md#get_appliance_restore_by_moid) | **GET** /api/v1/appliance/Restores/{Moid} | Read a &#39;appliance.Restore&#39; resource.
[**get_appliance_restore_list**](ApplianceApi.md#get_appliance_restore_list) | **GET** /api/v1/appliance/Restores | Read a &#39;appliance.Restore&#39; resource.
[**get_appliance_setup_info_by_moid**](ApplianceApi.md#get_appliance_setup_info_by_moid) | **GET** /api/v1/appliance/SetupInfos/{Moid} | Read a &#39;appliance.SetupInfo&#39; resource.
[**get_appliance_setup_info_list**](ApplianceApi.md#get_appliance_setup_info_list) | **GET** /api/v1/appliance/SetupInfos | Read a &#39;appliance.SetupInfo&#39; resource.
[**get_appliance_system_info_by_moid**](ApplianceApi.md#get_appliance_system_info_by_moid) | **GET** /api/v1/appliance/SystemInfos/{Moid} | Read a &#39;appliance.SystemInfo&#39; resource.
[**get_appliance_system_info_list**](ApplianceApi.md#get_appliance_system_info_list) | **GET** /api/v1/appliance/SystemInfos | Read a &#39;appliance.SystemInfo&#39; resource.
[**get_appliance_upgrade_by_moid**](ApplianceApi.md#get_appliance_upgrade_by_moid) | **GET** /api/v1/appliance/Upgrades/{Moid} | Read a &#39;appliance.Upgrade&#39; resource.
[**get_appliance_upgrade_list**](ApplianceApi.md#get_appliance_upgrade_list) | **GET** /api/v1/appliance/Upgrades | Read a &#39;appliance.Upgrade&#39; resource.
[**get_appliance_upgrade_policy_by_moid**](ApplianceApi.md#get_appliance_upgrade_policy_by_moid) | **GET** /api/v1/appliance/UpgradePolicies/{Moid} | Read a &#39;appliance.UpgradePolicy&#39; resource.
[**get_appliance_upgrade_policy_list**](ApplianceApi.md#get_appliance_upgrade_policy_list) | **GET** /api/v1/appliance/UpgradePolicies | Read a &#39;appliance.UpgradePolicy&#39; resource.
[**patch_appliance_backup_policy**](ApplianceApi.md#patch_appliance_backup_policy) | **PATCH** /api/v1/appliance/BackupPolicies/{Moid} | Update a &#39;appliance.BackupPolicy&#39; resource.
[**patch_appliance_certificate_setting**](ApplianceApi.md#patch_appliance_certificate_setting) | **PATCH** /api/v1/appliance/CertificateSettings/{Moid} | Update a &#39;appliance.CertificateSetting&#39; resource.
[**patch_appliance_data_export_policy**](ApplianceApi.md#patch_appliance_data_export_policy) | **PATCH** /api/v1/appliance/DataExportPolicies/{Moid} | Update a &#39;appliance.DataExportPolicy&#39; resource.
[**patch_appliance_diag_setting**](ApplianceApi.md#patch_appliance_diag_setting) | **PATCH** /api/v1/appliance/DiagSettings/{Moid} | Update a &#39;appliance.DiagSetting&#39; resource.
[**patch_appliance_setup_info**](ApplianceApi.md#patch_appliance_setup_info) | **PATCH** /api/v1/appliance/SetupInfos/{Moid} | Update a &#39;appliance.SetupInfo&#39; resource.
[**patch_appliance_upgrade**](ApplianceApi.md#patch_appliance_upgrade) | **PATCH** /api/v1/appliance/Upgrades/{Moid} | Update a &#39;appliance.Upgrade&#39; resource.
[**patch_appliance_upgrade_policy**](ApplianceApi.md#patch_appliance_upgrade_policy) | **PATCH** /api/v1/appliance/UpgradePolicies/{Moid} | Update a &#39;appliance.UpgradePolicy&#39; resource.
[**update_appliance_backup_policy**](ApplianceApi.md#update_appliance_backup_policy) | **POST** /api/v1/appliance/BackupPolicies/{Moid} | Update a &#39;appliance.BackupPolicy&#39; resource.
[**update_appliance_certificate_setting**](ApplianceApi.md#update_appliance_certificate_setting) | **POST** /api/v1/appliance/CertificateSettings/{Moid} | Update a &#39;appliance.CertificateSetting&#39; resource.
[**update_appliance_data_export_policy**](ApplianceApi.md#update_appliance_data_export_policy) | **POST** /api/v1/appliance/DataExportPolicies/{Moid} | Update a &#39;appliance.DataExportPolicy&#39; resource.
[**update_appliance_diag_setting**](ApplianceApi.md#update_appliance_diag_setting) | **POST** /api/v1/appliance/DiagSettings/{Moid} | Update a &#39;appliance.DiagSetting&#39; resource.
[**update_appliance_setup_info**](ApplianceApi.md#update_appliance_setup_info) | **POST** /api/v1/appliance/SetupInfos/{Moid} | Update a &#39;appliance.SetupInfo&#39; resource.
[**update_appliance_upgrade**](ApplianceApi.md#update_appliance_upgrade) | **POST** /api/v1/appliance/Upgrades/{Moid} | Update a &#39;appliance.Upgrade&#39; resource.
[**update_appliance_upgrade_policy**](ApplianceApi.md#update_appliance_upgrade_policy) | **POST** /api/v1/appliance/UpgradePolicies/{Moid} | Update a &#39;appliance.UpgradePolicy&#39; resource.


# **create_appliance_backup**
> ApplianceBackup create_appliance_backup(appliance_backup)

Create a 'appliance.Backup' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup import ApplianceBackup
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
    api_instance = appliance_api.ApplianceApi(api_client)
    appliance_backup = ApplianceBackup() # ApplianceBackup | The 'appliance.Backup' resource to create.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)
    if_none_match = "If-None-Match_example" # str | For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn't happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don't have to be identical byte for byte. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a 'appliance.Backup' resource.
        api_response = api_instance.create_appliance_backup(appliance_backup)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_backup: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a 'appliance.Backup' resource.
        api_response = api_instance.create_appliance_backup(appliance_backup, if_match=if_match, if_none_match=if_none_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_backup** | [**ApplianceBackup**](ApplianceBackup.md)| The &#39;appliance.Backup&#39; resource to create. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]
 **if_none_match** | **str**| For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn&#39;t happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource&#39;s ETag doesn&#39;t match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don&#39;t have to be identical byte for byte. | [optional]

### Return type

[**ApplianceBackup**](ApplianceBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Backup&#39; resource was created as requested. The &#39;appliance.Backup&#39; resource is created before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Backup&#39; resource is asynchronously being created as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_backup_policy**
> ApplianceBackupPolicy create_appliance_backup_policy(appliance_backup_policy)

Create a 'appliance.BackupPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup_policy import ApplianceBackupPolicy
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
    api_instance = appliance_api.ApplianceApi(api_client)
    appliance_backup_policy = ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to create.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)
    if_none_match = "If-None-Match_example" # str | For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn't happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don't have to be identical byte for byte. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a 'appliance.BackupPolicy' resource.
        api_response = api_instance.create_appliance_backup_policy(appliance_backup_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_backup_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a 'appliance.BackupPolicy' resource.
        api_response = api_instance.create_appliance_backup_policy(appliance_backup_policy, if_match=if_match, if_none_match=if_none_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_backup_policy** | [**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)| The &#39;appliance.BackupPolicy&#39; resource to create. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]
 **if_none_match** | **str**| For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn&#39;t happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource&#39;s ETag doesn&#39;t match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don&#39;t have to be identical byte for byte. | [optional]

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.BackupPolicy&#39; resource was created as requested. The &#39;appliance.BackupPolicy&#39; resource is created before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.BackupPolicy&#39; resource is asynchronously being created as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_data_export_policy**
> ApplianceDataExportPolicy create_appliance_data_export_policy(appliance_data_export_policy)

Create a 'appliance.DataExportPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_data_export_policy import ApplianceDataExportPolicy
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    appliance_data_export_policy = ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to create.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)
    if_none_match = "If-None-Match_example" # str | For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn't happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don't have to be identical byte for byte. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.create_appliance_data_export_policy(appliance_data_export_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_data_export_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.create_appliance_data_export_policy(appliance_data_export_policy, if_match=if_match, if_none_match=if_none_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_data_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_data_export_policy** | [**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)| The &#39;appliance.DataExportPolicy&#39; resource to create. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]
 **if_none_match** | **str**| For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn&#39;t happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource&#39;s ETag doesn&#39;t match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don&#39;t have to be identical byte for byte. | [optional]

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DataExportPolicy&#39; resource was created as requested. The &#39;appliance.DataExportPolicy&#39; resource is created before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DataExportPolicy&#39; resource is asynchronously being created as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_device_claim**
> ApplianceDeviceClaim create_appliance_device_claim(appliance_device_claim)

Create a 'appliance.DeviceClaim' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_device_claim import ApplianceDeviceClaim
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
    api_instance = appliance_api.ApplianceApi(api_client)
    appliance_device_claim = ApplianceDeviceClaim() # ApplianceDeviceClaim | The 'appliance.DeviceClaim' resource to create.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)
    if_none_match = "If-None-Match_example" # str | For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn't happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don't have to be identical byte for byte. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a 'appliance.DeviceClaim' resource.
        api_response = api_instance.create_appliance_device_claim(appliance_device_claim)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_device_claim: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a 'appliance.DeviceClaim' resource.
        api_response = api_instance.create_appliance_device_claim(appliance_device_claim, if_match=if_match, if_none_match=if_none_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_device_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_device_claim** | [**ApplianceDeviceClaim**](ApplianceDeviceClaim.md)| The &#39;appliance.DeviceClaim&#39; resource to create. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]
 **if_none_match** | **str**| For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn&#39;t happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource&#39;s ETag doesn&#39;t match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don&#39;t have to be identical byte for byte. | [optional]

### Return type

[**ApplianceDeviceClaim**](ApplianceDeviceClaim.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DeviceClaim&#39; resource was created as requested. The &#39;appliance.DeviceClaim&#39; resource is created before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DeviceClaim&#39; resource is asynchronously being created as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_diag_setting**
> ApplianceDiagSetting create_appliance_diag_setting(appliance_diag_setting)

Create a 'appliance.DiagSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_diag_setting import ApplianceDiagSetting
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
    api_instance = appliance_api.ApplianceApi(api_client)
    appliance_diag_setting = ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to create.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)
    if_none_match = "If-None-Match_example" # str | For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn't happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don't have to be identical byte for byte. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a 'appliance.DiagSetting' resource.
        api_response = api_instance.create_appliance_diag_setting(appliance_diag_setting)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_diag_setting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a 'appliance.DiagSetting' resource.
        api_response = api_instance.create_appliance_diag_setting(appliance_diag_setting, if_match=if_match, if_none_match=if_none_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_diag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_diag_setting** | [**ApplianceDiagSetting**](ApplianceDiagSetting.md)| The &#39;appliance.DiagSetting&#39; resource to create. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]
 **if_none_match** | **str**| For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn&#39;t happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource&#39;s ETag doesn&#39;t match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don&#39;t have to be identical byte for byte. | [optional]

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DiagSetting&#39; resource was created as requested. The &#39;appliance.DiagSetting&#39; resource is created before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DiagSetting&#39; resource is asynchronously being created as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_appliance_restore**
> ApplianceRestore create_appliance_restore(appliance_restore)

Create a 'appliance.Restore' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_restore import ApplianceRestore
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    appliance_restore = ApplianceRestore() # ApplianceRestore | The 'appliance.Restore' resource to create.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)
    if_none_match = "If-None-Match_example" # str | For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn't happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource's ETag doesn't match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don't have to be identical byte for byte. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a 'appliance.Restore' resource.
        api_response = api_instance.create_appliance_restore(appliance_restore)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_restore: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a 'appliance.Restore' resource.
        api_response = api_instance.create_appliance_restore(appliance_restore, if_match=if_match, if_none_match=if_none_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->create_appliance_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appliance_restore** | [**ApplianceRestore**](ApplianceRestore.md)| The &#39;appliance.Restore&#39; resource to create. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]
 **if_none_match** | **str**| For methods that apply server-side changes, If-None-Match used with the * value can be used to create a resource not known to exist, guaranteeing that another resource creation didn&#39;t happen before, losing the data of the previous put. The request will be processed only if the eventually existing resource&#39;s ETag doesn&#39;t match any of the values listed. Otherwise, the status code 412 (Precondition Failed) is used. The asterisk is a special value representing any resource. It is only useful when creating a resource, usually with PUT, to check if another resource with the identity has already been created before. The comparison with the stored ETag uses the weak comparison algorithm, meaning two resources are considered identical if the content is equivalent - they don&#39;t have to be identical byte for byte. | [optional]

### Return type

[**ApplianceRestore**](ApplianceRestore.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Restore&#39; resource was created as requested. The &#39;appliance.Restore&#39; resource is created before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Restore&#39; resource is asynchronously being created as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appliance_backup**
> delete_appliance_backup(moid)

Delete a 'appliance.Backup' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Delete a 'appliance.Backup' resource.
        api_instance.delete_appliance_backup(moid)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->delete_appliance_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource has been deleted successfully. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The request has been accepted, the resource is being deleted asynchronously. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_appliance_restore**
> delete_appliance_restore(moid)

Delete a 'appliance.Restore' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Delete a 'appliance.Restore' resource.
        api_instance.delete_appliance_restore(moid)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->delete_appliance_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource has been deleted successfully. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The request has been accepted, the resource is being deleted asynchronously. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_backup_by_moid**
> ApplianceBackup get_appliance_backup_by_moid(moid)

Read a 'appliance.Backup' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup import ApplianceBackup
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.Backup' resource.
        api_response = api_instance.get_appliance_backup_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_backup_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceBackup**](ApplianceBackup.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.Backup&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_backup_list**
> ApplianceBackupResponse get_appliance_backup_list()

Read a 'appliance.Backup' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup_response import ApplianceBackupResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.Backup' resource.
        api_response = api_instance.get_appliance_backup_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_backup_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceBackupResponse**](ApplianceBackupResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.Backup&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_backup_policy_by_moid**
> ApplianceBackupPolicy get_appliance_backup_policy_by_moid(moid)

Read a 'appliance.BackupPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup_policy import ApplianceBackupPolicy
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.BackupPolicy' resource.
        api_response = api_instance.get_appliance_backup_policy_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_backup_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.BackupPolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_backup_policy_list**
> ApplianceBackupPolicyResponse get_appliance_backup_policy_list()

Read a 'appliance.BackupPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup_policy_response import ApplianceBackupPolicyResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.BackupPolicy' resource.
        api_response = api_instance.get_appliance_backup_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_backup_policy_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceBackupPolicyResponse**](ApplianceBackupPolicyResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.BackupPolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_certificate_setting_by_moid**
> ApplianceCertificateSetting get_appliance_certificate_setting_by_moid(moid)

Read a 'appliance.CertificateSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_certificate_setting import ApplianceCertificateSetting
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.CertificateSetting' resource.
        api_response = api_instance.get_appliance_certificate_setting_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_certificate_setting_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.CertificateSetting&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_certificate_setting_list**
> ApplianceCertificateSettingResponse get_appliance_certificate_setting_list()

Read a 'appliance.CertificateSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_certificate_setting_response import ApplianceCertificateSettingResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.CertificateSetting' resource.
        api_response = api_instance.get_appliance_certificate_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_certificate_setting_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceCertificateSettingResponse**](ApplianceCertificateSettingResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.CertificateSetting&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_data_export_policy_by_moid**
> ApplianceDataExportPolicy get_appliance_data_export_policy_by_moid(moid)

Read a 'appliance.DataExportPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_data_export_policy import ApplianceDataExportPolicy
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.get_appliance_data_export_policy_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_data_export_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.DataExportPolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_data_export_policy_list**
> ApplianceDataExportPolicyResponse get_appliance_data_export_policy_list()

Read a 'appliance.DataExportPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_data_export_policy_response import ApplianceDataExportPolicyResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.get_appliance_data_export_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_data_export_policy_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceDataExportPolicyResponse**](ApplianceDataExportPolicyResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.DataExportPolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_device_claim_by_moid**
> ApplianceDeviceClaim get_appliance_device_claim_by_moid(moid)

Read a 'appliance.DeviceClaim' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_device_claim import ApplianceDeviceClaim
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.DeviceClaim' resource.
        api_response = api_instance.get_appliance_device_claim_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_device_claim_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceDeviceClaim**](ApplianceDeviceClaim.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.DeviceClaim&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_device_claim_list**
> ApplianceDeviceClaimResponse get_appliance_device_claim_list()

Read a 'appliance.DeviceClaim' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_device_claim_response import ApplianceDeviceClaimResponse
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.DeviceClaim' resource.
        api_response = api_instance.get_appliance_device_claim_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_device_claim_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceDeviceClaimResponse**](ApplianceDeviceClaimResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.DeviceClaim&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_diag_setting_by_moid**
> ApplianceDiagSetting get_appliance_diag_setting_by_moid(moid)

Read a 'appliance.DiagSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_diag_setting import ApplianceDiagSetting
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.DiagSetting' resource.
        api_response = api_instance.get_appliance_diag_setting_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_diag_setting_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.DiagSetting&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_diag_setting_list**
> ApplianceDiagSettingResponse get_appliance_diag_setting_list()

Read a 'appliance.DiagSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_diag_setting_response import ApplianceDiagSettingResponse
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.DiagSetting' resource.
        api_response = api_instance.get_appliance_diag_setting_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_diag_setting_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceDiagSettingResponse**](ApplianceDiagSettingResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.DiagSetting&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_image_bundle_by_moid**
> ApplianceImageBundle get_appliance_image_bundle_by_moid(moid)

Read a 'appliance.ImageBundle' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_image_bundle import ApplianceImageBundle
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.ImageBundle' resource.
        api_response = api_instance.get_appliance_image_bundle_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_image_bundle_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceImageBundle**](ApplianceImageBundle.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.ImageBundle&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_image_bundle_list**
> ApplianceImageBundleResponse get_appliance_image_bundle_list()

Read a 'appliance.ImageBundle' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_image_bundle_response import ApplianceImageBundleResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.ImageBundle' resource.
        api_response = api_instance.get_appliance_image_bundle_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_image_bundle_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceImageBundleResponse**](ApplianceImageBundleResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.ImageBundle&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_node_info_by_moid**
> ApplianceNodeInfo get_appliance_node_info_by_moid(moid)

Read a 'appliance.NodeInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_node_info import ApplianceNodeInfo
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.NodeInfo' resource.
        api_response = api_instance.get_appliance_node_info_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_node_info_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceNodeInfo**](ApplianceNodeInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.NodeInfo&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_node_info_list**
> ApplianceNodeInfoResponse get_appliance_node_info_list()

Read a 'appliance.NodeInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_node_info_response import ApplianceNodeInfoResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.NodeInfo' resource.
        api_response = api_instance.get_appliance_node_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_node_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceNodeInfoResponse**](ApplianceNodeInfoResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.NodeInfo&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_release_note_by_moid**
> ApplianceReleaseNote get_appliance_release_note_by_moid(moid)

Read a 'appliance.ReleaseNote' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_release_note import ApplianceReleaseNote
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.ReleaseNote' resource.
        api_response = api_instance.get_appliance_release_note_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_release_note_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceReleaseNote**](ApplianceReleaseNote.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.ReleaseNote&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_release_note_list**
> ApplianceReleaseNoteResponse get_appliance_release_note_list()

Read a 'appliance.ReleaseNote' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_release_note_response import ApplianceReleaseNoteResponse
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.ReleaseNote' resource.
        api_response = api_instance.get_appliance_release_note_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_release_note_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceReleaseNoteResponse**](ApplianceReleaseNoteResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.ReleaseNote&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_restore_by_moid**
> ApplianceRestore get_appliance_restore_by_moid(moid)

Read a 'appliance.Restore' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_restore import ApplianceRestore
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.Restore' resource.
        api_response = api_instance.get_appliance_restore_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_restore_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceRestore**](ApplianceRestore.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.Restore&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_restore_list**
> ApplianceRestoreResponse get_appliance_restore_list()

Read a 'appliance.Restore' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_restore_response import ApplianceRestoreResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.Restore' resource.
        api_response = api_instance.get_appliance_restore_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_restore_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceRestoreResponse**](ApplianceRestoreResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.Restore&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_setup_info_by_moid**
> ApplianceSetupInfo get_appliance_setup_info_by_moid(moid)

Read a 'appliance.SetupInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_setup_info import ApplianceSetupInfo
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.SetupInfo' resource.
        api_response = api_instance.get_appliance_setup_info_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_setup_info_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceSetupInfo**](ApplianceSetupInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.SetupInfo&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_setup_info_list**
> ApplianceSetupInfoResponse get_appliance_setup_info_list()

Read a 'appliance.SetupInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_setup_info_response import ApplianceSetupInfoResponse
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.SetupInfo' resource.
        api_response = api_instance.get_appliance_setup_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_setup_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceSetupInfoResponse**](ApplianceSetupInfoResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.SetupInfo&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_system_info_by_moid**
> ApplianceSystemInfo get_appliance_system_info_by_moid(moid)

Read a 'appliance.SystemInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_system_info import ApplianceSystemInfo
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.SystemInfo' resource.
        api_response = api_instance.get_appliance_system_info_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_system_info_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceSystemInfo**](ApplianceSystemInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.SystemInfo&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_system_info_list**
> ApplianceSystemInfoResponse get_appliance_system_info_list()

Read a 'appliance.SystemInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_system_info_response import ApplianceSystemInfoResponse
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.SystemInfo' resource.
        api_response = api_instance.get_appliance_system_info_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_system_info_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceSystemInfoResponse**](ApplianceSystemInfoResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.SystemInfo&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_by_moid**
> ApplianceUpgrade get_appliance_upgrade_by_moid(moid)

Read a 'appliance.Upgrade' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_upgrade import ApplianceUpgrade
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.Upgrade' resource.
        api_response = api_instance.get_appliance_upgrade_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_upgrade_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceUpgrade**](ApplianceUpgrade.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.Upgrade&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_list**
> ApplianceUpgradeResponse get_appliance_upgrade_list()

Read a 'appliance.Upgrade' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_upgrade_response import ApplianceUpgradeResponse
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.Upgrade' resource.
        api_response = api_instance.get_appliance_upgrade_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_upgrade_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceUpgradeResponse**](ApplianceUpgradeResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.Upgrade&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_policy_by_moid**
> ApplianceUpgradePolicy get_appliance_upgrade_policy_by_moid(moid)

Read a 'appliance.UpgradePolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_upgrade_policy import ApplianceUpgradePolicy
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.

    # example passing only required values which don't have defaults set
    try:
        # Read a 'appliance.UpgradePolicy' resource.
        api_response = api_instance.get_appliance_upgrade_policy_by_moid(moid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_upgrade_policy_by_moid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |

### Return type

[**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An instance of the &#39;appliance.UpgradePolicy&#39; resource. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appliance_upgrade_policy_list**
> ApplianceUpgradePolicyResponse get_appliance_upgrade_policy_list()

Read a 'appliance.UpgradePolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_upgrade_policy_response import ApplianceUpgradePolicyResponse
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
    api_instance = appliance_api.ApplianceApi(api_client)
    filter = "$filter=CreateTime gt 2012-08-29T21:58:33Z" # str | Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). (optional) if omitted the server will use the default value of ""
    orderby = "$orderby=CreationTime" # str | Determines what properties are used to sort the collection of resources. (optional)
    top = $top=10 # int | Specifies the maximum number of resources to return in the response. (optional) if omitted the server will use the default value of 100
    skip = $skip=100 # int | Specifies the number of resources to skip in the response. (optional) if omitted the server will use the default value of 0
    select = "$select=CreateTime,ModTime" # str | Specifies a subset of properties to return. (optional) if omitted the server will use the default value of ""
    expand = "$expand=DisplayNames" # str | Specify additional attributes or related resources to return in addition to the primary resources. (optional)
    apply = "$apply_example" # str | Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \"$apply\" query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \"aggregate\" and \"groupby\". The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. (optional)
    count = True # bool | The $count query specifies the service should return the count of the matching resources, instead of returning the resources. (optional)
    inlinecount = "$inlinecount=true" # str | The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. (optional) if omitted the server will use the default value of "allpages"
    at = "at=VersionType eq 'Configured'" # str | Similar to \"$filter\", but \"at\" is specifically used to filter versioning information properties for resources to return. A URI with an \"at\" Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. (optional)
    tags = "tags_example" # str | The 'tags' parameter is used to request a summary of the Tag utilization for this resource. When the 'tags' parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Read a 'appliance.UpgradePolicy' resource.
        api_response = api_instance.get_appliance_upgrade_policy_list(filter=filter, orderby=orderby, top=top, skip=skip, select=select, expand=expand, apply=apply, count=count, inlinecount=inlinecount, at=at, tags=tags)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->get_appliance_upgrade_policy_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria for the resources to return. A URI with a $filter query option identifies a subset of the entries from the Collection of Entries. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the $filter option. The expression language that is used in $filter queries supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false). | [optional] if omitted the server will use the default value of ""
 **orderby** | **str**| Determines what properties are used to sort the collection of resources. | [optional]
 **top** | **int**| Specifies the maximum number of resources to return in the response. | [optional] if omitted the server will use the default value of 100
 **skip** | **int**| Specifies the number of resources to skip in the response. | [optional] if omitted the server will use the default value of 0
 **select** | **str**| Specifies a subset of properties to return. | [optional] if omitted the server will use the default value of ""
 **expand** | **str**| Specify additional attributes or related resources to return in addition to the primary resources. | [optional]
 **apply** | **str**| Specify one or more transformation operations to perform aggregation on the resources. The transformations are processed in order with the output from a transformation being used as input for the subsequent transformation. The \&quot;$apply\&quot; query takes a sequence of set transformations, separated by forward slashes to express that they are consecutively applied, i.e. the result of each transformation is the input to the next transformation. Supported aggregation methods are \&quot;aggregate\&quot; and \&quot;groupby\&quot;. The **aggregate** transformation takes a comma-separated list of one or more aggregate expressions as parameters and returns a result set with a single instance, representing the aggregated value for all instances in the input set. The **groupby** transformation takes one or two parameters and 1. Splits the initial set into subsets where all instances in a subset have the same values for the grouping properties specified in the first parameter, 2. Applies set transformations to each subset according to the second parameter, resulting in a new set of potentially different structure and cardinality, 3. Ensures that the instances in the result set contain all grouping properties with the correct values for the group, 4. Concatenates the intermediate result sets into one result set. A groupby transformation affects the structure of the result set. | [optional]
 **count** | **bool**| The $count query specifies the service should return the count of the matching resources, instead of returning the resources. | [optional]
 **inlinecount** | **str**| The $inlinecount query option allows clients to request an inline count of the matching resources included with the resources in the response. | [optional] if omitted the server will use the default value of "allpages"
 **at** | **str**| Similar to \&quot;$filter\&quot;, but \&quot;at\&quot; is specifically used to filter versioning information properties for resources to return. A URI with an \&quot;at\&quot; Query Option identifies a subset of the Entries from the Collection of Entries identified by the Resource Path section of the URI. The subset is determined by selecting only the Entries that satisfy the predicate expression specified by the query option. The expression language that is used in at operators supports references to properties and literals. The literal values can be strings enclosed in single quotes, numbers and boolean values (true or false) or any of the additional literal representations shown in the Abstract Type System section. | [optional]
 **tags** | **str**| The &#39;tags&#39; parameter is used to request a summary of the Tag utilization for this resource. When the &#39;tags&#39; parameter is specified, the response provides a list of tag keys, the number of times the key has been used across all documents, and the tag values that have been assigned to the tag key. | [optional]

### Return type

[**ApplianceUpgradePolicyResponse**](ApplianceUpgradePolicyResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of &#39;appliance.UpgradePolicy&#39; resources for the given filter criteria |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  * Content-Disposition -  <br>  * Content-Length -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_backup_policy**
> ApplianceBackupPolicy patch_appliance_backup_policy(moid, appliance_backup_policy)

Update a 'appliance.BackupPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup_policy import ApplianceBackupPolicy
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_backup_policy = ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.BackupPolicy' resource.
        api_response = api_instance.patch_appliance_backup_policy(moid, appliance_backup_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_backup_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.BackupPolicy' resource.
        api_response = api_instance.patch_appliance_backup_policy(moid, appliance_backup_policy, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_backup_policy** | [**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)| The &#39;appliance.BackupPolicy&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.BackupPolicy&#39; resource was patched as requested. The &#39;appliance.BackupPolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.BackupPolicy&#39; resource is asynchronously being patched as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_certificate_setting**
> ApplianceCertificateSetting patch_appliance_certificate_setting(moid, appliance_certificate_setting)

Update a 'appliance.CertificateSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_certificate_setting import ApplianceCertificateSetting
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_certificate_setting = ApplianceCertificateSetting() # ApplianceCertificateSetting | The 'appliance.CertificateSetting' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.CertificateSetting' resource.
        api_response = api_instance.patch_appliance_certificate_setting(moid, appliance_certificate_setting)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_certificate_setting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.CertificateSetting' resource.
        api_response = api_instance.patch_appliance_certificate_setting(moid, appliance_certificate_setting, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_certificate_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_certificate_setting** | [**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)| The &#39;appliance.CertificateSetting&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.CertificateSetting&#39; resource was patched as requested. The &#39;appliance.CertificateSetting&#39; resource is patched before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.CertificateSetting&#39; resource is asynchronously being patched as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_data_export_policy**
> ApplianceDataExportPolicy patch_appliance_data_export_policy(moid, appliance_data_export_policy)

Update a 'appliance.DataExportPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_data_export_policy import ApplianceDataExportPolicy
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_data_export_policy = ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.patch_appliance_data_export_policy(moid, appliance_data_export_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_data_export_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.patch_appliance_data_export_policy(moid, appliance_data_export_policy, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_data_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_data_export_policy** | [**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)| The &#39;appliance.DataExportPolicy&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DataExportPolicy&#39; resource was patched as requested. The &#39;appliance.DataExportPolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DataExportPolicy&#39; resource is asynchronously being patched as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_diag_setting**
> ApplianceDiagSetting patch_appliance_diag_setting(moid, appliance_diag_setting)

Update a 'appliance.DiagSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_diag_setting import ApplianceDiagSetting
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_diag_setting = ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.DiagSetting' resource.
        api_response = api_instance.patch_appliance_diag_setting(moid, appliance_diag_setting)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_diag_setting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.DiagSetting' resource.
        api_response = api_instance.patch_appliance_diag_setting(moid, appliance_diag_setting, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_diag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_diag_setting** | [**ApplianceDiagSetting**](ApplianceDiagSetting.md)| The &#39;appliance.DiagSetting&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DiagSetting&#39; resource was patched as requested. The &#39;appliance.DiagSetting&#39; resource is patched before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DiagSetting&#39; resource is asynchronously being patched as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_setup_info**
> ApplianceSetupInfo patch_appliance_setup_info(moid, appliance_setup_info)

Update a 'appliance.SetupInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_setup_info import ApplianceSetupInfo
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_setup_info = ApplianceSetupInfo() # ApplianceSetupInfo | The 'appliance.SetupInfo' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.SetupInfo' resource.
        api_response = api_instance.patch_appliance_setup_info(moid, appliance_setup_info)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_setup_info: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.SetupInfo' resource.
        api_response = api_instance.patch_appliance_setup_info(moid, appliance_setup_info, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_setup_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_setup_info** | [**ApplianceSetupInfo**](ApplianceSetupInfo.md)| The &#39;appliance.SetupInfo&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceSetupInfo**](ApplianceSetupInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.SetupInfo&#39; resource was patched as requested. The &#39;appliance.SetupInfo&#39; resource is patched before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.SetupInfo&#39; resource is asynchronously being patched as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_upgrade**
> ApplianceUpgrade patch_appliance_upgrade(moid, appliance_upgrade)

Update a 'appliance.Upgrade' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_upgrade import ApplianceUpgrade
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_upgrade = ApplianceUpgrade() # ApplianceUpgrade | The 'appliance.Upgrade' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.Upgrade' resource.
        api_response = api_instance.patch_appliance_upgrade(moid, appliance_upgrade)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_upgrade: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.Upgrade' resource.
        api_response = api_instance.patch_appliance_upgrade(moid, appliance_upgrade, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_upgrade** | [**ApplianceUpgrade**](ApplianceUpgrade.md)| The &#39;appliance.Upgrade&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceUpgrade**](ApplianceUpgrade.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Upgrade&#39; resource was patched as requested. The &#39;appliance.Upgrade&#39; resource is patched before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Upgrade&#39; resource is asynchronously being patched as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_appliance_upgrade_policy**
> ApplianceUpgradePolicy patch_appliance_upgrade_policy(moid, appliance_upgrade_policy)

Update a 'appliance.UpgradePolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_upgrade_policy import ApplianceUpgradePolicy
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_upgrade_policy = ApplianceUpgradePolicy() # ApplianceUpgradePolicy | The 'appliance.UpgradePolicy' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.UpgradePolicy' resource.
        api_response = api_instance.patch_appliance_upgrade_policy(moid, appliance_upgrade_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_upgrade_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.UpgradePolicy' resource.
        api_response = api_instance.patch_appliance_upgrade_policy(moid, appliance_upgrade_policy, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->patch_appliance_upgrade_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_upgrade_policy** | [**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)| The &#39;appliance.UpgradePolicy&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.UpgradePolicy&#39; resource was patched as requested. The &#39;appliance.UpgradePolicy&#39; resource is patched before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.UpgradePolicy&#39; resource is asynchronously being patched as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_backup_policy**
> ApplianceBackupPolicy update_appliance_backup_policy(moid, appliance_backup_policy)

Update a 'appliance.BackupPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_backup_policy import ApplianceBackupPolicy
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_backup_policy = ApplianceBackupPolicy() # ApplianceBackupPolicy | The 'appliance.BackupPolicy' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.BackupPolicy' resource.
        api_response = api_instance.update_appliance_backup_policy(moid, appliance_backup_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_backup_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.BackupPolicy' resource.
        api_response = api_instance.update_appliance_backup_policy(moid, appliance_backup_policy, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_backup_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_backup_policy** | [**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)| The &#39;appliance.BackupPolicy&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceBackupPolicy**](ApplianceBackupPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.BackupPolicy&#39; resource was modified as requested. The &#39;appliance.BackupPolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.BackupPolicy&#39; resource is asynchronously being modified as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_certificate_setting**
> ApplianceCertificateSetting update_appliance_certificate_setting(moid, appliance_certificate_setting)

Update a 'appliance.CertificateSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_certificate_setting import ApplianceCertificateSetting
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_certificate_setting = ApplianceCertificateSetting() # ApplianceCertificateSetting | The 'appliance.CertificateSetting' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.CertificateSetting' resource.
        api_response = api_instance.update_appliance_certificate_setting(moid, appliance_certificate_setting)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_certificate_setting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.CertificateSetting' resource.
        api_response = api_instance.update_appliance_certificate_setting(moid, appliance_certificate_setting, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_certificate_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_certificate_setting** | [**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)| The &#39;appliance.CertificateSetting&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceCertificateSetting**](ApplianceCertificateSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.CertificateSetting&#39; resource was modified as requested. The &#39;appliance.CertificateSetting&#39; resource is modified before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.CertificateSetting&#39; resource is asynchronously being modified as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_data_export_policy**
> ApplianceDataExportPolicy update_appliance_data_export_policy(moid, appliance_data_export_policy)

Update a 'appliance.DataExportPolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_data_export_policy import ApplianceDataExportPolicy
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_data_export_policy = ApplianceDataExportPolicy() # ApplianceDataExportPolicy | The 'appliance.DataExportPolicy' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.update_appliance_data_export_policy(moid, appliance_data_export_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_data_export_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.DataExportPolicy' resource.
        api_response = api_instance.update_appliance_data_export_policy(moid, appliance_data_export_policy, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_data_export_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_data_export_policy** | [**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)| The &#39;appliance.DataExportPolicy&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceDataExportPolicy**](ApplianceDataExportPolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DataExportPolicy&#39; resource was modified as requested. The &#39;appliance.DataExportPolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DataExportPolicy&#39; resource is asynchronously being modified as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_diag_setting**
> ApplianceDiagSetting update_appliance_diag_setting(moid, appliance_diag_setting)

Update a 'appliance.DiagSetting' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_diag_setting import ApplianceDiagSetting
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_diag_setting = ApplianceDiagSetting() # ApplianceDiagSetting | The 'appliance.DiagSetting' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.DiagSetting' resource.
        api_response = api_instance.update_appliance_diag_setting(moid, appliance_diag_setting)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_diag_setting: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.DiagSetting' resource.
        api_response = api_instance.update_appliance_diag_setting(moid, appliance_diag_setting, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_diag_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_diag_setting** | [**ApplianceDiagSetting**](ApplianceDiagSetting.md)| The &#39;appliance.DiagSetting&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceDiagSetting**](ApplianceDiagSetting.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.DiagSetting&#39; resource was modified as requested. The &#39;appliance.DiagSetting&#39; resource is modified before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.DiagSetting&#39; resource is asynchronously being modified as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_setup_info**
> ApplianceSetupInfo update_appliance_setup_info(moid, appliance_setup_info)

Update a 'appliance.SetupInfo' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_setup_info import ApplianceSetupInfo
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_setup_info = ApplianceSetupInfo() # ApplianceSetupInfo | The 'appliance.SetupInfo' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.SetupInfo' resource.
        api_response = api_instance.update_appliance_setup_info(moid, appliance_setup_info)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_setup_info: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.SetupInfo' resource.
        api_response = api_instance.update_appliance_setup_info(moid, appliance_setup_info, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_setup_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_setup_info** | [**ApplianceSetupInfo**](ApplianceSetupInfo.md)| The &#39;appliance.SetupInfo&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceSetupInfo**](ApplianceSetupInfo.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.SetupInfo&#39; resource was modified as requested. The &#39;appliance.SetupInfo&#39; resource is modified before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.SetupInfo&#39; resource is asynchronously being modified as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_upgrade**
> ApplianceUpgrade update_appliance_upgrade(moid, appliance_upgrade)

Update a 'appliance.Upgrade' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.appliance_upgrade import ApplianceUpgrade
from openapi_client.model.error import Error
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_upgrade = ApplianceUpgrade() # ApplianceUpgrade | The 'appliance.Upgrade' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.Upgrade' resource.
        api_response = api_instance.update_appliance_upgrade(moid, appliance_upgrade)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_upgrade: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.Upgrade' resource.
        api_response = api_instance.update_appliance_upgrade(moid, appliance_upgrade, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_upgrade** | [**ApplianceUpgrade**](ApplianceUpgrade.md)| The &#39;appliance.Upgrade&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceUpgrade**](ApplianceUpgrade.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.Upgrade&#39; resource was modified as requested. The &#39;appliance.Upgrade&#39; resource is modified before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.Upgrade&#39; resource is asynchronously being modified as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_appliance_upgrade_policy**
> ApplianceUpgradePolicy update_appliance_upgrade_policy(moid, appliance_upgrade_policy)

Update a 'appliance.UpgradePolicy' resource.

### Example

* Api Key Authentication (cookieAuth):
* OAuth Authentication (oAuth2):
```python
import time
import openapi_client
from openapi_client.api import appliance_api
from openapi_client.model.error import Error
from openapi_client.model.appliance_upgrade_policy import ApplianceUpgradePolicy
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
    api_instance = appliance_api.ApplianceApi(api_client)
    moid = "Moid_example" # str | The unique Moid identifier of a resource instance.
    appliance_upgrade_policy = ApplianceUpgradePolicy() # ApplianceUpgradePolicy | The 'appliance.UpgradePolicy' resource to update.
    if_match = "If-Match_example" # str | For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a 'appliance.UpgradePolicy' resource.
        api_response = api_instance.update_appliance_upgrade_policy(moid, appliance_upgrade_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_upgrade_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a 'appliance.UpgradePolicy' resource.
        api_response = api_instance.update_appliance_upgrade_policy(moid, appliance_upgrade_policy, if_match=if_match)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ApplianceApi->update_appliance_upgrade_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **moid** | **str**| The unique Moid identifier of a resource instance. |
 **appliance_upgrade_policy** | [**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)| The &#39;appliance.UpgradePolicy&#39; resource to update. |
 **if_match** | **str**| For methods that apply server-side changes, and in particular for PUT, If-Match can be used to prevent the lost update problem. It can check if the modification of a resource that the user wants to upload will not override another change that has been done since the original resource was fetched. If the request cannot be fulfilled, the 412 (Precondition Failed) response is returned. When modifying a resource using POST or PUT, the If-Match header must be set to the value of the resource ModTime property after which no lost update problem should occur. For example, a client send a GET request to obtain a resource, which includes the ModTime property. The ModTime indicates the last time the resource was created or modified. The client then sends a POST or PUT request with the If-Match header set to the ModTime property of the resource as obtained in the GET request. | [optional]

### Return type

[**ApplianceUpgradePolicy**](ApplianceUpgradePolicy.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [http_signature](../README.md#http_signature), [oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The HTTP 200 status response code indicates that the request has succeeded and the &#39;appliance.UpgradePolicy&#39; resource was modified as requested. The &#39;appliance.UpgradePolicy&#39; resource is modified before this response is sent back and the resource is returned in the body of the message. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**202** | The HTTP 202 status response code indicates that the request has succeeded. The &#39;appliance.UpgradePolicy&#39; resource is asynchronously being modified as requested. |  * Set-Cookie -  <br>  * x-starship-traceid -  <br>  |
**400** | The request could not be understood by the server due to malformed syntax. The client SHOULD NOT repeat the request without modifications. For example, the request may contain an incorrect JSON syntax, or the request fails validation checks. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**401** | The request requires user authentication. The client may repeat the request with a suitable Authorization header field. If the request already included Authorization credentials, then the 401 response indicates that authorization has been refused for those credentials. The HTTP body may contain a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**403** | The request was properly authenticated, but the server is refusing to fulfill it. The HTTP body may contain a document that provides more details about the error. For example, the user may not have sufficient privileges to perform the request. |  * x-starship-traceid -  <br>  |
**404** | The specified resource was not found. The HTTP body contains a document that provides more details about the error. |  * x-starship-traceid -  <br>  |
**0** | An unexpected error occurred. |  * x-starship-traceid -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

