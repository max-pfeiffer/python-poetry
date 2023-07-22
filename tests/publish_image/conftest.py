import pytest
from click.testing import CliRunner
from python_on_whales import DockerClient, Image


@pytest.fixture(scope="package")
def cli_runner() -> CliRunner:
    runner = CliRunner()
    return runner
