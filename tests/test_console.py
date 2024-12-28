# tests/test_console.py
import click.testing
import pytest
import requests
from unittest.mock import MagicMock

from yhmt import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_main_succeeds(runner, mock_requests_get):
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0

@pytest.fixture
def mock_requests_get(mocker):
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock

def test_main_failure(runner, mock_requests_fail):
    with pytest.raises(click.exceptions.ClickException) as excinfo:
        runner = click.testing.CliRunner()
        result = runner.invoke(console.main)
    assert str(excinfo.value) == "Mock fail"

@pytest.fixture
def mock_requests_fail_old(mocker):
    mock = mocker.patch("requests.get", side_effect=requests.RequestException("Mock fail"))
    return mock

@pytest.fixture
def mock_requests_fail(mocker):
    mock_response = MagicMock()  # Create a mock response object
    mock_response.__enter__.side_effect = requests.RequestException("Mock fail") # Raise the exception when the context manager is entered
    mock_get = mocker.patch("requests.get")
    mock_get.return_value = mock_response
    return mock_get
