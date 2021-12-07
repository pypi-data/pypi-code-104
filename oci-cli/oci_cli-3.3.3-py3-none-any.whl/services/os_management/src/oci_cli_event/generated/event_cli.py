# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.os_management.src.oci_cli_os_management.generated import os_management_service_cli


@click.command(cli_util.override('event.event_root_group.command_name', 'event'), cls=CommandGroupWithAlias, help=cli_util.override('event.event_root_group.help', """API for the OS Management service. Use these API operations for working
with Managed instances and Managed instance groups."""), short_help=cli_util.override('event.event_root_group.short_help', """OS Management API"""))
@cli_util.help_option_group
def event_root_group():
    pass


@click.command(cli_util.override('event.related_event_collection_group.command_name', 'related-event-collection'), cls=CommandGroupWithAlias, help="""Results of a event occurence search. Contains RelatedEventSummary.""")
@cli_util.help_option_group
def related_event_collection_group():
    pass


@click.command(cli_util.override('event.event_content_group.command_name', 'event-content'), cls=CommandGroupWithAlias, help="""Information about the data collected as a ZIP file when the event occurred.""")
@cli_util.help_option_group
def event_content_group():
    pass


@click.command(cli_util.override('event.event_collection_group.command_name', 'event-collection'), cls=CommandGroupWithAlias, help="""Results of a event search. Contains both EventSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def event_collection_group():
    pass


@click.command(cli_util.override('event.event_group.command_name', 'event'), cls=CommandGroupWithAlias, help="""Description of Event.""")
@cli_util.help_option_group
def event_group():
    pass


@click.command(cli_util.override('event.event_report_group.command_name', 'event-report'), cls=CommandGroupWithAlias, help="""Summary about event occurrences on a system.""")
@cli_util.help_option_group
def event_report_group():
    pass


@click.command(cli_util.override('event.binary_group.command_name', 'binary'), cls=CommandGroupWithAlias, help="""""")
@cli_util.help_option_group
def binary_group():
    pass


os_management_service_cli.os_management_service_group.add_command(event_root_group)
event_root_group.add_command(related_event_collection_group)
event_root_group.add_command(event_content_group)
event_root_group.add_command(event_collection_group)
event_root_group.add_command(event_group)
event_root_group.add_command(event_report_group)
event_root_group.add_command(binary_group)


@event_content_group.command(name=cli_util.override('event.delete_event_content.command_name', 'delete'), help=u"""Delete an event content ZIP archive from the service \n[Command Reference](deleteEventContent)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""Instance Oracle Cloud identifier (ocid)""")
@cli_util.option('--event-id', required=True, help=u"""Unique Event identifier (OCID)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_event_content(ctx, from_json, managed_instance_id, event_id, compartment_id, if_match):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'event', ctx)
    result = client.delete_event_content(
        managed_instance_id=managed_instance_id,
        event_id=event_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@event_group.command(name=cli_util.override('event.get_event.command_name', 'get'), help=u"""Gets an Event by identifier \n[Command Reference](getEvent)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""Instance Oracle Cloud identifier (ocid)""")
@cli_util.option('--event-id', required=True, help=u"""Unique Event identifier (OCID)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'Event'})
@cli_util.wrap_exceptions
def get_event(ctx, from_json, managed_instance_id, event_id, compartment_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'event', ctx)
    result = client.get_event(
        managed_instance_id=managed_instance_id,
        event_id=event_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@binary_group.command(name=cli_util.override('event.get_event_content.command_name', 'get-event-content'), help=u"""Get additional data about a event as a ZIP archive. The archive content depends on the event eventType. \n[Command Reference](getEventContent)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""Instance Oracle Cloud identifier (ocid)""")
@cli_util.option('--event-id', required=True, help=u"""Unique Event identifier (OCID)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def get_event_content(ctx, from_json, file, managed_instance_id, event_id, compartment_id):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'event', ctx)
    result = client.get_event_content(
        managed_instance_id=managed_instance_id,
        event_id=event_id,
        compartment_id=compartment_id,
        **kwargs
    )

    # If outputting to stdout we don't want to print a progress bar because it will get mixed up with the output
    # Also we need a non-zero Content-Length in order to display a meaningful progress bar
    bar = None
    if hasattr(file, 'name') and file.name != '<stdout>' and 'Content-Length' in result.headers:
        content_length = int(result.headers['Content-Length'])
        if content_length > 0:
            bar = click.progressbar(length=content_length, label='Downloading file')

    try:
        if bar:
            bar.__enter__()

        # TODO: Make the download size a configurable option
        # use decode_content=True to automatically unzip service responses (this should be overridden for object storage)
        for chunk in result.data.raw.stream(cli_constants.MEBIBYTE, decode_content=True):
            if bar:
                bar.update(len(chunk))
            file.write(chunk)
    finally:
        if bar:
            bar.render_finish()
        file.close()


@event_report_group.command(name=cli_util.override('event.get_event_report.command_name', 'get'), help=u"""Get summary information about events on this instance. \n[Command Reference](getEventReport)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""Instance Oracle Cloud identifier (ocid)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--latest-timestamp-less-than', type=custom_types.CLI_DATETIME, help=u"""filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--latest-timestamp-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'EventReport'})
@cli_util.wrap_exceptions
def get_event_report(ctx, from_json, managed_instance_id, compartment_id, latest_timestamp_less_than, latest_timestamp_greater_than_or_equal_to):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if latest_timestamp_less_than is not None:
        kwargs['latest_timestamp_less_than'] = latest_timestamp_less_than
    if latest_timestamp_greater_than_or_equal_to is not None:
        kwargs['latest_timestamp_greater_than_or_equal_to'] = latest_timestamp_greater_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'event', ctx)
    result = client.get_event_report(
        managed_instance_id=managed_instance_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@event_collection_group.command(name=cli_util.override('event.list_events.command_name', 'list-events'), help=u"""Returns a list of Events. \n[Command Reference](listEvents)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""Instance Oracle Cloud identifier (ocid)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--event-id', help=u"""Unique event identifier (OCID)""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--event-type', type=custom_types.CliCaseInsensitiveChoice(["KERNEL_OOPS", "KERNEL_CRASH", "CRASH", "EXPLOIT_ATTEMPT", "COMPLIANCE", "TUNING_SUGGESTION", "TUNING_APPLIED", "SECURITY", "ERROR", "WARNING"]), help=u"""A filter to return only event of given type.""")
@cli_util.option('--latest-timestamp-less-than', type=custom_types.CLI_DATETIME, help=u"""filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--latest-timestamp-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'EventCollection'})
@cli_util.wrap_exceptions
def list_events(ctx, from_json, all_pages, page_size, managed_instance_id, compartment_id, event_id, limit, page, sort_order, sort_by, event_type, latest_timestamp_less_than, latest_timestamp_greater_than_or_equal_to):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    kwargs = {}
    if event_id is not None:
        kwargs['event_id'] = event_id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if event_type is not None:
        kwargs['event_type'] = event_type
    if latest_timestamp_less_than is not None:
        kwargs['latest_timestamp_less_than'] = latest_timestamp_less_than
    if latest_timestamp_greater_than_or_equal_to is not None:
        kwargs['latest_timestamp_greater_than_or_equal_to'] = latest_timestamp_greater_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'event', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_events,
            managed_instance_id=managed_instance_id,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_events,
            limit,
            page_size,
            managed_instance_id=managed_instance_id,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_events(
            managed_instance_id=managed_instance_id,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@related_event_collection_group.command(name=cli_util.override('event.list_related_events.command_name', 'list-related-events'), help=u"""Returns a list of related events. For now pagination is not implemented. \n[Command Reference](listRelatedEvents)""")
@cli_util.option('--event-fingerprint', required=True, help=u"""Event fingerprint identifier""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["instanceId", "id", "eventFingerprint"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for id is descending.""")
@cli_util.option('--latest-timestamp-less-than', type=custom_types.CLI_DATETIME, help=u"""filter event occurrence. Selecting only those last occurred before given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--latest-timestamp-greater-than-or-equal-to', type=custom_types.CLI_DATETIME, help=u"""filter event occurrence. Selecting only those last occurred on or after given date in ISO 8601 format Example: 2017-07-14T02:40:00.000Z""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'os_management', 'class': 'RelatedEventCollection'})
@cli_util.wrap_exceptions
def list_related_events(ctx, from_json, all_pages, page_size, event_fingerprint, compartment_id, limit, page, sort_order, sort_by, latest_timestamp_less_than, latest_timestamp_greater_than_or_equal_to):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if latest_timestamp_less_than is not None:
        kwargs['latest_timestamp_less_than'] = latest_timestamp_less_than
    if latest_timestamp_greater_than_or_equal_to is not None:
        kwargs['latest_timestamp_greater_than_or_equal_to'] = latest_timestamp_greater_than_or_equal_to
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'event', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_related_events,
            event_fingerprint=event_fingerprint,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_related_events,
            limit,
            page_size,
            event_fingerprint=event_fingerprint,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_related_events(
            event_fingerprint=event_fingerprint,
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@event_group.command(name=cli_util.override('event.update_event.command_name', 'update'), help=u"""Updates an existing event associated to a managed instance \n[Command Reference](updateEvent)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""Instance Oracle Cloud identifier (ocid)""")
@cli_util.option('--event-id', required=True, help=u"""Unique Event identifier (OCID)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'os_management', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'os_management', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'os_management', 'class': 'Event'})
@cli_util.wrap_exceptions
def update_event(ctx, from_json, force, managed_instance_id, event_id, compartment_id, freeform_tags, defined_tags, if_match):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('os_management', 'event', ctx)
    result = client.update_event(
        managed_instance_id=managed_instance_id,
        event_id=event_id,
        compartment_id=compartment_id,
        update_event_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@event_content_group.command(name=cli_util.override('event.upload_event_content.command_name', 'upload'), help=u"""Upload the event content as a ZIP archive from the managed instance to the service \n[Command Reference](uploadEventContent)""")
@cli_util.option('--managed-instance-id', required=True, help=u"""Instance Oracle Cloud identifier (ocid)""")
@cli_util.option('--event-id', required=True, help=u"""Unique Event identifier (OCID)""")
@cli_util.option('--compartment-id', required=True, help=u"""The ID of the compartment in which to list resources.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def upload_event_content(ctx, from_json, managed_instance_id, event_id, compartment_id, if_match):

    if isinstance(managed_instance_id, six.string_types) and len(managed_instance_id.strip()) == 0:
        raise click.UsageError('Parameter --managed-instance-id cannot be whitespace or empty string')

    if isinstance(event_id, six.string_types) and len(event_id.strip()) == 0:
        raise click.UsageError('Parameter --event-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('os_management', 'event', ctx)
    result = client.upload_event_content(
        managed_instance_id=managed_instance_id,
        event_id=event_id,
        compartment_id=compartment_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)
