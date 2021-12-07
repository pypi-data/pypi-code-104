# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatasetFormatDetails(object):
    """
    Specifies how to process the data. Supported formats include IMAGE and TEXT.
    """

    #: A constant which can be used with the format_type property of a DatasetFormatDetails.
    #: This constant has a value of "DOCUMENT"
    FORMAT_TYPE_DOCUMENT = "DOCUMENT"

    #: A constant which can be used with the format_type property of a DatasetFormatDetails.
    #: This constant has a value of "IMAGE"
    FORMAT_TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the format_type property of a DatasetFormatDetails.
    #: This constant has a value of "TEXT"
    FORMAT_TYPE_TEXT = "TEXT"

    def __init__(self, **kwargs):
        """
        Initializes a new DatasetFormatDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_labeling_service.models.ImageDatasetFormatDetails`
        * :class:`~oci.data_labeling_service.models.DocumentDatasetFormatDetails`
        * :class:`~oci.data_labeling_service.models.TextDatasetFormatDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format_type:
            The value to assign to the format_type property of this DatasetFormatDetails.
            Allowed values for this property are: "DOCUMENT", "IMAGE", "TEXT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format_type: str

        """
        self.swagger_types = {
            'format_type': 'str'
        }

        self.attribute_map = {
            'format_type': 'formatType'
        }

        self._format_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['formatType']

        if type == 'IMAGE':
            return 'ImageDatasetFormatDetails'

        if type == 'DOCUMENT':
            return 'DocumentDatasetFormatDetails'

        if type == 'TEXT':
            return 'TextDatasetFormatDetails'
        else:
            return 'DatasetFormatDetails'

    @property
    def format_type(self):
        """
        **[Required]** Gets the format_type of this DatasetFormatDetails.
        Format type. IMAGE format are for record contents that are JPEGs or PNGs. TEXT format is for record contents that are txt files.

        Allowed values for this property are: "DOCUMENT", "IMAGE", "TEXT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format_type of this DatasetFormatDetails.
        :rtype: str
        """
        return self._format_type

    @format_type.setter
    def format_type(self, format_type):
        """
        Sets the format_type of this DatasetFormatDetails.
        Format type. IMAGE format are for record contents that are JPEGs or PNGs. TEXT format is for record contents that are txt files.


        :param format_type: The format_type of this DatasetFormatDetails.
        :type: str
        """
        allowed_values = ["DOCUMENT", "IMAGE", "TEXT"]
        if not value_allowed_none_or_none_sentinel(format_type, allowed_values):
            format_type = 'UNKNOWN_ENUM_VALUE'
        self._format_type = format_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
