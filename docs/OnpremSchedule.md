# OnpremSchedule

Schedule is used by Intersight Appliance services to store task scheduling information. For example, appliance backup service uses Schedule to store the backup schedule of the Intersight Appliance. The Upgrade service uses Schedule to store the user-defined schedule for software upgrades of the Intersight Appliance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_id** | **str** | The concrete type of this complex type. Its value must be the same as the &#39;objectType&#39; property. The OpenAPI document references this property as a discriminator value. | [readonly] 
**object_type** | **str** | The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types. | 
**day_of_month** | **int** | Schedule a task on a specific day of the month. Valid values are 1 through 31. If monthOfYear is specified, then dayOfMonth value must be valid for that month. DayOfMonth may not be set when dayOfWeek is specfied. | [optional] 
**day_of_week** | **int** | Schedule a task on a specific day of the week. Valid values are 1 through 7, with 1 being Sunday. DayOfWeek may not be specfied when dayOfMonth is specified. | [optional] 
**month_of_year** | **int** | Schedule a task on a specific month of the year. Valid values are 1 through 12, with 1 being January. | [optional] 
**repeat_interval** | **int** | Schedule a task to run periodically at an interval. Default unit of the RepeatInterval is in minutes. If the RepeateInterval value is set, then all other properties are ignored by the scheduler. RepeateInterval constraints are enforced by the services that use the schedule. Each service has pre-configured service specific properties for enforcing minimum and maximum values of the RepeatInterval. | [optional] 
**time_of_day** | **int** | Time of the day in seconds. TimeOfDay is required for all schedule configurations, except when the RepeateInterval field is specified. | [optional] 
**time_zone** | **str** | Timezone to use for the schedule calculation. If a timezone value is not speficied, then the schedule calculation will be based on UTC. | [optional]  if omitted the server will use the default value of "Pacific/Niue"
**week_of_month** | **int** | Schedule a task on a specific week of the month. Valid values are 1 through 5. Value of 5 means last week of the month. WeekOfMonth may not be set when dayOfMonth is specified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


