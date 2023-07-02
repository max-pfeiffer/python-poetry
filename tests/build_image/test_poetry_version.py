import pytest
from docker.models.containers import Container

from build.constants import POETRY_VERSIONS
from tests.constants import IMAGE_TAGS
from tests.utils import ImageTagComponents


@pytest.mark.parametrize("test_container", IMAGE_TAGS, indirect=True)
@pytest.mark.usefixtures("images")
def test_poetry_configuration(test_container: Container) -> None:
    image_tag_components: ImageTagComponents = (
        ImageTagComponents.create_from_tag(test_container.image.tags[0])
    )

    (exit_code, output) = test_container.exec_run(["poetry", "--version"])
    assert exit_code == 0

    assert image_tag_components.poetry_version in output.decode("utf-8")
