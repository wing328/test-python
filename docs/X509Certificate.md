# X509Certificate

The representation of an X.509 certificate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**issuer** | [**PkixDistinguishedName**](PkixDistinguishedName.md) |  | [optional] 
**not_after** | **datetime** | The date on which the certificate&#39;s validity period ends. | [optional] [readonly] 
**not_before** | **datetime** | The date on which the certificate&#39;s validity period begins. | [optional] [readonly] 
**pem_certificate** | **str** | The base64 encoded certificate in PEM format. | [optional] 
**sha256_fingerprint** | **str** | The computed SHA-256 fingerprint of the certificate. Equivalent to &#39;openssl x509 -fingerprint -sha256&#39;. | [optional] [readonly] 
**signature_algorithm** | **str** | Signature algorithm, as specified in [RFC 5280](https://tools.ietf.org/html/rfc5280). | [optional] [readonly] 
**subject** | [**PkixDistinguishedName**](PkixDistinguishedName.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


