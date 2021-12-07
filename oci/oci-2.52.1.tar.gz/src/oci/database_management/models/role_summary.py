# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoleSummary(object):
    """
    Summary of each role.
    """

    #: A constant which can be used with the admin_option property of a RoleSummary.
    #: This constant has a value of "YES"
    ADMIN_OPTION_YES = "YES"

    #: A constant which can be used with the admin_option property of a RoleSummary.
    #: This constant has a value of "NO"
    ADMIN_OPTION_NO = "NO"

    #: A constant which can be used with the delegate_option property of a RoleSummary.
    #: This constant has a value of "YES"
    DELEGATE_OPTION_YES = "YES"

    #: A constant which can be used with the delegate_option property of a RoleSummary.
    #: This constant has a value of "NO"
    DELEGATE_OPTION_NO = "NO"

    #: A constant which can be used with the default_role property of a RoleSummary.
    #: This constant has a value of "YES"
    DEFAULT_ROLE_YES = "YES"

    #: A constant which can be used with the default_role property of a RoleSummary.
    #: This constant has a value of "NO"
    DEFAULT_ROLE_NO = "NO"

    #: A constant which can be used with the common property of a RoleSummary.
    #: This constant has a value of "YES"
    COMMON_YES = "YES"

    #: A constant which can be used with the common property of a RoleSummary.
    #: This constant has a value of "NO"
    COMMON_NO = "NO"

    #: A constant which can be used with the inherited property of a RoleSummary.
    #: This constant has a value of "YES"
    INHERITED_YES = "YES"

    #: A constant which can be used with the inherited property of a RoleSummary.
    #: This constant has a value of "NO"
    INHERITED_NO = "NO"

    def __init__(self, **kwargs):
        """
        Initializes a new RoleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this RoleSummary.
        :type name: str

        :param admin_option:
            The value to assign to the admin_option property of this RoleSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type admin_option: str

        :param delegate_option:
            The value to assign to the delegate_option property of this RoleSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type delegate_option: str

        :param default_role:
            The value to assign to the default_role property of this RoleSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type default_role: str

        :param common:
            The value to assign to the common property of this RoleSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type common: str

        :param inherited:
            The value to assign to the inherited property of this RoleSummary.
            Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type inherited: str

        """
        self.swagger_types = {
            'name': 'str',
            'admin_option': 'str',
            'delegate_option': 'str',
            'default_role': 'str',
            'common': 'str',
            'inherited': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'admin_option': 'adminOption',
            'delegate_option': 'delegateOption',
            'default_role': 'defaultRole',
            'common': 'common',
            'inherited': 'inherited'
        }

        self._name = None
        self._admin_option = None
        self._delegate_option = None
        self._default_role = None
        self._common = None
        self._inherited = None

    @property
    def name(self):
        """
        Gets the name of this RoleSummary.
        The name of a granted role


        :return: The name of this RoleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RoleSummary.
        The name of a granted role


        :param name: The name of this RoleSummary.
        :type: str
        """
        self._name = name

    @property
    def admin_option(self):
        """
        Gets the admin_option of this RoleSummary.
        Indicates whether the grant was with the ADMIN OPTION (YES) or not (NO)

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The admin_option of this RoleSummary.
        :rtype: str
        """
        return self._admin_option

    @admin_option.setter
    def admin_option(self, admin_option):
        """
        Sets the admin_option of this RoleSummary.
        Indicates whether the grant was with the ADMIN OPTION (YES) or not (NO)


        :param admin_option: The admin_option of this RoleSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(admin_option, allowed_values):
            admin_option = 'UNKNOWN_ENUM_VALUE'
        self._admin_option = admin_option

    @property
    def delegate_option(self):
        """
        Gets the delegate_option of this RoleSummary.
        Indicates whether the grant was with the DELEGATE OPTION (YES) or not (NO)

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The delegate_option of this RoleSummary.
        :rtype: str
        """
        return self._delegate_option

    @delegate_option.setter
    def delegate_option(self, delegate_option):
        """
        Sets the delegate_option of this RoleSummary.
        Indicates whether the grant was with the DELEGATE OPTION (YES) or not (NO)


        :param delegate_option: The delegate_option of this RoleSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(delegate_option, allowed_values):
            delegate_option = 'UNKNOWN_ENUM_VALUE'
        self._delegate_option = delegate_option

    @property
    def default_role(self):
        """
        Gets the default_role of this RoleSummary.
        Indicates whether the role is designated as a DEFAULT ROLE for the user (YES) or not (NO)

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The default_role of this RoleSummary.
        :rtype: str
        """
        return self._default_role

    @default_role.setter
    def default_role(self, default_role):
        """
        Sets the default_role of this RoleSummary.
        Indicates whether the role is designated as a DEFAULT ROLE for the user (YES) or not (NO)


        :param default_role: The default_role of this RoleSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(default_role, allowed_values):
            default_role = 'UNKNOWN_ENUM_VALUE'
        self._default_role = default_role

    @property
    def common(self):
        """
        Gets the common of this RoleSummary.
        Indicates how the grant was made. Possible values:
        YES if the role was granted commonly (CONTAINER=ALL was used)
        NO if the role was granted locally (CONTAINER=ALL was not used)

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The common of this RoleSummary.
        :rtype: str
        """
        return self._common

    @common.setter
    def common(self, common):
        """
        Sets the common of this RoleSummary.
        Indicates how the grant was made. Possible values:
        YES if the role was granted commonly (CONTAINER=ALL was used)
        NO if the role was granted locally (CONTAINER=ALL was not used)


        :param common: The common of this RoleSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(common, allowed_values):
            common = 'UNKNOWN_ENUM_VALUE'
        self._common = common

    @property
    def inherited(self):
        """
        Gets the inherited of this RoleSummary.
        Indicates whether the role grant was inherited from another container (YES) or not (NO)

        Allowed values for this property are: "YES", "NO", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The inherited of this RoleSummary.
        :rtype: str
        """
        return self._inherited

    @inherited.setter
    def inherited(self, inherited):
        """
        Sets the inherited of this RoleSummary.
        Indicates whether the role grant was inherited from another container (YES) or not (NO)


        :param inherited: The inherited of this RoleSummary.
        :type: str
        """
        allowed_values = ["YES", "NO"]
        if not value_allowed_none_or_none_sentinel(inherited, allowed_values):
            inherited = 'UNKNOWN_ENUM_VALUE'
        self._inherited = inherited

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
