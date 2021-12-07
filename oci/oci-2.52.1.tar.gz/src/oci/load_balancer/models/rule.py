# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Rule(object):
    """
    An object that represents an action to apply to a listener.
    """

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "ADD_HTTP_REQUEST_HEADER"
    ACTION_ADD_HTTP_REQUEST_HEADER = "ADD_HTTP_REQUEST_HEADER"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "EXTEND_HTTP_REQUEST_HEADER_VALUE"
    ACTION_EXTEND_HTTP_REQUEST_HEADER_VALUE = "EXTEND_HTTP_REQUEST_HEADER_VALUE"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "REMOVE_HTTP_REQUEST_HEADER"
    ACTION_REMOVE_HTTP_REQUEST_HEADER = "REMOVE_HTTP_REQUEST_HEADER"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "ADD_HTTP_RESPONSE_HEADER"
    ACTION_ADD_HTTP_RESPONSE_HEADER = "ADD_HTTP_RESPONSE_HEADER"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "EXTEND_HTTP_RESPONSE_HEADER_VALUE"
    ACTION_EXTEND_HTTP_RESPONSE_HEADER_VALUE = "EXTEND_HTTP_RESPONSE_HEADER_VALUE"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "REMOVE_HTTP_RESPONSE_HEADER"
    ACTION_REMOVE_HTTP_RESPONSE_HEADER = "REMOVE_HTTP_RESPONSE_HEADER"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "ALLOW"
    ACTION_ALLOW = "ALLOW"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "CONTROL_ACCESS_USING_HTTP_METHODS"
    ACTION_CONTROL_ACCESS_USING_HTTP_METHODS = "CONTROL_ACCESS_USING_HTTP_METHODS"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "REDIRECT"
    ACTION_REDIRECT = "REDIRECT"

    #: A constant which can be used with the action property of a Rule.
    #: This constant has a value of "HTTP_HEADER"
    ACTION_HTTP_HEADER = "HTTP_HEADER"

    def __init__(self, **kwargs):
        """
        Initializes a new Rule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.load_balancer.models.AddHttpRequestHeaderRule`
        * :class:`~oci.load_balancer.models.RedirectRule`
        * :class:`~oci.load_balancer.models.RemoveHttpRequestHeaderRule`
        * :class:`~oci.load_balancer.models.ExtendHttpRequestHeaderValueRule`
        * :class:`~oci.load_balancer.models.RemoveHttpResponseHeaderRule`
        * :class:`~oci.load_balancer.models.ControlAccessUsingHttpMethodsRule`
        * :class:`~oci.load_balancer.models.AllowRule`
        * :class:`~oci.load_balancer.models.HttpHeaderRule`
        * :class:`~oci.load_balancer.models.AddHttpResponseHeaderRule`
        * :class:`~oci.load_balancer.models.ExtendHttpResponseHeaderValueRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this Rule.
            Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT", "HTTP_HEADER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        """
        self.swagger_types = {
            'action': 'str'
        }

        self.attribute_map = {
            'action': 'action'
        }

        self._action = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['action']

        if type == 'ADD_HTTP_REQUEST_HEADER':
            return 'AddHttpRequestHeaderRule'

        if type == 'REDIRECT':
            return 'RedirectRule'

        if type == 'REMOVE_HTTP_REQUEST_HEADER':
            return 'RemoveHttpRequestHeaderRule'

        if type == 'EXTEND_HTTP_REQUEST_HEADER_VALUE':
            return 'ExtendHttpRequestHeaderValueRule'

        if type == 'REMOVE_HTTP_RESPONSE_HEADER':
            return 'RemoveHttpResponseHeaderRule'

        if type == 'CONTROL_ACCESS_USING_HTTP_METHODS':
            return 'ControlAccessUsingHttpMethodsRule'

        if type == 'ALLOW':
            return 'AllowRule'

        if type == 'HTTP_HEADER':
            return 'HttpHeaderRule'

        if type == 'ADD_HTTP_RESPONSE_HEADER':
            return 'AddHttpResponseHeaderRule'

        if type == 'EXTEND_HTTP_RESPONSE_HEADER_VALUE':
            return 'ExtendHttpResponseHeaderValueRule'
        else:
            return 'Rule'

    @property
    def action(self):
        """
        **[Required]** Gets the action of this Rule.
        Allowed values for this property are: "ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT", "HTTP_HEADER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this Rule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Rule.

        :param action: The action of this Rule.
        :type: str
        """
        allowed_values = ["ADD_HTTP_REQUEST_HEADER", "EXTEND_HTTP_REQUEST_HEADER_VALUE", "REMOVE_HTTP_REQUEST_HEADER", "ADD_HTTP_RESPONSE_HEADER", "EXTEND_HTTP_RESPONSE_HEADER_VALUE", "REMOVE_HTTP_RESPONSE_HEADER", "ALLOW", "CONTROL_ACCESS_USING_HTTP_METHODS", "REDIRECT", "HTTP_HEADER"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
