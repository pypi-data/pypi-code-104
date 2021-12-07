# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectVersionCollection(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectVersionCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this ObjectVersionCollection.
        :type items: list[oci.object_storage.models.ObjectVersionSummary]

        :param prefixes:
            The value to assign to the prefixes property of this ObjectVersionCollection.
        :type prefixes: list[str]

        """
        self.swagger_types = {
            'items': 'list[ObjectVersionSummary]',
            'prefixes': 'list[str]'
        }

        self.attribute_map = {
            'items': 'items',
            'prefixes': 'prefixes'
        }

        self._items = None
        self._prefixes = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ObjectVersionCollection.
        An array of object version summaries.


        :return: The items of this ObjectVersionCollection.
        :rtype: list[oci.object_storage.models.ObjectVersionSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ObjectVersionCollection.
        An array of object version summaries.


        :param items: The items of this ObjectVersionCollection.
        :type: list[oci.object_storage.models.ObjectVersionSummary]
        """
        self._items = items

    @property
    def prefixes(self):
        """
        Gets the prefixes of this ObjectVersionCollection.
        Prefixes that are common to the results returned by the request if the request specified a delimiter.


        :return: The prefixes of this ObjectVersionCollection.
        :rtype: list[str]
        """
        return self._prefixes

    @prefixes.setter
    def prefixes(self, prefixes):
        """
        Sets the prefixes of this ObjectVersionCollection.
        Prefixes that are common to the results returned by the request if the request specified a delimiter.


        :param prefixes: The prefixes of this ObjectVersionCollection.
        :type: list[str]
        """
        self._prefixes = prefixes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
