# HclProductAllOf

Definition of the list of properties defined in 'hcl.Product', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_names** | **[str]** |  | [optional] 
**error_code** | **str** | Error code indicating the support status. | [optional] [readonly]  if omitted the server will use the default value of "Success"
**firmwares** | [**[HclFirmware]**](HclFirmware.md) |  | [optional] 
**id** | **str** | Identifier of the product. | [optional] 
**model** | **str** | Model/PID of the product/adapter. | [optional] 
**revision** | **str** | Revision of the adapter model. | [optional] 
**type** | **str** | Type of the product/adapter say OCP, PT, GPU. | [optional] 
**vendor** | **str** | Vendor of the product or adapter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


