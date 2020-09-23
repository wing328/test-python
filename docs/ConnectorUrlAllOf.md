# ConnectorUrlAllOf

Definition of the list of properties defined in 'connector.Url', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_query** | **bool** | Flag to append a query to the url even if rawQuery is empty. | [optional] 
**fragment** | **str** | The fragment identifier component of a URI allows indirect identification of a secondary resource by reference to a primary resource and additional identifying information. The identified secondary resource may be some portion or subset of the primary resource, some view on representations of the primary resource, or some other resource defined or described by those representations. A fragment identifier component is indicated by the presence of a number sign (\&quot;#\&quot;) character and terminated by the end of the URI. | [optional] 
**host** | **str** | The host name identifies the host that holds the resource. The host can be an IP or a hostname that is resolvable by the dns server configured on the platform. | [optional] 
**opaque** | **str** | A URI is opaque if, and only if, it is absolute and its scheme-specific part does not begin with a slash character (&#39;/&#39;). An opaque URI has a scheme, a scheme-specific part, and possibly a fragment; all other components are undefined. | [optional] 
**path** | **str** | The path identifies the specific resource in the host that the web client wants to access. Value is the decoded form of the path. e.g. &#39;/foo/bar&#39;. | [optional] 
**raw_path** | **str** | The URI encoded form of the path property. e.g. &#39;%2Fapi%2Fv1%2F&#39;. | [optional] 
**raw_query** | **str** | The query component, as defined in RFC 3986, contains non-hierarchical data that, along with data in the path component, serves to identify a resource within the scope of the URI&#39;s scheme and naming authority (if any). The query component is indicated by the first question mark character and terminated by a number sign character or by the end of the URI. The rawQuery contains the URIs encoded query component, excluding the ? character. | [optional] 
**scheme** | **str** | The scheme identifies the protocol to be used to access the resource on the Internet. It can be HTTP (without SSL) or HTTPS (with SSL). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


