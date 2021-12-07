# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeploymentBackupDetails(object):
    """
    The information about a new DeploymentBackup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeploymentBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDeploymentBackupDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDeploymentBackupDetails.
        :type compartment_id: str

        :param deployment_id:
            The value to assign to the deployment_id property of this CreateDeploymentBackupDetails.
        :type deployment_id: str

        :param namespace_name:
            The value to assign to the namespace_name property of this CreateDeploymentBackupDetails.
        :type namespace_name: str

        :param bucket_name:
            The value to assign to the bucket_name property of this CreateDeploymentBackupDetails.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this CreateDeploymentBackupDetails.
        :type object_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeploymentBackupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeploymentBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'deployment_id': 'str',
            'namespace_name': 'str',
            'bucket_name': 'str',
            'object_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'deployment_id': 'deploymentId',
            'namespace_name': 'namespaceName',
            'bucket_name': 'bucketName',
            'object_name': 'objectName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._deployment_id = None
        self._namespace_name = None
        self._bucket_name = None
        self._object_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDeploymentBackupDetails.
        An object's Display Name.


        :return: The display_name of this CreateDeploymentBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDeploymentBackupDetails.
        An object's Display Name.


        :param display_name: The display_name of this CreateDeploymentBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDeploymentBackupDetails.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDeploymentBackupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDeploymentBackupDetails.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDeploymentBackupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deployment_id(self):
        """
        **[Required]** Gets the deployment_id of this CreateDeploymentBackupDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deployment_id of this CreateDeploymentBackupDetails.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """
        Sets the deployment_id of this CreateDeploymentBackupDetails.
        The `OCID`__ of the deployment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deployment_id: The deployment_id of this CreateDeploymentBackupDetails.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this CreateDeploymentBackupDetails.
        Name of namespace that serves as a container for all of your buckets


        :return: The namespace_name of this CreateDeploymentBackupDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CreateDeploymentBackupDetails.
        Name of namespace that serves as a container for all of your buckets


        :param namespace_name: The namespace_name of this CreateDeploymentBackupDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CreateDeploymentBackupDetails.
        Name of the bucket where the object is to be uploaded in the object storage


        :return: The bucket_name of this CreateDeploymentBackupDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CreateDeploymentBackupDetails.
        Name of the bucket where the object is to be uploaded in the object storage


        :param bucket_name: The bucket_name of this CreateDeploymentBackupDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this CreateDeploymentBackupDetails.
        Name of the object to be uploaded to object storage


        :return: The object_name of this CreateDeploymentBackupDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this CreateDeploymentBackupDetails.
        Name of the object to be uploaded to object storage


        :param object_name: The object_name of this CreateDeploymentBackupDetails.
        :type: str
        """
        self._object_name = object_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDeploymentBackupDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDeploymentBackupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDeploymentBackupDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDeploymentBackupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDeploymentBackupDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDeploymentBackupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDeploymentBackupDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDeploymentBackupDetails.
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
