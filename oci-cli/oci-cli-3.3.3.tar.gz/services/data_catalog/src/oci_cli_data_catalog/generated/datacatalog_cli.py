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


@cli.command(cli_util.override('data_catalog.data_catalog_root_group.command_name', 'data-catalog'), cls=CommandGroupWithAlias, help=cli_util.override('data_catalog.data_catalog_root_group.help', """Use the Data Catalog APIs to collect, organize, find, access, understand, enrich, and activate technical, business, and operational metadata.
For more information, see [Data Catalog]."""), short_help=cli_util.override('data_catalog.data_catalog_root_group.short_help', """Data Catalog API"""))
@cli_util.help_option_group
def data_catalog_root_group():
    pass


@click.command(cli_util.override('data_catalog.job_definition_collection_group.command_name', 'job-definition-collection'), cls=CommandGroupWithAlias, help="""Results of a job definition listing. Job definitions are resources that describe the scope and type of jobs (eg: harvest, profiling, sampling) that are defined by users in the system.""")
@cli_util.help_option_group
def job_definition_collection_group():
    pass


@click.command(cli_util.override('data_catalog.catalog_group.command_name', 'catalog'), cls=CommandGroupWithAlias, help="""A data catalog enables you to collect, organize, find, access, understand, enrich, and activate technical, business, and operational metadata.""")
@cli_util.help_option_group
def catalog_group():
    pass


@click.command(cli_util.override('data_catalog.term_relationship_group.command_name', 'term-relationship'), cls=CommandGroupWithAlias, help="""Full term relationship definition. Business term relationship between two terms in a business glossary.""")
@cli_util.help_option_group
def term_relationship_group():
    pass


@click.command(cli_util.override('data_catalog.folder_tag_collection_group.command_name', 'folder-tag-collection'), cls=CommandGroupWithAlias, help="""Results of a folders tag listing. Folder tags allow association of folder objects to business terms.""")
@cli_util.help_option_group
def folder_tag_collection_group():
    pass


@click.command(cli_util.override('data_catalog.pattern_group.command_name', 'pattern'), cls=CommandGroupWithAlias, help="""Pattern representation. A Pattern is defined using an expression and can be used as data selectors or filters to provide a singular view of an entity across multiple physical data artifacts.""")
@cli_util.help_option_group
def pattern_group():
    pass


@click.command(cli_util.override('data_catalog.entity_tag_collection_group.command_name', 'entity-tag-collection'), cls=CommandGroupWithAlias, help="""Results of an entity tags listing. Entity tags allow assciation of business terms with entities.""")
@cli_util.help_option_group
def entity_tag_collection_group():
    pass


@click.command(cli_util.override('data_catalog.work_request_group.command_name', 'work-request'), cls=CommandGroupWithAlias, help="""A description of workrequest status.""")
@cli_util.help_option_group
def work_request_group():
    pass


@click.command(cli_util.override('data_catalog.job_metric_group.command_name', 'job-metric'), cls=CommandGroupWithAlias, help="""A set of metrics are collected periodically to assess the state and performance characteristics of the execution instance of a job. The metrics are grouped based on their category and sub categories and aggregated based on their batch information.""")
@cli_util.help_option_group
def job_metric_group():
    pass


@click.command(cli_util.override('data_catalog.type_group.command_name', 'type'), cls=CommandGroupWithAlias, help="""Full data catalog type definition. Fully defines a type of the data catalog. All types are statically defined in the system and are immutable. It isn't possible to create new types or update existing types via the API.""")
@cli_util.help_option_group
def type_group():
    pass


@click.command(cli_util.override('data_catalog.folder_collection_group.command_name', 'folder-collection'), cls=CommandGroupWithAlias, help="""Results of a folders listing. Folders are external organization concept that groups data entities.""")
@cli_util.help_option_group
def folder_collection_group():
    pass


@click.command(cli_util.override('data_catalog.data_asset_collection_group.command_name', 'data-asset-collection'), cls=CommandGroupWithAlias, help="""Results of a data assets listing. A data asset is often synonymous with a 'System', such as a database, or may be a file container or a message stream.""")
@cli_util.help_option_group
def data_asset_collection_group():
    pass


@click.command(cli_util.override('data_catalog.rule_summary_group.command_name', 'rule-summary'), cls=CommandGroupWithAlias, help="""A list of rule resources. One or more rules can be defined for a data entity. Each rule can be defined on one or more attributes of the data entity.""")
@cli_util.help_option_group
def rule_summary_group():
    pass


@click.command(cli_util.override('data_catalog.custom_property_group.command_name', 'custom-property'), cls=CommandGroupWithAlias, help="""Custom Property Definition""")
@cli_util.help_option_group
def custom_property_group():
    pass


@click.command(cli_util.override('data_catalog.work_request_log_group.command_name', 'work-request-log'), cls=CommandGroupWithAlias, help="""A log message from the execution of a work request.""")
@cli_util.help_option_group
def work_request_log_group():
    pass


@click.command(cli_util.override('data_catalog.attribute_tag_group.command_name', 'attribute-tag'), cls=CommandGroupWithAlias, help="""Represents an association of an entity attribute to a term.""")
@cli_util.help_option_group
def attribute_tag_group():
    pass


@click.command(cli_util.override('data_catalog.job_log_group.command_name', 'job-log'), cls=CommandGroupWithAlias, help="""Job log details. A job log is an audit log record inserted during the lifecycle of a job execution instance.""")
@cli_util.help_option_group
def job_log_group():
    pass


@click.command(cli_util.override('data_catalog.data_asset_group.command_name', 'data-asset'), cls=CommandGroupWithAlias, help="""Data asset representation. A physical store, or stream, of data known to the data catalog and containing one or many data entities, possibly in an organized structure of folders. A data asset is often synonymous with a 'System', such as a database, or may be a file container or a message stream.""")
@cli_util.help_option_group
def data_asset_group():
    pass


@click.command(cli_util.override('data_catalog.attribute_tag_collection_group.command_name', 'attribute-tag-collection'), cls=CommandGroupWithAlias, help="""Results of an attribute tags listing. Attribnute tags allow association of business terms with attributes.""")
@cli_util.help_option_group
def attribute_tag_collection_group():
    pass


@click.command(cli_util.override('data_catalog.work_request_error_group.command_name', 'work-request-error'), cls=CommandGroupWithAlias, help="""An error encountered while executing a work request.""")
@cli_util.help_option_group
def work_request_error_group():
    pass


@click.command(cli_util.override('data_catalog.connection_group.command_name', 'connection'), cls=CommandGroupWithAlias, help="""Detailed representation of a connection to a data asset, minus any sensitive properties.""")
@cli_util.help_option_group
def connection_group():
    pass


@click.command(cli_util.override('data_catalog.term_group.command_name', 'term'), cls=CommandGroupWithAlias, help="""Full term definition. A defined business term in a business glossary. As well as a term definition, simple format rules for attributes mapping to the term (for example, the expected data type and length restrictions) may be stated at the term level. Nesting of terms to support a hierarchy is supported by default.""")
@cli_util.help_option_group
def term_group():
    pass


@click.command(cli_util.override('data_catalog.job_collection_group.command_name', 'job-collection'), cls=CommandGroupWithAlias, help="""Results of a jobs listing. Jobs are scheduled instances of a job definition.""")
@cli_util.help_option_group
def job_collection_group():
    pass


@click.command(cli_util.override('data_catalog.attribute_group.command_name', 'attribute'), cls=CommandGroupWithAlias, help="""Details of an entity attribute. An attribute of a data entity describing an item of data, with a name and data type. Synonymous with 'column' in a database.""")
@cli_util.help_option_group
def attribute_group():
    pass


@click.command(cli_util.override('data_catalog.job_definition_group.command_name', 'job-definition'), cls=CommandGroupWithAlias, help="""Representation of a job definition resource. Job definitions define the harvest scope and includes the list of objects to be harvested along with a schedule. The list of objects is usually specified through a combination of object type, regular expressions, or specific names of objects and a sample size for the data harvested.""")
@cli_util.help_option_group
def job_definition_group():
    pass


@click.command(cli_util.override('data_catalog.job_execution_group.command_name', 'job-execution'), cls=CommandGroupWithAlias, help="""A job execution is a unit of work being executed on behalf of a job.""")
@cli_util.help_option_group
def job_execution_group():
    pass


@click.command(cli_util.override('data_catalog.connection_collection_group.command_name', 'connection-collection'), cls=CommandGroupWithAlias, help="""Results of a connections listing. Each member of the result is a summary representation of a connection to a data asset.""")
@cli_util.help_option_group
def connection_collection_group():
    pass


@click.command(cli_util.override('data_catalog.entity_tag_group.command_name', 'entity-tag'), cls=CommandGroupWithAlias, help="""Represents an association of an entity to a term.""")
@cli_util.help_option_group
def entity_tag_group():
    pass


@click.command(cli_util.override('data_catalog.attribute_collection_group.command_name', 'attribute-collection'), cls=CommandGroupWithAlias, help="""Results of an attributes listing. Attributes describe an item of data with name and datatype.""")
@cli_util.help_option_group
def attribute_collection_group():
    pass


@click.command(cli_util.override('data_catalog.metastore_group.command_name', 'metastore'), cls=CommandGroupWithAlias, help="""A Data Catalog Metastore provides a centralized metastore repository for use by other OCI services.""")
@cli_util.help_option_group
def metastore_group():
    pass


@click.command(cli_util.override('data_catalog.folder_tag_group.command_name', 'folder-tag'), cls=CommandGroupWithAlias, help="""Represents an association of a folder to a term.""")
@cli_util.help_option_group
def folder_tag_group():
    pass


@click.command(cli_util.override('data_catalog.search_result_group.command_name', 'search-result'), cls=CommandGroupWithAlias, help="""The search result object is the definition of an element that is returned as part of search. It contains basic information about the object such as key, name and description. The search result also contains the list of tags for each object along with other contextual information like the data asset root, folder, or entity parents.""")
@cli_util.help_option_group
def search_result_group():
    pass


@click.command(cli_util.override('data_catalog.data_asset_tag_group.command_name', 'data-asset-tag'), cls=CommandGroupWithAlias, help="""Represents an association of a data asset to a term.""")
@cli_util.help_option_group
def data_asset_tag_group():
    pass


@click.command(cli_util.override('data_catalog.suggest_results_group.command_name', 'suggest-results'), cls=CommandGroupWithAlias, help="""The list of potential matches returned from the suggest operation for the given input text. The size of the list will be determined by the limit parameter.""")
@cli_util.help_option_group
def suggest_results_group():
    pass


@click.command(cli_util.override('data_catalog.glossary_group.command_name', 'glossary'), cls=CommandGroupWithAlias, help="""Full glossary details. A glossary of business terms, such as 'Customer', 'Account', 'Contact' , 'Address', or 'Product', with definitions, used to provide common meaning across disparate data assets. Business glossaries may be hierarchical where some terms may contain child terms to allow them to be used as 'taxonomies'. By linking data assets, data entities, and attributes to glossaries and glossary terms, the glossary can act as a way of organizing data catalog objects in a hierarchy to make a large number of objects more navigable and easier to consume. Objects in the data aatalog, such as data assets or data entities, may be linked to any level in the glossary, so that the glossary can be used to browse the available data according to the business model of the organization.""")
@cli_util.help_option_group
def glossary_group():
    pass


@click.command(cli_util.override('data_catalog.folder_group.command_name', 'folder'), cls=CommandGroupWithAlias, help="""A generic term used in the data catalog for an external organization concept used for a collection of data entities or processes within a data asset. This term is an internal term which models multiple external types of folder, such as file directories, database schemas, and so on. Some data assets, such as Object Store containers, may contain many levels of folders.""")
@cli_util.help_option_group
def folder_group():
    pass


@click.command(cli_util.override('data_catalog.namespace_group.command_name', 'namespace'), cls=CommandGroupWithAlias, help="""Namespace Definition""")
@cli_util.help_option_group
def namespace_group():
    pass


@click.command(cli_util.override('data_catalog.catalog_private_endpoint_group.command_name', 'catalog-private-endpoint'), cls=CommandGroupWithAlias, help="""A private network reverse connection creates a connection from service to customer subnet over a private network.""")
@cli_util.help_option_group
def catalog_private_endpoint_group():
    pass


@click.command(cli_util.override('data_catalog.data_asset_tag_collection_group.command_name', 'data-asset-tag-collection'), cls=CommandGroupWithAlias, help="""Results of a data asset tag listing. Data asset tags represent an association of a data asset to a term.""")
@cli_util.help_option_group
def data_asset_tag_collection_group():
    pass


@click.command(cli_util.override('data_catalog.job_metric_collection_group.command_name', 'job-metric-collection'), cls=CommandGroupWithAlias, help="""Results of a job metrics listing. Job metrics are datum about a job execution in key value pairs.""")
@cli_util.help_option_group
def job_metric_collection_group():
    pass


@click.command(cli_util.override('data_catalog.job_log_collection_group.command_name', 'job-log-collection'), cls=CommandGroupWithAlias, help="""Results of a job logs Listing. A job log is an audit log record inserted during the lifecycle of a job execution instance.""")
@cli_util.help_option_group
def job_log_collection_group():
    pass


@click.command(cli_util.override('data_catalog.job_group.command_name', 'job'), cls=CommandGroupWithAlias, help="""Details of a job. Jobs are scheduled instances of a job definition.""")
@cli_util.help_option_group
def job_group():
    pass


@click.command(cli_util.override('data_catalog.entity_group.command_name', 'entity'), cls=CommandGroupWithAlias, help="""Data entity details. A representation of data with a set of attributes, normally representing a single business entity. Synonymous with 'table' or 'view' in a database, or a single logical file structure that one or many files may match.""")
@cli_util.help_option_group
def entity_group():
    pass


@click.command(cli_util.override('data_catalog.type_collection_group.command_name', 'type-collection'), cls=CommandGroupWithAlias, help="""Results of a types listing. Types define the basic type of catalog objects and are immutable.""")
@cli_util.help_option_group
def type_collection_group():
    pass


@click.command(cli_util.override('data_catalog.job_execution_collection_group.command_name', 'job-execution-collection'), cls=CommandGroupWithAlias, help="""Results of a job executions listing. Job executions are execution instances of a scheduled job.""")
@cli_util.help_option_group
def job_execution_collection_group():
    pass


data_catalog_root_group.add_command(job_definition_collection_group)
data_catalog_root_group.add_command(catalog_group)
data_catalog_root_group.add_command(term_relationship_group)
data_catalog_root_group.add_command(folder_tag_collection_group)
data_catalog_root_group.add_command(pattern_group)
data_catalog_root_group.add_command(entity_tag_collection_group)
data_catalog_root_group.add_command(work_request_group)
data_catalog_root_group.add_command(job_metric_group)
data_catalog_root_group.add_command(type_group)
data_catalog_root_group.add_command(folder_collection_group)
data_catalog_root_group.add_command(data_asset_collection_group)
data_catalog_root_group.add_command(rule_summary_group)
data_catalog_root_group.add_command(custom_property_group)
data_catalog_root_group.add_command(work_request_log_group)
data_catalog_root_group.add_command(attribute_tag_group)
data_catalog_root_group.add_command(job_log_group)
data_catalog_root_group.add_command(data_asset_group)
data_catalog_root_group.add_command(attribute_tag_collection_group)
data_catalog_root_group.add_command(work_request_error_group)
data_catalog_root_group.add_command(connection_group)
data_catalog_root_group.add_command(term_group)
data_catalog_root_group.add_command(job_collection_group)
data_catalog_root_group.add_command(attribute_group)
data_catalog_root_group.add_command(job_definition_group)
data_catalog_root_group.add_command(job_execution_group)
data_catalog_root_group.add_command(connection_collection_group)
data_catalog_root_group.add_command(entity_tag_group)
data_catalog_root_group.add_command(attribute_collection_group)
data_catalog_root_group.add_command(metastore_group)
data_catalog_root_group.add_command(folder_tag_group)
data_catalog_root_group.add_command(search_result_group)
data_catalog_root_group.add_command(data_asset_tag_group)
data_catalog_root_group.add_command(suggest_results_group)
data_catalog_root_group.add_command(glossary_group)
data_catalog_root_group.add_command(folder_group)
data_catalog_root_group.add_command(namespace_group)
data_catalog_root_group.add_command(catalog_private_endpoint_group)
data_catalog_root_group.add_command(data_asset_tag_collection_group)
data_catalog_root_group.add_command(job_metric_collection_group)
data_catalog_root_group.add_command(job_log_collection_group)
data_catalog_root_group.add_command(job_group)
data_catalog_root_group.add_command(entity_group)
data_catalog_root_group.add_command(type_collection_group)
data_catalog_root_group.add_command(job_execution_collection_group)


@data_asset_group.command(name=cli_util.override('data_catalog.add_data_selector_patterns.command_name', 'add'), help=u"""Add data selector pattern to the data asset. \n[Command Reference](addDataSelectorPatterns)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of pattern Ids.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'data_catalog', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'data_catalog', 'class': 'list[string]'}}, output_type={'module': 'data_catalog', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def add_data_selector_patterns(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, items, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.add_data_selector_patterns(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        data_selector_pattern_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@type_group.command(name=cli_util.override('data_catalog.associate_custom_property.command_name', 'associate-custom-property'), help=u"""Associate the custom property for the given type \n[Command Reference](associateCustomProperty)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--type-key', required=True, help=u"""Unique type key.""")
@cli_util.option('--custom-property-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""array of custom property Ids""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-event-enabled', type=click.BOOL, help=u"""If an OCI Event will be emitted when the custom property is modified.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-ids': {'module': 'data_catalog', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-ids': {'module': 'data_catalog', 'class': 'list[string]'}}, output_type={'module': 'data_catalog', 'class': 'Type'})
@cli_util.wrap_exceptions
def associate_custom_property(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, type_key, custom_property_ids, is_event_enabled, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(type_key, six.string_types) and len(type_key.strip()) == 0:
        raise click.UsageError('Parameter --type-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if custom_property_ids is not None:
        _details['customPropertyIds'] = cli_util.parse_json_parameter("custom_property_ids", custom_property_ids)

    if is_event_enabled is not None:
        _details['isEventEnabled'] = is_event_enabled

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.associate_custom_property(
        catalog_id=catalog_id,
        type_key=type_key,
        associate_custom_property_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_type') and callable(getattr(client, 'get_type')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_type(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@catalog_group.command(name=cli_util.override('data_catalog.attach_catalog_private_endpoint.command_name', 'attach'), help=u"""Attaches a private reverse connection endpoint resource to a data catalog resource. When provided, 'If-Match' is checked against 'ETag' values of the resource. \n[Command Reference](attachCatalogPrivateEndpoint)""")
@cli_util.option('--catalog-private-endpoint-id', required=True, help=u"""The identifier of the private endpoint to be attached to the catalog resource.""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def attach_catalog_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_private_endpoint_id, catalog_id, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['catalogPrivateEndpointId'] = catalog_private_endpoint_id

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.attach_catalog_private_endpoint(
        catalog_id=catalog_id,
        attach_catalog_private_endpoint_details=_details,
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


@catalog_group.command(name=cli_util.override('data_catalog.change_catalog_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource. \n[Command Reference](changeCatalogCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The identifier of the compartment where the resource should be moved.""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_catalog_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, catalog_id, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.change_catalog_compartment(
        catalog_id=catalog_id,
        change_catalog_compartment_details=_details,
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


@catalog_private_endpoint_group.command(name=cli_util.override('data_catalog.change_catalog_private_endpoint_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource. \n[Command Reference](changeCatalogPrivateEndpointCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""The identifier of the compartment where the resource should be moved.""")
@cli_util.option('--catalog-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_catalog_private_endpoint_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, catalog_private_endpoint_id, if_match):

    if isinstance(catalog_private_endpoint_id, six.string_types) and len(catalog_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.change_catalog_private_endpoint_compartment(
        catalog_private_endpoint_id=catalog_private_endpoint_id,
        change_catalog_private_endpoint_compartment_details=_details,
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


@metastore_group.command(name=cli_util.override('data_catalog.change_metastore_compartment.command_name', 'change-compartment'), help=u"""Moves a resource into a different compartment. When provided, 'If-Match' is checked against 'ETag' values of the resource. \n[Command Reference](changeMetastoreCompartment)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment to which the metastore should be moved.""")
@cli_util.option('--metastore-id', required=True, help=u"""The metastore's OCID.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def change_metastore_compartment(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, metastore_id, if_match):

    if isinstance(metastore_id, six.string_types) and len(metastore_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.change_metastore_compartment(
        metastore_id=metastore_id,
        change_metastore_compartment_details=_details,
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


@attribute_group.command(name=cli_util.override('data_catalog.create_attribute.command_name', 'create'), help=u"""Creates a new entity attribute. \n[Command Reference](createAttribute)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--external-data-type', required=True, help=u"""Data type of the attribute as defined in the external system.""")
@cli_util.option('--time-external', required=True, type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of this object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--business-name', help=u"""Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.""")
@cli_util.option('--description', help=u"""Detailed description of the attribute.""")
@cli_util.option('--is-incremental-data', type=click.BOOL, help=u"""Property that identifies if this attribute can be used as a watermark to extract incremental data.""")
@cli_util.option('--is-nullable', type=click.BOOL, help=u"""Property that identifies if this attribute can be assigned null values.""")
@cli_util.option('--length', type=click.INT, help=u"""Max allowed length of the attribute value.""")
@cli_util.option('--position', type=click.INT, help=u"""Position of the attribute in the record definition.""")
@cli_util.option('--precision', type=click.INT, help=u"""Precision of the attribute value usually applies to float data type.""")
@cli_util.option('--scale', type=click.INT, help=u"""Scale of the attribute value usually applies to float data type.""")
@cli_util.option('--min-collection-count', type=click.INT, help=u"""The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.""")
@cli_util.option('--max-collection-count', type=click.INT, help=u"""The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type. For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\". Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json""")
@cli_util.option('--external-datatype-entity-key', help=u"""External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.""")
@cli_util.option('--external-parent-attribute-key', help=u"""External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the attribute type. Each attribute type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most attributes have required properties within the \"default\" category. To determine the set of required and optional properties for an attribute type, a query can be done on '/types?type=attribute' that returns a collection of all attribute types. The appropriate attribute type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Attribute'})
@cli_util.wrap_exceptions
def create_attribute(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, entity_key, display_name, external_data_type, time_external, business_name, description, is_incremental_data, is_nullable, length, position, precision, scale, min_collection_count, max_collection_count, external_datatype_entity_key, external_parent_attribute_key, custom_property_members, properties):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['externalDataType'] = external_data_type
    _details['timeExternal'] = time_external

    if business_name is not None:
        _details['businessName'] = business_name

    if description is not None:
        _details['description'] = description

    if is_incremental_data is not None:
        _details['isIncrementalData'] = is_incremental_data

    if is_nullable is not None:
        _details['isNullable'] = is_nullable

    if length is not None:
        _details['length'] = length

    if position is not None:
        _details['position'] = position

    if precision is not None:
        _details['precision'] = precision

    if scale is not None:
        _details['scale'] = scale

    if min_collection_count is not None:
        _details['minCollectionCount'] = min_collection_count

    if max_collection_count is not None:
        _details['maxCollectionCount'] = max_collection_count

    if external_datatype_entity_key is not None:
        _details['externalDatatypeEntityKey'] = external_datatype_entity_key

    if external_parent_attribute_key is not None:
        _details['externalParentAttributeKey'] = external_parent_attribute_key

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_attribute(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        create_attribute_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_attribute') and callable(getattr(client, 'get_attribute')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_attribute(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@attribute_tag_group.command(name=cli_util.override('data_catalog.create_attribute_tag.command_name', 'create'), help=u"""Creates a new entity attribute tag. \n[Command Reference](createAttributeTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--attribute-key', required=True, help=u"""Unique attribute key.""")
@cli_util.option('--name', help=u"""The name of the tag in the case of a free form tag. When linking to a glossary term, this field is not specified.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term or null in the case of a free form tag.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'AttributeTag'})
@cli_util.wrap_exceptions
def create_attribute_tag(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, entity_key, attribute_key, name, term_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(attribute_key, six.string_types) and len(attribute_key.strip()) == 0:
        raise click.UsageError('Parameter --attribute-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if term_key is not None:
        _details['termKey'] = term_key

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_attribute_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        attribute_key=attribute_key,
        create_attribute_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_attribute_tag') and callable(getattr(client, 'get_attribute_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_attribute_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@catalog_group.command(name=cli_util.override('data_catalog.create_catalog.command_name', 'create'), help=u"""Creates a new data catalog instance that includes a console and an API URL for managing metadata operations. For more information, please see the documentation. \n[Command Reference](createCatalog)""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier.""")
@cli_util.option('--display-name', help=u"""Data catalog identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_catalog(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_catalog(
        create_catalog_details=_details,
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


@catalog_private_endpoint_group.command(name=cli_util.override('data_catalog.create_catalog_private_endpoint.command_name', 'create'), help=u"""Create a new private reverse connection endpoint. \n[Command Reference](createCatalogPrivateEndpoint)""")
@cli_util.option('--dns-zones', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--subnet-id', required=True, help=u"""The OCID of subnet to which the reverse connection is to be created""")
@cli_util.option('--compartment-id', required=True, help=u"""Compartment identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name of the private endpoint resource being created.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-zones': {'module': 'data_catalog', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'data_catalog', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_catalog_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, dns_zones, subnet_id, compartment_id, freeform_tags, defined_tags, display_name):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)
    _details['subnetId'] = subnet_id
    _details['compartmentId'] = compartment_id

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_catalog_private_endpoint(
        create_catalog_private_endpoint_details=_details,
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


@connection_group.command(name=cli_util.override('data_catalog.create_connection.command_name', 'create'), help=u"""Creates a new connection. \n[Command Reference](createConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--type-key', required=True, help=u"""The key of the object type. Type key's can be found via the '/types' endpoint.""")
@cli_util.option('--properties', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--description', help=u"""A description of the connection.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--enc-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the encrypted values for sensitive properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-default', type=click.BOOL, help=u"""Indicates whether this connection is the default connection. The first connection of a data asset defaults to being the default, subsequent connections default to not being the default. If a default connection already exists, then trying to create a connection as the default will fail. In this case the default connection would need to be updated not to be the default and then the new connection can then be created as the default.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}, 'enc-properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}, 'enc-properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Connection'})
@cli_util.wrap_exceptions
def create_connection(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, display_name, type_key, properties, description, custom_property_members, enc_properties, is_default):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['typeKey'] = type_key
    _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if description is not None:
        _details['description'] = description

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if enc_properties is not None:
        _details['encProperties'] = cli_util.parse_json_parameter("enc_properties", enc_properties)

    if is_default is not None:
        _details['isDefault'] = is_default

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        create_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_connection') and callable(getattr(client, 'get_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@custom_property_group.command(name=cli_util.override('data_catalog.create_custom_property.command_name', 'create'), help=u"""Create a new Custom Property \n[Command Reference](createCustomProperty)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the custom property.""")
@cli_util.option('--data-type', type=custom_types.CliCaseInsensitiveChoice(["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"]), help=u"""The data type of the custom property""")
@cli_util.option('--is-sortable', type=click.BOOL, help=u"""If this field allows to sort from UI""")
@cli_util.option('--is-filterable', type=click.BOOL, help=u"""If this field allows to filter or create facets from UI""")
@cli_util.option('--is-multi-valued', type=click.BOOL, help=u"""If this field allows multiple values to be set""")
@cli_util.option('--is-hidden', type=click.BOOL, help=u"""If this field is a hidden field""")
@cli_util.option('--is-editable', type=click.BOOL, help=u"""If this field is a editable field""")
@cli_util.option('--is-shown-in-list', type=click.BOOL, help=u"""If this field is displayed in a list view of applicable objects.""")
@cli_util.option('--is-hidden-in-search', type=click.BOOL, help=u"""If this field is allowed to pop in search results""")
@cli_util.option('--is-event-enabled', type=click.BOOL, help=u"""If an OCI Event will be emitted when the custom property is modified.""")
@cli_util.option('--allowed-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Allowed values for the custom property if any""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the data asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. To determine the set of optional and required properties for a data asset type, a query can be done on '/types?type=dataAsset' that returns a collection of all data asset types. The appropriate data asset type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'allowed-values': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'allowed-values': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'CustomProperty'})
@cli_util.wrap_exceptions
def create_custom_property(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, namespace_id, display_name, description, data_type, is_sortable, is_filterable, is_multi_valued, is_hidden, is_editable, is_shown_in_list, is_hidden_in_search, is_event_enabled, allowed_values, properties):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if data_type is not None:
        _details['dataType'] = data_type

    if is_sortable is not None:
        _details['isSortable'] = is_sortable

    if is_filterable is not None:
        _details['isFilterable'] = is_filterable

    if is_multi_valued is not None:
        _details['isMultiValued'] = is_multi_valued

    if is_hidden is not None:
        _details['isHidden'] = is_hidden

    if is_editable is not None:
        _details['isEditable'] = is_editable

    if is_shown_in_list is not None:
        _details['isShownInList'] = is_shown_in_list

    if is_hidden_in_search is not None:
        _details['isHiddenInSearch'] = is_hidden_in_search

    if is_event_enabled is not None:
        _details['isEventEnabled'] = is_event_enabled

    if allowed_values is not None:
        _details['allowedValues'] = cli_util.parse_json_parameter("allowed_values", allowed_values)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_custom_property(
        catalog_id=catalog_id,
        namespace_id=namespace_id,
        create_custom_property_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_custom_property') and callable(getattr(client, 'get_custom_property')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_custom_property(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@data_asset_group.command(name=cli_util.override('data_catalog.create_data_asset.command_name', 'create'), help=u"""Create a new data asset. \n[Command Reference](createDataAsset)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--type-key', required=True, help=u"""The key of the data asset type. This can be obtained via the '/types' endpoint.""")
@cli_util.option('--description', help=u"""Detailed description of the data asset.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the data asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. To determine the set of optional and required properties for a data asset type, a query can be done on '/types?type=dataAsset' that returns a collection of all data asset types. The appropriate data asset type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def create_data_asset(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, display_name, type_key, description, custom_property_members, properties):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['typeKey'] = type_key

    if description is not None:
        _details['description'] = description

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_data_asset(
        catalog_id=catalog_id,
        create_data_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@data_asset_tag_group.command(name=cli_util.override('data_catalog.create_data_asset_tag.command_name', 'create'), help=u"""Creates a new data asset tag. \n[Command Reference](createDataAssetTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--name', help=u"""The name of the tag in the case of a free form tag. When linking to a glossary term, this field is not specified.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term or null in the case of a free form tag.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'DataAssetTag'})
@cli_util.wrap_exceptions
def create_data_asset_tag(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, name, term_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if term_key is not None:
        _details['termKey'] = term_key

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_data_asset_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        create_data_asset_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset_tag') and callable(getattr(client, 'get_data_asset_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@entity_group.command(name=cli_util.override('data_catalog.create_entity.command_name', 'create'), help=u"""Creates a new data entity. \n[Command Reference](createEntity)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--time-external', required=True, type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of the object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--business-name', help=u"""Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.""")
@cli_util.option('--description', help=u"""Detailed description of a data entity.""")
@cli_util.option('--is-logical', type=click.BOOL, help=u"""Property to indicate if the object is a physical materialized object or virtual. For example, View.""")
@cli_util.option('--is-partition', type=click.BOOL, help=u"""Property to indicate if the object is a sub object of a parent physical object.""")
@cli_util.option('--folder-key', help=u"""Key of the associated folder.""")
@cli_util.option('--pattern-key', help=u"""Key of the associated pattern if this is a logical entity.""")
@cli_util.option('--realized-expression', help=u"""The expression realized after resolving qualifiers . Used in deriving this logical entity""")
@cli_util.option('--harvest-status', type=custom_types.CliCaseInsensitiveChoice(["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]), help=u"""Status of the object as updated by the harvest process. When an entity object is created , it's harvest status will indicate if the entity's metadata has been fully harvested or not. The harvest process can perform shallow harvesting to allow users to browse the metadata and can on-demand deep harvest on any object This requires a harvest status indicator for catalog objects.""")
@cli_util.option('--last-job-key', help=u"""Key of the last harvest process to update this object.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the entity type. Each entity type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most entities have required properties within the \"default\" category. To determine the set of required and optional properties for an entity type, a query can be done on '/types?type=dataEntity' that returns a collection of all entity types. The appropriate entity type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Entity'})
@cli_util.wrap_exceptions
def create_entity(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, display_name, time_external, business_name, description, is_logical, is_partition, folder_key, pattern_key, realized_expression, harvest_status, last_job_key, custom_property_members, properties):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['timeExternal'] = time_external

    if business_name is not None:
        _details['businessName'] = business_name

    if description is not None:
        _details['description'] = description

    if is_logical is not None:
        _details['isLogical'] = is_logical

    if is_partition is not None:
        _details['isPartition'] = is_partition

    if folder_key is not None:
        _details['folderKey'] = folder_key

    if pattern_key is not None:
        _details['patternKey'] = pattern_key

    if realized_expression is not None:
        _details['realizedExpression'] = realized_expression

    if harvest_status is not None:
        _details['harvestStatus'] = harvest_status

    if last_job_key is not None:
        _details['lastJobKey'] = last_job_key

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_entity(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        create_entity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_entity') and callable(getattr(client, 'get_entity')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_entity(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@entity_tag_group.command(name=cli_util.override('data_catalog.create_entity_tag.command_name', 'create'), help=u"""Creates a new entity tag. \n[Command Reference](createEntityTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--name', help=u"""The name of the tag in the case of a free form tag. When linking to a glossary term, this field is not specified.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term or null in the case of a free form tag.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'EntityTag'})
@cli_util.wrap_exceptions
def create_entity_tag(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, entity_key, name, term_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if term_key is not None:
        _details['termKey'] = term_key

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_entity_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        create_entity_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_entity_tag') and callable(getattr(client, 'get_entity_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_entity_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@folder_group.command(name=cli_util.override('data_catalog.create_folder.command_name', 'create'), help=u"""Creates a new folder. \n[Command Reference](createFolder)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--time-external', required=True, type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of this object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--business-name', help=u"""Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.""")
@cli_util.option('--description', help=u"""Detailed description of a folder.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the folder type. Each folder type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most folders have required properties within the \"default\" category. To determine the set of optional and required properties for a folder type, a query can be done on '/types?type=folder' that returns a collection of all folder types. The appropriate folder type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--parent-folder-key', help=u"""The key of the containing folder or null if there isn't a parent folder.""")
@cli_util.option('--last-job-key', help=u"""The job key of the harvest process that updated the folder definition from the source system.""")
@cli_util.option('--harvest-status', type=custom_types.CliCaseInsensitiveChoice(["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]), help=u"""Folder harvesting status.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Folder'})
@cli_util.wrap_exceptions
def create_folder(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, display_name, time_external, business_name, description, custom_property_members, properties, parent_folder_key, last_job_key, harvest_status):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['timeExternal'] = time_external

    if business_name is not None:
        _details['businessName'] = business_name

    if description is not None:
        _details['description'] = description

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if parent_folder_key is not None:
        _details['parentFolderKey'] = parent_folder_key

    if last_job_key is not None:
        _details['lastJobKey'] = last_job_key

    if harvest_status is not None:
        _details['harvestStatus'] = harvest_status

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_folder(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        create_folder_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_folder') and callable(getattr(client, 'get_folder')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_folder(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@folder_tag_group.command(name=cli_util.override('data_catalog.create_folder_tag.command_name', 'create'), help=u"""Creates a new folder tag. \n[Command Reference](createFolderTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--folder-key', required=True, help=u"""Unique folder key.""")
@cli_util.option('--name', help=u"""The name of the tag in the case of a free form tag. When linking to a glossary term, this field is not specified.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term or null in the case of a free form tag.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'FolderTag'})
@cli_util.wrap_exceptions
def create_folder_tag(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, folder_key, name, term_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if name is not None:
        _details['name'] = name

    if term_key is not None:
        _details['termKey'] = term_key

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_folder_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        folder_key=folder_key,
        create_folder_tag_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_folder_tag') and callable(getattr(client, 'get_folder_tag')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_folder_tag(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@glossary_group.command(name=cli_util.override('data_catalog.create_glossary.command_name', 'create'), help=u"""Creates a new glossary. \n[Command Reference](createGlossary)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the glossary.""")
@cli_util.option('--workflow-status', type=custom_types.CliCaseInsensitiveChoice(["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]), help=u"""Status of the approval process workflow for this business glossary.""")
@cli_util.option('--owner', help=u"""OCID of the user who is the owner of the glossary.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}}, output_type={'module': 'data_catalog', 'class': 'Glossary'})
@cli_util.wrap_exceptions
def create_glossary(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, display_name, description, workflow_status, owner, custom_property_members):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if workflow_status is not None:
        _details['workflowStatus'] = workflow_status

    if owner is not None:
        _details['owner'] = owner

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_glossary(
        catalog_id=catalog_id,
        create_glossary_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_glossary') and callable(getattr(client, 'get_glossary')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_glossary(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_catalog.create_job.command_name', 'create'), help=u"""Creates a new job. \n[Command Reference](createJob)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--job-definition-key', required=True, help=u"""The unique key of the job definition that defined the scope of this job.""")
@cli_util.option('--description', help=u"""Detailed description of the job.""")
@cli_util.option('--schedule-cron-expression', help=u"""Schedule specified in the cron expression format that has seven fields for second, minute, hour, day-of-month, month, day-of-week, year. It can also include special characters like * for all and ? for any. There are also pre-defined schedules that can be specified using special strings. For example, @hourly will run the job every hour.""")
@cli_util.option('--time-schedule-begin', type=custom_types.CLI_DATETIME, help=u"""Date that the schedule should be operational. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-schedule-end', type=custom_types.CLI_DATETIME, help=u"""Date that the schedule should end from being operational. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--connection-key', help=u"""The key of the connection used by the job. This connection will override the default connection specified in the associated job definition. All executions will use this connection.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "EXPIRED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Job'})
@cli_util.wrap_exceptions
def create_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, display_name, job_definition_key, description, schedule_cron_expression, time_schedule_begin, time_schedule_end, connection_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['jobDefinitionKey'] = job_definition_key

    if description is not None:
        _details['description'] = description

    if schedule_cron_expression is not None:
        _details['scheduleCronExpression'] = schedule_cron_expression

    if time_schedule_begin is not None:
        _details['timeScheduleBegin'] = time_schedule_begin

    if time_schedule_end is not None:
        _details['timeScheduleEnd'] = time_schedule_end

    if connection_key is not None:
        _details['connectionKey'] = connection_key

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_job(
        catalog_id=catalog_id,
        create_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_definition_group.command(name=cli_util.override('data_catalog.create_job_definition.command_name', 'create'), help=u"""Creates a new job definition. \n[Command Reference](createJobDefinition)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--job-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE", "IMPORT_DATA_ASSET"]), help=u"""Type of the job definition.""")
@cli_util.option('--description', help=u"""Detailed description of the job definition.""")
@cli_util.option('--is-incremental', type=click.BOOL, help=u"""Specifies if the job definition is incremental or full.""")
@cli_util.option('--data-asset-key', help=u"""The key of the data asset for which the job is defined.""")
@cli_util.option('--connection-key', help=u"""The key of the connection resource to be used for the job.""")
@cli_util.option('--is-sample-data-extracted', type=click.BOOL, help=u"""Specify if sample data to be extracted as part of this harvest.""")
@cli_util.option('--sample-data-size-in-mbs', type=click.INT, help=u"""Specify the sample data size in MB, specified as number of rows, for this metadata harvest.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the job type. Each job type definition may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job definitions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'JobDefinition'})
@cli_util.wrap_exceptions
def create_job_definition(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, display_name, job_type, description, is_incremental, data_asset_key, connection_key, is_sample_data_extracted, sample_data_size_in_mbs, properties):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['jobType'] = job_type

    if description is not None:
        _details['description'] = description

    if is_incremental is not None:
        _details['isIncremental'] = is_incremental

    if data_asset_key is not None:
        _details['dataAssetKey'] = data_asset_key

    if connection_key is not None:
        _details['connectionKey'] = connection_key

    if is_sample_data_extracted is not None:
        _details['isSampleDataExtracted'] = is_sample_data_extracted

    if sample_data_size_in_mbs is not None:
        _details['sampleDataSizeInMBs'] = sample_data_size_in_mbs

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_job_definition(
        catalog_id=catalog_id,
        create_job_definition_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job_definition') and callable(getattr(client, 'get_job_definition')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job_definition(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_execution_group.command(name=cli_util.override('data_catalog.create_job_execution.command_name', 'create'), help=u"""Creates a new job execution. \n[Command Reference](createJobExecution)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--sub-type', help=u"""Sub-type of this job execution.""")
@cli_util.option('--job-type', type=custom_types.CliCaseInsensitiveChoice(["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE", "IMPORT_DATA_ASSET"]), help=u"""Type of the job execution.""")
@cli_util.option('--parent-key', help=u"""The unique key of the parent execution or null if this job execution has no parent.""")
@cli_util.option('--time-started', type=custom_types.CLI_DATETIME, help=u"""Time that job execution started. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-ended', type=custom_types.CLI_DATETIME, help=u"""Time that the job execution ended or null if it hasn't yet completed. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", "SUCCEEDED_WITH_WARNINGS"]), help=u"""Status of the job execution, such as running, paused, or completed.""")
@cli_util.option('--error-code', help=u"""Error code returned from the job execution or null if job is still running or didn't return an error.""")
@cli_util.option('--error-message', help=u"""Error message returned from the job execution or null if job is still running or didn't return an error.""")
@cli_util.option('--schedule-instance-key', help=u"""The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.""")
@cli_util.option('--process-key', help=u"""Process identifier related to the job execution if the job is an external job.""")
@cli_util.option('--external-url', help=u"""If the job is an external process, then a URL of the job for accessing this resource and its status.""")
@cli_util.option('--event-key', help=u"""An identifier used for log message correlation.""")
@cli_util.option('--data-entity-key', help=u"""The key of the associated data entity resource.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the execution context properties which are specific to a job execution. Each job execution may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job executions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", "SUCCEEDED_WITH_WARNINGS"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'JobExecution'})
@cli_util.wrap_exceptions
def create_job_execution(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, job_key, sub_type, job_type, parent_key, time_started, time_ended, lifecycle_state, error_code, error_message, schedule_instance_key, process_key, external_url, event_key, data_entity_key, properties):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if sub_type is not None:
        _details['subType'] = sub_type

    if job_type is not None:
        _details['jobType'] = job_type

    if parent_key is not None:
        _details['parentKey'] = parent_key

    if time_started is not None:
        _details['timeStarted'] = time_started

    if time_ended is not None:
        _details['timeEnded'] = time_ended

    if lifecycle_state is not None:
        _details['lifecycleState'] = lifecycle_state

    if error_code is not None:
        _details['errorCode'] = error_code

    if error_message is not None:
        _details['errorMessage'] = error_message

    if schedule_instance_key is not None:
        _details['scheduleInstanceKey'] = schedule_instance_key

    if process_key is not None:
        _details['processKey'] = process_key

    if external_url is not None:
        _details['externalUrl'] = external_url

    if event_key is not None:
        _details['eventKey'] = event_key

    if data_entity_key is not None:
        _details['dataEntityKey'] = data_entity_key

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_job_execution(
        catalog_id=catalog_id,
        job_key=job_key,
        create_job_execution_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job_execution') and callable(getattr(client, 'get_job_execution')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job_execution(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@metastore_group.command(name=cli_util.override('data_catalog.create_metastore.command_name', 'create'), help=u"""Creates a new metastore. \n[Command Reference](createMetastore)""")
@cli_util.option('--compartment-id', required=True, help=u"""OCID of the compartment which holds the metastore.""")
@cli_util.option('--default-managed-table-location', required=True, help=u"""Location under which managed tables will be created by default. This references Object Storage using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/""")
@cli_util.option('--default-external-table-location', required=True, help=u"""Location under which external tables will be created by default. This references Object Storage using an HDFS URI format. Example: oci://bucket@namespace/sub-dir/""")
@cli_util.option('--display-name', help=u"""Mutable name of the metastore.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def create_metastore(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, compartment_id, default_managed_table_location, default_external_table_location, display_name, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['compartmentId'] = compartment_id
    _details['defaultManagedTableLocation'] = default_managed_table_location
    _details['defaultExternalTableLocation'] = default_external_table_location

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_metastore(
        create_metastore_details=_details,
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


@namespace_group.command(name=cli_util.override('data_catalog.create_namespace.command_name', 'create'), help=u"""Create a new Namespace to be used by a custom property \n[Command Reference](createNamespace)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the Namespace.""")
@cli_util.option('--is-service-defined', type=click.BOOL, help=u"""If this field is defined by service or by a user""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Namespace'})
@cli_util.wrap_exceptions
def create_namespace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, display_name, description, is_service_defined):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_service_defined is not None:
        _details['isServiceDefined'] = is_service_defined

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_namespace(
        catalog_id=catalog_id,
        create_namespace_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_namespace') and callable(getattr(client, 'get_namespace')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_namespace(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@pattern_group.command(name=cli_util.override('data_catalog.create_pattern.command_name', 'create'), help=u"""Create a new pattern. \n[Command Reference](createPattern)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the Pattern.""")
@cli_util.option('--expression', help=u"""The expression used in the pattern that may include qualifiers. Refer to the user documentation for details of the format and examples.""")
@cli_util.option('--check-file-path-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of file paths against which the expression can be tried, as a check. This documents, for reference purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true, this will be run as a validation during the request, such that if the check fails the request fails. If isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even if the check fails, with a lifecycleState of FAILED.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enable-check-failure-limit', type=click.BOOL, help=u"""Indicates whether the expression check, against the checkFilePathList, will fail the request if the count of UNMATCHED files is above the checkFailureLimit.""")
@cli_util.option('--check-failure-limit', type=click.INT, help=u"""The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the pattern type. Each pattern type definition defines it's set of required and optional properties. Example: `{\"properties\": { \"default\": { \"tbd\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'check-file-path-list': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'check-file-path-list': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Pattern'})
@cli_util.wrap_exceptions
def create_pattern(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, display_name, description, expression, check_file_path_list, is_enable_check_failure_limit, check_failure_limit, properties):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if expression is not None:
        _details['expression'] = expression

    if check_file_path_list is not None:
        _details['checkFilePathList'] = cli_util.parse_json_parameter("check_file_path_list", check_file_path_list)

    if is_enable_check_failure_limit is not None:
        _details['isEnableCheckFailureLimit'] = is_enable_check_failure_limit

    if check_failure_limit is not None:
        _details['checkFailureLimit'] = check_failure_limit

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_pattern(
        catalog_id=catalog_id,
        create_pattern_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_pattern') and callable(getattr(client, 'get_pattern')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_pattern(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@term_group.command(name=cli_util.override('data_catalog.create_term.command_name', 'create'), help=u"""Create a new term within a glossary. \n[Command Reference](createTerm)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey' must be unique. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the term.""")
@cli_util.option('--is-allowed-to-have-child-terms', type=click.BOOL, help=u"""Indicates whether a term may contain child terms.""")
@cli_util.option('--parent-term-key', help=u"""The terms parent term key. Will be null if the term has no parent term.""")
@cli_util.option('--owner', help=u"""OCID of the user who is the owner of this business terminology.""")
@cli_util.option('--workflow-status', type=custom_types.CliCaseInsensitiveChoice(["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]), help=u"""Status of the approval process workflow for this business term in the glossary.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}}, output_type={'module': 'data_catalog', 'class': 'Term'})
@cli_util.wrap_exceptions
def create_term(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, glossary_key, display_name, description, is_allowed_to_have_child_terms, parent_term_key, owner, workflow_status, custom_property_members):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_allowed_to_have_child_terms is not None:
        _details['isAllowedToHaveChildTerms'] = is_allowed_to_have_child_terms

    if parent_term_key is not None:
        _details['parentTermKey'] = parent_term_key

    if owner is not None:
        _details['owner'] = owner

    if workflow_status is not None:
        _details['workflowStatus'] = workflow_status

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_term(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        create_term_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_term') and callable(getattr(client, 'get_term')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_term(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@term_relationship_group.command(name=cli_util.override('data_catalog.create_term_relationship.command_name', 'create'), help=u"""Creates a new term relationship for this term within a glossary. \n[Command Reference](createTermRelationship)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--display-name', required=True, help=u"""A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey' must be unique. Avoid entering confidential information. This is the same as 'relationshipType' for 'termRelationship'.""")
@cli_util.option('--related-term-key', required=True, help=u"""Unique id of the related term.""")
@cli_util.option('--description', help=u"""Detailed description of the term relationship usually defined at the time of creation.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'TermRelationship'})
@cli_util.wrap_exceptions
def create_term_relationship(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, glossary_key, term_key, display_name, related_term_key, description):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['relatedTermKey'] = related_term_key

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.create_term_relationship(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        term_key=term_key,
        create_term_relationship_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_term_relationship') and callable(getattr(client, 'get_term_relationship')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_term_relationship(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@attribute_group.command(name=cli_util.override('data_catalog.delete_attribute.command_name', 'delete'), help=u"""Deletes a specific entity attribute. \n[Command Reference](deleteAttribute)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--attribute-key', required=True, help=u"""Unique attribute key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_attribute(ctx, from_json, catalog_id, data_asset_key, entity_key, attribute_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(attribute_key, six.string_types) and len(attribute_key.strip()) == 0:
        raise click.UsageError('Parameter --attribute-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_attribute(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        attribute_key=attribute_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@attribute_tag_group.command(name=cli_util.override('data_catalog.delete_attribute_tag.command_name', 'delete'), help=u"""Deletes a specific entity attribute tag. \n[Command Reference](deleteAttributeTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--attribute-key', required=True, help=u"""Unique attribute key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_attribute_tag(ctx, from_json, catalog_id, data_asset_key, entity_key, attribute_key, tag_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(attribute_key, six.string_types) and len(attribute_key.strip()) == 0:
        raise click.UsageError('Parameter --attribute-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_attribute_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        attribute_key=attribute_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@catalog_group.command(name=cli_util.override('data_catalog.delete_catalog.command_name', 'delete'), help=u"""Deletes a data catalog resource by identifier. \n[Command Reference](deleteCatalog)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
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
def delete_catalog(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_catalog(
        catalog_id=catalog_id,
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


@catalog_private_endpoint_group.command(name=cli_util.override('data_catalog.delete_catalog_private_endpoint.command_name', 'delete'), help=u"""Deletes a private reverse connection endpoint by identifier. \n[Command Reference](deleteCatalogPrivateEndpoint)""")
@cli_util.option('--catalog-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
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
def delete_catalog_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_private_endpoint_id, if_match):

    if isinstance(catalog_private_endpoint_id, six.string_types) and len(catalog_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_catalog_private_endpoint(
        catalog_private_endpoint_id=catalog_private_endpoint_id,
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


@connection_group.command(name=cli_util.override('data_catalog.delete_connection.command_name', 'delete'), help=u"""Deletes a specific connection of a data asset. \n[Command Reference](deleteConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-key', required=True, help=u"""Unique connection key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_connection(ctx, from_json, catalog_id, data_asset_key, connection_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@custom_property_group.command(name=cli_util.override('data_catalog.delete_custom_property.command_name', 'delete'), help=u"""Deletes a specific custom property identified by it's key. \n[Command Reference](deleteCustomProperty)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--custom-property-key', required=True, help=u"""Unique Custom Property key""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_custom_property(ctx, from_json, catalog_id, namespace_id, custom_property_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    if isinstance(custom_property_key, six.string_types) and len(custom_property_key.strip()) == 0:
        raise click.UsageError('Parameter --custom-property-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_custom_property(
        catalog_id=catalog_id,
        namespace_id=namespace_id,
        custom_property_key=custom_property_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.delete_data_asset.command_name', 'delete'), help=u"""Deletes a specific data asset identified by it's key. \n[Command Reference](deleteDataAsset)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_asset(ctx, from_json, catalog_id, data_asset_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_data_asset(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_tag_group.command(name=cli_util.override('data_catalog.delete_data_asset_tag.command_name', 'delete'), help=u"""Deletes a specific data asset tag. \n[Command Reference](deleteDataAssetTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_data_asset_tag(ctx, from_json, catalog_id, data_asset_key, tag_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_data_asset_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@entity_group.command(name=cli_util.override('data_catalog.delete_entity.command_name', 'delete'), help=u"""Deletes a specific data entity. \n[Command Reference](deleteEntity)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_entity(ctx, from_json, catalog_id, data_asset_key, entity_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_entity(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@entity_tag_group.command(name=cli_util.override('data_catalog.delete_entity_tag.command_name', 'delete'), help=u"""Deletes a specific entity tag. \n[Command Reference](deleteEntityTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_entity_tag(ctx, from_json, catalog_id, data_asset_key, entity_key, tag_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_entity_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_catalog.delete_folder.command_name', 'delete'), help=u"""Deletes a specific folder of a data asset identified by it's key. \n[Command Reference](deleteFolder)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--folder-key', required=True, help=u"""Unique folder key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_folder(ctx, from_json, catalog_id, data_asset_key, folder_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_folder(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        folder_key=folder_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_tag_group.command(name=cli_util.override('data_catalog.delete_folder_tag.command_name', 'delete'), help=u"""Deletes a specific folder tag. \n[Command Reference](deleteFolderTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--folder-key', required=True, help=u"""Unique folder key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_folder_tag(ctx, from_json, catalog_id, data_asset_key, folder_key, tag_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_folder_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        folder_key=folder_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@glossary_group.command(name=cli_util.override('data_catalog.delete_glossary.command_name', 'delete'), help=u"""Deletes a specific glossary identified by it's key. \n[Command Reference](deleteGlossary)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_glossary(ctx, from_json, catalog_id, glossary_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_glossary(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('data_catalog.delete_job.command_name', 'delete'), help=u"""Deletes a specific job identified by it's key. \n[Command Reference](deleteJob)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_job(ctx, from_json, catalog_id, job_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_job(
        catalog_id=catalog_id,
        job_key=job_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_definition_group.command(name=cli_util.override('data_catalog.delete_job_definition.command_name', 'delete'), help=u"""Deletes a specific job definition identified by it's key. \n[Command Reference](deleteJobDefinition)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-definition-key', required=True, help=u"""Unique job definition key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_job_definition(ctx, from_json, catalog_id, job_definition_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_definition_key, six.string_types) and len(job_definition_key.strip()) == 0:
        raise click.UsageError('Parameter --job-definition-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_job_definition(
        catalog_id=catalog_id,
        job_definition_key=job_definition_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@metastore_group.command(name=cli_util.override('data_catalog.delete_metastore.command_name', 'delete'), help=u"""Deletes a metastore resource by identifier. \n[Command Reference](deleteMetastore)""")
@cli_util.option('--metastore-id', required=True, help=u"""The metastore's OCID.""")
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
def delete_metastore(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, metastore_id, if_match):

    if isinstance(metastore_id, six.string_types) and len(metastore_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_metastore(
        metastore_id=metastore_id,
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


@namespace_group.command(name=cli_util.override('data_catalog.delete_namespace.command_name', 'delete'), help=u"""Deletes a specific Namespace identified by it's key. \n[Command Reference](deleteNamespace)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_namespace(ctx, from_json, catalog_id, namespace_id, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_namespace(
        catalog_id=catalog_id,
        namespace_id=namespace_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@pattern_group.command(name=cli_util.override('data_catalog.delete_pattern.command_name', 'delete'), help=u"""Deletes a specific pattern identified by it's key. \n[Command Reference](deletePattern)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--pattern-key', required=True, help=u"""Unique pattern key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_pattern(ctx, from_json, catalog_id, pattern_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(pattern_key, six.string_types) and len(pattern_key.strip()) == 0:
        raise click.UsageError('Parameter --pattern-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_pattern(
        catalog_id=catalog_id,
        pattern_key=pattern_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@term_group.command(name=cli_util.override('data_catalog.delete_term.command_name', 'delete'), help=u"""Deletes a specific glossary term. \n[Command Reference](deleteTerm)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_term(ctx, from_json, catalog_id, glossary_key, term_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_term(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        term_key=term_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@term_relationship_group.command(name=cli_util.override('data_catalog.delete_term_relationship.command_name', 'delete'), help=u"""Deletes a specific glossary term relationship. \n[Command Reference](deleteTermRelationship)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--term-relationship-key', required=True, help=u"""Unique glossary term relationship key.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_term_relationship(ctx, from_json, catalog_id, glossary_key, term_key, term_relationship_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')

    if isinstance(term_relationship_key, six.string_types) and len(term_relationship_key.strip()) == 0:
        raise click.UsageError('Parameter --term-relationship-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.delete_term_relationship(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        term_key=term_key,
        term_relationship_key=term_relationship_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@catalog_group.command(name=cli_util.override('data_catalog.detach_catalog_private_endpoint.command_name', 'detach'), help=u"""Detaches a private reverse connection endpoint resource to a data catalog resource. When provided, 'If-Match' is checked against 'ETag' values of the resource. \n[Command Reference](detachCatalogPrivateEndpoint)""")
@cli_util.option('--catalog-private-endpoint-id', required=True, help=u"""The identifier of the private endpoint to be detached from catalog resource.""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def detach_catalog_private_endpoint(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_private_endpoint_id, catalog_id, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['catalogPrivateEndpointId'] = catalog_private_endpoint_id

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.detach_catalog_private_endpoint(
        catalog_id=catalog_id,
        detach_catalog_private_endpoint_details=_details,
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


@type_group.command(name=cli_util.override('data_catalog.disassociate_custom_property.command_name', 'disassociate-custom-property'), help=u"""Remove the custom property for the given type \n[Command Reference](disassociateCustomProperty)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--type-key', required=True, help=u"""Unique type key.""")
@cli_util.option('--custom-property-ids', type=custom_types.CLI_COMPLEX_TYPE, help=u"""array of custom property Ids""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-event-enabled', type=click.BOOL, help=u"""If an OCI Event will be emitted when the custom property is modified.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-ids': {'module': 'data_catalog', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-ids': {'module': 'data_catalog', 'class': 'list[string]'}}, output_type={'module': 'data_catalog', 'class': 'Type'})
@cli_util.wrap_exceptions
def disassociate_custom_property(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, type_key, custom_property_ids, is_event_enabled, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(type_key, six.string_types) and len(type_key.strip()) == 0:
        raise click.UsageError('Parameter --type-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if custom_property_ids is not None:
        _details['customPropertyIds'] = cli_util.parse_json_parameter("custom_property_ids", custom_property_ids)

    if is_event_enabled is not None:
        _details['isEventEnabled'] = is_event_enabled

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.disassociate_custom_property(
        catalog_id=catalog_id,
        type_key=type_key,
        disassociate_custom_property_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_type') and callable(getattr(client, 'get_type')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_type(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@glossary_group.command(name=cli_util.override('data_catalog.expand_tree_for_glossary.command_name', 'expand-tree-for'), help=u"""Returns the fully expanded tree hierarchy of parent and child terms in this glossary. \n[Command Reference](expandTreeForGlossary)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'list[GlossaryTreeElement]'})
@cli_util.wrap_exceptions
def expand_tree_for_glossary(ctx, from_json, catalog_id, glossary_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.expand_tree_for_glossary(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@glossary_group.command(name=cli_util.override('data_catalog.export_glossary.command_name', 'export'), help=u"""Export the glossary and the terms and return the exported glossary as csv or json. \n[Command Reference](exportGlossary)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--is-relationship-exported', type=click.BOOL, help=u"""Specify if the relationship metadata is exported for the glossary.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def export_glossary(ctx, from_json, catalog_id, glossary_key, is_relationship_exported):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    kwargs = {}
    if is_relationship_exported is not None:
        kwargs['is_relationship_exported'] = is_relationship_exported
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.export_glossary(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@attribute_group.command(name=cli_util.override('data_catalog.get_attribute.command_name', 'get'), help=u"""Gets a specific entity attribute by key. \n[Command Reference](getAttribute)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--attribute-key', required=True, help=u"""Unique attribute key.""")
@cli_util.option('--is-include-object-relationships', type=click.BOOL, help=u"""Indicates whether the list of objects and their relationships to this object will be provided in the response.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "entityKey", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "externalDataType", "externalKey", "isIncrementalData", "isNullable", "length", "position", "precision", "scale", "timeExternal", "uri", "properties", "path", "minCollectionCount", "maxCollectionCount", "datatypeEntityKey", "externalDatatypeEntityKey", "parentAttributeKey", "externalParentAttributeKey"]), multiple=True, help=u"""Specifies the fields to return in an entity attribute response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Attribute'})
@cli_util.wrap_exceptions
def get_attribute(ctx, from_json, catalog_id, data_asset_key, entity_key, attribute_key, is_include_object_relationships, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(attribute_key, six.string_types) and len(attribute_key.strip()) == 0:
        raise click.UsageError('Parameter --attribute-key cannot be whitespace or empty string')

    kwargs = {}
    if is_include_object_relationships is not None:
        kwargs['is_include_object_relationships'] = is_include_object_relationships
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_attribute(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        attribute_key=attribute_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@attribute_tag_group.command(name=cli_util.override('data_catalog.get_attribute_tag.command_name', 'get'), help=u"""Gets a specific entity attribute tag by key. \n[Command Reference](getAttributeTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--attribute-key', required=True, help=u"""Unique attribute key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "createdById", "uri", "attributeKey"]), multiple=True, help=u"""Specifies the fields to return in an entity attribute tag response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'AttributeTag'})
@cli_util.wrap_exceptions
def get_attribute_tag(ctx, from_json, catalog_id, data_asset_key, entity_key, attribute_key, tag_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(attribute_key, six.string_types) and len(attribute_key.strip()) == 0:
        raise click.UsageError('Parameter --attribute-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_attribute_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        attribute_key=attribute_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@catalog_group.command(name=cli_util.override('data_catalog.get_catalog.command_name', 'get'), help=u"""Gets a data catalog by identifier. \n[Command Reference](getCatalog)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Catalog'})
@cli_util.wrap_exceptions
def get_catalog(ctx, from_json, catalog_id):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_catalog(
        catalog_id=catalog_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@catalog_private_endpoint_group.command(name=cli_util.override('data_catalog.get_catalog_private_endpoint.command_name', 'get'), help=u"""Gets a specific private reverse connection by identifier. \n[Command Reference](getCatalogPrivateEndpoint)""")
@cli_util.option('--catalog-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'CatalogPrivateEndpoint'})
@cli_util.wrap_exceptions
def get_catalog_private_endpoint(ctx, from_json, catalog_private_endpoint_id):

    if isinstance(catalog_private_endpoint_id, six.string_types) and len(catalog_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-private-endpoint-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_catalog_private_endpoint(
        catalog_private_endpoint_id=catalog_private_endpoint_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@connection_group.command(name=cli_util.override('data_catalog.get_connection.command_name', 'get'), help=u"""Gets a specific data asset connection by key. \n[Command Reference](getConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-key', required=True, help=u"""Unique connection key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "dataAssetKey", "typeKey", "timeCreated", "timeUpdated", "createdById", "updatedById", "properties", "externalKey", "timeStatusUpdated", "lifecycleState", "isDefault", "uri"]), multiple=True, help=u"""Specifies the fields to return in a connection response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Connection'})
@cli_util.wrap_exceptions
def get_connection(ctx, from_json, catalog_id, data_asset_key, connection_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@custom_property_group.command(name=cli_util.override('data_catalog.get_custom_property.command_name', 'get'), help=u"""Gets a specific custom property for the given key within a data catalog. \n[Command Reference](getCustomProperty)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--custom-property-key', required=True, help=u"""Unique Custom Property key""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "dataType", "namespaceName", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "properties"]), multiple=True, help=u"""Specifies the fields to return in a custom property response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'CustomProperty'})
@cli_util.wrap_exceptions
def get_custom_property(ctx, from_json, catalog_id, namespace_id, custom_property_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    if isinstance(custom_property_key, six.string_types) and len(custom_property_key.strip()) == 0:
        raise click.UsageError('Parameter --custom-property-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_custom_property(
        catalog_id=catalog_id,
        namespace_id=namespace_id,
        custom_property_key=custom_property_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.get_data_asset.command_name', 'get'), help=u"""Gets a specific data asset for the given key within a data catalog. \n[Command Reference](getDataAsset)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "externalKey", "typeKey", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "uri", "properties"]), multiple=True, help=u"""Specifies the fields to return in a data asset response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def get_data_asset(ctx, from_json, catalog_id, data_asset_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_data_asset(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_tag_group.command(name=cli_util.override('data_catalog.get_data_asset_tag.command_name', 'get'), help=u"""Gets a specific data asset tag by key. \n[Command Reference](getDataAssetTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "createdById", "uri", "dataAssetKey"]), multiple=True, help=u"""Specifies the fields to return in a data asset tag response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'DataAssetTag'})
@cli_util.wrap_exceptions
def get_data_asset_tag(ctx, from_json, catalog_id, data_asset_key, tag_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_data_asset_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@entity_group.command(name=cli_util.override('data_catalog.get_entity.command_name', 'get'), help=u"""Gets a specific data entity by key for a data asset. \n[Command Reference](getEntity)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--is-include-object-relationships', type=click.BOOL, help=u"""Indicates whether the list of objects and their relationships to this object will be provided in the response.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "dataAssetKey", "timeCreated", "timeUpdated", "createdById", "updatedById", "lifecycleState", "externalKey", "timeExternal", "timeStatusUpdated", "isLogical", "isPartition", "folderKey", "folderName", "typeKey", "path", "harvestStatus", "lastJobKey", "uri", "properties"]), multiple=True, help=u"""Specifies the fields to return in an entity response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Entity'})
@cli_util.wrap_exceptions
def get_entity(ctx, from_json, catalog_id, data_asset_key, entity_key, is_include_object_relationships, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    if is_include_object_relationships is not None:
        kwargs['is_include_object_relationships'] = is_include_object_relationships
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_entity(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@entity_tag_group.command(name=cli_util.override('data_catalog.get_entity_tag.command_name', 'get'), help=u"""Gets a specific entity tag by key. \n[Command Reference](getEntityTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "createdById", "uri", "entityKey"]), multiple=True, help=u"""Specifies the fields to return in an entity tag response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'EntityTag'})
@cli_util.wrap_exceptions
def get_entity_tag(ctx, from_json, catalog_id, data_asset_key, entity_key, tag_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_entity_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_group.command(name=cli_util.override('data_catalog.get_folder.command_name', 'get'), help=u"""Gets a specific data asset folder by key. \n[Command Reference](getFolder)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--folder-key', required=True, help=u"""Unique folder key.""")
@cli_util.option('--is-include-object-relationships', type=click.BOOL, help=u"""Indicates whether the list of objects and their relationships to this object will be provided in the response.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "parentFolderKey", "path", "dataAssetKey", "properties", "externalKey", "timeCreated", "timeUpdated", "createdById", "updatedById", "timeExternal", "lifecycleState", "harvestStatus", "lastJobKey", "uri"]), multiple=True, help=u"""Specifies the fields to return in a folder response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Folder'})
@cli_util.wrap_exceptions
def get_folder(ctx, from_json, catalog_id, data_asset_key, folder_key, is_include_object_relationships, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    if is_include_object_relationships is not None:
        kwargs['is_include_object_relationships'] = is_include_object_relationships
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_folder(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        folder_key=folder_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@folder_tag_group.command(name=cli_util.override('data_catalog.get_folder_tag.command_name', 'get'), help=u"""Gets a specific folder tag by key. \n[Command Reference](getFolderTag)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--folder-key', required=True, help=u"""Unique folder key.""")
@cli_util.option('--tag-key', required=True, help=u"""Unique tag key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "createdById", "uri", "folderKey"]), multiple=True, help=u"""Specifies the fields to return in a folder tag response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'FolderTag'})
@cli_util.wrap_exceptions
def get_folder_tag(ctx, from_json, catalog_id, data_asset_key, folder_key, tag_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    if isinstance(tag_key, six.string_types) and len(tag_key.strip()) == 0:
        raise click.UsageError('Parameter --tag-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_folder_tag(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        folder_key=folder_key,
        tag_key=tag_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@glossary_group.command(name=cli_util.override('data_catalog.get_glossary.command_name', 'get'), help=u"""Gets a specific glossary by key within a data catalog. \n[Command Reference](getGlossary)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "owner", "workflowStatus", "uri"]), multiple=True, help=u"""Specifies the fields to return in a glossary response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Glossary'})
@cli_util.wrap_exceptions
def get_glossary(ctx, from_json, catalog_id, glossary_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_glossary(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_group.command(name=cli_util.override('data_catalog.get_job.command_name', 'get'), help=u"""Gets a specific job by key within a data catalog. \n[Command Reference](getJob)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "lifecycleState", "timeCreated", "timeUpdated", "jobType", "scheduleCronExpression", "timeScheduleBegin", "timeScheduleEnd", "scheduleType", "connectionKey", "jobDefinitionKey", "internalVersion", "executionCount", "timeOfLatestExecution", "executions", "createdById", "updatedById", "uri", "jobDefinitionName", "errorCode", "errorMessage"]), multiple=True, help=u"""Specifies the fields to return in a job response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Job'})
@cli_util.wrap_exceptions
def get_job(ctx, from_json, catalog_id, job_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_job(
        catalog_id=catalog_id,
        job_key=job_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_definition_group.command(name=cli_util.override('data_catalog.get_job_definition.command_name', 'get'), help=u"""Gets a specific job definition by key within a data catalog. \n[Command Reference](getJobDefinition)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-definition-key', required=True, help=u"""Unique job definition key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "jobType", "isIncremental", "dataAssetKey", "connectionKey", "internalVersion", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "uri", "isSampleDataExtracted", "sampleDataSizeInMBs", "timeLatestExecutionStarted", "timeLatestExecutionEnded", "jobExecutionState", "scheduleType", "properties"]), multiple=True, help=u"""Specifies the fields to return in a job definition response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobDefinition'})
@cli_util.wrap_exceptions
def get_job_definition(ctx, from_json, catalog_id, job_definition_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_definition_key, six.string_types) and len(job_definition_key.strip()) == 0:
        raise click.UsageError('Parameter --job-definition-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_job_definition(
        catalog_id=catalog_id,
        job_definition_key=job_definition_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_execution_group.command(name=cli_util.override('data_catalog.get_job_execution.command_name', 'get'), help=u"""Gets a specific job execution by key. \n[Command Reference](getJobExecution)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--job-execution-key', required=True, help=u"""The key of the job execution.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "jobKey", "jobType", "subType", "parentKey", "scheduleInstanceKey", "lifecycleState", "timeCreated", "timeStarted", "timeEnded", "errorCode", "errorMessage", "processKey", "externalUrl", "eventKey", "dataEntityKey", "createdById", "updatedById", "properties", "uri"]), multiple=True, help=u"""Specifies the fields to return in a job execution response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobExecution'})
@cli_util.wrap_exceptions
def get_job_execution(ctx, from_json, catalog_id, job_key, job_execution_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    if isinstance(job_execution_key, six.string_types) and len(job_execution_key.strip()) == 0:
        raise click.UsageError('Parameter --job-execution-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_job_execution(
        catalog_id=catalog_id,
        job_key=job_key,
        job_execution_key=job_execution_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_log_group.command(name=cli_util.override('data_catalog.get_job_log.command_name', 'get'), help=u"""Gets a specific job log by key. \n[Command Reference](getJobLog)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--job-execution-key', required=True, help=u"""The key of the job execution.""")
@cli_util.option('--job-log-key', required=True, help=u"""Unique job log key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "jobExecutionKey", "createdById", "updatedById", "timeUpdated", "timeCreated", "severity", "logMessage", "uri"]), multiple=True, help=u"""Specifies the fields to return in a job log response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobLog'})
@cli_util.wrap_exceptions
def get_job_log(ctx, from_json, catalog_id, job_key, job_execution_key, job_log_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    if isinstance(job_execution_key, six.string_types) and len(job_execution_key.strip()) == 0:
        raise click.UsageError('Parameter --job-execution-key cannot be whitespace or empty string')

    if isinstance(job_log_key, six.string_types) and len(job_log_key.strip()) == 0:
        raise click.UsageError('Parameter --job-log-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_job_log(
        catalog_id=catalog_id,
        job_key=job_key,
        job_execution_key=job_execution_key,
        job_log_key=job_log_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@job_metric_group.command(name=cli_util.override('data_catalog.get_job_metrics.command_name', 'get'), help=u"""Gets a specific job metric by key. \n[Command Reference](getJobMetrics)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--job-execution-key', required=True, help=u"""The key of the job execution.""")
@cli_util.option('--job-metrics-key', required=True, help=u"""Unique job metrics key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "description", "displayName", "timeInserted", "category", "subCategory", "unit", "value", "batchKey", "jobExecutionKey", "createdById", "updatedById", "timeUpdated", "timeCreated", "uri"]), multiple=True, help=u"""Specifies the fields to return in a job metric response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobMetric'})
@cli_util.wrap_exceptions
def get_job_metrics(ctx, from_json, catalog_id, job_key, job_execution_key, job_metrics_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    if isinstance(job_execution_key, six.string_types) and len(job_execution_key.strip()) == 0:
        raise click.UsageError('Parameter --job-execution-key cannot be whitespace or empty string')

    if isinstance(job_metrics_key, six.string_types) and len(job_metrics_key.strip()) == 0:
        raise click.UsageError('Parameter --job-metrics-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_job_metrics(
        catalog_id=catalog_id,
        job_key=job_key,
        job_execution_key=job_execution_key,
        job_metrics_key=job_metrics_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@metastore_group.command(name=cli_util.override('data_catalog.get_metastore.command_name', 'get'), help=u"""Gets a metastore by identifier. \n[Command Reference](getMetastore)""")
@cli_util.option('--metastore-id', required=True, help=u"""The metastore's OCID.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Metastore'})
@cli_util.wrap_exceptions
def get_metastore(ctx, from_json, metastore_id):

    if isinstance(metastore_id, six.string_types) and len(metastore_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_metastore(
        metastore_id=metastore_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('data_catalog.get_namespace.command_name', 'get'), help=u"""Gets a specific namespace for the given key within a data catalog. \n[Command Reference](getNamespace)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "properties"]), multiple=True, help=u"""Specifies the fields to return in a namespace response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Namespace'})
@cli_util.wrap_exceptions
def get_namespace(ctx, from_json, catalog_id, namespace_id, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_namespace(
        catalog_id=catalog_id,
        namespace_id=namespace_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@pattern_group.command(name=cli_util.override('data_catalog.get_pattern.command_name', 'get'), help=u"""Gets a specific pattern for the given key within a data catalog. \n[Command Reference](getPattern)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--pattern-key', required=True, help=u"""Unique pattern key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "expression", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "properties"]), multiple=True, help=u"""Specifies the fields to return in a pattern response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Pattern'})
@cli_util.wrap_exceptions
def get_pattern(ctx, from_json, catalog_id, pattern_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(pattern_key, six.string_types) and len(pattern_key.strip()) == 0:
        raise click.UsageError('Parameter --pattern-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_pattern(
        catalog_id=catalog_id,
        pattern_key=pattern_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@term_group.command(name=cli_util.override('data_catalog.get_term.command_name', 'get'), help=u"""Gets a specific glossary term by key. \n[Command Reference](getTerm)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "glossaryKey", "parentTermKey", "isAllowedToHaveChildTerms", "path", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "owner", "workflowStatus", "uri", "relatedTerms", "associatedObjectCount", "associatedObjects"]), multiple=True, help=u"""Specifies the fields to return in a term response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Term'})
@cli_util.wrap_exceptions
def get_term(ctx, from_json, catalog_id, glossary_key, term_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_term(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        term_key=term_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@term_relationship_group.command(name=cli_util.override('data_catalog.get_term_relationship.command_name', 'get'), help=u"""Gets a specific glossary term relationship by key. \n[Command Reference](getTermRelationship)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--term-relationship-key', required=True, help=u"""Unique glossary term relationship key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "relatedTermKey", "relatedTermDisplayName", "parentTermKey", "parentTermDisplayName", "lifecycleState", "timeCreated", "uri"]), multiple=True, help=u"""Specifies the fields to return in a term relationship response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'TermRelationship'})
@cli_util.wrap_exceptions
def get_term_relationship(ctx, from_json, catalog_id, glossary_key, term_key, term_relationship_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')

    if isinstance(term_relationship_key, six.string_types) and len(term_relationship_key.strip()) == 0:
        raise click.UsageError('Parameter --term-relationship-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_term_relationship(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        term_key=term_key,
        term_relationship_key=term_relationship_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@type_group.command(name=cli_util.override('data_catalog.get_type.command_name', 'get'), help=u"""Gets a specific type by key within a data catalog. \n[Command Reference](getType)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--type-key', required=True, help=u"""Unique type key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "description", "name", "catalogId", "properties", "isInternal", "isTag", "isApproved", "typeCategory", "externalTypeName", "lifecycleState", "uri"]), multiple=True, help=u"""Specifies the fields to return in a type response.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Type'})
@cli_util.wrap_exceptions
def get_type(ctx, from_json, catalog_id, type_key, fields):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(type_key, six.string_types) and len(type_key.strip()) == 0:
        raise click.UsageError('Parameter --type-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_type(
        catalog_id=catalog_id,
        type_key=type_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@work_request_group.command(name=cli_util.override('data_catalog.get_work_request.command_name', 'get'), help=u"""Gets the status of the work request with the given OCID. \n[Command Reference](getWorkRequest)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the asynchronous request.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'WorkRequest'})
@cli_util.wrap_exceptions
def get_work_request(ctx, from_json, work_request_id):

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.get_work_request(
        work_request_id=work_request_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.import_connection.command_name', 'import-connection'), help=u"""Import new connection for this data asset. \n[Command Reference](importConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-payload', required=True, help=u"""The information used to import the connection.""")
@cli_util.option('--connection-detail', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'connection-detail': {'module': 'data_catalog', 'class': 'CreateConnectionDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-detail': {'module': 'data_catalog', 'class': 'CreateConnectionDetails'}}, output_type={'module': 'data_catalog', 'class': 'Connection'})
@cli_util.wrap_exceptions
def import_connection(ctx, from_json, catalog_id, data_asset_key, connection_payload, connection_detail, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['connectionPayload'] = connection_payload

    if connection_detail is not None:
        _details['connectionDetail'] = cli_util.parse_json_parameter("connection_detail", connection_detail)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.import_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        import_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.import_data_asset.command_name', 'import'), help=u"""Import technical objects to a Data Asset \n[Command Reference](importDataAsset)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--import-file-contents', required=True, help=u"""The file contents to be imported. File size not to exceed 10 MB.""")
@cli_util.option('--import-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CUSTOM_PROPERTY_VALUES", "ALL"]), multiple=True, help=u"""Type of import.""")
@cli_util.option('--is-missing-value-ignored', type=click.BOOL, help=u"""Specify whether to ignore the missing values in the import file.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'ImportDataAssetJobResult'})
@cli_util.wrap_exceptions
def import_data_asset(ctx, from_json, catalog_id, data_asset_key, import_file_contents, import_type, is_missing_value_ignored):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if is_missing_value_ignored is not None:
        kwargs['is_missing_value_ignored'] = is_missing_value_ignored
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['importFileContents'] = import_file_contents

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.import_data_asset(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        import_type=import_type,
        import_data_asset_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@glossary_group.command(name=cli_util.override('data_catalog.import_glossary.command_name', 'import'), help=u"""Import the glossary and the terms from csv or json files and return the imported glossary resource. \n[Command Reference](importGlossary)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--glossary-file-contents', help=u"""The file contents used for the import of glossary.""")
@cli_util.option('--is-relationship-imported', type=click.BOOL, help=u"""Specify if the relationship metadata is imported for the glossary.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def import_glossary(ctx, from_json, catalog_id, glossary_key, glossary_file_contents, is_relationship_imported):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    kwargs = {}
    if is_relationship_imported is not None:
        kwargs['is_relationship_imported'] = is_relationship_imported
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if glossary_file_contents is not None:
        _details['glossaryFileContents'] = glossary_file_contents

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.import_glossary(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        import_glossary_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@entity_group.command(name=cli_util.override('data_catalog.list_aggregated_physical_entities.command_name', 'list-aggregated-physical'), help=u"""List the physical entities aggregated by this logical entity. \n[Command Reference](listAggregatedPhysicalEntities)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "dataAssetKey", "timeCreated", "timeUpdated", "createdById", "updatedById", "lifecycleState", "externalKey", "timeExternal", "timeStatusUpdated", "isLogical", "isPartition", "folderKey", "folderName", "typeKey", "path", "harvestStatus", "lastJobKey", "uri", "properties"]), multiple=True, help=u"""Specifies the fields to return in an entity response.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'EntityCollection'})
@cli_util.wrap_exceptions
def list_aggregated_physical_entities(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, entity_key, fields, display_name_contains, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_aggregated_physical_entities,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_aggregated_physical_entities,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    else:
        result = client.list_aggregated_physical_entities(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@attribute_tag_collection_group.command(name=cli_util.override('data_catalog.list_attribute_tags.command_name', 'list-attribute-tags'), help=u"""Returns a list of all tags for an entity attribute. \n[Command Reference](listAttributeTags)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--attribute-key', required=True, help=u"""Unique attribute key.""")
@cli_util.option('--name', help=u"""Immutable resource name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term.""")
@cli_util.option('--term-path', help=u"""Path of the related term.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "uri", "glossaryKey", "attributeKey"]), multiple=True, help=u"""Specifies the fields to return in an entity attribute tag summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'AttributeTagCollection'})
@cli_util.wrap_exceptions
def list_attribute_tags(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, entity_key, attribute_key, name, lifecycle_state, term_key, term_path, time_created, created_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(attribute_key, six.string_types) and len(attribute_key.strip()) == 0:
        raise click.UsageError('Parameter --attribute-key cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if term_key is not None:
        kwargs['term_key'] = term_key
    if term_path is not None:
        kwargs['term_path'] = term_path
    if time_created is not None:
        kwargs['time_created'] = time_created
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_attribute_tags,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            attribute_key=attribute_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_attribute_tags,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            attribute_key=attribute_key,
            **kwargs
        )
    else:
        result = client.list_attribute_tags(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            attribute_key=attribute_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@attribute_collection_group.command(name=cli_util.override('data_catalog.list_attributes.command_name', 'list-attributes'), help=u"""Returns a list of all attributes of an data entity. \n[Command Reference](listAttributes)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--business-name', help=u"""A filter to return only resources that match the entire business name given. The match is not case sensitive.""")
@cli_util.option('--display-or-business-name-contains', help=u"""A filter to return only resources that match display name or business name pattern given. The match is not case sensitive. For Example : /folders?displayOrBusinessNameContains=Cu.* The above would match all folders with display name or business name that starts with \"Cu\".""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--external-key', help=u"""Unique external identifier of this resource in the external source system.""")
@cli_util.option('--time-external', type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of this object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--external-type-name', help=u"""Data type as defined in an external system.""")
@cli_util.option('--is-incremental-data', type=click.BOOL, help=u"""Identifies whether this attribute can be used as a watermark to extract incremental data.""")
@cli_util.option('--is-nullable', type=click.BOOL, help=u"""Identifies whether this attribute can be assigned null value.""")
@cli_util.option('--length', type=click.INT, help=u"""Max allowed length of the attribute value.""")
@cli_util.option('--position', type=click.INT, help=u"""Position of the attribute in the record definition.""")
@cli_util.option('--precision', type=click.INT, help=u"""Precision of the attribute value usually applies to float data type.""")
@cli_util.option('--scale', type=click.INT, help=u"""Scale of the attribute value usually applies to float data type.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "entityKey", "lifecycleState", "timeCreated", "externalDataType", "externalKey", "length", "precision", "scale", "isNullable", "uri", "path", "minCollectionCount", "maxCollectionCount", "datatypeEntityKey", "externalDatatypeEntityKey", "parentAttributeKey", "externalParentAttributeKey", "position"]), multiple=True, help=u"""Specifies the fields to return in an entity attribute summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME", "POSITION"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. Default order for POSITION is ascending. If no value is specified POSITION is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'AttributeCollection'})
@cli_util.wrap_exceptions
def list_attributes(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, entity_key, display_name, business_name, display_or_business_name_contains, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, external_key, time_external, external_type_name, is_incremental_data, is_nullable, length, position, precision, scale, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if business_name is not None:
        kwargs['business_name'] = business_name
    if display_or_business_name_contains is not None:
        kwargs['display_or_business_name_contains'] = display_or_business_name_contains
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if external_key is not None:
        kwargs['external_key'] = external_key
    if time_external is not None:
        kwargs['time_external'] = time_external
    if external_type_name is not None:
        kwargs['external_type_name'] = external_type_name
    if is_incremental_data is not None:
        kwargs['is_incremental_data'] = is_incremental_data
    if is_nullable is not None:
        kwargs['is_nullable'] = is_nullable
    if length is not None:
        kwargs['length'] = length
    if position is not None:
        kwargs['position'] = position
    if precision is not None:
        kwargs['precision'] = precision
    if scale is not None:
        kwargs['scale'] = scale
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_attributes,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_attributes,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    else:
        result = client.list_attributes(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@catalog_private_endpoint_group.command(name=cli_util.override('data_catalog.list_catalog_private_endpoints.command_name', 'list'), help=u"""Returns a list of all the catalog private endpoints in the specified compartment. \n[Command Reference](listCatalogPrivateEndpoints)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'list[CatalogPrivateEndpointSummary]'})
@cli_util.wrap_exceptions
def list_catalog_private_endpoints(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_catalog_private_endpoints,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_catalog_private_endpoints,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_catalog_private_endpoints(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@catalog_group.command(name=cli_util.override('data_catalog.list_catalogs.command_name', 'list'), help=u"""Returns a list of all the data catalogs in the specified compartment. \n[Command Reference](listCatalogs)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'list[CatalogSummary]'})
@cli_util.wrap_exceptions
def list_catalogs(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_catalogs,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_catalogs,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_catalogs(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@connection_collection_group.command(name=cli_util.override('data_catalog.list_connections.command_name', 'list-connections'), help=u"""Returns a list of all Connections for a data asset. \n[Command Reference](listConnections)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--external-key', help=u"""Unique external identifier of this resource in the external source system.""")
@cli_util.option('--time-status-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource's status was last updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--is-default', type=click.BOOL, help=u"""Indicates whether this connection is the default connection.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "dataAssetKey", "typeKey", "timeCreated", "externalKey", "lifecycleState", "isDefault", "uri"]), multiple=True, help=u"""Specifies the fields to return in a connection summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'ConnectionCollection'})
@cli_util.wrap_exceptions
def list_connections(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, display_name, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, external_key, time_status_updated, is_default, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if external_key is not None:
        kwargs['external_key'] = external_key
    if time_status_updated is not None:
        kwargs['time_status_updated'] = time_status_updated
    if is_default is not None:
        kwargs['is_default'] = is_default
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_connections,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_connections,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    else:
        result = client.list_connections(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@custom_property_group.command(name=cli_util.override('data_catalog.list_custom_properties.command_name', 'list'), help=u"""Returns a list of custom properties within a data catalog. \n[Command Reference](listCustomProperties)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--data-types', type=custom_types.CliCaseInsensitiveChoice(["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"]), multiple=True, help=u"""Return the custom properties which has specified data types""")
@cli_util.option('--type-name', type=custom_types.CliCaseInsensitiveChoice(["DATA_ASSET", "AUTONOMOUS_DATA_WAREHOUSE", "HIVE", "KAFKA", "MYSQL", "ORACLE_OBJECT_STORAGE", "AUTONOMOUS_TRANSACTION_PROCESSING", "ORACLE", "POSTGRESQL", "MICROSOFT_AZURE_SQL_DATABASE", "MICROSOFT_SQL_SERVER", "IBM_DB2", "DATA_ENTITY", "LOGICAL_ENTITY", "TABLE", "VIEW", "ATTRIBUTE", "FOLDER", "ORACLE_ANALYTICS_SUBJECT_AREA_COLUMN", "ORACLE_ANALYTICS_LOGICAL_COLUMN", "ORACLE_ANALYTICS_PHYSICAL_COLUMN", "ORACLE_ANALYTICS_ANALYSIS_COLUMN", "ORACLE_ANALYTICS_SERVER", "ORACLE_ANALYTICS_CLOUD", "ORACLE_ANALYTICS_SUBJECT_AREA", "ORACLE_ANALYTICS_DASHBOARD", "ORACLE_ANALYTICS_BUSINESS_MODEL", "ORACLE_ANALYTICS_PHYSICAL_DATABASE", "ORACLE_ANALYTICS_PHYSICAL_SCHEMA", "ORACLE_ANALYTICS_PRESENTATION_TABLE", "ORACLE_ANALYTICS_LOGICAL_TABLE", "ORACLE_ANALYTICS_PHYSICAL_TABLE", "ORACLE_ANALYTICS_ANALYSIS", "DATABASE_SCHEMA", "TOPIC", "CONNECTION", "GLOSSARY", "TERM", "CATEGORY", "FILE", "BUCKET", "MESSAGE", "UNRECOGNIZED_FILE"]), multiple=True, help=u"""A filter to return only resources that match the entire type name given. The match is not case sensitive""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "dataType", "namespaceName", "lifecycleState", "timeCreated"]), multiple=True, help=u"""Specifies the fields to return in a custom property summary response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["DISPLAYNAME", "USAGECOUNT"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for USAGECOUNT and DISPLAYNAME is Ascending""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'CustomPropertyCollection'})
@cli_util.wrap_exceptions
def list_custom_properties(ctx, from_json, all_pages, page_size, catalog_id, namespace_id, display_name, display_name_contains, data_types, type_name, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, fields, sort_order, sort_by, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if data_types is not None and len(data_types) > 0:
        kwargs['data_types'] = data_types
    if type_name is not None and len(type_name) > 0:
        kwargs['type_name'] = type_name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_custom_properties,
            catalog_id=catalog_id,
            namespace_id=namespace_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_custom_properties,
            limit,
            page_size,
            catalog_id=catalog_id,
            namespace_id=namespace_id,
            **kwargs
        )
    else:
        result = client.list_custom_properties(
            catalog_id=catalog_id,
            namespace_id=namespace_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_asset_tag_collection_group.command(name=cli_util.override('data_catalog.list_data_asset_tags.command_name', 'list-data-asset-tags'), help=u"""Returns a list of all tags for a data asset. \n[Command Reference](listDataAssetTags)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--name', help=u"""Immutable resource name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term.""")
@cli_util.option('--term-path', help=u"""Path of the related term.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "uri", "glossaryKey", "dataAssetKey"]), multiple=True, help=u"""Specifies the fields to return in a data asset tag summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'DataAssetTagCollection'})
@cli_util.wrap_exceptions
def list_data_asset_tags(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, name, lifecycle_state, term_key, term_path, time_created, created_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if term_key is not None:
        kwargs['term_key'] = term_key
    if term_path is not None:
        kwargs['term_path'] = term_path
    if time_created is not None:
        kwargs['time_created'] = time_created
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_asset_tags,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_asset_tags,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    else:
        result = client.list_data_asset_tags(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@data_asset_collection_group.command(name=cli_util.override('data_catalog.list_data_assets.command_name', 'list-data-assets'), help=u"""Returns a list of data assets within a data catalog. \n[Command Reference](listDataAssets)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--external-key', help=u"""Unique external identifier of this resource in the external source system.""")
@cli_util.option('--type-key', help=u"""The key of the object type.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "externalKey", "typeKey", "lifecycleState", "timeCreated", "uri"]), multiple=True, help=u"""Specifies the fields to return in a data asset summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'DataAssetCollection'})
@cli_util.wrap_exceptions
def list_data_assets(ctx, from_json, all_pages, page_size, catalog_id, display_name, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, external_key, type_key, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if external_key is not None:
        kwargs['external_key'] = external_key
    if type_key is not None:
        kwargs['type_key'] = type_key
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_data_assets,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_data_assets,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_data_assets(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@pattern_group.command(name=cli_util.override('data_catalog.list_derived_logical_entities.command_name', 'list-derived-logical-entities'), help=u"""List logical entities derived from this pattern. \n[Command Reference](listDerivedLogicalEntities)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--pattern-key', required=True, help=u"""Unique pattern key.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'EntityCollection'})
@cli_util.wrap_exceptions
def list_derived_logical_entities(ctx, from_json, all_pages, page_size, catalog_id, pattern_key, display_name_contains, sort_by, sort_order, limit, page, if_match):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(pattern_key, six.string_types) and len(pattern_key.strip()) == 0:
        raise click.UsageError('Parameter --pattern-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_derived_logical_entities,
            catalog_id=catalog_id,
            pattern_key=pattern_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_derived_logical_entities,
            limit,
            page_size,
            catalog_id=catalog_id,
            pattern_key=pattern_key,
            **kwargs
        )
    else:
        result = client.list_derived_logical_entities(
            catalog_id=catalog_id,
            pattern_key=pattern_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@entity_group.command(name=cli_util.override('data_catalog.list_entities.command_name', 'list'), help=u"""Returns a list of all entities of a data asset. \n[Command Reference](listEntities)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--business-name', help=u"""A filter to return only resources that match the entire business name given. The match is not case sensitive.""")
@cli_util.option('--display-or-business-name-contains', help=u"""A filter to return only resources that match display name or business name pattern given. The match is not case sensitive. For Example : /folders?displayOrBusinessNameContains=Cu.* The above would match all folders with display name or business name that starts with \"Cu\".""")
@cli_util.option('--type-key', help=u"""The key of the object type.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--external-key', help=u"""Unique external identifier of this resource in the external source system.""")
@cli_util.option('--pattern-key', help=u"""Unique pattern key.""")
@cli_util.option('--time-external', type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of this object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-status-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource's status was last updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--is-logical', type=click.BOOL, help=u"""Identifies if the object is a physical object (materialized) or virtual/logical object defined on other objects.""")
@cli_util.option('--is-partition', type=click.BOOL, help=u"""Identifies if an object is a sub object (partition) of a physical or materialized parent object.""")
@cli_util.option('--folder-key', help=u"""Key of the associated folder.""")
@cli_util.option('--path', help=u"""Full path of the resource for resources that support paths.""")
@cli_util.option('--harvest-status', type=custom_types.CliCaseInsensitiveChoice(["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]), help=u"""Harvest status of the harvestable resource as updated by the harvest process.""")
@cli_util.option('--last-job-key', help=u"""Key of the last harvest process to update this resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "dataAssetKey", "timeCreated", "timeUpdated", "updatedById", "lifecycleState", "folderKey", "folderName", "externalKey", "path", "uri"]), multiple=True, help=u"""Specifies the fields to return in an entity summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'EntityCollection'})
@cli_util.wrap_exceptions
def list_entities(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, display_name, business_name, display_or_business_name_contains, type_key, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, external_key, pattern_key, time_external, time_status_updated, is_logical, is_partition, folder_key, path, harvest_status, last_job_key, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if business_name is not None:
        kwargs['business_name'] = business_name
    if display_or_business_name_contains is not None:
        kwargs['display_or_business_name_contains'] = display_or_business_name_contains
    if type_key is not None:
        kwargs['type_key'] = type_key
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if external_key is not None:
        kwargs['external_key'] = external_key
    if pattern_key is not None:
        kwargs['pattern_key'] = pattern_key
    if time_external is not None:
        kwargs['time_external'] = time_external
    if time_status_updated is not None:
        kwargs['time_status_updated'] = time_status_updated
    if is_logical is not None:
        kwargs['is_logical'] = is_logical
    if is_partition is not None:
        kwargs['is_partition'] = is_partition
    if folder_key is not None:
        kwargs['folder_key'] = folder_key
    if path is not None:
        kwargs['path'] = path
    if harvest_status is not None:
        kwargs['harvest_status'] = harvest_status
    if last_job_key is not None:
        kwargs['last_job_key'] = last_job_key
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_entities,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_entities,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    else:
        result = client.list_entities(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@entity_tag_collection_group.command(name=cli_util.override('data_catalog.list_entity_tags.command_name', 'list-entity-tags'), help=u"""Returns a list of all tags for a data entity. \n[Command Reference](listEntityTags)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--name', help=u"""Immutable resource name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term.""")
@cli_util.option('--term-path', help=u"""Path of the related term.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "uri", "glossaryKey", "entityKey"]), multiple=True, help=u"""Specifies the fields to return in an entity tag summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'EntityTagCollection'})
@cli_util.wrap_exceptions
def list_entity_tags(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, entity_key, name, lifecycle_state, term_key, term_path, time_created, created_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if term_key is not None:
        kwargs['term_key'] = term_key
    if term_path is not None:
        kwargs['term_path'] = term_path
    if time_created is not None:
        kwargs['time_created'] = time_created
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_entity_tags,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_entity_tags,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    else:
        result = client.list_entity_tags(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@folder_tag_collection_group.command(name=cli_util.override('data_catalog.list_folder_tags.command_name', 'list-folder-tags'), help=u"""Returns a list of all tags for a folder. \n[Command Reference](listFolderTags)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--folder-key', required=True, help=u"""Unique folder key.""")
@cli_util.option('--name', help=u"""Immutable resource name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--term-key', help=u"""Unique key of the related term.""")
@cli_util.option('--term-path', help=u"""Path of the related term.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "name", "termKey", "termPath", "termDescription", "lifecycleState", "timeCreated", "uri", "glossaryKey", "folderKey"]), multiple=True, help=u"""Specifies the fields to return in a folder tag summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'FolderTagCollection'})
@cli_util.wrap_exceptions
def list_folder_tags(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, folder_key, name, lifecycle_state, term_key, term_path, time_created, created_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if term_key is not None:
        kwargs['term_key'] = term_key
    if term_path is not None:
        kwargs['term_path'] = term_path
    if time_created is not None:
        kwargs['time_created'] = time_created
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_folder_tags,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            folder_key=folder_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_folder_tags,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            folder_key=folder_key,
            **kwargs
        )
    else:
        result = client.list_folder_tags(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            folder_key=folder_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@folder_collection_group.command(name=cli_util.override('data_catalog.list_folders.command_name', 'list-folders'), help=u"""Returns a list of all folders. \n[Command Reference](listFolders)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--business-name', help=u"""A filter to return only resources that match the entire business name given. The match is not case sensitive.""")
@cli_util.option('--display-or-business-name-contains', help=u"""A filter to return only resources that match display name or business name pattern given. The match is not case sensitive. For Example : /folders?displayOrBusinessNameContains=Cu.* The above would match all folders with display name or business name that starts with \"Cu\".""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--parent-folder-key', help=u"""Unique folder key.""")
@cli_util.option('--path', help=u"""Full path of the resource for resources that support paths.""")
@cli_util.option('--external-key', help=u"""Unique external identifier of this resource in the external source system.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--harvest-status', type=custom_types.CliCaseInsensitiveChoice(["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]), help=u"""Harvest status of the harvestable resource as updated by the harvest process.""")
@cli_util.option('--last-job-key', help=u"""Key of the last harvest process to update this resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "parentFolderKey", "path", "dataAssetKey", "externalKey", "timeExternal", "timeCreated", "lifecycleState", "uri"]), multiple=True, help=u"""Specifies the fields to return in a folder summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'FolderCollection'})
@cli_util.wrap_exceptions
def list_folders(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, display_name, business_name, display_or_business_name_contains, display_name_contains, lifecycle_state, parent_folder_key, path, external_key, time_created, time_updated, created_by_id, updated_by_id, harvest_status, last_job_key, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if business_name is not None:
        kwargs['business_name'] = business_name
    if display_or_business_name_contains is not None:
        kwargs['display_or_business_name_contains'] = display_or_business_name_contains
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if parent_folder_key is not None:
        kwargs['parent_folder_key'] = parent_folder_key
    if path is not None:
        kwargs['path'] = path
    if external_key is not None:
        kwargs['external_key'] = external_key
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if harvest_status is not None:
        kwargs['harvest_status'] = harvest_status
    if last_job_key is not None:
        kwargs['last_job_key'] = last_job_key
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_folders,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_folders,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    else:
        result = client.list_folders(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@glossary_group.command(name=cli_util.override('data_catalog.list_glossaries.command_name', 'list'), help=u"""Returns a list of all glossaries within a data catalog. \n[Command Reference](listGlossaries)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "lifecycleState", "timeCreated", "uri", "workflowStatus"]), multiple=True, help=u"""Specifies the fields to return in a glossary summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'GlossaryCollection'})
@cli_util.wrap_exceptions
def list_glossaries(ctx, from_json, all_pages, page_size, catalog_id, display_name, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_glossaries,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_glossaries,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_glossaries(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_definition_collection_group.command(name=cli_util.override('data_catalog.list_job_definitions.command_name', 'list-job-definitions'), help=u"""Returns a list of job definitions within a data catalog. \n[Command Reference](listJobDefinitions)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--job-execution-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", "SUCCEEDED_WITH_WARNINGS"]), help=u"""Job execution state.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--job-type', type=custom_types.CliCaseInsensitiveChoice(["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE", "IMPORT_DATA_ASSET"]), help=u"""Job type.""")
@cli_util.option('--is-incremental', type=click.BOOL, help=u"""Whether job definition is an incremental harvest (true) or a full harvest (false).""")
@cli_util.option('--data-asset-key', help=u"""Unique data asset key.""")
@cli_util.option('--connection-key', help=u"""Unique connection key.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--sample-data-size-in-mbs', help=u"""The sample data size in MB, specified as number of rows, for a metadata harvest.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "jobType", "connectionKey", "lifecycleState", "timeCreated", "isSampleDataExtracted", "uri", "timeLatestExecutionStarted", "timeLatestExecutionEnded", "jobExecutionState", "scheduleType"]), multiple=True, help=u"""Specifies the fields to return in a job definition summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME", "TIMELATESTEXECUTIONSTARTED"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. Default order for TIMELATESTEXECUTIONSTARTED is descending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobDefinitionCollection'})
@cli_util.wrap_exceptions
def list_job_definitions(ctx, from_json, all_pages, page_size, catalog_id, display_name, display_name_contains, job_execution_state, lifecycle_state, job_type, is_incremental, data_asset_key, connection_key, time_created, time_updated, created_by_id, updated_by_id, sample_data_size_in_mbs, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if job_execution_state is not None:
        kwargs['job_execution_state'] = job_execution_state
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if job_type is not None:
        kwargs['job_type'] = job_type
    if is_incremental is not None:
        kwargs['is_incremental'] = is_incremental
    if data_asset_key is not None:
        kwargs['data_asset_key'] = data_asset_key
    if connection_key is not None:
        kwargs['connection_key'] = connection_key
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if sample_data_size_in_mbs is not None:
        kwargs['sample_data_size_in_mbs'] = sample_data_size_in_mbs
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_definitions,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_definitions,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_job_definitions(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_execution_collection_group.command(name=cli_util.override('data_catalog.list_job_executions.command_name', 'list-job-executions'), help=u"""Returns a list of job executions for a job. \n[Command Reference](listJobExecutions)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", "SUCCEEDED_WITH_WARNINGS"]), help=u"""Job execution lifecycle state.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--job-type', type=custom_types.CliCaseInsensitiveChoice(["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE", "IMPORT_DATA_ASSET"]), help=u"""Job type.""")
@cli_util.option('--sub-type', help=u"""Sub-type of this job execution.""")
@cli_util.option('--parent-key', help=u"""The unique key of the parent execution or null if this job execution has no parent.""")
@cli_util.option('--time-start', type=custom_types.CLI_DATETIME, help=u"""Time that the job execution was started or in the case of a future time, the time when the job will start. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-end', type=custom_types.CLI_DATETIME, help=u"""Time that the job execution ended or null if the job is still running or hasn't run yet. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--error-code', help=u"""Error code returned from the job execution or null if job is still running or didn't return an error.""")
@cli_util.option('--error-message', help=u"""Error message returned from the job execution or null if job is still running or didn't return an error.""")
@cli_util.option('--process-key', help=u"""Process identifier related to the job execution.""")
@cli_util.option('--external-url', help=u"""The a URL of the job for accessing this resource and its status.""")
@cli_util.option('--event-key', help=u"""Event that triggered the execution of this job or null.""")
@cli_util.option('--data-entity-key', help=u"""Unique entity key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "jobKey", "jobType", "parentKey", "scheduleInstanceKey", "lifecycleState", "timeCreated", "timeStarted", "timeEnded", "uri"]), multiple=True, help=u"""Specifies the fields to return in a job execution summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED"]), help=u"""The field to sort by. Only one sort order may be provided; the default is descending. Use sortOrder query param to specify order.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobExecutionCollection'})
@cli_util.wrap_exceptions
def list_job_executions(ctx, from_json, all_pages, page_size, catalog_id, job_key, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, job_type, sub_type, parent_key, time_start, time_end, error_code, error_message, process_key, external_url, event_key, data_entity_key, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if job_type is not None:
        kwargs['job_type'] = job_type
    if sub_type is not None:
        kwargs['sub_type'] = sub_type
    if parent_key is not None:
        kwargs['parent_key'] = parent_key
    if time_start is not None:
        kwargs['time_start'] = time_start
    if time_end is not None:
        kwargs['time_end'] = time_end
    if error_code is not None:
        kwargs['error_code'] = error_code
    if error_message is not None:
        kwargs['error_message'] = error_message
    if process_key is not None:
        kwargs['process_key'] = process_key
    if external_url is not None:
        kwargs['external_url'] = external_url
    if event_key is not None:
        kwargs['event_key'] = event_key
    if data_entity_key is not None:
        kwargs['data_entity_key'] = data_entity_key
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_executions,
            catalog_id=catalog_id,
            job_key=job_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_executions,
            limit,
            page_size,
            catalog_id=catalog_id,
            job_key=job_key,
            **kwargs
        )
    else:
        result = client.list_job_executions(
            catalog_id=catalog_id,
            job_key=job_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_log_collection_group.command(name=cli_util.override('data_catalog.list_job_logs.command_name', 'list-job-logs'), help=u"""Returns a list of job logs. \n[Command Reference](listJobLogs)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--job-execution-key', required=True, help=u"""The key of the job execution.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--severity', help=u"""Severity level for this Log.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "jobExecutionKey", "severity", "timeCreated", "logMessage", "uri"]), multiple=True, help=u"""Specifies the fields to return in a job log summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobLogCollection'})
@cli_util.wrap_exceptions
def list_job_logs(ctx, from_json, all_pages, page_size, catalog_id, job_key, job_execution_key, lifecycle_state, severity, time_created, time_updated, created_by_id, updated_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    if isinstance(job_execution_key, six.string_types) and len(job_execution_key.strip()) == 0:
        raise click.UsageError('Parameter --job-execution-key cannot be whitespace or empty string')

    kwargs = {}
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if severity is not None:
        kwargs['severity'] = severity
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_logs,
            catalog_id=catalog_id,
            job_key=job_key,
            job_execution_key=job_execution_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_logs,
            limit,
            page_size,
            catalog_id=catalog_id,
            job_key=job_key,
            job_execution_key=job_execution_key,
            **kwargs
        )
    else:
        result = client.list_job_logs(
            catalog_id=catalog_id,
            job_key=job_key,
            job_execution_key=job_execution_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_metric_collection_group.command(name=cli_util.override('data_catalog.list_job_metrics.command_name', 'list-job-metrics'), help=u"""Returns a list of job metrics. \n[Command Reference](listJobMetrics)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--job-execution-key', required=True, help=u"""The key of the job execution.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--category', help=u"""Category of this metric.""")
@cli_util.option('--sub-category', help=u"""Sub category of this metric under the category. Used for aggregating values. May be null.""")
@cli_util.option('--unit', help=u"""Unit of this metric.""")
@cli_util.option('--value', help=u"""Value of this metric.""")
@cli_util.option('--batch-key', help=u"""Batch key for grouping, may be null.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-inserted', type=custom_types.CLI_DATETIME, help=u"""The time the metric was logged or captured in the system where the job executed. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "description", "displayName", "timeInserted", "category", "subCategory", "unit", "value", "batchKey", "jobExecutionKey", "timeCreated", "uri"]), multiple=True, help=u"""Specifies the fields to return in a job metric summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobMetricCollection'})
@cli_util.wrap_exceptions
def list_job_metrics(ctx, from_json, all_pages, page_size, catalog_id, job_key, job_execution_key, display_name, display_name_contains, category, sub_category, unit, value, batch_key, time_created, time_updated, time_inserted, created_by_id, updated_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    if isinstance(job_execution_key, six.string_types) and len(job_execution_key.strip()) == 0:
        raise click.UsageError('Parameter --job-execution-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if category is not None:
        kwargs['category'] = category
    if sub_category is not None:
        kwargs['sub_category'] = sub_category
    if unit is not None:
        kwargs['unit'] = unit
    if value is not None:
        kwargs['value'] = value
    if batch_key is not None:
        kwargs['batch_key'] = batch_key
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if time_inserted is not None:
        kwargs['time_inserted'] = time_inserted
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_job_metrics,
            catalog_id=catalog_id,
            job_key=job_key,
            job_execution_key=job_execution_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_job_metrics,
            limit,
            page_size,
            catalog_id=catalog_id,
            job_key=job_key,
            job_execution_key=job_execution_key,
            **kwargs
        )
    else:
        result = client.list_job_metrics(
            catalog_id=catalog_id,
            job_key=job_key,
            job_execution_key=job_execution_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@job_collection_group.command(name=cli_util.override('data_catalog.list_jobs.command_name', 'list-jobs'), help=u"""Returns a list of jobs within a data catalog. \n[Command Reference](listJobs)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "EXPIRED"]), help=u"""Job lifecycle state.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--job-type', type=custom_types.CliCaseInsensitiveChoice(["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE", "IMPORT_DATA_ASSET"]), help=u"""Job type.""")
@cli_util.option('--job-definition-key', help=u"""Unique job definition key.""")
@cli_util.option('--data-asset-key', help=u"""Unique data asset key.""")
@cli_util.option('--schedule-cron-expression', help=u"""Schedule specified in the cron expression format that has seven fields for second, minute, hour, day-of-month, month, day-of-week, year. It can also include special characters like * for all and ? for any. There are also pre-defined schedules that can be specified using special strings. For example, @hourly will run the job every hour.""")
@cli_util.option('--time-schedule-begin', type=custom_types.CLI_DATETIME, help=u"""Date that the schedule should be operational. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-schedule-end', type=custom_types.CLI_DATETIME, help=u"""Date that the schedule should end from being operational. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--schedule-type', type=custom_types.CliCaseInsensitiveChoice(["SCHEDULED", "IMMEDIATE"]), help=u"""Type of the job schedule.""")
@cli_util.option('--connection-key', help=u"""Unique connection key.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "jobDefinitionKey", "lifecycleState", "timeCreated", "timeUpdated", "createdById", "updatedById", "jobType", "scheduleCronExpression", "timeScheduleBegin", "scheduleType", "executionCount", "timeOfLatestExecution", "executions", "uri", "jobDefinitionName", "errorCode", "errorMessage"]), multiple=True, help=u"""Specifies the fields to return in a job summary response.""")
@cli_util.option('--execution-count', type=click.INT, help=u"""The total number of executions for this job schedule.""")
@cli_util.option('--time-of-latest-execution', type=custom_types.CLI_DATETIME, help=u"""The date and time the most recent execution for this job ,in the format defined by [RFC3339]. Example: `2019-03-25T21:10:29.600Z`""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'JobCollection'})
@cli_util.wrap_exceptions
def list_jobs(ctx, from_json, all_pages, page_size, catalog_id, display_name, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, job_type, job_definition_key, data_asset_key, schedule_cron_expression, time_schedule_begin, time_schedule_end, schedule_type, connection_key, fields, execution_count, time_of_latest_execution, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if job_type is not None:
        kwargs['job_type'] = job_type
    if job_definition_key is not None:
        kwargs['job_definition_key'] = job_definition_key
    if data_asset_key is not None:
        kwargs['data_asset_key'] = data_asset_key
    if schedule_cron_expression is not None:
        kwargs['schedule_cron_expression'] = schedule_cron_expression
    if time_schedule_begin is not None:
        kwargs['time_schedule_begin'] = time_schedule_begin
    if time_schedule_end is not None:
        kwargs['time_schedule_end'] = time_schedule_end
    if schedule_type is not None:
        kwargs['schedule_type'] = schedule_type
    if connection_key is not None:
        kwargs['connection_key'] = connection_key
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if execution_count is not None:
        kwargs['execution_count'] = execution_count
    if time_of_latest_execution is not None:
        kwargs['time_of_latest_execution'] = time_of_latest_execution
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_jobs,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_jobs,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_jobs(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@metastore_group.command(name=cli_util.override('data_catalog.list_metastores.command_name', 'list'), help=u"""Returns a list of all metastores in the specified compartment. \n[Command Reference](listMetastores)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to list resources.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'list[MetastoreSummary]'})
@cli_util.wrap_exceptions
def list_metastores(ctx, from_json, all_pages, page_size, compartment_id, display_name, limit, page, lifecycle_state, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_metastores,
            compartment_id=compartment_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_metastores,
            limit,
            page_size,
            compartment_id=compartment_id,
            **kwargs
        )
    else:
        result = client.list_metastores(
            compartment_id=compartment_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@namespace_group.command(name=cli_util.override('data_catalog.list_namespaces.command_name', 'list'), help=u"""Returns a list of namespaces within a data catalog. \n[Command Reference](listNamespaces)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "lifecycleState", "timeCreated"]), multiple=True, help=u"""Specifies the fields to return in a namespace summary response.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'NamespaceCollection'})
@cli_util.wrap_exceptions
def list_namespaces(ctx, from_json, all_pages, page_size, catalog_id, display_name, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, sort_by, sort_order, fields, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_namespaces,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_namespaces,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_namespaces(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@pattern_group.command(name=cli_util.override('data_catalog.list_patterns.command_name', 'list'), help=u"""Returns a list of patterns within a data catalog. \n[Command Reference](listPatterns)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "catalogId", "expression", "lifecycleState", "timeCreated"]), multiple=True, help=u"""Specifies the fields to return in a pattern summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'PatternCollection'})
@cli_util.wrap_exceptions
def list_patterns(ctx, from_json, all_pages, page_size, catalog_id, display_name, display_name_contains, lifecycle_state, time_created, time_updated, created_by_id, updated_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_patterns,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_patterns,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_patterns(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@rule_summary_group.command(name=cli_util.override('data_catalog.list_rules.command_name', 'list-rules'), help=u"""Returns a list of all rules of a data entity. \n[Command Reference](listRules)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--rule-type', type=custom_types.CliCaseInsensitiveChoice(["PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY"]), help=u"""Rule type used to filter the response to a list rules call.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--origin-type', type=custom_types.CliCaseInsensitiveChoice(["SOURCE", "USER", "PROFILING"]), help=u"""Rule origin type used to filter the response to a list rules call.""")
@cli_util.option('--external-key', help=u"""Unique external identifier of this resource in the external source system.""")
@cli_util.option('--time-created', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was created. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-updated', type=custom_types.CLI_DATETIME, help=u"""Time that the resource was updated. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--created-by-id', help=u"""OCID of the user who created the resource.""")
@cli_util.option('--updated-by-id', help=u"""OCID of the user who updated the resource.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "ruleType", "externalKey", "referencedFolderKey", "referencedFolderName", "referencedEntityKey", "referencedEntityName", "referencedRuleKey", "referencedRuleName", "originType", "lifecycleState", "timeCreated", "uri"]), multiple=True, help=u"""Specifies the fields to return in a rule summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'RuleCollection'})
@cli_util.wrap_exceptions
def list_rules(ctx, from_json, all_pages, page_size, catalog_id, data_asset_key, entity_key, display_name, display_name_contains, rule_type, lifecycle_state, origin_type, external_key, time_created, time_updated, created_by_id, updated_by_id, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if rule_type is not None:
        kwargs['rule_type'] = rule_type
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if origin_type is not None:
        kwargs['origin_type'] = origin_type
    if external_key is not None:
        kwargs['external_key'] = external_key
    if time_created is not None:
        kwargs['time_created'] = time_created
    if time_updated is not None:
        kwargs['time_updated'] = time_updated
    if created_by_id is not None:
        kwargs['created_by_id'] = created_by_id
    if updated_by_id is not None:
        kwargs['updated_by_id'] = updated_by_id
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_rules,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_rules,
            limit,
            page_size,
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    else:
        result = client.list_rules(
            catalog_id=catalog_id,
            data_asset_key=data_asset_key,
            entity_key=entity_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@term_group.command(name=cli_util.override('data_catalog.list_tags.command_name', 'list-tags'), help=u"""Returns a list of all user created tags in the system. \n[Command Reference](listTags)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "glossaryKey", "parentTermKey", "isAllowedToHaveChildTerms", "path", "lifecycleState", "timeCreated", "workflowStatus", "associatedObjectCount", "uri"]), multiple=True, help=u"""Specifies the fields to return in a term summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'TermCollection'})
@cli_util.wrap_exceptions
def list_tags(ctx, from_json, all_pages, page_size, catalog_id, display_name, display_name_contains, lifecycle_state, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_tags,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_tags,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_tags(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@term_relationship_group.command(name=cli_util.override('data_catalog.list_term_relationships.command_name', 'list'), help=u"""Returns a list of all term relationships within a glossary. \n[Command Reference](listTermRelationships)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "relatedTermKey", "relatedTermDisplayName", "parentTermKey", "parentTermDisplayName", "lifecycleState", "timeCreated", "uri"]), multiple=True, help=u"""Specifies the fields to return in a term relationship summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'TermRelationshipCollection'})
@cli_util.wrap_exceptions
def list_term_relationships(ctx, from_json, all_pages, page_size, catalog_id, glossary_key, term_key, display_name, display_name_contains, lifecycle_state, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_term_relationships,
            catalog_id=catalog_id,
            glossary_key=glossary_key,
            term_key=term_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_term_relationships,
            limit,
            page_size,
            catalog_id=catalog_id,
            glossary_key=glossary_key,
            term_key=term_key,
            **kwargs
        )
    else:
        result = client.list_term_relationships(
            catalog_id=catalog_id,
            glossary_key=glossary_key,
            term_key=term_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@term_group.command(name=cli_util.override('data_catalog.list_terms.command_name', 'list'), help=u"""Returns a list of all terms within a glossary. \n[Command Reference](listTerms)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--display-name-contains', help=u"""A filter to return only resources that match display name pattern given. The match is not case sensitive. For Example : /folders?displayNameContains=Cu.* The above would match all folders with display name that starts with \"Cu\".""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--parent-term-key', help=u"""Unique key of the parent term.""")
@cli_util.option('--is-allowed-to-have-child-terms', type=click.BOOL, help=u"""Indicates whether a term may contain child terms.""")
@cli_util.option('--workflow-status', type=custom_types.CliCaseInsensitiveChoice(["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]), help=u"""Status of the approval workflow for this business term in the glossary.""")
@cli_util.option('--path', help=u"""Full path of the resource for resources that support paths.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "displayName", "description", "glossaryKey", "parentTermKey", "isAllowedToHaveChildTerms", "path", "lifecycleState", "timeCreated", "workflowStatus", "associatedObjectCount", "uri"]), multiple=True, help=u"""Specifies the fields to return in a term summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'TermCollection'})
@cli_util.wrap_exceptions
def list_terms(ctx, from_json, all_pages, page_size, catalog_id, glossary_key, display_name, display_name_contains, lifecycle_state, parent_term_key, is_allowed_to_have_child_terms, workflow_status, path, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if display_name_contains is not None:
        kwargs['display_name_contains'] = display_name_contains
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if parent_term_key is not None:
        kwargs['parent_term_key'] = parent_term_key
    if is_allowed_to_have_child_terms is not None:
        kwargs['is_allowed_to_have_child_terms'] = is_allowed_to_have_child_terms
    if workflow_status is not None:
        kwargs['workflow_status'] = workflow_status
    if path is not None:
        kwargs['path'] = path
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_terms,
            catalog_id=catalog_id,
            glossary_key=glossary_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_terms,
            limit,
            page_size,
            catalog_id=catalog_id,
            glossary_key=glossary_key,
            **kwargs
        )
    else:
        result = client.list_terms(
            catalog_id=catalog_id,
            glossary_key=glossary_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@type_collection_group.command(name=cli_util.override('data_catalog.list_types.command_name', 'list-types'), help=u"""Returns a list of all types within a data catalog. \n[Command Reference](listTypes)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--name', help=u"""Immutable resource name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--is-internal', help=u"""Indicates whether the type is internal, making it unavailable for use by metadata elements.""")
@cli_util.option('--is-tag', help=u"""Indicates whether the type can be used for tagging metadata elements.""")
@cli_util.option('--is-approved', help=u"""Indicates whether the type is approved for use as a classifying object.""")
@cli_util.option('--external-type-name', help=u"""Data type as defined in an external system.""")
@cli_util.option('--type-category', help=u"""Indicates the category of this type . For example, data assets or connections.""")
@cli_util.option('--fields', type=custom_types.CliCaseInsensitiveChoice(["key", "description", "name", "catalogId", "lifecycleState", "typeCategory", "uri"]), multiple=True, help=u"""Specifies the fields to return in a type summary response.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'TypeCollection'})
@cli_util.wrap_exceptions
def list_types(ctx, from_json, all_pages, page_size, catalog_id, name, lifecycle_state, is_internal, is_tag, is_approved, external_type_name, type_category, fields, sort_by, sort_order, limit, page):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if is_internal is not None:
        kwargs['is_internal'] = is_internal
    if is_tag is not None:
        kwargs['is_tag'] = is_tag
    if is_approved is not None:
        kwargs['is_approved'] = is_approved
    if external_type_name is not None:
        kwargs['external_type_name'] = external_type_name
    if type_category is not None:
        kwargs['type_category'] = type_category
    if fields is not None and len(fields) > 0:
        kwargs['fields'] = fields
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_types,
            catalog_id=catalog_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_types,
            limit,
            page_size,
            catalog_id=catalog_id,
            **kwargs
        )
    else:
        result = client.list_types(
            catalog_id=catalog_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@work_request_error_group.command(name=cli_util.override('data_catalog.list_work_request_errors.command_name', 'list'), help=u"""Returns a (paginated) list of errors for a given work request. \n[Command Reference](listWorkRequestErrors)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["CODE", "TIMESTAMP"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMESTAMP is descending. Default order for CODE and MESSAGE is ascending. If no value is specified TIMESTAMP is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'list[WorkRequestError]'})
@cli_util.wrap_exceptions
def list_work_request_errors(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
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


@work_request_log_group.command(name=cli_util.override('data_catalog.list_work_request_logs.command_name', 'list'), help=u"""Returns a (paginated) list of logs for a given work request. \n[Command Reference](listWorkRequestLogs)""")
@cli_util.option('--work-request-id', required=True, help=u"""The OCID of the asynchronous request.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["MESSAGE", "TIMESTAMP"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMESTAMP is descending. Default order for MESSAGE is ascending. If no value is specified TIMESTAMP is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'list[WorkRequestLog]'})
@cli_util.wrap_exceptions
def list_work_request_logs(ctx, from_json, all_pages, page_size, work_request_id, page, limit, sort_by, sort_order):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(work_request_id, six.string_types) and len(work_request_id.strip()) == 0:
        raise click.UsageError('Parameter --work-request-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
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


@work_request_group.command(name=cli_util.override('data_catalog.list_work_requests.command_name', 'list'), help=u"""Lists the work requests in a compartment. \n[Command Reference](listWorkRequests)""")
@cli_util.option('--compartment-id', required=True, help=u"""The OCID of the compartment where you want to list resources.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'list[WorkRequest]'})
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
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
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


@catalog_group.command(name=cli_util.override('data_catalog.object_stats.command_name', 'object-stats'), help=u"""Returns stats on objects by type in the repository. \n[Command Reference](objectStats)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def object_stats(ctx, from_json, catalog_id, sort_by, sort_order, limit, page):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.object_stats(
        catalog_id=catalog_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.parse_connection.command_name', 'parse-connection'), help=u"""Parse data asset references through connections from this data asset. \n[Command Reference](parseConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-detail', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-payload', help=u"""The information used to parse the connection from the wallet file payload.""")
@cli_util.option('--wallet-secret-id', help=u"""OCID of the OCI Vault secret holding the Oracle wallet to parse.""")
@cli_util.option('--wallet-secret-name', help=u"""Name of the OCI Vault secret holding the Oracle wallet to parse.""")
@cli_util.option('--connection-key', help=u"""Unique connection key.""")
@json_skeleton_utils.get_cli_json_input_option({'connection-detail': {'module': 'data_catalog', 'class': 'Connection'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-detail': {'module': 'data_catalog', 'class': 'Connection'}}, output_type={'module': 'data_catalog', 'class': 'list[ConnectionAliasSummary]'})
@cli_util.wrap_exceptions
def parse_connection(ctx, from_json, catalog_id, data_asset_key, connection_detail, connection_payload, wallet_secret_id, wallet_secret_name, connection_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if connection_key is not None:
        kwargs['connection_key'] = connection_key
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if connection_detail is not None:
        _details['connectionDetail'] = cli_util.parse_json_parameter("connection_detail", connection_detail)

    if connection_payload is not None:
        _details['connectionPayload'] = connection_payload

    if wallet_secret_id is not None:
        _details['walletSecretId'] = wallet_secret_id

    if wallet_secret_name is not None:
        _details['walletSecretName'] = wallet_secret_name

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.parse_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        parse_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@catalog_group.command(name=cli_util.override('data_catalog.process_recommendation.command_name', 'process-recommendation'), help=u"""Act on a recommendation. A recommendation can be accepted or rejected. For example, if a recommendation of type LINK_GLOSSARY_TERM is accepted, the system will link the source object (e.g. an attribute) to a target glossary term. \n[Command Reference](processRecommendation)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--recommendation-key', required=True, help=u"""Unique identifier of the recommendation.""")
@cli_util.option('--recommendation-status', required=True, type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "REJECTED", "INFERRED"]), help=u"""The status of a recommendation.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains additional properties which are specific to the associated objects. Each associated object defines it's set of required and optional properties. Example: `{             \"DataEntity\": {               \"parentId\": \"entityId\"             },             \"Term\": {               \"parentId\": \"glossaryId\"             }           }`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'ProcessRecommendationDetails'})
@cli_util.wrap_exceptions
def process_recommendation(ctx, from_json, catalog_id, recommendation_key, recommendation_status, properties, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['recommendationKey'] = recommendation_key
    _details['recommendationStatus'] = recommendation_status

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.process_recommendation(
        catalog_id=catalog_id,
        process_recommendation_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@catalog_group.command(name=cli_util.override('data_catalog.recommendations.command_name', 'recommendations'), help=u"""Returns a list of recommendations for the given object and recommendation type. By default, it will return inferred recommendations for review. The optional query param 'RecommendationStatus' can be set, to return only recommendations having that status. \n[Command Reference](recommendations)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--recommendation-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["LINK_GLOSSARY_TERM"]), multiple=True, help=u"""A filter used to return only recommendations of the specified type.""")
@cli_util.option('--source-object-key', required=True, help=u"""A filter used to provide the unique identifier of the source object, for which a list of recommendations will be returned for review.""")
@cli_util.option('--source-object-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["DATA_ENTITY", "ATTRIBUTE", "TERM", "CATEGORY"]), help=u"""A filter used to provide the type of the source object, for which a list of recommendations will be returned for review.""")
@cli_util.option('--recommendation-status', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "REJECTED", "INFERRED"]), help=u"""A filter used to return only recommendations having the requested status.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'RecommendationCollection'})
@cli_util.wrap_exceptions
def recommendations(ctx, from_json, catalog_id, recommendation_type, source_object_key, source_object_type, recommendation_status):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if recommendation_status is not None:
        kwargs['recommendation_status'] = recommendation_status
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.recommendations(
        catalog_id=catalog_id,
        recommendation_type=recommendation_type,
        source_object_key=source_object_key,
        source_object_type=source_object_type,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.remove_data_selector_patterns.command_name', 'remove'), help=u"""Remove data selector pattern from the data asset. \n[Command Reference](removeDataSelectorPatterns)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--items', required=True, type=custom_types.CLI_COMPLEX_TYPE, help=u"""Collection of pattern Ids.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'data_catalog', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'data_catalog', 'class': 'list[string]'}}, output_type={'module': 'data_catalog', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def remove_data_selector_patterns(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, items, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.remove_data_selector_patterns(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        data_selector_pattern_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@search_result_group.command(name=cli_util.override('data_catalog.search_criteria.command_name', 'search-criteria'), help=u"""Returns a list of search results within a data catalog. \n[Command Reference](searchCriteria)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--query-parameterconflict', help=u"""Search query dsl that defines the query components including fields and predicates.""")
@cli_util.option('--faceted-query', help=u"""Query string that a dataObject is to be searched with. Used in the faceted query request""")
@cli_util.option('--dimensions', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of properties of dataObjects that needs to aggregated on for facets.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--sort', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of objects having details about sort field and order.

This option is a JSON list with items of type FacetedSearchSortRequest.  For documentation on FacetedSearchSortRequest please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/FacetedSearchSortRequest.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--filters', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given. The match is not case sensitive.""")
@cli_util.option('--name', help=u"""Immutable resource name.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), help=u"""A filter to return only resources that match the specified lifecycle state. The value is case insensitive.""")
@cli_util.option('--timeout', help=u"""A search timeout string (for example, timeout=4000ms), bounding the search request to be executed within the specified time value and bail with the hits accumulated up to that point when expired. Defaults to no timeout.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({'dimensions': {'module': 'data_catalog', 'class': 'list[string]'}, 'sort': {'module': 'data_catalog', 'class': 'list[FacetedSearchSortRequest]'}, 'filters': {'module': 'data_catalog', 'class': 'FacetedSearchFilterRequest'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dimensions': {'module': 'data_catalog', 'class': 'list[string]'}, 'sort': {'module': 'data_catalog', 'class': 'list[FacetedSearchSortRequest]'}, 'filters': {'module': 'data_catalog', 'class': 'FacetedSearchFilterRequest'}}, output_type={'module': 'data_catalog', 'class': 'SearchResultCollection'})
@cli_util.wrap_exceptions
def search_criteria(ctx, from_json, catalog_id, query_parameterconflict, faceted_query, dimensions, sort, filters, display_name, name, lifecycle_state, timeout, sort_by, sort_order, limit, page):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if display_name is not None:
        kwargs['display_name'] = display_name
    if name is not None:
        kwargs['name'] = name
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if timeout is not None:
        kwargs['timeout'] = timeout
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if query_parameterconflict is not None:
        _details['query'] = query_parameterconflict

    if faceted_query is not None:
        _details['facetedQuery'] = faceted_query

    if dimensions is not None:
        _details['dimensions'] = cli_util.parse_json_parameter("dimensions", dimensions)

    if sort is not None:
        _details['sort'] = cli_util.parse_json_parameter("sort", sort)

    if filters is not None:
        _details['filters'] = cli_util.parse_json_parameter("filters", filters)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.search_criteria(
        catalog_id=catalog_id,
        search_criteria_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@suggest_results_group.command(name=cli_util.override('data_catalog.suggest_matches.command_name', 'suggest-matches'), help=u"""Returns a list of potential string matches for a given input string. \n[Command Reference](suggestMatches)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--input-text', required=True, help=u"""Text input string used for computing potential matching suggestions.""")
@cli_util.option('--timeout', help=u"""A search timeout string (for example, timeout=4000ms), bounding the search request to be executed within the specified time value and bail with the hits accumulated up to that point when expired. Defaults to no timeout.""")
@cli_util.option('--limit', type=click.INT, help=u"""Limit for the list of potential matches returned from the Suggest API. If not specified, will default to 10.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'SuggestResults'})
@cli_util.wrap_exceptions
def suggest_matches(ctx, from_json, catalog_id, input_text, timeout, limit):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if timeout is not None:
        kwargs['timeout'] = timeout
    if limit is not None:
        kwargs['limit'] = limit
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.suggest_matches(
        catalog_id=catalog_id,
        input_text=input_text,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.synchronous_export_data_asset.command_name', 'synchronous-export'), help=u"""Export technical objects from a Data Asset \n[Command Reference](synchronousExportDataAsset)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--export-type', required=True, type=custom_types.CliCaseInsensitiveChoice(["CUSTOM_PROPERTY_VALUES", "ALL"]), multiple=True, help=u"""Type of export.""")
@cli_util.option('--file', type=click.File(mode='wb'), required=True, help="The name of the file that will receive the response data, or '-' to write to STDOUT.")
@cli_util.option('--export-scope', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Array of objects and their child types to be selected for export.

This option is a JSON list with items of type DataAssetExportScope.  For documentation on DataAssetExportScope please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/DataAssetExportScope.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@json_skeleton_utils.get_cli_json_input_option({'export-scope': {'module': 'data_catalog', 'class': 'list[DataAssetExportScope]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'export-scope': {'module': 'data_catalog', 'class': 'list[DataAssetExportScope]'}})
@cli_util.wrap_exceptions
def synchronous_export_data_asset(ctx, from_json, file, catalog_id, data_asset_key, export_type, export_scope):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if export_scope is not None:
        _details['exportScope'] = cli_util.parse_json_parameter("export_scope", export_scope)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.synchronous_export_data_asset(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        export_type=export_type,
        synchronous_export_data_asset_details=_details,
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


@connection_group.command(name=cli_util.override('data_catalog.test_connection.command_name', 'test'), help=u"""Test the connection by connecting to the data asset using credentials in the metadata. \n[Command Reference](testConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-key', required=True, help=u"""Unique connection key.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'ValidateConnectionResult'})
@cli_util.wrap_exceptions
def test_connection(ctx, from_json, catalog_id, data_asset_key, connection_key):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.test_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        connection_key=connection_key,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@attribute_group.command(name=cli_util.override('data_catalog.update_attribute.command_name', 'update'), help=u"""Updates a specific data asset attribute. \n[Command Reference](updateAttribute)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--attribute-key', required=True, help=u"""Unique attribute key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--business-name', help=u"""Optional user friendly business name of the attribute. If set, this supplements the harvested display name of the object.""")
@cli_util.option('--description', help=u"""Detailed description of the attribute.""")
@cli_util.option('--external-data-type', help=u"""Data type of the attribute as defined in the external system.""")
@cli_util.option('--is-incremental-data', type=click.BOOL, help=u"""Property that identifies if this attribute can be used as a watermark to extract incremental data.""")
@cli_util.option('--is-nullable', type=click.BOOL, help=u"""Property that identifies if this attribute can be assigned nullable values.""")
@cli_util.option('--length', type=click.INT, help=u"""Max allowed length of the attribute value.""")
@cli_util.option('--position', type=click.INT, help=u"""Position of the attribute in the record definition.""")
@cli_util.option('--precision', type=click.INT, help=u"""Precision of the attribute value usually applies to float data type.""")
@cli_util.option('--scale', type=click.INT, help=u"""Scale of the attribute value usually applies to float data type.""")
@cli_util.option('--time-external', type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of this object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--min-collection-count', type=click.INT, help=u"""The minimum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type.""")
@cli_util.option('--max-collection-count', type=click.INT, help=u"""The maximum count for the number of instances of a given type stored in this collection type attribute,applicable if this attribute is a complex type. For type specifications in systems that specify only \"capacity\" without upper or lower bound , this property can also be used to just mean \"capacity\". Some examples are Varray size in Oracle , Occurs Clause in Cobol , capacity in XmlSchemaObjectCollection , maxOccurs in  Xml , maxItems in Json""")
@cli_util.option('--external-datatype-entity-key', help=u"""External entity key that represents the datatype of this attribute , applicable if this attribute is a complex type.""")
@cli_util.option('--external-parent-attribute-key', help=u"""External attribute key that represents the parent attribute  of this attribute , applicable if the parent attribute is of complex type.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the attribute type. Each attribute type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most attributes have required properties within the \"default\" category. To determine the set of required and optional properties for an Attribute type, a query can be done on '/types?type=attribute' which returns a collection of all attribute types. The appropriate attribute type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Attribute'})
@cli_util.wrap_exceptions
def update_attribute(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, entity_key, attribute_key, display_name, business_name, description, external_data_type, is_incremental_data, is_nullable, length, position, precision, scale, time_external, min_collection_count, max_collection_count, external_datatype_entity_key, external_parent_attribute_key, custom_property_members, properties, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')

    if isinstance(attribute_key, six.string_types) and len(attribute_key.strip()) == 0:
        raise click.UsageError('Parameter --attribute-key cannot be whitespace or empty string')
    if not force:
        if custom_property_members or properties:
            if not click.confirm("WARNING: Updates to custom-property-members and properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if business_name is not None:
        _details['businessName'] = business_name

    if description is not None:
        _details['description'] = description

    if external_data_type is not None:
        _details['externalDataType'] = external_data_type

    if is_incremental_data is not None:
        _details['isIncrementalData'] = is_incremental_data

    if is_nullable is not None:
        _details['isNullable'] = is_nullable

    if length is not None:
        _details['length'] = length

    if position is not None:
        _details['position'] = position

    if precision is not None:
        _details['precision'] = precision

    if scale is not None:
        _details['scale'] = scale

    if time_external is not None:
        _details['timeExternal'] = time_external

    if min_collection_count is not None:
        _details['minCollectionCount'] = min_collection_count

    if max_collection_count is not None:
        _details['maxCollectionCount'] = max_collection_count

    if external_datatype_entity_key is not None:
        _details['externalDatatypeEntityKey'] = external_datatype_entity_key

    if external_parent_attribute_key is not None:
        _details['externalParentAttributeKey'] = external_parent_attribute_key

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_attribute(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        attribute_key=attribute_key,
        update_attribute_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_attribute') and callable(getattr(client, 'get_attribute')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_attribute(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@catalog_group.command(name=cli_util.override('data_catalog.update_catalog.command_name', 'update'), help=u"""Updates the data catalog. \n[Command Reference](updateCatalog)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--display-name', help=u"""Data catalog identifier.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_catalog', 'class': 'Catalog'})
@cli_util.wrap_exceptions
def update_catalog(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_catalog(
        catalog_id=catalog_id,
        update_catalog_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_catalog') and callable(getattr(client, 'get_catalog')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_catalog(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@catalog_private_endpoint_group.command(name=cli_util.override('data_catalog.update_catalog_private_endpoint.command_name', 'update'), help=u"""Updates the private reverse connection endpoint. \n[Command Reference](updateCatalogPrivateEndpoint)""")
@cli_util.option('--catalog-private-endpoint-id', required=True, help=u"""Unique private reverse connection identifier.""")
@cli_util.option('--dns-zones', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of DNS zones to be used by the data assets to be harvested. Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--display-name', help=u"""Display name of the private endpoint resource.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]), multiple=True, help="""This operation asynchronously creates, modifies or deletes a resource and uses a work request to track the progress of the operation. Specify this option to perform the action and then wait until the work request reaches a certain state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the work request to reach the state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the work request to see if it has reached the state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'dns-zones': {'module': 'data_catalog', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'dns-zones': {'module': 'data_catalog', 'class': 'list[string]'}, 'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.wrap_exceptions
def update_catalog_private_endpoint(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_private_endpoint_id, dns_zones, freeform_tags, defined_tags, display_name, if_match):

    if isinstance(catalog_private_endpoint_id, six.string_types) and len(catalog_private_endpoint_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-private-endpoint-id cannot be whitespace or empty string')
    if not force:
        if dns_zones or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to dns-zones and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if dns_zones is not None:
        _details['dnsZones'] = cli_util.parse_json_parameter("dns_zones", dns_zones)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    if display_name is not None:
        _details['displayName'] = display_name

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_catalog_private_endpoint(
        catalog_private_endpoint_id=catalog_private_endpoint_id,
        update_catalog_private_endpoint_details=_details,
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


@connection_group.command(name=cli_util.override('data_catalog.update_connection.command_name', 'update'), help=u"""Updates a specific connection of a data asset. \n[Command Reference](updateConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-key', required=True, help=u"""Unique connection key.""")
@cli_util.option('--description', help=u"""A description of the connection.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"username\": \"user1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--enc-properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the encrypted values for sensitive properties which are specific to the connection type. Each connection type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most connections have required properties within the \"default\" category. To determine the set of optional and required properties for a connection type, a query can be done on '/types?type=connection' that returns a collection of all connection types. The appropriate connection type, which will include definitions of all of it's properties, can be identified from this collection. Example: `{\"encProperties\": { \"default\": { \"password\": \"example-password\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-default', type=click.BOOL, help=u"""Indicates whether this connection is the default connection.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}, 'enc-properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}, 'enc-properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Connection'})
@cli_util.wrap_exceptions
def update_connection(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, connection_key, description, display_name, custom_property_members, properties, enc_properties, is_default, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')
    if not force:
        if custom_property_members or properties or enc_properties:
            if not click.confirm("WARNING: Updates to custom-property-members and properties and enc-properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if description is not None:
        _details['description'] = description

    if display_name is not None:
        _details['displayName'] = display_name

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if enc_properties is not None:
        _details['encProperties'] = cli_util.parse_json_parameter("enc_properties", enc_properties)

    if is_default is not None:
        _details['isDefault'] = is_default

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        connection_key=connection_key,
        update_connection_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_connection') and callable(getattr(client, 'get_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@custom_property_group.command(name=cli_util.override('data_catalog.update_custom_property.command_name', 'update'), help=u"""Updates a specific custom property identified by the given key. \n[Command Reference](updateCustomProperty)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--custom-property-key', required=True, help=u"""Unique Custom Property key""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the data asset.""")
@cli_util.option('--is-sortable', type=click.BOOL, help=u"""If this field allows to sort from UI""")
@cli_util.option('--is-filterable', type=click.BOOL, help=u"""If this field allows to filter or create facets from UI""")
@cli_util.option('--is-multi-valued', type=click.BOOL, help=u"""If this field allows multiple values to be set""")
@cli_util.option('--is-hidden', type=click.BOOL, help=u"""If this field is a hidden field""")
@cli_util.option('--is-editable', type=click.BOOL, help=u"""If this field is a editable field""")
@cli_util.option('--is-shown-in-list', type=click.BOOL, help=u"""If this field is displayed in a list view of applicable objects.""")
@cli_util.option('--is-hidden-in-search', type=click.BOOL, help=u"""If this field is allowed to pop in search results""")
@cli_util.option('--is-event-enabled', type=click.BOOL, help=u"""If an OCI Event will be emitted when the custom property is modified.""")
@cli_util.option('--allowed-values', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Allowed values for the custom property if any""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'allowed-values': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'allowed-values': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'CustomProperty'})
@cli_util.wrap_exceptions
def update_custom_property(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, namespace_id, custom_property_key, display_name, description, is_sortable, is_filterable, is_multi_valued, is_hidden, is_editable, is_shown_in_list, is_hidden_in_search, is_event_enabled, allowed_values, properties, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    if isinstance(custom_property_key, six.string_types) and len(custom_property_key.strip()) == 0:
        raise click.UsageError('Parameter --custom-property-key cannot be whitespace or empty string')
    if not force:
        if allowed_values or properties:
            if not click.confirm("WARNING: Updates to allowed-values and properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_sortable is not None:
        _details['isSortable'] = is_sortable

    if is_filterable is not None:
        _details['isFilterable'] = is_filterable

    if is_multi_valued is not None:
        _details['isMultiValued'] = is_multi_valued

    if is_hidden is not None:
        _details['isHidden'] = is_hidden

    if is_editable is not None:
        _details['isEditable'] = is_editable

    if is_shown_in_list is not None:
        _details['isShownInList'] = is_shown_in_list

    if is_hidden_in_search is not None:
        _details['isHiddenInSearch'] = is_hidden_in_search

    if is_event_enabled is not None:
        _details['isEventEnabled'] = is_event_enabled

    if allowed_values is not None:
        _details['allowedValues'] = cli_util.parse_json_parameter("allowed_values", allowed_values)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_custom_property(
        catalog_id=catalog_id,
        namespace_id=namespace_id,
        custom_property_key=custom_property_key,
        update_custom_property_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_custom_property') and callable(getattr(client, 'get_custom_property')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_custom_property(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@data_asset_group.command(name=cli_util.override('data_catalog.update_data_asset.command_name', 'update'), help=u"""Updates a specific data asset identified by the given key. \n[Command Reference](updateDataAsset)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the data asset.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the asset type. Each data asset type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most data assets have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'DataAsset'})
@cli_util.wrap_exceptions
def update_data_asset(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, display_name, description, custom_property_members, properties, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')
    if not force:
        if custom_property_members or properties:
            if not click.confirm("WARNING: Updates to custom-property-members and properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_data_asset(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        update_data_asset_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_data_asset') and callable(getattr(client, 'get_data_asset')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_data_asset(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@entity_group.command(name=cli_util.override('data_catalog.update_entity.command_name', 'update'), help=u"""Updates a specific data entity. \n[Command Reference](updateEntity)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--entity-key', required=True, help=u"""Unique entity key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--business-name', help=u"""Optional user friendly business name of the data entity. If set, this supplements the harvested display name of the object.""")
@cli_util.option('--description', help=u"""Detailed description of a data entity.""")
@cli_util.option('--time-external', type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of the object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--is-logical', type=click.BOOL, help=u"""Property to indicate if the object is a physical materialized object or virtual. For example, View.""")
@cli_util.option('--is-partition', type=click.BOOL, help=u"""Property to indicate if the object is a sub object of a parent physical object.""")
@cli_util.option('--folder-key', help=u"""Key of the associated folder.""")
@cli_util.option('--pattern-key', help=u"""Key of the associated pattern if this is a logical entity.""")
@cli_util.option('--realized-expression', help=u"""The expression realized after resolving qualifiers . Used in deriving this logical entity""")
@cli_util.option('--harvest-status', type=custom_types.CliCaseInsensitiveChoice(["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]), help=u"""Status of the object as updated by the harvest process. When an entity object is created, it's harvest status will indicate if the entity's metadata has been fully harvested or not. The harvest process can perform shallow harvesting to allow users to browse the metadata and can on-demand deep harvest on any object This requires a harvest status indicator for catalog objects.""")
@cli_util.option('--last-job-key', help=u"""Key of the last harvest process to update this object.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the entity type. Each entity type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most entities have required properties within the \"default\" category. To determine the set of required and optional properties for an entity type, a query can be done on '/types?type=dataEntity' that returns a collection of all entity types. The appropriate entity type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Entity'})
@cli_util.wrap_exceptions
def update_entity(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, entity_key, display_name, business_name, description, time_external, is_logical, is_partition, folder_key, pattern_key, realized_expression, harvest_status, last_job_key, custom_property_members, properties, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(entity_key, six.string_types) and len(entity_key.strip()) == 0:
        raise click.UsageError('Parameter --entity-key cannot be whitespace or empty string')
    if not force:
        if custom_property_members or properties:
            if not click.confirm("WARNING: Updates to custom-property-members and properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if business_name is not None:
        _details['businessName'] = business_name

    if description is not None:
        _details['description'] = description

    if time_external is not None:
        _details['timeExternal'] = time_external

    if is_logical is not None:
        _details['isLogical'] = is_logical

    if is_partition is not None:
        _details['isPartition'] = is_partition

    if folder_key is not None:
        _details['folderKey'] = folder_key

    if pattern_key is not None:
        _details['patternKey'] = pattern_key

    if realized_expression is not None:
        _details['realizedExpression'] = realized_expression

    if harvest_status is not None:
        _details['harvestStatus'] = harvest_status

    if last_job_key is not None:
        _details['lastJobKey'] = last_job_key

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_entity(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        entity_key=entity_key,
        update_entity_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_entity') and callable(getattr(client, 'get_entity')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_entity(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@folder_group.command(name=cli_util.override('data_catalog.update_folder.command_name', 'update'), help=u"""Updates a specific folder of a data asset. \n[Command Reference](updateFolder)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--folder-key', required=True, help=u"""Unique folder key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--business-name', help=u"""Optional user friendly business name of the folder. If set, this supplements the harvested display name of the object.""")
@cli_util.option('--description', help=u"""Detailed description of a folder.""")
@cli_util.option('--parent-folder-key', help=u"""The key of the containing folder.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the folder type. Each folder type definition defines it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most folders have required properties within the \"default\" category. To determine the set of optional and required properties for a folder type, a query can be done on '/types?type=folder' that returns a collection of all folder types. The appropriate folder type, which includes definitions of all of it's properties, can be identified from this collection. Example: `{\"properties\": { \"default\": { \"key1\": \"value1\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--time-external', type=custom_types.CLI_DATETIME, help=u"""Last modified timestamp of this object in the external system.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--harvest-status', type=custom_types.CliCaseInsensitiveChoice(["COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"]), help=u"""Harvest status of the folder.""")
@cli_util.option('--last-job-key', help=u"""The key of the last harvest process to update the metadata of this object.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Folder'})
@cli_util.wrap_exceptions
def update_folder(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, folder_key, display_name, business_name, description, parent_folder_key, custom_property_members, properties, time_external, harvest_status, last_job_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(folder_key, six.string_types) and len(folder_key.strip()) == 0:
        raise click.UsageError('Parameter --folder-key cannot be whitespace or empty string')
    if not force:
        if custom_property_members or properties:
            if not click.confirm("WARNING: Updates to custom-property-members and properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if business_name is not None:
        _details['businessName'] = business_name

    if description is not None:
        _details['description'] = description

    if parent_folder_key is not None:
        _details['parentFolderKey'] = parent_folder_key

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    if time_external is not None:
        _details['timeExternal'] = time_external

    if harvest_status is not None:
        _details['harvestStatus'] = harvest_status

    if last_job_key is not None:
        _details['lastJobKey'] = last_job_key

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_folder(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        folder_key=folder_key,
        update_folder_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_folder') and callable(getattr(client, 'get_folder')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_folder(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@glossary_group.command(name=cli_util.override('data_catalog.update_glossary.command_name', 'update'), help=u"""Updates a specific glossary identified by the given key. \n[Command Reference](updateGlossary)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the glossary.""")
@cli_util.option('--owner', help=u"""OCID of the user who is the owner of the glossary.""")
@cli_util.option('--workflow-status', type=custom_types.CliCaseInsensitiveChoice(["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]), help=u"""Status of the approval process workflow for this business glossary.""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}}, output_type={'module': 'data_catalog', 'class': 'Glossary'})
@cli_util.wrap_exceptions
def update_glossary(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, glossary_key, display_name, description, owner, workflow_status, custom_property_members, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')
    if not force:
        if custom_property_members:
            if not click.confirm("WARNING: Updates to custom-property-members will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if owner is not None:
        _details['owner'] = owner

    if workflow_status is not None:
        _details['workflowStatus'] = workflow_status

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_glossary(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        update_glossary_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_glossary') and callable(getattr(client, 'get_glossary')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_glossary(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_group.command(name=cli_util.override('data_catalog.update_job.command_name', 'update'), help=u"""Updates a specific job identified by the given key. \n[Command Reference](updateJob)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-key', required=True, help=u"""Unique job key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the job.""")
@cli_util.option('--schedule-cron-expression', help=u"""Schedule specified in the cron expression format that has seven fields for second, minute, hour, day-of-month, month, day-of-week, year. It can also include special characters like * for all and ? for any. There are also pre-defined schedules that can be specified using special strings. For example, @hourly will run the job every hour.""")
@cli_util.option('--time-schedule-begin', type=custom_types.CLI_DATETIME, help=u"""Date that the schedule should be operational. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--time-schedule-end', type=custom_types.CLI_DATETIME, help=u"""Date that the schedule should end from being operational. An [RFC3339] formatted datetime string.""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--connection-key', help=u"""The key of the connection resource that is used for the harvest by this job.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["ACTIVE", "INACTIVE", "EXPIRED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Job'})
@cli_util.wrap_exceptions
def update_job(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, job_key, display_name, description, schedule_cron_expression, time_schedule_begin, time_schedule_end, connection_key, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_key, six.string_types) and len(job_key.strip()) == 0:
        raise click.UsageError('Parameter --job-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if schedule_cron_expression is not None:
        _details['scheduleCronExpression'] = schedule_cron_expression

    if time_schedule_begin is not None:
        _details['timeScheduleBegin'] = time_schedule_begin

    if time_schedule_end is not None:
        _details['timeScheduleEnd'] = time_schedule_end

    if connection_key is not None:
        _details['connectionKey'] = connection_key

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_job(
        catalog_id=catalog_id,
        job_key=job_key,
        update_job_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job') and callable(getattr(client, 'get_job')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@job_definition_group.command(name=cli_util.override('data_catalog.update_job_definition.command_name', 'update'), help=u"""Update a specific job definition identified by the given key. \n[Command Reference](updateJobDefinition)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--job-definition-key', required=True, help=u"""Unique job definition key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--is-incremental', type=click.BOOL, help=u"""Specifies if the job definition is incremental or full.""")
@cli_util.option('--data-asset-key', help=u"""The key of the data asset for which the job is defined.""")
@cli_util.option('--description', help=u"""Detailed description of the job definition.""")
@cli_util.option('--connection-key', help=u"""The key of the connection resource to be used for harvest, sampling, profiling jobs.""")
@cli_util.option('--is-sample-data-extracted', type=click.BOOL, help=u"""Specify if sample data to be extracted as part of this harvest.""")
@cli_util.option('--sample-data-size-in-mbs', type=click.INT, help=u"""Specify the sample data size in MB, specified as number of rows, for this metadata harvest.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the job type. Each job type definition may define it's set of required and optional properties. The map keys are category names and the values are maps of property name to property value. Every property is contained inside of a category. Most job definitions have required properties within the \"default\" category. Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'JobDefinition'})
@cli_util.wrap_exceptions
def update_job_definition(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, job_definition_key, display_name, is_incremental, data_asset_key, description, connection_key, is_sample_data_extracted, sample_data_size_in_mbs, properties, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(job_definition_key, six.string_types) and len(job_definition_key.strip()) == 0:
        raise click.UsageError('Parameter --job-definition-key cannot be whitespace or empty string')
    if not force:
        if properties:
            if not click.confirm("WARNING: Updates to properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if is_incremental is not None:
        _details['isIncremental'] = is_incremental

    if data_asset_key is not None:
        _details['dataAssetKey'] = data_asset_key

    if description is not None:
        _details['description'] = description

    if connection_key is not None:
        _details['connectionKey'] = connection_key

    if is_sample_data_extracted is not None:
        _details['isSampleDataExtracted'] = is_sample_data_extracted

    if sample_data_size_in_mbs is not None:
        _details['sampleDataSizeInMBs'] = sample_data_size_in_mbs

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_job_definition(
        catalog_id=catalog_id,
        job_definition_key=job_definition_key,
        update_job_definition_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_job_definition') and callable(getattr(client, 'get_job_definition')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_job_definition(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@metastore_group.command(name=cli_util.override('data_catalog.update_metastore.command_name', 'update'), help=u"""Updates a metastore resource by identifier. \n[Command Reference](updateMetastore)""")
@cli_util.option('--metastore-id', required=True, help=u"""The metastore's OCID.""")
@cli_util.option('--display-name', help=u"""Mutable name of the metastore.""")
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Usage of predefined tag keys. These predefined keys are scoped to namespaces. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'freeform-tags': {'module': 'data_catalog', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'data_catalog', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'data_catalog', 'class': 'Metastore'})
@cli_util.wrap_exceptions
def update_metastore(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, metastore_id, display_name, freeform_tags, defined_tags, if_match):

    if isinstance(metastore_id, six.string_types) and len(metastore_id.strip()) == 0:
        raise click.UsageError('Parameter --metastore-id cannot be whitespace or empty string')
    if not force:
        if freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_metastore(
        metastore_id=metastore_id,
        update_metastore_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_metastore') and callable(getattr(client, 'get_metastore')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_metastore(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@namespace_group.command(name=cli_util.override('data_catalog.update_namespace.command_name', 'update'), help=u"""Updates a specific namespace identified by the given key. \n[Command Reference](updateNamespace)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--namespace-id', required=True, help=u"""Unique namespace identifier.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the namespace.""")
@cli_util.option('--is-service-defined', type=click.BOOL, help=u"""If this field is defined by service or by a user""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'Namespace'})
@cli_util.wrap_exceptions
def update_namespace(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, namespace_id, display_name, description, is_service_defined, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(namespace_id, six.string_types) and len(namespace_id.strip()) == 0:
        raise click.UsageError('Parameter --namespace-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if is_service_defined is not None:
        _details['isServiceDefined'] = is_service_defined

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_namespace(
        catalog_id=catalog_id,
        namespace_id=namespace_id,
        update_namespace_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_namespace') and callable(getattr(client, 'get_namespace')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_namespace(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@pattern_group.command(name=cli_util.override('data_catalog.update_pattern.command_name', 'update'), help=u"""Updates a specific pattern identified by the given key. \n[Command Reference](updatePattern)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--pattern-key', required=True, help=u"""Unique pattern key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the Pattern.""")
@cli_util.option('--expression', help=u"""The expression used in the pattern that may include qualifiers. Refer to the user documentation for details of the format and examples.""")
@cli_util.option('--check-file-path-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of file paths against which the expression can be tried, as a check. This documents, for reference purposes, some example objects a pattern is meant to work with. If isEnableCheckFailureLimit is set to true, this will be run as a validation during the request, such that if the check fails the request fails. If isEnableCheckFailureLimit instead is set to (the default) false, a pattern will still be created or updated even if the check fails, with a lifecycleState of FAILED.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--is-enable-check-failure-limit', type=click.BOOL, help=u"""Indicates whether the expression check, against the checkFilePathList, will fail the request if the count of UNMATCHED files is above the checkFailureLimit.""")
@cli_util.option('--check-failure-limit', type=click.INT, help=u"""The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if checkFilePathList is provided - but if isEnableCheckFailureLimit is set to true it is required.""")
@cli_util.option('--properties', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A map of maps that contains the properties which are specific to the pattern type. Each pattern type definition defines it's set of required and optional properties. Example: `{\"properties\": { \"default\": { \"tbd\"}}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'check-file-path-list': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'check-file-path-list': {'module': 'data_catalog', 'class': 'list[string]'}, 'properties': {'module': 'data_catalog', 'class': 'dict(str, dict(str, string))'}}, output_type={'module': 'data_catalog', 'class': 'Pattern'})
@cli_util.wrap_exceptions
def update_pattern(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, pattern_key, display_name, description, expression, check_file_path_list, is_enable_check_failure_limit, check_failure_limit, properties, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(pattern_key, six.string_types) and len(pattern_key.strip()) == 0:
        raise click.UsageError('Parameter --pattern-key cannot be whitespace or empty string')
    if not force:
        if check_file_path_list or properties:
            if not click.confirm("WARNING: Updates to check-file-path-list and properties will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if expression is not None:
        _details['expression'] = expression

    if check_file_path_list is not None:
        _details['checkFilePathList'] = cli_util.parse_json_parameter("check_file_path_list", check_file_path_list)

    if is_enable_check_failure_limit is not None:
        _details['isEnableCheckFailureLimit'] = is_enable_check_failure_limit

    if check_failure_limit is not None:
        _details['checkFailureLimit'] = check_failure_limit

    if properties is not None:
        _details['properties'] = cli_util.parse_json_parameter("properties", properties)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_pattern(
        catalog_id=catalog_id,
        pattern_key=pattern_key,
        update_pattern_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_pattern') and callable(getattr(client, 'get_pattern')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_pattern(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@term_group.command(name=cli_util.override('data_catalog.update_term.command_name', 'update'), help=u"""Updates a specific glossary term. \n[Command Reference](updateTerm)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Does not have to be unique, and it's changeable. Avoid entering confidential information.""")
@cli_util.option('--description', help=u"""Detailed description of the term.""")
@cli_util.option('--parent-term-key', help=u"""This terms parent term key. Will be null if the term has no parent term.""")
@cli_util.option('--owner', help=u"""OCID of the user who is the owner of this business terminology.""")
@cli_util.option('--workflow-status', type=custom_types.CliCaseInsensitiveChoice(["NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"]), help=u"""Status of the approval process workflow for this business term in the glossary""")
@cli_util.option('--custom-property-members', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of customized properties along with the values for this object

This option is a JSON list with items of type CustomPropertySetUsage.  For documentation on CustomPropertySetUsage please see our API reference: https://docs.cloud.oracle.com/api/#/en/datacatalog/20190325/datatypes/CustomPropertySetUsage.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'custom-property-members': {'module': 'data_catalog', 'class': 'list[CustomPropertySetUsage]'}}, output_type={'module': 'data_catalog', 'class': 'Term'})
@cli_util.wrap_exceptions
def update_term(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, glossary_key, term_key, display_name, description, parent_term_key, owner, workflow_status, custom_property_members, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')
    if not force:
        if custom_property_members:
            if not click.confirm("WARNING: Updates to custom-property-members will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    if parent_term_key is not None:
        _details['parentTermKey'] = parent_term_key

    if owner is not None:
        _details['owner'] = owner

    if workflow_status is not None:
        _details['workflowStatus'] = workflow_status

    if custom_property_members is not None:
        _details['customPropertyMembers'] = cli_util.parse_json_parameter("custom_property_members", custom_property_members)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_term(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        term_key=term_key,
        update_term_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_term') and callable(getattr(client, 'get_term')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_term(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@term_relationship_group.command(name=cli_util.override('data_catalog.update_term_relationship.command_name', 'update'), help=u"""Updates a specific glossary term relationship. \n[Command Reference](updateTermRelationship)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--glossary-key', required=True, help=u"""Unique glossary key.""")
@cli_util.option('--term-key', required=True, help=u"""Unique glossary term key.""")
@cli_util.option('--term-relationship-key', required=True, help=u"""Unique glossary term relationship key.""")
@cli_util.option('--display-name', help=u"""A user-friendly display name. Is changeable. The combination of 'displayName' and 'parentTermKey' must be unique. Avoid entering confidential information. This is the same as 'relationshipType' for 'termRelationship'.""")
@cli_util.option('--description', help=u"""Detailed description of the term relationship usually defined at the time of creation.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'data_catalog', 'class': 'TermRelationship'})
@cli_util.wrap_exceptions
def update_term_relationship(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, glossary_key, term_key, term_relationship_key, display_name, description, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(glossary_key, six.string_types) and len(glossary_key.strip()) == 0:
        raise click.UsageError('Parameter --glossary-key cannot be whitespace or empty string')

    if isinstance(term_key, six.string_types) and len(term_key.strip()) == 0:
        raise click.UsageError('Parameter --term-key cannot be whitespace or empty string')

    if isinstance(term_relationship_key, six.string_types) and len(term_relationship_key.strip()) == 0:
        raise click.UsageError('Parameter --term-relationship-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if description is not None:
        _details['description'] = description

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.update_term_relationship(
        catalog_id=catalog_id,
        glossary_key=glossary_key,
        term_key=term_key,
        term_relationship_key=term_relationship_key,
        update_term_relationship_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_term_relationship') and callable(getattr(client, 'get_term_relationship')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_term_relationship(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@connection_group.command(name=cli_util.override('data_catalog.upload_credentials.command_name', 'upload-credentials'), help=u"""Upload connection credentails and metadata for this connection. \n[Command Reference](uploadCredentials)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-key', required=True, help=u"""Unique connection key.""")
@cli_util.option('--credential-payload', required=True, help=u"""Information used in updating connection credentials.""")
@cli_util.option('--connection-detail', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource to see if it has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'connection-detail': {'module': 'data_catalog', 'class': 'UpdateConnectionDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-detail': {'module': 'data_catalog', 'class': 'UpdateConnectionDetails'}}, output_type={'module': 'data_catalog', 'class': 'Connection'})
@cli_util.wrap_exceptions
def upload_credentials(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, catalog_id, data_asset_key, connection_key, credential_payload, connection_detail, if_match):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    if isinstance(connection_key, six.string_types) and len(connection_key.strip()) == 0:
        raise click.UsageError('Parameter --connection-key cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['credentialPayload'] = credential_payload

    if connection_detail is not None:
        _details['connectionDetail'] = cli_util.parse_json_parameter("connection_detail", connection_detail)

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.upload_credentials(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        connection_key=connection_key,
        upload_credentials_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_connection') and callable(getattr(client, 'get_connection')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_connection(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
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


@catalog_group.command(name=cli_util.override('data_catalog.users.command_name', 'users'), help=u"""Returns active users in the system. \n[Command Reference](users)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "DISPLAYNAME"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is ascending. If no value is specified TIMECREATED is default.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'asc' or 'desc'.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""The page token representing the page at which to start retrieving results. This is usually retrieved from a previous list call.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def users(ctx, from_json, catalog_id, sort_by, sort_order, limit, page):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    kwargs = {}
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.users(
        catalog_id=catalog_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@data_asset_group.command(name=cli_util.override('data_catalog.validate_connection.command_name', 'validate-connection'), help=u"""Validate connection by connecting to the data asset using credentials in metadata. \n[Command Reference](validateConnection)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--data-asset-key', required=True, help=u"""Unique data asset key.""")
@cli_util.option('--connection-detail', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--connection-payload', help=u"""The information used to validate the connection.""")
@json_skeleton_utils.get_cli_json_input_option({'connection-detail': {'module': 'data_catalog', 'class': 'CreateConnectionDetails'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'connection-detail': {'module': 'data_catalog', 'class': 'CreateConnectionDetails'}}, output_type={'module': 'data_catalog', 'class': 'ValidateConnectionResult'})
@cli_util.wrap_exceptions
def validate_connection(ctx, from_json, catalog_id, data_asset_key, connection_detail, connection_payload):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(data_asset_key, six.string_types) and len(data_asset_key.strip()) == 0:
        raise click.UsageError('Parameter --data-asset-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if connection_detail is not None:
        _details['connectionDetail'] = cli_util.parse_json_parameter("connection_detail", connection_detail)

    if connection_payload is not None:
        _details['connectionPayload'] = connection_payload

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.validate_connection(
        catalog_id=catalog_id,
        data_asset_key=data_asset_key,
        validate_connection_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@pattern_group.command(name=cli_util.override('data_catalog.validate_pattern.command_name', 'validate'), help=u"""Validate pattern by deriving file groups representing logical entities using the expression \n[Command Reference](validatePattern)""")
@cli_util.option('--catalog-id', required=True, help=u"""Unique catalog identifier.""")
@cli_util.option('--pattern-key', required=True, help=u"""Unique pattern key.""")
@cli_util.option('--expression', help=u"""The expression used in the pattern that may include qualifiers. Refer to the user documentation for details of the format and examples.""")
@cli_util.option('--check-file-path-list', type=custom_types.CLI_COMPLEX_TYPE, help=u"""List of file paths against which the expression can be tried, as a check. This documents, for reference purposes, some example objects a pattern is meant to work with.

If provided with the request,this overrides the list which already exists as part of the pattern, if any.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--check-failure-limit', type=click.INT, help=u"""The maximum number of UNMATCHED files, in checkFilePathList, above which the check fails. Optional, if checkFilePathList is provided.

If provided with the request, this overrides the value which already exists as part of the pattern, if any.""")
@json_skeleton_utils.get_cli_json_input_option({'check-file-path-list': {'module': 'data_catalog', 'class': 'list[string]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'check-file-path-list': {'module': 'data_catalog', 'class': 'list[string]'}}, output_type={'module': 'data_catalog', 'class': 'ValidatePatternResult'})
@cli_util.wrap_exceptions
def validate_pattern(ctx, from_json, catalog_id, pattern_key, expression, check_file_path_list, check_failure_limit):

    if isinstance(catalog_id, six.string_types) and len(catalog_id.strip()) == 0:
        raise click.UsageError('Parameter --catalog-id cannot be whitespace or empty string')

    if isinstance(pattern_key, six.string_types) and len(pattern_key.strip()) == 0:
        raise click.UsageError('Parameter --pattern-key cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if expression is not None:
        _details['expression'] = expression

    if check_file_path_list is not None:
        _details['checkFilePathList'] = cli_util.parse_json_parameter("check_file_path_list", check_file_path_list)

    if check_failure_limit is not None:
        _details['checkFailureLimit'] = check_failure_limit

    client = cli_util.build_client('data_catalog', 'data_catalog', ctx)
    result = client.validate_pattern(
        catalog_id=catalog_id,
        pattern_key=pattern_key,
        validate_pattern_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)
