"""Basic test fixtures."""

from random import randrange

import pytest
from python_on_whales import Builder, DockerClient
from semver import VersionInfo


@pytest.fixture(scope="session")
def docker_client() -> DockerClient:
    """Provide the Python on Whales docker client.

    :return:
    """
    return DockerClient(debug=True)


@pytest.fixture(scope="session")
def pow_buildx_builder(docker_client: DockerClient) -> Builder:
    """Provide a Pyhton on Whales BuildX builder instance.

    :param docker_client:
    :return:
    """
    builder: Builder = docker_client.buildx.create(
        driver="docker-container", driver_options=dict(network="host")
    )
    yield builder
    docker_client.buildx.stop(builder)
    docker_client.buildx.remove(builder)


@pytest.fixture(scope="session")
def image_version() -> str:
    """Generate a image version.

    :return:
    """
    image_version: str = str(
        VersionInfo(major=randrange(100), minor=randrange(100), patch=randrange(100))
    )
    return image_version
