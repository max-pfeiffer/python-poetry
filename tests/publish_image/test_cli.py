"""Tests for building and publishing the image using CLI and command line arguments."""

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
        args=[
            "--docker-hub-username",
            REGISTRY_USERNAME,
            "--docker-hub-token",
            REGISTRY_PASSWORD,
            "--version-tag",
            image_version,
            "--python-version",
            python_version,
            "--os-variant",
            os_variant,
            "--poetry-version",
            poetry_version,
            "--registry",
            publish_registry_container.get_registry(),
        ],
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
        args=[
            "--docker-hub-username",
            "bang",
            "--docker-hub-token",
            "boom",
            "--version-tag",
            image_version,
            "--python-version",
            python_version,
            "--os-variant",
            os_variant,
            "--poetry-version",
            poetry_version,
            "--registry",
            publish_registry_container.get_registry(),
        ],
    )
    assert result.exit_code == 1
    assert isinstance(result.exception, DockerException)
