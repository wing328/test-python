# TelemetryDruidThetaSketchOperationsPostAggregatorAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Output name for the post-aggregator. | [optional] 
**func** | **str** |  | [optional] 
**fields** | **[str]** | array of fieldAccess type post aggregators to access the thetaSketch aggregators or thetaSketchSetOp type post aggregators to allow arbitrary combination of set operations. | [optional] 
**size** | **int** | must be max of size from sketches in fields input. | [optional]  if omitted the server will use the default value of 16384

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


