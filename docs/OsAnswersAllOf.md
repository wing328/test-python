# OsAnswersAllOf

Definition of the list of properties defined in 'os.Answers', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_file** | **str** | If the source of the answers is a static file, the content of the file is stored as value in this property. The value is mandatory only when the &#39;Source&#39; property has been set to &#39;File&#39;. | [optional] 
**hostname** | **str** | Hostname to be configured for the server in the OS. | [optional] 
**ip_config_type** | **str** | IP configuration type. Values are Static or Dynamic configuration of IP. In case of static IP configuration, IP address, gateway and other details need to be populated. In case of dynamic the IP configuration is obtained dynamically from DHCP. | [optional]  if omitted the server will use the default value of "static"
**ip_configuration** | [**OsIpConfiguration**](OsIpConfiguration.md) |  | [optional] 
**is_answer_file_set** | **bool** | Indicates whether the value of the &#39;answerFile&#39; property has been set. | [optional] [readonly] 
**is_root_password_crypted** | **bool** | Enable to indicate Root Password provided is encrypted. | [optional] 
**is_root_password_set** | **bool** | Indicates whether the value of the &#39;rootPassword&#39; property has been set. | [optional] [readonly] 
**nameserver** | **str** | IP address of the name server to be configured in the OS. | [optional] 
**product_key** | **str** | The product key to be used for a specific version of Windows installation. | [optional] 
**root_password** | **str** | Password configured for the root / administrator user in the OS. You can enter a plain text or an encrypted password. Intersight encrypts the plaintext password. Enable the Encrypted Password option to provide an encrypted password. For more details on encrypting passwords, see Help Center. | [optional] 
**source** | **str** | Answer values can be provided from three sources - Embedded in OS image, static file, or as placeholder values for an answer file template. Source of the answers is given as value, Embedded/File/Template. &#39;Embedded&#39; option indicates that the answer file is embedded within the OS Image. &#39;File&#39; option indicates that the answers are provided as a file. &#39;Template&#39; indicates that the placeholders in the selected os.ConfigurationFile MO are replaced with values provided as os.Answers MO. | [optional]  if omitted the server will use the default value of "None"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


