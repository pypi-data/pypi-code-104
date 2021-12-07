# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAnnotationDetails(object):
    """
    This is the payload sent in the CreateAnnotation operation. It contains all the information required for a user to create an Annotation for a record.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAnnotationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entities:
            The value to assign to the entities property of this UpdateAnnotationDetails.
        :type entities: list[oci.data_labeling_service_dataplane.models.Entity]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAnnotationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAnnotationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entities': 'list[Entity]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entities': 'entities',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._entities = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def entities(self):
        """
        Gets the entities of this UpdateAnnotationDetails.
        The entity types will be validated against the dataset to ensure consistency.


        :return: The entities of this UpdateAnnotationDetails.
        :rtype: list[oci.data_labeling_service_dataplane.models.Entity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """
        Sets the entities of this UpdateAnnotationDetails.
        The entity types will be validated against the dataset to ensure consistency.


        :param entities: The entities of this UpdateAnnotationDetails.
        :type: list[oci.data_labeling_service_dataplane.models.Entity]
        """
        self._entities = entities

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAnnotationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateAnnotationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAnnotationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateAnnotationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAnnotationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateAnnotationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAnnotationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateAnnotationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
