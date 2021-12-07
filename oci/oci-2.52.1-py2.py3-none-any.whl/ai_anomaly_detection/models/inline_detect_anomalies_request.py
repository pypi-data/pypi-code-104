# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .detect_anomalies_details import DetectAnomaliesDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InlineDetectAnomaliesRequest(DetectAnomaliesDetails):
    """
    This is the specialised JSON format that we accept as Training data, with an additional
    field for 'requestType' which is a required field used deciding whether it is an inline
    request or contains embedded data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InlineDetectAnomaliesRequest object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_anomaly_detection.models.InlineDetectAnomaliesRequest.request_type` attribute
        of this class is ``INLINE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_id:
            The value to assign to the model_id property of this InlineDetectAnomaliesRequest.
        :type model_id: str

        :param request_type:
            The value to assign to the request_type property of this InlineDetectAnomaliesRequest.
            Allowed values for this property are: "INLINE", "BASE64_ENCODED"
        :type request_type: str

        :param signal_names:
            The value to assign to the signal_names property of this InlineDetectAnomaliesRequest.
        :type signal_names: list[str]

        :param data:
            The value to assign to the data property of this InlineDetectAnomaliesRequest.
        :type data: list[oci.ai_anomaly_detection.models.DataItem]

        """
        self.swagger_types = {
            'model_id': 'str',
            'request_type': 'str',
            'signal_names': 'list[str]',
            'data': 'list[DataItem]'
        }

        self.attribute_map = {
            'model_id': 'modelId',
            'request_type': 'requestType',
            'signal_names': 'signalNames',
            'data': 'data'
        }

        self._model_id = None
        self._request_type = None
        self._signal_names = None
        self._data = None
        self._request_type = 'INLINE'

    @property
    def signal_names(self):
        """
        **[Required]** Gets the signal_names of this InlineDetectAnomaliesRequest.
        List of signal names.


        :return: The signal_names of this InlineDetectAnomaliesRequest.
        :rtype: list[str]
        """
        return self._signal_names

    @signal_names.setter
    def signal_names(self, signal_names):
        """
        Sets the signal_names of this InlineDetectAnomaliesRequest.
        List of signal names.


        :param signal_names: The signal_names of this InlineDetectAnomaliesRequest.
        :type: list[str]
        """
        self._signal_names = signal_names

    @property
    def data(self):
        """
        **[Required]** Gets the data of this InlineDetectAnomaliesRequest.
        Array containing data.


        :return: The data of this InlineDetectAnomaliesRequest.
        :rtype: list[oci.ai_anomaly_detection.models.DataItem]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this InlineDetectAnomaliesRequest.
        Array containing data.


        :param data: The data of this InlineDetectAnomaliesRequest.
        :type: list[oci.ai_anomaly_detection.models.DataItem]
        """
        self._data = data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
