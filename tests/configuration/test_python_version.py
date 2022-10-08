from time import sleep
from uuid import uuid4

import pytest
from docker.models.containers import Container

from build.constants import (
    PYTHON_VERSIONS,
)
from tests.constants import SLEEP_TIME
from tests.utils import ImageTagComponents


@pytest.mark.parametrize(
    "cleaned_up_test_container", [str(uuid4())], indirect=True
)
def test_python_version(
    docker_client,
    python_poetry_image,
    cleaned_up_test_container,
) -> None:
    image_tag_components: ImageTagComponents = (
        ImageTagComponents.create_from_tag(python_poetry_image)
    )

    test_container: Container = docker_client.containers.run(
        python_poetry_image,
        name=cleaned_up_test_container,
        detach=True,
        tty=True,
    )
    sleep(SLEEP_TIME)

    (exit_code, output) = test_container.exec_run(["python", "--version"])
    assert exit_code == 0

    version_string: str = (
        f"Python {PYTHON_VERSIONS[image_tag_components.target_architecture]}"
    )
    assert version_string in output.decode("utf-8")
