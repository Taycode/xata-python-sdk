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

class FilterPredicateOp(object):
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
        'any': 'OneOfFilterPredicateOpAny',
        'all': 'OneOfFilterPredicateOpAll',
        '_none': 'OneOfFilterPredicateOpNone',
        '_not': 'OneOfFilterPredicateOpNot',
        '_is': 'OneOfFilterPredicateOpIs',
        'is_not': 'OneOfFilterPredicateOpIsNot',
        'lt': 'FilterRangeValue',
        'le': 'FilterRangeValue',
        'gt': 'FilterRangeValue',
        'ge': 'FilterRangeValue',
        'contains': 'str',
        'starts_with': 'str',
        'ends_with': 'str',
        'pattern': 'str'
    }

    attribute_map = {
        'any': '$any',
        'all': '$all',
        '_none': '$none',
        '_not': '$not',
        '_is': '$is',
        'is_not': '$isNot',
        'lt': '$lt',
        'le': '$le',
        'gt': '$gt',
        'ge': '$ge',
        'contains': '$contains',
        'starts_with': '$startsWith',
        'ends_with': '$endsWith',
        'pattern': '$pattern'
    }

    def __init__(self, any=None, all=None, _none=None, _not=None, _is=None, is_not=None, lt=None, le=None, gt=None, ge=None, contains=None, starts_with=None, ends_with=None, pattern=None):  # noqa: E501
        """FilterPredicateOp - a model defined in Swagger"""  # noqa: E501
        self._any = None
        self._all = None
        self.__none = None
        self.__not = None
        self.__is = None
        self._is_not = None
        self._lt = None
        self._le = None
        self._gt = None
        self._ge = None
        self._contains = None
        self._starts_with = None
        self._ends_with = None
        self._pattern = None
        self.discriminator = None
        if any is not None:
            self.any = any
        if all is not None:
            self.all = all
        if _none is not None:
            self._none = _none
        if _not is not None:
            self._not = _not
        if _is is not None:
            self._is = _is
        if is_not is not None:
            self.is_not = is_not
        if lt is not None:
            self.lt = lt
        if le is not None:
            self.le = le
        if gt is not None:
            self.gt = gt
        if ge is not None:
            self.ge = ge
        if contains is not None:
            self.contains = contains
        if starts_with is not None:
            self.starts_with = starts_with
        if ends_with is not None:
            self.ends_with = ends_with
        if pattern is not None:
            self.pattern = pattern

    @property
    def any(self):
        """Gets the any of this FilterPredicateOp.  # noqa: E501


        :return: The any of this FilterPredicateOp.  # noqa: E501
        :rtype: OneOfFilterPredicateOpAny
        """
        return self._any

    @any.setter
    def any(self, any):
        """Sets the any of this FilterPredicateOp.


        :param any: The any of this FilterPredicateOp.  # noqa: E501
        :type: OneOfFilterPredicateOpAny
        """

        self._any = any

    @property
    def all(self):
        """Gets the all of this FilterPredicateOp.  # noqa: E501


        :return: The all of this FilterPredicateOp.  # noqa: E501
        :rtype: OneOfFilterPredicateOpAll
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this FilterPredicateOp.


        :param all: The all of this FilterPredicateOp.  # noqa: E501
        :type: OneOfFilterPredicateOpAll
        """

        self._all = all

    @property
    def _none(self):
        """Gets the _none of this FilterPredicateOp.  # noqa: E501


        :return: The _none of this FilterPredicateOp.  # noqa: E501
        :rtype: OneOfFilterPredicateOpNone
        """
        return self.__none

    @_none.setter
    def _none(self, _none):
        """Sets the _none of this FilterPredicateOp.


        :param _none: The _none of this FilterPredicateOp.  # noqa: E501
        :type: OneOfFilterPredicateOpNone
        """

        self.__none = _none

    @property
    def _not(self):
        """Gets the _not of this FilterPredicateOp.  # noqa: E501


        :return: The _not of this FilterPredicateOp.  # noqa: E501
        :rtype: OneOfFilterPredicateOpNot
        """
        return self.__not

    @_not.setter
    def _not(self, _not):
        """Sets the _not of this FilterPredicateOp.


        :param _not: The _not of this FilterPredicateOp.  # noqa: E501
        :type: OneOfFilterPredicateOpNot
        """

        self.__not = _not

    @property
    def _is(self):
        """Gets the _is of this FilterPredicateOp.  # noqa: E501


        :return: The _is of this FilterPredicateOp.  # noqa: E501
        :rtype: OneOfFilterPredicateOpIs
        """
        return self.__is

    @_is.setter
    def _is(self, _is):
        """Sets the _is of this FilterPredicateOp.


        :param _is: The _is of this FilterPredicateOp.  # noqa: E501
        :type: OneOfFilterPredicateOpIs
        """

        self.__is = _is

    @property
    def is_not(self):
        """Gets the is_not of this FilterPredicateOp.  # noqa: E501


        :return: The is_not of this FilterPredicateOp.  # noqa: E501
        :rtype: OneOfFilterPredicateOpIsNot
        """
        return self._is_not

    @is_not.setter
    def is_not(self, is_not):
        """Sets the is_not of this FilterPredicateOp.


        :param is_not: The is_not of this FilterPredicateOp.  # noqa: E501
        :type: OneOfFilterPredicateOpIsNot
        """

        self._is_not = is_not

    @property
    def lt(self):
        """Gets the lt of this FilterPredicateOp.  # noqa: E501


        :return: The lt of this FilterPredicateOp.  # noqa: E501
        :rtype: FilterRangeValue
        """
        return self._lt

    @lt.setter
    def lt(self, lt):
        """Sets the lt of this FilterPredicateOp.


        :param lt: The lt of this FilterPredicateOp.  # noqa: E501
        :type: FilterRangeValue
        """

        self._lt = lt

    @property
    def le(self):
        """Gets the le of this FilterPredicateOp.  # noqa: E501


        :return: The le of this FilterPredicateOp.  # noqa: E501
        :rtype: FilterRangeValue
        """
        return self._le

    @le.setter
    def le(self, le):
        """Sets the le of this FilterPredicateOp.


        :param le: The le of this FilterPredicateOp.  # noqa: E501
        :type: FilterRangeValue
        """

        self._le = le

    @property
    def gt(self):
        """Gets the gt of this FilterPredicateOp.  # noqa: E501


        :return: The gt of this FilterPredicateOp.  # noqa: E501
        :rtype: FilterRangeValue
        """
        return self._gt

    @gt.setter
    def gt(self, gt):
        """Sets the gt of this FilterPredicateOp.


        :param gt: The gt of this FilterPredicateOp.  # noqa: E501
        :type: FilterRangeValue
        """

        self._gt = gt

    @property
    def ge(self):
        """Gets the ge of this FilterPredicateOp.  # noqa: E501


        :return: The ge of this FilterPredicateOp.  # noqa: E501
        :rtype: FilterRangeValue
        """
        return self._ge

    @ge.setter
    def ge(self, ge):
        """Sets the ge of this FilterPredicateOp.


        :param ge: The ge of this FilterPredicateOp.  # noqa: E501
        :type: FilterRangeValue
        """

        self._ge = ge

    @property
    def contains(self):
        """Gets the contains of this FilterPredicateOp.  # noqa: E501


        :return: The contains of this FilterPredicateOp.  # noqa: E501
        :rtype: str
        """
        return self._contains

    @contains.setter
    def contains(self, contains):
        """Sets the contains of this FilterPredicateOp.


        :param contains: The contains of this FilterPredicateOp.  # noqa: E501
        :type: str
        """

        self._contains = contains

    @property
    def starts_with(self):
        """Gets the starts_with of this FilterPredicateOp.  # noqa: E501


        :return: The starts_with of this FilterPredicateOp.  # noqa: E501
        :rtype: str
        """
        return self._starts_with

    @starts_with.setter
    def starts_with(self, starts_with):
        """Sets the starts_with of this FilterPredicateOp.


        :param starts_with: The starts_with of this FilterPredicateOp.  # noqa: E501
        :type: str
        """

        self._starts_with = starts_with

    @property
    def ends_with(self):
        """Gets the ends_with of this FilterPredicateOp.  # noqa: E501


        :return: The ends_with of this FilterPredicateOp.  # noqa: E501
        :rtype: str
        """
        return self._ends_with

    @ends_with.setter
    def ends_with(self, ends_with):
        """Sets the ends_with of this FilterPredicateOp.


        :param ends_with: The ends_with of this FilterPredicateOp.  # noqa: E501
        :type: str
        """

        self._ends_with = ends_with

    @property
    def pattern(self):
        """Gets the pattern of this FilterPredicateOp.  # noqa: E501


        :return: The pattern of this FilterPredicateOp.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this FilterPredicateOp.


        :param pattern: The pattern of this FilterPredicateOp.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

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
        if issubclass(FilterPredicateOp, dict):
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
        if not isinstance(other, FilterPredicateOp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
