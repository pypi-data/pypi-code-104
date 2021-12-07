# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInsights(object):
    """
    Logical grouping used for Operations Insights Exadata related operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInsights object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_insights:
            The value to assign to the exadata_insights property of this ExadataInsights.
        :type exadata_insights: object

        """
        self.swagger_types = {
            'exadata_insights': 'object'
        }

        self.attribute_map = {
            'exadata_insights': 'exadataInsights'
        }

        self._exadata_insights = None

    @property
    def exadata_insights(self):
        """
        Gets the exadata_insights of this ExadataInsights.
        Exadata Insights Object.


        :return: The exadata_insights of this ExadataInsights.
        :rtype: object
        """
        return self._exadata_insights

    @exadata_insights.setter
    def exadata_insights(self, exadata_insights):
        """
        Sets the exadata_insights of this ExadataInsights.
        Exadata Insights Object.


        :param exadata_insights: The exadata_insights of this ExadataInsights.
        :type: object
        """
        self._exadata_insights = exadata_insights

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
