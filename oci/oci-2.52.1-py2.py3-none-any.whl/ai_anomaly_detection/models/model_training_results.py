# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelTrainingResults(object):
    """
    Specifies the details for an Anomaly Detection model trained with MSET.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModelTrainingResults object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fap:
            The value to assign to the fap property of this ModelTrainingResults.
        :type fap: float

        :param multivariate_fap:
            The value to assign to the multivariate_fap property of this ModelTrainingResults.
        :type multivariate_fap: float

        :param is_training_goal_achieved:
            The value to assign to the is_training_goal_achieved property of this ModelTrainingResults.
        :type is_training_goal_achieved: bool

        :param warning:
            The value to assign to the warning property of this ModelTrainingResults.
        :type warning: str

        :param signal_details:
            The value to assign to the signal_details property of this ModelTrainingResults.
        :type signal_details: list[oci.ai_anomaly_detection.models.PerSignalDetails]

        :param row_reduction_details:
            The value to assign to the row_reduction_details property of this ModelTrainingResults.
        :type row_reduction_details: oci.ai_anomaly_detection.models.RowReductionDetails

        """
        self.swagger_types = {
            'fap': 'float',
            'multivariate_fap': 'float',
            'is_training_goal_achieved': 'bool',
            'warning': 'str',
            'signal_details': 'list[PerSignalDetails]',
            'row_reduction_details': 'RowReductionDetails'
        }

        self.attribute_map = {
            'fap': 'fap',
            'multivariate_fap': 'multivariateFap',
            'is_training_goal_achieved': 'isTrainingGoalAchieved',
            'warning': 'warning',
            'signal_details': 'signalDetails',
            'row_reduction_details': 'rowReductionDetails'
        }

        self._fap = None
        self._multivariate_fap = None
        self._is_training_goal_achieved = None
        self._warning = None
        self._signal_details = None
        self._row_reduction_details = None

    @property
    def fap(self):
        """
        **[Required]** Gets the fap of this ModelTrainingResults.
        The final-achieved model accuracy metric on individual value level


        :return: The fap of this ModelTrainingResults.
        :rtype: float
        """
        return self._fap

    @fap.setter
    def fap(self, fap):
        """
        Sets the fap of this ModelTrainingResults.
        The final-achieved model accuracy metric on individual value level


        :param fap: The fap of this ModelTrainingResults.
        :type: float
        """
        self._fap = fap

    @property
    def multivariate_fap(self):
        """
        Gets the multivariate_fap of this ModelTrainingResults.
        The model accuracy metric on timestamp level.


        :return: The multivariate_fap of this ModelTrainingResults.
        :rtype: float
        """
        return self._multivariate_fap

    @multivariate_fap.setter
    def multivariate_fap(self, multivariate_fap):
        """
        Sets the multivariate_fap of this ModelTrainingResults.
        The model accuracy metric on timestamp level.


        :param multivariate_fap: The multivariate_fap of this ModelTrainingResults.
        :type: float
        """
        self._multivariate_fap = multivariate_fap

    @property
    def is_training_goal_achieved(self):
        """
        Gets the is_training_goal_achieved of this ModelTrainingResults.
        A boolean value to indicate if train goal/targetFap is achieved for trained model


        :return: The is_training_goal_achieved of this ModelTrainingResults.
        :rtype: bool
        """
        return self._is_training_goal_achieved

    @is_training_goal_achieved.setter
    def is_training_goal_achieved(self, is_training_goal_achieved):
        """
        Sets the is_training_goal_achieved of this ModelTrainingResults.
        A boolean value to indicate if train goal/targetFap is achieved for trained model


        :param is_training_goal_achieved: The is_training_goal_achieved of this ModelTrainingResults.
        :type: bool
        """
        self._is_training_goal_achieved = is_training_goal_achieved

    @property
    def warning(self):
        """
        Gets the warning of this ModelTrainingResults.
        A warning message to explain the reason when targetFap cannot be achieved for trained model


        :return: The warning of this ModelTrainingResults.
        :rtype: str
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """
        Sets the warning of this ModelTrainingResults.
        A warning message to explain the reason when targetFap cannot be achieved for trained model


        :param warning: The warning of this ModelTrainingResults.
        :type: str
        """
        self._warning = warning

    @property
    def signal_details(self):
        """
        Gets the signal_details of this ModelTrainingResults.
        The list of signal details.


        :return: The signal_details of this ModelTrainingResults.
        :rtype: list[oci.ai_anomaly_detection.models.PerSignalDetails]
        """
        return self._signal_details

    @signal_details.setter
    def signal_details(self, signal_details):
        """
        Sets the signal_details of this ModelTrainingResults.
        The list of signal details.


        :param signal_details: The signal_details of this ModelTrainingResults.
        :type: list[oci.ai_anomaly_detection.models.PerSignalDetails]
        """
        self._signal_details = signal_details

    @property
    def row_reduction_details(self):
        """
        Gets the row_reduction_details of this ModelTrainingResults.

        :return: The row_reduction_details of this ModelTrainingResults.
        :rtype: oci.ai_anomaly_detection.models.RowReductionDetails
        """
        return self._row_reduction_details

    @row_reduction_details.setter
    def row_reduction_details(self, row_reduction_details):
        """
        Sets the row_reduction_details of this ModelTrainingResults.

        :param row_reduction_details: The row_reduction_details of this ModelTrainingResults.
        :type: oci.ai_anomaly_detection.models.RowReductionDetails
        """
        self._row_reduction_details = row_reduction_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
