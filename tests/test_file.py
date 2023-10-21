"""
Test support for logging to file functions.

99% tested by default configuration
"""

from pathlib import Path

from simple_logging_config import configure_logging


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
