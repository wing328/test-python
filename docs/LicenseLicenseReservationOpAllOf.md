# LicenseLicenseReservationOpAllOf

Definition of the list of properties defined in 'license.LicenseReservationOp', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_code** | **str** | Revervation code used to install the license. | [optional] 
**auth_code_installed** | **bool** | Flag to indicate whether authorization code is installed. | [optional] [readonly] 
**confirm_code** | **str** | Confirm code used to complete the license update on smart license account. | [optional] [readonly] 
**generate_request_code** | **bool** | Trigger the generation of request code for specific license reservation. | [optional] 
**generate_return_code** | **bool** | Trigger the generation of return code for specific license reservation. | [optional] 
**request_code** | **str** | Revervation code used to generate authorization code from CSSM. | [optional] [readonly] 
**return_code** | **str** | Return code used to return the reserved license to smart license account. | [optional] [readonly] 
**account** | [**IamAccountRelationship**](IamAccountRelationship.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


