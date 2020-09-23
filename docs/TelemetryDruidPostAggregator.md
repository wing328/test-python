# TelemetryDruidPostAggregator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The post-aggregator type. | 
**name** | **str** | Output name for the post-aggregator. | [optional] 
**fn** | **str** | null | [optional] 
**fields** | **[str]** | array of fieldAccess type post aggregators to access the thetaSketch aggregators or thetaSketchSetOp type post aggregators to allow arbitrary combination of set operations. | [optional] 
**ordering** | **str** | Arithmetic post-aggregators may specify an ordering, which defines the order of resulting values when sorting results. This can be useful for topN queries for instance. If no ordering (or null) is specified, the default floating point ordering is used. numericFirst ordering always returns finite values first, followed by NaN, and infinite values last. | [optional] 
**field_name** | **str** | The name field value of the hyperUnique aggregator. | [optional] 
**value** | **float** | The numerical value. | [optional] 
**field** | **str** | Post aggregator of type fieldAccess that refers to a thetaSketch aggregator or that of type thetaSketchSetOp. | [optional] 
**func** | **str** |  | [optional] 
**size** | **int** | must be max of size from sketches in fields input. | [optional]  if omitted the server will use the default value of 16384
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


