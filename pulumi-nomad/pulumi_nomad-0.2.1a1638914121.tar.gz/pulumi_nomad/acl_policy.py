# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AclPolicyArgs', 'AclPolicy']

@pulumi.input_type
class AclPolicyArgs:
    def __init__(__self__, *,
                 rules_hcl: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AclPolicy resource.
        :param pulumi.Input[str] rules_hcl: `(string: <required>)` - The contents of the policy to register,
               as HCL or JSON.
        :param pulumi.Input[str] description: `(string: "")` - A description of the policy.
        :param pulumi.Input[str] name: `(string: <required>)` - A unique name for the policy.
        """
        pulumi.set(__self__, "rules_hcl", rules_hcl)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="rulesHcl")
    def rules_hcl(self) -> pulumi.Input[str]:
        """
        `(string: <required>)` - The contents of the policy to register,
        as HCL or JSON.
        """
        return pulumi.get(self, "rules_hcl")

    @rules_hcl.setter
    def rules_hcl(self, value: pulumi.Input[str]):
        pulumi.set(self, "rules_hcl", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: "")` - A description of the policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: <required>)` - A unique name for the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _AclPolicyState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules_hcl: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AclPolicy resources.
        :param pulumi.Input[str] description: `(string: "")` - A description of the policy.
        :param pulumi.Input[str] name: `(string: <required>)` - A unique name for the policy.
        :param pulumi.Input[str] rules_hcl: `(string: <required>)` - The contents of the policy to register,
               as HCL or JSON.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rules_hcl is not None:
            pulumi.set(__self__, "rules_hcl", rules_hcl)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: "")` - A description of the policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: <required>)` - A unique name for the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="rulesHcl")
    def rules_hcl(self) -> Optional[pulumi.Input[str]]:
        """
        `(string: <required>)` - The contents of the policy to register,
        as HCL or JSON.
        """
        return pulumi.get(self, "rules_hcl")

    @rules_hcl.setter
    def rules_hcl(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rules_hcl", value)


class AclPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules_hcl: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages an ACL policy registered in Nomad.

        ## Example Usage

        Registering a policy from a HCL file:

        ```python
        import pulumi
        import pulumi_nomad as nomad

        dev = nomad.AclPolicy("dev",
            description="Submit jobs to the dev environment.",
            rules_hcl=(lambda path: open(path).read())(f"{path['module']}/dev.hcl"))
        ```

        Registering a policy from inline HCL:

        ```python
        import pulumi
        import pulumi_nomad as nomad

        dev = nomad.AclPolicy("dev",
            description="Submit jobs to the dev environment.",
            rules_hcl=\"\"\"namespace "dev" {
          policy = "write"
        }

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: `(string: "")` - A description of the policy.
        :param pulumi.Input[str] name: `(string: <required>)` - A unique name for the policy.
        :param pulumi.Input[str] rules_hcl: `(string: <required>)` - The contents of the policy to register,
               as HCL or JSON.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AclPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an ACL policy registered in Nomad.

        ## Example Usage

        Registering a policy from a HCL file:

        ```python
        import pulumi
        import pulumi_nomad as nomad

        dev = nomad.AclPolicy("dev",
            description="Submit jobs to the dev environment.",
            rules_hcl=(lambda path: open(path).read())(f"{path['module']}/dev.hcl"))
        ```

        Registering a policy from inline HCL:

        ```python
        import pulumi
        import pulumi_nomad as nomad

        dev = nomad.AclPolicy("dev",
            description="Submit jobs to the dev environment.",
            rules_hcl=\"\"\"namespace "dev" {
          policy = "write"
        }

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param AclPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AclPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules_hcl: Optional[pulumi.Input[str]] = None,
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
            __props__ = AclPolicyArgs.__new__(AclPolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if rules_hcl is None and not opts.urn:
                raise TypeError("Missing required property 'rules_hcl'")
            __props__.__dict__["rules_hcl"] = rules_hcl
        super(AclPolicy, __self__).__init__(
            'nomad:index/aclPolicy:AclPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rules_hcl: Optional[pulumi.Input[str]] = None) -> 'AclPolicy':
        """
        Get an existing AclPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: `(string: "")` - A description of the policy.
        :param pulumi.Input[str] name: `(string: <required>)` - A unique name for the policy.
        :param pulumi.Input[str] rules_hcl: `(string: <required>)` - The contents of the policy to register,
               as HCL or JSON.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AclPolicyState.__new__(_AclPolicyState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["rules_hcl"] = rules_hcl
        return AclPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        `(string: "")` - A description of the policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        `(string: <required>)` - A unique name for the policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rulesHcl")
    def rules_hcl(self) -> pulumi.Output[str]:
        """
        `(string: <required>)` - The contents of the policy to register,
        as HCL or JSON.
        """
        return pulumi.get(self, "rules_hcl")

