# coding: utf-8

"""
    external/v1/external_session_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""


import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING

import six

from grid.openapi.configuration import Configuration

if TYPE_CHECKING:
    from datetime import datetime
    from grid.openapi.models import *

class Body2(object):
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
        'count': 'int',
        'object_key': 'str'
    }

    attribute_map = {
        'count': 'count',
        'object_key': 'objectKey'
    }

    def __init__(self, count: 'int' = None, object_key: 'str' = None, _configuration=None):  # noqa: E501
        """Body2 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._object_key = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if object_key is not None:
            self.object_key = object_key

    @property
    def count(self) -> 'int':
        """Gets the count of this Body2.  # noqa: E501


        :return: The count of this Body2.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: 'int'):
        """Sets the count of this Body2.


        :param count: The count of this Body2.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def object_key(self) -> 'str':
        """Gets the object_key of this Body2.  # noqa: E501


        :return: The object_key of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key: 'str'):
        """Sets the object_key of this Body2.


        :param object_key: The object_key of this Body2.  # noqa: E501
        :type: str
        """

        self._object_key = object_key

    def to_dict(self) -> dict:
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
        if issubclass(Body2, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'Body2') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, Body2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'Body2') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, Body2):
            return True

        return self.to_dict() != other.to_dict()
