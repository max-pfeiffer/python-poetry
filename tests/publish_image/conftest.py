import pytest
from click.testing import CliRunner
from os import getenv


@pytest.fixture(scope="package")
def cli_runner() -> CliRunner:
    runner = CliRunner()
    return runner


@pytest.fixture(scope="package")
def python_version() -> str:
    python_version: str = getenv("PYTHON_VERSION")
    return python_version


@pytest.fixture(scope="package")
def os_variant() -> str:
    os_variant: str = getenv("OS_VARIANT")
    return os_variant


@pytest.fixture(scope="package")
def poetry_version() -> str:
    poetry_version: str = getenv("POETRY_VERSION")
    return poetry_version
