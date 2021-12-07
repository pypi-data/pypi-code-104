from contextlib import contextmanager
from typing import Dict, Generator, Tuple
from urllib.parse import urlparse

import click
from requests import PreparedRequest, RequestException

from . import utils
from .docker_utils import convert_host_abs_path_to_container, is_docker
from .logger import get_logger
from .utils import is_connection_healthy

LOCALHOST_PREFIX = "localhost"
DOCKER_HOST_PREFIX = "host.docker"

log = get_logger(__name__)


def validate_target_url(
    ctx: click.core.Context, param: click.core.Parameter, raw_value: str
) -> str:
    if not raw_value:
        raise click.BadParameter("Target URL cannot be empty.")
    if is_docker() and raw_value.lower().startswith(LOCALHOST_PREFIX):
        raise click.BadArgumentUsage(
            "Target URL cannot be localhost when running in Docker. Please use host.docker.internal instead."
        )
    if not is_docker() and DOCKER_HOST_PREFIX in raw_value.lower():
        click.secho(
            "You are running the CLI outside Docker but the target URL is a Docker host. Please double check.",
            fg="yellow",
        )

    # Before we parse the URL, prefix the URL with http:// if it's a localhost or host.docker.internal
    target_url = (
        f"http://{raw_value}"
        if raw_value.lower().startswith(LOCALHOST_PREFIX)
        or raw_value.lower().startswith(DOCKER_HOST_PREFIX)
        else raw_value
    )
    try:
        result = urlparse(target_url)
        log.debug(f"Parsed URL: {result}")
        if not result.scheme or not result.netloc:
            raise click.BadParameter("Target URL should have a scheme and host.")
    except ValueError as exc:
        raise click.BadParameter(
            "Please provide a valid URL (e.g. https://api.example.com)"
        ) from exc

    if not is_connection_healthy(target_url):
        raise click.BadArgumentUsage("Cannot reach target URL: {}".format(raw_value))
    return target_url


def validate_schema(
    ctx: click.core.Context, param: click.core.Parameter, raw_value: str
) -> str:
    if "app" not in ctx.params:
        try:
            netloc = urlparse(raw_value).netloc
        except ValueError as exc:
            raise click.UsageError(
                "Invalid schema, must be a valid URL or file path."
            ) from exc
        if not netloc:
            mapped_file = _check_and_map_schema_file(raw_value)
            if not mapped_file:
                raise click.UsageError(_get_env_specific_schema_file_usage_error())
                # Click ends execution here
            return mapped_file
        else:
            _validate_url(raw_value)
    return raw_value


def _check_and_map_schema_file(filename: str) -> str:
    """Check if the schema file exists accounting for Docker volume mounts.
    Returns mapped schema file on success, AND empty string on error
    """
    if "\x00" in filename:
        return ""

    mapped_filename = convert_host_abs_path_to_container(filename)
    if not mapped_filename or not utils.file_exists(mapped_filename):
        return ""

    return mapped_filename


def _validate_url(value: str) -> None:
    try:
        PreparedRequest().prepare_url(value, {})  # type: ignore
    except RequestException as exc:
        raise click.UsageError(
            "Invalid schema, must be a valid URL or file path."
        ) from exc


def _get_env_specific_schema_file_usage_error() -> str:
    """Return an appropriate message based on the env - Docker or no Docker"""
    if is_docker():
        return "Invalid path for schema file. Please provide the absolute path on the Docker host."
    else:
        return "Invalid path for schema file."


@contextmanager
def reraise_format_error(raw_value: str) -> Generator[None, None, None]:
    try:
        yield
    except ValueError as exc:
        raise click.BadParameter(
            f"Should be in KEY:VALUE format. Got: {raw_value}"
        ) from exc


def validate_headers(
    ctx: click.core.Context, param: click.core.Parameter, raw_value: Tuple[str, ...]
) -> Dict[str, str]:
    headers = {}
    for header in raw_value:
        with reraise_format_error(header):
            key, value = header.split(":", maxsplit=1)
        value = value.lstrip()
        key = key.strip()
        if not key:
            raise click.BadParameter("Header name should not be empty")
        if not utils.is_latin_1_encodable(key):
            raise click.BadParameter("Header name should be latin-1 encodable")
        if not utils.is_latin_1_encodable(value):
            raise click.BadParameter("Header value should be latin-1 encodable")
        if utils.has_invalid_characters(key, value):
            raise click.BadParameter(
                "Invalid return character or leading space in header"
            )
        headers[key] = value
    return headers
