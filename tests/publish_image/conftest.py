import pytest
from click.testing import CliRunner
from python_on_whales import DockerClient, Image


@pytest.fixture(scope="package")
def cli_runner() -> CliRunner:
    runner = CliRunner()
    return runner


@pytest.fixture(scope="package")
def cleanup_images(docker_client: DockerClient):
    yield
    images: list[Image] = docker_client.image.list("pfeiffermax/python-poetry")
    docker_client.image.remove(images)
