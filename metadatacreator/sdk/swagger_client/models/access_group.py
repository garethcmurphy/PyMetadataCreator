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


class AccessGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, sAMAccountName=None, description=None, member=None, memberOf=None):
        """
        AccessGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sAMAccountName': 'str',
            'description': 'str',
            'member': 'list[str]',
            'memberOf': 'list[str]'
        }

        self.attribute_map = {
            'sAMAccountName': 'sAMAccountName',
            'description': 'description',
            'member': 'member',
            'memberOf': 'memberOf'
        }

        self._sAMAccountName = sAMAccountName
        self._description = description
        self._member = member
        self._memberOf = memberOf

    @property
    def sAMAccountName(self):
        """
        Gets the sAMAccountName of this AccessGroup.

        :return: The sAMAccountName of this AccessGroup.
        :rtype: str
        """
        return self._sAMAccountName

    @sAMAccountName.setter
    def sAMAccountName(self, sAMAccountName):
        """
        Sets the sAMAccountName of this AccessGroup.

        :param sAMAccountName: The sAMAccountName of this AccessGroup.
        :type: str
        """
        if sAMAccountName is None:
            raise ValueError("Invalid value for `sAMAccountName`, must not be `None`")

        self._sAMAccountName = sAMAccountName

    @property
    def description(self):
        """
        Gets the description of this AccessGroup.

        :return: The description of this AccessGroup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AccessGroup.

        :param description: The description of this AccessGroup.
        :type: str
        """

        self._description = description

    @property
    def member(self):
        """
        Gets the member of this AccessGroup.

        :return: The member of this AccessGroup.
        :rtype: list[str]
        """
        return self._member

    @member.setter
    def member(self, member):
        """
        Sets the member of this AccessGroup.

        :param member: The member of this AccessGroup.
        :type: list[str]
        """

        self._member = member

    @property
    def memberOf(self):
        """
        Gets the memberOf of this AccessGroup.

        :return: The memberOf of this AccessGroup.
        :rtype: list[str]
        """
        return self._memberOf

    @memberOf.setter
    def memberOf(self, memberOf):
        """
        Sets the memberOf of this AccessGroup.

        :param memberOf: The memberOf of this AccessGroup.
        :type: list[str]
        """

        self._memberOf = memberOf

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
        if not isinstance(other, AccessGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
