import pytest
from python_on_whales import Container, DockerClient

from tests.constants import IMAGE_REFERENCES
from tests.utils import ImageTagComponents


@pytest.mark.parametrize("image_reference", IMAGE_REFERENCES)
@pytest.mark.usefixtures("images")
def test_python_version(
    docker_client: DockerClient,
    image_reference: str,
) -> None:
    container: Container
    with docker_client.container.run(
        image_reference, detach=True, interactive=True, tty=True
    ) as container:
        output = container.execute(["python", "--version"])
        image_tag_components: ImageTagComponents = (
            ImageTagComponents.create_from_reference(image_reference)
        )
        assert image_tag_components.python_version in output
