# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataSourceDetails(object):
    """
    Possible data sources
    """

    #: A constant which can be used with the data_source_type property of a DataSourceDetails.
    #: This constant has a value of "ORACLE_OBJECT_STORAGE"
    DATA_SOURCE_TYPE_ORACLE_OBJECT_STORAGE = "ORACLE_OBJECT_STORAGE"

    #: A constant which can be used with the data_source_type property of a DataSourceDetails.
    #: This constant has a value of "ORACLE_ATP"
    DATA_SOURCE_TYPE_ORACLE_ATP = "ORACLE_ATP"

    #: A constant which can be used with the data_source_type property of a DataSourceDetails.
    #: This constant has a value of "INFLUX"
    DATA_SOURCE_TYPE_INFLUX = "INFLUX"

    def __init__(self, **kwargs):
        """
        Initializes a new DataSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_anomaly_detection.models.DataSourceDetailsObjectStorage`
        * :class:`~oci.ai_anomaly_detection.models.DataSourceDetailsInflux`
        * :class:`~oci.ai_anomaly_detection.models.DataSourceDetailsATP`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_type:
            The value to assign to the data_source_type property of this DataSourceDetails.
            Allowed values for this property are: "ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_source_type: str

        """
        self.swagger_types = {
            'data_source_type': 'str'
        }

        self.attribute_map = {
            'data_source_type': 'dataSourceType'
        }

        self._data_source_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dataSourceType']

        if type == 'ORACLE_OBJECT_STORAGE':
            return 'DataSourceDetailsObjectStorage'

        if type == 'INFLUX':
            return 'DataSourceDetailsInflux'

        if type == 'ORACLE_ATP':
            return 'DataSourceDetailsATP'
        else:
            return 'DataSourceDetails'

    @property
    def data_source_type(self):
        """
        **[Required]** Gets the data_source_type of this DataSourceDetails.
        Data source type where actually data asset is being stored

        Allowed values for this property are: "ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_source_type of this DataSourceDetails.
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """
        Sets the data_source_type of this DataSourceDetails.
        Data source type where actually data asset is being stored


        :param data_source_type: The data_source_type of this DataSourceDetails.
        :type: str
        """
        allowed_values = ["ORACLE_OBJECT_STORAGE", "ORACLE_ATP", "INFLUX"]
        if not value_allowed_none_or_none_sentinel(data_source_type, allowed_values):
            data_source_type = 'UNKNOWN_ENUM_VALUE'
        self._data_source_type = data_source_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
