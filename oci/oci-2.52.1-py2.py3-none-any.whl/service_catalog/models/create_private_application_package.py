# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreatePrivateApplicationPackage(object):
    """
    A base object for creating a private application package.
    """

    #: A constant which can be used with the package_type property of a CreatePrivateApplicationPackage.
    #: This constant has a value of "STACK"
    PACKAGE_TYPE_STACK = "STACK"

    def __init__(self, **kwargs):
        """
        Initializes a new CreatePrivateApplicationPackage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_catalog.models.CreatePrivateApplicationStackPackage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_type:
            The value to assign to the package_type property of this CreatePrivateApplicationPackage.
            Allowed values for this property are: "STACK"
        :type package_type: str

        :param version:
            The value to assign to the version property of this CreatePrivateApplicationPackage.
        :type version: str

        """
        self.swagger_types = {
            'package_type': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'package_type': 'packageType',
            'version': 'version'
        }

        self._package_type = None
        self._version = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['packageType']

        if type == 'STACK':
            return 'CreatePrivateApplicationStackPackage'
        else:
            return 'CreatePrivateApplicationPackage'

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this CreatePrivateApplicationPackage.
        The package's type.

        Allowed values for this property are: "STACK"


        :return: The package_type of this CreatePrivateApplicationPackage.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this CreatePrivateApplicationPackage.
        The package's type.


        :param package_type: The package_type of this CreatePrivateApplicationPackage.
        :type: str
        """
        allowed_values = ["STACK"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            raise ValueError(
                "Invalid value for `package_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._package_type = package_type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this CreatePrivateApplicationPackage.
        The package version.


        :return: The version of this CreatePrivateApplicationPackage.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this CreatePrivateApplicationPackage.
        The package version.


        :param version: The version of this CreatePrivateApplicationPackage.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
