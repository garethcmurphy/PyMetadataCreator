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


class AccessToken(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, ttl=1209600.0, scopes=None, created=None, userId=None):
        """
        AccessToken - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'ttl': 'float',
            'scopes': 'list[str]',
            'created': 'datetime',
            'userId': 'ObjectID'
        }

        self.attribute_map = {
            'id': 'id',
            'ttl': 'ttl',
            'scopes': 'scopes',
            'created': 'created',
            'userId': 'userId'
        }

        self._id = id
        self._ttl = ttl
        self._scopes = scopes
        self._created = created
        self._userId = userId

    @property
    def id(self):
        """
        Gets the id of this AccessToken.

        :return: The id of this AccessToken.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccessToken.

        :param id: The id of this AccessToken.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def ttl(self):
        """
        Gets the ttl of this AccessToken.
        time to live in seconds (2 weeks by default)

        :return: The ttl of this AccessToken.
        :rtype: float
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this AccessToken.
        time to live in seconds (2 weeks by default)

        :param ttl: The ttl of this AccessToken.
        :type: float
        """

        self._ttl = ttl

    @property
    def scopes(self):
        """
        Gets the scopes of this AccessToken.
        Array of scopes granted to this access token.

        :return: The scopes of this AccessToken.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this AccessToken.
        Array of scopes granted to this access token.

        :param scopes: The scopes of this AccessToken.
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def created(self):
        """
        Gets the created of this AccessToken.

        :return: The created of this AccessToken.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this AccessToken.

        :param created: The created of this AccessToken.
        :type: datetime
        """

        self._created = created

    @property
    def userId(self):
        """
        Gets the userId of this AccessToken.

        :return: The userId of this AccessToken.
        :rtype: ObjectID
        """
        return self._userId

    @userId.setter
    def userId(self, userId):
        """
        Sets the userId of this AccessToken.

        :param userId: The userId of this AccessToken.
        :type: ObjectID
        """

        self._userId = userId

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
        if not isinstance(other, AccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
