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

class BranchMigration(object):
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
        'id': 'str',
        'parent_id': 'str',
        'status': 'str',
        'title': 'str',
        'last_git_revision': 'str',
        'local_changes': 'bool',
        'created_at': 'datetime',
        'new_tables': 'dict(str, Table)',
        'removed_tables': 'list[str]',
        'table_migrations': 'dict(str, TableMigration)',
        'new_table_order': 'list[str]',
        'renamed_tables': 'list[TableRename]'
    }

    attribute_map = {
        'id': 'id',
        'parent_id': 'parentID',
        'status': 'status',
        'title': 'title',
        'last_git_revision': 'lastGitRevision',
        'local_changes': 'localChanges',
        'created_at': 'createdAt',
        'new_tables': 'newTables',
        'removed_tables': 'removedTables',
        'table_migrations': 'tableMigrations',
        'new_table_order': 'newTableOrder',
        'renamed_tables': 'renamedTables'
    }

    def __init__(self, id=None, parent_id=None, status=None, title=None, last_git_revision=None, local_changes=None, created_at=None, new_tables=None, removed_tables=None, table_migrations=None, new_table_order=None, renamed_tables=None):  # noqa: E501
        """BranchMigration - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._parent_id = None
        self._status = None
        self._title = None
        self._last_git_revision = None
        self._local_changes = None
        self._created_at = None
        self._new_tables = None
        self._removed_tables = None
        self._table_migrations = None
        self._new_table_order = None
        self._renamed_tables = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if parent_id is not None:
            self.parent_id = parent_id
        self.status = status
        if title is not None:
            self.title = title
        if last_git_revision is not None:
            self.last_git_revision = last_git_revision
        self.local_changes = local_changes
        if created_at is not None:
            self.created_at = created_at
        if new_tables is not None:
            self.new_tables = new_tables
        if removed_tables is not None:
            self.removed_tables = removed_tables
        if table_migrations is not None:
            self.table_migrations = table_migrations
        self.new_table_order = new_table_order
        if renamed_tables is not None:
            self.renamed_tables = renamed_tables

    @property
    def id(self):
        """Gets the id of this BranchMigration.  # noqa: E501


        :return: The id of this BranchMigration.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BranchMigration.


        :param id: The id of this BranchMigration.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this BranchMigration.  # noqa: E501


        :return: The parent_id of this BranchMigration.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BranchMigration.


        :param parent_id: The parent_id of this BranchMigration.  # noqa: E501
        :type: str
        """

        self._parent_id = parent_id

    @property
    def status(self):
        """Gets the status of this BranchMigration.  # noqa: E501


        :return: The status of this BranchMigration.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BranchMigration.


        :param status: The status of this BranchMigration.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def title(self):
        """Gets the title of this BranchMigration.  # noqa: E501


        :return: The title of this BranchMigration.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BranchMigration.


        :param title: The title of this BranchMigration.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def last_git_revision(self):
        """Gets the last_git_revision of this BranchMigration.  # noqa: E501


        :return: The last_git_revision of this BranchMigration.  # noqa: E501
        :rtype: str
        """
        return self._last_git_revision

    @last_git_revision.setter
    def last_git_revision(self, last_git_revision):
        """Sets the last_git_revision of this BranchMigration.


        :param last_git_revision: The last_git_revision of this BranchMigration.  # noqa: E501
        :type: str
        """

        self._last_git_revision = last_git_revision

    @property
    def local_changes(self):
        """Gets the local_changes of this BranchMigration.  # noqa: E501


        :return: The local_changes of this BranchMigration.  # noqa: E501
        :rtype: bool
        """
        return self._local_changes

    @local_changes.setter
    def local_changes(self, local_changes):
        """Sets the local_changes of this BranchMigration.


        :param local_changes: The local_changes of this BranchMigration.  # noqa: E501
        :type: bool
        """
        if local_changes is None:
            raise ValueError("Invalid value for `local_changes`, must not be `None`")  # noqa: E501

        self._local_changes = local_changes

    @property
    def created_at(self):
        """Gets the created_at of this BranchMigration.  # noqa: E501


        :return: The created_at of this BranchMigration.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BranchMigration.


        :param created_at: The created_at of this BranchMigration.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def new_tables(self):
        """Gets the new_tables of this BranchMigration.  # noqa: E501


        :return: The new_tables of this BranchMigration.  # noqa: E501
        :rtype: dict(str, Table)
        """
        return self._new_tables

    @new_tables.setter
    def new_tables(self, new_tables):
        """Sets the new_tables of this BranchMigration.


        :param new_tables: The new_tables of this BranchMigration.  # noqa: E501
        :type: dict(str, Table)
        """

        self._new_tables = new_tables

    @property
    def removed_tables(self):
        """Gets the removed_tables of this BranchMigration.  # noqa: E501


        :return: The removed_tables of this BranchMigration.  # noqa: E501
        :rtype: list[str]
        """
        return self._removed_tables

    @removed_tables.setter
    def removed_tables(self, removed_tables):
        """Sets the removed_tables of this BranchMigration.


        :param removed_tables: The removed_tables of this BranchMigration.  # noqa: E501
        :type: list[str]
        """

        self._removed_tables = removed_tables

    @property
    def table_migrations(self):
        """Gets the table_migrations of this BranchMigration.  # noqa: E501


        :return: The table_migrations of this BranchMigration.  # noqa: E501
        :rtype: dict(str, TableMigration)
        """
        return self._table_migrations

    @table_migrations.setter
    def table_migrations(self, table_migrations):
        """Sets the table_migrations of this BranchMigration.


        :param table_migrations: The table_migrations of this BranchMigration.  # noqa: E501
        :type: dict(str, TableMigration)
        """

        self._table_migrations = table_migrations

    @property
    def new_table_order(self):
        """Gets the new_table_order of this BranchMigration.  # noqa: E501


        :return: The new_table_order of this BranchMigration.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_table_order

    @new_table_order.setter
    def new_table_order(self, new_table_order):
        """Sets the new_table_order of this BranchMigration.


        :param new_table_order: The new_table_order of this BranchMigration.  # noqa: E501
        :type: list[str]
        """
        if new_table_order is None:
            raise ValueError("Invalid value for `new_table_order`, must not be `None`")  # noqa: E501

        self._new_table_order = new_table_order

    @property
    def renamed_tables(self):
        """Gets the renamed_tables of this BranchMigration.  # noqa: E501


        :return: The renamed_tables of this BranchMigration.  # noqa: E501
        :rtype: list[TableRename]
        """
        return self._renamed_tables

    @renamed_tables.setter
    def renamed_tables(self, renamed_tables):
        """Sets the renamed_tables of this BranchMigration.


        :param renamed_tables: The renamed_tables of this BranchMigration.  # noqa: E501
        :type: list[TableRename]
        """

        self._renamed_tables = renamed_tables

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
        if issubclass(BranchMigration, dict):
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
        if not isinstance(other, BranchMigration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
