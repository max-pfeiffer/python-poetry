import pytest
from docker.client import DockerClient
from docker.models.images import Image

from build.constants import TARGET_ARCHITECTURES
from build.images import PythonPoetryImage


@pytest.fixture(scope="session", params=TARGET_ARCHITECTURES)
def python_poetry_image(
    docker_client: DockerClient, version: str, request
) -> str:
    target_architecture: str = request.param

    python_poetry_image: Image = PythonPoetryImage(
        docker_client, target_architecture, version
    ).build()
    image_tag: str = python_poetry_image.tags[0]
    yield image_tag
    docker_client.images.remove(image_tag, force=True)


@pytest.fixture(scope="function")
def cleaned_up_test_container(docker_client: DockerClient, request) -> None:
    test_container_name: str = request.param
    yield test_container_name
    test_container = docker_client.containers.get(test_container_name)
    test_container.stop()
    test_container.remove()
