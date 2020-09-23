# TelemetryDruidDimensionTopNMetricSpecAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ordering** | **str** | Specifies the sorting order. It can be one of the following values. \&quot;lexicographic\&quot;, \&quot;alphanumeric\&quot;, \&quot;numeric\&quot;, \&quot;strlen\&quot;. * lexicographic - Sorts values by converting Strings to their UTF-8 byte array representations and comparing lexicographically, byte-by-byte. * alphanumeric - Suitable for strings with both numeric and non-numeric content, e.g. \&quot;file12 sorts after file2\&quot;. See https://github.com/amjjd/java-alphanum for more details on how this ordering sorts values. This ordering is not suitable for numbers with decimal points or negative numbers. * numeric - Sorts values as numbers, supports integers and floating point values. Negative values are supported. This sorting order will try to parse all string values as numbers. Unparseable values are treated as nulls, and nulls precede numbers. When comparing two unparseable values (e.g., \&quot;hello\&quot; and \&quot;world\&quot;), this ordering will sort by comparing the unparsed strings lexicographically. * strlen - Sorts values by the their string lengths. When there is a tie, this comparator falls back to using the String compareTo method. * version - Sorts values as versions, e.g. \&quot;10.0 sorts after 9.0\&quot;, \&quot;1.0.0-SNAPSHOT sorts after 1.0.0\&quot;. | [optional]  if omitted the server will use the default value of "lexicographic"
**previous_stop** | **str** | The starting point of the sort. For example, if a previousStop value is &#39;b&#39;, all values before &#39;b&#39; are discarded. This field can be used to paginate through all the dimension values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


