"""Tests for invalid CLI calls."""

from click.testing import CliRunner, Result

from build.publish import main


def test_missing_options_and_env(cli_runner: CliRunner):
    """Test for building and publishing an image with an invalid CLI configuration.

    :param cli_runner:
    :return:
    """
    result: Result = cli_runner.invoke(main)
    assert result.exit_code == 2
