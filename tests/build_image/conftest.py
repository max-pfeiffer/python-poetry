import pytest
from python_on_whales import Builder, DockerClient

from tests.constants import (
    BAKE_FILE,
    CONTEXT,
    REGISTRY_PASSWORD,
    REGISTRY_USERNAME,
    VERSION,
)
from tests.registry_container import DockerRegistryContainer
from tests.utils import extract_image_references_from_build_config


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
    docker_client: DockerClient,
    pow_buildx_builder: Builder,
    registry_container: DockerRegistryContainer,
):
    docker_client.login(
        server=registry_container.get_registry(),
        username=REGISTRY_USERNAME,
        password=REGISTRY_PASSWORD,
    )
    build_config: dict = docker_client.buildx.bake(
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
    image_references: list[str] = extract_image_references_from_build_config(
        build_config
    )
    yield image_references
