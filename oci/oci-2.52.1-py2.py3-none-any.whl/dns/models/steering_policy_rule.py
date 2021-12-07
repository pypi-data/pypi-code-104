# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyRule(object):
    """
    The configuration of the sorting and filtering behaviors in a steering policy. Rules can
    filter and sort answers based on weight, priority, endpoint health, and other data.


    A rule may optionally include a sequence of cases, each with an optional `caseCondition`
    expression. Cases allow a sequence of conditions to be defined that will apply different
    parameters to the rule when the conditions are met. For more information about cases,
    see `Traffic Management API Guide`__.


    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm
    """

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "FILTER"
    RULE_TYPE_FILTER = "FILTER"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "HEALTH"
    RULE_TYPE_HEALTH = "HEALTH"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "WEIGHTED"
    RULE_TYPE_WEIGHTED = "WEIGHTED"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "PRIORITY"
    RULE_TYPE_PRIORITY = "PRIORITY"

    #: A constant which can be used with the rule_type property of a SteeringPolicyRule.
    #: This constant has a value of "LIMIT"
    RULE_TYPE_LIMIT = "LIMIT"

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.dns.models.SteeringPolicyFilterRule`
        * :class:`~oci.dns.models.SteeringPolicyWeightedRule`
        * :class:`~oci.dns.models.SteeringPolicyLimitRule`
        * :class:`~oci.dns.models.SteeringPolicyHealthRule`
        * :class:`~oci.dns.models.SteeringPolicyPriorityRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this SteeringPolicyRule.
        :type description: str

        :param rule_type:
            The value to assign to the rule_type property of this SteeringPolicyRule.
            Allowed values for this property are: "FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_type: str

        """
        self.swagger_types = {
            'description': 'str',
            'rule_type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'rule_type': 'ruleType'
        }

        self._description = None
        self._rule_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['ruleType']

        if type == 'FILTER':
            return 'SteeringPolicyFilterRule'

        if type == 'WEIGHTED':
            return 'SteeringPolicyWeightedRule'

        if type == 'LIMIT':
            return 'SteeringPolicyLimitRule'

        if type == 'HEALTH':
            return 'SteeringPolicyHealthRule'

        if type == 'PRIORITY':
            return 'SteeringPolicyPriorityRule'
        else:
            return 'SteeringPolicyRule'

    @property
    def description(self):
        """
        Gets the description of this SteeringPolicyRule.
        A user-defined description of the rule's purpose or behavior.


        :return: The description of this SteeringPolicyRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SteeringPolicyRule.
        A user-defined description of the rule's purpose or behavior.


        :param description: The description of this SteeringPolicyRule.
        :type: str
        """
        self._description = description

    @property
    def rule_type(self):
        """
        **[Required]** Gets the rule_type of this SteeringPolicyRule.
        The type of a rule determines its sorting/filtering behavior.
        * `FILTER` - Filters the list of answers based on their defined boolean data. Answers remain
          only if their `shouldKeep` value is `true`.


        * `HEALTH` - Removes answers from the list if their `rdata` matches a target in the
          health check monitor referenced by the steering policy and the target is reported down.


        * `WEIGHTED` - Uses a number between 0 and 255 to determine how often an answer will be served
          in relation to other answers. Anwers with a higher weight will be served more frequently.


        * `PRIORITY` - Uses a defined rank value of answers to determine which answer to serve,
          moving those with the lowest values to the beginning of the list without changing the
          relative order of those with the same value. Answers can be given a value between `0` and `255`.


        * `LIMIT` - Filters answers that are too far down the list. Parameter `defaultCount`
          specifies how many answers to keep. **Example:** If `defaultCount` has a value of `2` and
          there are five answers left, when the `LIMIT` rule is processed, only the first two answers
          will remain in the list.

        Allowed values for this property are: "FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_type of this SteeringPolicyRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this SteeringPolicyRule.
        The type of a rule determines its sorting/filtering behavior.
        * `FILTER` - Filters the list of answers based on their defined boolean data. Answers remain
          only if their `shouldKeep` value is `true`.


        * `HEALTH` - Removes answers from the list if their `rdata` matches a target in the
          health check monitor referenced by the steering policy and the target is reported down.


        * `WEIGHTED` - Uses a number between 0 and 255 to determine how often an answer will be served
          in relation to other answers. Anwers with a higher weight will be served more frequently.


        * `PRIORITY` - Uses a defined rank value of answers to determine which answer to serve,
          moving those with the lowest values to the beginning of the list without changing the
          relative order of those with the same value. Answers can be given a value between `0` and `255`.


        * `LIMIT` - Filters answers that are too far down the list. Parameter `defaultCount`
          specifies how many answers to keep. **Example:** If `defaultCount` has a value of `2` and
          there are five answers left, when the `LIMIT` rule is processed, only the first two answers
          will remain in the list.


        :param rule_type: The rule_type of this SteeringPolicyRule.
        :type: str
        """
        allowed_values = ["FILTER", "HEALTH", "WEIGHTED", "PRIORITY", "LIMIT"]
        if not value_allowed_none_or_none_sentinel(rule_type, allowed_values):
            rule_type = 'UNKNOWN_ENUM_VALUE'
        self._rule_type = rule_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
