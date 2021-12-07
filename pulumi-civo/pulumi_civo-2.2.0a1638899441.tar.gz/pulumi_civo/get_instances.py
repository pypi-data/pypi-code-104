# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetInstancesResult',
    'AwaitableGetInstancesResult',
    'get_instances',
    'get_instances_output',
]

@pulumi.output_type
class GetInstancesResult:
    """
    A collection of values returned by getInstances.
    """
    def __init__(__self__, filters=None, id=None, instances=None, region=None, sorts=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetInstancesFilterResult']]:
        """
        One or more key/value pairs on which to filter results
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def instances(self) -> Sequence['outputs.GetInstancesInstanceResult']:
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        If used, all instances will be from the provided region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetInstancesSortResult']]:
        """
        One or more key/direction pairs on which to sort results
        """
        return pulumi.get(self, "sorts")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            filters=self.filters,
            id=self.id,
            instances=self.instances,
            region=self.region,
            sorts=self.sorts)


def get_instances(filters: Optional[Sequence[pulumi.InputType['GetInstancesFilterArgs']]] = None,
                  region: Optional[str] = None,
                  sorts: Optional[Sequence[pulumi.InputType['GetInstancesSortArgs']]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    Get information on instances for use in other resources, with the ability to filter and sort the results. If no filters are specified, all instances will be returned.

    Note: You can use the `Instance` data source to obtain metadata about a single instance if you already know the id, unique hostname, or unique tag to retrieve.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    small_size = civo.get_instances(region="NYC1",
        filters=[civo.GetInstancesFilterArgs(
            key="size",
            values=[g3["small"]],
        )])
    ```


    :param Sequence[pulumi.InputType['GetInstancesFilterArgs']] filters: One or more key/value pairs on which to filter results
    :param str region: If used, all instances will be from the provided region
    :param Sequence[pulumi.InputType['GetInstancesSortArgs']] sorts: One or more key/direction pairs on which to sort results
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['region'] = region
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        filters=__ret__.filters,
        id=__ret__.id,
        instances=__ret__.instances,
        region=__ret__.region,
        sorts=__ret__.sorts)


@_utilities.lift_output_func(get_instances)
def get_instances_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInstancesFilterArgs']]]]] = None,
                         region: Optional[pulumi.Input[Optional[str]]] = None,
                         sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetInstancesSortArgs']]]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInstancesResult]:
    """
    Get information on instances for use in other resources, with the ability to filter and sort the results. If no filters are specified, all instances will be returned.

    Note: You can use the `Instance` data source to obtain metadata about a single instance if you already know the id, unique hostname, or unique tag to retrieve.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    small_size = civo.get_instances(region="NYC1",
        filters=[civo.GetInstancesFilterArgs(
            key="size",
            values=[g3["small"]],
        )])
    ```


    :param Sequence[pulumi.InputType['GetInstancesFilterArgs']] filters: One or more key/value pairs on which to filter results
    :param str region: If used, all instances will be from the provided region
    :param Sequence[pulumi.InputType['GetInstancesSortArgs']] sorts: One or more key/direction pairs on which to sort results
    """
    ...
