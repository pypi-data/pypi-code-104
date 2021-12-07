# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 auth_token: Optional[pulumi.Input[str]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] url: Splunk instance URL
        :param pulumi.Input[str] auth_token: Authentication tokens, also known as JSON Web Tokens (JWT), are a method for authenticating Splunk platform users into
               the Splunk platform
        :param pulumi.Input[bool] insecure_skip_verify: insecure skip verification flag
        :param pulumi.Input[str] password: Splunk instance password
        :param pulumi.Input[int] timeout: Timeout when making calls to Splunk server. Defaults to 60 seconds
        :param pulumi.Input[str] username: Splunk instance admin username
        """
        pulumi.set(__self__, "url", url)
        if auth_token is not None:
            pulumi.set(__self__, "auth_token", auth_token)
        if insecure_skip_verify is not None:
            pulumi.set(__self__, "insecure_skip_verify", insecure_skip_verify)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        Splunk instance URL
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[pulumi.Input[str]]:
        """
        Authentication tokens, also known as JSON Web Tokens (JWT), are a method for authenticating Splunk platform users into
        the Splunk platform
        """
        return pulumi.get(self, "auth_token")

    @auth_token.setter
    def auth_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_token", value)

    @property
    @pulumi.getter(name="insecureSkipVerify")
    def insecure_skip_verify(self) -> Optional[pulumi.Input[bool]]:
        """
        insecure skip verification flag
        """
        return pulumi.get(self, "insecure_skip_verify")

    @insecure_skip_verify.setter
    def insecure_skip_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure_skip_verify", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Splunk instance password
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout when making calls to Splunk server. Defaults to 60 seconds
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Splunk instance admin username
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_token: Optional[pulumi.Input[str]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the splunk package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_token: Authentication tokens, also known as JSON Web Tokens (JWT), are a method for authenticating Splunk platform users into
               the Splunk platform
        :param pulumi.Input[bool] insecure_skip_verify: insecure skip verification flag
        :param pulumi.Input[str] password: Splunk instance password
        :param pulumi.Input[int] timeout: Timeout when making calls to Splunk server. Defaults to 60 seconds
        :param pulumi.Input[str] url: Splunk instance URL
        :param pulumi.Input[str] username: Splunk instance admin username
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the splunk package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_token: Optional[pulumi.Input[str]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["auth_token"] = auth_token
            __props__.__dict__["insecure_skip_verify"] = pulumi.Output.from_input(insecure_skip_verify).apply(pulumi.runtime.to_json) if insecure_skip_verify is not None else None
            __props__.__dict__["password"] = password
            __props__.__dict__["timeout"] = pulumi.Output.from_input(timeout).apply(pulumi.runtime.to_json) if timeout is not None else None
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["username"] = username
        super(Provider, __self__).__init__(
            'splunk',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> pulumi.Output[Optional[str]]:
        """
        Authentication tokens, also known as JSON Web Tokens (JWT), are a method for authenticating Splunk platform users into
        the Splunk platform
        """
        return pulumi.get(self, "auth_token")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Splunk instance password
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        Splunk instance URL
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        """
        Splunk instance admin username
        """
        return pulumi.get(self, "username")

