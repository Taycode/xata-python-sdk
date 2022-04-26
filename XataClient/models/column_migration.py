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

class ColumnMigration(object):
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
        'old': 'Column',
        'new': 'Column'
    }

    attribute_map = {
        'old': 'old',
        'new': 'new'
    }

    def __init__(self, old=None, new=None):  # noqa: E501
        """ColumnMigration - a model defined in Swagger"""  # noqa: E501
        self._old = None
        self._new = None
        self.discriminator = None
        self.old = old
        self.new = new

    @property
    def old(self):
        """Gets the old of this ColumnMigration.  # noqa: E501


        :return: The old of this ColumnMigration.  # noqa: E501
        :rtype: Column
        """
        return self._old

    @old.setter
    def old(self, old):
        """Sets the old of this ColumnMigration.


        :param old: The old of this ColumnMigration.  # noqa: E501
        :type: Column
        """
        if old is None:
            raise ValueError("Invalid value for `old`, must not be `None`")  # noqa: E501

        self._old = old

    @property
    def new(self):
        """Gets the new of this ColumnMigration.  # noqa: E501


        :return: The new of this ColumnMigration.  # noqa: E501
        :rtype: Column
        """
        return self._new

    @new.setter
    def new(self, new):
        """Sets the new of this ColumnMigration.


        :param new: The new of this ColumnMigration.  # noqa: E501
        :type: Column
        """
        if new is None:
            raise ValueError("Invalid value for `new`, must not be `None`")  # noqa: E501

        self._new = new

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
        if issubclass(ColumnMigration, dict):
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
        if not isinstance(other, ColumnMigration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other