"""Tests for building and publishing the image using CLI and environment variables."""

from build.publish import main
from click.testing import CliRunner, Result
from python_on_whales import DockerException
from testcontainers.registry import DockerRegistryContainer

from tests.constants import REGISTRY_PASSWORD, REGISTRY_USERNAME


def test_registry_with_credentials(
    image_version: str,
    publish_registry_container: DockerRegistryContainer,
    cli_runner: CliRunner,
    python_version: str,
    os_variant: str,
    poetry_version: str,
):
    """Test building and publishing the image to a Docker registry.

    The registry requires authentication. It requires authentication for this case.

    :param image_version:
    :param cli_runner:
    :param python_version:
    :param os_variant:
    :param poetry_version:
    :return:
    """
    result: Result = cli_runner.invoke(
        main,
        env={
            "DOCKER_HUB_USERNAME": REGISTRY_USERNAME,
            "DOCKER_HUB_TOKEN": REGISTRY_PASSWORD,
            "GIT_TAG_NAME": image_version,
            "PYTHON_VERSION": python_version,
            "OS_VARIANT": os_variant,
            "POETRY_VERSION": poetry_version,
            "REGISTRY": publish_registry_container.get_registry(),
        },
    )
    assert result.exit_code == 0


def test_registry_with_wrong_credentials(
    image_version: str,
    publish_registry_container: DockerRegistryContainer,
    cli_runner: CliRunner,
    python_version: str,
    os_variant: str,
    poetry_version: str,
):
    """Test building and publishing the image to a Docker registry.

    The registry requires authentication. The credentials are invalid in this case.

    :param image_version:
    :param cli_runner:
    :param python_version:
    :param os_variant:
    :param poetry_version:
    :return:
    """
    result: Result = cli_runner.invoke(
        main,
        env={
            "DOCKER_HUB_USERNAME": "boom",
            "DOCKER_HUB_TOKEN": "bang",
            "GIT_TAG_NAME": image_version,
            "PYTHON_VERSION": python_version,
            "OS_VARIANT": os_variant,
            "POETRY_VERSION": poetry_version,
            "REGISTRY": publish_registry_container.get_registry(),
        },
    )
    assert result.exit_code == 1
    assert isinstance(result.exception, DockerException)
