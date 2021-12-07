# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InfluxDetails(object):
    """
    Possible data sources
    """

    #: A constant which can be used with the influx_version property of a InfluxDetails.
    #: This constant has a value of "V_1_8"
    INFLUX_VERSION_V_1_8 = "V_1_8"

    #: A constant which can be used with the influx_version property of a InfluxDetails.
    #: This constant has a value of "V_2_0"
    INFLUX_VERSION_V_2_0 = "V_2_0"

    def __init__(self, **kwargs):
        """
        Initializes a new InfluxDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.ai_anomaly_detection.models.InfluxDetailsV1v8`
        * :class:`~oci.ai_anomaly_detection.models.InfluxDetailsV2v0`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param influx_version:
            The value to assign to the influx_version property of this InfluxDetails.
            Allowed values for this property are: "V_1_8", "V_2_0", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type influx_version: str

        """
        self.swagger_types = {
            'influx_version': 'str'
        }

        self.attribute_map = {
            'influx_version': 'influxVersion'
        }

        self._influx_version = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['influxVersion']

        if type == 'V_1_8':
            return 'InfluxDetailsV1v8'

        if type == 'V_2_0':
            return 'InfluxDetailsV2v0'
        else:
            return 'InfluxDetails'

    @property
    def influx_version(self):
        """
        **[Required]** Gets the influx_version of this InfluxDetails.
        Data source type where actually data asset is being stored

        Allowed values for this property are: "V_1_8", "V_2_0", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The influx_version of this InfluxDetails.
        :rtype: str
        """
        return self._influx_version

    @influx_version.setter
    def influx_version(self, influx_version):
        """
        Sets the influx_version of this InfluxDetails.
        Data source type where actually data asset is being stored


        :param influx_version: The influx_version of this InfluxDetails.
        :type: str
        """
        allowed_values = ["V_1_8", "V_2_0"]
        if not value_allowed_none_or_none_sentinel(influx_version, allowed_values):
            influx_version = 'UNKNOWN_ENUM_VALUE'
        self._influx_version = influx_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
