import pytest
from python_on_whales import DockerClient, Builder


@pytest.fixture(scope="session")
def docker_client() -> DockerClient:
    return DockerClient()


@pytest.fixture(scope="session")
def pow_buildx_builder(docker_client: DockerClient) -> Builder:
    builder: Builder = docker_client.buildx.create(
        driver="docker-container", driver_options=dict(network="host")
    )
    yield builder
    docker_client.buildx.stop(builder)
    docker_client.buildx.remove(builder)
