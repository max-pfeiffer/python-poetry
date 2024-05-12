"""Test fixtures for image build tests."""

from os import getenv
from time import sleep

import pytest
from python_on_whales import Builder, DockerClient
from testcontainers.registry import DockerRegistryContainer

from build.constants import PLATFORMS
from build.utils import get_image_reference
from tests.constants import CONTEXT, REGISTRY_PASSWORD, REGISTRY_USERNAME


@pytest.fixture(scope="package")
def registry_container() -> DockerRegistryContainer:
    """Provide a Registry container locally for publishing the image.

    :return:
    """
    registry_container = DockerRegistryContainer(
        username=REGISTRY_USERNAME, password=REGISTRY_PASSWORD
    ).with_bind_ports(5000, 5000)
    registry_container.start()

    # Wait for the registry container to come up
    sleep(3.0)

    yield registry_container
    registry_container.stop()


@pytest.fixture(scope="package")
def image_reference(
    docker_client: DockerClient,
    pow_buildx_builder: Builder,
    image_version: str,
    registry_container: DockerRegistryContainer,
) -> str:
    """Build the image and return the image reference.

    :param docker_client:
    :param pow_buildx_builder:
    :param image_version:
    :param registry_container:
    :return:
    """
    docker_client.login(
        server=registry_container.get_registry(),
        username=REGISTRY_USERNAME,
        password=REGISTRY_PASSWORD,
    )
    registry: str = registry_container.get_registry()
    python_version: str = getenv("PYTHON_VERSION")
    os_variant: str = getenv("OS_VARIANT")
    poetry_version: str = getenv("POETRY_VERSION")
    github_ref_name: str = getenv("GITHUB_REF_NAME")

    image_reference: str = get_image_reference(
        registry, image_version, poetry_version, python_version, os_variant
    )
    cache_scope: str = f"{poetry_version}-{python_version}-{os_variant}"

    if github_ref_name:
        cache_to: str = f"type=gha,mode=max,scope={github_ref_name}-{cache_scope}"
        cache_from: str = f"type=gha,scope={github_ref_name}-{cache_scope}"
    else:
        cache_to = f"type=local,mode=max,dest=/tmp,scope={cache_scope}"
        cache_from = f"type=local,src=/tmp,scope={cache_scope}"

    docker_client.buildx.build(
        context_path=CONTEXT,
        target="production-image",
        build_args={
            "POETRY_VERSION": poetry_version,
            "OFFICIAL_PYTHON_IMAGE": f"python:{python_version}-{os_variant}",
        },
        tags=image_reference,
        platforms=PLATFORMS,
        builder=pow_buildx_builder,
        cache_to=cache_to,
        cache_from=cache_from,
        push=True,
    )
    yield image_reference
