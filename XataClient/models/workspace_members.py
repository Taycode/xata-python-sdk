# coding: utf-8

"""
    xata

    xata.io API  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WorkspaceMembers(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'members': 'list[WorkspaceMember]',
        'invites': 'list[WorkspaceInvite]'
    }

    attribute_map = {
        'members': 'members',
        'invites': 'invites'
    }

    def __init__(self, members=None, invites=None):  # noqa: E501
        """WorkspaceMembers - a model defined in Swagger"""  # noqa: E501
        self._members = None
        self._invites = None
        self.discriminator = None
        self.members = members
        self.invites = invites

    @property
    def members(self):
        """Gets the members of this WorkspaceMembers.  # noqa: E501


        :return: The members of this WorkspaceMembers.  # noqa: E501
        :rtype: list[WorkspaceMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this WorkspaceMembers.


        :param members: The members of this WorkspaceMembers.  # noqa: E501
        :type: list[WorkspaceMember]
        """
        if members is None:
            raise ValueError("Invalid value for `members`, must not be `None`")  # noqa: E501

        self._members = members

    @property
    def invites(self):
        """Gets the invites of this WorkspaceMembers.  # noqa: E501


        :return: The invites of this WorkspaceMembers.  # noqa: E501
        :rtype: list[WorkspaceInvite]
        """
        return self._invites

    @invites.setter
    def invites(self, invites):
        """Sets the invites of this WorkspaceMembers.


        :param invites: The invites of this WorkspaceMembers.  # noqa: E501
        :type: list[WorkspaceInvite]
        """
        if invites is None:
            raise ValueError("Invalid value for `invites`, must not be `None`")  # noqa: E501

        self._invites = invites

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(WorkspaceMembers, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkspaceMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
