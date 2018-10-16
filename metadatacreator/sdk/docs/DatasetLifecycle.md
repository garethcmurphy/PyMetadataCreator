# DatasetLifecycle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of status information. This must be the ID of the associated dataset | 
**archivable** | **bool** | Flag which is true, if dataset is available to be archived and no archive job for this dataset exists yet | [optional] 
**retrievable** | **bool** | Flag which is true, if dataset is stored on archive system and is ready to be retrieved | [optional] 
**dateOfDiskPurging** | **datetime** | Day when dataset will be removed from disk, assuming that is already stored on tape. | [optional] 
**archiveRetentionTime** | **datetime** | Day when the dataset&#39;s future fate will be evaluated again, e.g. to decide if the dataset can be deleted from archive. | [optional] 
**dateOfPublishing** | **datetime** | Day when dataset is supposed to become public according to data policy | [optional] 
**isOnCentralDisk** | **bool** | Flag which is true, if full dataset is available on central fileserver. If false data needs to be copied from decentral storage place to  a cache server before the ingest. This information needs to be transferred to the archive system at archive time | [optional] 
**isOnDisk** | **bool** | Flag which is true, if full dataset is available on disk. Warning: will be obsoleted in coming versions | [optional] 
**isOnTape** | **bool** | Flag which is true, if full dataset has been stored to tape. Warning: will be obsoleted in coming versions | [optional] 
**archiveStatusMessage** | **str** | Current status of Dataset with respect to storage on disk/tape. Warning: will be obsoleted in coming versions | [optional] 
**retrieveStatusMessage** | **str** | Latest message for this dataset concerning retrieve from archive system. Warning: will be obsoleted in coming versions | [optional] 
**lastUpdateMessage** | **str** | Latest status update / transition message for this dataset. Warning: will be obsoleted in coming versions | [optional] 
**archiveReturnMessage** | **str** | Detailed status or error message returned by archive system when treating this dataset. Warning: will be obsoleted in coming versions | [optional] 
**dateOfLastMessage** | **datetime** | Time when last status message was sent. Format according to chapter 5.6 internet date/time format in RFC 3339. This will be filled automatically if not provided. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server. Warning: will be obsoleted in coming versions | [optional] 
**isExported** | **bool** | Flag is true if data was exported to another location. Warning: will be obsoleted in coming versions | [optional] 
**exportedTo** | **str** | Location of the export destination. Warning: will be obsoleted in coming versions | [optional] 
**ownerGroup** | **str** | Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151 | 
**accessGroups** | **list[str]** | Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group &#39;public&#39; makes data available to all users | [optional] 
**createdBy** | **str** | Functional or user account name who created this instance | [optional] 
**updatedBy** | **str** | Functional or user account name who last updated this instance | [optional] 
**datasetId** | **str** |  | [optional] 
**rawDatasetId** | **str** |  | [optional] 
**derivedDatasetId** | **str** |  | [optional] 
**createdAt** | **datetime** |  | [optional] 
**updatedAt** | **datetime** |  | [optional] 
**MessageHistory** | [**list[Message]**](Message.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


