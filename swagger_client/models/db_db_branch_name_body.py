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

class DbDbBranchNameBody(object):
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
        '_from': 'str',
        'metadata': 'BranchMetadata'
    }

    attribute_map = {
        '_from': 'from',
        'metadata': 'metadata'
    }

    def __init__(self, _from=None, metadata=None):  # noqa: E501
        """DbDbBranchNameBody - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._metadata = None
        self.discriminator = None
        if _from is not None:
            self._from = _from
        if metadata is not None:
            self.metadata = metadata

    @property
    def _from(self):
        """Gets the _from of this DbDbBranchNameBody.  # noqa: E501

        Select the branch to fork from. Defaults to 'main'  # noqa: E501

        :return: The _from of this DbDbBranchNameBody.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this DbDbBranchNameBody.

        Select the branch to fork from. Defaults to 'main'  # noqa: E501

        :param _from: The _from of this DbDbBranchNameBody.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def metadata(self):
        """Gets the metadata of this DbDbBranchNameBody.  # noqa: E501


        :return: The metadata of this DbDbBranchNameBody.  # noqa: E501
        :rtype: BranchMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DbDbBranchNameBody.


        :param metadata: The metadata of this DbDbBranchNameBody.  # noqa: E501
        :type: BranchMetadata
        """

        self._metadata = metadata

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
        if issubclass(DbDbBranchNameBody, dict):
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
        if not isinstance(other, DbDbBranchNameBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
