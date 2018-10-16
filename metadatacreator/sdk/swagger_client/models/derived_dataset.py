# coding: utf-8

"""
    dacat-api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DerivedDataset(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, investigator=None, inputDatasets=None, usedSoftware=None, jobParameters=None, jobLogData=None, pid=None, owner=None, ownerEmail=None, orcidOfOwner=None, contactEmail=None, sourceFolder=None, size=None, packedSize=None, creationTime=None, type=None, validationStatus=None, keywords=None, description=None, userTargetLocation=None, classification=None, license=None, version=None, doi=None, isPublished=None, ownerGroup=None, accessGroups=None, createdBy=None, updatedBy=None, createdAt=None, updatedAt=None):
        """
        DerivedDataset - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'investigator': 'str',
            'inputDatasets': 'list[str]',
            'usedSoftware': 'list[str]',
            'jobParameters': 'object',
            'jobLogData': 'str',
            'pid': 'str',
            'owner': 'str',
            'ownerEmail': 'str',
            'orcidOfOwner': 'str',
            'contactEmail': 'str',
            'sourceFolder': 'str',
            'size': 'float',
            'packedSize': 'float',
            'creationTime': 'datetime',
            'type': 'str',
            'validationStatus': 'str',
            'keywords': 'list[str]',
            'description': 'str',
            'userTargetLocation': 'str',
            'classification': 'str',
            'license': 'str',
            'version': 'str',
            'doi': 'str',
            'isPublished': 'bool',
            'ownerGroup': 'str',
            'accessGroups': 'list[str]',
            'createdBy': 'str',
            'updatedBy': 'str',
            'createdAt': 'datetime',
            'updatedAt': 'datetime'
        }

        self.attribute_map = {
            'investigator': 'investigator',
            'inputDatasets': 'inputDatasets',
            'usedSoftware': 'usedSoftware',
            'jobParameters': 'jobParameters',
            'jobLogData': 'jobLogData',
            'pid': 'pid',
            'owner': 'owner',
            'ownerEmail': 'ownerEmail',
            'orcidOfOwner': 'orcidOfOwner',
            'contactEmail': 'contactEmail',
            'sourceFolder': 'sourceFolder',
            'size': 'size',
            'packedSize': 'packedSize',
            'creationTime': 'creationTime',
            'type': 'type',
            'validationStatus': 'validationStatus',
            'keywords': 'keywords',
            'description': 'description',
            'userTargetLocation': 'userTargetLocation',
            'classification': 'classification',
            'license': 'license',
            'version': 'version',
            'doi': 'doi',
            'isPublished': 'isPublished',
            'ownerGroup': 'ownerGroup',
            'accessGroups': 'accessGroups',
            'createdBy': 'createdBy',
            'updatedBy': 'updatedBy',
            'createdAt': 'createdAt',
            'updatedAt': 'updatedAt'
        }

        self._investigator = investigator
        self._inputDatasets = inputDatasets
        self._usedSoftware = usedSoftware
        self._jobParameters = jobParameters
        self._jobLogData = jobLogData
        self._pid = pid
        self._owner = owner
        self._ownerEmail = ownerEmail
        self._orcidOfOwner = orcidOfOwner
        self._contactEmail = contactEmail
        self._sourceFolder = sourceFolder
        self._size = size
        self._packedSize = packedSize
        self._creationTime = creationTime
        self._type = type
        self._validationStatus = validationStatus
        self._keywords = keywords
        self._description = description
        self._userTargetLocation = userTargetLocation
        self._classification = classification
        self._license = license
        self._version = version
        self._doi = doi
        self._isPublished = isPublished
        self._ownerGroup = ownerGroup
        self._accessGroups = accessGroups
        self._createdBy = createdBy
        self._updatedBy = updatedBy
        self._createdAt = createdAt
        self._updatedAt = updatedAt

    @property
    def investigator(self):
        """
        Gets the investigator of this DerivedDataset.
        Email of person pursuing the data analysis

        :return: The investigator of this DerivedDataset.
        :rtype: str
        """
        return self._investigator

    @investigator.setter
    def investigator(self, investigator):
        """
        Sets the investigator of this DerivedDataset.
        Email of person pursuing the data analysis

        :param investigator: The investigator of this DerivedDataset.
        :type: str
        """
        if investigator is None:
            raise ValueError("Invalid value for `investigator`, must not be `None`")

        self._investigator = investigator

    @property
    def inputDatasets(self):
        """
        Gets the inputDatasets of this DerivedDataset.
        Array of input dataset identifiers used in producing the derived dataset. Ideally these are the global identifier to existing datasets inside this or federated data catalogs

        :return: The inputDatasets of this DerivedDataset.
        :rtype: list[str]
        """
        return self._inputDatasets

    @inputDatasets.setter
    def inputDatasets(self, inputDatasets):
        """
        Sets the inputDatasets of this DerivedDataset.
        Array of input dataset identifiers used in producing the derived dataset. Ideally these are the global identifier to existing datasets inside this or federated data catalogs

        :param inputDatasets: The inputDatasets of this DerivedDataset.
        :type: list[str]
        """
        if inputDatasets is None:
            raise ValueError("Invalid value for `inputDatasets`, must not be `None`")

        self._inputDatasets = inputDatasets

    @property
    def usedSoftware(self):
        """
        Gets the usedSoftware of this DerivedDataset.
        A list of links to software repositories which uniquely identifies the software used and the version for yielding the derived data

        :return: The usedSoftware of this DerivedDataset.
        :rtype: list[str]
        """
        return self._usedSoftware

    @usedSoftware.setter
    def usedSoftware(self, usedSoftware):
        """
        Sets the usedSoftware of this DerivedDataset.
        A list of links to software repositories which uniquely identifies the software used and the version for yielding the derived data

        :param usedSoftware: The usedSoftware of this DerivedDataset.
        :type: list[str]
        """
        if usedSoftware is None:
            raise ValueError("Invalid value for `usedSoftware`, must not be `None`")

        self._usedSoftware = usedSoftware

    @property
    def jobParameters(self):
        """
        Gets the jobParameters of this DerivedDataset.
        The creation process of the drived data will usually depend on input job parameters. The full structure of these input parameters are stored here

        :return: The jobParameters of this DerivedDataset.
        :rtype: object
        """
        return self._jobParameters

    @jobParameters.setter
    def jobParameters(self, jobParameters):
        """
        Sets the jobParameters of this DerivedDataset.
        The creation process of the drived data will usually depend on input job parameters. The full structure of these input parameters are stored here

        :param jobParameters: The jobParameters of this DerivedDataset.
        :type: object
        """

        self._jobParameters = jobParameters

    @property
    def jobLogData(self):
        """
        Gets the jobLogData of this DerivedDataset.
        The output job logfile. Keep the size of this log data well below 15 MB 

        :return: The jobLogData of this DerivedDataset.
        :rtype: str
        """
        return self._jobLogData

    @jobLogData.setter
    def jobLogData(self, jobLogData):
        """
        Sets the jobLogData of this DerivedDataset.
        The output job logfile. Keep the size of this log data well below 15 MB 

        :param jobLogData: The jobLogData of this DerivedDataset.
        :type: str
        """

        self._jobLogData = jobLogData

    @property
    def pid(self):
        """
        Gets the pid of this DerivedDataset.
        Persistent Identifier for datasets derived from UUIDv4 and prepended automatically by site specific PID prefix like 20.500.12345/

        :return: The pid of this DerivedDataset.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this DerivedDataset.
        Persistent Identifier for datasets derived from UUIDv4 and prepended automatically by site specific PID prefix like 20.500.12345/

        :param pid: The pid of this DerivedDataset.
        :type: str
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")

        self._pid = pid

    @property
    def owner(self):
        """
        Gets the owner of this DerivedDataset.
        Owner of the data set, usually first name + lastname

        :return: The owner of this DerivedDataset.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this DerivedDataset.
        Owner of the data set, usually first name + lastname

        :param owner: The owner of this DerivedDataset.
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner

    @property
    def ownerEmail(self):
        """
        Gets the ownerEmail of this DerivedDataset.
        Email of owner of the data set

        :return: The ownerEmail of this DerivedDataset.
        :rtype: str
        """
        return self._ownerEmail

    @ownerEmail.setter
    def ownerEmail(self, ownerEmail):
        """
        Sets the ownerEmail of this DerivedDataset.
        Email of owner of the data set

        :param ownerEmail: The ownerEmail of this DerivedDataset.
        :type: str
        """

        self._ownerEmail = ownerEmail

    @property
    def orcidOfOwner(self):
        """
        Gets the orcidOfOwner of this DerivedDataset.
        ORCID of owner https://orcid.org if available

        :return: The orcidOfOwner of this DerivedDataset.
        :rtype: str
        """
        return self._orcidOfOwner

    @orcidOfOwner.setter
    def orcidOfOwner(self, orcidOfOwner):
        """
        Sets the orcidOfOwner of this DerivedDataset.
        ORCID of owner https://orcid.org if available

        :param orcidOfOwner: The orcidOfOwner of this DerivedDataset.
        :type: str
        """

        self._orcidOfOwner = orcidOfOwner

    @property
    def contactEmail(self):
        """
        Gets the contactEmail of this DerivedDataset.
        Email of contact person for this dataset

        :return: The contactEmail of this DerivedDataset.
        :rtype: str
        """
        return self._contactEmail

    @contactEmail.setter
    def contactEmail(self, contactEmail):
        """
        Sets the contactEmail of this DerivedDataset.
        Email of contact person for this dataset

        :param contactEmail: The contactEmail of this DerivedDataset.
        :type: str
        """
        if contactEmail is None:
            raise ValueError("Invalid value for `contactEmail`, must not be `None`")

        self._contactEmail = contactEmail

    @property
    def sourceFolder(self):
        """
        Gets the sourceFolder of this DerivedDataset.
        Absolute file path on file server containing the files of this dataset, optionally including protocol and file server hostname, e.g. nfs://fileserver1.example.com/some/path/to/sourcefolder. In case of a single file dataset, e.g. HDF5 data it contains the path up to, but excluding the filename.

        :return: The sourceFolder of this DerivedDataset.
        :rtype: str
        """
        return self._sourceFolder

    @sourceFolder.setter
    def sourceFolder(self, sourceFolder):
        """
        Sets the sourceFolder of this DerivedDataset.
        Absolute file path on file server containing the files of this dataset, optionally including protocol and file server hostname, e.g. nfs://fileserver1.example.com/some/path/to/sourcefolder. In case of a single file dataset, e.g. HDF5 data it contains the path up to, but excluding the filename.

        :param sourceFolder: The sourceFolder of this DerivedDataset.
        :type: str
        """
        if sourceFolder is None:
            raise ValueError("Invalid value for `sourceFolder`, must not be `None`")

        self._sourceFolder = sourceFolder

    @property
    def size(self):
        """
        Gets the size of this DerivedDataset.
        Total size of all source files contained in source folder on disk when unpacked

        :return: The size of this DerivedDataset.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this DerivedDataset.
        Total size of all source files contained in source folder on disk when unpacked

        :param size: The size of this DerivedDataset.
        :type: float
        """

        self._size = size

    @property
    def packedSize(self):
        """
        Gets the packedSize of this DerivedDataset.
        Total size of all datablock package files created for this dataset

        :return: The packedSize of this DerivedDataset.
        :rtype: float
        """
        return self._packedSize

    @packedSize.setter
    def packedSize(self, packedSize):
        """
        Sets the packedSize of this DerivedDataset.
        Total size of all datablock package files created for this dataset

        :param packedSize: The packedSize of this DerivedDataset.
        :type: float
        """

        self._packedSize = packedSize

    @property
    def creationTime(self):
        """
        Gets the creationTime of this DerivedDataset.
        Time when dataset became fully available on disk, i.e. all containing files have been written. Format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server.

        :return: The creationTime of this DerivedDataset.
        :rtype: datetime
        """
        return self._creationTime

    @creationTime.setter
    def creationTime(self, creationTime):
        """
        Sets the creationTime of this DerivedDataset.
        Time when dataset became fully available on disk, i.e. all containing files have been written. Format according to chapter 5.6 internet date/time format in RFC 3339. Local times without timezone/offset info are automatically transformed to UTC using the timezone of the API server.

        :param creationTime: The creationTime of this DerivedDataset.
        :type: datetime
        """
        if creationTime is None:
            raise ValueError("Invalid value for `creationTime`, must not be `None`")

        self._creationTime = creationTime

    @property
    def type(self):
        """
        Gets the type of this DerivedDataset.
        Characterize type of dataset, either 'base' or 'raw' or 'derived'. Autofilled

        :return: The type of this DerivedDataset.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DerivedDataset.
        Characterize type of dataset, either 'base' or 'raw' or 'derived'. Autofilled

        :param type: The type of this DerivedDataset.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def validationStatus(self):
        """
        Gets the validationStatus of this DerivedDataset.
        Defines a level of trust, e.g. a measure of how much data was verified or used by other persons

        :return: The validationStatus of this DerivedDataset.
        :rtype: str
        """
        return self._validationStatus

    @validationStatus.setter
    def validationStatus(self, validationStatus):
        """
        Sets the validationStatus of this DerivedDataset.
        Defines a level of trust, e.g. a measure of how much data was verified or used by other persons

        :param validationStatus: The validationStatus of this DerivedDataset.
        :type: str
        """

        self._validationStatus = validationStatus

    @property
    def keywords(self):
        """
        Gets the keywords of this DerivedDataset.
        Array of tags associated with the meaning or contents of this dataset. Values should ideally come from defined vocabularies, taxonomies, ontologies or knowledge graphs

        :return: The keywords of this DerivedDataset.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this DerivedDataset.
        Array of tags associated with the meaning or contents of this dataset. Values should ideally come from defined vocabularies, taxonomies, ontologies or knowledge graphs

        :param keywords: The keywords of this DerivedDataset.
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def description(self):
        """
        Gets the description of this DerivedDataset.
        Free text explanation of contents of dataset

        :return: The description of this DerivedDataset.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DerivedDataset.
        Free text explanation of contents of dataset

        :param description: The description of this DerivedDataset.
        :type: str
        """

        self._description = description

    @property
    def userTargetLocation(self):
        """
        Gets the userTargetLocation of this DerivedDataset.
        User choosable absolute virtual path where datasets are stored. Mainly used as a help for the enduser at dataset retrieval time to find the proper dataset. Will be prepended by p-group

        :return: The userTargetLocation of this DerivedDataset.
        :rtype: str
        """
        return self._userTargetLocation

    @userTargetLocation.setter
    def userTargetLocation(self, userTargetLocation):
        """
        Sets the userTargetLocation of this DerivedDataset.
        User choosable absolute virtual path where datasets are stored. Mainly used as a help for the enduser at dataset retrieval time to find the proper dataset. Will be prepended by p-group

        :param userTargetLocation: The userTargetLocation of this DerivedDataset.
        :type: str
        """

        self._userTargetLocation = userTargetLocation

    @property
    def classification(self):
        """
        Gets the classification of this DerivedDataset.
        ACIA information about AUthenticity,COnfidentiality,INtegrity and AVailability requirements of dataset. E.g. AV(ailabilty)=medium could trigger the creation of a two tape copies. Format 'AV=medium,CO=low'

        :return: The classification of this DerivedDataset.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """
        Sets the classification of this DerivedDataset.
        ACIA information about AUthenticity,COnfidentiality,INtegrity and AVailability requirements of dataset. E.g. AV(ailabilty)=medium could trigger the creation of a two tape copies. Format 'AV=medium,CO=low'

        :param classification: The classification of this DerivedDataset.
        :type: str
        """

        self._classification = classification

    @property
    def license(self):
        """
        Gets the license of this DerivedDataset.
        Name of license under which data can be used

        :return: The license of this DerivedDataset.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this DerivedDataset.
        Name of license under which data can be used

        :param license: The license of this DerivedDataset.
        :type: str
        """

        self._license = license

    @property
    def version(self):
        """
        Gets the version of this DerivedDataset.
        Version of API used in creation of dataset

        :return: The version of this DerivedDataset.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DerivedDataset.
        Version of API used in creation of dataset

        :param version: The version of this DerivedDataset.
        :type: str
        """

        self._version = version

    @property
    def doi(self):
        """
        Gets the doi of this DerivedDataset.
        Digital object Identifier like doi: used for publication purposes

        :return: The doi of this DerivedDataset.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """
        Sets the doi of this DerivedDataset.
        Digital object Identifier like doi: used for publication purposes

        :param doi: The doi of this DerivedDataset.
        :type: str
        """

        self._doi = doi

    @property
    def isPublished(self):
        """
        Gets the isPublished of this DerivedDataset.
        Flag is true when data are made publically available

        :return: The isPublished of this DerivedDataset.
        :rtype: bool
        """
        return self._isPublished

    @isPublished.setter
    def isPublished(self, isPublished):
        """
        Sets the isPublished of this DerivedDataset.
        Flag is true when data are made publically available

        :param isPublished: The isPublished of this DerivedDataset.
        :type: bool
        """

        self._isPublished = isPublished

    @property
    def ownerGroup(self):
        """
        Gets the ownerGroup of this DerivedDataset.
        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151

        :return: The ownerGroup of this DerivedDataset.
        :rtype: str
        """
        return self._ownerGroup

    @ownerGroup.setter
    def ownerGroup(self, ownerGroup):
        """
        Sets the ownerGroup of this DerivedDataset.
        Defines the group which owns the data, and therefore has unrestricted access to this data. Usually a pgroup like p12151

        :param ownerGroup: The ownerGroup of this DerivedDataset.
        :type: str
        """
        if ownerGroup is None:
            raise ValueError("Invalid value for `ownerGroup`, must not be `None`")

        self._ownerGroup = ownerGroup

    @property
    def accessGroups(self):
        """
        Gets the accessGroups of this DerivedDataset.
        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users

        :return: The accessGroups of this DerivedDataset.
        :rtype: list[str]
        """
        return self._accessGroups

    @accessGroups.setter
    def accessGroups(self, accessGroups):
        """
        Sets the accessGroups of this DerivedDataset.
        Optional additional groups which have read access to the data. Users which are member in one of the groups listed here are allowed to access this data. The special group 'public' makes data available to all users

        :param accessGroups: The accessGroups of this DerivedDataset.
        :type: list[str]
        """

        self._accessGroups = accessGroups

    @property
    def createdBy(self):
        """
        Gets the createdBy of this DerivedDataset.
        Functional or user account name who created this instance

        :return: The createdBy of this DerivedDataset.
        :rtype: str
        """
        return self._createdBy

    @createdBy.setter
    def createdBy(self, createdBy):
        """
        Sets the createdBy of this DerivedDataset.
        Functional or user account name who created this instance

        :param createdBy: The createdBy of this DerivedDataset.
        :type: str
        """

        self._createdBy = createdBy

    @property
    def updatedBy(self):
        """
        Gets the updatedBy of this DerivedDataset.
        Functional or user account name who last updated this instance

        :return: The updatedBy of this DerivedDataset.
        :rtype: str
        """
        return self._updatedBy

    @updatedBy.setter
    def updatedBy(self, updatedBy):
        """
        Sets the updatedBy of this DerivedDataset.
        Functional or user account name who last updated this instance

        :param updatedBy: The updatedBy of this DerivedDataset.
        :type: str
        """

        self._updatedBy = updatedBy

    @property
    def createdAt(self):
        """
        Gets the createdAt of this DerivedDataset.

        :return: The createdAt of this DerivedDataset.
        :rtype: datetime
        """
        return self._createdAt

    @createdAt.setter
    def createdAt(self, createdAt):
        """
        Sets the createdAt of this DerivedDataset.

        :param createdAt: The createdAt of this DerivedDataset.
        :type: datetime
        """

        self._createdAt = createdAt

    @property
    def updatedAt(self):
        """
        Gets the updatedAt of this DerivedDataset.

        :return: The updatedAt of this DerivedDataset.
        :rtype: datetime
        """
        return self._updatedAt

    @updatedAt.setter
    def updatedAt(self, updatedAt):
        """
        Sets the updatedAt of this DerivedDataset.

        :param updatedAt: The updatedAt of this DerivedDataset.
        :type: datetime
        """

        self._updatedAt = updatedAt

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DerivedDataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
