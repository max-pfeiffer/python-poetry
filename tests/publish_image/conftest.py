"""Test fixtures for image publishing."""

from collections.abc import Generator
from os import getenv
from typing import Any

import pytest
from click.testing import CliRunner
from testcontainers.registry import DockerRegistryContainer

from tests.constants import REGISTRY_PASSWORD, REGISTRY_USERNAME


@pytest.fixture(scope="package")
def publish_registry_container() -> Generator[DockerRegistryContainer, Any, None]:
    """Provide a Registry container locally for publishing the image.

    :return:
    """
    with DockerRegistryContainer(
        username=REGISTRY_USERNAME, password=REGISTRY_PASSWORD
    ).with_bind_ports(5000, 5000) as registry_container:
        yield registry_container


@pytest.fixture(scope="package")
def cli_runner() -> CliRunner:
    """Provide CLI runner for testing click CLI.

    :return:
    """
    runner = CliRunner()
    return runner


@pytest.fixture(scope="package")
def python_version() -> str:
    """Python version provided via environment variable.

    :return:
    """
    python_version: str = getenv("PYTHON_VERSION")
    return python_version


@pytest.fixture(scope="package")
def os_variant() -> str:
    """OS variant provided via environment variable.

    :return:
    """
    os_variant: str = getenv("OS_VARIANT")
    return os_variant


@pytest.fixture(scope="package")
def poetry_version() -> str:
    """Poetry version provided via environment variable.

    :return:
    """
    poetry_version: str = getenv("POETRY_VERSION")
    return poetry_version
