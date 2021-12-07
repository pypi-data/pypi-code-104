# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportContent(object):
    """
    The content to export.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExportContent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_names:
            The value to assign to the field_names property of this ExportContent.
        :type field_names: list[str]

        :param parser_names:
            The value to assign to the parser_names property of this ExportContent.
        :type parser_names: list[str]

        :param source_names:
            The value to assign to the source_names property of this ExportContent.
        :type source_names: list[str]

        """
        self.swagger_types = {
            'field_names': 'list[str]',
            'parser_names': 'list[str]',
            'source_names': 'list[str]'
        }

        self.attribute_map = {
            'field_names': 'fieldNames',
            'parser_names': 'parserNames',
            'source_names': 'sourceNames'
        }

        self._field_names = None
        self._parser_names = None
        self._source_names = None

    @property
    def field_names(self):
        """
        Gets the field_names of this ExportContent.
        The field names.


        :return: The field_names of this ExportContent.
        :rtype: list[str]
        """
        return self._field_names

    @field_names.setter
    def field_names(self, field_names):
        """
        Sets the field_names of this ExportContent.
        The field names.


        :param field_names: The field_names of this ExportContent.
        :type: list[str]
        """
        self._field_names = field_names

    @property
    def parser_names(self):
        """
        Gets the parser_names of this ExportContent.
        The parser names.


        :return: The parser_names of this ExportContent.
        :rtype: list[str]
        """
        return self._parser_names

    @parser_names.setter
    def parser_names(self, parser_names):
        """
        Sets the parser_names of this ExportContent.
        The parser names.


        :param parser_names: The parser_names of this ExportContent.
        :type: list[str]
        """
        self._parser_names = parser_names

    @property
    def source_names(self):
        """
        Gets the source_names of this ExportContent.
        The source names.


        :return: The source_names of this ExportContent.
        :rtype: list[str]
        """
        return self._source_names

    @source_names.setter
    def source_names(self, source_names):
        """
        Sets the source_names of this ExportContent.
        The source names.


        :param source_names: The source_names of this ExportContent.
        :type: list[str]
        """
        self._source_names = source_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
