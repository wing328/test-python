# PkixEcdsaKeySpec

The key pair is generated using Elliptic Curve Digital Signature Algorithm (ECDSA), as defined in FIPS 186-4. The ECDSA standard was originally developed for the American National Standards Institute by the Accredited Standards Committee on Financial Services, X9. ANS X9.62 defines methods for digital signature generation and verification using ECDSA. Specifications for the generation of the domain parameters used during the generation and verification of digital signatures are also included in ANS X9.62.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**curve** | **str** | A specific set of Elliptic Curve parameters, as recommended by NIST in FIPS 186-4. | [optional]  if omitted the server will use the default value of "P256"
**name** | **str** | Name of the key generation algorithm. | [optional] [readonly]  if omitted the server will use the default value of "RSA"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


