# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from printnanny_api_client.configuration import Configuration


class PatchedOctoPrintDeviceRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'model': 'str',
        'platform': 'str',
        'cpu_flags': 'list[str]',
        'hardware': 'str',
        'revision': 'str',
        'serial': 'str',
        'cores': 'int',
        'ram': 'int',
        'python_version': 'str',
        'pip_version': 'str',
        'virtualenv': 'str',
        'octoprint_version': 'str',
        'plugin_version': 'str',
        'print_nanny_client_version': 'str',
        'active_session': 'PrintSessionRequest'
    }

    attribute_map = {
        'name': 'name',
        'model': 'model',
        'platform': 'platform',
        'cpu_flags': 'cpu_flags',
        'hardware': 'hardware',
        'revision': 'revision',
        'serial': 'serial',
        'cores': 'cores',
        'ram': 'ram',
        'python_version': 'python_version',
        'pip_version': 'pip_version',
        'virtualenv': 'virtualenv',
        'octoprint_version': 'octoprint_version',
        'plugin_version': 'plugin_version',
        'print_nanny_client_version': 'print_nanny_client_version',
        'active_session': 'active_session'
    }

    def __init__(self, name=None, model=None, platform=None, cpu_flags=None, hardware=None, revision=None, serial=None, cores=None, ram=None, python_version=None, pip_version=None, virtualenv=None, octoprint_version=None, plugin_version=None, print_nanny_client_version=None, active_session=None, local_vars_configuration=None):  # noqa: E501
        """PatchedOctoPrintDeviceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._model = None
        self._platform = None
        self._cpu_flags = None
        self._hardware = None
        self._revision = None
        self._serial = None
        self._cores = None
        self._ram = None
        self._python_version = None
        self._pip_version = None
        self._virtualenv = None
        self._octoprint_version = None
        self._plugin_version = None
        self._print_nanny_client_version = None
        self._active_session = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if model is not None:
            self.model = model
        if platform is not None:
            self.platform = platform
        self.cpu_flags = cpu_flags
        self.hardware = hardware
        self.revision = revision
        if serial is not None:
            self.serial = serial
        if cores is not None:
            self.cores = cores
        if ram is not None:
            self.ram = ram
        if python_version is not None:
            self.python_version = python_version
        if pip_version is not None:
            self.pip_version = pip_version
        self.virtualenv = virtualenv
        if octoprint_version is not None:
            self.octoprint_version = octoprint_version
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if print_nanny_client_version is not None:
            self.print_nanny_client_version = print_nanny_client_version
        if active_session is not None:
            self.active_session = active_session

    @property
    def name(self):
        """Gets the name of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The name of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedOctoPrintDeviceRequest.


        :param name: The name of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def model(self):
        """Gets the model of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The model of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PatchedOctoPrintDeviceRequest.


        :param model: The model of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type model: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) < 1):
            raise ValueError("Invalid value for `model`, length must be greater than or equal to `1`")  # noqa: E501

        self._model = model

    @property
    def platform(self):
        """Gets the platform of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The platform of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PatchedOctoPrintDeviceRequest.


        :param platform: The platform of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type platform: str
        """
        if (self.local_vars_configuration.client_side_validation and
                platform is not None and len(platform) > 255):
            raise ValueError("Invalid value for `platform`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                platform is not None and len(platform) < 1):
            raise ValueError("Invalid value for `platform`, length must be greater than or equal to `1`")  # noqa: E501

        self._platform = platform

    @property
    def cpu_flags(self):
        """Gets the cpu_flags of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The cpu_flags of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._cpu_flags

    @cpu_flags.setter
    def cpu_flags(self, cpu_flags):
        """Sets the cpu_flags of this PatchedOctoPrintDeviceRequest.


        :param cpu_flags: The cpu_flags of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type cpu_flags: list[str]
        """

        self._cpu_flags = cpu_flags

    @property
    def hardware(self):
        """Gets the hardware of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The hardware of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this PatchedOctoPrintDeviceRequest.


        :param hardware: The hardware of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type hardware: str
        """
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) > 255):
            raise ValueError("Invalid value for `hardware`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                hardware is not None and len(hardware) < 1):
            raise ValueError("Invalid value for `hardware`, length must be greater than or equal to `1`")  # noqa: E501

        self._hardware = hardware

    @property
    def revision(self):
        """Gets the revision of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The revision of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PatchedOctoPrintDeviceRequest.


        :param revision: The revision of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type revision: str
        """
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) > 255):
            raise ValueError("Invalid value for `revision`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                revision is not None and len(revision) < 1):
            raise ValueError("Invalid value for `revision`, length must be greater than or equal to `1`")  # noqa: E501

        self._revision = revision

    @property
    def serial(self):
        """Gets the serial of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The serial of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this PatchedOctoPrintDeviceRequest.


        :param serial: The serial of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type serial: str
        """
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) > 255):
            raise ValueError("Invalid value for `serial`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                serial is not None and len(serial) < 1):
            raise ValueError("Invalid value for `serial`, length must be greater than or equal to `1`")  # noqa: E501

        self._serial = serial

    @property
    def cores(self):
        """Gets the cores of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The cores of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this PatchedOctoPrintDeviceRequest.


        :param cores: The cores of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type cores: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._cores = cores

    @property
    def ram(self):
        """Gets the ram of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The ram of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this PatchedOctoPrintDeviceRequest.


        :param ram: The ram of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type ram: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._ram = ram

    @property
    def python_version(self):
        """Gets the python_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The python_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._python_version

    @python_version.setter
    def python_version(self, python_version):
        """Sets the python_version of this PatchedOctoPrintDeviceRequest.


        :param python_version: The python_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type python_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                python_version is not None and len(python_version) > 255):
            raise ValueError("Invalid value for `python_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                python_version is not None and len(python_version) < 1):
            raise ValueError("Invalid value for `python_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._python_version = python_version

    @property
    def pip_version(self):
        """Gets the pip_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The pip_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._pip_version

    @pip_version.setter
    def pip_version(self, pip_version):
        """Sets the pip_version of this PatchedOctoPrintDeviceRequest.


        :param pip_version: The pip_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type pip_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pip_version is not None and len(pip_version) > 255):
            raise ValueError("Invalid value for `pip_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pip_version is not None and len(pip_version) < 1):
            raise ValueError("Invalid value for `pip_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._pip_version = pip_version

    @property
    def virtualenv(self):
        """Gets the virtualenv of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The virtualenv of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtualenv

    @virtualenv.setter
    def virtualenv(self, virtualenv):
        """Sets the virtualenv of this PatchedOctoPrintDeviceRequest.


        :param virtualenv: The virtualenv of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type virtualenv: str
        """
        if (self.local_vars_configuration.client_side_validation and
                virtualenv is not None and len(virtualenv) > 255):
            raise ValueError("Invalid value for `virtualenv`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                virtualenv is not None and len(virtualenv) < 1):
            raise ValueError("Invalid value for `virtualenv`, length must be greater than or equal to `1`")  # noqa: E501

        self._virtualenv = virtualenv

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The octoprint_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this PatchedOctoPrintDeviceRequest.


        :param octoprint_version: The octoprint_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type octoprint_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 255):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) < 1):
            raise ValueError("Invalid value for `octoprint_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def plugin_version(self):
        """Gets the plugin_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The plugin_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this PatchedOctoPrintDeviceRequest.


        :param plugin_version: The plugin_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type plugin_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                plugin_version is not None and len(plugin_version) > 255):
            raise ValueError("Invalid value for `plugin_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plugin_version is not None and len(plugin_version) < 1):
            raise ValueError("Invalid value for `plugin_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._plugin_version = plugin_version

    @property
    def print_nanny_client_version(self):
        """Gets the print_nanny_client_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The print_nanny_client_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_client_version

    @print_nanny_client_version.setter
    def print_nanny_client_version(self, print_nanny_client_version):
        """Sets the print_nanny_client_version of this PatchedOctoPrintDeviceRequest.


        :param print_nanny_client_version: The print_nanny_client_version of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type print_nanny_client_version: str
        """
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) > 255):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) < 1):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._print_nanny_client_version = print_nanny_client_version

    @property
    def active_session(self):
        """Gets the active_session of this PatchedOctoPrintDeviceRequest.  # noqa: E501


        :return: The active_session of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :rtype: PrintSessionRequest
        """
        return self._active_session

    @active_session.setter
    def active_session(self, active_session):
        """Sets the active_session of this PatchedOctoPrintDeviceRequest.


        :param active_session: The active_session of this PatchedOctoPrintDeviceRequest.  # noqa: E501
        :type active_session: PrintSessionRequest
        """

        self._active_session = active_session

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchedOctoPrintDeviceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedOctoPrintDeviceRequest):
            return True

        return self.to_dict() != other.to_dict()
