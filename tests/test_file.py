

"""
Test support for logging to file functions.

99% tested by default configuration
"""

from os import makedirs
from pathlib import Path

import pytest

from simple_logging_config import configure_logging


@pytest.fixture(scope="function", autouse=True)
def configure():
    """
    Ensure logging is reset after each test.
    """
    yield
    configure_logging().reset()


class TestLogFileSettings:
    """
    Class to test log to file functions
    """

    def test_log_file_path_as_filename(self):
        """
        Test log file path can be set as a file name
        """
        log_file_path_as_filename = "test_as_filename.log"
        configure_logging(log_file_path=log_file_path_as_filename)
        assert Path(log_file_path_as_filename).is_file()

    def test_log_file_path_as_path(self):
        """
        Test log file path can be set as a folder
        """
        log_file_path_as_path = "logs_folder"
        makedirs(Path(log_file_path_as_path), exist_ok=True)
        configure_logging(log_file_path=log_file_path_as_path)
        assert Path(log_file_path_as_path).is_dir()
