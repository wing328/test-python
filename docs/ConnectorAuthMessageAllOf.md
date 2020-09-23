# ConnectorAuthMessageAllOf

Definition of the list of properties defined in 'connector.AuthMessage', excluding properties defined in parent classes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_user_locale** | **str** | The platform locale to assign user. A locale defines one or more organizations (domains) the user is allowed access, and access is limited to the organizations specified in the locale. | [optional] 
**remote_user_name** | **str** | The user name passed to the platform for use in platform audit logs. | [optional] 
**remote_user_roles** | **str** | The list of roles to pass to the platform to validate the action against. | [optional] 
**remote_user_session_id** | **str** | The session Id passed to the platform for use in platforms auditing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


