import docker
import pytest
from docker.client import DockerClient
from python_on_whales import Builder
from python_on_whales import DockerClient as PowDockerClient


@pytest.fixture(scope="session")
def docker_client() -> DockerClient:
    return docker.from_env()


@pytest.fixture(scope="session")
def pow_docker_client() -> PowDockerClient:
    return PowDockerClient()


@pytest.fixture(scope="session")
def pow_buildx_builder(pow_docker_client: PowDockerClient) -> Builder:
    builder: Builder = pow_docker_client.buildx.create(
        driver="docker-container", driver_options=dict(network="host")
    )
    yield builder
    pow_docker_client.buildx.stop(builder)
    pow_docker_client.buildx.remove(builder)
