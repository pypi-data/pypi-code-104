# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecordAnalyticsAggregation(object):
    """
    Aggregation entities are required by the api consistency guidelines for API Consistency Guidelines#AnalyticsAPIs.  These are used to summarize record information for a given dataset and will be used to populate UI elements.  Aggregations need to have the fields that identify the exact scope that they're summarizing.  Any filters to the list API we apply would have to show up in the aggregation. We should limit the number of filters and dimensions as much as possible.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RecordAnalyticsAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param count:
            The value to assign to the count property of this RecordAnalyticsAggregation.
        :type count: float

        :param dimensions:
            The value to assign to the dimensions property of this RecordAnalyticsAggregation.
        :type dimensions: oci.data_labeling_service_dataplane.models.RecordAggregationDimensions

        :param dataset_id:
            The value to assign to the dataset_id property of this RecordAnalyticsAggregation.
        :type dataset_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RecordAnalyticsAggregation.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RecordAnalyticsAggregation.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'count': 'float',
            'dimensions': 'RecordAggregationDimensions',
            'dataset_id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'count': 'count',
            'dimensions': 'dimensions',
            'dataset_id': 'datasetId',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState'
        }

        self._count = None
        self._dimensions = None
        self._dataset_id = None
        self._compartment_id = None
        self._lifecycle_state = None

    @property
    def count(self):
        """
        **[Required]** Gets the count of this RecordAnalyticsAggregation.
        the count of the matching results


        :return: The count of this RecordAnalyticsAggregation.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this RecordAnalyticsAggregation.
        the count of the matching results


        :param count: The count of this RecordAnalyticsAggregation.
        :type: float
        """
        self._count = count

    @property
    def dimensions(self):
        """
        Gets the dimensions of this RecordAnalyticsAggregation.

        :return: The dimensions of this RecordAnalyticsAggregation.
        :rtype: oci.data_labeling_service_dataplane.models.RecordAggregationDimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this RecordAnalyticsAggregation.

        :param dimensions: The dimensions of this RecordAnalyticsAggregation.
        :type: oci.data_labeling_service_dataplane.models.RecordAggregationDimensions
        """
        self._dimensions = dimensions

    @property
    def dataset_id(self):
        """
        **[Required]** Gets the dataset_id of this RecordAnalyticsAggregation.
        ocid of the dataset the annotation belongs to


        :return: The dataset_id of this RecordAnalyticsAggregation.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """
        Sets the dataset_id of this RecordAnalyticsAggregation.
        ocid of the dataset the annotation belongs to


        :param dataset_id: The dataset_id of this RecordAnalyticsAggregation.
        :type: str
        """
        self._dataset_id = dataset_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RecordAnalyticsAggregation.
        ocid of the compartment the records


        :return: The compartment_id of this RecordAnalyticsAggregation.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RecordAnalyticsAggregation.
        ocid of the compartment the records


        :param compartment_id: The compartment_id of this RecordAnalyticsAggregation.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RecordAnalyticsAggregation.
        Describes the lifecycle state.


        :return: The lifecycle_state of this RecordAnalyticsAggregation.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RecordAnalyticsAggregation.
        Describes the lifecycle state.


        :param lifecycle_state: The lifecycle_state of this RecordAnalyticsAggregation.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
