"""
Test support for logging to file functions.

99% tested by default configuration
"""

# Line 31 untested

import logging

# import pytest

from simple_logging_config import configure_logging


logger = logging.getLogger(__name__)


class TestLogFileSettings:
    """
    Class to test default config .
    """

    def test_log_file_path(self):
        """
        Test first line of str() returns correct string
        """
        log_file_path = "test.log"
        slc = configure_logging(log_file_path=log_file_path)
        logging.getLogger(__name__).debug(slc.log_file_path)
        assert slc.log_file_path == log_file_path
