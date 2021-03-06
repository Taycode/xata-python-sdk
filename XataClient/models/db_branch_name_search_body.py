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

class DbBranchNameSearchBody(object):
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
        'tables': 'list[str]',
        'query': 'str',
        'fuzziness': 'int'
    }

    attribute_map = {
        'tables': 'tables',
        'query': 'query',
        'fuzziness': 'fuzziness'
    }

    def __init__(self, tables=None, query=None, fuzziness=1):  # noqa: E501
        """DbBranchNameSearchBody - a model defined in Swagger"""  # noqa: E501
        self._tables = None
        self._query = None
        self._fuzziness = None
        self.discriminator = None
        if tables is not None:
            self.tables = tables
        self.query = query
        if fuzziness is not None:
            self.fuzziness = fuzziness

    @property
    def tables(self):
        """Gets the tables of this DbBranchNameSearchBody.  # noqa: E501

        An array with the tables in which to search. By default, all tables are included.  # noqa: E501

        :return: The tables of this DbBranchNameSearchBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """Sets the tables of this DbBranchNameSearchBody.

        An array with the tables in which to search. By default, all tables are included.  # noqa: E501

        :param tables: The tables of this DbBranchNameSearchBody.  # noqa: E501
        :type: list[str]
        """

        self._tables = tables

    @property
    def query(self):
        """Gets the query of this DbBranchNameSearchBody.  # noqa: E501

        The query string.  # noqa: E501

        :return: The query of this DbBranchNameSearchBody.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this DbBranchNameSearchBody.

        The query string.  # noqa: E501

        :param query: The query of this DbBranchNameSearchBody.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def fuzziness(self):
        """Gets the fuzziness of this DbBranchNameSearchBody.  # noqa: E501

        Maximum [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) for the search terms. The Levenshtein distance is the number of one charcter changes needed to make two strings equal. The default is 1, meaning that single character typos per word are tollerated by search. You can set it to 0 to remove the typo tollerance or set it to 2  to allow two typos in a word.   # noqa: E501

        :return: The fuzziness of this DbBranchNameSearchBody.  # noqa: E501
        :rtype: int
        """
        return self._fuzziness

    @fuzziness.setter
    def fuzziness(self, fuzziness):
        """Sets the fuzziness of this DbBranchNameSearchBody.

        Maximum [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) for the search terms. The Levenshtein distance is the number of one charcter changes needed to make two strings equal. The default is 1, meaning that single character typos per word are tollerated by search. You can set it to 0 to remove the typo tollerance or set it to 2  to allow two typos in a word.   # noqa: E501

        :param fuzziness: The fuzziness of this DbBranchNameSearchBody.  # noqa: E501
        :type: int
        """

        self._fuzziness = fuzziness

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
        if issubclass(DbBranchNameSearchBody, dict):
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
        if not isinstance(other, DbBranchNameSearchBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
