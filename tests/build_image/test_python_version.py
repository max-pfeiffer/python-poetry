"""Tests for Python version."""

from python_on_whales import Container, DockerClient

from tests.utils import ImageTagComponents


def test_python_version(
    docker_client: DockerClient,
    image_reference: str,
) -> None:
    """Tests the Python version.

    :param docker_client:
    :param image_reference:
    :return:
    """
    container: Container
    with docker_client.container.run(
        image_reference, detach=True, interactive=True, tty=True
    ) as container:
        output = container.execute(["python", "--version"])
        image_tag_components: ImageTagComponents = (
            ImageTagComponents.create_from_reference(image_reference)
        )
        assert image_tag_components.python_version in output
