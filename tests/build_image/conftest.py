from time import sleep
import pytest
from python_on_whales import Builder, DockerClient

from tests.constants import (
    CONTEXT,
    REGISTRY_PASSWORD,
    REGISTRY_USERNAME,
)
from tests.registry_container import DockerRegistryContainer
from os import getenv


@pytest.fixture(scope="package")
def registry_container() -> DockerRegistryContainer:
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
):
    docker_client.login(
        server=registry_container.get_registry(),
        username=REGISTRY_USERNAME,
        password=REGISTRY_PASSWORD,
    )
    registry: str = registry_container.get_registry()

    python_version: str = getenv("PYTHON_VERSION")
    os_variant: str = getenv("OS_VARIANT")
    poetry_version: str = getenv("POETRY_VERSION")

    tag: str = f"{registry}/pfeiffermax/python-poetry:{image_version}-poetry{poetry_version}-python{python_version}-{os_variant}"
    cache_scope: str = (
        f"{image_version}-{poetry_version}-{python_version}-{os_variant}"
    )

    platforms: list[str] = ["linux/amd64", "linux/arm64/v8"]
    cache_to: str = f"type=gha,mode=max,scope=$GITHUB_REF_NAME-{cache_scope}"
    cache_from: str = f"type=gha,scope=$GITHUB_REF_NAME-{cache_scope}"

    if getenv("USE_LOCAL_CACHE_STORAGE_BACKEND"):
        cache_to = f"type=local,mode=max,dest=/tmp,scope={cache_scope}"
        cache_from = f"type=local,src=/tmp,scope={cache_scope}"

    docker_client.buildx.build(
        context_path=CONTEXT,
        target="production-image",
        build_args={
            "POETRY_VERSION": poetry_version,
            "OFFICIAL_PYTHON_IMAGE": f"python:{python_version}-{os_variant}",
        },
        tags=tag,
        platforms=platforms,
        builder=pow_buildx_builder,
        cache_to=cache_to,
        cache_from=cache_from,
        push=True,
    )
    yield tag
