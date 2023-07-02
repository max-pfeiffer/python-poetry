from time import sleep

import pytest
from docker.client import DockerClient
from docker.models.containers import Container
from python_on_whales import Builder
from python_on_whales import DockerClient as PowDockerClient
from slugify import slugify

from build.utils import extract_image_tags_from_build_config
from tests.constants import (
    BAKE_FILE,
    CONTEXT,
    REGISTRY_PASSWORD,
    REGISTRY_USERNAME,
    SLEEP_TIME,
    VERSION,
)
from tests.registry_container import DockerRegistryContainer


@pytest.fixture(scope="package")
def registry_container() -> DockerRegistryContainer:
    registry_container = DockerRegistryContainer(
        username=REGISTRY_USERNAME, password=REGISTRY_PASSWORD
    ).with_bind_ports(5000, 5000)
    registry_container.start()
    yield registry_container
    registry_container.stop()


@pytest.fixture(scope="package")
def images(
    pow_docker_client: PowDockerClient,
    pow_buildx_builder: Builder,
    registry_container: DockerRegistryContainer,
):
    pow_docker_client.login(
        server=registry_container.get_registry(),
        username=REGISTRY_USERNAME,
        password=REGISTRY_PASSWORD,
    )
    build_config: dict = pow_docker_client.buildx.bake(
        targets=["python-poetry"],
        builder=pow_buildx_builder,
        files=[BAKE_FILE],
        variables=dict(
            REGISTRY=registry_container.get_registry(),
            CONTEXT=CONTEXT,
            IMAGE_VERSION=VERSION,
        ),
        push=True,
    )
    image_tags: list[str] = extract_image_tags_from_build_config(build_config)
    yield image_tags


@pytest.fixture(scope="function")
def test_container(docker_client: DockerClient, request):
    image_tag: str = request.param
    image_name: str = slugify(image_tag)
    test_container: Container = docker_client.containers.run(
        image_tag,
        name=image_name,
        detach=True,
        tty=True,
    )
    sleep(SLEEP_TIME)
    yield test_container
    test_container.stop()
    test_container.remove()
