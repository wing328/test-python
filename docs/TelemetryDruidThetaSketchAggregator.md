# TelemetryDruidThetaSketchAggregator

Theta sketch aggregation provides a class of specialized algorithms, called streaming algorithms, or sketches that can produce results orders-of magnitude faster and with mathematically proven error bounds. For interactive queries there may not be other viable alternatives, and in the case of real-time analysis, sketches are the only known solution. In the analysis of big data there are often problem queries that don’t scale because they require huge compute resources and time to generate exact results. Examples include count distinct, quantiles, most-frequent items, joins, matrix computations, and graph analysis. If approximate results are acceptable, theta sketch aggregation can be used. Logically speaking, a Theta sketch object can be thought of as a set data structure. Sketches are read and aggregated (set unioned) together. A theta sketch query returns the estimate of the number of unique entries in the sketch object. You can use post aggregators to do union, intersection or difference on sketch columns in the same row. You can use thetaSketch aggregator on columns which were not ingested using the same. It will return estimated cardinality of the column.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The aggregator type. | 
**name** | **str** | A String for the output (result) name of the calculation. | 
**field_name** | **str** | A String for the name of the aggregator used at ingestion time. | 
**size** | **int** | Must be a power of 2. Internally, size refers to the maximum number of entries sketch object will retain. Higher size means higher accuracy but more space to store sketches. Note that after you index with a particular size, druid will persist sketch in segments and you will use size greater or equal to that at query time. In general, We recommend just sticking to default size. | [optional]  if omitted the server will use the default value of 16384
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


