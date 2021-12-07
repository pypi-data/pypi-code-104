# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryFindingBenefits(object):
    """
    The finding benefits data for the SQL Tuning Advisor summary report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryFindingBenefits object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_time_before_recommended:
            The value to assign to the db_time_before_recommended property of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type db_time_before_recommended: int

        :param db_time_after_recommended:
            The value to assign to the db_time_after_recommended property of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type db_time_after_recommended: int

        :param db_time_before_implemented:
            The value to assign to the db_time_before_implemented property of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type db_time_before_implemented: int

        :param db_time_after_implemented:
            The value to assign to the db_time_after_implemented property of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type db_time_after_implemented: int

        """
        self.swagger_types = {
            'db_time_before_recommended': 'int',
            'db_time_after_recommended': 'int',
            'db_time_before_implemented': 'int',
            'db_time_after_implemented': 'int'
        }

        self.attribute_map = {
            'db_time_before_recommended': 'dbTimeBeforeRecommended',
            'db_time_after_recommended': 'dbTimeAfterRecommended',
            'db_time_before_implemented': 'dbTimeBeforeImplemented',
            'db_time_after_implemented': 'dbTimeAfterImplemented'
        }

        self._db_time_before_recommended = None
        self._db_time_after_recommended = None
        self._db_time_before_implemented = None
        self._db_time_after_implemented = None

    @property
    def db_time_before_recommended(self):
        """
        **[Required]** Gets the db_time_before_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of Potential database time before SQL recommendations are implemented.


        :return: The db_time_before_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :rtype: int
        """
        return self._db_time_before_recommended

    @db_time_before_recommended.setter
    def db_time_before_recommended(self, db_time_before_recommended):
        """
        Sets the db_time_before_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of Potential database time before SQL recommendations are implemented.


        :param db_time_before_recommended: The db_time_before_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type: int
        """
        self._db_time_before_recommended = db_time_before_recommended

    @property
    def db_time_after_recommended(self):
        """
        **[Required]** Gets the db_time_after_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of Potential database time after SQL recommendations are implemented.


        :return: The db_time_after_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :rtype: int
        """
        return self._db_time_after_recommended

    @db_time_after_recommended.setter
    def db_time_after_recommended(self, db_time_after_recommended):
        """
        Sets the db_time_after_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of Potential database time after SQL recommendations are implemented.


        :param db_time_after_recommended: The db_time_after_recommended of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type: int
        """
        self._db_time_after_recommended = db_time_after_recommended

    @property
    def db_time_before_implemented(self):
        """
        **[Required]** Gets the db_time_before_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of database time benefit before SQL recommendations are implemented.


        :return: The db_time_before_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :rtype: int
        """
        return self._db_time_before_implemented

    @db_time_before_implemented.setter
    def db_time_before_implemented(self, db_time_before_implemented):
        """
        Sets the db_time_before_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of database time benefit before SQL recommendations are implemented.


        :param db_time_before_implemented: The db_time_before_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type: int
        """
        self._db_time_before_implemented = db_time_before_implemented

    @property
    def db_time_after_implemented(self):
        """
        **[Required]** Gets the db_time_after_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of database time benefit after SQL recommendations are implemented.


        :return: The db_time_after_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :rtype: int
        """
        return self._db_time_after_implemented

    @db_time_after_implemented.setter
    def db_time_after_implemented(self, db_time_after_implemented):
        """
        Sets the db_time_after_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        The count of database time benefit after SQL recommendations are implemented.


        :param db_time_after_implemented: The db_time_after_implemented of this SqlTuningAdvisorTaskSummaryFindingBenefits.
        :type: int
        """
        self._db_time_after_implemented = db_time_after_implemented

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
