# BootPxeAllOf

Definition of the list of properties defined in 'boot.Pxe', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface_name** | **str** | The name of the underlying virtual ethernet interface used by the PXE boot device. | [optional] 
**interface_source** | **str** | Lists the supported Interface Source for PXE device. Supported values are \&quot;name\&quot; and \&quot;mac\&quot;. | [optional]  if omitted the server will use the default value of "name"
**ip_type** | **str** | The IP Address family type to use during the PXE Boot process. | [optional]  if omitted the server will use the default value of "None"
**mac_address** | **str** | The MAC Address of the underlying virtual ethernet interface used by the PXE boot device. | [optional] 
**port** | **int** | The Port ID of the adapter on which the underlying virtual ethernet interface is present. If no port is specified, the default value is -1. Supported values are -1 to 255. | [optional] 
**slot** | **str** | The slot ID of the adapter on which the underlying virtual ethernet interface is present. Supported values are ( 1 - 255, \&quot;MLOM\&quot;, \&quot;L\&quot;, \&quot;L1\&quot;, \&quot;L2\&quot;, \&quot;OCP\&quot;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


