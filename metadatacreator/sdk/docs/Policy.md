# Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager** | **list[str]** | Defines the emails of users that can modify the policy parameters | [optional] 
**tapeRedundancy** | **str** | Defines the level of redundancy in storage to minimize loss of data. Allowed values are low, medium, high. Low could e.g. mean one tape copy only, medium could mean two tape copies and high two geo-redundant tape copies | [optional] [default to 'low']
**autoArchive** | **bool** | automatically archive dataset | [optional] 
**autoArchiveDelay** | **float** | Number of days after dataset creation that (remaining) datasets are archived automatically | [optional] [default to 7.0]
**archiveEmailNotification** | **bool** | Flag is true when an email notification should be sent to archiveEmailsToBeNotified upon an archive job creation | [optional] [default to False]
**archiveEmailsToBeNotified** | **list[str]** | Array of additional email addresses that should be notified up an archive job creation | [optional] 
**retrieveEmailNotification** | **bool** | Flag is true when an email notification should be sent to retrieveEmailsToBeNotified upon a retrieval job creation | [optional] [default to False]
**retrieveEmailsToBeNotified** | **list[str]** | Array of additional email addresses that should be notified up a retrieval job creation | [optional] 
**ownerGroup** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**accessGroups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | [optional] 
**createdBy** | **str** | Functional or user account name who created this instance | [optional] 
**updatedBy** | **str** | Functional or user account name who last updated this instance | [optional] 
**id** | [**ObjectID**](ObjectID.md) |  | [optional] 
**createdAt** | **datetime** |  | [optional] 
**updatedAt** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


