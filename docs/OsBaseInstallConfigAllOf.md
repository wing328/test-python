# OsBaseInstallConfigAllOf

Definition of the list of properties defined in 'os.BaseInstallConfig', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_parameters** | [**[OsPlaceHolder]**](OsPlaceHolder.md) |  | [optional] 
**answers** | [**OsAnswers**](OsAnswers.md) |  | [optional] 
**description** | **str** | User provided description about the OS install configuration. | [optional] 
**install_method** | **str** | The install method to be used for OS installation - vMedia, iPXE.  Only vMedia is supported as of now. | [optional]  if omitted the server will use the default value of "vMedia"
**operating_system_parameters** | [**OsOperatingSystemParameters**](OsOperatingSystemParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


