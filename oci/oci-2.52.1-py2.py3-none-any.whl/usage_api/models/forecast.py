# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Forecast(object):
    """
    Forecast configuration of usage/cost.
    """

    #: A constant which can be used with the forecast_type property of a Forecast.
    #: This constant has a value of "BASIC"
    FORECAST_TYPE_BASIC = "BASIC"

    def __init__(self, **kwargs):
        """
        Initializes a new Forecast object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param forecast_type:
            The value to assign to the forecast_type property of this Forecast.
            Allowed values for this property are: "BASIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type forecast_type: str

        :param time_forecast_started:
            The value to assign to the time_forecast_started property of this Forecast.
        :type time_forecast_started: datetime

        :param time_forecast_ended:
            The value to assign to the time_forecast_ended property of this Forecast.
        :type time_forecast_ended: datetime

        """
        self.swagger_types = {
            'forecast_type': 'str',
            'time_forecast_started': 'datetime',
            'time_forecast_ended': 'datetime'
        }

        self.attribute_map = {
            'forecast_type': 'forecastType',
            'time_forecast_started': 'timeForecastStarted',
            'time_forecast_ended': 'timeForecastEnded'
        }

        self._forecast_type = None
        self._time_forecast_started = None
        self._time_forecast_ended = None

    @property
    def forecast_type(self):
        """
        Gets the forecast_type of this Forecast.
        BASIC uses the exponential smoothing (ETS) model to project future usage/costs based on history data. The basis for projections is a periodic set of equivalent historical days for which the projection is being made.

        Allowed values for this property are: "BASIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The forecast_type of this Forecast.
        :rtype: str
        """
        return self._forecast_type

    @forecast_type.setter
    def forecast_type(self, forecast_type):
        """
        Sets the forecast_type of this Forecast.
        BASIC uses the exponential smoothing (ETS) model to project future usage/costs based on history data. The basis for projections is a periodic set of equivalent historical days for which the projection is being made.


        :param forecast_type: The forecast_type of this Forecast.
        :type: str
        """
        allowed_values = ["BASIC"]
        if not value_allowed_none_or_none_sentinel(forecast_type, allowed_values):
            forecast_type = 'UNKNOWN_ENUM_VALUE'
        self._forecast_type = forecast_type

    @property
    def time_forecast_started(self):
        """
        Gets the time_forecast_started of this Forecast.
        The forecast start time. Defaults to UTC-1 if not specified.


        :return: The time_forecast_started of this Forecast.
        :rtype: datetime
        """
        return self._time_forecast_started

    @time_forecast_started.setter
    def time_forecast_started(self, time_forecast_started):
        """
        Sets the time_forecast_started of this Forecast.
        The forecast start time. Defaults to UTC-1 if not specified.


        :param time_forecast_started: The time_forecast_started of this Forecast.
        :type: datetime
        """
        self._time_forecast_started = time_forecast_started

    @property
    def time_forecast_ended(self):
        """
        **[Required]** Gets the time_forecast_ended of this Forecast.
        The forecast end time.


        :return: The time_forecast_ended of this Forecast.
        :rtype: datetime
        """
        return self._time_forecast_ended

    @time_forecast_ended.setter
    def time_forecast_ended(self, time_forecast_ended):
        """
        Sets the time_forecast_ended of this Forecast.
        The forecast end time.


        :param time_forecast_ended: The time_forecast_ended of this Forecast.
        :type: datetime
        """
        self._time_forecast_ended = time_forecast_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
