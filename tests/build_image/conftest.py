import pytest
from docker.client import DockerClient
from docker.models.images import Image

from build.constants import TARGET_ARCHITECTURES
from build.images import PythonPoetryImage
from tests.registry_container import DockerRegistryContainer
from python_on_whales import Builder
from python_on_whales import DockerClient as PowDockerClient
from tests.constants import VERSION, CONTEXT, BAKE_FILE, SLEEP_TIME
from tests.utils import extract_image_tags_from_build_config
from docker.models.containers import Container
from time import sleep
from slugify import slugify


@pytest.fixture(scope="package")
def registry_container() -> DockerRegistryContainer:
    registry_container = DockerRegistryContainer().with_bind_ports(5000, 5000)
    registry_container.start()
    yield registry_container
    registry_container.stop()


@pytest.fixture(scope="package")
def images(
    pow_docker_client: PowDockerClient,
    pow_buildx_builder: Builder,
    registry_container: DockerRegistryContainer,
):
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


# @pytest.fixture(scope="package", params=TARGET_ARCHITECTURES)
# def python_poetry_image(
#     docker_client: DockerClient, version: str, request
# ) -> str:
#     target_architecture: str = request.param

#     python_poetry_image: Image = PythonPoetryImage(
#         docker_client, target_architecture, version
#     ).build()
#     image_tag: str = python_poetry_image.tags[0]
#     yield image_tag
#     docker_client.images.remove(image_tag, force=True)


# @pytest.fixture(scope="function")
# def cleaned_up_test_container(docker_client: DockerClient, request) -> None:
#     test_container_name: str = request.param
#     yield test_container_name
#     test_container = docker_client.containers.get(test_container_name)
#     test_container.stop()
#     test_container.remove()
