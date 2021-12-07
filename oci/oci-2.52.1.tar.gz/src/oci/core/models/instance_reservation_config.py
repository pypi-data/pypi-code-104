# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceReservationConfig(object):
    """
    Data that defines the capacity configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceReservationConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fault_domain:
            The value to assign to the fault_domain property of this InstanceReservationConfig.
        :type fault_domain: str

        :param instance_shape:
            The value to assign to the instance_shape property of this InstanceReservationConfig.
        :type instance_shape: str

        :param instance_shape_config:
            The value to assign to the instance_shape_config property of this InstanceReservationConfig.
        :type instance_shape_config: oci.core.models.InstanceReservationShapeConfigDetails

        :param reserved_count:
            The value to assign to the reserved_count property of this InstanceReservationConfig.
        :type reserved_count: int

        :param used_count:
            The value to assign to the used_count property of this InstanceReservationConfig.
        :type used_count: int

        """
        self.swagger_types = {
            'fault_domain': 'str',
            'instance_shape': 'str',
            'instance_shape_config': 'InstanceReservationShapeConfigDetails',
            'reserved_count': 'int',
            'used_count': 'int'
        }

        self.attribute_map = {
            'fault_domain': 'faultDomain',
            'instance_shape': 'instanceShape',
            'instance_shape_config': 'instanceShapeConfig',
            'reserved_count': 'reservedCount',
            'used_count': 'usedCount'
        }

        self._fault_domain = None
        self._instance_shape = None
        self._instance_shape_config = None
        self._reserved_count = None
        self._used_count = None

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this InstanceReservationConfig.
        The fault domain of this capacity configuration.
        If a value is not supplied, this capacity configuration is applicable to all fault domains in the specified availability domain.
        For more information, see `Capacity Reservations`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm


        :return: The fault_domain of this InstanceReservationConfig.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this InstanceReservationConfig.
        The fault domain of this capacity configuration.
        If a value is not supplied, this capacity configuration is applicable to all fault domains in the specified availability domain.
        For more information, see `Capacity Reservations`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/reserve-capacity.htm


        :param fault_domain: The fault_domain of this InstanceReservationConfig.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def instance_shape(self):
        """
        **[Required]** Gets the instance_shape of this InstanceReservationConfig.
        The shape to use when launching instances using compute capacity reservations. The shape determines the number of CPUs, the amount of memory,
        and other resources allocated to the instance.
        You can list all available shapes by calling :class:`ListComputeCapacityReservationInstanceShapes`.


        :return: The instance_shape of this InstanceReservationConfig.
        :rtype: str
        """
        return self._instance_shape

    @instance_shape.setter
    def instance_shape(self, instance_shape):
        """
        Sets the instance_shape of this InstanceReservationConfig.
        The shape to use when launching instances using compute capacity reservations. The shape determines the number of CPUs, the amount of memory,
        and other resources allocated to the instance.
        You can list all available shapes by calling :class:`ListComputeCapacityReservationInstanceShapes`.


        :param instance_shape: The instance_shape of this InstanceReservationConfig.
        :type: str
        """
        self._instance_shape = instance_shape

    @property
    def instance_shape_config(self):
        """
        Gets the instance_shape_config of this InstanceReservationConfig.

        :return: The instance_shape_config of this InstanceReservationConfig.
        :rtype: oci.core.models.InstanceReservationShapeConfigDetails
        """
        return self._instance_shape_config

    @instance_shape_config.setter
    def instance_shape_config(self, instance_shape_config):
        """
        Sets the instance_shape_config of this InstanceReservationConfig.

        :param instance_shape_config: The instance_shape_config of this InstanceReservationConfig.
        :type: oci.core.models.InstanceReservationShapeConfigDetails
        """
        self._instance_shape_config = instance_shape_config

    @property
    def reserved_count(self):
        """
        **[Required]** Gets the reserved_count of this InstanceReservationConfig.
        The total number of instances that can be launched from the capacity configuration.


        :return: The reserved_count of this InstanceReservationConfig.
        :rtype: int
        """
        return self._reserved_count

    @reserved_count.setter
    def reserved_count(self, reserved_count):
        """
        Sets the reserved_count of this InstanceReservationConfig.
        The total number of instances that can be launched from the capacity configuration.


        :param reserved_count: The reserved_count of this InstanceReservationConfig.
        :type: int
        """
        self._reserved_count = reserved_count

    @property
    def used_count(self):
        """
        **[Required]** Gets the used_count of this InstanceReservationConfig.
        The amount of capacity in use out of the total capacity reserved in this capacity configuration.


        :return: The used_count of this InstanceReservationConfig.
        :rtype: int
        """
        return self._used_count

    @used_count.setter
    def used_count(self, used_count):
        """
        Sets the used_count of this InstanceReservationConfig.
        The amount of capacity in use out of the total capacity reserved in this capacity configuration.


        :param used_count: The used_count of this InstanceReservationConfig.
        :type: int
        """
        self._used_count = used_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
