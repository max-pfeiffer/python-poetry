from random import randrange

import docker
import pytest
from docker.models.images import Image
from semver import VersionInfo

from build.constants import (
    TARGET_ARCHITECTURES,
)
from build.images import PythonPoetryImage
from tests.utils import ImageTagComponents


@pytest.fixture(scope="session")
def docker_client() -> docker.client:
    return docker.client.from_env()


@pytest.fixture(scope="session")
def version() -> str:
    version: VersionInfo = VersionInfo(
        major=randrange(100), minor=randrange(100), patch=randrange(100)
    )
    version_string: str = str(version)
    return version_string


@pytest.fixture(scope="session", params=TARGET_ARCHITECTURES)
def python_poetry_image(docker_client, version, request) -> str:
    target_architecture: str = request.param

    python_poetry_image: Image = PythonPoetryImage(docker_client).build(
        target_architecture, version=version
    )
    image_tag: str = python_poetry_image.tags[0]
    yield image_tag
    docker_client.images.remove(image_tag, force=True)


@pytest.fixture(scope="function")
def cleaned_up_test_container(docker_client, request) -> None:
    test_container_name: str = request.param
    yield test_container_name
    test_container = docker_client.containers.get(test_container_name)
    test_container.stop()
    test_container.remove()
