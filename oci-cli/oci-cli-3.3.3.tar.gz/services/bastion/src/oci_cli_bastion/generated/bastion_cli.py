# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('bastion.bastion_root_group.command_name', 'bastion'), cls=CommandGroupWithAlias, help=cli_util.override('bastion.bastion_root_group.help', """Oracle Cloud Infrastructure Bastion provides restricted and time-limited access to target resources that don't have public endpoints. Through the configuration of a bastion, you can let authorized users connect from specific IP addresses to target resources by way of Secure Shell (SSH) sessions hosted on the bastion."""), short_help=cli_util.override('bastion.bastion_root_group.short_help', """Bastion API"""))
@cli_util.help_option_group
def bastion_root_group():
    pass


@click.command(cli_util.override('bastion.session_group.command_name', 'session'), cls=CommandGroupWithAlias, help="""A bastion session resource. A bastion session lets authorized users connect to a target resource using a Secure Shell (SSH) for a predetermined amount of time.""")
@cli_util.help_option_group
def session_group():
    pass


@click.command(cli_util.override('bastion.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('bastion.work_request_log_entry_group.command_name', 'work-request-log-entry'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_entry_group():
    pass


@click.command(cli_util.override('bastion.bastion_group.command_name', 'bastion'), cls=CommandGroupWithAlias, help="""A bastion resource. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a private subnet.""")
@cli_util.help_option_group
def bastion_group():
    pass


@click.command(cli_util.override('bastion.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status.""")
@cli_util.help_option_group
def work_request_group():
    pass


bastion_root_group.add_command(session_group)
bastion_root_group.add_command(work_request_error_group)
bastion_root_group.add_command(work_request_log_entry_group)
bastion_root_group.add_command(bastion_group)
bastion_root_group.add_command(work_request_group)


@bastion_group.command(name=cli_util.override('bastion.change_bastion_compartment.command_name', 'change-compartment'), help=u"""Moves a bastion into a different compartment. \n[Command Reference](changeBastionCompartment)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion.""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment that the bastion should move to.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_bastion_compartment(ctx, from_json, bastion_id, compartment_id, if_match):

    if isinstance(bastion_id, six.string_types) and len(bastion_id.strip()) == 0:
        raise click.UsageError('Parameter --bastion-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.change_bastion_compartment(
        bastion_id=bastion_id,
        change_bastion_compartment_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bastion_group.command(name=cli_util.override('bastion.create_bastion.command_name', 'create'), help=u"""Creates a new bastion. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. A bastion resides in a public subnet and establishes the network infrastructure needed to connect a user to a target resource in a private subnet. \n[Command Reference](createBastion)""")
@cli_util.option('--bastion-type', required=True, help=u"""The type of bastion. Use `standard`.""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment where the bastion is located.""")
@cli_util.option('--target-subnet-id', required=True, help=u"""The unique identifier (OCID) of the subnet that the bastion connects to.""")
@cli_util.option('--name', help=u"""The name of the bastion, which can't be changed after creation.""")
@cli_util.option('--phone-book-entry', help=u"""The phonebook entry of the customer's team, which can't be changed after creation. Not applicable to `standard` bastions.""")
@cli_util.option('--static-jump-host-ip-addresses', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--client-cidr-block-allow-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--max-session-ttl-in-seconds', type=click.INT, help=u"""The maximum amount of time that any session on the bastion can remain active.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'static-jump-host-ip-addresses': {'module': 'bastion', 'class': 'list[string]'}, 'client-cidr-block-allow-list': {'module': 'bastion', 'class': 'list[string]'}, 'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'static-jump-host-ip-addresses': {'module': 'bastion', 'class': 'list[string]'}, 'client-cidr-block-allow-list': {'module': 'bastion', 'class': 'list[string]'}, 'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'bastion', 'class': 'Bastion'})
@cli_util.wrap_exceptions
def create_bastion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bastion_type, compartment_id, target_subnet_id, name, phone_book_entry, static_jump_host_ip_addresses, client_cidr_block_allow_list, max_session_ttl_in_seconds, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['bastionType'] = bastion_type
    _details['compartmentId'] = compartment_id
    _details['targetSubnetId'] = target_subnet_id

    if name is not None:
        _details['name'] = name

    if phone_book_entry is not None:
        _details['phoneBookEntry'] = phone_book_entry

    if static_jump_host_ip_addresses is not None:
        _details['staticJumpHostIpAddresses'] = cli_util.parse_json_parameter("static_jump_host_ip_addresses", static_jump_host_ip_addresses)

    if client_cidr_block_allow_list is not None:
        _details['clientCidrBlockAllowList'] = cli_util.parse_json_parameter("client_cidr_block_allow_list", client_cidr_block_allow_list)

    if max_session_ttl_in_seconds is not None:
        _details['maxSessionTtlInSeconds'] = max_session_ttl_in_seconds

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.create_bastion(
        create_bastion_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@session_group.command(name=cli_util.override('bastion.create_session.command_name', 'create'), help=u"""Creates a new session in a bastion. A bastion session lets authorized users connect to a target resource for a predetermined amount of time. The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running. \n[Command Reference](createSession)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion on which to create this session.""")
@cli_util.option('--target-resource-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--key-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name of the session.""")
@cli_util.option('--key-type', type=custom_types.CliCaseInsensitiveChoice(["PUB"]), help=u"""The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.""")
@cli_util.option('--session-ttl-in-seconds', type=click.INT, help=u"""The amount of time the session can remain active.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'target-resource-details': {'module': 'bastion', 'class': 'CreateSessionTargetResourceDetails'}, 'key-details': {'module': 'bastion', 'class': 'PublicKeyDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'target-resource-details': {'module': 'bastion', 'class': 'CreateSessionTargetResourceDetails'}, 'key-details': {'module': 'bastion', 'class': 'PublicKeyDetails'}}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def create_session(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bastion_id, target_resource_details, key_details, display_name, key_type, session_ttl_in_seconds):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['bastionId'] = bastion_id
    _details['targetResourceDetails'] = cli_util.parse_json_parameter("target_resource_details", target_resource_details)
    _details['keyDetails'] = cli_util.parse_json_parameter("key_details", key_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if key_type is not None:
        _details['keyType'] = key_type

    if session_ttl_in_seconds is not None:
        _details['sessionTtlInSeconds'] = session_ttl_in_seconds

    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.create_session(
        create_session_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@session_group.command(name=cli_util.override('bastion.create_session_create_managed_ssh_session_target_resource_details.command_name', 'create-session-create-managed-ssh-session-target-resource-details'), help=u"""Creates a new session in a bastion. A bastion session lets authorized users connect to a target resource for a predetermined amount of time. The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running. \n[Command Reference](createSession)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion on which to create this session.""")
@cli_util.option('--key-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--target-resource-details-target-resource-operating-system-user-name', required=True, help=u"""The name of the user on the target resource operating system that the session uses for the connection.""")
@cli_util.option('--target-resource-details-target-resource-id', required=True, help=u"""The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.""")
@cli_util.option('--display-name', help=u"""The name of the session.""")
@cli_util.option('--key-type', type=custom_types.CliCaseInsensitiveChoice(["PUB"]), help=u"""The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.""")
@cli_util.option('--session-ttl-in-seconds', type=click.INT, help=u"""The amount of time the session can remain active.""")
@cli_util.option('--target-resource-details-target-resource-port', type=click.INT, help=u"""The port number to connect to on the target resource.""")
@cli_util.option('--target-resource-details-target-resource-private-ip-address', help=u"""The private IP address of the target resource that the session connects to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'key-details': {'module': 'bastion', 'class': 'PublicKeyDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'key-details': {'module': 'bastion', 'class': 'PublicKeyDetails'}}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def create_session_create_managed_ssh_session_target_resource_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bastion_id, key_details, target_resource_details_target_resource_operating_system_user_name, target_resource_details_target_resource_id, display_name, key_type, session_ttl_in_seconds, target_resource_details_target_resource_port, target_resource_details_target_resource_private_ip_address):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetResourceDetails'] = {}
    _details['bastionId'] = bastion_id
    _details['keyDetails'] = cli_util.parse_json_parameter("key_details", key_details)
    _details['targetResourceDetails']['targetResourceOperatingSystemUserName'] = target_resource_details_target_resource_operating_system_user_name
    _details['targetResourceDetails']['targetResourceId'] = target_resource_details_target_resource_id

    if display_name is not None:
        _details['displayName'] = display_name

    if key_type is not None:
        _details['keyType'] = key_type

    if session_ttl_in_seconds is not None:
        _details['sessionTtlInSeconds'] = session_ttl_in_seconds

    if target_resource_details_target_resource_port is not None:
        _details['targetResourceDetails']['targetResourcePort'] = target_resource_details_target_resource_port

    if target_resource_details_target_resource_private_ip_address is not None:
        _details['targetResourceDetails']['targetResourcePrivateIpAddress'] = target_resource_details_target_resource_private_ip_address

    _details['targetResourceDetails']['sessionType'] = 'MANAGED_SSH'

    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.create_session(
        create_session_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@session_group.command(name=cli_util.override('bastion.create_session_create_port_forwarding_session_target_resource_details.command_name', 'create-session-create-port-forwarding-session-target-resource-details'), help=u"""Creates a new session in a bastion. A bastion session lets authorized users connect to a target resource for a predetermined amount of time. The Bastion service recognizes two types of sessions, managed SSH sessions and SSH port forwarding sessions. Managed SSH sessions require that the target resource has an OpenSSH server and the Oracle Cloud Agent both running. \n[Command Reference](createSession)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion on which to create this session.""")
@cli_util.option('--key-details', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""The name of the session.""")
@cli_util.option('--key-type', type=custom_types.CliCaseInsensitiveChoice(["PUB"]), help=u"""The type of the key used to connect to the session. PUB is a standard public key in OpenSSH format.""")
@cli_util.option('--session-ttl-in-seconds', type=click.INT, help=u"""The amount of time the session can remain active.""")
@cli_util.option('--target-resource-details-target-resource-port', type=click.INT, help=u"""The port number to connect to on the target resource.""")
@cli_util.option('--target-resource-details-target-resource-id', help=u"""The unique identifier (OCID) of the target resource (a Compute instance, for example) that the session connects to.""")
@cli_util.option('--target-resource-details-target-resource-private-ip-address', help=u"""The private IP address of the target resource that the session connects to.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'key-details': {'module': 'bastion', 'class': 'PublicKeyDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'key-details': {'module': 'bastion', 'class': 'PublicKeyDetails'}}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def create_session_create_port_forwarding_session_target_resource_details(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bastion_id, key_details, display_name, key_type, session_ttl_in_seconds, target_resource_details_target_resource_port, target_resource_details_target_resource_id, target_resource_details_target_resource_private_ip_address):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['targetResourceDetails'] = {}
    _details['bastionId'] = bastion_id
    _details['keyDetails'] = cli_util.parse_json_parameter("key_details", key_details)

    if display_name is not None:
        _details['displayName'] = display_name

    if key_type is not None:
        _details['keyType'] = key_type

    if session_ttl_in_seconds is not None:
        _details['sessionTtlInSeconds'] = session_ttl_in_seconds

    if target_resource_details_target_resource_port is not None:
        _details['targetResourceDetails']['targetResourcePort'] = target_resource_details_target_resource_port

    if target_resource_details_target_resource_id is not None:
        _details['targetResourceDetails']['targetResourceId'] = target_resource_details_target_resource_id

    if target_resource_details_target_resource_private_ip_address is not None:
        _details['targetResourceDetails']['targetResourcePrivateIpAddress'] = target_resource_details_target_resource_private_ip_address

    _details['targetResourceDetails']['sessionType'] = 'PORT_FORWARDING'

    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.create_session(
        create_session_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@bastion_group.command(name=cli_util.override('bastion.delete_bastion.command_name', 'delete'), help=u"""Deletes a bastion identified by the bastion ID. \n[Command Reference](deleteBastion)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_bastion(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, bastion_id, if_match):

    if isinstance(bastion_id, six.string_types) and len(bastion_id.strip()) == 0:
        raise click.UsageError('Parameter --bastion-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.delete_bastion(
        bastion_id=bastion_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@session_group.command(name=cli_util.override('bastion.delete_session.command_name', 'delete'), help=u"""Deletes a session identified by the session ID. \n[Command Reference](deleteSession)""")
@cli_util.option('--session-id', required=True, help=u"""The unique identifier (OCID) of the session.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_session(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, session_id, if_match):

    if isinstance(session_id, six.string_types) and len(session_id.strip()) == 0:
        raise click.UsageError('Parameter --session-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.delete_session(
        session_id=session_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Please retrieve the work request to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@bastion_group.command(name=cli_util.override('bastion.get_bastion.command_name', 'get'), help=u"""Retrieves a bastion identified by the bastion ID. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. \n[Command Reference](getBastion)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'Bastion'})
@cli_util.wrap_exceptions
def get_bastion(ctx, from_json, bastion_id):

    if isinstance(bastion_id, six.string_types) and len(bastion_id.strip()) == 0:
        raise click.UsageError('Parameter --bastion-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.get_bastion(
        bastion_id=bastion_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@session_group.command(name=cli_util.override('bastion.get_session.command_name', 'get'), help=u"""Retrieves a session identified by the session ID. A bastion session lets authorized users connect to a target resource for a predetermined amount of time. \n[Command Reference](getSession)""")
@cli_util.option('--session-id', required=True, help=u"""The unique identifier (OCID) of the session.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def get_session(ctx, from_json, session_id):

    if isinstance(session_id, six.string_types) and len(session_id.strip()) == 0:
        raise click.UsageError('Parameter --session-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.get_session(
        session_id=session_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('bastion.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given ID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The unique identifier (OCID) of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@bastion_group.command(name=cli_util.override('bastion.list_bastions.command_name', 'list'), help=u"""Retrieves a list of BastionSummary objects in a compartment. Bastions provide secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. \n[Command Reference](listBastions)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment in which to list resources.""")
@cli_util.option('--bastion-lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--bastion-id', help=u"""The unique identifier (OCID) of the bastion in which to list resources.""")
@cli_util.option('--name', help=u"""A filter to return only resources that match the entire name given.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "name"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'list[BastionSummary]'})
@cli_util.wrap_exceptions
def list_bastions(ctx, from_json, all_pages, page_size, compartment_id, bastion_lifecycle_state, bastion_id, name, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if bastion_lifecycle_state is not None:
        kwargs['bastion_lifecycle_state'] = bastion_lifecycle_state
    if bastion_id is not None:
        kwargs['bastion_id'] = bastion_id
    if name is not None:
        kwargs['name'] = name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_bastions,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_bastions,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_bastions(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@session_group.command(name=cli_util.override('bastion.list_sessions.command_name', 'list'), help=u"""Retrieves a list of SessionSummary objects for an existing bastion. Bastion sessions let authorized users connect to a target resource for a predetermined amount of time. \n[Command Reference](listSessions)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion in which to list sessions.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--session-lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--session-id', help=u"""The unique identifier (OCID) of the session in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending. If no value is specified timeCreated is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'list[SessionSummary]'})
@cli_util.wrap_exceptions
def list_sessions(ctx, from_json, all_pages, page_size, bastion_id, display_name, session_lifecycle_state, session_id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if session_lifecycle_state is not None:
        kwargs['session_lifecycle_state'] = session_lifecycle_state
    if session_id is not None:
        kwargs['session_id'] = session_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_sessions,
            bastion_id=bastion_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_sessions,
            limit,
            page_size,
            bastion_id=bastion_id,
            **kwargs
        )
    else:
        result = client.list_sessions(
            bastion_id=bastion_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('bastion.list_work_request_errors.command_name', 'list'), help=u"""Return a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The unique identifier (OCID) of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_errors,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_errors,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_errors(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_log_entry_group.command(name=cli_util.override('bastion.list_work_request_logs.command_name', 'list-work-request-logs'), help=u"""Return a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The unique identifier (OCID) of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'list[WorkRequestLogEntry]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_request_logs,
            work_request_id=work_request_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_request_logs,
            limit,
            page_size,
            work_request_id=work_request_id,
            **kwargs
        )
    else:
        result = client.list_work_request_logs(
            work_request_id=work_request_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('bastion.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The unique identifier (OCID) of the compartment in which to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'list[WorkRequestSummary]'})
@cli_util.wrap_exceptions
def list_work_requests(ctx, from_json, all_pages, page_size, compartment_id, page, limit):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('bastion', 'bastion', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_work_requests,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_work_requests,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_work_requests(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@bastion_group.command(name=cli_util.override('bastion.update_bastion.command_name', 'update'), help=u"""Updates the bastion identified by the bastion ID. A bastion provides secured, public access to target resources in the cloud that you cannot otherwise reach from the internet. \n[Command Reference](updateBastion)""")
@cli_util.option('--bastion-id', required=True, help=u"""The unique identifier (OCID) of the bastion.""")
@cli_util.option('--max-session-ttl-in-seconds', type=click.INT, help=u"""The maximum amount of time that any session on the bastion can remain active.""")
@cli_util.option('--static-jump-host-ip-addresses', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of IP addresses of the hosts that the bastion has access to. Not applicable to `standard` bastions.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--client-cidr-block-allow-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of address ranges in CIDR notation that you want to allow to connect to sessions hosted by this bastion.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'static-jump-host-ip-addresses': {'module': 'bastion', 'class': 'list[string]'}, 'client-cidr-block-allow-list': {'module': 'bastion', 'class': 'list[string]'}, 'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'static-jump-host-ip-addresses': {'module': 'bastion', 'class': 'list[string]'}, 'client-cidr-block-allow-list': {'module': 'bastion', 'class': 'list[string]'}, 'freeform-tags': {'module': 'bastion', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'bastion', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_bastion(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, bastion_id, max_session_ttl_in_seconds, static_jump_host_ip_addresses, client_cidr_block_allow_list, freeform_tags, defined_tags, if_match):

    if isinstance(bastion_id, six.string_types) and len(bastion_id.strip()) == 0:
        raise click.UsageError('Parameter --bastion-id cannot be whitespace or empty string')
    if not force:
        if static_jump_host_ip_addresses or client_cidr_block_allow_list or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to static-jump-host-ip-addresses and client-cidr-block-allow-list and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if max_session_ttl_in_seconds is not None:
        _details['maxSessionTtlInSeconds'] = max_session_ttl_in_seconds

    if static_jump_host_ip_addresses is not None:
        _details['staticJumpHostIpAddresses'] = cli_util.parse_json_parameter("static_jump_host_ip_addresses", static_jump_host_ip_addresses)

    if client_cidr_block_allow_list is not None:
        _details['clientCidrBlockAllowList'] = cli_util.parse_json_parameter("client_cidr_block_allow_list", client_cidr_block_allow_list)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.update_bastion(
        bastion_id=bastion_id,
        update_bastion_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_work_request') and callable(getattr(client, 'get_work_request')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the work request has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_work_request(result.headers['opc-work-request-id']), 'status', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the work request entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for work request to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the work request to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@session_group.command(name=cli_util.override('bastion.update_session.command_name', 'update'), help=u"""Updates the session identified by the session ID. A bastion session lets authorized users connect to a target resource for a predetermined amount of time. \n[Command Reference](updateSession)""")
@cli_util.option('--session-id', required=True, help=u"""The unique identifier (OCID) of the session.""")
@cli_util.option('--display-name', help=u"""The name of the session.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'bastion', 'class': 'Session'})
@cli_util.wrap_exceptions
def update_session(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, session_id, display_name, if_match):

    if isinstance(session_id, six.string_types) and len(session_id.strip()) == 0:
        raise click.UsageError('Parameter --session-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('bastion', 'bastion', ctx)
    result = client.update_session(
        session_id=session_id,
        update_session_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_session') and callable(getattr(client, 'get_session')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_session(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)
