# TelemetryDruidAndFilter

A logical AND expression filter.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The filter type. | 
**fields** | [**[TelemetryDruidFilter]**](TelemetryDruidFilter.md) |  | 
**extraction_fn** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | All filters except the \&quot;spatial\&quot; filter support extraction functions. An extraction function is defined by setting the \&quot;extractionFn\&quot; field on a filter. See Extraction function for more details on extraction functions. If specified, the extraction function will be used to transform input values before the filter is applied. The example below shows a selector filter combined with an extraction function. This filter will transform input values according to the values defined in the lookup map; transformed values will then be matched with the string \&quot;bar_1\&quot;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

