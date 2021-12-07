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
    'GetKubernetesVersionResult',
    'AwaitableGetKubernetesVersionResult',
    'get_kubernetes_version',
    'get_kubernetes_version_output',
]

@pulumi.output_type
class GetKubernetesVersionResult:
    """
    A collection of values returned by getKubernetesVersion.
    """
    def __init__(__self__, filters=None, id=None, sorts=None, versions=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)
        if versions and not isinstance(versions, list):
            raise TypeError("Expected argument 'versions' to be a list")
        pulumi.set(__self__, "versions", versions)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetKubernetesVersionFilterResult']]:
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
    def sorts(self) -> Optional[Sequence['outputs.GetKubernetesVersionSortResult']]:
        """
        One or more key/direction pairs on which to sort results
        """
        return pulumi.get(self, "sorts")

    @property
    @pulumi.getter
    def versions(self) -> Sequence['outputs.GetKubernetesVersionVersionResult']:
        return pulumi.get(self, "versions")


class AwaitableGetKubernetesVersionResult(GetKubernetesVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKubernetesVersionResult(
            filters=self.filters,
            id=self.id,
            sorts=self.sorts,
            versions=self.versions)


def get_kubernetes_version(filters: Optional[Sequence[pulumi.InputType['GetKubernetesVersionFilterArgs']]] = None,
                           sorts: Optional[Sequence[pulumi.InputType['GetKubernetesVersionSortArgs']]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKubernetesVersionResult:
    """
    Provides access to the available Civo Kubernetes versions, with the ability to filter the results.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    stable = civo.get_kubernetes_version(filters=[civo.GetKubernetesVersionFilterArgs(
        key="type",
        values=["stable"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetKubernetesVersionFilterArgs']] filters: One or more key/value pairs on which to filter results
    :param Sequence[pulumi.InputType['GetKubernetesVersionSortArgs']] sorts: One or more key/direction pairs on which to sort results
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('civo:index/getKubernetesVersion:getKubernetesVersion', __args__, opts=opts, typ=GetKubernetesVersionResult).value

    return AwaitableGetKubernetesVersionResult(
        filters=__ret__.filters,
        id=__ret__.id,
        sorts=__ret__.sorts,
        versions=__ret__.versions)


@_utilities.lift_output_func(get_kubernetes_version)
def get_kubernetes_version_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetKubernetesVersionFilterArgs']]]]] = None,
                                  sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetKubernetesVersionSortArgs']]]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKubernetesVersionResult]:
    """
    Provides access to the available Civo Kubernetes versions, with the ability to filter the results.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_civo as civo

    stable = civo.get_kubernetes_version(filters=[civo.GetKubernetesVersionFilterArgs(
        key="type",
        values=["stable"],
    )])
    ```


    :param Sequence[pulumi.InputType['GetKubernetesVersionFilterArgs']] filters: One or more key/value pairs on which to filter results
    :param Sequence[pulumi.InputType['GetKubernetesVersionSortArgs']] sorts: One or more key/direction pairs on which to sort results
    """
    ...
