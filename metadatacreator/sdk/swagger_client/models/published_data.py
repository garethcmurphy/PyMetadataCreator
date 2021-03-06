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


class PublishedData(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, doi=None, affiliation=None, creator=None, publisher=None, publicationYear=None, title=None, url=None, abstract=None, dataDescription=None, thumbnail=None, resourceType=None, numberOfFiles=None, sizeOfArchive=None, pidArray=None, authors=None, doiRegisteredSuccessfullyTime=None):
        """
        PublishedData - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'doi': 'str',
            'affiliation': 'str',
            'creator': 'str',
            'publisher': 'str',
            'publicationYear': 'float',
            'title': 'str',
            'url': 'str',
            'abstract': 'str',
            'dataDescription': 'str',
            'thumbnail': 'str',
            'resourceType': 'str',
            'numberOfFiles': 'float',
            'sizeOfArchive': 'float',
            'pidArray': 'list[str]',
            'authors': 'list[str]',
            'doiRegisteredSuccessfullyTime': 'datetime'
        }

        self.attribute_map = {
            'doi': 'doi',
            'affiliation': 'affiliation',
            'creator': 'creator',
            'publisher': 'publisher',
            'publicationYear': 'publicationYear',
            'title': 'title',
            'url': 'url',
            'abstract': 'abstract',
            'dataDescription': 'dataDescription',
            'thumbnail': 'thumbnail',
            'resourceType': 'resourceType',
            'numberOfFiles': 'numberOfFiles',
            'sizeOfArchive': 'sizeOfArchive',
            'pidArray': 'pidArray',
            'authors': 'authors',
            'doiRegisteredSuccessfullyTime': 'doiRegisteredSuccessfullyTime'
        }

        self._doi = doi
        self._affiliation = affiliation
        self._creator = creator
        self._publisher = publisher
        self._publicationYear = publicationYear
        self._title = title
        self._url = url
        self._abstract = abstract
        self._dataDescription = dataDescription
        self._thumbnail = thumbnail
        self._resourceType = resourceType
        self._numberOfFiles = numberOfFiles
        self._sizeOfArchive = sizeOfArchive
        self._pidArray = pidArray
        self._authors = authors
        self._doiRegisteredSuccessfullyTime = doiRegisteredSuccessfullyTime

    @property
    def doi(self):
        """
        Gets the doi of this PublishedData.
        Digital Object Identifier

        :return: The doi of this PublishedData.
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """
        Sets the doi of this PublishedData.
        Digital Object Identifier

        :param doi: The doi of this PublishedData.
        :type: str
        """
        if doi is None:
            raise ValueError("Invalid value for `doi`, must not be `None`")

        self._doi = doi

    @property
    def affiliation(self):
        """
        Gets the affiliation of this PublishedData.
        Creator Affiliation

        :return: The affiliation of this PublishedData.
        :rtype: str
        """
        return self._affiliation

    @affiliation.setter
    def affiliation(self, affiliation):
        """
        Sets the affiliation of this PublishedData.
        Creator Affiliation

        :param affiliation: The affiliation of this PublishedData.
        :type: str
        """
        if affiliation is None:
            raise ValueError("Invalid value for `affiliation`, must not be `None`")

        self._affiliation = affiliation

    @property
    def creator(self):
        """
        Gets the creator of this PublishedData.
        Creator of dataset/dataset collection

        :return: The creator of this PublishedData.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this PublishedData.
        Creator of dataset/dataset collection

        :param creator: The creator of this PublishedData.
        :type: str
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")

        self._creator = creator

    @property
    def publisher(self):
        """
        Gets the publisher of this PublishedData.
        Dataset publisher

        :return: The publisher of this PublishedData.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher of this PublishedData.
        Dataset publisher

        :param publisher: The publisher of this PublishedData.
        :type: str
        """
        if publisher is None:
            raise ValueError("Invalid value for `publisher`, must not be `None`")

        self._publisher = publisher

    @property
    def publicationYear(self):
        """
        Gets the publicationYear of this PublishedData.
        Year of publication 

        :return: The publicationYear of this PublishedData.
        :rtype: float
        """
        return self._publicationYear

    @publicationYear.setter
    def publicationYear(self, publicationYear):
        """
        Sets the publicationYear of this PublishedData.
        Year of publication 

        :param publicationYear: The publicationYear of this PublishedData.
        :type: float
        """
        if publicationYear is None:
            raise ValueError("Invalid value for `publicationYear`, must not be `None`")

        self._publicationYear = publicationYear

    @property
    def title(self):
        """
        Gets the title of this PublishedData.
        Title

        :return: The title of this PublishedData.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this PublishedData.
        Title

        :param title: The title of this PublishedData.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def url(self):
        """
        Gets the url of this PublishedData.
        Full URL to the landing page for this DOI

        :return: The url of this PublishedData.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PublishedData.
        Full URL to the landing page for this DOI

        :param url: The url of this PublishedData.
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url

    @property
    def abstract(self):
        """
        Gets the abstract of this PublishedData.
        Abstract text for published datasets

        :return: The abstract of this PublishedData.
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """
        Sets the abstract of this PublishedData.
        Abstract text for published datasets

        :param abstract: The abstract of this PublishedData.
        :type: str
        """
        if abstract is None:
            raise ValueError("Invalid value for `abstract`, must not be `None`")

        self._abstract = abstract

    @property
    def dataDescription(self):
        """
        Gets the dataDescription of this PublishedData.
        Link to description of how to re-use data

        :return: The dataDescription of this PublishedData.
        :rtype: str
        """
        return self._dataDescription

    @dataDescription.setter
    def dataDescription(self, dataDescription):
        """
        Sets the dataDescription of this PublishedData.
        Link to description of how to re-use data

        :param dataDescription: The dataDescription of this PublishedData.
        :type: str
        """
        if dataDescription is None:
            raise ValueError("Invalid value for `dataDescription`, must not be `None`")

        self._dataDescription = dataDescription

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this PublishedData.
        Small, less than 16 MB base 64 image preview of dataset

        :return: The thumbnail of this PublishedData.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this PublishedData.
        Small, less than 16 MB base 64 image preview of dataset

        :param thumbnail: The thumbnail of this PublishedData.
        :type: str
        """
        if thumbnail is None:
            raise ValueError("Invalid value for `thumbnail`, must not be `None`")

        self._thumbnail = thumbnail

    @property
    def resourceType(self):
        """
        Gets the resourceType of this PublishedData.
        Type of files, format etc

        :return: The resourceType of this PublishedData.
        :rtype: str
        """
        return self._resourceType

    @resourceType.setter
    def resourceType(self, resourceType):
        """
        Sets the resourceType of this PublishedData.
        Type of files, format etc

        :param resourceType: The resourceType of this PublishedData.
        :type: str
        """
        if resourceType is None:
            raise ValueError("Invalid value for `resourceType`, must not be `None`")

        self._resourceType = resourceType

    @property
    def numberOfFiles(self):
        """
        Gets the numberOfFiles of this PublishedData.
        Number of files

        :return: The numberOfFiles of this PublishedData.
        :rtype: float
        """
        return self._numberOfFiles

    @numberOfFiles.setter
    def numberOfFiles(self, numberOfFiles):
        """
        Sets the numberOfFiles of this PublishedData.
        Number of files

        :param numberOfFiles: The numberOfFiles of this PublishedData.
        :type: float
        """
        if numberOfFiles is None:
            raise ValueError("Invalid value for `numberOfFiles`, must not be `None`")

        self._numberOfFiles = numberOfFiles

    @property
    def sizeOfArchive(self):
        """
        Gets the sizeOfArchive of this PublishedData.
        Size of archive

        :return: The sizeOfArchive of this PublishedData.
        :rtype: float
        """
        return self._sizeOfArchive

    @sizeOfArchive.setter
    def sizeOfArchive(self, sizeOfArchive):
        """
        Sets the sizeOfArchive of this PublishedData.
        Size of archive

        :param sizeOfArchive: The sizeOfArchive of this PublishedData.
        :type: float
        """
        if sizeOfArchive is None:
            raise ValueError("Invalid value for `sizeOfArchive`, must not be `None`")

        self._sizeOfArchive = sizeOfArchive

    @property
    def pidArray(self):
        """
        Gets the pidArray of this PublishedData.
        Array of one or more PIDS which make up the published data

        :return: The pidArray of this PublishedData.
        :rtype: list[str]
        """
        return self._pidArray

    @pidArray.setter
    def pidArray(self, pidArray):
        """
        Sets the pidArray of this PublishedData.
        Array of one or more PIDS which make up the published data

        :param pidArray: The pidArray of this PublishedData.
        :type: list[str]
        """
        if pidArray is None:
            raise ValueError("Invalid value for `pidArray`, must not be `None`")

        self._pidArray = pidArray

    @property
    def authors(self):
        """
        Gets the authors of this PublishedData.
        Array of one or more persons who are able to update this entry of published data

        :return: The authors of this PublishedData.
        :rtype: list[str]
        """
        return self._authors

    @authors.setter
    def authors(self, authors):
        """
        Sets the authors of this PublishedData.
        Array of one or more persons who are able to update this entry of published data

        :param authors: The authors of this PublishedData.
        :type: list[str]
        """
        if authors is None:
            raise ValueError("Invalid value for `authors`, must not be `None`")

        self._authors = authors

    @property
    def doiRegisteredSuccessfullyTime(self):
        """
        Gets the doiRegisteredSuccessfullyTime of this PublishedData.
        Time when doi is successfully registered

        :return: The doiRegisteredSuccessfullyTime of this PublishedData.
        :rtype: datetime
        """
        return self._doiRegisteredSuccessfullyTime

    @doiRegisteredSuccessfullyTime.setter
    def doiRegisteredSuccessfullyTime(self, doiRegisteredSuccessfullyTime):
        """
        Sets the doiRegisteredSuccessfullyTime of this PublishedData.
        Time when doi is successfully registered

        :param doiRegisteredSuccessfullyTime: The doiRegisteredSuccessfullyTime of this PublishedData.
        :type: datetime
        """

        self._doiRegisteredSuccessfullyTime = doiRegisteredSuccessfullyTime

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
        if not isinstance(other, PublishedData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
