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

class StartedFromMetadata(object):
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
        'branch_name': 'BranchName',
        'db_branch_id': 'str',
        'migration_id': 'str'
    }

    attribute_map = {
        'branch_name': 'branchName',
        'db_branch_id': 'dbBranchID',
        'migration_id': 'migrationID'
    }

    def __init__(self, branch_name=None, db_branch_id=None, migration_id=None):  # noqa: E501
        """StartedFromMetadata - a model defined in Swagger"""  # noqa: E501
        self._branch_name = None
        self._db_branch_id = None
        self._migration_id = None
        self.discriminator = None
        self.branch_name = branch_name
        self.db_branch_id = db_branch_id
        self.migration_id = migration_id

    @property
    def branch_name(self):
        """Gets the branch_name of this StartedFromMetadata.  # noqa: E501


        :return: The branch_name of this StartedFromMetadata.  # noqa: E501
        :rtype: BranchName
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """Sets the branch_name of this StartedFromMetadata.


        :param branch_name: The branch_name of this StartedFromMetadata.  # noqa: E501
        :type: BranchName
        """
        if branch_name is None:
            raise ValueError("Invalid value for `branch_name`, must not be `None`")  # noqa: E501

        self._branch_name = branch_name

    @property
    def db_branch_id(self):
        """Gets the db_branch_id of this StartedFromMetadata.  # noqa: E501


        :return: The db_branch_id of this StartedFromMetadata.  # noqa: E501
        :rtype: str
        """
        return self._db_branch_id

    @db_branch_id.setter
    def db_branch_id(self, db_branch_id):
        """Sets the db_branch_id of this StartedFromMetadata.


        :param db_branch_id: The db_branch_id of this StartedFromMetadata.  # noqa: E501
        :type: str
        """
        if db_branch_id is None:
            raise ValueError("Invalid value for `db_branch_id`, must not be `None`")  # noqa: E501

        self._db_branch_id = db_branch_id

    @property
    def migration_id(self):
        """Gets the migration_id of this StartedFromMetadata.  # noqa: E501


        :return: The migration_id of this StartedFromMetadata.  # noqa: E501
        :rtype: str
        """
        return self._migration_id

    @migration_id.setter
    def migration_id(self, migration_id):
        """Sets the migration_id of this StartedFromMetadata.


        :param migration_id: The migration_id of this StartedFromMetadata.  # noqa: E501
        :type: str
        """
        if migration_id is None:
            raise ValueError("Invalid value for `migration_id`, must not be `None`")  # noqa: E501

        self._migration_id = migration_id

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
        if issubclass(StartedFromMetadata, dict):
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
        if not isinstance(other, StartedFromMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
