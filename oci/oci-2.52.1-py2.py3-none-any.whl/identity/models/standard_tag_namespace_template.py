# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StandardTagNamespaceTemplate(object):
    """
    The template of the standard tag namespace. This object includes necessary details to create the provided standard tag namespace.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StandardTagNamespaceTemplate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this StandardTagNamespaceTemplate.
        :type description: str

        :param standard_tag_namespace_name:
            The value to assign to the standard_tag_namespace_name property of this StandardTagNamespaceTemplate.
        :type standard_tag_namespace_name: str

        :param tag_definition_templates:
            The value to assign to the tag_definition_templates property of this StandardTagNamespaceTemplate.
        :type tag_definition_templates: list[oci.identity.models.StandardTagDefinitionTemplate]

        :param status:
            The value to assign to the status property of this StandardTagNamespaceTemplate.
        :type status: str

        """
        self.swagger_types = {
            'description': 'str',
            'standard_tag_namespace_name': 'str',
            'tag_definition_templates': 'list[StandardTagDefinitionTemplate]',
            'status': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'standard_tag_namespace_name': 'standardTagNamespaceName',
            'tag_definition_templates': 'tagDefinitionTemplates',
            'status': 'status'
        }

        self._description = None
        self._standard_tag_namespace_name = None
        self._tag_definition_templates = None
        self._status = None

    @property
    def description(self):
        """
        **[Required]** Gets the description of this StandardTagNamespaceTemplate.
        The default description of the tag namespace that users can use to create the tag namespace


        :return: The description of this StandardTagNamespaceTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StandardTagNamespaceTemplate.
        The default description of the tag namespace that users can use to create the tag namespace


        :param description: The description of this StandardTagNamespaceTemplate.
        :type: str
        """
        self._description = description

    @property
    def standard_tag_namespace_name(self):
        """
        **[Required]** Gets the standard_tag_namespace_name of this StandardTagNamespaceTemplate.
        The reserved name of this standard tag namespace


        :return: The standard_tag_namespace_name of this StandardTagNamespaceTemplate.
        :rtype: str
        """
        return self._standard_tag_namespace_name

    @standard_tag_namespace_name.setter
    def standard_tag_namespace_name(self, standard_tag_namespace_name):
        """
        Sets the standard_tag_namespace_name of this StandardTagNamespaceTemplate.
        The reserved name of this standard tag namespace


        :param standard_tag_namespace_name: The standard_tag_namespace_name of this StandardTagNamespaceTemplate.
        :type: str
        """
        self._standard_tag_namespace_name = standard_tag_namespace_name

    @property
    def tag_definition_templates(self):
        """
        **[Required]** Gets the tag_definition_templates of this StandardTagNamespaceTemplate.
        The template of the tag definition. This object includes necessary details to create the provided standard tag definition.


        :return: The tag_definition_templates of this StandardTagNamespaceTemplate.
        :rtype: list[oci.identity.models.StandardTagDefinitionTemplate]
        """
        return self._tag_definition_templates

    @tag_definition_templates.setter
    def tag_definition_templates(self, tag_definition_templates):
        """
        Sets the tag_definition_templates of this StandardTagNamespaceTemplate.
        The template of the tag definition. This object includes necessary details to create the provided standard tag definition.


        :param tag_definition_templates: The tag_definition_templates of this StandardTagNamespaceTemplate.
        :type: list[oci.identity.models.StandardTagDefinitionTemplate]
        """
        self._tag_definition_templates = tag_definition_templates

    @property
    def status(self):
        """
        **[Required]** Gets the status of this StandardTagNamespaceTemplate.
        The status of the standard tag namespace


        :return: The status of this StandardTagNamespaceTemplate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StandardTagNamespaceTemplate.
        The status of the standard tag namespace


        :param status: The status of this StandardTagNamespaceTemplate.
        :type: str
        """
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
