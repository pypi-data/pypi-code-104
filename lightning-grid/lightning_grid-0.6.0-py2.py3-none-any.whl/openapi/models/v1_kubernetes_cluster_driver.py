# coding: utf-8

"""
    external/v1/external_session_service.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    NOTE
    ----
    standard swagger-codegen-cli for this python client has been modified
    by custom templates. The purpose of these templates is to include
    typing information in the API and Model code. Please refer to the
    main grid repository for more info
"""


import pprint
import re  # noqa: F401
from typing import TYPE_CHECKING

import six

from grid.openapi.configuration import Configuration

if TYPE_CHECKING:
    from datetime import datetime
    from grid.openapi.models import *

class V1KubernetesClusterDriver(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'aws': 'V1AWSClusterDriverSpec',
        'azure': 'V1AzureClusterDriverSpec',
        'extra_gridlet_env_var': 'dict(str, str)',
        'kubeconfig': 'V1ExternalKubeconfig',
        'namespace': 'str',
        'root_domain_name': 'str'
    }

    attribute_map = {
        'aws': 'aws',
        'azure': 'azure',
        'extra_gridlet_env_var': 'extraGridletEnvVar',
        'kubeconfig': 'kubeconfig',
        'namespace': 'namespace',
        'root_domain_name': 'rootDomainName'
    }

    def __init__(self, aws: 'V1AWSClusterDriverSpec' = None, azure: 'V1AzureClusterDriverSpec' = None, extra_gridlet_env_var: 'dict(str, str)' = None, kubeconfig: 'V1ExternalKubeconfig' = None, namespace: 'str' = None, root_domain_name: 'str' = None, _configuration=None):  # noqa: E501
        """V1KubernetesClusterDriver - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._aws = None
        self._azure = None
        self._extra_gridlet_env_var = None
        self._kubeconfig = None
        self._namespace = None
        self._root_domain_name = None
        self.discriminator = None

        if aws is not None:
            self.aws = aws
        if azure is not None:
            self.azure = azure
        if extra_gridlet_env_var is not None:
            self.extra_gridlet_env_var = extra_gridlet_env_var
        if kubeconfig is not None:
            self.kubeconfig = kubeconfig
        if namespace is not None:
            self.namespace = namespace
        if root_domain_name is not None:
            self.root_domain_name = root_domain_name

    @property
    def aws(self) -> 'V1AWSClusterDriverSpec':
        """Gets the aws of this V1KubernetesClusterDriver.  # noqa: E501


        :return: The aws of this V1KubernetesClusterDriver.  # noqa: E501
        :rtype: V1AWSClusterDriverSpec
        """
        return self._aws

    @aws.setter
    def aws(self, aws: 'V1AWSClusterDriverSpec'):
        """Sets the aws of this V1KubernetesClusterDriver.


        :param aws: The aws of this V1KubernetesClusterDriver.  # noqa: E501
        :type: V1AWSClusterDriverSpec
        """

        self._aws = aws

    @property
    def azure(self) -> 'V1AzureClusterDriverSpec':
        """Gets the azure of this V1KubernetesClusterDriver.  # noqa: E501


        :return: The azure of this V1KubernetesClusterDriver.  # noqa: E501
        :rtype: V1AzureClusterDriverSpec
        """
        return self._azure

    @azure.setter
    def azure(self, azure: 'V1AzureClusterDriverSpec'):
        """Sets the azure of this V1KubernetesClusterDriver.


        :param azure: The azure of this V1KubernetesClusterDriver.  # noqa: E501
        :type: V1AzureClusterDriverSpec
        """

        self._azure = azure

    @property
    def extra_gridlet_env_var(self) -> 'dict(str, str)':
        """Gets the extra_gridlet_env_var of this V1KubernetesClusterDriver.  # noqa: E501


        :return: The extra_gridlet_env_var of this V1KubernetesClusterDriver.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extra_gridlet_env_var

    @extra_gridlet_env_var.setter
    def extra_gridlet_env_var(self, extra_gridlet_env_var: 'dict(str, str)'):
        """Sets the extra_gridlet_env_var of this V1KubernetesClusterDriver.


        :param extra_gridlet_env_var: The extra_gridlet_env_var of this V1KubernetesClusterDriver.  # noqa: E501
        :type: dict(str, str)
        """

        self._extra_gridlet_env_var = extra_gridlet_env_var

    @property
    def kubeconfig(self) -> 'V1ExternalKubeconfig':
        """Gets the kubeconfig of this V1KubernetesClusterDriver.  # noqa: E501


        :return: The kubeconfig of this V1KubernetesClusterDriver.  # noqa: E501
        :rtype: V1ExternalKubeconfig
        """
        return self._kubeconfig

    @kubeconfig.setter
    def kubeconfig(self, kubeconfig: 'V1ExternalKubeconfig'):
        """Sets the kubeconfig of this V1KubernetesClusterDriver.


        :param kubeconfig: The kubeconfig of this V1KubernetesClusterDriver.  # noqa: E501
        :type: V1ExternalKubeconfig
        """

        self._kubeconfig = kubeconfig

    @property
    def namespace(self) -> 'str':
        """Gets the namespace of this V1KubernetesClusterDriver.  # noqa: E501


        :return: The namespace of this V1KubernetesClusterDriver.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: 'str'):
        """Sets the namespace of this V1KubernetesClusterDriver.


        :param namespace: The namespace of this V1KubernetesClusterDriver.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def root_domain_name(self) -> 'str':
        """Gets the root_domain_name of this V1KubernetesClusterDriver.  # noqa: E501


        :return: The root_domain_name of this V1KubernetesClusterDriver.  # noqa: E501
        :rtype: str
        """
        return self._root_domain_name

    @root_domain_name.setter
    def root_domain_name(self, root_domain_name: 'str'):
        """Sets the root_domain_name of this V1KubernetesClusterDriver.


        :param root_domain_name: The root_domain_name of this V1KubernetesClusterDriver.  # noqa: E501
        :type: str
        """

        self._root_domain_name = root_domain_name

    def to_dict(self) -> dict:
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1KubernetesClusterDriver, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self) -> str:
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self) -> str:
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other: 'V1KubernetesClusterDriver') -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, V1KubernetesClusterDriver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other: 'V1KubernetesClusterDriver') -> bool:
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1KubernetesClusterDriver):
            return True

        return self.to_dict() != other.to_dict()
