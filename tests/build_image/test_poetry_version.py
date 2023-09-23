from python_on_whales import Container, DockerClient

from tests.utils import ImageTagComponents


def test_poetry_configuration(
    docker_client: DockerClient, image_reference: str
) -> None:
    container: Container
    with docker_client.container.run(
        image_reference, detach=True, interactive=True, tty=True
    ) as container:
        output = container.execute(["poetry", "--version"])
        image_tag_components: ImageTagComponents = (
            ImageTagComponents.create_from_reference(image_reference)
        )
        assert image_tag_components.poetry_version in output
